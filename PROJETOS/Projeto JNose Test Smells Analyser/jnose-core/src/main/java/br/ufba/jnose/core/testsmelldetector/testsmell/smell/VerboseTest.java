package br.ufba.jnose.core.testsmelldetector.testsmell.smell;

import br.ufba.jnose.core.testsmelldetector.testsmell.*;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.expr.SimpleName;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;

import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;

/*
If a test methods contains a statements that exceeds a certain threshold, the method is marked as smelly
 */
public class VerboseTest extends AbstractSmell {

    private ArrayList<MethodUsage> instanceAbstract;
    public static int MAX_STATEMENTS = 30;
    CompilationUnit testFileCompilationUnit = null;
    public VerboseTest() {
        super("Verbose Test");
        instanceAbstract = new ArrayList<> (  );
    }

    /**
     * Analyze the test file for test methods for the 'Verbose Test' smell
     */
    @Override
    public void runAnalysis(CompilationUnit testFileCompilationUnit, CompilationUnit productionFileCompilationUnit, String testFileName, String productionFileName) throws FileNotFoundException {
        classVisitor = new VerboseTest.ClassVisitor();
        classVisitor.visit(testFileCompilationUnit, null);
        this.testFileCompilationUnit = testFileCompilationUnit;
        for (MethodUsage method : instanceAbstract) {
            TestMethod testClass = new TestMethod(method.getTestMethodName());
            testClass.setRange(method.getBlock());
//            testClass.addDataItem("begin", method.getBlock ());
//            testClass.addDataItem("end", method.getBlock ()); // [Remover]
            testClass.setHasSmell(true);
            smellyElementList.add(testClass);
        }
    }
    
    public ArrayList<SmellyElement> list(){
    	return (ArrayList<SmellyElement>) smellyElementList;
    }

    private class ClassVisitor extends VoidVisitorAdapter<Void> {
        //        final int MAX_STATEMENTS = 123;
        private MethodDeclaration currentMethod = null;
        private int verboseCount = 0;

        // examine all methods in the test class
        @Override
        public void visit(MethodDeclaration n, Void arg) {
            if (Util.isValidTestMethod(n)) {
                currentMethod = n;

                //method should not be abstract
                if (!currentMethod.isAbstract()) {
                    if (currentMethod.getBody().isPresent()) {
                        //get the total number of statements contained in the method
                        int inicio = currentMethod.getBody().get().getBegin().get().line;
                        int fim = currentMethod.getBody().get().getEnd().get().line;
                        if ((fim-inicio) >= MAX_STATEMENTS) {
                            verboseCount++;
                            instanceAbstract.add ( new MethodUsage (n.getNameAsString(), "",n.getRange().get().begin.line + "-" + n.getRange().get().end.line));
                        }
                    }
                }

                //reset values for next method
                currentMethod = null;
                verboseCount = 0;
            }
        }
    }
}
