import psycopg2
import sys

#creating a connection with the database
def get_connections():
    try:
        return psycopg2.connect(
            database="photon",
            user="student",
        )
    except Exception as e:
        print(f"Error: {e}")  
        return None 

# Inserting function
def insert_player(id, codename):
    conn = get_connections()
    # checking if the connection worked
    if conn:
        cursor = conn.cursor()
       # inserting player into the database
        cursor.execute("INSERT into players(id,codename) VALUES (%s,%s)", (id, codename))
        conn.commit()
        conn.close()
        print("Player inserted successfully!")
    else:
        print("Connection failed")
        sys.exit()

# testing inserting 
insert_player(1, "PlayerOne")
insert_player(2, "PlayerTwo")
