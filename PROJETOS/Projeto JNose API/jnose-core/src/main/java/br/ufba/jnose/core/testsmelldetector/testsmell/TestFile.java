package br.ufba.jnose.core.testsmelldetector.testsmell;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class TestFile {
    private final String testFilePath;
    private final String productionFilePath;
    private List<AbstractSmell> testSmells;
    private Integer loc;
    private Integer qtdMethods;
    private String app;


    public String getProductionFilePath() {
        return productionFilePath;
    }

    public String getTestFilePath() {
        return testFilePath;
    }

    public List<AbstractSmell> getTestSmells() {
        return testSmells;
    }

    public TestFile(String app, String testFilePath, String productionFilePath, Integer loc, Integer qtdMethods) {
        this.app = app;
        this.testFilePath = testFilePath;
        this.productionFilePath = productionFilePath;
        this.testSmells = new ArrayList<>();
        this.loc = loc;
        this.qtdMethods = qtdMethods;
    }

    public void addSmell(AbstractSmell smell) {
        testSmells.add(smell);
    }

    public String getTestFileName() {
        int lastIndex = testFilePath.lastIndexOf(File.separator);
        return testFilePath.substring(lastIndex + 1, testFilePath.length());
    }

    public String getTestFileNameWithoutExtension() {
        int lastIndex = getTestFileName().lastIndexOf(".");
        return getTestFileName().substring(0, lastIndex);
    }

    public String getProductionFileNameWithoutExtension() {
        int lastIndex = getProductionFileName().lastIndexOf(".");
        if (lastIndex == -1)
            return "";
        return getProductionFileName().substring(0, lastIndex);
    }

    public String getProductionFileName() {
        int lastIndex = productionFilePath.lastIndexOf(File.separatorChar);
        if (lastIndex == -1)
            return "";
        return productionFilePath.substring(lastIndex + 1, productionFilePath.length());
    }

}