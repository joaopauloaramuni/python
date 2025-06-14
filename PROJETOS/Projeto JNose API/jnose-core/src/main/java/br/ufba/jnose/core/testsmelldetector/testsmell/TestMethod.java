package br.ufba.jnose.core.testsmelldetector.testsmell;

public class TestMethod extends SmellyElement {

    private String methodName;
    private boolean hasSmell;
    private Integer begin;
    private Integer end;
    private String range;

    public TestMethod(String methodName) {
        this.methodName = methodName;
    }

    public void setHasSmell(boolean hasSmell) {
        this.hasSmell = hasSmell;
    }

    @Override
    public String getElementName() {
        return methodName;
    }

    @Override
    public boolean getHasSmell() {
        return hasSmell;
    }

    @Override
    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
    }

    public Integer getBegin() {
        return begin;
    }

    public void setBegin(Integer begin) {
        this.begin = begin;
    }

    public Integer getEnd() {
        return end;
    }

    public void setEnd(Integer end) {
        this.end = end;
    }

}
