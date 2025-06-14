package br.ufba.jnose.core.testsmelldetector.testsmell.smell;

import br.ufba.jnose.core.testsmelldetector.testsmell.*;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.expr.MethodCallExpr;
import com.github.javaparser.ast.expr.NameExpr;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;

import java.io.FileNotFoundException;
import java.util.ArrayList;

/*
Use of Thread.sleep() in test methods can possibly lead to unexpected results as the processing time of tasks on different devices/machines can be different. Use mock objects instead
This code marks a method as smelly if the method body calls Thread.sleep()
 */
public class SleepyTest extends AbstractSmell {

    private ArrayList<MethodUsage> spleepyInstance;

    public SleepyTest() {
        super("Sleepy Test");
        spleepyInstance = new ArrayList<>();
    }

    /**
     * Analyze the test file for test methods that use Thread.sleep()
     */
    @Override
    public void runAnalysis(CompilationUnit testFileCompilationUnit, CompilationUnit productionFileCompilationUnit, String testFileName, String productionFileName) throws FileNotFoundException {
        classVisitor = new SleepyTest.ClassVisitor();
        classVisitor.visit(testFileCompilationUnit, null);

        for (MethodUsage method : spleepyInstance) {
            TestMethod testClass = new TestMethod(method.getTestMethodName());
            testClass.setRange(method.getRange());
//            testClass.addDataItem("begin", method.getLine());
//            testClass.addDataItem("end", method.getLine()); // [Remover]
            testClass.setHasSmell(true);
            smellyElementList.add(testClass);
        }
    }
    
    public ArrayList<SmellyElement> list(){
    	return (ArrayList<SmellyElement>) smellyElementList;
    }

    private class ClassVisitor extends VoidVisitorAdapter<Void> {
        private MethodDeclaration currentMethod = null;
        private int sleepCount = 0;

        // examine all methods in the test class
        @Override
        public void visit(MethodDeclaration n, Void arg) {
            if (Util.isValidTestMethod(n)) {
                currentMethod = n;
                super.visit(n, arg);

                //reset values for next method
                currentMethod = null;
                sleepCount = 0;
            }
        }

        // examine the methods being called within the test method
        @Override
        public void visit(MethodCallExpr n, Void arg) {
            super.visit(n, arg);
            if (currentMethod != null) {
                // if the name of a method being called is 'sleep'
                if (n.getNameAsString().equals("sleep")) {
                    //check the scope of the method
                    if ((n.getScope().isPresent() && n.getScope().get() instanceof NameExpr)) {
                        //proceed only if the scope is "Thread"
                        if ((((NameExpr) n.getScope().get()).getNameAsString().equals("Thread"))) {
                            sleepCount++;
                            spleepyInstance.add(new MethodUsage(currentMethod.getNameAsString(), "", n.getRange().get().begin.line + "-" + n.getRange().get().end.line));
                        }
                    }
                }
            }
        }
    }
}
