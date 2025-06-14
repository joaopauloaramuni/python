package br.ufba.jnose.test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;


import java.io.File;
import java.io.FileInputStream;
import java.util.ArrayList;

import org.junit.jupiter.api.*;

import com.github.javaparser.JavaParser;
import com.github.javaparser.ast.CompilationUnit;

import br.ufba.jnose.core.testsmelldetector.testsmell.SmellyElement;
import br.ufba.jnose.core.testsmelldetector.testsmell.smell.AssertionRoulette;

@DisplayName("Assertion Roulette Test")
public class AssertionRouletteTest {

	public AssertionRoulette assertionTest;
	FileInputStream fileInputStream;
	CompilationUnit compilationUnit;
	SmellyElement smellyElementList;
	

	@BeforeEach
	public void setUp() throws Exception {
		assertionTest = new AssertionRoulette();
		fileInputStream = new FileInputStream(new File("src/test/java/br/ufba/jnose/test/fixtures/AssertionRouletteFixture.java"));
	}
	
	@Test
	@DisplayName("should get number of tests")
	public void should_get_number_of_tests() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			assertionTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = assertionTest.list();
			
			assertEquals(4, testes.size());
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}
	
	@Test
	@DisplayName("should get test smells informations")
	public void should_get_test_smells_informations() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			assertionTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = assertionTest.list();

			assertEquals(testes.get(0).getRange(), "33-33");
			assertEquals(testes.get(1).getRange(), "47-47");
			assertEquals(testes.get(2).getRange(), "48-48");
			assertEquals(testes.get(3).getRange(), "49-49");

			assertEquals(testes.get(0).getElementName(),"should_be_assertion_roulette_2");
			assertEquals(testes.get(1).getElementName(),"should_be_assertion_roulette_4");
			assertEquals(testes.get(2).getElementName(),"should_be_assertion_roulette_4");
			assertEquals(testes.get(3).getElementName(),"should_be_assertion_roulette_4");
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}


}
