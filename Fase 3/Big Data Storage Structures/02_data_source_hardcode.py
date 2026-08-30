### Criando o TableEnviroment ##########################################################################################################################
#   Autor: Vinicius Henrique dos Santos
#   Empresa: FIAP
#   Objetivo: criar data sources a partir de hardcode via Python
########################################################################################################################################################

from pyflink.table import EnvironmentSettings, TableEnvironment, DataTypes

def main():
    settings = EnvironmentSettings.new_instance()\
                  .in_batch_mode()\
                  .build()
    tbl_env = TableEnvironment.create(settings)
### Lista com os valores de temperatura dos sensores (exemplo) ###
    sensores = [
        ('Joao', 1),
        ('Ana', 2),
        ('Maria', 3),
        ('Pedro', 4),
        ('Laura', 5),
        ('Carla', 6),
        ('Joao', 7),
        ('Ana', 8),
        ('Maria', 9),
        ('Pedro', 10)

    ]

### Nota do Professor ######################################################################################################################
#   Cria-se a tbl1 a partir da variavel de ambiente definida (tbl_env) previamente usando o metodo "from_elements" com a lista (sensores)
#   Voce pode trabalhar com listas, dicionarios, tuplas, ou arrays para construir sua tabela dessa forma.
#   
#   Veja detalhes da documentacao: https://nightlies.apache.org/flink/flink-docs-release-1.17/api/python/reference/pyflink.table/api/pyflink.table.table_environment.TableEnvironment.from_elements.html
#   
############################################################################################################################################

    tbl1 = tbl_env.from_elements(sensores)
    print('\ntbl1 schema')
    tbl1.print_schema()

    print('\ntbl1 data')

### Nota do Professor #####################################################################################################################
#   Voce pode colocar os seus dados de uma tabela flink para um dataframe pandas, o que pode ser muito util para se trabalhar e analisar
#   uma quantidade pequena de dados. Recomendo fortemente que voce nao considere isso trabalhando com grandes volumes (cenario mais comum
#   ao se usar o apache flink), pois o Flink normalmente roda em varios clusters trabalhando com memoria distribuida e o pandas concentra
#   todo o processamento necessario no cluster principal (nao paraleliza) o que pode impactar todos os jobs em execucao
###########################################################################################################################################
    
    print(tbl1.to_pandas())

### Nota do Professor #####################################################################################################################
#   Aqui estamos definindo a tbl2 pela definicao do "schema", onde passamos uma lista com o nome das colunas e a lista com os valores 
#   (sensores), por padrao o metodo from_elements (assim como na criacao da tbl1) infere e "tenta adivinhar" o tipo dos dados que estamos
#   passando para ele. 
###########################################################################################################################################  

    col_names = ['engenheiro_resp', 'id_sensor']
    tbl2 = tbl_env.from_elements(sensores, col_names)
    print('\ntbl2 schema')
    tbl2.print_schema()

    print('\ntbl2 data')
    print(tbl2.to_pandas())

### Nota do professor ######################################################################################################################
#   Essa eh a melhor forma de se criar uma fonte de dados originada de um objeto Python, pois usamos a classe DataTypes e o metodo ROW para 
#   definir explicitamente quais sao os tipos de cada variavel da nossa tabela. Depois disso passamos a lista de valores e o "schema" no 
#   metodo from_elements para criar a tbl3
############################################################################################################################################
    
    schema = DataTypes.ROW([
        DataTypes.FIELD('engenheiro_resp', DataTypes.STRING()),
        DataTypes.FIELD('id_sensor', DataTypes.INT())
    ])
    tbl3 = tbl_env.from_elements(sensores, schema)
    print('\ntbl3 schema')
    tbl3.print_schema()

    print('\ntbl3 data')
    print(tbl3.to_pandas())



if __name__ == '__main__':
    main()