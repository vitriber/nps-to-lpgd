import os
import sys
import psycopg2

class DataBase:
    def get_connection():
        host = os.environ.get('DATABASE')
        database = os.environ.get('DATABASE_NAME')
        user = os.environ.get('DATABASE_USER')
        password = os.environ.get('DATABASE_PASSWORD')   
        return psycopg2.connect(host=host, database=database, user=user, password=password)   

    def select(query, args=(), one=False):
        try:    
            conn = DataBase.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, args)
            r = [dict((cursor.description[i][0], value) \
                    for i, value in enumerate(row)) for row in cursor.fetchall()]
            cursor.connection.close()
            return (r[0] if r else None) if one else r
        except Exception as ex:
            print("DataBase Error: Query select error - {}".format(ex), True)

    def insert(query):
        try:
            conn = DataBase.get_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            cursor.lastrowid = cursor.fetchone()[0] 
            id = cursor.lastrowid
            conn.commit() 
            cursor.close()                      
            return id         
        except Exception as ex:
            print("DataBase Error: Query insert error - {}".format(ex), True)
        finally:
            if conn is not None:
                conn.close()  

    def update(query):
        try:
            conn = DataBase.get_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()                        
            cursor.close()            
        except Exception as ex:
            print("DataBase Error: Query update error - {}".format(ex), True)
        finally:
            if conn is not None:
                conn.close()      