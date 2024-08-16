from sqlite3 import Connection

class TripsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def create_trip(self, trip_infos: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO trips
                    (id, destination, start_date, end_date, owner_name, owner_email)
                VALUES
                    (?, ?, ?, ?, ?, ?)
            ''', (
                trip_infos["id"],
                trip_infos["destination"],
                trip_infos["start_date"],
                trip_infos["end_date"],
                trip_infos["owner_name"],
                trip_infos["owner_email"]
            )
        )
        self.__conn.commit()