from fastapi.testclient import TestClient

from app.main import app
from app.utils import quadratic_equation


def test_quadratic_equation() -> None:
    assert quadratic_equation(1, -3, 2) == (2.0, 1.0)
    assert quadratic_equation(2, -7, 3) == (3.0, 0.5)
    assert quadratic_equation(1, 2, -3) == (1.0, -3.0)

    assert quadratic_equation(1, -4, 4) == 2.0
    assert quadratic_equation(2, -8, 8) == 2.0

    assert quadratic_equation(1, 2, 3) is None
    assert quadratic_equation(2, 3, 4) is None


client = TestClient(app)


def test_get_quadratic_equation():
    response = client.get("/get_quadratic_equation?a=1&b=-3&c=2")
    assert response.status_code == 200
    assert response.json() == {"solution": [2.0, 1.0]}

    response = client.get("/get_quadratic_equation?a=1&b=2&c=1")
    assert response.status_code == 200
    assert response.json() == {"solution": -1.0}

    response = client.get("/get_quadratic_equation?a=1&b=2&c=3")
    assert response.status_code == 200
    assert response.json() == {"solution": None}

    response = client.get("/get_quadratic_equation?a=0&b=2&c=3")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["query", "a"],
                "msg": "ensure this value is greater than 0",
                "type": "value_error",
            }
        ]
    }

    response = client.get("/get_quadratic_equation?a=1&b=2")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [{"loc": ["query", "c"], "msg": "field required", "type": "value_error.missing"}]
    }

    response = client.get("/get_quadratic_equation?a=1&b=2&c=foo")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {"loc": ["query", "c"], "msg": "value is not a valid float", "type": "type_error.float"}
        ]
    }


def test_guess_color_blue():
    response = client.get("/guess_color/50")
    assert response.status_code == 200
    assert response.json() == {"color": "blue"}


def test_guess_color_green():
    response = client.get("/guess_color/80")
    assert response.status_code == 200
    assert response.json() == {"color": "green"}


def test_guess_color_red():
    response = client.get("/guess_color/100")
    assert response.status_code == 200
    assert response.json() == {"color": "red"}


def test_guess_color_invalid_input():
    response = client.get("/guess_color/0")
    assert response.status_code == 400


def test_guess_color_missing_input():
    response = client.get("/guess_color/")
    assert response.status_code == 404


def test_guess_color_invalid_path():
    response = client.get("/guess_color/string")
    assert response.status_code == 422


def test_guess_color_item_number_too_large():
    response = client.get("/guess_color/101")
    assert response.status_code == 400


def test_guess_color_item_number_too_small():
    response = client.get("/guess_color/-1")
    assert response.status_code == 400
