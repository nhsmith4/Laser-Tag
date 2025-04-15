import psycopg2
import sys
import globe.debug as debug
from globe.debug import printDebug

# Creating a connection to the database
def get_connections():
    try:
        return psycopg2.connect(
            database="photon",
            user="student",
        )
    except Exception as e:
        printDebug(f"Error: {e}")  
        return None

# Checking if the player ID exists in the database
def player_exists(entry_id):
    try:
        int(entry_id)
    except:
        return None
    conn = get_connections()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM players WHERE id = %s;" % entry_id)
        result = cursor.fetchone()
        printDebug(result, debug.ADVANCED)
        conn.close()
        if result:
            return result[1]
        else:
            return None
    return None
 


# Inserting a player into the database
def insert_player(id, codename):
    # Check if the player ID already exists
    if player_exists(id):
        print(f"Player with ID {id} already exists.")
        return

    conn = get_connections()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO players (id, codename) VALUES (%s, %s)", (id, codename))
        conn.commit()
        conn.close()
        printDebug("Player inserted successfully!")
    else:
        print("Connection failed database!")
        sys.exit()

if __name__ == "__main__":
    insert_player(1,"player1")
    insert_player(1,"player2")
    insert_player(2,"player3")
    print(player_exists(1))
    print(player_exists(2))
