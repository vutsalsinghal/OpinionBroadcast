pragma solidity ^0.4.23;

contract Opinion{
	address owner;
	constructor() public{owner = msg.sender;}

	// Dictionary of addresses that are approved to share opinions
	mapping (address => bool) approvedOpinionGiver;
	string opinion;
	 
	// Event to announce an opinion on the blockchain
	event OpinionBroadcast(address _opinionGiver, string _opinion);
	
	modifier onlyOwner {
		require(msg.sender == owner);
		_;
	}
	
	// Function has 'payable' modifier so it'll invoked when ether is sent to the contract address.
	function() public payable{
		// msg is a special variable that contains information about the transaction
		if (msg.value > 50000000000000000) {  
			//if the value sent greater than 0.05 ether (in Wei)
			// then add the sender's address to approvedOpinionGiver 
			approvedOpinionGiver[msg.sender] = true;
		}
	}
	
	// Read-only function that checks if the specified address is approved to broadcast opinions.
	function isApproved(address _opinionGiver) public view returns (bool approved) {
		return approvedOpinionGiver[_opinionGiver];
	} 
	
	// Read-only function that returns the current opinion
	function getCurrentOpinion() public view returns(string) {
		return opinion;
	}

	// Function modifies the state on the blockchain
	function broadcastOpinion(string _opinion) public returns (bool success) {
		// Looking up the address of the sender will return false if the sender isn't approved
		if (approvedOpinionGiver[msg.sender]) {
			opinion = _opinion;
			emit OpinionBroadcast(msg.sender, opinion);
			return true;
			
		} else {
			return false;
		}
	}

	// Function to transfer ether to the owner
    function transferAmt(uint amount) public onlyOwner{
    	owner.transfer(amount);
    }

	// Function to self-destruct contract if need be!
	function kill() public onlyOwner{
			selfdestruct(owner);
	}
}
