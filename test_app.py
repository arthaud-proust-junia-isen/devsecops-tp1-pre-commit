import pytest

from app import calculate, get_password


def test_addition():
    assert calculate(2, 3, "add") == 5


def test_subtraction():
    assert calculate(5, 2, "subtract") == 3


def test_multiplication():
    assert calculate(4, 2, "multiply") == 8


def test_division():
    assert calculate(9, 3, "divide") == 3


def test_division_by_zero():
    with pytest.raises(ValueError):
        calculate(10, 0, "divide")


def test_unknown_operation():
    with pytest.raises(ValueError):
        calculate(1, 2, "power")


def test_password_missing(monkeypatch):
    monkeypatch.delenv("APP_PASSWORD", raising=False)
    with pytest.raises(RuntimeError):
        get_password()


def test_password_from_env(monkeypatch):
    monkeypatch.setenv("APP_PASSWORD", "valeur-de-test")  # pragma: allowlist secret
    assert get_password() == "valeur-de-test"  # pragma: allowlist secret
