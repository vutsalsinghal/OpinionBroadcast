#!/home/pyofey/.virtualenvs/pyeth/bin/python3
import time, sys
from contract_abi import abi
from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider('https://ropsten.infura.io/<YOUR-KEY>'))

contract_address     = w3.toChecksumAddress('0x7cEA0D686D503420D1D6673500237B9b54085f73')
wallet_address       = w3.toChecksumAddress('0x8b8ba03ed61ad1cb0e9befd0d02ecb444834887d')
wallet_private_key   = '<YOUR-KEY>'
contract = w3.eth.contract(address=contract_address, abi=abi)

def send_ether_to_contract(amount_in_ether):
    print('Preparing to send {} ether to contract...'.format(amount_in_ether))
    amount_in_wei = amount_in_ether*1000000000000000000
    nonce = w3.eth.getTransactionCount(wallet_address)

    txn_dict = {
            'to': contract_address,
            'value': int(amount_in_wei),
            'gas': 140000,
            'gasPrice': w3.toWei('14', 'gwei'),
            'nonce': nonce,
            'chainId': 3 #ID:3 for Ropsten Testnet
    }

    signed_txn = w3.eth.account.signTransaction(txn_dict, private_key=wallet_private_key)
    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)   
    print('Waiting for txn to be mined...')
    txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)
    print('txn_receipt: ',txn_receipt)
    
def check_whether_address_is_approved(address):
    return contract.functions.isApproved(address).call()

def get_current_opionion():
    return contract.functions.getCurrentOpinion().call()

def broadcast_an_opinion(opn):
    print('Broadcasting opinion "{}"'.format(opn))
    nonce = w3.eth.getTransactionCount(wallet_address)
    txn_dict = contract.functions.broadcastOpinion(opn).buildTransaction({
        'chainId': 3,
        'gas': 140000,
        'gasPrice': w3.toWei('14', 'gwei'),
        'nonce': nonce,
    })

    signed_txn = w3.eth.account.signTransaction(txn_dict, private_key=wallet_private_key)
    result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print('Waiting for txn to be mined...')
    txn_receipt = w3.eth.waitForTransactionReceipt(result)
    print('txn_receipt :',txn_receipt)
    processed_receipt = contract.events.OpinionBroadcast().processReceipt(txn_receipt)
    print('processed_receipt: ',processed_receipt)
    
    output = "\nAddress {} broadcasted the opinion: {}"\
        .format(processed_receipt[0].args._opinionGiver, processed_receipt[0].args._opinion)
    print(output)
    return {'status': 'added', 'processed_receipt': processed_receipt}

def transfer_amount(amt_in_ether):
    print('Transfering {} ether to owner!'.format(amt_in_ether))
    nonce = w3.eth.getTransactionCount(wallet_address)
    txn_dict = contract.functions.transferAmt(amt_in_ether*1000000000000000000).buildTransaction({
        'chainId': 3,
        'gas': 140000,
        'gasPrice': w3.toWei('14', 'gwei'),
        'nonce': nonce,
    })

    signed_txn = w3.eth.account.signTransaction(txn_dict, private_key=wallet_private_key)
    result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    print('Waiting for txn to be mined...')
    txn_receipt = w3.eth.waitForTransactionReceipt(result)
    print('txn_receipt: ',txn_receipt)

def kill_contract():
    print('Contract self-destruct initiated...')
    nonce = w3.eth.getTransactionCount(wallet_address)
    txn_dict = contract.functions.kill().buildTransaction({
        'chainId': 3,
        'gas': 140000,
        'gasPrice': w3.toWei('14', 'gwei'),
        'nonce': nonce,
    })

    signed_txn = w3.eth.account.signTransaction(txn_dict, private_key=wallet_private_key)
    result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    print('Waiting for txn to be mined...')
    txn_receipt = w3.eth.waitForTransactionReceipt(result)
    print('txn_receipt: ',txn_receipt)


# Function calls:

#send_ether_to_contract(0.051)
#print('Approved to broadcast opinion?:',check_whether_address_is_approved(wallet_address))
#print('Current opinion: ',get_current_opionion())
#broadcast_an_opinion('Hi There!')
#transfer_amount(2)
#kill_contract()
