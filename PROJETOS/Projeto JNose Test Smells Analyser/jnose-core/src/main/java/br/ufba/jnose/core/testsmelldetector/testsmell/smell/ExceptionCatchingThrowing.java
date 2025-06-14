package br.ufba.jnose.core.testsmelldetector.testsmell.smell;

import br.ufba.jnose.core.testsmelldetector.testsmell.*;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.stmt.TryStmt;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;

import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;

/*
This class checks if test methods in the class either catch or throw exceptions. Use Junit's exception handling to automatically pass/fail the test
If this code detects the existence of a catch block or a throw statement in the methods body, the method is marked as smelly
 */
public class ExceptionCatchingThrowing extends AbstractSmell {

    private List<MethodUsage> methodExceptions;
    public ExceptionCatchingThrowing() {
        super("Exception Catching Throwing");
        methodExceptions = new ArrayList<>();
    }

    /**
     * Analyze the test file for test methods that have exception handling
     */
    @Override
    public void runAnalysis(CompilationUnit testFileCompilationUnit, CompilationUnit productionFileCompilationUnit, String testFileName, String productionFileName) throws FileNotFoundException {
        classVisitor = new ExceptionCatchingThrowing.ClassVisitor();
        classVisitor.visit(testFileCompilationUnit, null);

        for (MethodUsage method : methodExceptions) {
            TestMethod testClass = new TestMethod(method.getTestMethodName());
            testClass.setRange(method.getBlock());
//            testClass.addDataItem("begin", method.getBlock());
//            testClass.addDataItem("end", method.getBlock()); // [Remover]
            testClass.setHasSmell(true);
            smellyElementList.add(testClass);
        }
    }
    
    public ArrayList<SmellyElement> list(){
    	return (ArrayList<SmellyElement>) smellyElementList;
    }

    private class ClassVisitor extends VoidVisitorAdapter<Void> {
        private MethodDeclaration currentMethod = null;

        // examine all methods in the test class
        @Override
        public void visit(MethodDeclaration n, Void arg) {
            if (Util.isValidTestMethod(n)) {
                currentMethod = n;
                super.visit(n, arg);

                //reset values for next method
                currentMethod = null;
            }
        }

        @Override
        public void visit(TryStmt n, Void arg) {
            methodExceptions.add(new MethodUsage(currentMethod.getNameAsString(), "",n.getRange().get().begin.line + "-" + n.getRange().get().end.line));
        }
    }
}