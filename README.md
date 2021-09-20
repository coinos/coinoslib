# Coinoslib
Coinos.io is a web custody service that allows you to receive and send Bitcoin payments on several networks (Mainchain, Liquid and Lightning), to facilitate integration into other applications this library was developed.

[![Donate](https://img.shields.io/badge/Donate-Bitcoin-green.svg)](https://coinos.io/lukedevj)


## Instalation

```bash
git clone https://github.com/lukedevj/coinoslib.git
cd coinoslib
python setup install
```
## Setup

- [Create Account](https://coinos.io/)
- [Get WJT Token](https://coinos.io/settings)

```python
>>> from coinoslib import Coinoslib 
>>>
>>> coinoslib = Coinoslib(<token>)
>>>
>>> # Add a new invoice.
>>> coinoslib.add_invoice(1, memo='Hello, word!')
lnbc10n1ps53ertpp5xkh2kj5xx3hwxtv0gvykjwnwee6t6dlk2crdj0uen6svqtenpenqdq5fpjkcmr09ss8wmmjvssscqzpgxqyz5vqsp5edas0dg8gqevk4ey0j6yg34a9ec9gn7v5cf5zlc5kq0x0ec0ngsq9qyyssqq28uy663nqw0em2fyzcagx6g0t4ukm2hx4wsfj7rzmhrakuggrc4q5jrd652satnxy0k93w8cj0wn62skslamf3yfr50duwejvqkvkgp8f0yjv
>>>
>>> # Returns the current balance of the wallet.
>>> coinoslib.get_balance()
1
>>> # Pay an invoice
>>> coinos.pay_invoice('lnbc10n1ps53eh6pp5trq7mttdzjj0np9lsq5wpufstqpq59dn29f8y7fwsmhqp6xa0fdqdqcyq58v6tpypxyu5zptyhxxmefcqzpgxqyz5vqsp5mvecr7z94ussajk892e7lc729xuke6xvq8v354ckvgrdqfzpr4lq9qyyssqff0d2e6elksx3s0x7pg2gzl5s3wlrwue8h8247dc9yeedtr7fpm5qjmqec8ygg2vvffde56y3r6ngk8vsd6099mywc6ardvyalcf7vqquqy90u')
{'id': None, 'invoice_id': None, 'path': None, 'memo': None, 'address': None, 'received': None, 'tip': 0, 'redeemed': False, 'redeemcode': None, 'amount': -1, 'account_id': None, 'user_id': None, 'hash':'lnbc10n1ps53eh6pp5trq7mttdzjj0np9lsq5wpufstqpq59dn29f8y7fwsmhqp6xa0fdqdqcyq58v6tpypxyu5zptyhxxmefcqzpgxqyz5vqsp5mvecr7z94ussajk892e7lc729xuke6xvq8v354ckvgrdqfzpr4lq9qyyssqff0d2e6elksx3s0x7pg2gzl5s3wlrwue8h8247dc9yeedtr7fpm5qjmqec8ygg2vvffde56y3r6ngk8vsd6099mywc6ardvyalcf7vqquqy90u'}
>>>
>>> # List invoices
>>> coinoslib.list_invoices()
{'id': None, 'account_id': None, 'invoice_id': None, 'user_id': None, 'path': None, 'memo': None, 'hash': 'lnbc1ps533qlpp57j5xck6j73j8vw2v0dkd6z9jqrkfww3xmyxl543cqxcc6ftus7jqdqqcqzpgxqyz5vqsp5dhaqz8g7j3ftly6g3uw5nue0tvyzmrl03mltlg3v4m6sljuvwarq9qyyssq6prm4jh9su24ups0dgcjz79tqv0h2t9kechk57kgp9ee4l5hys63xppq8alumfzldylau64zjt7swag9579qnu9s0p7kyrp3lw5naacq02sw23'}
>>>
>>> # Lookup invoice
>>> coinoslib.lookup_invoice('lnbc1ps533qlpp57j5xck6j73j8vw2v0dkd6z9jqrkfww3xmyxl543cqxcc6ftus7jqdqqcqzpgxqyz5vqsp5dhaqz8g7j3ftly6g3uw5nue0tvyzmrl03mltlg3v4m6sljuvwarq9qyyssq6prm4jh9su24ups0dgcjz79tqv0h2t9kechk57kgp9ee4l5hys63xppq8alumfzldylau64zjt7swag9579qnu9s0p7kyrp3lw5naacq02sw23')
{'id': None, 'account_id': None, 'invoice_id': None, 'user_id': None, 'path': None, 'memo': None, 'hash': 'lnbc1ps533qlpp57j5xck6j73j8vw2v0dkd6z9jqrkfww3xmyxl543cqxcc6ftus7jqdqqcqzpgxqyz5vqsp5dhaqz8g7j3ftly6g3uw5nue0tvyzmrl03mltlg3v4m6sljuvwarq9qyyssq6prm4jh9su24ups0dgcjz79tqv0h2t9kechk57kgp9ee4l5hys63xppq8alumfzldylau64zjt7swag9579qnu9s0p7kyrp3lw5naacq02sw23', 'rate': 43933.83, 'preimage': '', 'network': 'lightning', 'currency': 'USD', 'address': None, 'received': 1, 'amount': 1, 'fee': 0, 'tip': 0, 'redeemed': False, 'redeemcode': None, 'confirmed': 1, 'account': {'contract': None, 'id': None, 'user_id': None, 'path': None, 'seed': None, 'network': None, 'name': 'Bitcoin', 'domain': None, 'ticker': 'BTC', 'asset': '', 'balance': 0, 'pending': 0, 'hide': None, 'index': 0, 'privkey': None, 'pubkey': None, 'precision': 8}}
```


