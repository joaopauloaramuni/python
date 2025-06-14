package br.ufba.jnose.core.testsmelldetector.testsmell.smell;

import br.ufba.jnose.core.testsmelldetector.testsmell.MethodUsage;
import br.ufba.jnose.core.testsmelldetector.testsmell.SmellyElement;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.FieldDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.VariableDeclarator;
import com.github.javaparser.ast.expr.*;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import br.ufba.jnose.core.testsmelldetector.testsmell.AbstractSmell;
import br.ufba.jnose.core.testsmelldetector.testsmell.TestMethod;
import br.ufba.jnose.core.testsmelldetector.testsmell.Util;

import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;

public class ResourceOptimism extends AbstractSmell {

    private ArrayList<MethodUsage> instanceResource;

    public ResourceOptimism() {
        super("Resource Optimism");
        instanceResource = new ArrayList<> ();
    }

    /**
     * Analyze the test file for the 'ResourceOptimism' smell
     */
    @Override
    public void runAnalysis(CompilationUnit testFileCompilationUnit, CompilationUnit productionFileCompilationUnit, String testFileName, String productionFileName) throws FileNotFoundException {
        classVisitor = new ResourceOptimism.ClassVisitor();
        classVisitor.visit(testFileCompilationUnit, null);

        for (MethodUsage method : instanceResource) {
            TestMethod testClass = new TestMethod(method.getTestMethodName());
            testClass.setRange(method.getBlock());
//            testClass.addDataItem("begin", method.getBlock ());
//            testClass.addDataItem("end",method.getBlock ()); // [Remover]
            testClass.setHasSmell(true);
            smellyElementList.add(testClass);
        }
    }
    
    public ArrayList<SmellyElement> list(){
    	return (ArrayList<SmellyElement>) smellyElementList;
    }

    private class ClassVisitor extends VoidVisitorAdapter<Void> {
        private MethodDeclaration currentMethod = null;
        private int resourceOptimismCount = 0;
        private boolean hasSmell = false;
        private List<String> methodVariables = new ArrayList<>();
        private List<String> classVariables = new ArrayList<>();


        // examine all methods in the test class
        @Override
        public void visit(MethodDeclaration n, Void arg) {
            if (Util.isValidTestMethod(n) || Util.isValidSetupMethod(n)) {
                currentMethod = n;
                super.visit(n, arg);

                if(methodVariables.size() >= 1 || hasSmell==true){
                    instanceResource.add(new MethodUsage (n.getNameAsString ( ), "",n.getRange().get().begin.line + "-" + n.getRange().get().end.line));
                }

                //reset values for next method
                currentMethod = null;
                resourceOptimismCount = 0;
                hasSmell = false;
                methodVariables = new ArrayList<>();
            }
        }

        @Override
        public void visit(VariableDeclarationExpr n, Void arg) {
            if (currentMethod != null) {
                for (VariableDeclarator variableDeclarator : n.getVariables()) {
                    if (variableDeclarator.getType().equals("File")) {
                        methodVariables.add(variableDeclarator.getNameAsString());
                    }
                }
            }
            super.visit(n, arg);
        }

        @Override
        public void visit(ObjectCreationExpr n, Void arg) {
            if (currentMethod != null) {
                if (n.getParentNode().isPresent()) {
                    if (!(n.getParentNode().get() instanceof VariableDeclarator)) { // VariableDeclarator is handled in the override method
                        if (n.getType().asString().equals("File")) {
                            hasSmell = true;
                        }
                    }
                }
            }
            super.visit(n, arg);
        }

        @Override
        public void visit(VariableDeclarator n, Void arg) {
            if (currentMethod != null) {
                if (n.getType().asString().equals("File")) {
                    methodVariables.add(n.getNameAsString());
                }
            } else {
                if (n.getType().asString().equals("File")) {
                    classVariables.add(n.getNameAsString());
                }
            }
            super.visit(n, arg);
        }

        @Override
        public void visit(FieldDeclaration n, Void arg) {
            for (VariableDeclarator variableDeclarator : n.getVariables()) {
                if (variableDeclarator.getType().equals("File")) {
                    classVariables.add(variableDeclarator.getNameAsString());
                }
            }
            super.visit(n, arg);
        }


        @Override
        public void visit(MethodCallExpr n, Void arg) {
            super.visit(n, arg);
            if (currentMethod != null) {
                if (n.getNameAsString().equals("exists") ||
                        n.getNameAsString().equals("isFile") ||
                        n.getNameAsString().equals("notExists")) {
                    if (n.getScope().isPresent()) {
                        if(n.getScope().get() instanceof NameExpr) {
                            if (methodVariables.contains(((NameExpr) n.getScope().get()).getNameAsString())) {
                                methodVariables.remove(((NameExpr) n.getScope().get()).getNameAsString());
                            }
                        }
                    }
                }
            }
        }
    }
}


