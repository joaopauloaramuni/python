package br.ufba.jnose.pages.modals;

import br.ufba.jnose.entities.Projeto;
import de.agilecoders.wicket.core.markup.html.bootstrap.dialog.Modal;
import org.apache.wicket.markup.html.basic.Label;
import org.apache.wicket.model.Model;

import java.text.SimpleDateFormat;

public class ModalDetalhes<Void> extends Modal<Void> {

    public ModalDetalhes(String id, Projeto projeto) {
        super(id);
        this.header(Model.of(projeto.getName()));
        add(new Label("name", projeto.getName()));
        add(new Label("url", projeto.getUrl()));
        add(new Label("path", projeto.getPath()));
        add(new Label("version", projeto.getJunitVersion()));
        add(new Label("stars", projeto.getStars()));
        SimpleDateFormat df = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
        if(projeto.getDateUpdate() == null) {
            add(new Label("update", ""));
        }else{
            add(new Label("update", df.format(projeto.getDateUpdate())));
        }
    }

}
