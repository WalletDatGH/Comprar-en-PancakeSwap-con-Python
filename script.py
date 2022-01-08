import time
from web3 import Web3
 
PancakeABI = open('pcABI','r').read().replace('\n','')
 
bsc="https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))
print(web3.isConnected())
 
#Mi direccion publica
sender_address = "Dirección de tu Wallet Publica"
 
#Direccion Pancake V2 Swap router address
router_address = "0x10ED43C718714eb63d5aA57B78B54704E256024E"
 
#Contrato de BNB
spend = web3.toChecksumAddress("0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c")
 
#Clave privada de tu Wallet
private="Tu clave privada"

balance = web3.eth.get_balance(sender_address)
#print(balance)
 
humanReadable = web3.fromWei(balance,'ether')
#print(humanReadable)
 
#Token que quieres recibir, en este caso BUSD
contract_id = web3.toChecksumAddress("0xe9e7cea3dedca5984780bafc599bd69add087d56")

contract = web3.eth.contract(address=router_address, abi=PancakeABI)
 
nonce = web3.eth.get_transaction_count(sender_address)
 
start = time.time()
print(web3.toWei('0.005','ether'))
 
pancakeswap2_txn = contract.functions.swapExactETHForTokens(
  0, 
  [spend,contract_id],
  sender_address,
  (int(time.time()) + 1000000)
).buildTransaction({
  'from': sender_address,
  'value': web3.toWei(0.005,'ether'),#Cantidad en BNB
  'gas': 250000,
  'gasPrice': web3.toWei('5','gwei'),
  'nonce': nonce,
})
 
signed_txn = web3.eth.account.sign_transaction(pancakeswap2_txn, private_key=private)
tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
print(web3.toHex(tx_token))