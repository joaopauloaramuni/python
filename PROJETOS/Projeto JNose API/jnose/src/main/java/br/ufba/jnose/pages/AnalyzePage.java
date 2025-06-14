package br.ufba.jnose.pages;

import br.ufba.jnose.core.Config;
import br.ufba.jnose.core.JNoseCore;
import br.ufba.jnose.dto.TestClass;
import br.ufba.jnose.dto.TestSmell;
import br.ufba.jnose.pages.base.BasePage;
import br.ufba.jnose.pages.modals.ModalView;
import de.agilecoders.wicket.core.markup.html.bootstrap.common.NotificationPanel;
import org.apache.wicket.ajax.AjaxRequestTarget;
import org.apache.wicket.ajax.markup.html.AjaxLink;
import org.apache.wicket.ajax.markup.html.form.AjaxButton;
import org.apache.wicket.markup.html.WebMarkupContainer;
import org.apache.wicket.markup.html.basic.Label;
import org.apache.wicket.markup.html.form.Form;
import org.apache.wicket.markup.html.form.upload.FileUpload;
import org.apache.wicket.markup.html.form.upload.FileUploadField;
import org.apache.wicket.markup.html.list.ListItem;
import org.apache.wicket.markup.html.list.ListView;
import org.apache.wicket.request.cycle.RequestCycle;
import org.apache.wicket.request.http.WebRequest;
import org.apache.wicket.util.lang.Bytes;

import javax.servlet.http.HttpServletRequest;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Stream;

public class AnalyzePage extends BasePage {
    private static final long serialVersionUID = 1L;

    private WebMarkupContainer container;

    private ListView<TestSmell> listview;

    private AjaxButton btSubmit;

    private List<String> fileInList;

    public AnalyzePage() {
        this(new ArrayList<>());
    }

    public AnalyzePage(List<TestSmell> listaTestSmellBeans) {
        super("AnalyzePage");

        fileInList = new ArrayList<>();
        fileInList.add("//zero");//add line zero

        loadDescriptions();

        WebRequest req = (WebRequest) RequestCycle.get().getRequest();
        HttpServletRequest httpReq = (HttpServletRequest) req.getContainerRequest();
        String clientAddress = httpReq.getRemoteHost();

        WebMarkupContainer containerFeedback = new WebMarkupContainer("containerFeedback");
        containerFeedback.setOutputMarkupId(true);
        add(containerFeedback);

        NotificationPanel notificationPanel = new NotificationPanel("feedback");
        notificationPanel.setOutputMarkupId(true);
        containerFeedback.add(notificationPanel);

        Form form = new Form<Void>("fom");
        form.setMultiPart(true);
        form.setMaxSize(Bytes.kilobytes(1000));
        form.setOutputMarkupId(true);

        FileUploadField fileUpload1 = new FileUploadField("fileUpload1");
        fileUpload1.setRequired(true);
        form.add(fileUpload1);

        FileUploadField fileUpload2 = new FileUploadField("fileUpload2");
        fileUpload2.setRequired(false);
        form.add(fileUpload2);


        btSubmit = new AjaxButton("btSubmit") {
            @Override
            protected void onSubmit(AjaxRequestTarget target) {

                final FileUpload uploadedFile1 = fileUpload1.getFileUpload();

                final FileUpload uploadedFile2 = fileUpload2.getFileUpload();

                File classTestFile = null;
                File classProductionFile = null;

                if (uploadedFile1 != null) {
                    try {
                        classTestFile = new File(uploadedFile1.getClientFileName());
                        uploadedFile1.writeTo(classTestFile);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }

                try (Stream<String> stream = Files.lines(classTestFile.getAbsoluteFile().toPath())) {
                    stream.forEach(line -> fileInList.add(line));
                } catch (IOException e) {
                    e.printStackTrace();
                }

                if (uploadedFile2 != null) {
                    try {
                        classProductionFile = new File(uploadedFile2.getClientFileName());
                        uploadedFile2.writeTo(classProductionFile);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }

                TestClass testClass = new TestClass();
                testClass.setName(uploadedFile1.getClientFileName());
                testClass.setPathFile(classTestFile.getAbsolutePath());

                if (classProductionFile != null) {
                    testClass.setProductionFile(classProductionFile.getAbsolutePath());
                } else {
                    testClass.setProductionFile("");
                }

                testClass.setProjectName("");

                //Mudar a lógica depois no Core
                testClass.setJunitVersion(TestClass.JunitVersion.JUnit4);

                JNoseCore jNoseCore = new JNoseCore(loadConfig(!testClass.getProductionFile().isBlank()),3);
//                Boolean isClassTest = jNoseCore.isTestFile(testClass);
                jNoseCore.getTestSmells(testClass);

                List<TestSmell> listaTestSmellBean = testClass.getListTestSmell();
                listview.setList(listaTestSmellBean);

                target.add(container, form, containerFeedback);

                info("ClassTest: " + uploadedFile1.getClientFileName() + " - Processed - " + listaTestSmellBean.size() + " TestSmells found.");

                if (classProductionFile != null) {
                    info("ClassProduction: " + uploadedFile2.getClientFileName());
                    classProductionFile.delete();
                }

                classTestFile.delete();
            }
        };
        form.add(btSubmit);

        add(form);

        listview = new ListView<TestSmell>("listview", listaTestSmellBeans) {
            protected void populateItem(ListItem<TestSmell> item) {
                TestSmell testSmell = item.getModelObject();

                item.add(new Label("nome", testSmell.getName()));
                item.add(new Label("method", testSmell.getMethod()));
                item.add(new Label("range", testSmell.getRange()));

                String contentDescription = descriptions.get(testSmell.getName());
                String content = contentDescription + "<br><br><b>You code:</b><br><pre><br>" + getLines(testSmell.getRange()) + "<br></pre> <br>";

                ModalView modal = new ModalView("modal",testSmell.getName(),content);
                item.add(modal);

                AjaxLink linkModal = new AjaxLink<>("lkModal") {
                    @Override
                    public void onClick(AjaxRequestTarget ajaxRequestTarget) {
                        modal.show(true);
                        ajaxRequestTarget.add(modal);
                    }
                };
                item.add(linkModal);
            }
        };

        container = new WebMarkupContainer("container");
        container.setOutputMarkupId(true);
        container.add(listview);
        add(container);

    }

    private Config loadConfig(boolean withClassProduction) {
        Config config = new Config() {
            @Override
            public Boolean assertionRoulette() {
                return true;
            }

            @Override
            public Boolean conditionalTestLogic() {
                return true;
            }

            @Override
            public Boolean constructorInitialization() {
                return true;
            }

            @Override
            public Boolean defaultTest() {
                return true;
            }

            @Override
            public Boolean dependentTest() {
                return true;
            }

            @Override
            public Boolean duplicateAssert() {
                return true;
            }

            @Override
            public Boolean eagerTest() {
                return withClassProduction;
            }

            @Override
            public Boolean emptyTest() {
                return true;
            }

            @Override
            public Boolean exceptionCatchingThrowing() {
                return true;
            }

            @Override
            public Boolean generalFixture() {
                return true;
            }

            @Override
            public Boolean mysteryGuest() {
                return true;
            }

            @Override
            public Boolean printStatement() {
                return true;
            }

            @Override
            public Boolean redundantAssertion() {
                return true;
            }

            @Override
            public Boolean sensitiveEquality() {
                return true;
            }

            @Override
            public Boolean verboseTest() {
                return true;
            }

            @Override
            public Boolean sleepyTest() {
                return true;
            }

            @Override
            public Boolean lazyTest() {
                return withClassProduction;
            }

            @Override
            public Boolean unknownTest() {
                return true;
            }

            @Override
            public Boolean ignoredTest() {
                return true;
            }

            @Override
            public Boolean resourceOptimism() {
                return true;
            }

            @Override
            public Boolean magicNumberTest() {
                return true;
            }

            @Override
            public Integer maxStatements() {
                return 30;
            }
        };

        return config;
    }

    private Map<String, String> descriptions = new HashMap<>();

    private void loadDescriptions() {

        descriptions.put("Unknown Test", "A test method without a assertion condition, the test will always be valid, not resulting in an exception. This programming practice makes it difficult to understand the test.");
        descriptions.put("Sleepy Test", "Developers introduce this test smell when they need to pause the execution of instructions in a test method for a certain period and continue the execution.");
        descriptions.put("Assertion Roulette", "This test smell occurs when the test method has a series of assertions without a description. If an assertion fails, it is not known which one generated the failure and its reason.");
        descriptions.put("Conditional Test Logic", "Tests containing conditional logic (IF instructions or loops).");
        descriptions.put("Redundant Assertion", "This smell occurs when the test methods contain assertion statements that are always true or false. A test is intended to return a binary result, regardless of whether the desired result is correct or not, and must not return the same output, regardless of the input.");
        descriptions.put("Sensitive Equality", "It is quick and easy to write equality checks using 'string'. A typical way is to calculate a real result, map it to a string, which is then compared to a literal string that represents the expected value. Such tests, however, can depend on many irrelevant details, such as commas, quotes, spaces, etc. Whenever a 'string' is changed, the tests start to fail. The solution is to replace the equality checks using 'string' with real equality checks.");
        descriptions.put("Duplicate Assert", "This smell occurs when a test method tests the same condition several times on the same test method.");
        descriptions.put("Constructor Initialization", "Test methods that feature a constructor. Ideally, the test suite should not have a constructor. The initialization of the fields must be in the setUp() method. Developers who are unaware of the purpose of the setUp() method would allow this test smell by creating a constructor for the test suite.");
        descriptions.put("IgnoredTest", "Starting with JUnit 4, developers are provided with the ability to prevent the execution of test methods. However, these ignored test methods result in overhead in terms of compilation time and an increase in code complexity and understanding time.");
        descriptions.put("Resource Optimism", "Test code that makes optimistic assumptions about the existence or absence of a particular external resource, and the state of that external resource (such as private directories or database tables) can cause non-deterministic behavior in the test results. The situation in which the tests run well at one time and fail at another is not a situation that the test should take place.");
        descriptions.put("Magic Number Test", "Many 'Magic Numbers' or Strings used when creating objects that are likely to result in an unrepeatable test.");
        descriptions.put("EmptyTest", "Test methods that do not contain executable instructions.");
        descriptions.put("Exception Catching Throwing", "This test smell occurs when the approval or disapproval of a test method explicitly depends on the production method that generates an exception.");
        descriptions.put("General Fixture", "In the JUnit framework, a programmer can write a 'setUp()' method that will be executed before each test method to create an environment for the tests to be run. The test smell becomes evident when the 'setUp()' environment is very general and the tests only need part of this configuration. The 'setUp()' methods start to get big and their understanding is reduced, and with the addition of functions, it starts to get slow. The danger of having a test that takes too long to complete, interfering with the development process, encourages programmers not to run the tests.");
        descriptions.put("Mystery Guest", "When a test uses external resources, such as a file necessary for its execution, this external resource does not make the test autonomous. Consequently, there is not enough information to understand the tested functionality, making it difficult to use this test as documentation. In addition, these external resources can be shared. And its use introduces hidden dependencies: if any force changes or excludes this feature, the tests begin to fail.");
        descriptions.put("Print Statement", "The printing instructions in the unit tests are redundant, as the unit tests are performed as part of an automated script. It consumes resources or increases the execution time.");
        descriptions.put("Lazy Test", "This test smell occurs when several test methods check the same method using the same equipment (but, for example, they check the values of different instance variables). These tests are usually meaningful only when considered together.");
        descriptions.put("Eager Test", "When a test method checks several methods of the object to be tested, it is difficult to read and understand and, therefore, it is more difficult to use as documentation. In addition, it makes tests more dependent on each other and more difficult to maintain.");
        descriptions.put("Verbose Test", "Excess test code or Conditional Test Logic. Difficult to verify its accuracy and more likely to contain errors.");

    }

    private String getLines(String range) {

        StringBuffer lines = new StringBuffer();

        if (range.contains(",")) {
            String[] r = range.split(",");

            for (String number : r) {
                if (!number.isBlank()) {

                    if (number.contains("-")) {
                        getLinesByRange(lines, number);
                    } else {
                        Integer line = Integer.parseInt(number.trim());
                        lines.append(getLine(line - 2));
                        lines.append(getLine(line - 1));
                        lines.append("<b>" + fileInList.get(line) + "</b><br>");
                        lines.append(getLine(line + 1));
                        lines.append(getLine(line + 2));
                    }
                }
            }

        } else if (range.contains("-")) {
            getLinesByRange(lines, range);

        } else {
            Integer line = Integer.parseInt(range);
            lines.append(getLine(line - 2));
            lines.append(getLine(line - 1));
            lines.append("<b>" + fileInList.get(line) + "</b><br>");
            lines.append(getLine(line + 1));
            lines.append(getLine(line + 2));
        }

        return lines.toString();
    }

    private void getLinesByRange(StringBuffer lines, String range) {
        String[] r = range.trim().split("-");
        Integer start = Integer.parseInt(r[0]);
        Integer end = Integer.parseInt(r[1]);
        if (start == end) {
            lines.append(getLine(start - 2));
            lines.append(getLine(start - 1));
            lines.append("<b>" + fileInList.get(start) + "</b><br>");
            lines.append(getLine(start + 1));
            lines.append(getLine(start + 2));
        } else {
            lines.append(getLine(start - 2));
            lines.append(getLine(start - 1));
            fileInList.subList(start, end + 1).stream().forEach(line -> lines.append("<b>" + line + "</b><br>"));
            lines.append(getLine(end + 2));
            lines.append(getLine(end + 3));
        }
    }

    private String getLine(int line) {
        if (line > 0 && line < fileInList.size()) {
            return fileInList.get(line) + "<br>";
        } else {
            return "";
        }
    }

}




