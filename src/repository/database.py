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

    def insert(query, query_return=()):
        try:
            conn = DataBase.get_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            if(query_return): 
                cursor.execute(query_return)
                my_result = cursor.fetchall()
                cursor.close()
                return my_result
            cursor.close()     
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