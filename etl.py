import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries

# When moving large amounts of data from S3 staging area to Redshift, it is better to use the copy command instead of insert. The benefit of using the copy command is that the ingestion can be parallelized if the data is broken into parts. Each part can be independently ingested by a slice in the cluster. 

def load_staging_tables(cur, conn):
    """
    load data from S3 to staging tables on Redshift
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()

def insert_tables(cur, conn):
    """
    load data from staging tables to analytics tables on Redshift
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    """
    connect to cluster with the variables in dwh.cfg file
    load staging and analytic tables
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()