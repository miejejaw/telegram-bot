from database.db_connector import DbConnector

db = DbConnector("test.db")

def insert_user(user_id, full_name, phone_number, role):
    db.cursor.execute("INSERT INTO users (user_id, full_name, phone_number, role) VALUES (?, ?, ?, ?)",
                            (user_id, full_name, phone_number, role))
    db.conn.commit()

def get_user_by_id(user_id):
    db.cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    return db.cursor.fetchone()

def update_user(user_id, col, value):
    db.cursor.execute(f"UPDATE users SET {col}=? WHERE user_id=?", (value, user_id))
    db.conn.commit()
    
def get_all_drivers_id():
    db.cursor.execute("SELECT user_id FROM users WHERE role=?", ('driver',))
    drivers = db.cursor.fetchall()
    return [driver[0] for driver in drivers]