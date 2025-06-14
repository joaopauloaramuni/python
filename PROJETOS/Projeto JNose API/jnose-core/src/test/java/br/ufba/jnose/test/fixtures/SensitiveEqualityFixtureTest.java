package br.ufba.jnose.test.fixtures;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class SensitiveEqualityFixtureTest {
	
	SensitiveEqualityFixture s;

	@Before
	public void setUp() throws Exception {
		s = new SensitiveEqualityFixture();
	}

	@Test
	public void should_be_sensitive_equality() {
		assertEquals(s.x.toString(), "text");
	}

	@Test
	public void should_be_sensitive_equality_1() {
		System.out.println(s.x.toString());
		assertEquals(s.x.toString(), "text");
	}

}
