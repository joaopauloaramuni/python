package br.ufba.jnose.pages;

import br.ufba.jnose.base.CSVCore;
import br.ufba.jnose.base.Util;
import br.ufba.jnose.pages.base.ImprimirPage;
import org.apache.wicket.AttributeModifier;
import org.apache.wicket.markup.html.basic.Label;
import org.apache.wicket.markup.html.link.DownloadLink;
import org.apache.wicket.markup.html.list.ListItem;
import org.apache.wicket.markup.html.list.ListView;

import java.io.File;
import java.util.List;

public class ResultPage extends ImprimirPage {
    private static final long serialVersionUID = 1L;

    public ResultPage(List<List<String>> todasLinhas, String title, String csvFileName, boolean fontColorized) {

        add(new Label("title",title + " - View Sample (100 of " + todasLinhas.size() + ")"));

        DownloadLink lkEsportCSV = new DownloadLink("lkEsportCSV", gerarCSV(todasLinhas,csvFileName));
        add(lkEsportCSV);

        if(todasLinhas.size() > 101){
            todasLinhas = todasLinhas.subList(0, 101);
        }
        
        ListView<List<String>> lista = new ListView<List<String>>("lista", todasLinhas) {
            @Override
            protected void populateItem(ListItem<List<String>> item) {
                List<String> linha = item.getModelObject();
                for(int i = 0; i <= 35; i++){
                    lb(i,linha,item, fontColorized);
                }
            }
        };

        add(lista);
    }

    private File gerarCSV(List<List<String>> todasLinhas, String csvFileName){
        String pathFile = CSVCore.criarCSV(todasLinhas, br.ufba.jnose.base.Util.dateNowFolder(),csvFileName);
        return new File(pathFile);
    }

    private void lb(int numero, List<String> linha, ListItem<List<String>> item, Boolean fontColorized){
        if(linha.size() > numero) {

            Label lb = new Label("lb" + numero, linha.get(numero));
            if(Util.isInt(linha.get(numero))){
                Integer n = Integer.parseInt(linha.get(numero));
                if(fontColorized) {
                    if (n != 0) {
                        lb.add(new AttributeModifier("style", "color:red"));
                    } else {
                        lb.add(new AttributeModifier("style", "color:green"));
                    }
                }
            }

            item.add(lb);
        }else{
            item.add(new Label("lb" + numero).setVisible(false));
        }
    }
}