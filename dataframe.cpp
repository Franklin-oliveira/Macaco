#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <tuple>

// boost modules
#include <boost/python.hpp>
#include <boost/python/list.hpp>
#include <boost/python/extract.hpp>

// declaring namespace to shorten code
// using namespace boost::python;



// criando uma estrutura de dados (coluna do DataFrame)
struct column{
    char kind;  // tipo de dado na coluna
    void *pcol;  // ponteiro que aponta para a coluna
};

// criando a classe dataframe
class DataFrame{
public:
    // definindo colunas do dataframe (uma linha para cada tipo: string, int e float)
    std::map<std::string, std::vector<int>> intColumn;
    std::map<std::string, std::vector<double>> doubleColumn;
    std::map<std::string, std::vector<std::string>> stringColumn; 

    std::string check = "nothing";

    // funções para inserir colunas (atributos do dataframe)
    void addIntColumn(boost::python::list& l, std::string column_name);
    void addDoubleColumn(boost::python::list& l, std::string column_name);
    void addStringColumn(boost::python::list& l, std::string column_name);

    // funções para remover colunas (pop ou remove)
    void popIntColumn(boost::python::list& l, std::string column_name);
    void popDoubleColumn(boost::python::list& l, std::string column_name);
    void popStringColumn(boost::python::list& l, std::string column_name);

    // funções para acessar colunas
    boost::python::list getIntColumn(std::string column_name);
    boost::python::list getDoubleColumn(std::string column_name);
    boost::python::list getStringColumn(std::string column_name);
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
    .def_readwrite("intColumn", & DataFrame::intColumn)
    ;
}