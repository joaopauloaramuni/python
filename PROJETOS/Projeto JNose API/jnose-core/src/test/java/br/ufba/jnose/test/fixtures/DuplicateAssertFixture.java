package br.ufba.jnose.test.fixtures;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class DuplicateAssertFixture {

	@Test
	public void should_be_duplicate_assert() {
		assertEquals("","");
		assertEquals("","");
	}

}
