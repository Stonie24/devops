# tests/test_version_route.py
"""
Test routes for checking app version, app/main/routes
"""
# pylint: disable=redefined-outer-name,unused-argument

def test_version_route(client):
    """
    Test that /version route returns the correct app version
    """
    with client:
        response = client.get("/version", follow_redirects=True)
        assert response.status_code == 200
        # The route returns JSON, so check for the version string
        assert b"12.0.3-prod" in response.data
        assert b"version" in response.data
