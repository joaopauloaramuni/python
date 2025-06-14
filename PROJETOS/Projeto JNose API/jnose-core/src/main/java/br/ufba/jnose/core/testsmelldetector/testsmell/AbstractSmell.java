package br.ufba.jnose.core.testsmelldetector.testsmell;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;

import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;

public abstract class AbstractSmell {
    private final String smellName;
    protected final List<SmellyElement> smellyElementList;
    protected VoidVisitorAdapter<Void> classVisitor;

    public AbstractSmell(String smellName) {
        this.smellName = smellName;
        this.smellyElementList = new ArrayList<>();
    }

    /**
     * Returns the set of analyzed elements (i.e. test methods)
     */
    public List<SmellyElement> getSmellyElements(){return smellyElementList;}

    /**
     * Returns true if any of the elements has a smell
     */
    public boolean getHasSmell() {return smellyElementList.parallelStream().filter(x -> x.getHasSmell()).count() >= 1;}

    /**
     * Returns number of smell
     */
    public long getHasSmellCount() { return smellyElementList.parallelStream().filter(x -> x.getHasSmell()).count();}

    /**
     * Test Smell Name
     */
    public String getSmellName(){return smellName;}

    public abstract void runAnalysis(CompilationUnit testFileCompilationUnit,CompilationUnit productionFileCompilationUnit, String testFileName, String productionFileName) throws FileNotFoundException;

}
