import sqlite3
CONN = sqlite3.connect('league.db')
CURSOR = CONN.cursor()

class Database:
    @classmethod
    def create_tables(cls):
        sql_teams="""
        CREATE TABLE IF NOT EXISTS teams(
        team_id INTEGER PRIMARY KEY,
        team_name varchar(40)
        )
        """
        CURSOR.execute(sql_teams)
        CONN.commit()

        sql_games="""
        CREATE TABLE IF NOT EXISTS games(
        game_id INTEGER PRIMARY KEY,
        team_id INTEGER,
        FOREIGN KEY(team_id) REFERENCES teams(team_id)
        )
        """
        CURSOR.execute(sql_games)
        

        sql_stadiums="""
        CREATE TABLE IF NOT EXISTS stadiums(
        stadium_id INTEGER PRIMARY KEY,
        stadium_name varchar(40)
        )
        """
        CURSOR.execute(sql_stadiums)
        

        sql_locations="""
        CREATE TABLE IF NOT EXISTS locations(
        location_id INTEGER PRIMARY KEY,
        stadium_id INTEGER,
        FOREIGN KEY(stadium_id) REFERENCES stadiums(stadium_id)
        )
        """
        CURSOR.execute(sql_locations)
        
        CONN.commit()

    @classmethod
    def drop_tables(cls):
        sql_teams="""
        DROP TABLE IF EXISTS teams
        """
        CURSOR.execute(sql_teams)
        
        sql_games="""
        DROP TABLE IF EXISTS games
        """
        CURSOR.execute(sql_games)
        
        sql_stadiums="""
        DROP TABLE IF EXISTS stadiums
        """
        CURSOR.execute(sql_stadiums)
        
        sql_locations="""
        DROP TABLE IF EXISTS locations
        """
        CURSOR.execute(sql_locations)
        
        CONN.commit()
