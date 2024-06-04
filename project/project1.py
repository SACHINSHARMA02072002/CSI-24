import glob
import random
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

# Create SparkSession
spark = SparkSession.builder.appName("MNISTReader").getOrCreate()


# !wget {download_url} -P flat_files/mnist_png/


def read_images(folder_path):
  images = glob.glob(f"{folder_path}/*.png", recursive=True)
  random.shuffle(images)
  return images[:5]  

image_paths = []
for folder in glob.glob("flat_files/mnist_png/*"):
  image_paths += read_images(folder)


label_col = lit(folder.split("/")[-1])  
df = spark.createDataFrame(image_paths, ["image_path"])
if label_col is not None:
  df = df.withColumn("label", label_col)  


df = df.withColumn("image_bytes", col("image_path").binary())


schema = "image_path string, image_bytes binary"  


df.write \
  .format("delta") \
  .option("compression", "none") \
  .mode("overwrite") \
  .save("flat_files/mnist_delta")


spark.stop()

print("MNIST images saved to Delta table (flat_files/mnist_delta)")
