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
import br.ufba.jnose.core.testsmelldetector.testsmell.smell.UnknownTest;

public class UnknownTestTest {
	
	public UnknownTest unknownTest;
	FileInputStream fileInputStream;
	CompilationUnit compilationUnit;
	SmellyElement smellyElementList;

	@BeforeEach
	public void setUp() throws Exception {
		unknownTest = new UnknownTest();
		fileInputStream = new FileInputStream(new File("src/test/java/br/ufba/jnose/test/fixtures/UnkwonFixture.java"));
	}
	
	@Test
	public void should_get_number_of_tests() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			unknownTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = unknownTest.list();
			
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
			unknownTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = unknownTest.list();
			
			assertTrue(testes.size() == 3);

			assertEquals(testes.get(0).getElementName(),"should_be_unknown_test");
			assertEquals(testes.get(0).getRange(),"13-16");

			assertEquals(testes.get(1).getElementName(),"should_be_unknown_test_1");
			assertEquals(testes.get(1).getRange(),"18-21");

			assertEquals(testes.get(2).getElementName(),"should_be_unknown_test_2");
			assertEquals(testes.get(2).getRange(),"23-26");
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}

}