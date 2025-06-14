package br.ufba.jnose.core.testsmelldetector.testsmell.smell;

import br.ufba.jnose.core.testsmelldetector.testsmell.MethodUsage;
import br.ufba.jnose.core.testsmelldetector.testsmell.SmellyElement;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.expr.ConditionalExpr;
import com.github.javaparser.ast.stmt.*;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import br.ufba.jnose.core.testsmelldetector.testsmell.AbstractSmell;
import br.ufba.jnose.core.testsmelldetector.testsmell.TestMethod;
import br.ufba.jnose.core.testsmelldetector.testsmell.Util;

import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;

/*
This class check a test method for the existence of loops and conditional statements in the methods body
 */
public class ConditionalTestLogic extends AbstractSmell {

    private List<MethodUsage> methodConditional;

    public ConditionalTestLogic() {
        super("Conditional Test Logic");
        methodConditional = new ArrayList<>();
    }

    /**
     * Analyze the test file for test methods that use conditional statements
     */
    @Override
    public void runAnalysis(CompilationUnit testFileCompilationUnit, CompilationUnit productionFileCompilationUnit, String testFileName, String productionFileName) throws FileNotFoundException {
        classVisitor = new ConditionalTestLogic.ClassVisitor();
        classVisitor.visit(testFileCompilationUnit, null);

        for (MethodUsage method : methodConditional) {
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
        private int conditionCount, ifCount, switchCount, forCount, foreachCount, whileCount, doCount = 0;
        TestMethod testMethod;

        // examine all methods in the test class
        @Override
        public void visit(MethodDeclaration n, Void arg) {
            if (Util.isValidTestMethod(n)) {
                currentMethod = n;
                testMethod = new TestMethod(n.getNameAsString());
                testMethod.setHasSmell(false); //default value is false (i.e. no smell)
                super.visit(n, arg);

                testMethod.setHasSmell(true);

//                testMethod.addDataItem("ConditionCount", String.valueOf(conditionCount));
//                testMethod.addDataItem("IfCount", String.valueOf(ifCount));
//                testMethod.addDataItem("SwitchCount", String.valueOf(switchCount));
//                testMethod.addDataItem("ForeachCount", String.valueOf(foreachCount));
//                testMethod.addDataItem("ForCount", String.valueOf(forCount));
//                testMethod.addDataItem("WhileCount", String.valueOf(whileCount));
//                testMethod.addDataItem("DoCount", String.valueOf(doCount));

                //reset values for next method
                currentMethod = null;
                conditionCount = 0;
                ifCount = 0;
                switchCount = 0;
                forCount = 0;
                foreachCount = 0;
                whileCount = 0;
                doCount = 0;
            }
        }


        @Override
        public void visit(IfStmt n, Void arg) {
            super.visit(n, arg);
            if (currentMethod != null) {
                ifCount++;
//                methodConditional.add(new MethodUsage(currentMethod.getNameAsString(), "",
//                        String.valueOf(n.getRange().get().begin.line),
//                        String.valueOf(n.getRange().get().end.line)));
                methodConditional.add(new MethodUsage(currentMethod.getNameAsString(), "", n.getRange().get().begin.line + "-" + n.getRange().get().end.line));
            }
        }

        @Override
        public void visit(SwitchStmt n, Void arg) {
            super.visit(n, arg);
            if (currentMethod != null) {
                switchCount++;
                methodConditional.add(new MethodUsage(currentMethod.getNameAsString(), "",n.getRange().get().begin.line + "-" + n.getRange().get().end.line));
            }
        }

        @Override
        public void visit(ConditionalExpr n, Void arg) {
            super.visit(n, arg);
            if (currentMethod != null) {
                conditionCount++;
                methodConditional.add(new MethodUsage(currentMethod.getNameAsString(), "",n.getRange().get().begin.line + "-" + n.getRange().get().end.line));
            }
        }

        @Override
        public void visit(ForStmt n, Void arg) {

            super.visit(n, arg);
            if (currentMethod != null) {
                forCount++;
                methodConditional.add(new MethodUsage(currentMethod.getNameAsString(), "", n.getRange().get().begin.line + "-" + n.getRange().get().end.line));
            }
        }

        @Override
        public void visit(ForeachStmt n, Void arg) {
            super.visit(n, arg);
            if (currentMethod != null) {
                foreachCount++;
                methodConditional.add(new MethodUsage(currentMethod.getNameAsString(), "",n.getRange().get().begin.line + "-" + n.getRange().get().end.line));
            }
        }

        @Override
        public void visit(WhileStmt n, Void arg) {
            super.visit(n, arg);
            if (currentMethod != null) {
                whileCount++;
                methodConditional.add(new MethodUsage(currentMethod.getNameAsString(), "",n.getRange().get().begin.line + "-" + n.getRange().get().end.line));
            }
        }

        @Override
        public void visit(DoStmt n, Void arg) {
            super.visit(n, arg);
            if (currentMethod != null) {
                doCount++;
                methodConditional.add(new MethodUsage(currentMethod.getNameAsString(), "",n.getRange().get().begin.line + "-" + n.getRange().get().end.line));
            }
        }
    }
}
