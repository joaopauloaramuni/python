package br.ufba.jnose.pages;

import br.ufba.jnose.base.TestSmellDetectorConfig;
import br.ufba.jnose.pages.base.BasePage;
import org.apache.wicket.markup.html.form.Button;
import org.apache.wicket.markup.html.form.CheckBox;
import org.apache.wicket.markup.html.form.Form;
import org.apache.wicket.markup.html.form.TextField;
import org.apache.wicket.markup.html.link.Link;
import org.apache.wicket.model.PropertyModel;
import br.ufba.jnose.core.testsmelldetector.testsmell.smell.*;

public class ConfigPage extends BasePage {
    private static final long serialVersionUID = 1L;

    public Boolean assertionRoulette;
    public Boolean conditionalTestLogic;
    public Boolean constructorInitialization;
    public Boolean defaultTest;
    public Boolean dependentTest;
    public Boolean duplicateAssert;
    public Boolean eagerTest;
    public Boolean lazyTest;
    public Boolean unknownTest;
    public Boolean ignoredTest;
    public Boolean resourceOptimism;
    public Boolean magicNumberTest;
    public Boolean printStatement;
    public Boolean redundantAssertion;
    public Boolean sensitiveEquality;
    public Boolean verboseTest;
    public Boolean sleepyTest;
    public Boolean emptyTest;
    public Boolean exceptionCatchingThrowing;
    public Boolean generalFixture;
    public Boolean mysteryGuest;

    public String verboseTestMaxStatements;

    public ConfigPage() {
        super("ConfigPage");

        this.verboseTestMaxStatements = br.ufba.jnose.core.testsmelldetector.testsmell.smell.VerboseTest.MAX_STATEMENTS+"";

        emptyTest = TestSmellDetectorConfig.emptyTest;
        exceptionCatchingThrowing = TestSmellDetectorConfig.exceptionCatchingThrowing;
        generalFixture = TestSmellDetectorConfig.generalFixture;
        mysteryGuest = TestSmellDetectorConfig.mysteryGuest;
        sleepyTest = TestSmellDetectorConfig.sleepyTest;
        verboseTest = TestSmellDetectorConfig.verboseTest;
        sensitiveEquality = TestSmellDetectorConfig.sensitiveEquality;
        redundantAssertion = TestSmellDetectorConfig.redundantAssertion;
        printStatement = TestSmellDetectorConfig.printStatement;
        magicNumberTest = TestSmellDetectorConfig.magicNumberTest;
        resourceOptimism = TestSmellDetectorConfig.resourceOptimism;
        ignoredTest = TestSmellDetectorConfig.ignoredTest;
        unknownTest = TestSmellDetectorConfig.unknownTest;
        lazyTest = TestSmellDetectorConfig.lazyTest;
        assertionRoulette = TestSmellDetectorConfig.assertionRoulette;
        conditionalTestLogic = TestSmellDetectorConfig.conditionalTestLogic;
        constructorInitialization = TestSmellDetectorConfig.constructorInitialization;
        defaultTest = TestSmellDetectorConfig.defaultTest;
        dependentTest = TestSmellDetectorConfig.dependentTest;
        duplicateAssert = TestSmellDetectorConfig.duplicateAssert;
        eagerTest = TestSmellDetectorConfig.eagerTest;

        Form form = new Form<String>("form") {
            @Override
            protected void onSubmit() {
                TestSmellDetectorConfig.emptyTest = emptyTest;
                TestSmellDetectorConfig.exceptionCatchingThrowing = exceptionCatchingThrowing;
                TestSmellDetectorConfig.generalFixture = generalFixture;
                TestSmellDetectorConfig.mysteryGuest = mysteryGuest;
                TestSmellDetectorConfig.sleepyTest = sleepyTest;
                TestSmellDetectorConfig.sensitiveEquality = sensitiveEquality;
                TestSmellDetectorConfig.redundantAssertion = redundantAssertion;
                TestSmellDetectorConfig.printStatement = printStatement;
                TestSmellDetectorConfig.magicNumberTest = magicNumberTest;
                TestSmellDetectorConfig.resourceOptimism = resourceOptimism;
                TestSmellDetectorConfig.ignoredTest = ignoredTest;
                TestSmellDetectorConfig.unknownTest = unknownTest;
                TestSmellDetectorConfig.lazyTest = lazyTest;
                TestSmellDetectorConfig.assertionRoulette = assertionRoulette;
                TestSmellDetectorConfig.conditionalTestLogic = conditionalTestLogic;
                TestSmellDetectorConfig.constructorInitialization = constructorInitialization;
                TestSmellDetectorConfig.defaultTest = defaultTest;
                TestSmellDetectorConfig.dependentTest = dependentTest;
                TestSmellDetectorConfig.duplicateAssert = duplicateAssert;
                TestSmellDetectorConfig.eagerTest = eagerTest;

                TestSmellDetectorConfig.verboseTest = verboseTest;
                br.ufba.jnose.core.testsmelldetector.testsmell.smell.VerboseTest.MAX_STATEMENTS = Integer.parseInt(verboseTestMaxStatements);
            }
        };

        form.add(new Button("btAll"){
            @Override
            public void onSubmit() {
                TestSmellDetectorConfig.emptyTest = true;
                TestSmellDetectorConfig.exceptionCatchingThrowing = true;
                TestSmellDetectorConfig.generalFixture = true;
                TestSmellDetectorConfig.mysteryGuest = true;
                TestSmellDetectorConfig.sleepyTest = true;
                TestSmellDetectorConfig.verboseTest = true;
                TestSmellDetectorConfig.sensitiveEquality = true;
                TestSmellDetectorConfig.redundantAssertion = true;
                TestSmellDetectorConfig.printStatement = true;
                TestSmellDetectorConfig.magicNumberTest = true;
                TestSmellDetectorConfig.resourceOptimism = true;
                TestSmellDetectorConfig.ignoredTest = true;
                TestSmellDetectorConfig.unknownTest = true;
                TestSmellDetectorConfig.lazyTest = true;
                TestSmellDetectorConfig.assertionRoulette = true;
                TestSmellDetectorConfig.conditionalTestLogic = true;
                TestSmellDetectorConfig.constructorInitialization = true;
                TestSmellDetectorConfig.defaultTest = true;
                TestSmellDetectorConfig.dependentTest = true;
                TestSmellDetectorConfig.duplicateAssert = true;
                TestSmellDetectorConfig.eagerTest = true;

                emptyTest = TestSmellDetectorConfig.emptyTest;
                exceptionCatchingThrowing = TestSmellDetectorConfig.exceptionCatchingThrowing;
                generalFixture = TestSmellDetectorConfig.generalFixture;
                mysteryGuest = TestSmellDetectorConfig.mysteryGuest;
                sleepyTest = TestSmellDetectorConfig.sleepyTest;
                verboseTest = TestSmellDetectorConfig.verboseTest;
                sensitiveEquality = TestSmellDetectorConfig.sensitiveEquality;
                redundantAssertion = TestSmellDetectorConfig.redundantAssertion;
                printStatement = TestSmellDetectorConfig.printStatement;
                magicNumberTest = TestSmellDetectorConfig.magicNumberTest;
                resourceOptimism = TestSmellDetectorConfig.resourceOptimism;
                ignoredTest = TestSmellDetectorConfig.ignoredTest;
                unknownTest = TestSmellDetectorConfig.unknownTest;
                lazyTest = TestSmellDetectorConfig.lazyTest;
                assertionRoulette = TestSmellDetectorConfig.assertionRoulette;
                conditionalTestLogic = TestSmellDetectorConfig.conditionalTestLogic;
                constructorInitialization = TestSmellDetectorConfig.constructorInitialization;
                defaultTest = TestSmellDetectorConfig.defaultTest;
                dependentTest = TestSmellDetectorConfig.dependentTest;
                duplicateAssert = TestSmellDetectorConfig.duplicateAssert;
                eagerTest = TestSmellDetectorConfig.eagerTest;

                ConfigPage.this.setResponsePage(ConfigPage.class);
            }
        });

        form.add(new Button("btDAll"){
            @Override
            public void onSubmit() {
                TestSmellDetectorConfig.emptyTest = false;
                TestSmellDetectorConfig.exceptionCatchingThrowing = false;
                TestSmellDetectorConfig.generalFixture = false;
                TestSmellDetectorConfig.mysteryGuest = false;
                TestSmellDetectorConfig.sleepyTest = false;
                TestSmellDetectorConfig.verboseTest = false;
                TestSmellDetectorConfig.sensitiveEquality = false;
                TestSmellDetectorConfig.redundantAssertion = false;
                TestSmellDetectorConfig.printStatement = false;
                TestSmellDetectorConfig.magicNumberTest = false;
                TestSmellDetectorConfig.resourceOptimism = false;
                TestSmellDetectorConfig.ignoredTest = false;
                TestSmellDetectorConfig.unknownTest = false;
                TestSmellDetectorConfig.lazyTest = false;
                TestSmellDetectorConfig.assertionRoulette = false;
                TestSmellDetectorConfig.conditionalTestLogic = false;
                TestSmellDetectorConfig.constructorInitialization = false;
                TestSmellDetectorConfig.defaultTest = false;
                TestSmellDetectorConfig.dependentTest = false;
                TestSmellDetectorConfig.duplicateAssert = false;
                TestSmellDetectorConfig.eagerTest = false;

                emptyTest = TestSmellDetectorConfig.emptyTest;
                exceptionCatchingThrowing = TestSmellDetectorConfig.exceptionCatchingThrowing;
                generalFixture = TestSmellDetectorConfig.generalFixture;
                mysteryGuest = TestSmellDetectorConfig.mysteryGuest;
                sleepyTest = TestSmellDetectorConfig.sleepyTest;
                verboseTest = TestSmellDetectorConfig.verboseTest;
                sensitiveEquality = TestSmellDetectorConfig.sensitiveEquality;
                redundantAssertion = TestSmellDetectorConfig.redundantAssertion;
                printStatement = TestSmellDetectorConfig.printStatement;
                magicNumberTest = TestSmellDetectorConfig.magicNumberTest;
                resourceOptimism = TestSmellDetectorConfig.resourceOptimism;
                ignoredTest = TestSmellDetectorConfig.ignoredTest;
                unknownTest = TestSmellDetectorConfig.unknownTest;
                lazyTest = TestSmellDetectorConfig.lazyTest;
                assertionRoulette = TestSmellDetectorConfig.assertionRoulette;
                conditionalTestLogic = TestSmellDetectorConfig.conditionalTestLogic;
                constructorInitialization = TestSmellDetectorConfig.constructorInitialization;
                defaultTest = TestSmellDetectorConfig.defaultTest;
                dependentTest = TestSmellDetectorConfig.dependentTest;
                duplicateAssert = TestSmellDetectorConfig.duplicateAssert;
                eagerTest = TestSmellDetectorConfig.eagerTest;

                ConfigPage.this.setResponsePage(ConfigPage.class);
            }
        });

        form.add(new CheckBox("cbAssertionRoulette", new PropertyModel<>(this, "assertionRoulette")));
        form.add(new CheckBox("cbConditionalTestLogic", new PropertyModel<>(this, "conditionalTestLogic")));
        form.add(new CheckBox("cbConstructorInitialization", new PropertyModel<>(this, "constructorInitialization")));
        form.add(new CheckBox("cbDefaultTest", new PropertyModel<>(this, "defaultTest")));
        form.add(new CheckBox("cbDependentTest", new PropertyModel<>(this, "dependentTest")));
        form.add(new CheckBox("cbDuplicateAssert", new PropertyModel<>(this, "duplicateAssert")));
        form.add(new CheckBox("cbEagerTest", new PropertyModel<>(this, "eagerTest")));
        form.add(new CheckBox("cbEmptyTest", new PropertyModel<>(this, "emptyTest")));
        form.add(new CheckBox("cbExceptionCatchingThrowing", new PropertyModel<>(this, "exceptionCatchingThrowing")));
        form.add(new CheckBox("cbGeneralFixture", new PropertyModel<>(this, "generalFixture")));
        form.add(new CheckBox("cbMysteryGuest", new PropertyModel<>(this, "mysteryGuest")));
        form.add(new CheckBox("cbSleepyTest", new PropertyModel<>(this, "sleepyTest")));
        form.add(new CheckBox("cbSensitiveEquality", new PropertyModel<>(this, "sensitiveEquality")));
        form.add(new CheckBox("cbRedundantAssertion", new PropertyModel<>(this, "redundantAssertion")));
        form.add(new CheckBox("cbPrintStatement", new PropertyModel<>(this, "printStatement")));
        form.add(new CheckBox("cbMagicNumberTest", new PropertyModel<>(this, "magicNumberTest")));
        form.add(new CheckBox("cbResourceOptimism", new PropertyModel<>(this, "resourceOptimism")));
        form.add(new CheckBox("cbIgnoredTest", new PropertyModel<>(this, "ignoredTest")));
        form.add(new CheckBox("cbUnknownTest", new PropertyModel<>(this, "unknownTest")));
        form.add(new CheckBox("cbLazyTest", new PropertyModel<>(this, "lazyTest")));

        form.add(new CheckBox("cbVerboseTest", new PropertyModel<>(this, "verboseTest")));
        form.add(new TextField<String>("verboseTestMaxStatements", new PropertyModel<>(this, "verboseTestMaxStatements")));


        form.add(new Link<String>("lkSourceAssertionRoulette") {
            @Override
            public void onClick() {
                setResponsePage(new SourcePage(new AssertionRoulette()));
            }
        });
        form.add(new Link<String>("lkSourceConditionalTestLogic") {
            @Override
            public void onClick() {
                setResponsePage(new SourcePage(new ConditionalTestLogic()));
            }
        });
        form.add(new Link<String>("lkSourceConstructorInitialization") {
            @Override
            public void onClick() {
                setResponsePage(new SourcePage(new ConstructorInitialization()));
            }
        });
        form.add(new Link<String>("lkSourceDefaultTest") {
            @Override
            public void onClick() {
                setResponsePage(new SourcePage(new DefaultTest()));
            }
        });
        form.add(new Link<String>("lkSourceDependentTest") {
            @Override
            public void onClick() {
                setResponsePage(new SourcePage(new DependentTest()));
            }
        });
        form.add(new Link<String>("lkSourceDuplicateAssert") {
            @Override
            public void onClick() {
                setResponsePage(new SourcePage(new DuplicateAssert()));
            }
        });
        form.add(new Link<String>("lkSourceEagerTest") {
            @Override
            public void onClick() {
                setResponsePage(new SourcePage(new EagerTest()));
            }
        });
        form.add(new Link<String>("lkSourceEmptyTest") {
            @Override
            public void onClick() {
                setResponsePage(new SourcePage(new EmptyTest()));
            }
        });
        form.add(new Link<String>("lkSourceExceptionCatchingThrowing") {
            @Override
            public void onClick() {
                setResponsePage(new SourcePage(new ExceptionCatchingThrowing()));
            }
        });
        form.add(new Link<String>("lkSourceGeneralFixture") {
            @Override
            public void onClick() {
                setResponsePage(new SourcePage(new GeneralFixture()));
            }
        });
        form.add(new Link<String>("IgnoredTest") {
            @Override
            public void onClick() {
                setResponsePage(new SourcePage(new IgnoredTest()));
            }
        });
        form.add(new Link<String>("LazyTest") {
            @Override
            public void onClick() {
                setResponsePage(new SourcePage(new LazyTest()));
            }
        });
        form.add(new Link<String>("MagicNumberTest") {
            @Override
            public void onClick() {
                setResponsePage(new SourcePage(new MagicNumberTest()));
            }
        });
        form.add(new Link<String>("MysteryGuest") {
            @Override
            public void onClick() {
                setResponsePage(new SourcePage(new MysteryGuest()));
            }
        });
        form.add(new Link<String>("PrintStatement") {
            @Override
            public void onClick() {
                setResponsePage(new SourcePage(new PrintStatement()));
            }
        });
        form.add(new Link<String>("RedundantAssertion") {
            @Override
            public void onClick() {
                setResponsePage(new SourcePage(new RedundantAssertion()));
            }
        });
        form.add(new Link<String>("ResourceOptimism") {
            @Override
            public void onClick() {
                setResponsePage(new SourcePage(new ResourceOptimism()));
            }
        });
        form.add(new Link<String>("SensitiveEquality") {
            @Override
            public void onClick() {
                setResponsePage(new SourcePage(new SensitiveEquality()));
            }
        });
        form.add(new Link<String>("SleepyTest") {
            @Override
            public void onClick() {
                setResponsePage(new SourcePage(new SleepyTest()));
            }
        });
        form.add(new Link<String>("UnknownTest") {
            @Override
            public void onClick() {
                setResponsePage(new SourcePage(new UnknownTest()));
            }
        });
        form.add(new Link<String>("VerboseTest") {
            @Override
            public void onClick() {
                setResponsePage(new SourcePage(new VerboseTest()));
            }
        });

        add(form);

    }
}