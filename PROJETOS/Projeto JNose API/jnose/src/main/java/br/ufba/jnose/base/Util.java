package br.ufba.jnose.base;

import br.ufba.jnose.dto.TestClass;
import br.ufba.jnose.dto.TestSmell;
import org.apache.wicket.behavior.AttributeAppender;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

public class Util {

    public static boolean isInt(String s) {
        try {
            int i = Integer.parseInt(s);
            return true;
        }

        catch (NumberFormatException er) {
            return false;
        }
    }

    public static String dateNow() {
        return LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyyMMdd-HH:mm:ss")) + " - ";
    }

    public static String dateNowFolder() {
        return LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyyMMddHHmmss"));
    }

    public static void execCommand(final String commandLine, String pathExecute) {
        int r = 0;
        try {
            Process p = Runtime.getRuntime().exec(commandLine, null, new File(pathExecute));
            BufferedReader input = new BufferedReader(new InputStreamReader(p.getInputStream()));
            String lineOut;
            while ((lineOut = input.readLine()) != null) {
                System.out.println(lineOut);
            }
            input.close();
            r = p.waitFor();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static String getCode(TestClass testClass, TestSmell testSmell){
        String nomeClassPath = testClass.getPathFile();
        String range = testSmell.getRange();

        List<Integer> linhasComTestSmells = new ArrayList<>();

        if(range.contains("-")){
            String[] ranger2 = range.split("-");
            int inicio = Integer.parseInt(ranger2[0].trim());
            int fim = Integer.parseInt(ranger2[1].trim());
            for (int i = inicio; i <= fim; i++) {
                linhasComTestSmells.add(i);
            }
        }else if(range.contains(",")){
            String[] ranger2 = range.replace(" ","").split(",");
            for (String linha : ranger2) {
                linhasComTestSmells.add(Integer.parseInt(linha));
            }
        }else if(isInt(range.trim())){
            int range2 = Integer.parseInt(range.trim());
            linhasComTestSmells.add(range2);
        }

        List<String> linhasStringComSmells = new ArrayList();

        try {
            File file = new File(nomeClassPath);    //creates a new file instance
            FileReader fr = new FileReader(file);   //reads the file
            BufferedReader br = new BufferedReader(fr);  //creates a buffering character input stream
            String line;
            int contLinha = 1;
            while ((line = br.readLine()) != null) {
                if(linhasComTestSmells.contains(contLinha)) {
                    linhasStringComSmells.add(line);
                }
                contLinha++;
            }
            fr.close();    //closes the stream and release the resources
        } catch (IOException e) {
            e.printStackTrace();
        }

        return linhasStringComSmells.toString();
    }

    public static String getSHA5Code(TestClass testClass, TestSmell testSmell){
        String code = getCode(testClass,testSmell);
        byte[] encodedhash = null;

        MessageDigest digest = null;
        try {
            digest = MessageDigest.getInstance("SHA-256");
            encodedhash = digest.digest(code.getBytes(StandardCharsets.UTF_8));
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }

        return bytesToHex(encodedhash);
    }

    private static String bytesToHex(byte[] hash) {
        StringBuilder hexString = new StringBuilder(2 * hash.length);
        for (int i = 0; i < hash.length; i++) {
            String hex = Integer.toHexString(0xff & hash[i]);
            if(hex.length() == 1) {
                hexString.append('0');
            }
            hexString.append(hex);
        }
        return hexString.toString();
    }



}
