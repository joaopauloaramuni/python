package br.ufba.jnose.pages;

import br.ufba.jnose.business.ProjetoBusiness;
import br.ufba.jnose.base.GitCore;
import br.ufba.jnose.base.JNose;
import br.ufba.jnose.dtolocal.ProjetoDTO;
import br.ufba.jnose.entities.Projeto;
import br.ufba.jnose.pages.base.BasePage;
//import br.ufba.jnose.pages.charts.BasicLineOptions;
//import br.ufba.jnose.pages.charts.UserCommitBarOptions;
import org.apache.wicket.AttributeModifier;
import org.apache.wicket.ajax.AbstractAjaxTimerBehavior;
import org.apache.wicket.ajax.AjaxEventBehavior;
import org.apache.wicket.ajax.AjaxPreventSubmitBehavior;
import org.apache.wicket.ajax.AjaxRequestTarget;
import org.apache.wicket.ajax.markup.html.AjaxLink;
import org.apache.wicket.markup.html.basic.Label;
import org.apache.wicket.markup.html.form.Form;
import org.apache.wicket.markup.html.form.Radio;
import org.apache.wicket.markup.html.form.RadioGroup;
import org.apache.wicket.markup.html.link.Link;
import org.apache.wicket.markup.html.list.ListItem;
import org.apache.wicket.markup.html.list.ListView;
import org.apache.wicket.model.Model;
import org.apache.wicket.model.PropertyModel;
import org.apache.wicket.spring.injection.annot.SpringBean;
import org.apache.wicket.util.time.Duration;

import java.util.*;

public class EvolutionPage extends BasePage {
    private static final long serialVersionUID = 1L;

    private Label taLogInfo;
    private StringBuffer logRetorno;
    private List<ProjetoDTO> listaProjetos;
    private ListView<ProjetoDTO> lvProjetos;

    @SpringBean
    private ProjetoBusiness projetoBusiness;

    public EvolutionPage() {
        super("EvolutionPage");
        listaProjetos = new ArrayList<>();
        logRetorno = new StringBuffer();
        criarTimer();
        criarListaProjetos();
        criarLogInfo();
        loadProjetos();
    }

    private void loadProjetos() {
        List<Projeto> listProjetoBean = projetoBusiness.listAllWithFilter();
        for(Projeto projeto : listProjetoBean){
            listaProjetos.add(new ProjetoDTO(projeto));
        }
        lvProjetos.setList(listaProjetos);
    }

    private void criarLogInfo() {
        taLogInfo = new Label("taLogInfo", Model.of(logRetorno));
        taLogInfo.setEscapeModelStrings(false);
        taLogInfo.setOutputMarkupId(true);
        taLogInfo.setOutputMarkupPlaceholderTag(true);
        add(taLogInfo);
    }

    private void criarTimer() {
        AbstractAjaxTimerBehavior timer = new AbstractAjaxTimerBehavior(Duration.seconds(1)) {
            @Override
            protected void onTimer(AjaxRequestTarget target) {
                taLogInfo.setDefaultModelObject(logRetorno);
                target.add(taLogInfo);

                for(ProjetoDTO projeto:listaProjetos){
                    if(projeto.getMapResults().containsKey(1)){
                        projeto.lkResult1.setEnabled(true);
                        projeto.lkResult1.add(AttributeModifier.remove("style"));
                        target.add(projeto.lkResult1);
                    }else{
                        projeto.lkResult1.setEnabled(false);
                        projeto.lkResult1.add(AttributeModifier.append("style","background-color: #e0e0eb;"));
                        target.add(projeto.lkResult1);
                    }
                    if(projeto.getMapResults().containsKey(2)){
                        projeto.lkResult2.setEnabled(true);
                        projeto.lkResult2.add(AttributeModifier.remove("style"));
                        target.add(projeto.lkResult2);
                    }else{
                        projeto.lkResult2.setEnabled(false);
                        projeto.lkResult2.add(AttributeModifier.append("style","background-color: #e0e0eb;"));
                        target.add(projeto.lkResult2);
                    }
                    if(projeto.getMapResults().containsKey(3)){
                        projeto.lkResult3.setEnabled(true);
                        projeto.lkResult3.add(AttributeModifier.remove("style"));
                        target.add(projeto.lkResult3);
                    }else{
                        projeto.lkResult3.setEnabled(false);
                        projeto.lkResult3.add(AttributeModifier.append("style","background-color: #e0e0eb;"));
                        target.add(projeto.lkResult3);
                    }
                    if(projeto.getMapResults().containsKey(4)){
                        projeto.lkResult4.setEnabled(true);
                        projeto.lkResult4.add(AttributeModifier.remove("style"));
                        target.add(projeto.lkResult4);
                    }else{
                        projeto.lkResult4.setEnabled(false);
                        projeto.lkResult4.add(AttributeModifier.append("style","background-color: #e0e0eb;"));
                        target.add(projeto.lkResult4);
                    }
                    if(projeto.getMapResults().containsKey(2)){
                        projeto.lkChart2.setEnabled(true);
                        projeto.lkChart2.add(AttributeModifier.remove("style"));
                        target.add(projeto.lkChart2);
                    }else{
                        projeto.lkChart2.setEnabled(false);
                        projeto.lkChart2.add(AttributeModifier.append("style","background-color: #e0e0eb;"));
                        target.add(projeto.lkChart2);
                    }

                    if(projeto.getMapResults().containsKey(5)){
                        projeto.lkChart3.setEnabled(true);
                        projeto.lkChart3.add(AttributeModifier.remove("style"));
                        target.add(projeto.lkChart3);
                    }else{
                        projeto.lkChart3.setEnabled(false);
                        projeto.lkChart3.add(AttributeModifier.append("style","background-color: #e0e0eb;"));
                        target.add(projeto.lkChart3);
                    }
                }

            }
        };
        add(timer);
    }


    private void criarListaProjetos() {
        lvProjetos = new ListView<ProjetoDTO>("lvProjetos", listaProjetos) {
            @Override
            protected void populateItem(ListItem<ProjetoDTO> item) {

                ProjetoDTO projeto = item.getModelObject();

                Map<Integer, List<List<String>>> mapResults = new HashMap<>();
                projeto.setMapResults(mapResults);
                item.add(new Label("nomeProjeto", projeto.getName()));
                item.add(new Label("path", projeto.getPath()));
                item.add(new Label("branch", GitCore.branch(projeto.getPath())));
                projeto.setListaCommits(GitCore.gitLogOneLine(projeto.getPath()));
                projeto.setListaTags(GitCore.gitTags(projeto.getPath()));

                Form form = new Form<String>("form");
                form.setOutputMarkupId(true);
                form.add(new AjaxPreventSubmitBehavior());

                Link lkResult1 = new Link<String>("lkResult1") {
                    @Override
                    public void onClick() {
                        List<List<String>> todasLinhas1 = mapResults.get(1);
                        setResponsePage(new ResultPage(todasLinhas1, "Evolution Report 1 - TestSmells by Commit and Class: " + projeto.getName(), "resultado_evolution1", false));
                    }
                };
                lkResult1.setOutputMarkupId(true);
                lkResult1.setOutputMarkupPlaceholderTag(true);
                lkResult1.setEnabled(false);
                lkResult1.add(AttributeModifier.append("style","background-color: #e0e0eb;"));
                projeto.lkResult1 = lkResult1;
                form.add(lkResult1);

                Link lkResult2 = new Link<String>("lkResult2") {
                    @Override
                    public void onClick() {
                        List<List<String>> todasLinhas2 = mapResults.get(2);
                        setResponsePage(new ResultPage(todasLinhas2, "Evolution Report 2 - Total Testsmells by Commit: " + projeto.getName(), "resultado_evolution2", false));

                    }
                };
                lkResult2.setOutputMarkupId(true);
                lkResult2.setOutputMarkupPlaceholderTag(true);
                lkResult2.setEnabled(false);
                lkResult2.add(AttributeModifier.append("style","background-color: #e0e0eb;"));
                projeto.lkResult2 = lkResult2;
                form.add(lkResult2);

                Link lkResult3 = new Link<String>("lkResult3") {
                    @Override
                    public void onClick() {
                        List<List<String>> todasLinhas3 = mapResults.get(3);
                        setResponsePage(new ResultPage(todasLinhas3, "Evolution Report 3 - Total Testsmells by Commit: " + projeto.getName(), "resultado_evolution2", false));

                    }
                };
                lkResult3.setOutputMarkupId(true);
                lkResult3.setOutputMarkupPlaceholderTag(true);
                lkResult3.setEnabled(false);
                lkResult3.add(AttributeModifier.append("style","background-color: #e0e0eb;"));
                projeto.lkResult3 = lkResult3;
                form.add(lkResult3);

                Link lkResult4 = new Link<String>("lkResult4") {
                    @Override
                    public void onClick() {
                        List<List<String>> todasLinhas4 = mapResults.get(4);
                        setResponsePage(new ResultPage(todasLinhas4, "Evolution Report 4 - Total Testsmells by Commit: " + projeto.getName(), "resultado_evolution2", false));

                    }
                };
                lkResult4.setOutputMarkupId(true);
                lkResult4.setOutputMarkupPlaceholderTag(true);
                lkResult4.setEnabled(false);
                lkResult4.add(AttributeModifier.append("style","background-color: #e0e0eb;"));
                projeto.lkResult4 = lkResult4;
                form.add(lkResult4);

                Link lkChart2 = new Link<String>("lkChart2") {
                    @Override
                    public void onClick() {
                        List<List<String>> todasLinhas2 = mapResults.get(2);
//                        setResponsePage(new ChartsPage( projeto.getName() ,new BasicLineOptions(todasLinhas2)));
                    }
                };
                lkChart2.setOutputMarkupId(true);
                lkChart2.setOutputMarkupPlaceholderTag(true);
                lkChart2.setEnabled(false);
                lkChart2.add(AttributeModifier.append("style","background-color: #e0e0eb;"));
                projeto.lkChart2 = lkChart2;
                form.add(lkChart2);

                Link lkChart3 = new Link<String>("lkChart3") {
                    @Override
                    public void onClick() {
                        List<List<String>> todasLinhas5 = mapResults.get(5);
//                        setResponsePage(new ChartsPage( projeto.getName() ,new UserCommitBarOptions(todasLinhas5)));
                    }
                };
                lkChart3.setOutputMarkupId(true);
                lkChart3.setOutputMarkupPlaceholderTag(true);
                lkChart3.setEnabled(false);
                lkChart3.add(AttributeModifier.append("style","background-color: #e0e0eb;"));
                projeto.lkChart3 = lkChart3;
                form.add(lkChart3);

                AjaxLink btSubmit = new AjaxLink<String>("btSubmit") {
                    @Override
                    public void onClick(AjaxRequestTarget target) {
                        System.out.println("Processamento do projeto: " + projeto.getName() + " - Start");
                        logRetorno.insert(0,"Processamento do projeto: " + projeto.getName() + " - Start<br>");
                        new Thread() { // IMPORTANTE: AQUI SE CRIA AS THREADS
                            @Override
                            public void run() {
                                JNose.processarEvolution(projeto, logRetorno, projeto.getMapResults());
                            }
                        }.start();
                    }
                };
                btSubmit.setEnabled(false);
                form.add(btSubmit);


                RadioGroup radioCommitsTags = new RadioGroup("radioCommitsTags", PropertyModel.of (projeto, "optionSelected"));

                Radio radio1 = new Radio("commit",new Model<String>("commit"));
                radio1.add(new AjaxEventBehavior("change") {
                    protected void onEvent(AjaxRequestTarget target) {
                        projeto.setOptionSelected("commit");
                        btSubmit.setEnabled(true);
                        target.add(btSubmit);
                    }
                });
                radioCommitsTags.add(radio1);
                radioCommitsTags.add(new Label("ck1", Model.of(projeto.getListaCommits().size())));

                Radio radio2 = new Radio("tag",new Model<String>("tag"));
                radio2.add(new AjaxEventBehavior("change") {
                    protected void onEvent(AjaxRequestTarget target) {
                        projeto.setOptionSelected("tag");
                        btSubmit.setEnabled(true);
                        target.add(btSubmit);
                    }
                });
                radioCommitsTags.add(radio2);
                radioCommitsTags.add(new Label("ck2", Model.of(projeto.getListaTags().size())));
                radioCommitsTags.setOutputMarkupId(true);
                radioCommitsTags.setOutputMarkupPlaceholderTag(true);
                form.add(radioCommitsTags);
                item.add(form);
            }
        };
        lvProjetos.setOutputMarkupId(true);
        lvProjetos.setOutputMarkupPlaceholderTag(true);
        add(lvProjetos);
    }

}