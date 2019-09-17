#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <tuple>

//BST
#include "BST.cpp"

// boost modules
#include <boost/python.hpp>
#include <boost/python/list.hpp>
#include <boost/python/extract.hpp>

#include "dataframe.h"


// criando uma estrutura de dados (coluna do DataFrame)
struct column{
    char kind;  // tipo de dado na coluna
    void *pcol;  // ponteiro que aponta para a coluna
};

// definindo funções para inserir coluna 
void DataFrame::addIntColumn(boost::python::list& l, std::string column_name){
    std::vector<int> w;
    int token;
    for (int i = 0; i < len(l) ; i++){
        token = boost::python::extract<int>(l[i]);
        w.push_back(token);
    }
    intColumn[column_name] = w;
}
void DataFrame::addDoubleColumn(boost::python::list& l, std::string column_name){
    std::vector<double> w;
    double token;
    for (int i = 0; i < len(l) ; i++){
        token = boost::python::extract<double>(l[i]);
        w.push_back(token);
    }
    doubleColumn[column_name] = w;
}
void DataFrame::addStringColumn(boost::python::list& l, std::string column_name){
    std::vector<std::string> w;
    std::string token;
    for (int i = 0; i < len(l) ; i++){
        token = boost::python::extract<std::string>(l[i]);
        w.push_back(token);
    }
    stringColumn[column_name] = w;
}

// Funções para remover colunas
void DataFrame::popIntColumn(boost::python::list& l, std::string column_name){
    intColumn.erase(column_name);
}
void DataFrame::popDoubleColumn(boost::python::list& l, std::string column_name){
    doubleColumn.erase(column_name);
}
void DataFrame::popStringColumn(boost::python::list& l, std::string column_name){
    stringColumn.erase(column_name);
}

// funções para acessar colunas
boost::python::list DataFrame::getIntColumn(std::string column_name){
    boost::python::list l;
    for (auto i: intColumn[column_name])
    {
        l.append(i);
    }
    return l;
}
boost::python::list DataFrame::getDoubleColumn(std::string column_name){
    boost::python::list l;
    for (auto i: doubleColumn[column_name])
    {
        l.append(i);
    }
    return l;
}
boost::python::list DataFrame::getStringColumn(std::string column_name){
    boost::python::list l;
    for (auto i: stringColumn[column_name])
    {
        l.append(i);
    }
    return l;
}
boost::python::list DataFrame::getIntRow(boost::python::list & rows, std::string column_name){
    int row;
    boost::python::list result;
    for (int i = 0; i < len(rows) ; i++){
        row = boost::python::extract<int>(rows[i]);
        result.append(intColumn[column_name][row]);
    }
    return result;
}

boost::python::list DataFrame::getDoubleRow(boost::python::list & rows, std::string column_name){
    int row;
    boost::python::list result;
    for (int i = 0; i < len(rows) ; i++){
        row = boost::python::extract<int>(rows[i]);
        result.append(doubleColumn[column_name][row]);
    }
    return result;
}

boost::python::list DataFrame::getStringRow(boost::python::list & rows, std::string column_name){
    int row;
    boost::python::list result;
    for (int i = 0; i < len(rows) ; i++){
        row = boost::python::extract<int>(rows[i]);
        result.append(stringColumn[column_name][row]);
    }
    return result;
}
void DataFrame::addIntRow(boost::python::list& l, std::string column_name){
    for (int i = 0; i < len(l) ; i++){
           intColumn[column_name].push_back(boost::python::extract<int>(l[i]));
       }
}
void DataFrame::addDoubleRow(boost::python::list& l, std::string column_name){
    for (int i = 0; i < len(l) ; i++){
           doubleColumn[column_name].push_back(boost::python::extract<double>(l[i]));
       }
}
void DataFrame::addStringRow(boost::python::list& l, std::string column_name){
    for (int i = 0; i < len(l) ; i++){
           stringColumn[column_name].push_back(boost::python::extract<std::string>(l[i]));
       }
}

boost::python::list DataFrame::getIntNode(boost::python::list & nodes, std::string column_name){
    std::vector<int> out;
    std::set<int> s;
    int w;
    boost::python::list result;

    for (int i = 0; i < len(nodes) ; i++){
        w = boost::python::extract<int>(nodes[i]);
        s = intTrees[column_name].getRows(w);
        out.insert(out.end(), s.begin(), s.end());
    }
    for (int i = 0; i < out.size() ; i++)
    {
        result.append(out[i]);
    }
    return result;
}

boost::python::list DataFrame::getDoubleNode(boost::python::list & nodes, std::string column_name){
    std::vector<int> out;
    std::set<int> s;
    double w;
    boost::python::list result;

    for (int i = 0; i < len(nodes) ; i++){
        w = boost::python::extract<double>(nodes[i]);
        s = doubleTrees[column_name].getRows(w);
        out.insert(out.end(), s.begin(), s.end());
    }
    for (int i = 0; i < out.size() ; i++)
    {
        result.append(out[i]);
    }
    return result;
}

boost::python::list DataFrame::getStringNode(boost::python::list & nodes, std::string column_name){
    std::vector<int> out;
    std::set<int> s;
    std::string w;
    boost::python::list result;

    for (int i = 0; i < len(nodes) ; i++){
        w = boost::python::extract<std::string>(nodes[i]);
        s = stringTrees[column_name].getRows(w);
        out.insert(out.end(), s.begin(), s.end());
    }
    for (int i = 0; i < out.size() ; i++)
    {
        result.append(out[i]);
    }
    return result;
}


void DataFrame::indexIntCol(boost::python::list & l,std::string column_name){
    BST<int> Tree;
    for (int i = 0; i < intColumn[column_name].size(); ++i)
    {
        Tree.insertRowNode(intColumn[column_name][i],i);
    }
    intTrees[column_name] = Tree;
}
void DataFrame::indexDoubleCol(boost::python::list & l,std::string column_name){
    BST<double> Tree;
    for (int i = 0; i < doubleColumn[column_name].size(); ++i)
    {
        Tree.insertRowNode(doubleColumn[column_name][i],i);
    }
    doubleTrees[column_name] = Tree;
}
void DataFrame::indexStringCol(boost::python::list & l,std::string column_name){
    BST<std::string> Tree;
    for (int i = 0; i < stringColumn[column_name].size(); ++i)
    {
        Tree.insertRowNode(stringColumn[column_name][i],i);
    }
    stringTrees[column_name] = Tree;
}


// Exportando funções para o Python
using namespace boost::python;

BOOST_PYTHON_MODULE(dataframe){
    class_<DataFrame>("dataframe",init<>())
    .def_readwrite("check", & DataFrame::check)
    .def("addIntColumn", & DataFrame::addIntColumn)
    .def("addDoubleColumn", & DataFrame::addDoubleColumn)
    .def("addStringColumn", & DataFrame::addStringColumn)
    .def("popIntColumn", & DataFrame::popIntColumn)
    .def("popDoubleColumn", & DataFrame::popIntColumn)
    .def("popStringColumn", & DataFrame::popIntColumn)
    .def("getIntColumn", & DataFrame::getIntColumn)
    .def("getDoubleColumn", & DataFrame::getDoubleColumn)
    .def("getStringColumn", & DataFrame::getStringColumn)
    .def("addIntRow", & DataFrame::addIntRow)
    .def("addDoubleRow", & DataFrame::addDoubleRow)
    .def("addStringRow", & DataFrame::addStringRow)
    .def("getIntRow", & DataFrame::getIntRow)
    .def("getDoubleRow", & DataFrame::getDoubleRow)
    .def("getStringRow", & DataFrame::getStringRow)
    .def("getStringNode", & DataFrame::getIntNode)
    .def("getStringNode", & DataFrame::getDoubleNode)
    .def("getStringNode", & DataFrame::getStringNode)
    .def("indexIntCol", & DataFrame::indexIntCol)
    .def("indexDoubleCol", & DataFrame::indexDoubleCol)
    .def("indexStringCol", & DataFrame::indexStringCol)
    .def_readwrite("intColumn", & DataFrame::intColumn)
    ;
}