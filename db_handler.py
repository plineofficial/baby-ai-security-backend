import os
import psycopg2
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    try:
        db_conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            dbname=os.getenv('DB_NAME'), 
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        
        cursor = db_conn.cursor()
        cursor.execute(open("BAIS schema.sql", "r").read())     
        db_conn.commit()
    except Exception as ex:
        print(repr(ex))
    finally:
        cursor.close()
        db_conn.close()
        

if __name__ == "__main__":
    main()