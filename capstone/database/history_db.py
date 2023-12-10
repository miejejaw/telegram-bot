from database.db_connector import DbConnector

db = DbConnector("test.db")

def insert_to_history(ride):
    db.cursor.execute("INSERT INTO ride_history (booking_id, passenger_id, driver_id, current, destination) VALUES (?, ?, ?, ?)",
                        (ride[0], ride[1], ride[2], ride[3], ride[4]))
    db.conn.commit()

def get_history_by_passenger_id(passenger_id):
    db.cursor.execute("SELECT * FROM ride_history WHERE passenger_id=?", (passenger_id,))
    result = db.cursor.fetchone()
    return result