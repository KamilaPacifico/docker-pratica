import os
import requests

BASE_URL = os.getenv("BASE_URL", "http://localhost:5000")


def test_home():
    r = requests.get(f"{BASE_URL}/", timeout=5)
    assert r.status_code == 200
    assert r.json()["mensagem"] == "Olá, Docker!"


def test_health():
    r = requests.get(f"{BASE_URL}/health", timeout=5)
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_soma():
    r = requests.get(f"{BASE_URL}/soma/2/3", timeout=5)
    assert r.status_code == 200
    assert r.json()["resultado"] == 5