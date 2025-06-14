package br.ufba.jnose.dto;

import java.io.Serializable;
import java.math.BigInteger;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;

public class TestSmell implements Serializable {
    private static final long serialVersionUID = 1L;

    private String name;
    private String method;
    private String range;
    private TestClass testClass;
    private String code;

    public void setCode(String code){
        this.code = code;
    }

    public String getCode(){
        return code;
    }

    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }

    public void setTestClass(TestClass testClass){
        this.testClass = testClass;
    }

    public TestClass getTestClass(){
        return this.testClass;
    }

    public String getMethodNameHash(){
        String hash = "";
        try {
            MessageDigest md5 = MessageDigest.getInstance("MD5");
            md5.update(StandardCharsets.UTF_8.encode(this.method));
            hash = String.format("%032x", new BigInteger(1, md5.digest()));
        } catch (Exception e) {
            e.printStackTrace();
            return "";
        }
        return hash;
    }

    public String getMethodNameFullURIHash(){
        if(this.testClass == null){
            System.out.println("testClass = null ===========================");
        }
        String nomeProjeto = this.testClass.getProjectName();
        String nomeClasse = this.testClass.getFullName();
        String nomeMetodo = this.method;
        String baseText = nomeProjeto + nomeClasse + nomeMetodo;
        String hash = "";
        try {
            MessageDigest md5 = MessageDigest.getInstance("MD5");
            md5.update(StandardCharsets.UTF_8.encode(baseText));
            hash = String.format("%032x", new BigInteger(1, md5.digest()));
        } catch (Exception e) {
            e.printStackTrace();
        }
        return hash;
    }

    @Override
    public String toString() {
        return "TestSmell{" +
                "name='" + name + '\'' +
                ", method='" + method + '\'' +
                ", range='[" + range + "]" +'\'' +
                '}';
    }
}
