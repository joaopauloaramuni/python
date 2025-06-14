package br.ufba.jnose.core;

import br.ufba.jnose.core.testsmelldetector.testsmell.smell.VerboseTest;
import br.ufba.jnose.dto.*;
import br.ufba.jnose.core.testsmelldetector.testsmell.AbstractSmell;
import br.ufba.jnose.core.testsmelldetector.testsmell.SmellyElement;
import br.ufba.jnose.core.testsmelldetector.testsmell.TestFile;
import br.ufba.jnose.core.testsmelldetector.testsmell.TestSmellDetector;
import com.github.javaparser.JavaParser;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.ImportDeclaration;
import com.github.javaparser.ast.NodeList;
import com.github.javaparser.ast.PackageDeclaration;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.expr.AnnotationExpr;
import com.github.javaparser.metamodel.ClassOrInterfaceDeclarationMetaModel;

import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;
import java.util.concurrent.*;
import java.util.logging.Level;
import java.util.logging.Logger;

public class JNoseCore implements PropertyChangeListener{

    private ExecutorService threadpool;

    private final static Logger LOGGER = Logger.getLogger(JNoseCore.class.getName());

    private Config config;

    public static void main(String[] args) throws Exception {
        String directoryPath = "C:\\Users\\Tássio\\Desenvolvimento\\repo.git\\KTestSmells\\tmp\\commons-io";

        Config conf = new Config() {
            @Override
            public Boolean assertionRoulette() {
                return true;
            }
           

            @Override
            public Boolean conditionalTestLogic() {
                return true;
            }

            @Override
            public Boolean constructorInitialization() {
                return true;
            }

            @Override
            public Boolean defaultTest() {
                return true;
            }

            @Override
            public Boolean dependentTest() {
                return true;
            }

            @Override
            public Boolean duplicateAssert() {
                return true;
            }

            @Override
            public Boolean eagerTest() {
                return true;
            }

            @Override
            public Boolean emptyTest() {
                return true;
            }

            @Override
            public Boolean exceptionCatchingThrowing() {
                return true;
            }

            @Override
            public Boolean generalFixture() {
                return true;
            }

            @Override
            public Boolean mysteryGuest() {
                return true;
            }

            @Override
            public Boolean printStatement() {
                return true;
            }

            @Override
            public Boolean redundantAssertion() {
                return true;
            }

            @Override
            public Boolean sensitiveEquality() {
                return true;
            }

            @Override
            public Boolean verboseTest() {
                return true;
            }

            @Override
            public Boolean sleepyTest() {
                return true;
            }

            @Override
            public Boolean lazyTest() {
                return true;
            }

            @Override
            public Boolean unknownTest() {
                return true;
            }

            @Override
            public Boolean ignoredTest() {
                return true;
            }

            @Override
            public Boolean resourceOptimism() {
                return true;
            }

            @Override
            public Boolean magicNumberTest() {
                return true;
            }

            @Override
            public Integer maxStatements() {
                return 30;
            }
        };

        JNoseCore jNoseCore = new JNoseCore(conf, 3);

        List<TestClass> lista = jNoseCore.getFilesTest(directoryPath);

        for(TestClass testClass : lista){
            for (TestSmell testSmell : testClass.getListTestSmell()){
                System.out.println(
                            testClass.getPathFile() + ";" +
                            testClass.getProductionFile() + ";" +
                            testClass.getJunitVersion() + ";" +
                            testSmell.getName() + ";" +
                            testSmell.getMethod() + ";" +
                            testSmell.getRange()
                );
            }

//            System.out.println(testClass.getLineSumTestSmells());
        }

    }

    public JNoseCore(Config config, int numberThread) {
        threadpool = Executors.newFixedThreadPool(numberThread);
        this.config = config;
        VerboseTest.MAX_STATEMENTS = config.maxStatements();
    }

    public List<TestClass> getFilesTest(String directoryPath) throws Exception {
        LOGGER.log(Level.INFO, "getFilesTest: start");

        String projectName = directoryPath.substring(directoryPath.lastIndexOf(File.separatorChar) + 1, directoryPath.length());

        List<TestClass> files = new ArrayList<>();

        Path startDir = Paths.get(directoryPath);

        List<Future<List<TestClass>>> futures = new ArrayList<>();

        Files.walk(startDir)
                .filter(Files::isRegularFile)
                .forEach(filePath -> {
                    JNoseCallable jNoseCallable = new JNoseCallable(filePath, projectName, startDir, this);
                    Future<List<TestClass>> future = threadpool.submit(jNoseCallable);
                    futures.add(future);

//                    files.addAll(processarPath(filePath, projectName, startDir));
                });

        while (todosExecutados(futures)) {
//            System.out.println("A tarefa ainda não foi processada!");
            Thread.sleep(1); // sleep for 1 millisecond
        }


        for(Future<List<TestClass>> future : futures){
            files.addAll(future.get());
        }

        return files;
    }


    private Boolean todosExecutados(List<Future<List<TestClass>>> futures){
        for(Future future : futures){
            if(future.isDone() == false){
                return false;
            }
        }
        return true;
    }

    private List<TestClass> processarPath(Path filePath, String projectName, Path startDir){

        List<TestClass> files = new ArrayList<>();

        if (filePath.getFileName().toString().lastIndexOf(".") != -1) {
            String fileNameWithoutExtension = filePath.getFileName().toString().substring(0, filePath.getFileName().toString().lastIndexOf(".")).toLowerCase();

            if (filePath.toString().toLowerCase().endsWith(".java") && (
                    fileNameWithoutExtension.matches("^.*test\\d*$") ||
                    fileNameWithoutExtension.matches("^.*testcase\\d*$") ||
                            fileNameWithoutExtension.matches("^.*tests\\d*$") ||
                            fileNameWithoutExtension.matches("^test.*") ||
                            fileNameWithoutExtension.matches("^testcase.*") ||
                            fileNameWithoutExtension.matches("^tests.*"))) {

                Boolean testTrueFinal = fileNameWithoutExtension.matches("^.*test\\d*$");
                Boolean testCaseTrueFinal = fileNameWithoutExtension.matches("^.*testcase\\d*$");
                Boolean testsTrueFinal = fileNameWithoutExtension.matches("^.*tests\\d*$");

                Boolean testTrueInicio = fileNameWithoutExtension.matches("^test.*");
                Boolean testCaseTrueInicio = fileNameWithoutExtension.matches("^testcase.*");
                Boolean testsTrueInicio = fileNameWithoutExtension.matches("^tests.*");

                TestClass testClass = new TestClass();
                testClass.setProjectName(projectName);
                testClass.setPathFile(filePath.toString());

                if (isTestFile(testClass)) {
                    LOGGER.log(Level.INFO, "getFilesTest: " + testClass.getPathFile());
                    String productionFileName = "";
                    int index = 0;
                    if(testTrueInicio) index = 0;
                    if(testCaseTrueInicio) index = 0;
                    if(testsTrueInicio) index = 0;
                    if(testTrueFinal) index = testClass.getName().toLowerCase().lastIndexOf("test");
                    if(testCaseTrueFinal) index = testClass.getName().toLowerCase().lastIndexOf("testcase");
                    if(testsTrueFinal) index = testClass.getName().toLowerCase().lastIndexOf("tests");

                    if (index > 0) {
                        if(testTrueFinal)
                            productionFileName = testClass.getName().substring(0, testClass.getName().toLowerCase().lastIndexOf("test")) + ".java";
                        if(testCaseTrueFinal)
                            productionFileName = testClass.getName().substring(0, testClass.getName().toLowerCase().lastIndexOf("testcase")) + ".java";
                        if(testsTrueFinal)
                            productionFileName = testClass.getName().substring(0, testClass.getName().toLowerCase().lastIndexOf("tests")) + ".java";
                    }else{
                        if(testTrueInicio)
                            productionFileName = testClass.getName().substring(4, testClass.getName().length()) + ".java";
                        if(testCaseTrueInicio)
                            productionFileName = testClass.getName().substring(8, testClass.getName().length()) + ".java";
                        if(testsTrueInicio)
                            productionFileName = testClass.getName().substring(5, testClass.getName().length()) + ".java";
                    }
                    testClass.setProductionFile(getFileProduction(startDir.toString(), productionFileName));

                    if (!testClass.getProductionFile().isEmpty()) {
                        getTestSmells(testClass);
                        files.add(testClass);
                    }
                }
            }
        }
        return files;
    }


    public Boolean isTestFile(TestClass testClass) {
        LOGGER.log(Level.INFO, "isTestFile: start");

        Boolean isTestFile = false;
        try {
            FileInputStream fileInputStream = null;
            fileInputStream = new FileInputStream(new File(testClass.getPathFile()));
            CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
            testClass.setNumberLine(compilationUnit.getRange().get().end.line);
            detectJUnitVersion(compilationUnit.getImports(), testClass);
            List<NodeList<?>> nodeList = compilationUnit.getNodeLists();
            for (NodeList<?> node : nodeList) {
                isTestFile = flowClass(node, testClass);
            }

            if(testClass.getJunitVersion() != null && testClass.getJunitVersion() != TestClass.JunitVersion.None){
                isTestFile = true;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return isTestFile;
    }

    public void detectJUnitVersion(NodeList<ImportDeclaration> nodeList, TestClass testClass) {
        LOGGER.log(Level.INFO, "detectJUnitVersion: start");
        for (ImportDeclaration node : nodeList) {
            if (node.getNameAsString().contains("org.junit.jupiter")) {
                testClass.setJunitVersion(TestClass.JunitVersion.JUnit5);
                break;
            } else if (node.getNameAsString().contains("org.junit")) {
                testClass.setJunitVersion(TestClass.JunitVersion.JUnit4);
                break;
            } else if (node.getNameAsString().contains("junit.framework")) {
                testClass.setJunitVersion(TestClass.JunitVersion.JUnit3);
                break;
            } else {
                testClass.setJunitVersion(TestClass.JunitVersion.None);
            }
        }
    }


    public TestClass.JunitVersion getJUnitVersion(String directoryPath) {
        String projectName = directoryPath.substring(directoryPath.lastIndexOf(File.separatorChar) + 1, directoryPath.length());

        final br.ufba.jnose.dto.TestClass.JunitVersion[] jUnitVersion = new br.ufba.jnose.dto.TestClass.JunitVersion[1];

        jUnitVersion[0] = TestClass.JunitVersion.None;

        List<br.ufba.jnose.dto.TestClass> files = new ArrayList<>();
        Path startDir = Paths.get(directoryPath);
        try {
            Files.walk(startDir)
                    .filter(Files::isRegularFile)
                    .forEach(filePath -> {
                        if(filePath.getFileName().toString().toLowerCase().contains("loadtestcase")){
                            System.out.println("achei...");
                        }
                        if (filePath.getFileName().toString().lastIndexOf(".") != -1) {
                            String fileNameWithoutExtension = filePath.getFileName().toString().substring(0, filePath.getFileName().toString().lastIndexOf(".")).toLowerCase();
//                            if (filePath.toString().toLowerCase().endsWith(".java") && fileNameWithoutExtension.matches("^.*test\\d*$")) {
                            if (filePath.toString().toLowerCase().endsWith(".java") && (
                                    fileNameWithoutExtension.matches("^.*test\\d*$") ||
                                            fileNameWithoutExtension.matches("^.*testcase\\d*") ||
                                            fileNameWithoutExtension.matches("^.*tests\\d*$") ||
                                            fileNameWithoutExtension.matches("^test.*") ||
                                            fileNameWithoutExtension.matches("^testcase.*") ||
                                            fileNameWithoutExtension.matches("^tests.*"))) {
                                br.ufba.jnose.dto.TestClass testClass = new br.ufba.jnose.dto.TestClass();
                                testClass.setProjectName(projectName);
                                testClass.setPathFile(filePath.toString());
                                if (isTestFile(testClass)) {
                                    if(!testClass.getJunitVersion().equals(TestClass.JunitVersion.None)){
                                        jUnitVersion[0] = testClass.getJunitVersion();
                                    }
                                }
                            }
                        }
                    });
        } catch (IOException e) {
            e.printStackTrace();
        }
        return jUnitVersion[0];
    }

    private Boolean flowClass(NodeList<?> nodeList, TestClass testClass) {
        LOGGER.log(Level.INFO, "flowClass: start -> " + nodeList.toString());
        boolean isTestClass = false;
        for (Object node : nodeList) {
            if (node instanceof ClassOrInterfaceDeclaration) {
                ClassOrInterfaceDeclaration classAtual = ((ClassOrInterfaceDeclaration) node);
                testClass.setName(classAtual.getNameAsString());
                testClass.setFullName(classAtual.getName().toString());
                NodeList<?> nodeList_members = classAtual.getMembers();
                testClass.setNumberMethods(classAtual.getMembers().size());
                isTestClass = flowClass(nodeList_members, testClass);
                if(isTestClass)return true;
            } else if (node instanceof MethodDeclaration) {
                isTestClass = flowClass(((MethodDeclaration) node).getAnnotations(), testClass);
                if(isTestClass)return true;
            } else if (node instanceof AnnotationExpr) {
                if(((AnnotationExpr) node).getNameAsString().toLowerCase().contains("test")){
                    return true;
                }
            }
        }
        return isTestClass;
    }

    public String getFileProduction(String directoryPath, String productionFileName) {
        LOGGER.log(Level.INFO, "getFileProduction: start");
        final String[] retorno = {""};
        try {
            Path startDir = Paths.get(directoryPath);
            Files.walk(startDir)
                    .filter(Files::isRegularFile)
                    .forEach(filePath -> {
                        if (filePath.getFileName().toString().toLowerCase().equals(productionFileName.toLowerCase())) {
                            retorno[0] = filePath.toString();
                        }
                    });
        } catch (Exception e) {
            e.printStackTrace();
        }
        return retorno[0];
    }

    public void getTestSmells(TestClass testClass) {
        LOGGER.log(Level.INFO, "getTestSmells: start");

        TestSmellDetector testSmellDetector = TestSmellDetector.createTestSmellDetector(config);

        TestFile testFile = new TestFile(testClass.getProjectName(), testClass.getPathFile(), testClass.getProductionFile(), testClass.getNumberLine(), testClass.getNumberMethods());

        try {
            TestFile tempFile = testSmellDetector.detectSmells(testFile);
            for (AbstractSmell smell : tempFile.getTestSmells()) {
                smell.getSmellyElements();
                for (SmellyElement smellyElement : smell.getSmellyElements()) {
                    if (smellyElement.getHasSmell()) {
                        TestSmell testSmell = new TestSmell();
                        testSmell.setName(smell.getSmellName());
                        testSmell.setMethod(smellyElement.getElementName());
                        testSmell.setRange(smellyElement.getRange());
                        testSmell.setTestClass(testClass);
                        testClass.getListTestSmell().add(testSmell);
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        setLineSumTestSmells(testClass);
    }

    private void setLineSumTestSmells(TestClass testClass){

        Map<String,Integer> mapaSoma = new HashMap<>();

        List<TestSmell> listTestSmells = testClass.getListTestSmell();

        String[] lista = {"Unknown Test","IgnoredTest","Resource Optimism","Magic Number Test","Redundant Assertion","Sensitive Equality","Verbose Test","Sleepy Test","Lazy Test","Duplicate Assert","Eager Test","Assertion Roulette","Conditional Test Logic","Constructor Initialization","Default Test","EmptyTest","Exception Catching Throwing","General Fixture","Mystery Guest","Print Statement","Dependent Test"};
        for(String testsmellsName : lista){
            if(mapaSoma.get(testsmellsName) == null){
                mapaSoma.put(testsmellsName,0);
            }
        }

        for(TestSmell testsmells : listTestSmells){
            if(mapaSoma.get(testsmells.getName()) == null){
                mapaSoma.put(testsmells.getName(),0);
            }

            Integer valorAtual = mapaSoma.get(testsmells.getName());
            mapaSoma.put(testsmells.getName(),valorAtual+1);
        }

        testClass.setLineSumTestSmells(mapaSoma);
    }


    @Override
    public void propertyChange(PropertyChangeEvent propertyChangeEvent) {

    }
}

