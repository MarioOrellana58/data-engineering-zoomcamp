import pandas as pd
import pyarrow.parquet as pq
from sqlalchemy import create_engine
from time import time
import argparse
import os
import pyarrow.parquet as pq



def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    
    csv_name = 'output.csv'
    parquet_name = 'output.parquet'

    # download the csv
    print('llega')
    print(url)
    os.system(f'wget {url} -O {parquet_name}')
    print('llega2')

    if not os.path.isfile(parquet_name): return

    # Read Parquet file
    parquet_file = pq.ParquetFile(parquet_name)
    table = parquet_file.read()


    # Convert to Pandas DataFrame
    df = table.to_pandas()

    # Save as CSV
    df.to_csv(csv_name, index=False)


    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    engine.connect()

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    df = next(df_iter)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    
    df.to_sql(name=table_name, con=engine, if_exists='append')

    #not good practice
    while True:
        t_start = time()

        df = next(df_iter)
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        df.to_sql(name=table_name, con=engine, if_exists='append')

        t_end = time()

        #%.3f this is a float with 3 decimal
        print('inserted another chunck..., took %.3f second' %(t_end-t_start))



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    #arguments

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='Database name for postgres')
    parser.add_argument('--table_name', help='name of the table where we will write the results to')
    parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()
    
    main(args)