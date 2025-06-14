package br.ufba.jnose.pages;

import br.ufba.jnose.WicketApplication;
import br.ufba.jnose.business.ProjetoBusiness;
import br.ufba.jnose.base.Util;
import br.ufba.jnose.dtolocal.ProjetoDTO;
import br.ufba.jnose.dtolocal.TotalProcessado;
import br.ufba.jnose.entities.Projeto;
import br.ufba.jnose.pages.base.BasePage;
import br.ufba.jnose.base.JNose;
import com.googlecode.wicket.jquery.ui.panel.JQueryFeedbackPanel;
import org.apache.wicket.AttributeModifier;
import org.apache.wicket.ajax.AbstractAjaxTimerBehavior;
import org.apache.wicket.ajax.AjaxRequestTarget;
import org.apache.wicket.ajax.markup.html.form.AjaxCheckBox;
import org.apache.wicket.extensions.ajax.markup.html.AjaxIndicatorAppender;
import org.apache.wicket.extensions.ajax.markup.html.IndicatingAjaxLink;
import org.apache.wicket.markup.html.WebMarkupContainer;
import org.apache.wicket.markup.html.basic.Label;
import org.apache.wicket.markup.html.link.Link;
import org.apache.wicket.markup.html.list.ListItem;
import org.apache.wicket.markup.html.list.ListView;
import org.apache.wicket.markup.html.panel.FeedbackPanel;
import org.apache.wicket.model.Model;
import org.apache.wicket.model.PropertyModel;
import org.apache.wicket.protocol.http.WebApplication;
import org.apache.wicket.spring.injection.annot.SpringBean;
import org.apache.wicket.util.time.Duration;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.io.*;

public class ByTestSmellsPage extends BasePage {
    private static final long serialVersionUID = 2L;

    private String pastaPath;
    private String pathAppToWebapp;
    private String pastaPathReport;
    private Label lbPastaSelecionada;
    private List<ProjetoDTO> listaProjetos;
    private AjaxIndicatorAppender indicator;
    private ListView<ProjetoDTO> lvProjetos;
    private TotalProcessado totalProcessado;
    private Map<Integer, Integer> totalProgressBar;
    private Boolean processando;
    private IndicatingAjaxLink processarTodos;
    private Label lbProjetosSize;
    private String dataProcessamentoAtual;
    private StringBuffer logRetorno;
    private List<List<String>> listaResultado;
    private Link lkResultadoBotton;

    @SpringBean
    private ProjetoBusiness projetoBusiness;

    public ByTestSmellsPage() {
        super("ByTestSmellsPage");

        //carregar variáveis
        listaResultado = new ArrayList<>();
        logRetorno = new StringBuffer();
        processando = false;
        indicator = new AjaxIndicatorAppender();
        pastaPath = "";
        pathAppToWebapp = WebApplication.get().getServletContext().getRealPath("");
        pastaPathReport = pathAppToWebapp + File.separatorChar + "reports" + File.separatorChar;
        totalProcessado = new TotalProcessado();
        totalProgressBar = new HashMap<>();
        listaProjetos = new ArrayList<>();

        lbProjetosSize = new Label("lbProjetosSize", Model.of("0"));
        lbProjetosSize.setOutputMarkupPlaceholderTag(true).setOutputMarkupId(true);
        add(lbProjetosSize);

        criarListaProjetos();

        criarTimer();

        FeedbackPanel feedback = new JQueryFeedbackPanel("feedback");
        add(feedback.setOutputMarkupId(true));

        criarBotaoProcessarTodos();

        lbPastaSelecionada = new Label("lbPastaSelecionada", pastaPath);
        add(lbPastaSelecionada);

        lkResultadoBotton = new Link<String>("lkResultado") {
            @Override
            public void onClick() {
                setResponsePage(new ResultPage(listaResultado,"Result By TestSmells", "result_bytestsmells",false));
            }
        };
        lkResultadoBotton.setEnabled(processando);
        lkResultadoBotton.setOutputMarkupId(true);
        lkResultadoBotton.setOutputMarkupPlaceholderTag(true);
        add(lkResultadoBotton);

        loadProjetos();
    }

    private void criarBotaoProcessarTodos(){
        processarTodos = new IndicatingAjaxLink<String>("processarTodos") {
            @Override
            public void onClick(AjaxRequestTarget target) {
                lbPastaSelecionada.setDefaultModel(Model.of(pastaPath));
                processando = true;
                List<ProjetoDTO> listaParaProcessar = new ArrayList<>();
                for (ProjetoDTO projeto : listaProjetos) {
                    if (projeto.getParaProcessar()) {
                        listaParaProcessar.add(projeto);
                    }
                }

                JNose.processarProjetos(listaParaProcessar, dataProcessamentoAtual, pastaPathReport, totalProcessado);

                for (ProjetoDTO projeto : listaProjetos) {
                    if (projeto.getResultado() != null) {
                        listaResultado.addAll(projeto.getResultado());
                    }
                }

            }
        };
        processarTodos.setEnabled(false);
        add(processarTodos);
    }

    private void criarListaProjetos(){
        lvProjetos = new ListView<ProjetoDTO>("lvProjetos", listaProjetos) {
            @Override
            protected void populateItem(ListItem<ProjetoDTO> item) {
                ProjetoDTO projeto = item.getModelObject();

                Link lkResultado = new Link<String>("lkResultado") {
                    @Override
                    public void onClick() {
                        setResponsePage(new ResultPage2(projeto, projeto.getResultado(),"Result By TestSmells: " + projeto.getName(), projeto.getName()+"_result_bytestsmells",false));
                    }
                };
                lkResultado.setEnabled(projeto.getProcessado());
                lkResultado.setOutputMarkupId(true);
                lkResultado.setOutputMarkupPlaceholderTag(true);
                item.add(lkResultado);
                projeto.setLkResultado(lkResultado);

                AjaxCheckBox paraProcessarACB = new AjaxCheckBox("paraProcessarACB", new PropertyModel(projeto, "paraProcessar")) {
                    @Override
                    protected void onUpdate(AjaxRequestTarget target) {

                        List<ProjetoDTO> listaProjetosProcessar = new ArrayList<>();
                        for (ProjetoDTO projeto : listaProjetos)
                            if (projeto.getParaProcessar()) listaProjetosProcessar.add(projeto);

                        if (listaProjetosProcessar.size() > 0) {
                            processarTodos.setEnabled(true);
                        } else {
                            processarTodos.setEnabled(false);
                        }
                        target.add(processarTodos);

                        lbProjetosSize.setDefaultModel(Model.of(listaProjetosProcessar.size()));
                        target.add(lbProjetosSize);
                    }
                };
                item.add(paraProcessarACB);

                item.add(new Label("nomeProjeto", projeto.getName()));
                item.add(new Label("projeto", projeto.getPath()));

                WebMarkupContainer progressProject = new WebMarkupContainer("progressProject");
                progressProject.setOutputMarkupPlaceholderTag(true);
                progressProject.setOutputMarkupId(true);
                progressProject.add(new AttributeModifier("style", "width: " + projeto.getProcentagem() + "%"));
                item.add(progressProject);
                projeto.progressProject = progressProject;

                Label lbPorcetagem = new Label("lbPorcentagem", projeto.getProcentagem());
                lbPorcetagem.setOutputMarkupId(true);
                lbPorcetagem.setOutputMarkupPlaceholderTag(true);
                projeto.lbPorcentagem = lbPorcetagem;
                progressProject.add(lbPorcetagem);
            }
        };
        lvProjetos.setOutputMarkupId(true);
        lvProjetos.setOutputMarkupPlaceholderTag(true);
        add(lvProjetos);
    }

    private void loadProjetos(){
        dataProcessamentoAtual = Util.dateNowFolder();
        totalProcessado.setValor(0);
        lbPastaSelecionada.setDefaultModel(Model.of(WicketApplication.JNOSE_PROJECTS_FOLDER));
        List<Projeto> listProjectBean = projetoBusiness.listAllWithFilter();
        for(Projeto projeto : listProjectBean){
            listaProjetos.add(new ProjetoDTO(projeto));
        }
        lvProjetos.setList(listaProjetos);
        processarTodos.setEnabled(true);
        lbProjetosSize.setDefaultModel(Model.of(listaProjetos.size()));
    }

    private void criarTimer(){
        AbstractAjaxTimerBehavior timer = new AbstractAjaxTimerBehavior(Duration.seconds(1)) {
            int cont = 0;

            @Override
            protected void onTimer(AjaxRequestTarget target) {
                Boolean todosProjetosProcessados = true;

                List<ProjetoDTO> listaProjetosProcessar = new ArrayList<>();

                for (ProjetoDTO projeto : listaProjetos) {
                    if (projeto.getParaProcessar()) {
                        listaProjetosProcessar.add(projeto);
                    }
                }

                for (ProjetoDTO projeto : listaProjetosProcessar) {

                    lkResultadoBotton.setEnabled(projeto.getProcessado());
                    target.add(lkResultadoBotton);

                    WebMarkupContainer lkResultado = projeto.getLkResultado();
                    lkResultado.setEnabled(projeto.getProcessado());
                    target.add(lkResultado);

                    Label lbPorcentagem = projeto.lbPorcentagem;
                    lbPorcentagem.setDefaultModel(Model.of(projeto.getProcentagem()));
                    target.add(lbPorcentagem);

                    WebMarkupContainer progressProject = projeto.progressProject;
                    progressProject.add(new AttributeModifier("style", "width: " + projeto.getProcentagem() + "%"));
                    target.add(progressProject);

                    todosProjetosProcessados = todosProjetosProcessados && projeto.getProcessado();
                }

                if (todosProjetosProcessados) {
                    totalProcessado.setValor((100 - totalProcessado.getValor()) + totalProcessado.getValor());
                    processando = false;
                }

                boolean processado = true;
                for (ProjetoDTO p : listaProjetosProcessar) {
                    processado = processado && p.getProcessado();
                }

            }
        };
        add(timer);
    }

}