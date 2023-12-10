from database.db_connector import DbConnector

db = DbConnector("test.db")

def insert_rating(user_id, rate):
    db.cursor.execute("INSERT INTO rates (user_id, rate) VALUES (?, ?)",
                        (user_id, rate))
    db.conn.commit()

def update_rating(rate, user_id):
    db.cursor.execute("UPDATE rates SET rate=? WHERE user_id=?", (rate, user_id))
    db.conn.commit()
    
def get_rating(user_id):
    db.cursor.execute("SELECT * FROM rates WHERE user_id=?", (user_id,))
    result = db.cursor.fetchone()
    return result
