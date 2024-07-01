import sqlalchemy


src_engine = sqlalchemy.create_engine('source_db_connection_string')
tgt_engine = sqlalchemy.create_engine('target_db_connection_string')


src_tables = src_engine.table_names()

for table in src_tables:
    df = pd.read_sql_table(table, src_engine)
    df.to_sql(table, tgt_engine, if_exists='replace')
