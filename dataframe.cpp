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
    void InsertIntColumn(boost::python::list& l, std::string column_name);
    void InsertDoubleColumn(boost::python::list& l, std::string column_name);
    void InsertStringColumn(boost::python::list& l, std::string column_name);

    // funções para remover colunas (pop ou remove)
    void PopIntColumn(boost::python::list& l, std::string column_name);
    void PopDoubleColumn(boost::python::list& l, std::string column_name);
    void PopStringColumn(boost::python::list& l, std::string column_name);

    // funções para acessar colunas
    boost::python::list GetIntColumn(std::string column_name);
    boost::python::list GetDoubleColumn(std::string column_name);
    boost::python::list GetStringColumn(std::string column_name);
};


// definindo funções para inserir coluna 
void DataFrame::InsertIntColumn(boost::python::list& l, std::string column_name){
    std::vector<int> w;
    int token;
    for (int i = 0; i < len(l) ; i++){
        token = boost::python::extract<int>(l[i]);
        w.push_back(token);
    }
    intColumn[column_name] = w;
}
void DataFrame::InsertDoubleColumn(boost::python::list& l, std::string column_name){
    std::vector<double> w;
    double token;
    for (int i = 0; i < len(l) ; i++){
        token = boost::python::extract<double>(l[i]);
        w.push_back(token);
    }
    doubleColumn[column_name] = w;
}
void DataFrame::InsertStringColumn(boost::python::list& l, std::string column_name){
    std::vector<std::string> w;
    std::string token;
    for (int i = 0; i < len(l) ; i++){
        token = boost::python::extract<std::string>(l[i]);
        w.push_back(token);
    }
    stringColumn[column_name] = w;
}

// Funções para remover colunas
void DataFrame::PopIntColumn(boost::python::list& l, std::string column_name){
    intColumn.erase(column_name);
}
void DataFrame::PopDoubleColumn(boost::python::list& l, std::string column_name){
    doubleColumn.erase(column_name);
}
void DataFrame::PopStringColumn(boost::python::list& l, std::string column_name){
    stringColumn.erase(column_name);
}

// funções para acessar colunas
boost::python::list DataFrame::GetIntColumn(std::string column_name){
    boost::python::list l;
    for (auto i: intColumn[column_name])
    {
        l.append(i);
    }
    return l;
}
boost::python::list DataFrame::GetDoubleColumn(std::string column_name){
    boost::python::list l;
    for (auto i: doubleColumn[column_name])
    {
        l.append(i);
    }
    return l;
}
boost::python::list DataFrame::GetStringColumn(std::string column_name){
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
    .def("InsertIntColumn", & DataFrame::InsertIntColumn)
    .def("InsertDoubleColumn", & DataFrame::InsertDoubleColumn)
    .def("InsertStringColumn", & DataFrame::InsertStringColumn)
    .def("PopIntColumn", & DataFrame::PopIntColumn)
    .def("PopDoubleColumn", & DataFrame::PopIntColumn)
    .def("PopStringColumn", & DataFrame::PopIntColumn)
    .def("GetIntColumn", & DataFrame::GetIntColumn)
    .def("GetDoubleColumn", & DataFrame::GetDoubleColumn)
    .def("GetStringColumn", & DataFrame::GetStringColumn)
    .def_readwrite("intColumn", & DataFrame::intColumn)
    ;
}