from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    activity_name = "Chess Club"
    email = "remove-me@example.com"

    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert response.status_code == 200
    assert email in activities[activity_name]["participants"]

    delete_response = client.delete(f"/activities/{activity_name}/participants/{email}")
    assert delete_response.status_code == 200
    assert email not in activities[activity_name]["participants"]

    second_delete_response = client.delete(f"/activities/{activity_name}/participants/{email}")
    assert second_delete_response.status_code == 404
