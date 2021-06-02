![Screenshot](/images/spark-logo-trademark.png)

- [1. Descrição](#link1)
- [2. Instalação](#link2)
- [3. Exemplos](#link3)
- [4. Links](#link4)

<a id="link1"></a>
## 1. Descrição

O Apache Spark é um framework para processamento com grandes quantidades de dados de forma distribuída.</br> 
Apache Spark é um framework de código fonte aberto para computação distribuída. Foi desenvolvido no AMPLab da Universidade da Califórnia e posteriormente repassado para a Apache Software Foundation que o mantém desde então.

Por utilizar a memória RAM é mais rápido que o MapReduce que necessita realziar as operações em disco.

Permite a utilização em diversos tipos de tarefas como queries SQL, Machine Learning, graphs e etc.

Apache Spark suporta múltiplas linguagens como Java, Scala, R, or Python.

#Componentes</br>
![Screenshot](/images/arqui.jpg)

#RDD - Resilient Distributed Datasets</br>

Resilient Distributed Datasets (RDD) é a estrutura fundamental de dados do Spark. É uma coleção de dados apaenas de leitura, não podendo ser alterado. Cada dataset no RDD é dividido em partições lógicas, que podem ser manipuladas em diferentes nodes do cluster. RDDs podem ser formados de objetos presentes no Python, Java, ou Scala, incluindo classes definidas pelo usuário.

RDDs podem ser criados de duas formas:</br>
Paralelizando uma coleção.</br>
Referência a um dataset presente em um sisetma de arquivos, HDFS, HBase.</br>

When to use RDDs?
Consider these scenarios or common use cases for using RDDs when:

you want low-level transformation and actions and control on your dataset;
your data is unstructured, such as media streams or streams of text;
you want to manipulate your data with functional programming constructs than domain specific expressions;
you don’t care about imposing a schema, such as columnar format, while processing or accessing data attributes by name or column; and
you can forgo some optimization and performance benefits available with DataFrames and Datasets for structured and semi-structured data.



#Data Frame</br>
No Spark, um DataFrame é uma coleção distribuída de dados organizados em colunas, sendo conceituamente equivalentes a uma tabela em um banco relacional ou um data frame em R ou Python.

#Dataset</br>
Dataset é uma estrutura de dados que é tipada e é mapeada a um schema relacional. É uma extensão da API do data frame.

When should I use DataFrames or Datasets?
If you want rich semantics, high-level abstractions, and domain specific APIs, use DataFrame or Dataset.
If your processing demands high-level expressions, filters, maps, aggregation, averages, sum, SQL queries, columnar access and use of lambda functions on semi-structured data, use DataFrame or Dataset.
If you want higher degree of type-safety at compile time, want typed JVM objects, take advantage of Catalyst optimization, and benefit from Tungsten’s efficient code generation, use Dataset.
If you want unification and simplification of APIs across Spark Libraries, use DataFrame or Dataset.
If you are a R user, use DataFrames.
If you are a Python user, use DataFrames and resort back to RDDs if you need more control.
Note that you can always seamlessly interoperate or convert from DataFrame and/or Dataset to an RDD, by simple method call .rdd. For instance,

<a id="link2"></a>
## 2. Instalação

#scala</br>
```sudo apt install scala```</br>
![Screenshot](/images/s01.jpg)

```scala -version```</br>
![Screenshot](/images/s02.jpg)

#java</br>
![Screenshot](/images/s03.jpg)

#python</br>
![Screenshot](/images/s04.jpg)

#download spark</br>
```https://archive.apache.org/dist/spark/spark-3.0.1/spark-3.0.1-bin-hadoop2.7.tgz```</br>
![Screenshot](/images/s05.jpg)

#extract
```tar xvzf spark-3.0.1-bin-hadoop2.7.tgz```</br>
![Screenshot](/images/s06.jpg)

#mover para a pasta destino e permissões para o usuário padrão</br>
```sudo mv spark-3.0.1-bin-hadoop2.7 /usr/local/spark```</br>
```sudo chown -R hduser /usr/local/spark```</br>

![Screenshot](/images/s07.jpg)

## Configuração

#editar bashrc</br>
```nano ~/.bashrc```</br>

```#hadoop```</br>
```export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/hadoop/lib/native```</br>
```export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop```</br>
```export YARN_CONF_DIR=$HADOOP_HOME/etc/hadoop```</br>

```#spark```</br>
```export SPARK_HOME=/usr/local/spark```</br>
```export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin```</br>
```export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9-src.zip:$PYTHONPATH```</br>
```export PYSPARK_PYTHON=python3```</br>

```source ~/.bashrc```</br>
![Screenshot](/images/s08.jpg)

#conferência</br>
```spark-shell```</br>
![Screenshot](/images/s09.jpg)

```pyspark```</br>
![Screenshot](/images/s10.jpg)

#criar pasta para logs</br>
```hdfs dfs -mkdir /spark-logs```</br>
![Screenshot](/images/s11.jpg)

#editar arquivo host, acrescentando os IPs do master e dos workers</br>
```sudo nano /etc/hosts```</br>
![Screenshot](/images/s12.jpg)

#editar spark-env.sh</br>
```cd /usr/local/spark/conf```</br>
```cp spark-env.sh.template spark-env.sh```</br>
```nano spark-env.sh```</br>
```export SPARK_MASTER_HOST='192.168.1.31'```</br>
```export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-arm64```</br>
```export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop```</br>
![Screenshot](/images/s13.jpg)

#editar /usr/local/spark/conf/slaves, acrescentar o master e workers</br>
```nano slaves```</br>
![Screenshot](/images/s14.jpg)

#editar spark-defaults.conf</br>
```nano $SPARK_HOME/conf/spark-defaults.conf```</br>
```spark.master           yarn```</br>
```spark.driver.memory    2g```</br>
```spark.yarn.am.memory   2g```</br>
```spark.executor.memory  2g```</br>
```spark.eventLog.enabled  true```</br>
```spark.eventLog.dir hdfs://master:9000/spark-logs```</br>
```spark.history.provider            org.apache.spark.deploy.history.FsHistoryProvider```</br>
```spark.history.fs.logDirectory     hdfs://master:9000/spark-logs```</br>
```spark.history.fs.update.interval  10s```</br>
```spark.history.ui.port             18080```</br>
![Screenshot](/images/s15.jpg)

Realizar a mesma configração nos workers

#start no cluster</br>

#master</br>
```cd $SPARK_HOME/sbin```</br>
```./start-master.sh```</br>
![Screenshot](/images/s16.jpg)

#workers</br>
```cd $SPARK_HOME/sbin```</br>
```./start-slave.sh spark://master:7077```</br>
![Screenshot](/images/s17.jpg)</br>
![Screenshot](/images/s18.jpg)</br>

#abrir interface web</br>
```http://192.168.1.31:8080/```</br>
![Screenshot](/images/s19.jpg)</br>
![Screenshot](/images/s20.jpg)</br>


## 3. Exemplos

#spark-shell</br>
É um shell interativo para executar consultas ad-hoc. Este é um aplicativo Spark escrito em Scala para oferecer um ambiente de linha de comando e se familiarizar com os recursos do Spark.

Nesse exemplo será feita a leitura de um arquivo no HDFS e a contagem de palavras.

Ao chamar o spark-shell automaticamento são instanciadas:</br>
spark = SparkSession</br>
sc = SparkContext</br>

#arquivo entrada
![Screenshot](/images/s21.jpg)</br>

#spark-shell
![Screenshot](/images/s22.jpg)</br>

#comandos
![Screenshot](/images/s23.jpg)</br>

#resultado
![Screenshot](/images/s24.jpg)</br>
![Screenshot](/images/s25.jpg)</br>
![Screenshot](/images/s26.jpg)</br>







#criando um Keyspace</br>

#criando uma tabela</br>

<a id="link4"></a>
## 4. Links

Apache Spark</br>
https://spark.apache.org/</br>

Download Apache Spark</br>
https://spark.apache.org/downloads.html</br>

Databricks</br>
https://databricks.com/spark/about</br>