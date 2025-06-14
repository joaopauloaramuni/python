package br.ufba.jnose.core.testsmelldetector.testsmell.smell;

import br.ufba.jnose.core.testsmelldetector.testsmell.MethodUsage;
import br.ufba.jnose.core.testsmelldetector.testsmell.SmellyElement;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import br.ufba.jnose.core.testsmelldetector.testsmell.AbstractSmell;
import br.ufba.jnose.core.testsmelldetector.testsmell.TestMethod;
import br.ufba.jnose.core.testsmelldetector.testsmell.Util;

import java.io.FileNotFoundException;
import java.util.ArrayList;

/**
 * This class checks if a test method is empty (i.e. the method does not contain statements in its body)
 * If the the number of statements in the body is 0, then the method is smelly
 */
public class EmptyTest extends AbstractSmell {

    private ArrayList<MethodUsage> instanceEmpty;

    public EmptyTest() {
        super("EmptyTest");
        instanceEmpty = new ArrayList<>();
    }

    /**
     * Analyze the test file for test methods that are empty (i.e. no method body)
     */
    @Override
    public void runAnalysis(CompilationUnit testFileCompilationUnit, CompilationUnit productionFileCompilationUnit, String testFileName, String productionFileName) throws FileNotFoundException {
        classVisitor = new EmptyTest.ClassVisitor();
        classVisitor.visit(testFileCompilationUnit, null);

        for (MethodUsage method : instanceEmpty) {
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

    /**
     * Visitor class
     */
    private class ClassVisitor extends VoidVisitorAdapter<Void> {
        /**
         * The purpose of this method is to 'visit' all test methods in the test file
         */
        @Override
        public void visit(MethodDeclaration n, Void arg) {
            if (Util.isValidTestMethod(n)) {

                //method should not be abstract
                if (!n.isAbstract()) {
                    if (n.getBody().isPresent()) {
                        //get the total number of statements contained in the method
                        if (n.getBody().get().getStatements().size() == 0) {
                            instanceEmpty.add(new MethodUsage(n.getNameAsString(),"",n.getRange().get().begin.line + "-" + n.getRange().get().end.line));
                        }
                    }
                }
            }
        }
    }
}
