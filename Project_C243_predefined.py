from web3 import Web3

url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 = Web3(Web3.HTTPProvider(url))

latest_block = web3.eth.getBlockNumber()

print("Latest Block of Ethereum blockchain: {latest_block}")

latest_block = web3.eth.getBlock(latest_block_number)
block_transaction_count = latest_block['transactions']
print("Number of transactions happened in the block: {len(block_transaction_count)}")

block_count = 10  
newest_block = 'latest'  
reward_percentiles = None  
Transaction_fee = web3.eth.fee_history(block_count, newest_block, reward_percentiles)
print("Number of transactions happened in the block: {len(Transaction_fee['reward'])}")


