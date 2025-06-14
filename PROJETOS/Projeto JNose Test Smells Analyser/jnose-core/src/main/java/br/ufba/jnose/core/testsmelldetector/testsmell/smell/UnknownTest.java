package br.ufba.jnose.core.testsmelldetector.testsmell.smell;

import br.ufba.jnose.core.testsmelldetector.testsmell.*;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.NodeList;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.expr.AnnotationExpr;
import com.github.javaparser.ast.expr.MemberValuePair;
import com.github.javaparser.ast.expr.MethodCallExpr;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;

import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class UnknownTest extends AbstractSmell {

    private ArrayList<MethodUsage> instanceUnkNown;

    public UnknownTest() {
        super("Unknown Test");
        instanceUnkNown = new ArrayList<> ();
    }

    /**
     * Analyze the test file for test methods that do not have assert statement or exceptions
     */
    @Override
    public void runAnalysis(CompilationUnit testFileCompilationUnit, CompilationUnit productionFileCompilationUnit, String testFileName, String productionFileName) throws FileNotFoundException {
        classVisitor = new UnknownTest.ClassVisitor();
        classVisitor.visit(testFileCompilationUnit, null);

        for (MethodUsage method : instanceUnkNown) {
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
        private MethodDeclaration currentMethod = null;
        List<String> assertMessage = new ArrayList<>();
        boolean hasAssert = false;
        boolean hasExceptionAnnotation = false;


        // examine all methods in the test class
        @Override
        public void visit(MethodDeclaration n, Void arg) {
            if (Util.isValidTestMethod(n) && n.getBody().get().getStatements().size() >0) {
                Optional<AnnotationExpr> assertAnnotation = n.getAnnotationByName("Test");
                if (assertAnnotation.isPresent()) {
                    for (int i = 0; i < assertAnnotation.get().getNodeLists().size(); i++) {
                        NodeList<?> c = assertAnnotation.get().getNodeLists().get(i);
                        for (int j = 0; j < c.size(); j++)
                            if (c.get(j) instanceof MemberValuePair) {
                                if (((MemberValuePair) c.get(j)).getName().equals("expected") && ((MemberValuePair) c.get(j)).getValue().toString().contains("Exception"))
                                    ;
                                hasExceptionAnnotation = true;
                            }
                    }
                }
                currentMethod = n;
                super.visit(n, arg);

                // if there are duplicate messages, then the smell exists
                if (!hasAssert && !hasExceptionAnnotation)
                    instanceUnkNown.add(new MethodUsage(n.getNameAsString(), "",n.getRange().get().begin.line + "-" + n.getRange().get().end.line));

                //reset values for next method
                currentMethod = null;
                assertMessage = new ArrayList<>();
                hasAssert = false;
            }
        }


        // examine the methods being called within the test method
        @Override
        public void visit(MethodCallExpr n, Void arg) {
            super.visit(n, arg);
            if (currentMethod != null) {
                // if the name of a method being called start with 'assert'
                if (n.getNameAsString().startsWith(("assert"))) {
                    hasAssert = true;
                }
                // if the name of a method being called is 'fail'
                else if (n.getNameAsString().equals("fail")) {
                    hasAssert = true;
                }

            }
        }

    }
}

