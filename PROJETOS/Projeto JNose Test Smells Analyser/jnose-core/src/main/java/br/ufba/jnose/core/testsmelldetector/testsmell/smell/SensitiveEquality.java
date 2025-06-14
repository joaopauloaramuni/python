package br.ufba.jnose.core.testsmelldetector.testsmell.smell;

import br.ufba.jnose.core.testsmelldetector.testsmell.MethodUsage;
import br.ufba.jnose.core.testsmelldetector.testsmell.SmellyElement;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.expr.Expression;
import com.github.javaparser.ast.expr.MethodCallExpr;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import br.ufba.jnose.core.testsmelldetector.testsmell.AbstractSmell;
import br.ufba.jnose.core.testsmelldetector.testsmell.TestMethod;
import br.ufba.jnose.core.testsmelldetector.testsmell.Util;

import java.io.FileNotFoundException;
import java.util.ArrayList;

public class SensitiveEquality extends AbstractSmell {
	ArrayList<MethodUsage> methodSensitiveEquality = null;
	
    public SensitiveEquality() {
        super("Sensitive Equality");
        methodSensitiveEquality = new ArrayList<MethodUsage>();
    }

    /**
     * Analyze the test file for test methods the 'Sensitive Equality' smell
     */
    @Override
    public void runAnalysis(CompilationUnit testFileCompilationUnit, CompilationUnit productionFileCompilationUnit, String testFileName, String productionFileName) throws FileNotFoundException {
        classVisitor = new SensitiveEquality.ClassVisitor();
        classVisitor.visit(testFileCompilationUnit, null);
        
        for (MethodUsage method : methodSensitiveEquality) {
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

    private class ClassVisitor extends VoidVisitorAdapter<Void> {
        private MethodDeclaration currentMethod = null;
        private int sensitiveCount = 0;

        // examine all methods in the test class
        @Override
        public void visit(MethodDeclaration n, Void arg) {
            if (Util.isValidTestMethod(n)) {
                currentMethod = n;
                super.visit(n, arg);

                //reset values for next method
                currentMethod = null;
                sensitiveCount = 0;
            }
        }

        // examine the methods being called within the test method
        @Override
        public void visit(MethodCallExpr n, Void arg) {
            super.visit(n, arg);
            if (currentMethod != null) {
                // if the name of a method being called start with 'assert'
                if (n.getNameAsString().startsWith(("assert"))) {
                    // assert methods that contain toString
                    for (Expression argument : n.getArguments()) {
                        if (argument.toString().contains("toString")) {
                            sensitiveCount++;
                            methodSensitiveEquality.add(new MethodUsage(currentMethod.getNameAsString(), "",n.getRange().get().begin.line + "-" + n.getRange().get().end.line));
                        }
                    }
                }
                // if the name of a method being called is 'fail' \/ added validation to jUnit3 fail cases
                else if (n.getNameAsString().equals("fail") || n.getNameAsString().equals("failNotEquals") ||
                		 n.getNameAsString().equals("failSame") || n.getNameAsString().equals("failNotSame"))  {
                    // fail methods that contain toString
                    for (Expression argument : n.getArguments()) {
                        if (argument.toString().contains("toString")) {
                            sensitiveCount++;
                            methodSensitiveEquality.add(new MethodUsage(currentMethod.getNameAsString(), "",n.getRange().get().begin.line + "-" + n.getRange().get().end.line));
                        }
                    }
                }
            }
        }
    }
}
