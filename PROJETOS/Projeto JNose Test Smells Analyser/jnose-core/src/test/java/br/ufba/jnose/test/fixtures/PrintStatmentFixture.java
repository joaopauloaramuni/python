package br.ufba.jnose.test.fixtures;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class PrintStatmentFixture {

	@Before
	public void setUp() throws Exception {
	}

	@Test
	public void should_be_print_statement_one() {
		System.out.println("test with println");
	}
	
	@Test
	public void should_be_print_statement_two() {
		int a = 1;
		int b = 2;
		System.out.printf("test with printf = %d",(a + b));
	}
	
	@Test
	public void should_be_print_statement_three() {
		System.out.print("test with print");
	}

}
