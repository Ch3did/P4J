import pytest


@pytest.fixture
def template():
    return {
        "a": ":3",
        "b": "3:8",
        "c": {
            "x": "8:10",
            "y": "10:12",
            "z": {"w": "12:23", "u": "23:25", "v": "25:"},
        },
    }


@pytest.fixture
def positional_string():
    return "abcdefghijklmnopqrstuvxywz1234567890"
