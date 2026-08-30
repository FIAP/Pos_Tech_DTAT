### Criacao do Source Table - Kafka #################################################################################
#   Autor: Vinicius Henrique dos Santos
#   Empresa: FIAP
#   Objetivo: Criar um source Table apontando para um tópico Kafka
#####################################################################################################################    

import os
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, DataTypes, EnvironmentSettings, TableEnvironment
from pyflink.table.descriptors import Schema, Kafka, Json
from pyflink.table import expressions as expr


def main():

    ###############################################################
    # Cria o Stream Env e o Table Env
    ###############################################################

    env = StreamExecutionEnvironment.get_execution_environment()

    settings = EnvironmentSettings.new_instance()\
                      .in_streaming_mode()\
                      .use_blink_planner()\
                      .build()


    tbl_env = StreamTableEnvironment.create(stream_execution_environment=env,
                                            environment_settings=settings)
    
    kafka_jar = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            'flink-sql-connector-kafka_2.11-1.13.6.jar')

    tbl_env.get_config()\
            .get_configuration()\
            .set_string("pipeline.jars", "file://{}".format(kafka_jar))
    
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

    schema_eng = DataTypes.ROW([
        DataTypes.FIELD('engenheiro_resp', DataTypes.STRING()),
        DataTypes.FIELD('id_sensor', DataTypes.INT())
    ])
    tbl_eng = tbl_env.from_elements(sensores, schema_eng)
    tbl_env.create_temporary_view("tbl_eng", tbl_eng)
    print('\ntbl_eng schema')
    tbl_eng.print_schema()

    ###############################################################
    # Cria o Source Table 
    ###############################################################
    source_descriptor = Kafka(version="universal",
                              topic="dev_log_sensor",
                              start_from_earliest=False,
                              properties={
                                'zookeeper.connect': 'localhost:2181',
                                'bootstrap.servers': 'localhost:9092',
                                'group.id': 'g_dev_mysql'
                        })
    ###############################################################
    # Determina o formato os quais os dados serão lidos
    ###############################################################
    source_format = Json().fail_on_missing_field(True)\
                          .schema(DataTypes.ROW([
                            DataTypes.FIELD("id_log_sensor", DataTypes.STRING()),
                            DataTypes.FIELD("id_sensor", DataTypes.INT()),
                            DataTypes.FIELD("umidade", DataTypes.INT()),
                            DataTypes.FIELD("pressao", DataTypes.DOUBLE()),
                            DataTypes.FIELD("data", DataTypes.STRING())
                          ]))
    source_schema = Schema().field("id_log_sensor", DataTypes.STRING())\
                            .field("id_sensor", DataTypes.INT())\
                            .field("umidade", DataTypes.INT())\
                            .field("pressao", DataTypes.DOUBLE())\
                            .field("data", DataTypes.STRING())

    tbl_env.connect(source_descriptor)\
            .with_format(source_format)\
            .with_schema(source_schema)\
            .create_temporary_table('tb_log_sensor')
    
    


    ###############################################################################################################
    # O conector "blackhole" nos ajuda permitindo realizar testes sem necessariamente termos uma tabela de destino
    # Saiba mais em: https://nightlies.apache.org/flink/flink-docs-release-1.18/docs/connectors/table/blackhole/
    ###############################################################################################################

    tbl = tbl_env.from_path('tb_log_sensor')

    print("\nSchema Kafka para as informacoes de LOG DOS SENSORES")
    tbl.print_schema()

###########################################################################################
# Usa a TABLE API para selecionar todos os dados a medida em que eles vao caindo no tópico
# Aqui usamos o Limit para parar a captura dos dados. Teste tirar ou aumentar enquanto
# o seu seu produtor está ligado
###########################################################################################
    tb_sensores_01 = tbl_env.execute_sql("SELECT * FROM tb_log_sensor limit 20")
    with tb_sensores_01.collect() as tb_sensores_01:
     print('\nDados de: tb_sensores_01')
     for tb_sensores_01 in tb_sensores_01:
      print(tb_sensores_01)

########################################################################################
# Usa a TABLE API para calcular a média dos valores de temperatura e pressao por sensor
########################################################################################
    tb_sensores_02 = tbl_env.execute_sql(f"""SELECT 
                                            id_sensor, 
                                            avg(umidade) as avg_umidade, 
                                            avg(pressao) as avg_pressao  
                                         FROM tb_log_sensor 
                                         group by 
                                            id_sensor""")
    with tb_sensores_02.collect() as tb_sensores_02:
     print('\nDados de: tb_sensores_02')
     for tb_sensores_02 in tb_sensores_02:
      print(tb_sensores_02)

########################################################################################
# Usa a TABLE API para criar uma tabela realizando join com o "de para" de engenheiros
# criado previamente no script, seguindo o sugerido no 02_data_source_hardcode.py
########################################################################################
    tb_sensores_03 = tbl_env.execute_sql(f"""SELECT 
                                                a.id_sensor, 
                                                b.engenheiro_resp,
                                                avg(a.umidade) as avg_umidade, 
                                                avg(a.pressao) as avg_pressao  
                                            FROM tb_log_sensor a left join tbl_eng b
                                                on a.id_sensor = b.id_sensor
                                            group by 
                                                a.id_sensor,
                                                b.engenheiro_resp""")
    with tb_sensores_03.collect() as tb_sensores_03:
     print('\nDados de: tb_sensores_03')
     for tb_sensores_03 in tb_sensores_03:
      print(tb_sensores_03)


    tbl_env.execute('teste-kafka-source')

if __name__ == '__main__':
    main()

