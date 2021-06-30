# Coinoslib
Coinos.io is a web custody service that allows you to receive and send Bitcoin payments on several networks (Mainchain, Liquid and Lightning), to facilitate integration into other applications this library was developed.

[Buy me a coffee ☕︎](https://coinos.io/lukedevj)

## Features

- [ ] Account
  - [x] Login account
  - [x] Create new account
  - [x] Logout account
  - [ ] Check Balance
- [ ] Wallet
  - [x] Create new invoice
  - [x] Generate new address
  - [x] Withdraw funds
  - [ ] Create new asset  

## Instalation
<p> This library is not yet in "pipy" so be careful. </p>

```bash
git clone https://github.com/lukedevj/coinoslib.git
cd coinoslib
python setup install
```

## Documentation

<details>
<summary>Step 1: Starting the library and creating an account</summary>

```python
>>> from coinoslib import coinos
>>> from coinoslib import bitcoin
>>> from coinoslib import liquid
>>> from coinoslib import lightning
>>>
>>> username = 'admin'
>>> password = 'admin'
>>>
>>> create = coinos.create(username=username, password=password)
{'id': 14308, 'account_id': 20206, 'fiat': False, 'unit': ...}
```
</details>

<details>
<summary>Step 2: Logging into your account</summary>

```python
>>> login = coinos.login(username=username, password=password)
{'user': {'id': 14308, 'account': {'contract': None, 'id': ...}...}...}
```
</details>


<details>
<summary>Step 3: Receiving payment</summary>

```python
>>> bitcoin_address = bitcoin.address()
{'address': 'bc1q3q5cewpkvdam72xkzeav7q2nyun6vs39ll72zm'}
>>>
>>> liquid_address = liquid.address()
{'address': 'GrCPNDuttDLWt6dFycMPszMeTVXRjdrbox', 'confidentialAddress': 'VJLDLJLuxKMM42UzRkZEYE67ygngd6nQKShuULyUa3zKy4W1QKUsLdZJBekAkFrAPQCsigcfCn27pij9'}
>>>
>>> lightning_invoice = lightning.invoice(value=1, description="Hello, word!")
lnbc10n1psdey60pp55t0xp5ewqsptmtfd2agcsau82p2k74tjeq5rag06zn9phpuwrcnsdq5fpjkcmr09ss8wmmjvssscqzpgsp5u93sd4lw59sy96phtnyyekker44ww467v3zf00vs8mn4e4z7csrq9qyyssqte5j3pck3xl7xdjw03392rt2uy4pszcs7pxplryullg8h73l7zx4g2sg6uhslfl4qqzws84xay2jku3mlh0jj9rc7m5nhjexth4mw8spx0y279
```
</details>

<details>
<summary>Step 2: Making payment</summary>

```python
>>> liquid_withdraw = liquid.withdraw(
  address='VJLDLJLuxKMM42UzRkZEYE67ygngd6nQKShuULyUa3zKy4W3EJfUv7dnyGQwdrkQHESt4e3FjzCqc3zK', 
  value=10000, 
  feerate=1,
  asset=login['user']['account']['asset']
)
{"id":5234,"path":null,"createdAt":"2021-06-30T16:03:53.625Z","updatedAt":"2021-06-30T16:03:53.625Z",...}
>>>
>>> bitcoin_withdraw = bitcoin.withdraw(
  address='bc1q7f7vw85hyxc78zpulgu0hhe2gt6qtf86ne5l5x', 
  value=10000, 
  feerate=1,
  asset=login['user']['account']['asset']  
)
{"id":5627,"path":null,"createdAt":"2021-06-30T17:05:13.10Z","updatedAt":"2021-06-30T17:05:13.10Z",...}
>>>
>>> lightning_withdraw = lightning.withdraw(
invoice='lnbc10n1psdex05pp5fmjekp9j6qzwltsxmwv9u9qhp4ff080g9q56w4cdf7z9vdvm2y0qdqqxq9p5hsqrzjqtqkejjy2c44jrwj08y5ygqtmn8af7vscwnflttzpsgw7tuz9r407le3wgayerjssyqqqqd3qqqq89gqjqsp5qypqxpq9qcrsszg2pvxq6rs0zqg3yyc5z5tpwxqergd3c8g7rusq9qypqsq4k4yxye4mxztzx2aqy5d7ay8mkgqxma9rxgzyxyfnna33wfnze4r3vwvwppeqdd20h5k3ahar5z6qpcfk8adv7dlt6j2jmsj6vnpefsqjk8nvd'
)
{"id":5627,"path":null,"createdAt":"2021-06-30T17:05:13.10Z","updatedAt":"2021-06-30T17:05:13.10Z",...}
```
</details>

## Credits
<footer> Luke Pavsky </footer>
