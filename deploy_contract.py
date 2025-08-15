from web3 import Web3
import json

# Connect to Ganache (install Ganache GUI or use ganache-cli)
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

if not w3.is_connected():
    print("❌ Cannot connect to Ganache. Please start Ganache on port 7545")
    exit()

print("✅ Connected to Ganache blockchain")

# Load compiled contract
with open('src/blockchain/contract_abi.json', 'r') as f:
    abi = json.load(f)

with open('src/blockchain/contract_bytecode.txt', 'r') as f:
    bytecode = f.read().strip()

# Set default account
w3.eth.default_account = w3.eth.accounts[0]
print(f"Using account: {w3.eth.default_account}")

# Deploy contract
EvidenceChain = w3.eth.contract(abi=abi, bytecode=bytecode)

# Submit transaction
tx_hash = EvidenceChain.constructor().transact()
print(f"Deployment transaction: {tx_hash.hex()}")

# Wait for transaction receipt
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
contract_address = tx_receipt.contractAddress

print(f"✅ Contract deployed successfully!")
print(f"Contract address: {contract_address}")

# Save contract address
with open('src/blockchain/contract_address.txt', 'w') as f:
    f.write(contract_address)

print("✅ Contract address saved to src/blockchain/contract_address.txt")

# Test contract interaction
contract_instance = w3.eth.contract(address=contract_address, abi=abi)

# Test submit evidence
test_tx = contract_instance.functions.submitEvidence(
    "test_hash_123",
    "metadata_hash_456", 
    "Test evidence submission"
).transact()

receipt = w3.eth.wait_for_transaction_receipt(test_tx)
print(f"✅ Test evidence submitted successfully! TX: {test_tx.hex()}")

# Verify evidence
result = contract_instance.functions.verifyEvidence("test_hash_123").call()
print(f"✅ Evidence verification result: {result}")
