from .helpers import fetch, what_is_fee

def address() -> object:
    return fetch('GET', '/address?network=bitcoin&type=bech32').json()

def withdraw(
        address: str, value: int, feerate: int, asset: str, 
        description='') -> dict:
    tx = what_is_fee(
        'bitcoin', address, value, feerate, asset).json()['tx']
    
    return fetch(
        'POST', '/bitcoin/send', json={
            'address': address, 'asset': asset, 'memo': description, 'tx': tx}).json()
