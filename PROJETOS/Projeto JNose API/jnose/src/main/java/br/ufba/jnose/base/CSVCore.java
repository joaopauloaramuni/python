package br.ufba.jnose.base;

import org.apache.wicket.protocol.http.WebApplication;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public class CSVCore {

    private static String outputFile;
    private static FileWriter writer;

    private static String pathAppToWebapp;
    private static String reportPath;

    public static void load(WebApplication webApplication){
        pathAppToWebapp = webApplication.getServletContext().getRealPath("");
        reportPath = pathAppToWebapp + File.separatorChar + "reports" + File.separatorChar;
    }

    public static String criarTestmappingdetectorCSV(List<List<String>> todasLinhas, String pastaDataHora, String nomeProjeto){
        return criarCSV(todasLinhas,pastaDataHora,nomeProjeto + "_testmappingdetector");
    }

    public static String criarTestSmellsdetectorCSV(List<List<String>> todasLinhas, String pastaDataHora, String nomeProjeto){
        return criarCSV(todasLinhas,pastaDataHora,nomeProjeto + "_testsmesll");
    }

    public static String criarCoberturaCSV(List<List<String>> todasLinhas, String pastaDataHora){
        return criarCSV(todasLinhas,pastaDataHora,"ClassInfor");
    }

    public static String criarEvolution1CSV(List<List<String>> todasLinhas, String pastaDataHora, String nomeProjeto){
        return criarCSV(todasLinhas,pastaDataHora,nomeProjeto + "_testsmell_evolution1");
    }

    public static String criarEvolution2CSV(List<List<String>> todasLinhas, String pastaDataHora, String nomeProjeto){
        return criarCSV(todasLinhas,pastaDataHora,nomeProjeto +"_testsmell_evolution2");
    }

    public static String criarCSV(List<List<String>> todasLinhas,String pastaDataHora, String nomeArquivo){
        String outFolder = reportPath + pastaDataHora;
        String outFile = reportPath + pastaDataHora + File.separatorChar + nomeArquivo + ".csv";

        new File(outFolder).mkdirs();

        loadResultsWrite(outFile);

        for (List<String> linha : todasLinhas){
            writeLine(linha);
        }

        return getOutputFile();
    }

    private static void loadResultsWrite(String outputFile){
        CSVCore.outputFile = outputFile;
        try {
            new File(outputFile).createNewFile();
            writer = new FileWriter(outputFile,false);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static String getOutputFile() {
        return outputFile;
    }

    private static void writeLine(List<String> dataValues) {
        try {
            writer = new FileWriter(outputFile, true);

            for (int i = 0; i < dataValues.size(); i++) {
                if(dataValues.get(i) == null){
                    dataValues.set(i,"");
                }
                writer.append(dataValues.get(i).replace("\n", "").replace("\r", ""));

                if (i != dataValues.size() - 1)
                    writer.append(";");
                else
                    writer.append(System.lineSeparator());

            }
            writer.flush();
            writer.close();
        }catch (Exception e){
            e.printStackTrace();
        }
    }

}