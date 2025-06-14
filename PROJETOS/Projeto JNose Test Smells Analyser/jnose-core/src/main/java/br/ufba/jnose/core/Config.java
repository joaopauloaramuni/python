package br.ufba.jnose.core;

public interface Config {
    Boolean assertionRoulette();
    Boolean conditionalTestLogic();
    Boolean constructorInitialization();
    Boolean defaultTest();
    Boolean dependentTest();
    Boolean duplicateAssert();
    Boolean eagerTest();
    Boolean emptyTest();
    Boolean exceptionCatchingThrowing();
    Boolean generalFixture();
    Boolean mysteryGuest();
    Boolean printStatement();
    Boolean redundantAssertion();
    Boolean sensitiveEquality();
    Boolean verboseTest();
    Boolean sleepyTest();
    Boolean lazyTest();
    Boolean unknownTest();
    Boolean ignoredTest();
    Boolean resourceOptimism();
    Boolean magicNumberTest();
    Integer maxStatements();
}
