package br.ufba.jnose.core.testsmelldetector.testsmell.smell;

import br.ufba.jnose.core.testsmelldetector.testsmell.MethodUsage;
import br.ufba.jnose.core.testsmelldetector.testsmell.SmellyElement;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.Modifier;
import com.github.javaparser.ast.body.*;
import com.github.javaparser.ast.expr.MethodCallExpr;
import com.github.javaparser.ast.expr.NameExpr;
import com.github.javaparser.ast.expr.ObjectCreationExpr;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import br.ufba.jnose.core.testsmelldetector.testsmell.AbstractSmell;
import br.ufba.jnose.core.testsmelldetector.testsmell.TestMethod;
import br.ufba.jnose.core.testsmelldetector.testsmell.Util;

import java.io.FileNotFoundException;
import java.util.*;
import java.util.stream.Collectors;

public class LazyTest extends AbstractSmell {
    private static final String TEST_FILE = "Test";
    private static final String PRODUCTION_FILE = "Production";
    private String productionClassName;
    private List<MethodDeclaration> productionMethods;
    private List<ConstructorDeclaration> constructorMethods;
    private HashMap<String,ArrayList<String>> calledMethodsLine = new HashMap<>();
    private HashMap<String,ArrayList<String>> calledMethodsName = new HashMap<>();
    private ArrayList<MethodUsage> instanceLazy;

    public LazyTest() {
        super("Lazy Test");
        productionMethods = new ArrayList<>();
        constructorMethods = new ArrayList<>();
        instanceLazy = new ArrayList<>();
    }

    /**
     * Analyze the test file for test methods that exhibit the 'Lazy Test' smell
     */
    @Override
    public void runAnalysis(CompilationUnit testFileCompilationUnit, CompilationUnit productionFileCompilationUnit, String testFileName, String productionFileName) throws FileNotFoundException {

        if (productionFileCompilationUnit == null)
            throw new FileNotFoundException();

        classVisitor = new LazyTest.ClassVisitor(PRODUCTION_FILE);
        classVisitor.visit(productionFileCompilationUnit, null);

        classVisitor = new LazyTest.ClassVisitor(TEST_FILE);
        classVisitor.visit(testFileCompilationUnit, null);

        for (MethodUsage method : instanceLazy) {
            TestMethod testClass = new TestMethod(method.getTestMethodName());
            testClass.setRange(method.getRange());
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
        private List<String> productionVariables = new ArrayList<>();
        private String fileType;

        public ClassVisitor(String type) {
            fileType = type;
        }

        @Override
        public void visit(ClassOrInterfaceDeclaration n, Void arg) {
            if (Objects.equals(fileType, PRODUCTION_FILE)) {
                productionClassName = n.getNameAsString();
            }
            super.visit(n, arg);

            ArrayList<String> resultado = new ArrayList<>();

            calledMethodsLine.forEach( (key, value ) -> { // forEach() também é novidade Java 8
                if(calledMethodsLine.get(key).size() > 1){
                    List<String> names = calledMethodsName.get(key).stream().distinct().collect(Collectors.toList());
                    if(names.size()>1) {
                        List<String> lines = calledMethodsLine.get(key).stream().distinct().collect(Collectors.toList());
                        instanceLazy.add(new MethodUsage(names.toString()
                                .replace("[", "").replace("]", ""),
                                "", lines.toString()
                                .replace("[", "").replace("]", "")));
                    }
                }
            } );
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

                    //reset values for next method
                    currentMethod = null;
                    productionVariables = new ArrayList<>();
                }
            } else { //collect a list of all public/protected members of the production class
                for (Modifier modifier : n.getModifiers()) {
                    if (modifier.name().toLowerCase().equals("public") || modifier.name().toLowerCase().equals("protected")) {
                        productionMethods.add(n);
                    }
                }
            }
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
            super.visit(n, arg);
            if (currentMethod != null) {
                if (productionMethods.stream().anyMatch(i -> i.getNameAsString().equals(n.getNameAsString()) &&
                        i.getParameters().size() == n.getArguments().size())) {
                    //calledProductionMethods.add(new MethodUsage(currentMethod.getNameAsString(), n.getNameAsString(),n.getRange().get().begin.line + "-" + n.getRange().get().end.line));
                    String valor = n.getNameAsString();
                    ArrayList<String> lines = new ArrayList<>();
                    ArrayList<String> names = new ArrayList<>();
                    lines.add(String.valueOf(n.getRange().get().begin.line));
                    if(!names.contains(currentMethod.getNameAsString())) {
                        names.add(currentMethod.getNameAsString());
                    }
                    if(!calledMethodsLine.containsKey(valor)) {
                        calledMethodsLine.put(valor, lines);
                        calledMethodsName.put(valor,names);
                    }
                    else {
                        lines.addAll(calledMethodsLine.get(valor));
                        names.addAll(calledMethodsName.get(valor));
                        calledMethodsLine.computeIfPresent(valor, (k, v) -> v = lines);
                        calledMethodsName.computeIfPresent(valor, (k, v) -> v = names);
                    }
                } else {
                    if (n.getScope().isPresent()) {
                        if (n.getScope().get() instanceof NameExpr) {
                            //checks if the scope of the method being called is either of production class (e.g. static method)
                            //or
                            ///if the scope matches a variable which, in turn, is of type of the production class
                            if (((NameExpr) n.getScope().get()).getNameAsString().equals(productionClassName) ||
                                    productionVariables.contains(((NameExpr) n.getScope().get()).getNameAsString())) {
                                //calledProductionMethods.add(new MethodUsage(currentMethod.getNameAsString(), n.getNameAsString(), n.getRange().get().begin.line + "-" + n.getRange().get().end.line));
                                String valor = n.getNameAsString();
                                ArrayList<String> lines = new ArrayList<>();
                                ArrayList<String> names = new ArrayList<>();
                                lines.add(String.valueOf(n.getRange().get().begin.line));
                                names.add(currentMethod.getNameAsString());
                                if(!names.contains(currentMethod.getNameAsString())) {
                                    names.add(currentMethod.getNameAsString());
                                }
                                if(!calledMethodsLine.containsKey(valor)) {
                                    calledMethodsLine.put(valor, lines);
                                    calledMethodsName.put(valor,names);
                                }
                                else {
                                    lines.addAll(calledMethodsLine.get(valor));
                                    names.addAll(calledMethodsName.get(valor));
                                    calledMethodsLine.computeIfPresent(valor, (k, v) -> v = lines);
                                    calledMethodsName.computeIfPresent(valor, (k, v) -> v = names);
                                }
                            }
                        }
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
                        ArrayList<String> lines = new ArrayList<>();
                        ArrayList<String> names = new ArrayList<>();
                        lines.add(String.valueOf(n.getRange().get().begin.line));
                        names.add(currentMethod.getNameAsString());
                        if(!names.contains(currentMethod.getNameAsString())) {
                            names.add(currentMethod.getNameAsString());
                        }
                        if(!calledMethodsLine.containsKey(valor)) {
                            calledMethodsLine.put(valor, lines);
                            calledMethodsName.put(valor,names);
                        }
                        else {
                            lines.addAll(calledMethodsLine.get(valor));
                            names.addAll(calledMethodsName.get(valor));
                            calledMethodsLine.computeIfPresent(valor, (k, v) -> v = lines);
                            calledMethodsName.computeIfPresent(valor, (k, v) -> v = names);
                        }
                    }
                }
            }
        }

        @Override
        public void visit(ConstructorDeclaration n, Void arg){
            constructorMethods.add(n);
        }

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
