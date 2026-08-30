### Criando o TableEnviroment ##########################################################################################################################
#   Autor: Vinicius Henrique dos Santos
#   Empresa: FIAP
#   Objetivo: Criar o ambiente de tabelas para Streaming e para Batch process usando o Apache Flink
########################################################################################################################################################

from pyflink.table import EnvironmentSettings, TableEnvironment, StreamTableEnvironment
from pyflink.datastream import StreamExecutionEnvironment


############################################################
# Criando batch TableEnvironment
############################################################
batch_settings = EnvironmentSettings.new_instance()\
                                    .in_batch_mode()\
                                    .use_blink_planner()\
                                    .build()
batch_tbl_env = TableEnvironment.create(batch_settings)


############################################################
# Criando stream TableEnvironment
############################################################
stream_settings = EnvironmentSettings.new_instance()\
                                      .in_streaming_mode()\
                                      .use_blink_planner()\
                                      .build()
stream_tbl_env = TableEnvironment.create(stream_settings)

### Nota do professor #################################################################################################################
#   Nao estamos trabalhando com a DataStream API aqui, mas caso estivesse voce poderia reaproveitar um ambiente que ja esta criado, 
#   em uso nessa API de menor nivel em seu novo processo.
#######################################################################################################################################

ds_env = StreamExecutionEnvironment.get_execution_environment()
tbl_evn = StreamTableEnvironment.create(ds_env)
