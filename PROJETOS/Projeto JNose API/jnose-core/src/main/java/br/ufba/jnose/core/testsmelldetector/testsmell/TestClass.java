package br.ufba.jnose.core.testsmelldetector.testsmell;

public class TestClass extends SmellyElement {

    private final String className;
    private boolean hasSmell;
    private String range;

    public TestClass(String className) {
        this.className = className;
    }

    public void setHasSmell(boolean hasSmell) {
        this.hasSmell = hasSmell;
    }

    @Override
    public String getElementName() {
        return className;
    }

    @Override
    public boolean getHasSmell() {
        return hasSmell;
    }

    @Override
    public String getRange() {
        return range;
    }

}
