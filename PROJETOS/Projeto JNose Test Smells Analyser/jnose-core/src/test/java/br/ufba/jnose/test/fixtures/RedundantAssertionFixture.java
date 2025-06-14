package br.ufba.jnose.test.fixtures;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class RedundantAssertionFixture {

	@Before
	public void setUp() throws Exception {
	}

	@Test
	public void should_be_redundant_assertion() {
	    assertEquals(true, true);
	}
	
	@Test
	public void should_be_redundant_assertion_two() {
	    assertEquals(false, false);
	}

}
