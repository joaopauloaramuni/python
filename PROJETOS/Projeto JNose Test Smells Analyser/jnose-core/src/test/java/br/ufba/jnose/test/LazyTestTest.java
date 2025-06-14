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
import br.ufba.jnose.core.testsmelldetector.testsmell.smell.LazyTest;

public class LazyTestTest {

	public LazyTest lazyTest;
	FileInputStream fileInputStream;
	FileInputStream fileInputStream2;
	CompilationUnit compilationUnit;
	SmellyElement smellyElementList;
	
	@BeforeEach
	public void setUp() throws Exception {
		lazyTest = new LazyTest();
		fileInputStream = new FileInputStream(new File("src/test/java/br/ufba/jnose/test/fixtures/LazyFixture.java"));
		fileInputStream2 = new FileInputStream(new File("src/test/java/br/ufba/jnose/test/fixtures/LazyClassFixture.java"));
	}	
	
	@Test
	public void should_get_number_of_tests() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			CompilationUnit compilationUnit2 = JavaParser.parse(fileInputStream2);
			lazyTest.runAnalysis(compilationUnit,compilationUnit2,"LazyFixture","LazyClassFixture");
			ArrayList<SmellyElement> testes = lazyTest.list();
			
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
			CompilationUnit compilationUnit2 = JavaParser.parse(fileInputStream2);
			lazyTest.runAnalysis(compilationUnit,compilationUnit2,"LazyFixture","LazyClassFixture");
			ArrayList<SmellyElement> testes = lazyTest.list();
			
			assertTrue(testes.size() == 1);
			assertEquals(testes.get(0).getRange(),"33, 28");
			assertEquals(testes.get(0).getElementName(),"should_be_lazy_test_two, should_be_lazy_test");
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}

}
