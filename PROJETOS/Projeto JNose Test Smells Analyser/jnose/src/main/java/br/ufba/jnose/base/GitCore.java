package br.ufba.jnose.base;

import br.ufba.jnose.WicketApplication;
import br.ufba.jnose.dtolocal.Commit;
import br.ufba.jnose.dtolocal.ProjetoDTO;
import org.apache.commons.io.FileUtils;
import org.eclipse.jgit.api.BlameCommand;
import org.eclipse.jgit.api.Git;
import org.eclipse.jgit.api.LogCommand;
import org.eclipse.jgit.api.errors.GitAPIException;
import org.eclipse.jgit.blame.BlameResult;
import org.eclipse.jgit.diff.RawText;
import org.eclipse.jgit.lib.ObjectId;
import org.eclipse.jgit.lib.PersonIdent;
import org.eclipse.jgit.lib.Ref;
import org.eclipse.jgit.lib.Repository;
import org.eclipse.jgit.revwalk.RevCommit;
import org.kohsuke.github.GHRepository;
import org.kohsuke.github.GitHub;

import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.*;

public class GitCore {

    public static void main(String[] args) {
        GitCore.getStarts("hub4j/github-api");
    }

    /**
     * Retorna a quantidade de estrelas do projeto
     * @param repoLocal path do repo local
     * @return
     */
    public static Integer getStarts(String repoLocal){

        String url = getURL(repoLocal);
        String repoName = getNameByGithub(url);

        Integer stars = 0;
        try {
            GitHub github = GitHub.connectAnonymously();
            GHRepository repo = github.getRepository(repoName);
            stars = repo.getStargazersCount();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return stars;
    }


    private static String getNameByGithub(String path_) {
        String owner_ = "";

        path_ = path_.replace(".git","");

        if(path_.endsWith("/")){
            path_ = path_.substring(0,path_.length()-1);
        }

        String projeto_ = path_.substring(path_.lastIndexOf("/")+1,path_.length());
        owner_ = path_.substring(0,path_.lastIndexOf("/"));
        owner_ = owner_.substring(owner_.lastIndexOf("/")+1,owner_.length());

        return owner_ + "/" + projeto_;
    }

    public static ProjetoDTO gitClone(String repoURL) {
        String repoName = "";
        if (repoURL.contains(".git")) {
            repoName = repoURL.substring(repoURL.lastIndexOf("/") + 1, repoURL.lastIndexOf("."));
        } else {
            int x = repoURL.lastIndexOf("/");
            int size = repoURL.length();
            if (x == size - 1) {
                repoURL = repoURL.substring(0, repoURL.length() - 2);
                repoName = repoURL.substring(repoURL.lastIndexOf("/") + 1, repoURL.length());
            } else {
                repoName = repoURL.substring(repoURL.lastIndexOf("/") + 1, repoURL.length());
            }

        }
        File file = null;
        try {
            file = new File(WicketApplication.JNOSE_PROJECTS_FOLDER + repoName);
            if (file.exists()) {
                FileUtils.deleteDirectory(file);
            }
            Git git = Git.cloneRepository()
                    .setURI(repoURL)
                    .setDirectory(file)
                    .call();
        } catch (GitAPIException | IOException e) {
            e.printStackTrace();
        }

        br.ufba.jnose.entities.Projeto projetoBean = new br.ufba.jnose.entities.Projeto();
        projetoBean.setName(repoName);
        projetoBean.setPath(file.getPath());
        ProjetoDTO projeto = new ProjetoDTO(projetoBean);

        return projeto;
    }

    public static ArrayList<Commit> gitLogOneLine(String pathExecute) {

        ArrayList<Commit> lista = new ArrayList<>();
        try {
            Git git = Git.open(new File(pathExecute));
            git.log().all().call().forEach(revCommit -> {
                        PersonIdent authorIdent = revCommit.getAuthorIdent();
                        Date authorDate = authorIdent.getWhen();
                        TimeZone authorTimeZone = authorIdent.getTimeZone();

                        lista.add(new Commit(
                                revCommit.getId().getName(),
                                authorIdent.getName(),
                                authorDate,
                                revCommit.getFullMessage()));
                    }
            );
        } catch (Exception e) {
            e.printStackTrace();
        }

        return lista;
    }

    public static ArrayList<Commit> gitTags(String pathExecute) {

        ArrayList<Commit> lista = new ArrayList<>();

        try {
            Git git = Git.open(new File(pathExecute));

            List<Ref> call = git.tagList().call();
            for (Ref ref : call) {
                System.out.println("Tag: " + ref + " " + ref.getName() + " " + ref.getObjectId().getName());

                LogCommand log = git.log();

                Ref peeledRef = git.getRepository().peel(ref);
                if (peeledRef.getPeeledObjectId() != null) {
                    log.add(peeledRef.getPeeledObjectId());
                } else {
                    log.add(ref.getObjectId());
                }

                Iterable<RevCommit> logs = log.call();
                for (RevCommit revCommit : logs) {
                    PersonIdent authorIdent = revCommit.getAuthorIdent();
                    Date authorDate = authorIdent.getWhen();
                    TimeZone authorTimeZone = authorIdent.getTimeZone();
                    System.out.println(authorDate + " - Commit: " + revCommit + ", name: " + revCommit.getName() + ", id: " + revCommit.getId().getName());

                    lista.add(new Commit(
                            revCommit.getId().getName(),
                            authorIdent.getName(),
                            authorDate,
                            revCommit.getFullMessage(),
                            ref.getName()));
                    break;
                }
            }

        } catch (Exception e) {
            e.printStackTrace();
        }

        return lista;
    }

    public static void checkout(String commitId, String projetoPath) {
        try {
            Git git = Git.open(new File(projetoPath));
            git.checkout().setForced(true).setName(commitId).call();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static String getURL(String projetoPath) {
        String url = "";
        try {
            Git git = Git.open(new File(projetoPath));
            url = git.getRepository().getConfig().getString("remote", "origin", "url");
        } catch (Exception e) {
            e.printStackTrace();
        }
        return url;
    }

    public static String branch(String projetoPath) {
        String branchcurrent = "";
        try {
            Git git = Git.open(new File(projetoPath));
            branchcurrent = git.getRepository().getBranch();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return branchcurrent;
    }

    public static void pull(String projetoPath) {
        try {
            Git git = Git.open(new File(projetoPath));
            git.pull().call();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static Map<Integer,String> blame(String projetoPath, String filePathAbsolut) {

        Map<Integer,String> retorno = new HashMap<>();

        String filePathRepo = filePathAbsolut.replace(projetoPath+"/","");

        Git git = null;
        try {

            final SimpleDateFormat DATE_FORMAT = new SimpleDateFormat("YYYY-MM-dd HH:mm");

            git = Git.open(new File(projetoPath));
            BlameCommand blameCommand = git.blame();
            blameCommand.setStartCommit(git.getRepository().resolve("HEAD"));
            blameCommand.setFilePath(filePathRepo);
            BlameResult result = blameCommand.call();

//            System.out.println("Blaming " + filePath);
//            final BlameResult result = git.blame().setFilePath(filePath)
//                    .setTextComparator(RawTextComparator.WS_IGNORE_ALL).call();
            final RawText rawText = result.getResultContents();

            for (int i = 0; i < rawText.size(); i++) {
                final PersonIdent sourceAuthor = result.getSourceAuthor(i);
                final RevCommit sourceCommit = result.getSourceCommit(i);
                System.out.println(sourceAuthor.getName() +
                        (sourceCommit != null ? " - " + DATE_FORMAT.format(((long) sourceCommit.getCommitTime()) * 1000) +
                                " - " + sourceCommit.getName() : "") +
                        ": " + rawText.getString(i));

                retorno.put(i+1,sourceAuthor.getName());

            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        return retorno;
    }

    public static BlameResult getBlameResultForFile(String projetoPath, String filePath) {
        BlameResult blame = null;
        Git git = null;
        try {
            git = Git.open(new File(projetoPath));
            Iterable<RevCommit> lista = git.log().all().call();
            Repository jgitRepository = git.getRepository();
            BlameCommand blamer = new BlameCommand(jgitRepository);
            ObjectId commitID = jgitRepository.resolve("HEAD");
            blamer.setStartCommit(commitID);
            filePath = filePath.replace(projetoPath+"/","");
            blamer.setFilePath(filePath);
            blame = blamer.call();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return blame;
    }

}
