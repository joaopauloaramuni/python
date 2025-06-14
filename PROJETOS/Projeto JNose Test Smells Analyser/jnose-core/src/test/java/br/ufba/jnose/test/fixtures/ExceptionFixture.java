package br.ufba.jnose.test.fixtures;

import static org.junit.Assert.*;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

import org.junit.Before;
import org.junit.Test;

public class ExceptionFixture {

	@Before
	public void setUp() throws Exception {
	}
	@Test
	public void should_be_expection_one() {
		try {
				throw new Error("oops");
		     }
			finally {
				System.out.println("finally");
		}
	}
	
	@Test
	public void expection_two() {
		try {
			throw new Error("oops");
	     }
		catch(Error e) {
			System.out.println("catch");
		}
	}

}
