### Criacao do Source Table - Kafka #################################################################################
#   Autor: Vinicius Henrique dos Santos
#   Empresa: FIAP
#   Objetivo: Criar um source Table apontando para um tópico Kafka
#####################################################################################################################    

import os
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, DataTypes, EnvironmentSettings
from pyflink.table.descriptors import Schema, Kafka, Json

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


    ###############################################################
    # Cria o Source Table 
    ###############################################################
    source_descriptor = Kafka(version="universal",
                              topic="productsales",
                              start_from_earliest=True,
                              properties={
                                'zookeeper.connect': 'localhost:2181',
                                'bootstrap.servers': 'localhost:9092',
                                'group.id': 'xxxx'
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
                            DataTypes.FIELD("data", DataTypes.TIMESTAMP(3))
                          ]))
    source_schema = Schema().field("id_log_sensor", DataTypes.STRING())\
                            .field("id_sensor", DataTypes.INT())\
                            .field("umidade", DataTypes.INT())\
                            .field("pressao", DataTypes.DOUBLE())\
                            .field("data", DataTypes.TIMESTAMP(3))

    tbl_env.connect(source_descriptor)\
            .with_format(source_format)\
            .with_schema(source_schema)\
            .create_temporary_table('tb_log_sensor')

    ###############################################################################################################
    # O conector "blackhole" nos ajuda permitindo realizar testes sem necessariamente termos uma tabela de destino
    # Saiba mais em: https://nightlies.apache.org/flink/flink-docs-release-1.18/docs/connectors/table/blackhole/
    ###############################################################################################################

    tbl_env.execute_sql("""
        CREATE TABLE blackhole (
                id_log_sensor VARCHAR,
                id_sensor INT,
                umidade INT,
                pressao DOUBLE,
                data TIMESTAMP
        ) WITH (
                'connector' = 'blackhole'
        )
    """)

    tbl = tbl_env.from_path('tb_log_sensor')

    print("\nSchema Kafka para as informacoes de LOG DOS SENSORES")
    tbl.print_schema()

    tbl.insert_into('blackhole')

    tbl_env.execute('kafka-source-demo')


if __name__ == '__main__':
    main()

