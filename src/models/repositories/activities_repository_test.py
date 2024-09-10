import pytest
import uuid
from datetime import datetime
from src.models.settings.db_connection_handler import db_connection_handler
from .activities_repository import ActivitiesRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="Interacao com o banco")
def test_register_activity():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activity_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "title": "Go for a walk",
        "occurs_at": datetime.strptime("19-08-2024", "%d-%m-%Y")
    }

    activities_repository.register_activity(activity_infos)

@pytest.mark.skip(reason="Interacao com o banco")
def test_find_activities_from_trip():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activites = activities_repository.find_activities_from_trip(trip_id)
    print()
    print(activites)