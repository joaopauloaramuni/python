package br.ufba.jnose.test.fixtures;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

/**
 * Occurs when a test method has multiple non-documented assertions. Multiple
 * assertion statements in a test method without a descriptive message impacts
 * readability/understandability/maintainability as it’s not possible to
 * understand the reason for the failure of the test.
 */
public class AssertionRouletteFixture {

	@Test
	public void should_be_assertion_roulette_0() {
		LazyClassFixture aux = new LazyClassFixture();
		assertEquals(aux.first_method(),"method One");
	}

	@Test
	public void should_be_assertion_roulette_1() {
		LazyClassFixture aux = new LazyClassFixture();
		assertEquals(aux.first_method(),"method One", "msg the method one");
	}


	@Test
	public void should_be_assertion_roulette_2() {
		LazyClassFixture aux = new LazyClassFixture();
		assertEquals(aux.first_method(),"method One");
		assertNotEquals(aux.second_method(),"method One");
	}

	@Test
	public void should_be_assertion_roulette_3() {
		LazyClassFixture aux = new LazyClassFixture();
		assertEquals(aux.first_method(),"method One");
		assertNotEquals(aux.second_method(),"method One", "msg the method one");
	}

	@Test
	public void should_be_assertion_roulette_4() {
		LazyClassFixture aux = new LazyClassFixture();
		assertEquals(aux.first_method(),"method One");
		assertNotEquals(aux.second_method(),"method One");
		assertNotEquals(aux.second_method(),"method One");
		assertNotEquals(aux.second_method(),"method One");
	}

}
