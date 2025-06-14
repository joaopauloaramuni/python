package br.ufba.jnose.test.fixtures;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class SleepyFixture {

	@Before
	public void setUp() throws Exception {
	}

	@Test
	public void should_be_sleep_test() throws InterruptedException {
		Thread.sleep(500);
	}

	@Test
	public void should_be_sleep_test_1() throws InterruptedException {
		Thread.sleep(500, 1);
	}

	@Test
	public void should_be_sleep_test_2() throws InterruptedException {
		System.out.println("test");
		Thread.sleep(500, 1);
		Thread.sleep(500);
	}
}
