def test_home_page_with_fixture(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b"Kubernetes urls" in response.data
    assert b"Url" in response.data
    assert b"Name" in response.data
    assert b"Type" in response.data
