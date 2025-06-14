package br.ufba.jnose.pages;

import br.ufba.jnose.WicketApplication;
import br.ufba.jnose.core.testsmelldetector.testsmell.AbstractSmell;
import br.ufba.jnose.pages.base.ImprimirPage;
import org.apache.wicket.markup.html.basic.Label;

import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;

public class SourcePage extends ImprimirPage {
    private static final long serialVersionUID = 1L;

    public SourcePage(AbstractSmell testSmell) {

        add(new Label("title", "Source: " + testSmell.getSmellName()));

        String posURI = testSmell.getClass().getCanonicalName();
        posURI = posURI.replace(".", File.separator);
        posURI = posURI + ".java";

        File fileSource = new File(WicketApplication.JNOSE_PATH + "/src/main/java/" + posURI);

        String sourceString = readLineByLineJava8(WicketApplication.JNOSE_PATH + "/src/main/java/" + posURI);

        add(new Label("source",sourceString).setEscapeModelStrings(false));
    }

    private static String readLineByLineJava8(String filePath) {
        StringBuilder contentBuilder = new StringBuilder();

        try (Stream<String> stream = Files.lines(Paths.get(filePath), StandardCharsets.UTF_8)) {
            stream.forEach(s -> contentBuilder.append(s).append("\n"));
        } catch (IOException e) {
            e.printStackTrace();
        }

        return contentBuilder.toString();
    }
}