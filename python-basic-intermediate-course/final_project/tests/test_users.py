USER = {
    "first_name": "Ada", "last_name": "Lovelace",
    "email": "ada@example.com", "department": "Engineering",
    "role": "Developer", "active": True, "employee_id": "E-001",
    "phone": None, "comments": "First programmer",
}


def test_api_user_crud(client):
    created = client.post("/api/users", json=USER)
    assert created.status_code == 201
    user_id = created.json()["id"]

    listed = client.get("/api/users", params={"q": "Engineering"})
    assert listed.status_code == 200
    assert [user["id"] for user in listed.json()] == [user_id]

    changed = {**USER, "role": "Lead", "active": False}
    updated = client.put(f"/api/users/{user_id}", json=changed)
    assert updated.status_code == 200
    assert updated.json()["role"] == "Lead"
    assert updated.json()["active"] is False

    deleted = client.delete(f"/api/users/{user_id}")
    assert deleted.status_code == 204
    assert client.get(f"/api/users/{user_id}").status_code == 404


def test_validation_duplicates_and_html(client):
    assert client.post("/api/users", json={**USER, "email": "bad"}).status_code == 422
    assert client.post("/api/users", json=USER).status_code == 201
    assert client.post("/api/users", json={**USER, "employee_id": "E-002"}).status_code == 409
    dashboard = client.get("/")
    assert dashboard.status_code == 200
    assert "Total users" in dashboard.text
    assert "Ada Lovelace" in client.get("/users").text


def test_html_create_edit_delete(client):
    form = {key: str(value) for key, value in USER.items() if value is not None}
    response = client.post("/users", data=form, follow_redirects=False)
    assert response.status_code == 303
    location = response.headers["location"]
    assert "created=1" in location
    user_id = location.split("/")[2].split("?")[0]
    edit = {**form, "department": "Research", "active": "true"}
    assert client.post(f"/users/{user_id}/edit", data=edit,
                       follow_redirects=False).status_code == 303
    assert "Research" in client.get(f"/users/{user_id}").text
    assert client.post(f"/users/{user_id}/delete",
                       follow_redirects=False).status_code == 303

