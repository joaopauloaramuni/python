package br.ufba.jnose.dtolocal;

import br.ufba.jnose.dto.TestClass;
import br.ufba.jnose.entities.Projeto;
import org.apache.wicket.markup.html.WebMarkupContainer;
import org.apache.wicket.markup.html.basic.Label;
import org.apache.wicket.markup.html.link.Link;

import java.io.Serializable;
import java.util.List;
import java.util.Map;

public class ProjetoDTO implements Serializable {
    private static final long serialVersionUID = 1L;

    private Boolean paraProcessar;
    private Boolean processado;
    private Boolean processado2;
    private Integer procentagem;

    private List<List<String>> resultado;

    private List<br.ufba.jnose.dto.TestClass> resultadoByTestSmells;

    private List<Commit> listaCommits;

    private List<Commit> listaTags;

    private Integer commits;

    private Map<Integer, List<List<String>>> mapResults;

    public WebMarkupContainer iconProcessado;
    public WebMarkupContainer iconNaoProcessado;

    public WebMarkupContainer progressProject;

    private Link lkResultado;
    public Link lkCharts;
    public Link lkResult1;
    public Link lkResult2;
    public Link lkResult3;
    public Link lkResult4;
    public Link lkChart2;
    public Link lkChart3;

    public Label lbPorcentagem;
    public String bugs;

    private String repoGit;

    private String optionSelected;

    private br.ufba.jnose.entities.Projeto projeto;

    public ProjetoDTO(Projeto projeto) {
        if(this.projeto == null)this.projeto = new br.ufba.jnose.entities.Projeto();
        this.projeto.setName(projeto.getName());
        this.projeto.setPath(projeto.getPath());
        this.processado = false;
        this.processado2 = false;
        this.procentagem = 0;
        this.paraProcessar = true;
        this.commits = 0;
        this.optionSelected = "";
    }

    public ProjetoDTO(Projeto projeto, Boolean processado, Boolean processado2, Integer procentagem) {
        if(this.projeto == null)this.projeto = new Projeto();
        this.projeto.setName(projeto.getName());
        this.projeto.setPath(projeto.getPath());
        this.processado = processado;
        this.processado2 = processado2;
        this.procentagem = procentagem;
        this.paraProcessar = true;
        this.commits = 0;
        this.optionSelected = "";
    }

    public String getOptionSelected() {
        return optionSelected;
    }

    public void setOptionSelected(String optionSelected) {
        this.optionSelected = optionSelected;
    }

    public List<List<String>> getResultado() {
        return resultado;
    }

    public void setResultado(List<List<String>> resultado) {
        this.resultado = resultado;
    }

    public List<TestClass> getResultadoByTestSmells() {
        return resultadoByTestSmells;
    }

    public void setResultadoByTestSmells(List<TestClass> resultadoByTestSmells) {
        this.resultadoByTestSmells = resultadoByTestSmells;
    }

    public List<Commit> getListaCommits() {
        return listaCommits;
    }

    public void setListaCommits(List<Commit> listaCommits) {
        this.listaCommits = listaCommits;
    }

    public Integer getCommits() {
        return commits;
    }

    public void setCommits(Integer commits) {
        this.commits = commits;
    }

    public Boolean getParaProcessar() {
        return paraProcessar;
    }

    public void setParaProcessar(Boolean paraProcessar) {
        this.paraProcessar = paraProcessar;
    }

    public String getName() {
        return projeto.getName();
    }

    public void setName(String name) {
        this.projeto.setName(name);
    }

    public String getPath() {
        return projeto.getPath();
    }

    public void setPath(String path) {
        this.projeto.setPath(path);
    }

    public Boolean getProcessado() {
        return processado && processado2;
    }

    public void setProcessado(Boolean processado) {
        this.processado = processado;
    }

    public void setProcessado2(Boolean processado2) {
        this.processado2 = processado2;
    }

    public Integer getProcentagem() {
        return procentagem;
    }

    public void setProcentagem(Integer procentagem) {
        this.procentagem = procentagem;
    }

    public String getRepoGit() {
        return repoGit;
    }

    public void setRepoGit(String repoGit) {
        this.repoGit = repoGit;
    }

    public List<Commit> getListaTags() {
        return listaTags;
    }

    public void setListaTags(List<Commit> listaTags) {
        this.listaTags = listaTags;
    }

    public Map<Integer, List<List<String>>> getMapResults() {
        return mapResults;
    }

    public void setMapResults(Map<Integer, List<List<String>>> mapResults) {
        this.mapResults = mapResults;
    }

    public br.ufba.jnose.entities.Projeto getProjeto() {
        return projeto;
    }

    public void setProjeto(br.ufba.jnose.entities.Projeto projeto) {
        this.projeto = projeto;
    }

    public Link getLkResultado() {
        return lkResultado;
    }

    public void setLkResultado(Link lkResultado) {
        this.lkResultado = lkResultado;
    }
}
