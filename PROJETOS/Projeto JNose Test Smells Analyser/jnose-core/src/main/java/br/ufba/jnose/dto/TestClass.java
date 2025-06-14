package br.ufba.jnose.dto;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class TestClass implements Serializable {
    private static final long serialVersionUID = 1L;

    private String projectName;
    private String pathFile;
    private String name;

    private String fullName;
    private Integer numberMethods;
    private Integer numberLine;
    private String productionFile;
    private List<TestSmell> listTestSmell = new ArrayList<>();
    private JunitVersion junitVersion;
    private Map<String,Integer> lineSumTestSmells;

    public enum JunitVersion{None, JUnit3, JUnit4, JUnit5}

    public Map<String, Integer> getLineSumTestSmells() {
        return lineSumTestSmells;
    }

    public void setLineSumTestSmells(Map<String, Integer> lineSumTestSmells) {
        this.lineSumTestSmells = lineSumTestSmells;
    }

    public String getProjectName() {
        return projectName;
    }

    public void setProjectName(String projectName) {
        this.projectName = projectName;
    }

    public String getPathFile() {
        return pathFile;
    }

    public void setPathFile(String pathFile) {
        this.pathFile = pathFile;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getNumberMethods() {
        return numberMethods;
    }

    public void setNumberMethods(Integer numberMethods) {
        this.numberMethods = numberMethods;
    }

    public Integer getNumberLine() {
        return numberLine;
    }

    public void setNumberLine(Integer numberLine) {
        this.numberLine = numberLine;
    }

    public String getProductionFile() {
        return productionFile;
    }

    public void setProductionFile(String productionFile) {
        this.productionFile = productionFile;
    }

    public List<TestSmell> getListTestSmell() {
        return listTestSmell;
    }

    public void setListTestSmell(List<TestSmell> listTestSmell) {
        this.listTestSmell = listTestSmell;
    }

    public JunitVersion getJunitVersion() {
        return junitVersion;
    }

    public void setJunitVersion(JunitVersion junitVersion) {
        this.junitVersion = junitVersion;
    }

    public String getFullName() {
        return fullName;
    }

    public void setFullName(String fullName) {
        this.fullName = fullName;
    }

    @Override
    public String toString() {
        return "TestClass{" +
                "projectName=" + projectName +
                "pathFile=" + pathFile +
                ", name='" + name + '\'' +
                ", numberMethods=" + numberMethods +
                ", numberLine=" + numberLine +
                ", junitVersion='" + junitVersion + '\'' +
                ", productionFile='" + productionFile + '\'' +
                ", listTestSmell=" + listTestSmell +
                '}';
    }
}
