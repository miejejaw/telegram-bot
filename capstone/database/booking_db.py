from database.db_connector import DbConnector

db = DbConnector("test.db")

def insert_booking(user_id, current, destination):
    db.cursor.execute("INSERT INTO books (passenger_id, driver_id, current, destination) VALUES (?, ?, ?, ?)",
                        (user_id, "none", current, destination))
    db.conn.commit()
    return db.cursor.lastrowid

def update_driver_col(booking_id, driver_id):
    db.cursor.execute("UPDATE books SET driver_id=? WHERE booking_id=?", (driver_id, booking_id))
    db.conn.commit()

def delete_booking(booking_id):
    db.cursor.execute("DELETE FROM books WHERE booking_id=?", (booking_id,))
    db.conn.commit()
    
def get_booking(booking_id):
    db.cursor.execute("SELECT * FROM books WHERE booking_id=?", (booking_id,))
    result = db.cursor.fetchone()
    return result

def get_booking_by_passenger_id(passenger_id):
    db.cursor.execute("SELECT * FROM books WHERE passenger_id=?", (passenger_id,))
    result = db.cursor.fetchone()
    return result