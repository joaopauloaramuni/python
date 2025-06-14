package br.ufba.jnose.test;

import static org.junit.jupiter.api.Assertions.*;

import java.io.File;
import java.io.FileInputStream;
import java.util.ArrayList;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.github.javaparser.JavaParser;
import com.github.javaparser.ast.CompilationUnit;

import br.ufba.jnose.core.testsmelldetector.testsmell.SmellyElement;
import br.ufba.jnose.core.testsmelldetector.testsmell.smell.ConditionalTestLogic;

public class ConditionalTestLogicTest {

	public ConditionalTestLogic conditionalTest;
	FileInputStream fileInputStream;
	CompilationUnit compilationUnit;
	SmellyElement smellyElementList;
	
	@BeforeEach
	public void setUp() throws Exception {
		conditionalTest = new ConditionalTestLogic();
		fileInputStream = new FileInputStream(new File("src/test/java/br/ufba/jnose/test/fixtures/ConditionalFixture.java"));
	}
	
	@Test
	public void should_get_number_of_tests() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			conditionalTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = conditionalTest.list();
			
			assertTrue(testes.size() == 7);
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}

	@Test
	public void should_get_test_one_informations() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			conditionalTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = conditionalTest.list();
						
			assertEquals(testes.get(0).getElementName(),"should_be_conditional_one");
			assertEquals(testes.get(0).getRange(),"10-11");
			
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}
	
	@Test
	public void should_get_test_two_informations() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			conditionalTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = conditionalTest.list();

			
			assertEquals(testes.get(1).getElementName(),"should_be_conditional_two");
			assertEquals(testes.get(1).getRange(),"16-17");
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}

	@Test
	public void should_get_test_three_informations() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			conditionalTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = conditionalTest.list();
			
			assertEquals(testes.get(2).getElementName(),"should_be_conditional_three");
			assertEquals(testes.get(2).getRange(),"23-25");
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}
	
	@Test
	public void should_get_test_four_informations() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			conditionalTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = conditionalTest.list();
			
			assertEquals(testes.get(3).getElementName(),"should_be_conditional_four");
			assertEquals(testes.get(3).getRange(),"31-31");
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}
	
	@Test
	public void should_get_test_five_informations() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			conditionalTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = conditionalTest.list();
			
			assertEquals(testes.get(4).getElementName(),"should_be_conditional_five");
			assertEquals(testes.get(4).getRange(),"37-39");
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}
	
	@Test
	public void should_get_test_six_informations() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			conditionalTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = conditionalTest.list();
			
			assertEquals(testes.get(5).getElementName(),"should_be_conditional_six");
			assertEquals(testes.get(5).getRange(),"45-52");
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}
	
	@Test
	public void should_get_test_seven_informations() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			conditionalTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = conditionalTest.list();
			
			assertEquals(testes.get(6).getElementName(),"should_be_conditional_seven");
			assertEquals(testes.get(6).getRange(),"57-61");
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}

}
