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
import br.ufba.jnose.core.testsmelldetector.testsmell.smell.IgnoredTest;

public class IgnoredTestTest {
	
	public IgnoredTest ignoredTest;
	FileInputStream fileInputStream;
	CompilationUnit compilationUnit;
	SmellyElement smellyElementList;

	@BeforeEach
	public void setUp() throws Exception {
		ignoredTest = new IgnoredTest();
		fileInputStream = new FileInputStream(new File("src/test/java/br/ufba/jnose/test/fixtures/IgnoredFixture.java"));
	}
	
	@Test
	public void should_get_number_of_tests() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			ignoredTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = ignoredTest.list();
			
			
			assertTrue(testes.size() == 1);
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}

	@Test
	public void should_get_smells() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			ignoredTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = ignoredTest.list();
			
			assertEquals(testes.get(0).getRange(),"15-18");
			assertEquals(testes.get(0).getElementName(),"should_be_ignored_test");
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}

}