package br.ufba.jnose.test.fixtures;

import static org.junit.Assert.*;

import java.io.File;
import java.io.FileInputStream;

import org.junit.Before;
import org.junit.Test;

import br.ufba.jnose.core.testsmelldetector.testsmell.SmellyElement;
import br.ufba.jnose.core.testsmelldetector.testsmell.smell.LazyTest;

public class LazyFixture {
	
	public LazyFixture() {
	}
	
	LazyClassFixture lazy;
	
	@Before
	public void setUp() throws Exception {
		lazy = new LazyClassFixture();
	}
	
	@Test
	public void should_be_lazy_test() {
		assertEquals(lazy.first_method(),"method One");
	}
	
	@Test
	public void should_be_lazy_test_two() {
		assertNotEquals(lazy.first_method(),"method Two");
	}

}
