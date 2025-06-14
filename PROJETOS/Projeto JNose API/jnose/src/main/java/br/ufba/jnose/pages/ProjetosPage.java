package br.ufba.jnose.pages;

import br.ufba.jnose.business.ProjetoBusiness;
import br.ufba.jnose.base.GitCore;
import br.ufba.jnose.base.JNose;
import br.ufba.jnose.dtolocal.Commit;
import br.ufba.jnose.dtolocal.ProjetoDTO;
import br.ufba.jnose.entities.Projeto;
import br.ufba.jnose.pages.base.BasePage;
import org.apache.commons.io.FileUtils;
import org.apache.wicket.ajax.AjaxRequestTarget;
import br.ufba.jnose.pages.modals.ModalDetalhes;
import org.apache.wicket.ajax.markup.html.AjaxLink;
import org.apache.wicket.extensions.ajax.markup.html.IndicatingAjaxButton;
import org.apache.wicket.markup.html.basic.Label;
import org.apache.wicket.markup.html.form.Form;
import org.apache.wicket.markup.html.form.TextField;
import org.apache.wicket.markup.html.link.Link;
import org.apache.wicket.markup.html.list.ListItem;
import org.apache.wicket.markup.html.list.ListView;
import org.apache.wicket.model.PropertyModel;
import org.apache.wicket.spring.injection.annot.SpringBean;

import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class ProjetosPage extends BasePage {
    private static final long serialVersionUID = 1L;

    @SpringBean
    private ProjetoBusiness projetoBusiness;

    private String repoGit;

    public ProjetosPage(){
        this("");
    }

    public ProjetosPage(String repo) {
        super("ProjetosPage");
        this.repoGit = repo;

        Form form = new Form<>("form");

        TextField tfGitRepo = new TextField("tfGitRepo", new PropertyModel(this, "repoGit"));
        tfGitRepo.setRequired(true);
        form.add(tfGitRepo);

        form.add(new Link<String>("lkAddOracle") {
            @Override
            public void onClick() {
                repoGit = "https://github.com/tassiovirginio/jnose-dataset.git";
                setResponsePage(new ProjetosPage(repoGit));
            }
        });

        IndicatingAjaxButton btEnviar = new IndicatingAjaxButton("btClone") {
            @Override
            public void onSubmit(AjaxRequestTarget target) {
                ProjetoDTO projeto = GitCore.gitClone(repoGit);

                br.ufba.jnose.entities.Projeto projeto2 = new br.ufba.jnose.entities.Projeto();
                projeto2.setName(projeto.getName());
                projeto2.setJunitVersion(JNose.getJUnitVersion(projeto.getPath()).toString());
                projeto2.setStars(GitCore.getStarts(projeto.getPath()));
                projeto2.setPath(projeto.getPath());
                projeto2.setUrl(repoGit);
                ArrayList<Commit> lista = GitCore.gitLogOneLine(projeto.getPath());
                projeto2.setDateUpdate(lista.get(0).date);
                projetoBusiness.save(projeto2);

                setResponsePage(ProjetosPage.class);
            }
        };
        form.add(btEnviar);
        add(form);

        List<br.ufba.jnose.entities.Projeto> listaProjetosVerificar = projetoBusiness.listAll();

        for(Projeto projeto : listaProjetosVerificar){
            File file = new File(projeto.getPath());
            if(file.exists() == false){
                projetoBusiness.delete(projeto);
            }
        }

        List<br.ufba.jnose.entities.Projeto> listaProjetos = projetoBusiness.listAll();

        ListView<br.ufba.jnose.entities.Projeto> lista2 = new ListView<br.ufba.jnose.entities.Projeto>("lista", listaProjetos) {
            @Override
            protected void populateItem(ListItem<br.ufba.jnose.entities.Projeto> item) {
                br.ufba.jnose.entities.Projeto projeto = item.getModelObject();
                item.add(new Label("projetoNome", projeto.getName()));
                item.add(new Label("path", projeto.getPath()));
                item.add(new Label("url", projeto.getUrl()));
                item.add(new Label("junit", projeto.getJunitVersion()));
                item.add(new Label("stars", projeto.getStars()));

                ArrayList<Commit> lista = GitCore.gitLogOneLine(projeto.getPath());
                SimpleDateFormat df = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
                item.add(new Label("lastupdate", df.format(lista.get(0).date)));

                item.add(new Link<String>("linkPull") {
                    @Override
                    public void onClick() {
                        GitCore.pull(projeto.getPath());
                        ArrayList<Commit> lista = GitCore.gitLogOneLine(projeto.getPath());
                        Date dateUpdate = lista.get(0).date;
                        projeto.setDateUpdate(dateUpdate);
                        projetoBusiness.save(projeto);
                        setResponsePage(ProjetosPage.class);
                    }
                });
                item.add(new Link<String>("linkDelete") {
                    @Override
                    public void onClick() {
                        projetoBusiness.delete(projeto.getId());

                        File file = new File(projeto.getPath());
                        try {
                            FileUtils.deleteDirectory(file);
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                        setResponsePage(ProjetosPage.class);
                    }
                });

                final ModalDetalhes modal = new ModalDetalhes("modal", projeto);
                item.add(modal);

                item.add(new AjaxLink<Void>("btModal") {
                    @Override
                    public void onClick(AjaxRequestTarget ajaxRequestTarget) {
                        modal.show(true);
                        modal.setVisible(true);
                        ajaxRequestTarget.add(modal);
                    }
                });

            }
        };
        add(lista2);

    }

}


