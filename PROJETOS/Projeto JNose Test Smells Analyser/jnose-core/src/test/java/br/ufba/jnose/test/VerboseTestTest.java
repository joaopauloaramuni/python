package br.ufba.jnose.test;

import static org.junit.jupiter.api.Assertions.*;

import java.io.File;
import java.io.FileInputStream;
import java.util.ArrayList;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.github.javaparser.JavaParser;
import com.github.javaparser.ast.CompilationUnit;

import br.ufba.jnose.core.testsmelldetector.testsmell.SmellyElement;
import br.ufba.jnose.core.testsmelldetector.testsmell.smell.VerboseTest;

public class VerboseTestTest {

	public VerboseTest verboseTest;
	FileInputStream fileInputStream;
	CompilationUnit compilationUnit;
	SmellyElement smellyElementList;
	
	@BeforeEach
	public void setUp() throws Exception {
		verboseTest = new VerboseTest();
		fileInputStream = new FileInputStream(new File("src/test/java/br/ufba/jnose/test/fixtures/VerboseFixture.java"));
	}
	
	@Test
	public void should_get_number_of_tests() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			verboseTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = verboseTest.list();

			assertEquals(testes.size(), 3);
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}

	@Test
	public void should_get_smell_informations() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			verboseTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = verboseTest.list();
			
			assertEquals(testes.get(0).getRange(),"10-41");
			assertEquals(testes.get(0).getElementName(),"should_be_verbose_test_0");

			assertEquals(testes.get(1).getRange(),"43-74");
			assertEquals(testes.get(1).getElementName(),"should_be_verbose_test_1");

			assertEquals(testes.get(2).getRange(),"76-107");
			assertEquals(testes.get(2).getElementName(),"should_be_verbose_test_2");
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}
}
