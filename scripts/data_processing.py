from pyspark.sql import SparkSession
from pyspark.sql.functions import col, month, year

spark = SparkSession.builder \
    .appName("E-commerce Data Processing") \
    .config("spark.sql.warehouse.dir", "/tmp") \
    .config("spark.hadoop.fs.defaultFS", "file:///") \
    .config("spark.hadoop.fs.file.impl.disable.cache", "true") \
    .getOrCreate()

# Iniciar sessão Spark
spark = SparkSession.builder     .appName("E-commerce Data Processing")     .getOrCreate()

# Carregar dados
customers = spark.read.csv('../data/customers.csv', header=True, inferSchema=True)
products = spark.read.csv('../data/products.csv', header=True, inferSchema=True)
sales = spark.read.csv('../data/sales.csv', header=True, inferSchema=True)

# Processar dados
sales = sales.withColumn("sale_month", month(col("date")))
sales = sales.withColumn("sale_year", year(col("date")))

# Salvar os dados processados
sales.write.csv('../data/processed_sales.csv', header=True, mode='overwrite')
