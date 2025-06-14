package br.ufba.jnose.core.testsmelldetector.testsmell.smell;

import br.ufba.jnose.core.testsmelldetector.testsmell.MethodUsage;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.expr.BooleanLiteralExpr;
import com.github.javaparser.ast.expr.MethodCallExpr;
import com.github.javaparser.ast.expr.NullLiteralExpr;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import br.ufba.jnose.core.testsmelldetector.testsmell.AbstractSmell;
import br.ufba.jnose.core.testsmelldetector.testsmell.SmellyElement;
import br.ufba.jnose.core.testsmelldetector.testsmell.TestMethod;
import br.ufba.jnose.core.testsmelldetector.testsmell.Util;

import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;

/*
If a test method contains an assert statement that explicitly returns a true or false, the method is marked as smelly
 */
public class RedundantAssertion extends AbstractSmell {
	ArrayList<MethodUsage> methodPrints = null;
    
	public RedundantAssertion() {
        super("Redundant Assertion");
        methodPrints = new ArrayList<MethodUsage>(); //lista que guarda todos os metodos da classe
    }

    /**
     * Analyze the test file for test methods for multiple assert statements
     */
    @Override
    public void runAnalysis(CompilationUnit testFileCompilationUnit, CompilationUnit productionFileCompilationUnit, String testFileName, String productionFileName) throws FileNotFoundException {
        classVisitor = new RedundantAssertion.ClassVisitor();
        classVisitor.visit(testFileCompilationUnit, null);
        
        for (MethodUsage method : methodPrints) {
            TestMethod testClass = new TestMethod(method.getTestMethodName());
            testClass.setRange(method.getRange());
//            testClass.addDataItem("begin", method.getLine());
//            testClass.addDataItem("end",method.getLine()); // [Remover]
            testClass.setHasSmell(true);
            smellyElementList.add(testClass);
        }
    }
    
    public ArrayList<SmellyElement> list(){
    	return (ArrayList<SmellyElement>) smellyElementList;
    }

    /**
     * Returns the set of analyzed elements (i.e. test methods)
     */
    @Override
    public List<SmellyElement> getSmellyElements() {
        return smellyElementList;
    }

    private class ClassVisitor extends VoidVisitorAdapter<Void> {
        private MethodDeclaration currentMethod = null;
        private int redundantCount = 0;

        // examine all methods in the test class
        @Override
        public void visit(MethodDeclaration n, Void arg) {
            if (Util.isValidTestMethod(n)) {
                currentMethod = n;
                super.visit(n, arg);

                //reset values for next method
                currentMethod = null;
                redundantCount = 0;
            }
        }


        @Override
        public void visit(MethodCallExpr n, Void arg) {
            String argumentValue = null;

            super.visit(n, arg);
            if (currentMethod != null) {
                switch (n.getNameAsString()) {
                    case "assertTrue":
                    case "assertFalse":
                        if (n.getArguments().size() == 1 && n.getArgument(0) instanceof BooleanLiteralExpr) { // assertTrue(boolean condition) or assertFalse(boolean condition)
                            argumentValue = Boolean.toString(((BooleanLiteralExpr) n.getArgument(0)).getValue());
                        } else if (n.getArguments().size() == 2 && n.getArgument(1) instanceof BooleanLiteralExpr) { // assertTrue(java.lang.String message, boolean condition)  or assertFalse(java.lang.String message, boolean condition)
                            argumentValue = Boolean.toString(((BooleanLiteralExpr) n.getArgument(1)).getValue());
                        }

                        if (argumentValue != null && (argumentValue.toLowerCase().equals("true") || argumentValue.toLowerCase().equals("false"))) {
                            redundantCount++;
                            methodPrints.add(new MethodUsage(currentMethod.getNameAsString(), "",n.getRange().get().begin.line + "-" + n.getRange().get().end.line));
                        }
                    break;

                    case "assertNotNull":
                    case "assertNull":
                        if (n.getArguments().size() == 1 && n.getArgument(0) instanceof NullLiteralExpr) { // assertNotNull(java.lang.Object object) or assertNull(java.lang.Object object)
                            argumentValue = (((NullLiteralExpr) n.getArgument(0)).toString());
                        } else if (n.getArguments().size() == 2 && n.getArgument(1) instanceof NullLiteralExpr) { // assertNotNull(java.lang.String message, java.lang.Object object) or assertNull(java.lang.String message, java.lang.Object object)
                            argumentValue = (((NullLiteralExpr) n.getArgument(1)).toString());
                        }

                        if (argumentValue != null && (argumentValue.toLowerCase().equals("null"))) {
                            redundantCount++;
                            methodPrints.add(new MethodUsage(currentMethod.getNameAsString(), "",n.getRange().get().begin.line + "-" + n.getRange().get().end.line));
                        }
                    break;

                    default:
                        if (n.getNameAsString().startsWith("assert")) {
                            if (n.getArguments().size() == 2) { //e.g. assertArrayEquals(byte[] expecteds, byte[] actuals); assertEquals(long expected, long actual);
                                if (n.getArgument(0).equals(n.getArgument(1))) {
                                    redundantCount++;
                                    methodPrints.add(new MethodUsage(currentMethod.getNameAsString(), "",n.getRange().get().begin.line + "-" + n.getRange().get().end.line));
                                }
                            }
                            if (n.getArguments().size() == 3) { //e.g. assertArrayEquals(java.lang.String message, byte[] expecteds, byte[] actuals); assertEquals(java.lang.String message, long expected, long actual)
                                if (n.getArgument(1).equals(n.getArgument(2))) {
                                    redundantCount++;
                                    methodPrints.add(new MethodUsage(currentMethod.getNameAsString(), "",n.getRange().get().begin.line + "-" + n.getRange().get().end.line));
                                }
                            }
                        }
                    break;
                }
            }
        }
    }
}
