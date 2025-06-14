package br.ufba.jnose.core.testsmelldetector.testsmell.smell;

import br.ufba.jnose.core.testsmelldetector.testsmell.*;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.NodeList;
import com.github.javaparser.ast.body.BodyDeclaration;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.FieldDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.expr.AssignExpr;
import com.github.javaparser.ast.expr.NameExpr;
import com.github.javaparser.ast.stmt.BlockStmt;
import com.github.javaparser.ast.stmt.ExpressionStmt;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;

import java.io.FileNotFoundException;
import java.util.*;

public class GeneralFixture extends AbstractSmell {

    List<MethodDeclaration> methodList;
    MethodDeclaration setupMethod;
    List<FieldDeclaration> fieldList;
    List<MethodUsage> setupFields;
    TestMethod testMethod;
    private List<MethodUsage> instaceGeneral;

    public GeneralFixture() {
        super("General Fixture");
        methodList = new ArrayList<>();
        fieldList = new ArrayList<>();
        setupFields = new ArrayList<>();
        instaceGeneral = new ArrayList<>();
    }

    @Override
    public void runAnalysis(CompilationUnit testFileCompilationUnit, CompilationUnit productionFileCompilationUnit, String testFileName, String productionFileName) throws FileNotFoundException {
        classVisitor = new GeneralFixture.ClassVisitor();
        classVisitor.visit(testFileCompilationUnit, null); //This call will populate the list of test methods and identify the setup method [visit(ClassOrInterfaceDeclaration n)]

        //Proceed with general fixture analysis if setup method exists
        if (setupMethod != null) {
            //Get all fields that are initialized in the setup method
            //The following code block will identify the class level variables (i.e. fields) that are initialized in the setup method
            // TODO: There has to be a better way to do this identification/check!
            Optional<BlockStmt> blockStmt = setupMethod.getBody();
            NodeList nodeList = blockStmt.get().getStatements();
            for (int i = 0; i < nodeList.size(); i++) {
                for (int j = 0; j < fieldList.size(); j++) {
                    for (int k = 0; k < fieldList.get(j).getVariables().size(); k++) {
                        if (nodeList.get(i) instanceof ExpressionStmt) {
                            ExpressionStmt expressionStmt = (ExpressionStmt) nodeList.get(i);
                            if (expressionStmt.getExpression() instanceof AssignExpr) {
                                AssignExpr assignExpr = (AssignExpr) expressionStmt.getExpression();
                                if (fieldList.get(j).getVariable(k).getNameAsString().equals(assignExpr.getTarget().toString())) {
                                    setupFields.add(new MethodUsage(setupMethod.getNameAsString(),
                                            assignExpr.getTarget().toString(),
                                            String.valueOf(assignExpr.getRange().get().begin.line)
                                            ));
                                }
                            }
                        }
                    }
                }
            }
        }

        for (MethodDeclaration method : methodList) {
            //This call will visit each test method to identify the list of variables the method contains [visit(MethodDeclaration n)]
            classVisitor.visit(method, null);
        }

        for (MethodUsage method : instaceGeneral) {
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
        private MethodDeclaration methodDeclaration = null;
        private MethodDeclaration currentMethod = null;
        private Set<String> fixtureCount = new HashSet<>();

        @Override
        public void visit(ClassOrInterfaceDeclaration n, Void arg) {
            NodeList<BodyDeclaration<?>> members = n.getMembers();
            for (int i = 0; i < members.size(); i++) {
                if (members.get(i) instanceof MethodDeclaration) {
                    methodDeclaration = (MethodDeclaration) members.get(i);

                    //Get a list of all test methods
                    if (Util.isValidTestMethod(methodDeclaration)) {
                        methodList.add(methodDeclaration);
                    }

                    //Get the setup method
                    if (Util.isValidSetupMethod(methodDeclaration)) {
                        //It should have a body
                        if (methodDeclaration.getBody().isPresent()) {
                            setupMethod = methodDeclaration;
                        }
                    }
                }

                //Get all fields in the class
                if (members.get(i) instanceof FieldDeclaration) {
                    fieldList.add((FieldDeclaration) members.get(i));
                }
            }
        }

        // examine all methods in the test class
        @Override
        public void visit(MethodDeclaration n, Void arg) {
            if (Util.isValidTestMethod(n)) {
                currentMethod = n;

                //call visit(NameExpr) for current method
                super.visit(n, arg);

                // verify against the setup fields and set to the testmehtod
                for (MethodUsage field : setupFields){
                    if (!fixtureCount.contains(field.getProductionMethodName())) {
                        if (!instaceGeneral.contains(field)) {
                            instaceGeneral.add(field);
                        }
                    }
                }
                fixtureCount = new HashSet();
                currentMethod = null;
            }
        }

        @Override
        public void visit(NameExpr n, Void arg) {
            if (currentMethod != null) {
               for (MethodUsage field : setupFields) {
                    if (field.getProductionMethodName().equals(n.getNameAsString())) {
                        if(!fixtureCount.contains(n.getNameAsString())){
                            fixtureCount.add(n.getNameAsString());
                        }
                    }
                }
            }
            super.visit(n, arg);
        }
    }
}
