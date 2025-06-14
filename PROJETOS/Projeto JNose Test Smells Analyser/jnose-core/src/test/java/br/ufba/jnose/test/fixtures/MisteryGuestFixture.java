package br.ufba.jnose.test.fixtures;

import static org.junit.Assert.*;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

import org.junit.Before;
import org.junit.Test;

public class MisteryGuestFixture {

	@Test
	public void should_be_Mistery_Guest() throws IOException{
	    File tempFile = File.createTempFile("test", ".txt");
	}

	@Test
	public void should_be_Mistery_Guest2() throws IOException{
		File tempFile = new File("test.txt");
	}

	@Test
	public void should_be_Mistery_Guest3() throws IOException{
		FileOutputStream tempFile = new FileOutputStream("test.txt");
	}

	@Test
	public void should_be_Mistery_Guest4() throws IOException{
		setFile("file", new File("pom.xml"), "text/xml");
	}

	@Test
	public void should_be_Mistery_Guest5() throws IOException{
		set("file", new File("pom.xml"), "text/xml");
	}


	private void setFile(String fileName, File file, String content) throws IOException {}
	private void set(String fileName, File file, String content) throws IOException {}

}
