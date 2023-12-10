import sqlite3

class DbConnector:
    def __init__(self, database_path=':memory:'):
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT,
                full_name TEXT,
                phone_number TEXT,
                role TEXT
            )
        ''')
        self.conn.commit()
    
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
                passenger_id TEXT,
                driver_id TEXT,
                current TEXT,
                destination TEXT
            )
        ''')
        self.conn.commit()
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS rates (
                rating_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                rate TEXT
            )
        ''')
        self.conn.commit()
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ride_history (
                booking_id TEXT,
                passenger_id TEXT,
                driver_id TEXT,
                current TEXT,
                destination TEXT
            )
        ''')
        self.conn.commit()


        
