#model 3 lives here.
from config import CONN, CURSOR

class Locations:
    #create location    
    @classmethod    
    def create_location(cls, location_name):
        sql = "INSERT INTO locations (location_name) VALUES (?)"
        CURSOR.execute(sql, (location_name,))
        CONN.commit()
    
    #show all locations
    @classmethod
    def show_all_locations(cls):
        sql = "SELECT * FROM locations"
        CURSOR.execute(sql)
        locations = CURSOR.fetchall()
        return locations