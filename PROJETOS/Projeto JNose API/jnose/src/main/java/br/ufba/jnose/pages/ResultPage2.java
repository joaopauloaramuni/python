package br.ufba.jnose.pages;

import br.ufba.jnose.base.CSVCore;
import br.ufba.jnose.base.Util;
import br.ufba.jnose.dtolocal.ProjetoDTO;
import br.ufba.jnose.pages.base.ImprimirPage;
import org.apache.wicket.AttributeModifier;
import org.apache.wicket.markup.html.basic.Label;
import org.apache.wicket.markup.html.link.DownloadLink;
import org.apache.wicket.markup.html.link.Link;
import org.apache.wicket.markup.html.list.ListItem;
import org.apache.wicket.markup.html.list.ListView;

import java.io.File;
import java.util.List;

public class ResultPage2 extends ImprimirPage {
    private static final long serialVersionUID = 1L;

    public ResultPage2(ProjetoDTO projeto, List<List<String>> todasLinhas, String title, String csvFileName, boolean fontColorized) {

        add(new Label("title",title + " - View Sample (100 of " + todasLinhas.size() + ")"));

        DownloadLink lkEsportCSV = new DownloadLink("lkEsportCSV",gerarCSV(todasLinhas,csvFileName));
        add(lkEsportCSV);

        List<List<String>> todasLinhasSample;

        if(todasLinhas.size() > 101){
            todasLinhasSample = todasLinhas.subList(0, 101);
        }else{
            todasLinhasSample = todasLinhas;
        }

        ListView<List<String>> lista = new ListView<List<String>>("lista",todasLinhasSample) {
            @Override
            protected void populateItem(ListItem<List<String>> item) {
                List<String> linha = item.getModelObject();
                for(int i = 0; i <= 10; i++){
                    lb(i,linha,item, fontColorized);
                }

//                if(Util.isInt(linha.get(9))) {
//                    String testsmellName = linha.get(7);
//                    String pathFileTest = linha.get(2);
//                    int inicio = Integer.parseInt(linha.get(9));
//                    int fim = Integer.parseInt(linha.get(10));
//                    item.add(new Link<String>("codigo") {
//                        @Override
//                        public void onClick() {
//                            setResponsePage(new CodePage(projeto,testsmellName,pathFileTest,inicio,fim));
////                            System.out.println(pathFileTest + " - " + inicio + " - " + fim);
//                        }
//                    });
//                }else{
//                    item.add(new Link<String>("codigo") {
//                        @Override
//                        public void onClick() {
//                        }
//                    }.setVisible(false));
//                }

                if(linha.get(9).contains("-") || linha.get(9).contains(",") || Util.isInt(linha.get(9))) {
                    String testsmellName = linha.get(7);
                    String pathFileTest = linha.get(2);
//                    int inicio = Integer.parseInt(linha.get(9));
                    //int fim = Integer.parseInt(linha.get(10));
                    String range = linha.get(9);
                    item.add(new Link<String>("codigo") {
                        @Override
                        public void onClick() {
                            setResponsePage(new CodePage(projeto,testsmellName,pathFileTest,range));
                        }
                    });
                }else{
                    item.add(new Link<String>("codigo") {
                        @Override
                        public void onClick() {
                        }
                    }.setVisible(false));
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