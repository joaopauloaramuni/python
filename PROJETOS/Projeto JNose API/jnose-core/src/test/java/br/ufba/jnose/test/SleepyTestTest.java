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
import br.ufba.jnose.core.testsmelldetector.testsmell.smell.SleepyTest;

public class SleepyTestTest {

	public SleepyTest sleepyTest;
	FileInputStream fileInputStream;
	CompilationUnit compilationUnit;
	SmellyElement smellyElementList;
	
	@BeforeEach
	public void setUp() throws Exception {
		sleepyTest = new SleepyTest();
		fileInputStream = new FileInputStream(new File("src/test/java/br/ufba/jnose/test/fixtures/SleepyFixture.java"));
	}	
	
	@Test
	public void should_get_number_of_tests() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			sleepyTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = sleepyTest.list();
			
			assertEquals(testes.size(), 4);
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}
	
	@Test
	public void should_get_smell_informations() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			sleepyTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = sleepyTest.list();
			
			assertEquals(testes.get(0).getRange(), "16-16");
			assertEquals(testes.get(0).getElementName(),"should_be_sleep_test");

			assertEquals(testes.get(1).getRange(), "21-21");
			assertEquals(testes.get(1).getElementName(),"should_be_sleep_test_1");

			assertEquals(testes.get(2).getRange(), "27-27");
			assertEquals(testes.get(2).getElementName(),"should_be_sleep_test_2");

			assertEquals(testes.get(3).getRange(), "28-28");
			assertEquals(testes.get(3).getElementName(),"should_be_sleep_test_2");
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}

}