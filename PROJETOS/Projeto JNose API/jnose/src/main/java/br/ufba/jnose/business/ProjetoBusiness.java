package br.ufba.jnose.business;

import br.ufba.jnose.business.daos.ProjectDao;
import br.ufba.jnose.business.daos.utils.BusinessGeneric;
import br.ufba.jnose.entities.Projeto;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;
import java.util.List;
import static java.util.stream.Collectors.toList;

@Component
@Transactional
public class ProjetoBusiness extends BusinessGeneric<ProjectDao, Projeto> {
    public List<Projeto> listAllWithFilter(){
        return dao.listAll().stream().filter(o -> !o.getJunitVersion().equals("None")).collect(toList());
    }
}
