package br.ufba.jnose.test.fixtures;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Ignore;
import org.junit.Test;

public class IgnoredFixture {

	@Before
	public void setUp() throws Exception {
	}

	@Ignore("testing ignored test") @Test
	public void should_be_ignored_test() {
		System.out.println("Runnig a test");
	}

}
