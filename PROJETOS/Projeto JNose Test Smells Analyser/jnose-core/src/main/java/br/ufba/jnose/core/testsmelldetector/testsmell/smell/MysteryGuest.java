package br.ufba.jnose.core.testsmelldetector.testsmell.smell;

import br.ufba.jnose.core.testsmelldetector.testsmell.*;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.expr.AnnotationExpr;
import com.github.javaparser.ast.expr.NameExpr;
import com.github.javaparser.ast.expr.VariableDeclarationExpr;
import com.github.javaparser.ast.type.ClassOrInterfaceType;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;

import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * When a test uses external resources, such as a file containing test data, the test is no longer self contained.
 * Consequently, there is not enough information to understand the tested functionality, making it hard to use that test as documentation.
 * Moreover, using external resources introduces hidden dependencies: if some force changes or deletes such a resource, tests start failing.
 * Chances for this increase when more tests use the same resource.
 * A. van Deursen, L. Moonen, A. Bergh, G. Kok, “Refactoring Test Code”, Technical Report, CWI, 2001.
 */
public class MysteryGuest extends AbstractSmell {

    private ArrayList<MethodUsage> mysteryInstance;

    public MysteryGuest() {
        super("Mystery Guest");
        mysteryInstance = new ArrayList<>();
    }

    /**
     * Analyze the test file for test methods that use external resources
     */
    @Override
    public void runAnalysis(CompilationUnit testFileCompilationUnit, CompilationUnit productionFileCompilationUnit, String testFileName, String productionFileName) throws FileNotFoundException {
        classVisitor = new MysteryGuest.ClassVisitor();
        classVisitor.visit(testFileCompilationUnit, null);

        for (MethodUsage method : mysteryInstance) {
            TestMethod testClass = new TestMethod(method.getTestMethodName());
            testClass.setRange(method.getRange());
            testClass.setHasSmell(true);
            smellyElementList.add(testClass);
        }
    }

    public ArrayList<SmellyElement> list() {
        return (ArrayList<SmellyElement>) smellyElementList;
    }

    private class ClassVisitor extends VoidVisitorAdapter<Void> {
        final private List<String> mysteryTypes = new ArrayList<>(
                Arrays.asList(
                        "File",
                        "FileOutputStream",
                        "SQLiteOpenHelper",
                        "SQLiteDatabase",
                        "Cursor",
                        "Context",
                        "HttpClient",
                        "HttpResponse",
                        "HttpPost",
                        "HttpGet",
                        "SoapObject"
                ));
        private MethodDeclaration currentMethod = null;

        @Override
        public void visit(MethodDeclaration n, Void arg) {
            if (Util.isValidTestMethod(n)) {
                currentMethod = n;
                super.visit(n, arg);
                currentMethod = null;
            }
        }

        @Override
        public void visit(ClassOrInterfaceType n, Void arg) {
            if (mysteryTypes.contains(n.asString())) {
                MethodUsage methodUsage = new MethodUsage(currentMethod.getNameAsString(), "", currentMethod.getRange().get().begin.line + "-" + currentMethod.getRange().get().end.line);
                if(mysteryInstance.contains(methodUsage) == false){
                    mysteryInstance.add(methodUsage);
                }
            }
        }

    }
}
