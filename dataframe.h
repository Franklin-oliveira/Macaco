#ifndef DATAFRAME_H
#define DATAFRAME_H

// criando a classe dataframe
class DataFrame{
public:
    // COLUNAS
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


    // LINHAS
    // funções para acessar linhas
    void addIntRow(boost::python::list& l, std::string column_name);
    void addDoubleRow(boost::python::list& l, std::string column_name);
    void addStringRow(boost::python::list& l, std::string column_name);
    
    // retorna linhas do dataframe
    boost::python::list getIntRow(boost::python::list & rows, std::string column_name);
    boost::python::list getDoubleRow(boost::python::list & rows, std::string column_name);
    boost::python::list getStringRow(boost::python::list & rows, std::string column_name);


    // BST
    std::map<std::string,BST<int>> intTrees;
    std::map<std::string,BST<double>> doubleTrees;
    std::map<std::string,BST<std::string>> stringTrees;

    // retorna nós da BST
    boost::python::list getIntNode(boost::python::list & nodes, std::string column_name);
    boost::python::list getDoubleNode(boost::python::list & nodes, std::string column_name);
    boost::python::list getStringNode(boost::python::list & nodes, std::string column_name);


    // Cria índice para as colunas
    void indexIntCol(boost::python::list& l, std::string column_name);
    void indexDoubleCol(boost::python::list& l, std::string column_name);
    void indexStringCol(boost::python::list& l, std::string column_name);
};


#endif