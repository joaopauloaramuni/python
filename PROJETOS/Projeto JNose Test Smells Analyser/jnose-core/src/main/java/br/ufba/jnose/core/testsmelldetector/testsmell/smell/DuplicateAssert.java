package br.ufba.jnose.core.testsmelldetector.testsmell.smell;

import br.ufba.jnose.core.testsmelldetector.testsmell.MethodUsage;
import br.ufba.jnose.core.testsmelldetector.testsmell.SmellyElement;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.expr.MethodCallExpr;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import br.ufba.jnose.core.testsmelldetector.testsmell.AbstractSmell;
import br.ufba.jnose.core.testsmelldetector.testsmell.TestMethod;
import br.ufba.jnose.core.testsmelldetector.testsmell.Util;

import java.io.FileNotFoundException;
import java.util.*;
import java.util.ArrayList;

public class DuplicateAssert extends AbstractSmell {

    private ArrayList<MethodUsage> instanceDuplicate;

    public DuplicateAssert() {
        super("Duplicate Assert");
        instanceDuplicate = new ArrayList<> (  );
    }
    public class DuplicateAssertStructure {

        String text;
        int line;
        boolean checked;

        public DuplicateAssertStructure(String text,int line) {
            super();
            this.text = text;
            this.line = line;
            this.checked = false;
        }

        public String getText() {
            return text;
        }

        public void setText(String text) {
            this.text = text;
        }

        public int getLine() {
            return line;
        }

        public void setLine(int line) {
            this.line = line;
        }

        public boolean isChecked() {
            return checked;
        }

        public void setChecked(boolean checked) {
            this.checked = checked;
        }
    }
    
    public ArrayList<SmellyElement> list(){
    	return (ArrayList<SmellyElement>) smellyElementList;
    }
    /**
     * Analyze the test file for test methods that have multiple assert statements with the same explanation message
     */
    @Override
    public void runAnalysis(CompilationUnit testFileCompilationUnit, CompilationUnit productionFileCompilationUnit, String testFileName, String productionFileName) throws FileNotFoundException {
        classVisitor = new DuplicateAssert.ClassVisitor();
        classVisitor.visit(testFileCompilationUnit, null);

        for (MethodUsage method : instanceDuplicate) {
            TestMethod testClass = new TestMethod(method.getTestMethodName());
            testClass.setRange(method.getRange());
//            testClass.addDataItem("begin", method.getRange ());
//            testClass.addDataItem("end", method.getRange ()); // [Remover]
            testClass.setHasSmell(true);
            smellyElementList.add(testClass);
        }
    }

    private class ClassVisitor extends VoidVisitorAdapter<Void> {
        private MethodDeclaration currentMethod = null;
        List<String> assertMessage = new ArrayList<>();
        List<String> assertMethod = new ArrayList<>();
        List<DuplicateAssertStructure> assertMethodDA = new ArrayList<>();
        ArrayList<String> rangeLines = new ArrayList<>();
//        String rangeLines = "";

        // examine all methods in the test class
        @Override
        public void visit(MethodDeclaration n, Void arg) {
            if (Util.isValidTestMethod(n)) {
                currentMethod = n;
//                rangeLines = "";
                super.visit(n, arg);

                /* *
                 * Identification of all duplicate occurrences within the method
                 * */
                List<DuplicateAssertStructure> teste = assertMethodDA;
                for (int i = 0; i < teste.size() ; i++ ) {
                    if (!teste.get(i).isChecked()) {
                        boolean hasSmell = false;
                        for (int j = i + 1; j < teste.size() ; j++ ) {
                            //Só compara com outros asserts, caso o objeto ainda não tenha sido identificado como outro DA
                            if ((!teste.get(j).isChecked()) && (teste.get(i).text.equals(teste.get(j).text))) {
                                if (!hasSmell) {
                                    rangeLines.add(String.valueOf(teste.get(i).line));
//                                    rangeLines = rangeLines + " , " + teste.get(i).line;
                                    teste.get(i).setChecked(true);
                                }
                                rangeLines.add(String.valueOf(teste.get(j).line));
//                                rangeLines = rangeLines + " , " + teste.get(i).line;
                                teste.get(j).setChecked(true);
                                hasSmell = true;
                            }
                        }
                        if (hasSmell) {
                            instanceDuplicate.add (new MethodUsage(currentMethod.getNameAsString(),"", rangeLines.toString().replace("[","").replace("]","")));
                            rangeLines.clear();
                        }
                    }
                }

                //reset values for next method
                currentMethod = null;
                assertMessage = new ArrayList<>();
                assertMethod = new ArrayList<>();
                assertMethodDA = new ArrayList<>();
            }
        }

        // examine the methods being called within the test method
        @Override
        public void visit(MethodCallExpr n, Void arg) {
            super.visit(n, arg);
            if (currentMethod != null) {
                // if the name of a method being called start with 'assert'
                // if the name of a method being called is an assertion and has 3 parameters
                if (n.getNameAsString().startsWith("assert") || n.getNameAsString().startsWith("fail")) {
                    assertMethod.add(n.toString());
                    assertMethodDA.add(new DuplicateAssertStructure(n.toString(), n.getRange().get().begin.line));
                    if (n.getArguments().size() == 4) {
                        assertMessage.add(n.getArgument(0).toString());
                    }
                    if (n.getArguments().size() == 3) {
                        assertMessage.add(n.getArgument(0).toString());
                    }
                    if (n.getArguments().size() == 2) {
                        assertMessage.add(n.getArgument(0).toString());
                    }
                    if (n.getArguments().size() == 1) {
                        assertMessage.add(n.getArgument(0).toString());
                    }
                }
            }
        }
    }
}

