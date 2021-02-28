from web3 import Web3

RPC_URL="https://mainnet.infura.io/v3/81a9d68f92af428ab0cbc1f3dca05e6d"

web3 = Web3(Web3.HTTPProvider(RPC_URL))

ethereum_address="0xC2A8923D33464f147a3F07C59Ab603Da70825F97"

print("is Connected:", web3.isConnected())

balance = web3.eth.getBalance(ethereum_address)
print("balance:", web3.fromWei(balance, "ether"))

