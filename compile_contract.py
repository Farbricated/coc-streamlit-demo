from solcx import compile_source, set_solc_version
from web3 import Web3
import json
import os

# Set Solidity version
set_solc_version('0.8.0')

# Smart contract source code
contract_source = '''
pragma solidity ^0.8.0;

contract EvidenceChain {
    struct Evidence {
        string fileHash;
        string metadataHash;
        uint256 timestamp;
        address submitter;
        string description;
        bool exists;
    }
    
    mapping(string => Evidence) public evidenceRecords;
    mapping(address => bool) public authorizedUsers;
    
    event EvidenceSubmitted(
        string indexed fileHash,
        address indexed submitter,
        uint256 timestamp
    );
    
    constructor() {
        authorizedUsers[msg.sender] = true;
    }
    
    modifier onlyAuthorized() {
        require(authorizedUsers[msg.sender], "Unauthorized access");
        _;
    }
    
    function addAuthorizedUser(address _user) public onlyAuthorized {
        authorizedUsers[_user] = true;
    }
    
    function submitEvidence(
        string memory _fileHash,
        string memory _metadataHash,
        string memory _description
    ) public onlyAuthorized {
        require(!evidenceRecords[_fileHash].exists, "Evidence already exists");
        
        evidenceRecords[_fileHash] = Evidence({
            fileHash: _fileHash,
            metadataHash: _metadataHash,
            timestamp: block.timestamp,
            submitter: msg.sender,
            description: _description,
            exists: true
        });
        
        emit EvidenceSubmitted(_fileHash, msg.sender, block.timestamp);
    }
    
    function verifyEvidence(string memory _fileHash) 
        public 
        view 
        returns (bool, uint256, address, string memory) {
        
        Evidence memory evidence = evidenceRecords[_fileHash];
        
        if (evidence.exists) {
            return (
                true,
                evidence.timestamp,
                evidence.submitter,
                evidence.description
            );
        }
        
        return (false, 0, address(0), "");
    }
}
'''

# Compile contract
compiled_sol = compile_source(contract_source)

# Extract contract interface
contract_id, contract_interface = compiled_sol.popitem()

# Get ABI and bytecode
abi = contract_interface['abi']
bytecode = contract_interface['bin']

print("✅ Contract compiled successfully!")
print(f"ABI entries: {len(abi)}")
print(f"Bytecode length: {len(bytecode)}")

# Save ABI to file
os.makedirs('src/blockchain', exist_ok=True)
with open('src/blockchain/contract_abi.json', 'w') as f:
    json.dump(abi, f, indent=2)

with open('src/blockchain/contract_bytecode.txt', 'w') as f:
    f.write(bytecode)

print("✅ Contract ABI and bytecode saved to src/blockchain/")
