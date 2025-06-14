package br.ufba.jnose.pages.base;

import br.ufba.jnose.business.ProjetoBusiness;
import br.ufba.jnose.pages.*;
import org.apache.wicket.AttributeModifier;
import org.apache.wicket.ajax.AbstractAjaxTimerBehavior;
import org.apache.wicket.ajax.AjaxRequestTarget;
import org.apache.wicket.markup.html.WebMarkupContainer;
import org.apache.wicket.markup.html.WebPage;
import org.apache.wicket.markup.html.link.Link;
import org.apache.wicket.spring.injection.annot.SpringBean;
import org.apache.wicket.util.time.Duration;

public class BasePage extends WebPage {
    private static final long serialVersionUID = 1L;

    @SpringBean
    private ProjetoBusiness projetoBusiness;

    private WebMarkupContainer footTime;

    public BasePage(String paginaAtual) {

        footTime = new WebMarkupContainer("footTimeHome");
        footTime.setOutputMarkupId(true);
        footTime.setOutputMarkupPlaceholderTag(true);
        add(footTime);

        Link linkProjetos = new Link<String>("linkProjetos") {
            @Override
            public void onClick() {
                setResponsePage(ProjetosPage.class);
            }
        };
        if(paginaAtual.equals("ProjetosPage")){
            linkProjetos.add(new AttributeModifier("style", "color:red"));
        }

        Link linkByClassTest = new Link<String>("linkByClassTest") {
            @Override
            public void onClick() {
                setResponsePage(ByClassTestPage.class);
            }
        };
        if(paginaAtual.equals("ByClassTestPage")){
            linkByClassTest.add(new AttributeModifier("style", "color:red"));
        }

        Link linkByTestSmells = new Link<String>("linkByTestSmells") {
            @Override
            public void onClick() {
                setResponsePage(ByTestSmellsPage.class);
            }
        };
        if(paginaAtual.equals("ByTestSmellsPage")){
            linkByTestSmells.add(new AttributeModifier("style", "color:red"));
        }

        Link linkEvolution = new Link<String>("linkEvolution") {
            @Override
            public void onClick() {
                setResponsePage(EvolutionPage.class);
            }
        };
        if(paginaAtual.equals("EvolutionPage")){
            linkEvolution.add(new AttributeModifier("style", "color:red"));
        }

        Link linkAnalyze = new Link<String>("linkAnalyze") {
            @Override
            public void onClick() {
                setResponsePage(AnalyzePage.class);
            }
        };
        if(paginaAtual.equals("AnalyzePage")){
            linkAnalyze.add(new AttributeModifier("style", "color:red"));
        }

        Link linkConfig = new Link<String>("linkConfig") {
            @Override
            public void onClick() {
                setResponsePage(ConfigPage.class);
            }
        };
        if(paginaAtual.equals("ConfigPage")){
            linkConfig.add(new AttributeModifier("style", "color:red"));
        }

        Link linkStorage = new Link<String>("linkResearch") {
            @Override
            public void onClick() {
                setResponsePage(ResearchPage.class);
            }
        };
        if(paginaAtual.equals("StoragePage")){
            linkStorage.add(new AttributeModifier("style", "color:red"));
        }

        add(linkProjetos);
        add(linkByClassTest);
        add(linkByTestSmells);
        add(linkAnalyze);
        add(linkEvolution);
        add(linkConfig);
        add(linkStorage);

        AbstractAjaxTimerBehavior timerHome = new AbstractAjaxTimerBehavior(Duration.seconds(1)) {
            String signal = "";
            @Override
            protected void onTimer(AjaxRequestTarget target) {
                if(footTime.isVisible()){
                    footTime.setVisible(false);
                }else{
                    footTime.setVisible(true);
                }
                target.add(footTime);
            }
        };
        add(timerHome);

    }

}
