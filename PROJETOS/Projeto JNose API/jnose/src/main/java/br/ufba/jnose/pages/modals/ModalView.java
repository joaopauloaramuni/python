package br.ufba.jnose.pages.modals;

import de.agilecoders.wicket.core.markup.html.bootstrap.dialog.Modal;
import org.apache.wicket.markup.html.basic.Label;
import org.apache.wicket.model.Model;

public class ModalView extends Modal<Void> {

    public ModalView(String markupId, String header, String content) {
        super(markupId);
        header(Model.of(header));
        add(new Label("content",content).setEscapeModelStrings(false));
    }

}
