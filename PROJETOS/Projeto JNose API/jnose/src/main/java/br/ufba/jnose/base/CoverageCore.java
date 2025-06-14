package br.ufba.jnose.base;

import br.ufba.jnose.base.cobertura.ReportGenerator;
import br.ufba.jnose.dtolocal.ProjetoDTO;

import java.io.File;

public class CoverageCore {

    public static void processarCobertura(ProjetoDTO projeto, String folderTime, String pastaPathReport, StringBuffer logRetorno) {
        logRetorno.append(Util.dateNow() + projeto.getName() + " - <font style='color:blue'>Coverage</font> <br>");
        try {
            Util.execCommand("mvn clean org.jacoco:jacoco-maven-plugin:prepare-agent install -Drat.skip=true", projeto.getPath());
            ReportGenerator reportGenerator = new ReportGenerator(new File(projeto.getPath()), new File(pastaPathReport + folderTime + File.separatorChar));
            reportGenerator.create();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
