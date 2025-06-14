package br.ufba.jnose.entities;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.ManyToOne;
import java.io.Serializable;
import java.util.Objects;

@Entity
public class TestSmell implements Serializable {

    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue
    private Long id;

    private String nome;

    private String pathTestClass;

    private String pathProductionClass;

    private String method;

    private String begin;

    private String end;

    @ManyToOne
    private Projeto projeto;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getPathTestClass() {
        return pathTestClass;
    }

    public void setPathTestClass(String pathTestClass) {
        this.pathTestClass = pathTestClass;
    }

    public String getPathProductionClass() {
        return pathProductionClass;
    }

    public void setPathProductionClass(String pathProductionClass) {
        this.pathProductionClass = pathProductionClass;
    }

    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }

    public String getBegin() {
        return begin;
    }

    public void setBegin(String begin) {
        this.begin = begin;
    }

    public String getEnd() {
        return end;
    }

    public void setEnd(String end) {
        this.end = end;
    }

    public Projeto getProjeto() {
        return projeto;
    }

    public void setProjeto(Projeto projeto) {
        this.projeto = projeto;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        TestSmell testSmell = (TestSmell) o;
        return id.equals(testSmell.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }

    @Override
    public String toString() {
        return "TestSmell{" +
                "id=" + id +
                ", nome='" + nome + '\'' +
                ", pathTestClass='" + pathTestClass + '\'' +
                ", pathProductionClass='" + pathProductionClass + '\'' +
                ", method='" + method + '\'' +
                ", begin='" + begin + '\'' +
                ", end='" + end + '\'' +
                ", projeto=" + projeto +
                '}';
    }
}
