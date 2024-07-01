
tables_and_columns = {
    'table1': ['col1', 'col2', 'col3'],
    'table2': ['col1', 'col2']
}

for table, columns in tables_and_columns.items():
    query = f"SELECT {', '.join(columns)} FROM {table}"
    df = pd.read_sql(query, src_engine)
    df.to_sql(table, tgt_engine, if_exists='replace')
