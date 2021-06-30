from requests import Session

session = Session()

def fetch(method: str='POST', path: str='/', json=None) -> object:
    fetch = session.post if (method == 'POST') \
                else session.get
    fetch = fetch(
        'https://coinos.io/api' + str(path), json=json)
    
    if (fetch.status_code == 200):
        return fetch
    else:
        raise Exception('Request failed.')

def address(network: str='bitcoin') -> dict:
    return fetch('GET', f'/address?network={network}&type=bech32').json()

def addres_is_internal(address: str) -> bool:
    return fetch('GET', f'/isInternal?address={address}').json()

def what_is_fee(
        network: str, address: str, value: int, 
        feerate: int, asset: str) -> dict:
    feerate = feerate * 100
    return fetch(
        'POST', f'/{network}/fee', json={
                'address': address, 'amount': value, 'asset': asset,
                'feeRate': feerate, 'replaceable': True}).json()

def decode_invoice(invoice: str) -> dict:
    return fetch(
            'POST', '/invoice', json={'invoice': {'text': invoice}}).json()
