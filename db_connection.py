import psycopg2

def get_connection():
    """
    Establish a connection to the PostgreSQL database.
    Update the credentials based on your PostgreSQL setup.
    """
    try:
        conn = psycopg2.connect(
            dbname="cs623_project",         # database name
            user="postgres",           # PostgreSQL username
            password="Mamma@17",  # PostgreSQL password
            host="localhost",          # Host name
            port="5432"                # Port (default PostgreSQL port is 5432)
        )
        return conn
    except Exception as e:
        print("Error connecting to the database:", e) 
        return None