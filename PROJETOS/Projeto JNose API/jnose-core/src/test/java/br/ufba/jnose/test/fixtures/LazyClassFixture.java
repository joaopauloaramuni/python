package br.ufba.jnose.test.fixtures;

public class LazyClassFixture {
	
	public int initial_value;
	public String state;
	
	public LazyClassFixture() {
	}
	
	public String first_method() {
		return "method One";
	}
	
	public String second_method() {
		return "method Two";
	}
}
