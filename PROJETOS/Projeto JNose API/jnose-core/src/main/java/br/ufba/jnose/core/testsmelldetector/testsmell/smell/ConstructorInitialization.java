package br.ufba.jnose.core.testsmelldetector.testsmell.smell;

import br.ufba.jnose.core.testsmelldetector.testsmell.MethodUsage;
import br.ufba.jnose.core.testsmelldetector.testsmell.SmellyElement;
import br.ufba.jnose.core.testsmelldetector.testsmell.TestMethod;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.ConstructorDeclaration;
import com.github.javaparser.ast.type.ClassOrInterfaceType;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import br.ufba.jnose.core.testsmelldetector.testsmell.AbstractSmell;

import java.io.FileNotFoundException;
import java.util.ArrayList;

/*
This class checks if the code file contains a Constructor. Ideally, the test suite should not have a constructor. Initialization of fields should be in the setUP() method
If this code detects the existence of a constructor, it sets the class as smelly
 */
public class ConstructorInitialization extends AbstractSmell {

    private String testFileName;
    private ArrayList<MethodUsage> instanceConstructor;

    public ConstructorInitialization() {
        super("Constructor Initialization");
        instanceConstructor = new ArrayList<>();
    }

    public ArrayList<SmellyElement> list(){
    	return (ArrayList<SmellyElement>) smellyElementList;
    }

    /**
     * Analyze the test file for Constructor Initialization smell
     */
    @Override
    public void runAnalysis(CompilationUnit testFileCompilationUnit,CompilationUnit productionFileCompilationUnit, String testFileName, String productionFileName) throws FileNotFoundException {
        this.testFileName = testFileName;
        classVisitor = new ConstructorInitialization.ClassVisitor();
        classVisitor.visit(testFileCompilationUnit, null);

        for (MethodUsage method : instanceConstructor) {
            TestMethod testClass = new TestMethod(method.getTestMethodName());
            testClass.setRange(method.getBlock());
//            testClass.addDataItem("begin", method.getBlock());
//            testClass.addDataItem("end", method.getBlock()); // [Remover]
            testClass.setHasSmell(true);
            smellyElementList.add(testClass);
        }
    }
    
    public ArrayList<SmellyElement> listTests(){
    	return (ArrayList<SmellyElement>) smellyElementList;
    }

    private class ClassVisitor extends VoidVisitorAdapter<Void> {
        boolean constructorAllowed=false;

        @Override
        public void visit(ClassOrInterfaceDeclaration n, Void arg) {
            for(int i=0;i<n.getExtendedTypes().size();i++){
                ClassOrInterfaceType node = n.getExtendedTypes().get(i);
                constructorAllowed = node.getNameAsString().equals("ActivityInstrumentationTestCase2");
            }
            super.visit(n, arg);
        }

        @Override
        public void visit(ConstructorDeclaration n, Void arg) {
            // This check is needed to handle java files that have multiple classes
            if(n.getNameAsString().equals(testFileName)) {
                if(!constructorAllowed) {
                    instanceConstructor.add(new MethodUsage(n.getNameAsString(), "",n.getRange().get().begin.line + "-" + n.getRange().get().end.line));
                }
            }
        }
    }
}
