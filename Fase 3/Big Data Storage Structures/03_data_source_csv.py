### Criando o TableEnviroment ##########################################################################################################################
#   Autor: Vinicius Henrique dos Santos
#   Empresa: FIAP
#   Objetivo: criar data sources a partir de arquivos csv
########################################################################################################################################################

from pyflink.table import DataTypes, TableEnvironment, EnvironmentSettings, CsvTableSource

def main():
    env_settings = EnvironmentSettings.new_instance()\
                        .in_batch_mode()\
                        .build()
    tbl_env = TableEnvironment.create(env_settings)

    field_names = ['id_sensor', 'umidade', 'pressao', 'data']
    field_types = [DataTypes.INT(), DataTypes.INT(), DataTypes.DOUBLE(), DataTypes.DATE()]
    source = CsvTableSource(
### Nota do Professor ################################################################################################################
#   o parametro "source_path", nesse caso recebe o valor ./csv, que eh o local na rede onde o csv estara depositado para a leitura
#   podendo haver 1 ou mais de 1 arquivo com esse mesmo layout. Eh fundamental manter apenas os arquivos csv nessa pasta sempre que
#   for usar csv como uma fonte de dados dentro do flink, do contrario recebera erros
######################################################################################################################################
        '/home/fiap/flink/scripts/csv',
        field_names,
        field_types,
        ignore_first_line=True
    )
    tbl_env.register_table_source('tb_log_sensor', source)

    tbl = tbl_env.from_path('tb_log_sensor')

    print('\nSchema tb_log_sensor: ')
    tbl.print_schema()

    print('\nDados: ')
    print(tbl.to_pandas())

if __name__ == '__main__':
    main()
