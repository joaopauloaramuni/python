package br.ufba.jnose;

import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.List;

import br.ufba.jnose.base.JNose;

public class JNoseCLI {

    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Uso: java br.ufba.jnose.JNoseCLI <diretorioProjeto> <arquivoSaidaCSV>");
            System.exit(1);
        }

        String pathProjeto = args[0];
        String arquivoSaida = args[1];

        StringBuffer logRetorno = new StringBuffer();

        System.out.println("🔍 Processando projeto: " + pathProjeto);

        try {
            List<List<String>> resultado = JNose.processarTestSmellDetector2(pathProjeto, logRetorno);

            System.out.println("✅ Análise concluída. Gerando CSV: " + arquivoSaida);

            try (PrintWriter pw = new PrintWriter(new FileWriter(arquivoSaida))) {
                for (List<String> linha : resultado) {
                    pw.println(String.join(",", linha));
                }
            }

            System.out.println("✅ CSV gerado com sucesso!");
            System.out.println("📄 Log de execução:");
            System.out.println(logRetorno.toString());

        } catch (Exception e) {
            System.err.println("❌ Erro ao processar: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
