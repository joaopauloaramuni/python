package br.ufba.jnose.test.fixtures;

import static org.junit.Assert.*;

import java.io.File;
import java.io.FileWriter;

import org.junit.Before;
import org.junit.Test;

public class ResourceOptimismFixture {

	@Before
	public void setUp() throws Exception {
	}

	@Test
	public void should_be_resource_optimism() throws Exception {
		File file = new File( "file.txt" );
	    FileWriter fw = new FileWriter( file );
	    fw.write("my text");
	    fw.close();
	    file.delete();
	}
	
	@Test
	public void should_not_be_resource_optimism() throws Exception {
		File file = new File( "file.txt" );
	    if(file.exists()) {
	    	FileWriter fw = new FileWriter( file );
	    	fw.write("my text");
	    }
	}

}
