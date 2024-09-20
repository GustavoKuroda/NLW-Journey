from typing import Dict

class ActivityFinder:
    def __init__(self, activities_repository) -> None:
        self.__activities_repository = activities_repository

    def find_from_trip(self, trip_id: str) -> Dict:
        try:
            activities = self.__activities_repository.find_activities_from_trip(trip_id)

            formatted_activities = []
            for activity in activities:
                formatted_activities.append({
                    "id": activity[0],
                    "title": activity[1],
                    "occurs_at": activity[2]
                })

            return {
                "body": {"id": trip_id},
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "massage": str(exception)},
                "status_code": 400
            }