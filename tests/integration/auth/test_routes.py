"""
Test routes for routes for authorizing users, app/auth/routes
"""
# pylint: disable=redefined-outer-name,unused-argument
from flask import session

def test_register_login_login_register_when_logged_in(test_app, client, user_dict, register_user_response):
    """
    Test registering a user, loging in as user and try go to register page.
    """
    assert register_user_response.status_code == 200
    assert b"Sign In" in register_user_response.data # Check that was redirected to /login
    assert b"Congratulations, you are now a registered user!" in register_user_response.data

    with test_app.test_request_context():
        response = client.post('/login',
            data=user_dict,
            follow_redirects=True,
        )
        assert response.status_code == 200
        assert b"Hi, doe!" in response.data # Check that was redirected to /index

    response = client.post('/login',
        data=user_dict,
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Hi, doe!" in response.data # Check that was redirected to /index

    response = client.post('/register',
        data=user_dict,
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Hi, doe!" in response.data # Check that was redirected to /index

def test_register_user_wrong_password2(client, user_dict):
    """
    Test registering a user where repeat password is different.
    """
    user_dict["password2"] = "some else"
    response = client.post('/register',
        data=user_dict,
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"<h1>Register</h1>" in response.data
    assert b"Field must be equal to password." in response.data

def test_register_user_missing_data(client):
    """
    Test registering a user when missing data in form.
    """
    response = client.post('/register',
        data={
            "username": "",
            "email": "",
            "password": "",
            "password2": "",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"<h1>Register</h1>" in response.data
    assert str(response.data).count("This field is required.") == 4

def test_login_with_wrong_username_and_password(test_app, client, register_user_response, user_dict):
    """
    Test logging in with wrong username and password
    """
    with test_app.test_request_context():
        response = client.post('/login',
            data={
                "username": "not_me",
                "password": "something"
            },
            follow_redirects=True,
        )
        assert response.status_code == 200
        assert session.get('_user_id', None) is None
        assert b"Sign In" in response.data # Check that was redirected to /login
        assert b"Invalid username or password" in response.data

    with test_app.test_request_context():
        response = client.post('/login',
            data={
                "username": user_dict["username"],
                "password": "wrong password"
            },
            follow_redirects=True,
        )
        assert response.status_code == 200
        assert session.get('_user_id', None) is None
        assert b"Sign In" in response.data # Check that was redirected to /login
        assert b"Invalid username or password" in response.data

def test_logout(client, register_user_response, user_dict):
    """
    Test that logging out user works
    """
    client.post('/login',
        data=user_dict,
        follow_redirects=True,
    )

    response = client.post('/logout',
        follow_redirects=True,
    )
    assert response.status_code == 405
