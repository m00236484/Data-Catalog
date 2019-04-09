#!/usr/bin/python
from psycopg2.extras import RealDictCursor
import psycopg2
import datetime
import json


#from config import config
import json

class DbManager:
    def __init__(self):
        self.conn = None

    def connect(self,db,dbuser,dbpass,dbhost,dbport):
        """ Connect to the PostgreSQL database server """
        conn = None
        result = []
        try:
            # read connection parameters
            #params = config()

            # connect to the PostgreSQL server
            #print('Connecting to the PostgreSQL database...')
            #conn = psycopg2.connect(**params)
            conn = psycopg2.connect(dbname=db, user=dbuser, password=dbpass, host =dbhost, port=dbport)
            # create a cursor
            cur = conn.cursor()

            # execute a statement
            #print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            #print(db_version)

            # close the communication with the PostgreSQL
            self.conn = conn
            return self.conn
        except (Exception, psycopg2.DatabaseError) as error:
            return conn


    def sqlExec(self, sql ):
        print ("##### SQL To Execute #####")
        print(sql)
        if self.conn is None:
            self.connect()

        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(sql)

        result = json.dumps(cur.fetchall(), indent=4,  default=str)
        self.desConnect()
        return result



    def insExec(self, sql , data ):
        #print("##### SQL To Execute #####")
        #print(sql)
        result ={}
        if self.conn is None:
            self.connect()

        try:
            cur = self.conn.cursor()
            cur.execute(sql, data)
            id  = cur.fetchone()[0]

            # commit changes
            self.conn.commit()
            #print "Commit"
            #result = json.dumps(cur.fetchone()[0], indent=2)
            #self.desConnect()
            return id
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


    def connect(self):
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            # read connection parameters
            #params = config()

            # connect to the PostgreSQL server
            #print('Connecting to the PostgreSQL database...')
            #conn = psycopg2.connect(**params)
            conn = psycopg2.connect(dbname="datacatalog", user="postgres", password="postgres", host = "ec2-34-211-128-184.us-west-2.compute.amazonaws.com" , port="5432")
            # create a cursor
            cur = conn.cursor()

            # execute a statement
            #print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            #print(db_version)

            # close the communication with the PostgreSQL
            self.conn = conn
            return self.conn
        except (Exception, psycopg2.DatabaseError) as error:
            return conn


    def desConnect(self):
        if self.conn is not None:
            self.conn.close()
            print('Database connection closed.')

