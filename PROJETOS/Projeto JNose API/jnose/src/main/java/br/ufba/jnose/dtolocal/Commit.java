package br.ufba.jnose.dtolocal;

import java.io.Serializable;
import java.util.Date;

public class Commit implements Serializable {
    private static final long serialVersionUID = 1L;

    public String id;
    public String name;
    public Date date;
    public String msg;
    public String tag;

    public Commit(String id, String name, Date date, String msg) {
        this.id = id;
        this.name = name;
        this.date = date;
        this.msg = msg;
    }

    public Commit(String id, String name, Date date, String msg, String tag) {
        this.id = id;
        this.name = name;
        this.date = date;
        this.msg = msg;
        this.tag = tag;
    }

    @Override
    public String toString() {
        return "Commit{" +
                "id='" + id + '\'' +
                ", name='" + name + '\'' +
                ", date=" + date +
                ", msg='" + msg + '\'' +
                ", tag='" + tag + '\'' +
                '}';
    }
}
