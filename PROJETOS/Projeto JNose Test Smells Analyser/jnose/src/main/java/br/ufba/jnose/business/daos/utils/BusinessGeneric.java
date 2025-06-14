package br.ufba.jnose.business.daos.utils;

import org.hibernate.criterion.Order;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.transaction.annotation.Transactional;

import java.io.Serializable;
import java.util.List;

@Transactional
public class BusinessGeneric<T extends DAOGeneric, Y extends Serializable> {

    @Autowired
    protected T dao;

    public int size() {
        return dao.size();
    }

    public void save(Y u) {
        dao.save(u);
    }

    public void delete(Y u) {
        dao.delete(u);
    }

    public void delete(Long id) {
        dao.delete(id);
    }

    public List<Y> find(Long first, Long count) {
        return dao.findByHQL(Order.desc("id"), first.intValue(), count.intValue());
    }

    public Y find(Long id) {
        return (Y) dao.findById(id);
    }

    public List<Y> listAll() {
        return dao.listAll();
    }

}

