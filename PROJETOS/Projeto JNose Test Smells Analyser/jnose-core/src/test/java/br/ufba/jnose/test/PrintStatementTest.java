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
import br.ufba.jnose.core.testsmelldetector.testsmell.smell.PrintStatement;

public class PrintStatementTest {
	
	public PrintStatement printTest;
	FileInputStream fileInputStream;
	CompilationUnit compilationUnit;
	SmellyElement smellyElementList;

	@BeforeEach
	public void setUp() throws Exception {
		printTest = new PrintStatement();
		fileInputStream = new FileInputStream(new File("src/test/java/br/ufba/jnose/test/fixtures/PrintStatmentFixture.java"));
	}
	
	@Test
	public void should_get_number_of_tests() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			printTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = printTest.list();
			
			assertTrue(testes.size() == 3);
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}
	
	@Test
	public void should_get_test_one_informations() { 
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			printTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = printTest.list();
			
			assertEquals(testes.get(0).getRange(),"16");
			assertEquals(testes.get(0).getElementName(),"should_be_print_statement_one");
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}
	
	@Test
	public void should_get_test_two_informations() { 
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			printTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = printTest.list();
			
			assertEquals(testes.get(1).getRange(),"23");
			assertEquals(testes.get(1).getElementName(),"should_be_print_statement_two");
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}


	@Test
	public void should_get_test_three_informations() { 
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			printTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = printTest.list();
	
			assertFalse(printTest.list().isEmpty());
			assertEquals(testes.get(2).getRange(),"28");
			assertEquals(testes.get(2).getElementName(),"should_be_print_statement_three");	
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}

}