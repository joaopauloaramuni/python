package br.ufba.jnose.core.testsmelldetector.testsmell.smell;

import br.ufba.jnose.core.testsmelldetector.testsmell.AbstractSmell;
import br.ufba.jnose.core.testsmelldetector.testsmell.MethodUsage;
import br.ufba.jnose.core.testsmelldetector.testsmell.SmellyElement;
import br.ufba.jnose.core.testsmelldetector.testsmell.TestMethod;
import br.ufba.jnose.core.testsmelldetector.testsmell.Util;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.Modifier;
import com.github.javaparser.ast.body.*;
import com.github.javaparser.ast.expr.MethodCallExpr;
import com.github.javaparser.ast.expr.NameExpr;
import com.github.javaparser.ast.expr.ObjectCreationExpr;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;

import java.io.FileNotFoundException;
import java.util.*;
import java.util.stream.Collectors;

public class EagerTest extends AbstractSmell {

    private static final String TEST_FILE = "Test";
    private static final String PRODUCTION_FILE = "Production";
    private String productionClassName;
    private List<MethodDeclaration> productionMethods;
    private List<ConstructorDeclaration> constructorMethods;
    private ArrayList<MethodUsage> instanceEager;

    public EagerTest() {
        super("Eager Test");
        productionMethods = new ArrayList<>();
        constructorMethods = new ArrayList<>();
        instanceEager = new ArrayList<>();
    }

    /**
     * Analyze the test file for test methods that exhibit the 'Eager Test' smell
     */
    @Override
    public void runAnalysis(CompilationUnit testFileCompilationUnit, CompilationUnit productionFileCompilationUnit, String testFileName, String productionFileName) throws FileNotFoundException {

        if (productionFileCompilationUnit == null)
            throw new FileNotFoundException();

        classVisitor = new EagerTest.ClassVisitor(PRODUCTION_FILE);
        classVisitor.visit(productionFileCompilationUnit, null);

        classVisitor = new EagerTest.ClassVisitor(TEST_FILE);
        classVisitor.visit(testFileCompilationUnit, null);

        for (MethodUsage method : instanceEager) {
            TestMethod testClass = new TestMethod(method.getTestMethodName());
            testClass.setRange(method.getRange());
//            testClass.addDataItem("begin", method.getRange ());
//            testClass.addDataItem("end", method.getRange ()); // [Remover]
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
        private MethodDeclaration currentMethod = null;
        TestMethod testMethod;
        private int eagerCount = 0;
        private List<String> productionVariables = new ArrayList<>();
        private HashMap<String,ArrayList<String>> calledMethods = new HashMap<>();
        private String fileType;
        ArrayList<String> rangeLines = new ArrayList<>();

        public ClassVisitor(String type) {
            fileType = type;
        }

        @Override
        public void visit(ClassOrInterfaceDeclaration n, Void arg) {
            if (Objects.equals(fileType, PRODUCTION_FILE)) {
                productionClassName = n.getNameAsString();
            }
            super.visit(n, arg);
        }

        @Override
        public void visit(EnumDeclaration n, Void arg) {
            if (Objects.equals(fileType, PRODUCTION_FILE)) {
                productionClassName = n.getNameAsString();
            }
            super.visit(n, arg);
        }

        /**
         * The purpose of this method is to 'visit' all test methods.
         */
        @Override
        public void visit(MethodDeclaration n, Void arg) {
            // ensure that this method is only executed for the test file
            if (Objects.equals(fileType, TEST_FILE)) {
                if (Util.isValidTestMethod(n)) {
                    currentMethod = n;
                    testMethod = new TestMethod(currentMethod.getNameAsString());
                    testMethod.setHasSmell(false); //default value is false (i.e. no smell)

                    super.visit(n, arg);
                    if(calledMethods.size()> 1){
                        ArrayList<String> resultado = new ArrayList<>();
                        for(Map.Entry entry:calledMethods.entrySet()){
                            resultado.addAll((Collection<? extends String>) entry.getValue());
                        }
                        List<String> deduped = resultado.stream().distinct().collect(Collectors.toList());
                        Collections.sort(deduped);
                        instanceEager.add(new MethodUsage(currentMethod.getNameAsString(),
                                "",deduped.toString()
                                .replace("[","").replace("]","")));
                    }

                    //reset values for next method
                    currentMethod = null;
                    eagerCount = 0;
                    productionVariables.clear();
                    calledMethods.clear();
                }
            } else { //collect a list of all public/protected members of the production class
                for (Modifier modifier : n.getModifiers()) {
                    if (modifier.name().toLowerCase().equals("public") || modifier.name().toLowerCase().equals("protected")) {
                        productionMethods.add(n);
                    }
                }
            }
        }

        @Override
        public void visit(ObjectCreationExpr n, Void arg) {
            super.visit(n, arg);
            if (currentMethod != null) {
                for (int i = 0; i < constructorMethods.size(); i++) {
                    if (constructorMethods.get(i).getName().asString().equals(n.getType().toString())) {
                        String valor = constructorMethods.get(i).getName().asString();
                        ArrayList<String> a = new ArrayList<>();
                        a.add(String.valueOf(n.getRange().get().begin.line));
                        if(!calledMethods.containsKey(valor)) {
                            calledMethods.put(valor, a); ;
                        }
                        else {
                            a.addAll(calledMethods.get(valor));
                            calledMethods.computeIfPresent(valor, (k, v) -> v = a);
                        }

                    }
                }
            }
        }
        @Override
        public void visit(ConstructorDeclaration n, Void arg){
            constructorMethods.add(n);
        }
        /**
         * The purpose of this method is to identify the production class methods that are called from the test method
         * When the parser encounters a method call:
         * 1) the method is contained in the productionMethods list
         * or
         * 2) the code will check the 'scope' of the called method
         * A match is made if the scope is either:
         * equal to the name of the production class (as in the case of a static method) or
         * if the scope is a variable that has been declared to be of type of the production class (i.e. contained in the 'productionVariables' list).
         */
        @Override
        public void visit(MethodCallExpr n, Void arg) {
            NameExpr nameExpr = null;
            if (currentMethod != null) {
                if ((productionMethods.stream().anyMatch(i -> i.getNameAsString().equals(n.getNameAsString()) &&
                        i.getParameters().size() == n.getArguments().size()))) {
                    String valor = n.getNameAsString();
                    ArrayList<String> a = new ArrayList<>();
                    a.add(String.valueOf(n.getRange().get().begin.line));
                    if(!calledMethods.containsKey(n.getNameAsString())) {
                        calledMethods.put(valor, a); ;
                    }
                    else {
                        a.addAll(calledMethods.get(n.getNameAsString()));
                        calledMethods.computeIfPresent(n.getNameAsString(), (k, v) -> v = a);
                    }
                }
                else {
                    if (n.getScope().isPresent()) {
                        //this if statement checks if the method is chained and gets the final scope
                        if ((n.getScope().get() instanceof MethodCallExpr)) {
                            getFinalScope(n);
                            nameExpr = tempNameExpr;
                        }
                        if (n.getScope().get() instanceof NameExpr) {
                            nameExpr = (NameExpr) n.getScope().get();
                        }

                        if (nameExpr != null) {
                            //checks if the scope of the method being called is either of production class (e.g. static method)
                            //or
                            ///if the scope matches a variable which, in turn, is of type of the production class
                            if (nameExpr.getNameAsString().equals(productionClassName) ||
                                    productionVariables.contains(nameExpr.getNameAsString())) {
                                String valor = nameExpr.getNameAsString();
                                ArrayList<String> a = new ArrayList<>();
                                a.add(String.valueOf(n.getRange().get().begin.line));
                                if(!calledMethods.containsKey(n.getNameAsString())) {
                                    calledMethods.put(valor, a);
                                }
                                else {
                                    a.addAll(calledMethods.get(n.getNameAsString()));
                                    calledMethods.computeIfPresent(n.getNameAsString(), (k, v) -> v = a);
                                }
                            }
                        }
                    }
                }
            }
            super.visit(n, arg);
        }


        private NameExpr tempNameExpr;

        /**
         * This method is utilized to obtain the scope of a chained method statement
         */
        private void getFinalScope(MethodCallExpr n) {
            if (n.getScope().isPresent()) {
                if ((n.getScope().get() instanceof MethodCallExpr)) {
                    getFinalScope((MethodCallExpr) n.getScope().get());
                } else if ((n.getScope().get() instanceof NameExpr)) {
                    tempNameExpr = ((NameExpr) n.getScope().get());
                }
            }
        }

//        /**
//         * The purpose of this method is to capture the names of all variables, declared in the method body, that are of type of the production class.
//         * The variable is captured as and when the code statement is parsed/evaluated by the parser
//         */
//        @Override
//        public void visit(VariableDeclarationExpr n, Void arg) {
//            if (currentMethod != null) {
//                for (int i = 0; i < n.getVariables().size(); i++) {
//                    if (productionClassName.equals(n.getVariable(i).getType().asString())) {
//                        productionVariables.add(n.getVariable(i).getNameAsString());
//                    }
//                }
//            }
//            super.visit(n, arg);
//        }

        @Override
        public void visit(VariableDeclarator n, Void arg) {
            if (Objects.equals(fileType, TEST_FILE)) {
                if (productionClassName.equals(n.getType().asString())) {
                    productionVariables.add(n.getNameAsString());
                }
            }
            super.visit(n, arg);
        }
    }
}