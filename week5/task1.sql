import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import fastavro
from sqlalchemy import create_engine


engine = create_engine('your_database_connection_string')
query = "SELECT * FROM your_table"


df = pd.read_sql(query, engine)


df.to_csv('data.csv', index=False)


table = pa.Table.from_pandas(df)
pq.write_table(table, 'data.parquet')


records = df.to_dict(orient='records')
schema = {
    "type": "record",
    "name": "Record",
    "fields": [{"name": col, "type": "string"} for col in df.columns]
}
with open('data.avro', 'wb') as out:
    fastavro.writer(out, schema, records)
