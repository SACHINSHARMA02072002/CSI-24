
data_path = "dbfs:/path/to/your/data.json"

data_df = spark.read.json(data_path)

data_df.show(5)  











def flatten_json(df, prefix="", parent_key=None):
  if df.schema.dataType == ArrayType:
    
    exploded_df = df.withColumn("exploded", F.explode(df[df.schema.names[0]]))
    return flatten_json(exploded_df, prefix=prefix)
  elif df.schema.dataType == StructType:
    
    flattened_fields = [flatten_json(df.select(col.alias(prefix + col.name)) if parent_key is None else df.select(col.alias(parent_key + "_" + col.name)), prefix=prefix + col.name + "_", parent_key=prefix) for col in df.schema.fields]
    return flattened_fields
  else:
    
    return df.select(df.col.alias(prefix + parent_key if parent_key else df.col.name))


flattened_df = data_df.select(*flatten_json(data_df))














output_path = "dbfs:/path/to/your/flattened_data"

flattened_df.write.parquet(output_path, mode="overwrite")

print(f"Flattened data written to Parquet table: {output_path}")
