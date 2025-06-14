package br.ufba.jnose.core.testsmelldetector.testsmell;

import br.ufba.jnose.core.Config;
import br.ufba.jnose.core.testsmelldetector.testsmell.smell.*;
import com.github.javaparser.JavaParser;
import com.github.javaparser.ast.CompilationUnit;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class TestSmellDetector {

    private List<AbstractSmell> testSmells;

    private Config config;

    /**
     * Instantiates the various test smell analyzer classes and loads the objects into an List
     */
    public TestSmellDetector(Config config) {
        this.config = config;
        initializeSmells();
    }

    private void initializeSmells(){
        testSmells = new ArrayList<>();
        if(config.unknownTest()) testSmells.add(new UnknownTest());
        if(config.ignoredTest()) testSmells.add(new IgnoredTest());
        if(config.resourceOptimism()) testSmells.add(new ResourceOptimism());
        if(config.magicNumberTest()) testSmells.add(new MagicNumberTest());
        if(config.redundantAssertion()) testSmells.add(new RedundantAssertion());
        if(config.sensitiveEquality()) testSmells.add(new SensitiveEquality());
        if(config.verboseTest()) testSmells.add(new VerboseTest());
        if(config.sleepyTest()) testSmells.add(new SleepyTest());
        if(config.lazyTest()) testSmells.add(new LazyTest());
        if(config.duplicateAssert()) testSmells.add(new DuplicateAssert());
        if(config.eagerTest()) testSmells.add(new EagerTest());
        if(config.assertionRoulette()) testSmells.add(new AssertionRoulette());
        if(config.conditionalTestLogic()) testSmells.add(new ConditionalTestLogic());
        if(config.constructorInitialization()) testSmells.add(new ConstructorInitialization());
        if(config.defaultTest()) testSmells.add(new DefaultTest());
        if(config.emptyTest()) testSmells.add(new EmptyTest());
        if(config.exceptionCatchingThrowing()) testSmells.add(new ExceptionCatchingThrowing());
        if(config.generalFixture()) testSmells.add(new GeneralFixture());
        if(config.mysteryGuest()) testSmells.add(new MysteryGuest());
        if(config.printStatement()) testSmells.add(new PrintStatement());
        if(config.dependentTest())testSmells.add(new DependentTest());
    }

    /**
     * Factory method that provides a new instance of the TestSmellDetector
     *
     * @return new TestSmellDetector instance
     */
    public static TestSmellDetector createTestSmellDetector(Config config) {
        return new TestSmellDetector(config);
    }

    /**
     * Provides the names of the smells that are being checked for in the code
     *
     * @return list of smell names
     */
    public List<String> getTestSmellNames() {
        return testSmells.stream().map(AbstractSmell::getSmellName).collect(Collectors.toList());
    }

    /**
     * Loads the java source code file into an AST and then analyzes it for the existence of the different types of test smells
     */
    public TestFile detectSmells(TestFile testFile) throws IOException {
        CompilationUnit testFileCompilationUnit=null, productionFileCompilationUnit=null;
        FileInputStream testFileInputStream, productionFileInputStream;

        if(!testFile.getTestFilePath().isEmpty()) {
            testFileInputStream = new FileInputStream(testFile.getTestFilePath());
            //Linha que dar problema de memoria.
            testFileCompilationUnit = JavaParser.parse(testFileInputStream);
        }

        if(!testFile.getProductionFilePath().isEmpty()){
            productionFileInputStream = new FileInputStream(testFile.getProductionFilePath());
            productionFileCompilationUnit = JavaParser.parse(productionFileInputStream);
        }

        initializeSmells();

        for (AbstractSmell smell : testSmells) {
            try {
                smell.runAnalysis(testFileCompilationUnit, productionFileCompilationUnit,testFile.getTestFileNameWithoutExtension(),testFile.getProductionFileNameWithoutExtension());
            } catch (FileNotFoundException e) {
                testFile.addSmell(null);
                continue;
            }
            testFile.addSmell(smell);
        }

        return testFile;
    }

}
