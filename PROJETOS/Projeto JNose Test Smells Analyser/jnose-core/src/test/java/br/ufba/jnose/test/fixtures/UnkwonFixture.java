package br.ufba.jnose.test.fixtures;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class UnkwonFixture {

	@Before
	public void setUp() throws Exception {}

	@Test
	public void should_be_unknown_test() {
		int a  = 0;		
	}

	@Test
	public void should_be_unknown_test_1() {
		int a  = 2;
	}

	@Test
	public void should_be_unknown_test_2() {
		System.out.println("test");
	}

	@Test
	public void should_be_unknown_test_3() {} //this is a EmptyTest

}
