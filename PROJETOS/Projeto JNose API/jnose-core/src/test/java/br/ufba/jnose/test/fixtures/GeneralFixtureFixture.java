package br.ufba.jnose.test.fixtures;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class GeneralFixtureFixture {

	@Before
	public void setUp() throws Exception {
		number1 = 1;
		number2 = 2;
	}
	
	int number1;
	int number2;
	public int out_setup = 0;
	
	@Test
	public void should_not_be_general_fixture(){
		assertEquals(number1, number2);  // uses both fields instantiated within the setUp method
	}

	@Test
	public void should_be_general_fixture(){
	    assertEquals("explanation", number1, 2); // uses only the number1 field
	}

}
