from .helpers import fetch, decode_invoice

def invoice(value: int, description: str='') -> dict:
    return fetch(
        'POST', '/lightning/invoice', json={
            'amount': value, 'memo': description}).text

def withdraw(invoice: str, value: int=0, description: str='') -> dict:
    value = decode_invoice(invoice)['amount'] if (value == 0) \
            else value 
    return fetch(
        'POST', '/lightning/send', json={
            'amount': value, 'payreq': invoice, 'memo': description}).json()
