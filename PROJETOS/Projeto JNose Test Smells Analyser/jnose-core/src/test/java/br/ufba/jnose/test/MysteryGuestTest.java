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
import br.ufba.jnose.core.testsmelldetector.testsmell.smell.MysteryGuest;

public class MysteryGuestTest {

	public MysteryGuest mysteryTest;
	FileInputStream fileInputStream;

	@BeforeEach
	public void setUp() throws Exception {
		mysteryTest = new MysteryGuest();
		fileInputStream = new FileInputStream(new File("src/test/java/br/ufba/jnose/test/fixtures/MisteryGuestFixture.java"));
	}
	
	@Test
	public void should_get_number_of_tests() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			mysteryTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = mysteryTest.list();

//			for(SmellyElement element : testes){
//				System.out.println(element.getElementName() + " - " + element.getHasSmell() + " - " + element.getRange());
//			}
			
			assertEquals(testes.size(),5);
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}
	
	
	@Test
	public void should_get_smell_informations() {
		try{ 
			CompilationUnit compilationUnit = JavaParser.parse(fileInputStream);
			mysteryTest.runAnalysis(compilationUnit,new CompilationUnit(),"Aux","");
			ArrayList<SmellyElement> testes = mysteryTest.list();

			assertEquals(testes.get(0).getRange(), "14-17");
			assertEquals(testes.get(0).getElementName(),"should_be_Mistery_Guest");

			assertEquals(testes.get(1).getRange(), "19-22");
			assertEquals(testes.get(1).getElementName(),"should_be_Mistery_Guest2");

			assertEquals(testes.get(2).getRange(), "24-27");
			assertEquals(testes.get(2).getElementName(),"should_be_Mistery_Guest3");

			assertEquals(testes.get(3).getRange(), "29-32");
			assertEquals(testes.get(3).getElementName(),"should_be_Mistery_Guest4");

			assertEquals(testes.get(4).getRange(), "34-37");
			assertEquals(testes.get(4).getElementName(),"should_be_Mistery_Guest5");
		}
		catch (Exception e) {
	        e.printStackTrace();
	    }
	}

}

