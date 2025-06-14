package br.ufba.jnose.test.fixtures;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class EagerFixture {

	@Test
	public void should_be_eager_test() {
		LazyClassFixture aux = new LazyClassFixture();
		assertEquals(aux.first_method(),"method One");
		assertNotEquals(aux.second_method(),"method One");	
	}
}
