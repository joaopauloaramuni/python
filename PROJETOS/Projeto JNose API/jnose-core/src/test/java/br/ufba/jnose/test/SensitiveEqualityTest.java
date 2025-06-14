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
import br.ufba.jnose.core.testsmelldetector.testsmell.smell.SensitiveEquality;

public class SensitiveEqualityTest {
	
	public SensitiveEquality sensitiveTest;
	FileInputStream fileInputStream;
	CompilationUnit compilationUnit;
	SmellyElement smellyElementList;

	@BeforeEach
	public void setUp() throws Exception {
		sensitiveTest = new SensitiveEquality();
		fileInputStream = new FileInputStream(new File("src/test/java/br/ufba/jnose/test/fixtures/SensitiveEqualityFixtureTest.java"));
	}	
	
	@Test
	public void should_get_number_of_tests() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			sensitiveTest.runAnalysis(compilationUnit,new CompilationUnit(),"SentiviveEqualityTest","");
			ArrayList<SmellyElement> testes = sensitiveTest.list();
			
			assertEquals(testes.size(), 2);
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}
	
	@Test
	public void should_get_smell_informations() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			sensitiveTest.runAnalysis(compilationUnit,new CompilationUnit(),"SentiviveEqualityTest","");
			ArrayList<SmellyElement> testes = sensitiveTest.list();
			
			assertEquals(testes.get(0).getRange(),"19-19");
			assertEquals(testes.get(0).getElementName(),"should_be_sensitive_equality");

			assertEquals(testes.get(1).getRange(),"25-25");
			assertEquals(testes.get(1).getElementName(),"should_be_sensitive_equality_1");
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}

}
