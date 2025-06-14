package br.ufba.jnose.test.fixtures;

import org.junit.Test;

public class ConditionalFixture {

	
	@Test
	public void should_be_conditional_one() {
		if (true) {
		}	
	}
	
	@Test
	public void should_be_conditional_two() {
		for (int i = 0; i < 2; i++) {
		}		
	}
	
	@Test
	public void should_be_conditional_three() {
		int i = 0;
		while (i < 2) {
			i++;
		}
	}
	
	@Test
	public void should_be_conditional_four() {
		int i = 0;
		System.out.println((i <= 2) ? i : 2);
	}
	
	@Test
	public void should_be_conditional_five() {
		String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
		for (String i : cars) {
		  System.out.println(i);
		}	
	}
	
	@Test
	public void should_be_conditional_six() {
		int day = 4;
		switch (day) {
		  case 1:
		    System.out.println("Monday");
		    break;
		  case 2:
		    System.out.println("Tuesday");
		    break;
		}		
	}
	@Test
	public void should_be_conditional_seven() {
		int i = 0;
		do {
		  System.out.println(i);
		  i++;
		}
		while (i < 2);
	}
		
}
