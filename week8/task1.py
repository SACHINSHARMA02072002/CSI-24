from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("NYC Taxi Data Analysis").getOrCreate()







data_path = "path/to/your/nyc_taxi_data/*.csv"  

taxi_data_schema = "vendor_id INT, pickup_datetime TIMESTAMP, dropoff_datetime TIMESTAMP, passenger_count INT, trip_distance DOUBLE, Fare_amount DOUBLE, Extra DOUBLE, MTA_tax DOUBLE, Improvement_surcharge DOUBLE, Tip_amount DOUBLE, Tolls_amount DOUBLE, Total_amount DOUBLE"


taxi_df = spark.read.csv(data_path, schema=taxi_data_schema) 




taxi_df = taxi_df.withColumn(
    "Revenue",
    taxi_df["Fare_amount"]
    + taxi_df["Extra"]
    + taxi_df["MTA_tax"]
    + taxi_df["Improvement_surcharge"]
    + taxi_df["Tip_amount"]
    + taxi_df["Tolls_amount"]
    + taxi_df["Total_amount"]
)



area_passenger_count = taxi_df.groupBy("pickup_zone").agg(sum("passenger_count").alias("total_passengers"))
area_passenger_count.show() 







avg_fare_earnings_window = taxi_df.withWatermark("pickup_datetime", "60 seconds") \
                                 .groupBy(window("pickup_datetime", "60 seconds"), "vendor_id") \
                                 .agg(avg("Fare_amount").alias("avg_fare"), sum("Revenue").alias("total_earnings"))
avg_fare_earnings_window.show() 






window_spec = Window.orderBy("pickup_datetime").rowsBetween(-10, 0) 

payment_mode_counts = taxi_df.withWatermark("pickup_datetime", "1 second") \
                             .groupBy("payment_type", window_spec) \
                             .count()
payment_mode_counts.show() 





date_to_analyze = "2024-07-23" 

filtered_df = taxi_df.filter(F.col("pickup_datetime").cast("date").eq(date_to_analyze))


top_gaining_vendors = filtered_df.groupBy("vendor_id") \
                                  .agg(sum("passenger_count").alias("total






