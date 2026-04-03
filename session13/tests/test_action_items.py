def test_create_action_item_success(client, valid_action_item_data):
    meeting_id = "mtg-1"
    url = f"/meetings/{meeting_id}/action-items"
    response = client.post(url, json=valid_action_item_data)
    
    assert response.status_code == 200
    assert response.json()["description"] == valid_action_item_data["description"]
    assert response.json()["id"] == "1" 