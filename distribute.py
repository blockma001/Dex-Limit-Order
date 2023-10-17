# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 16:07:31 2021

@author: 97191
"""

from web3 import Web3
import time

poly = "https://rpc-mainnet.maticvigil.com/"
web3 = Web3(Web3.HTTPProvider(poly))
BridgeContractAddress = web3.toChecksumAddress('0x714BeaeE043948433ED3B9CFbbb22a2aEEC9a89d')
BridgeAbi = '[{"constant":false,"inputs":[{"name":"_token","type":"address"}],"name":"claim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"minFee","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address[]"},{"name":"_value","type":"uint256[]"}],"name":"sendEth","outputs":[{"name":"_success","type":"bool"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[],"name":"feePercent","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_tokenAddress","type":"address"},{"name":"_to","type":"address[]"},{"name":"_value","type":"uint256[]"}],"name":"sendErc20","outputs":[{"name":"_success","type":"bool"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"name":"_feePercent","type":"uint8"}],"name":"setFeePercent","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'

private_key = ''
sender_address = ''

add = ['0x35BA7B713a405beA50F364ce52A8089CE73C19fb','0xF47e8AB6629821dB8aeb1ed3114438B81483bA7a']
val = [400000000000000,400000000000000]

BridgeContract = web3.eth.contract(address=BridgeContractAddress, abi=BridgeAbi)
sender_address = web3.toChecksumAddress(sender_address)
balance = web3.eth.get_balance(sender_address)
humanReadable = web3.fromWei(balance, 'ether')
nonce = web3.eth.get_transaction_count(sender_address)

print(str(web3.isConnected()))
print('balanceOf:' + str(humanReadable) + 'matic')


txn = BridgeContract.functions.sendEth( add, val).buildTransaction({
 	'from': sender_address,
 	'chainId': 137,
 	'nonce': nonce,
 	'gas': 360000,
 	'value': 800000000000000,
 	'gasPrice': web3.eth.gasPrice,
})

signed_txn = web3.eth.account.sign_transaction(txn, private_key)
tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
print(str(web3.toHex(tx_token)))