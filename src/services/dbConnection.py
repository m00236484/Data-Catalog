#!/usr/bin/python
import psycopg2
import os
from config import config


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print dir_path
    cwd = os.getcwd()
    print cwd
    try:
        # read connection parameters
        #params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        #conn = psycopg2.connect(**params)
        conn = psycopg2.connect(dbname="datacatalog", user="postgres", password="postgres", host = "ec2-34-211-128-184.us-west-2.compute.amazonaws.com" , port="5432")
        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
        print "Connected"
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    cwd = os.getcwd()
    print os.path.abspath(os.path.join(cwd, os.pardir))
    connect()