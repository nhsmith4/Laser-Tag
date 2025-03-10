import psycopg2
import sys

# Creating a connection to the database
def get_connections():
    try:
        return psycopg2.connect(
            database="photon",
            user="student",
        )
    except Exception as e:
        print(f"Error: {e}")  
        return None

# Checking if the player ID exists in the database
def player_exists(id) -> bool:
    conn = get_connections()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM players WHERE id = %s", (id,))
        count = cursor.fetchone()[0]
        conn.close()
        return count > 0
    return False

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
        print("Player inserted successfully!")
    else:
        print("Connection failed")
        sys.exit()

if __name__ == "__main__":
    insert_player(1,"player1")
    insert_player(1,"player2")
    'insert_player(2,"player3")
