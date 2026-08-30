### Criando data Sink #######################################################################################################################
#   Autor: Vinicius Henrique dos Santos
#   Empresa: FIAP
#   Objetivo: Criar Source e Data Sink apontando para arquivos CSV de entrada e de Saida#
#############################################################################################################################################

from pyflink.table import EnvironmentSettings, TableEnvironment, StreamTableEnvironment, DataTypes, CsvTableSource, CsvTableSink, WriteMode
from pyflink.datastream import StreamExecutionEnvironment

def main():

### Nota do professor ######################################################################################################################
#   O script de criacao do data source precisa ser executado para que funcione o data sink, por conta disso um pedaco do script eh igual ao 
#   03_data_source_csv.py#
############################################################################################################################################

    env_settings = EnvironmentSettings.new_instance()\
                        .in_batch_mode()\
                        .use_blink_planner()\
                        .build()
    tbl_env = TableEnvironment.create(env_settings)

    tbl_env.get_config().get_configuration().set_string("parallelism.default", "1")

    in_field_names = ['id_sensor', 'umidade', 'pressao', 'data']
    in_field_types = [DataTypes.INT(), DataTypes.INT(), DataTypes.DOUBLE(), DataTypes.DATE()]
    source = CsvTableSource(
        '/home/fiap/flink/scripts/csv',  
        in_field_names,
        in_field_types,
        ignore_first_line=True
    )
    tbl_env.register_table_source('tb_log_sensor', source)

    tbl = tbl_env.from_path('tb_log_sensor')

    print('\nSchema tb_log_sensor')
    tbl.print_schema()

    out_field_names = ['sensor_id', 'umidade', 'pressao', 'data']
    out_field_types = [DataTypes.INT(), DataTypes.INT(), DataTypes.DOUBLE(), DataTypes.DATE()]
    sink = CsvTableSink(
        out_field_names,
        out_field_types,
        '/home/fiap/flink/scripts/csv-saida/log_csv_processado.csv',
        num_files=1,
        write_mode=WriteMode.OVERWRITE
    )
    tbl_env.register_table_sink('snk_log_csv', sink)

    tbl.insert_into('snk_log_csv')

    tbl_env.execute('source-demo')

if __name__ == '__main__':
    main()