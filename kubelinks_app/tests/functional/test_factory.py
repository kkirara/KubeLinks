def test_home_page_with_fixture(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/home' page is requested (GET)
    THEN check that the response is valid
    """
    response = client.get('/home')
    assert response.status_code == 200
    assert b"Url" in response.data
    assert b"Name" in response.data
    assert b"Type" in response.data
