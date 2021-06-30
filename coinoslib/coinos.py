from .helpers import fetch

def create(username: str='', password: str='') -> dict:
    return fetch(
        'POST', '/register', json={'user': {'username': username, 'password': password}}).json()

def login(username: str='', password: str='', token=None) -> dict:
    if len(username) == 0 and len(password) == 0:
        return fetch('GET', '/login').json()
        
    return fetch(
        'POST', '/taboggan', json={'username': username, 'password': password, 'token': token}).json()

def logout() -> bool:
    return fetch(
        'POST', '/logout', json={'subscription': None}).status_code == 200
