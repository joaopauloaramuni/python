package br.ufba.jnose.dtolocal;

import java.io.Serializable;

public class TotalProcessado implements Serializable {
    private static final long serialVersionUID = 1L;

    private int valor;

    public TotalProcessado() {
        this.valor = 0;
    }

    public int getValor() {
        return valor;
    }

    public void setValor(int valor) {
        this.valor = valor;
    }
}
