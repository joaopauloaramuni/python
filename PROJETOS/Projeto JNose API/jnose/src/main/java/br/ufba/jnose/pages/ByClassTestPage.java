package br.ufba.jnose.pages;

import br.ufba.jnose.WicketApplication;
import br.ufba.jnose.business.ProjetoBusiness;
import br.ufba.jnose.base.Util;
import br.ufba.jnose.dtolocal.TotalProcessado;
import br.ufba.jnose.base.JNose;
import br.ufba.jnose.dtolocal.ProjetoDTO;
import br.ufba.jnose.entities.Projeto;
import br.ufba.jnose.pages.base.BasePage;
//import br.ufba.jnose.pages.charts.TestSmellsBarOptions;
import com.googlecode.wicket.jquery.ui.panel.JQueryFeedbackPanel;
import org.apache.wicket.AttributeModifier;
import org.apache.wicket.ajax.AbstractAjaxTimerBehavior;
import org.apache.wicket.ajax.AjaxRequestTarget;
import org.apache.wicket.ajax.markup.html.form.AjaxCheckBox;
import org.apache.wicket.extensions.ajax.markup.html.IndicatingAjaxLink;
import org.apache.wicket.markup.html.WebMarkupContainer;
import org.apache.wicket.markup.html.link.Link;
import org.apache.wicket.markup.html.list.ListItem;
import org.apache.wicket.markup.html.list.ListView;
import org.apache.wicket.markup.html.panel.FeedbackPanel;
import org.apache.wicket.model.Model;
import org.apache.wicket.markup.html.basic.Label;
import org.apache.wicket.model.PropertyModel;
import org.apache.wicket.protocol.http.WebApplication;
import org.apache.wicket.spring.injection.annot.SpringBean;
import org.apache.wicket.util.time.Duration;

import java.io.*;
import java.util.*;
import java.util.List;

import static java.lang.System.out;

public class ByClassTestPage extends BasePage {
    private static final long serialVersionUID = 1L;

    private String pastaPath;
    private String pathAppToWebapp;
    private String pastaPathReport;
    private List<ProjetoDTO> listaProjetos;
    private ListView<ProjetoDTO> lvProjetos;
    private Label taLog;
    private TotalProcessado totalProcessado;
    private Boolean processando;
    private IndicatingAjaxLink processarTodos;
    private StringBuffer logRetorno;
    private String dataProcessamentoAtual;
    private boolean processarCobertura;
    private List<List<String>> listaResultado;

    private Link lkResultadoBotton;

    @SpringBean
    private ProjetoBusiness projetoBusiness;

    public ByClassTestPage() {
        super("ByClassTestPage");

        //Carregando variáveis
        pathAppToWebapp = WebApplication.get().getServletContext().getRealPath("");
        pastaPathReport = pathAppToWebapp + File.separatorChar + "reports" + File.separatorChar;
        pastaPath = "";
        logRetorno = new StringBuffer();
        processando = false;
        processarCobertura = false;
        totalProcessado = new TotalProcessado();
        totalProcessado.setValor(0);

        criarCheckBoxCobertura();

        taLog = new Label("taLog");
        taLog.setEscapeModelStrings(false).setOutputMarkupId(true).setOutputMarkupPlaceholderTag(true);
        add(taLog);

        criarListaProjetos();

        FeedbackPanel feedback = new JQueryFeedbackPanel("feedback");
        add(feedback.setOutputMarkupId(true));

        criarBotaoProcessarTodos();

        lkResultadoBotton = new Link<String>("lkResultado") {
            @Override
            public void onClick() {
                setResponsePage(new ResultPage(listaResultado, "Result By ClassTest", "result_byclasstest", true));
            }
        };
        lkResultadoBotton.setEnabled(processando);
        lkResultadoBotton.setOutputMarkupId(true);
        lkResultadoBotton.setOutputMarkupPlaceholderTag(true);
        add(lkResultadoBotton);

        Link lkCharts = new Link<String>("lkCharts") {
            @Override
            public void onClick() {
//                setResponsePage(new ChartsPage("Charts By ClassTest", new TestSmellsBarOptions(listaResultado)));
            }
        };
        add(lkCharts.setVisible(false));

        loadProjetos();

        criarTimer();
    }

    private void criarBotaoProcessarTodos() {
        processarTodos = new IndicatingAjaxLink<String>("processarTodos") {
            @Override
            public void onClick(AjaxRequestTarget target) {
                processando = true;
                List<ProjetoDTO> listaParaProcessar = new ArrayList<>();

                for (ProjetoDTO projetoDTO : listaProjetos) {
                    if (projetoDTO.getParaProcessar()) {
                        listaParaProcessar.add(projetoDTO);
                    }
                }
                listaResultado = JNose.processarProjetos2(listaParaProcessar, dataProcessamentoAtual, totalProcessado, pastaPathReport, logRetorno);
            }
        };
        processarTodos.setEnabled(false);
        add(processarTodos);
    }

    private void criarCheckBoxCobertura() {
        AjaxCheckBox acbCobertura = new AjaxCheckBox("acbCobertura", new PropertyModel(this, "processarCobertura")) {
            @Override
            protected void onUpdate(AjaxRequestTarget ajaxRequestTarget) {
                WicketApplication.COBERTURA_ON = processarCobertura;
                out.println("COVERAGE_ON: " + processarCobertura);
                logRetorno.insert(0, "COVERAGE_ON: " + processarCobertura + " <br>");
            }
        };
        add(acbCobertura);
    }


    private void loadProjetos() {
        dataProcessamentoAtual = Util.dateNowFolder();
        logRetorno = new StringBuffer();
        totalProcessado.setValor(0);
        List<Projeto> listaProjetosBean = projetoBusiness.listAllWithFilter();
        for (Projeto projeto : listaProjetosBean) {
            listaProjetos.add(new ProjetoDTO(projeto));
        }
        lvProjetos.setList(listaProjetos);
        processarTodos.setEnabled(true);
    }

    private void criarListaProjetos() {
        listaProjetos = new ArrayList<>();

        lvProjetos = new ListView<ProjetoDTO>("lvProjetos", listaProjetos) {
            @Override
            protected void populateItem(ListItem<ProjetoDTO> item) {

                ProjetoDTO projetoDTO = item.getModelObject();

                Link lkCharts = new Link<String>("lkCharts") {
                    @Override
                    public void onClick() {
//                        setResponsePage(new ChartsPage("Charts By ClassTest: " + projetoDTO.getName(), new TestSmellsBarOptions(projetoDTO.getResultado())));
                    }
                };
                lkCharts.setEnabled(projetoDTO.getProcessado());
                lkCharts.setOutputMarkupId(true);
                lkCharts.setOutputMarkupPlaceholderTag(true);
                item.add(lkCharts);
                projetoDTO.lkCharts = lkCharts;

                Link lkResultado = new Link<String>("lkResultado") {
                    @Override
                    public void onClick() {
                        setResponsePage(new ResultPage(projetoDTO.getResultado(), "Result By ClassTest: " + projetoDTO.getName(), projetoDTO.getName() + "_result_byclasstest", true));
                    }
                };
                lkResultado.setEnabled(projetoDTO.getProcessado());
                lkResultado.setOutputMarkupId(true);
                lkResultado.setOutputMarkupPlaceholderTag(true);
                item.add(lkResultado);
                projetoDTO.setLkResultado(lkResultado);

                AjaxCheckBox paraProcessarACB = new AjaxCheckBox("paraProcessarACB", new PropertyModel(projetoDTO, "paraProcessar")) {
                    @Override
                    protected void onUpdate(AjaxRequestTarget target) {

                        List<ProjetoDTO> listaProjetosProcessar = new ArrayList<>();

                        for (ProjetoDTO projetoDTO : listaProjetos) {
                            if (projetoDTO.getParaProcessar()) {
                                listaProjetosProcessar.add(projetoDTO);
                            }
                            ;
                        }

                        if (listaProjetosProcessar.size() > 0) {
                            processarTodos.setEnabled(true);
                        } else {
                            processarTodos.setEnabled(false);
                        }
                        target.add(processarTodos);
                    }
                };
                item.add(paraProcessarACB);

                item.add(new Label("nomeProjeto", projetoDTO.getName()));
                item.add(new Label("projeto", projetoDTO.getPath()));

                WebMarkupContainer iconProcessado = new WebMarkupContainer("iconProcessado");
                iconProcessado.setVisible(projetoDTO.getProcessado());
                iconProcessado.setOutputMarkupId(true);
                iconProcessado.setOutputMarkupPlaceholderTag(true);
                item.add(iconProcessado);
                projetoDTO.iconProcessado = iconProcessado;

                WebMarkupContainer iconNaoProcessado = new WebMarkupContainer("iconNaoProcessado");
                iconNaoProcessado.setVisible(!projetoDTO.getProcessado());
                iconNaoProcessado.setOutputMarkupId(true);
                iconNaoProcessado.setOutputMarkupPlaceholderTag(true);
                item.add(iconNaoProcessado);
                projetoDTO.iconNaoProcessado = iconNaoProcessado;

                WebMarkupContainer progressProject = new WebMarkupContainer("progressProject");
                progressProject.setOutputMarkupPlaceholderTag(true);
                progressProject.setOutputMarkupId(true);//style="width: 25%"
                progressProject.add(new AttributeModifier("style", "width: " + projetoDTO.getProcentagem() + "%"));
                item.add(progressProject);
                projetoDTO.progressProject = progressProject;

                Label lbPorcetagem = new Label("lbPorcentagem", projetoDTO.getProcentagem());
                lbPorcetagem.setOutputMarkupId(true);
                lbPorcetagem.setOutputMarkupPlaceholderTag(true);
                projetoDTO.lbPorcentagem = lbPorcetagem;
                progressProject.add(lbPorcetagem);

            }
        };
        lvProjetos.setOutputMarkupId(true);
        lvProjetos.setOutputMarkupPlaceholderTag(true);
        add(lvProjetos);

    }

    private void criarTimer() {
        AbstractAjaxTimerBehavior timer = new AbstractAjaxTimerBehavior(Duration.seconds(1)) {
            int cont = 0;

            @Override
            protected void onTimer(AjaxRequestTarget target) {
                taLog.setDefaultModel(Model.of(logRetorno));
                target.add(taLog);

                Boolean todosProjetosProcessados = true;

                List<ProjetoDTO> listaProjetosProcessar = new ArrayList<>();

                for (ProjetoDTO projetoDTO : listaProjetos) {

                    if (projetoDTO.getParaProcessar()) {
                        listaProjetosProcessar.add(projetoDTO);
                    }
                }

                for (ProjetoDTO projetoDTO : listaProjetosProcessar) {

                    if (!lkResultadoBotton.isEnabled()) {
                        lkResultadoBotton.setEnabled(projetoDTO.getProcessado());
                        target.add(lkResultadoBotton);
                    }


                    WebMarkupContainer lkResultado = projetoDTO.getLkResultado();
                    if (!lkResultado.isEnabled()) {
                        lkResultado.setEnabled(projetoDTO.getProcessado());
                        target.add(lkResultado);
                    }

                    WebMarkupContainer lkCharts = projetoDTO.lkCharts;
                    if (!lkCharts.isEnabled()) {
                        lkCharts.setEnabled(projetoDTO.getProcessado());
                        target.add(lkCharts);
                    }

                    WebMarkupContainer iconProcessado = projetoDTO.iconProcessado;
                    iconProcessado.setVisible(projetoDTO.getProcessado());
                    target.add(iconProcessado);

                    WebMarkupContainer iconNaoProcessado = projetoDTO.iconNaoProcessado;
                    iconNaoProcessado.setVisible(!projetoDTO.getProcessado());
                    target.add(iconNaoProcessado);

                    Label lbPorcentagem = projetoDTO.lbPorcentagem;
                    lbPorcentagem.setDefaultModel(Model.of(projetoDTO.getProcentagem()));
                    target.add(lbPorcentagem);

                    WebMarkupContainer progressProject = projetoDTO.progressProject;
                    progressProject.add(new AttributeModifier("style", "width: " + projetoDTO.getProcentagem() + "%"));
                    target.add(progressProject);

                    todosProjetosProcessados = todosProjetosProcessados && projetoDTO.getProcessado();
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