from requests import Session

session = Session()

class Coinoslib:

    def __init__(self, token: str):
        self.__auth = {'authorization': f'bearer {token}'}
        self.__url = 'https://coinos.io/api'

    def fetch(self, method, path: str = '/', json=None) -> object:
        if method == 'post':
            fetch = session.post
        else:
            fetch = session.get

        fetch = fetch(f'{self.__url}/{path}', json=json, headers=self.__auth)
        if not fetch.status_code == 200:
            raise Exception('Request failed.')
        else:
            return fetch

    def get_balance(self) -> int:
        """Returns the current balance of the wallet."""
        list_invoices = self.list_invoices()
        return int(list_invoices[0]['account']['balance']) if list_invoices else 0

    def add_invoice(self, value: int, memo: str) -> str:
        """Add a new invoice."""
        return self.fetch('post', 'lightning/invoice', json={'amount': value, 'memo': memo}).text

    def pay_invoice(self, invoice: str) -> dict:
        """Pay an invoice over lightning."""
        return self.fetch('post', 'lightning/send', json={'payreq': invoice}).json()

    def list_invoices(self) -> dict:
        """List all outgoing payments."""
        return self.fetch('get', 'payments').json()

    def lookup_invoice(self, invoice: str) -> dict:
        """Lookup an existing invoice by its payment hash."""
        filter_list_invoices = list(filter(lambda tx: tx['hash'] == invoice, self.list_invoices()))
        return filter_list_invoices[0] if filter_list_invoices else None