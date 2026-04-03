def test_create_meeting_success(client, valid_meeting_data):
    response = client.post("/meetings", json=valid_meeting_data)
    assert response.status_code == 201
    assert response.json()["title"] == valid_meeting_data["title"]
    assert "id" in response.json()

def test_create_meeting_error_title_too_short(client, valid_meeting_data):
    invalid_data = valid_meeting_data.copy()
    invalid_data["title"] = "Ab"
    response = client.post("/meetings", json=invalid_data)
    assert response.status_code == 422

def test_create_meeting_error_empty_participants(client, valid_meeting_data):
    invalid_data = valid_meeting_data.copy()
    invalid_data["participants"] = []
    response = client.post("/meetings", json=invalid_data)
    assert response.status_code == 422