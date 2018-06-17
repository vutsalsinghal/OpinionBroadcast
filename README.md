# [Tutorial]OpinionBroadcast

This start contract allows anyone to broadcast their opinion to the blockchain where it’ll be viewable for the rest of eternity. But there is a one time 0.05 Ether fee you need to pay in order to do so!

NOTE: This is a tutorial to get you a feel for deploying smart contracts and interacting with them on Ropsten TestNet. The process will be quite similar for deploying and interacting with contracts on MainNet.

## Requirements

- (Use of virtualenv is highly suggested!) `pip install requirements.txt`
- MetaMask [extension](https://metamask.io/)
- Remix - Solidity [IDE](https://remix.ethereum.org/#optimize=true)
- Get API key by creating free account on [Infura](https://infura.io/). This will enable us to work with Ropsten TestNet without hosting our own node. Infura will do the heavy lifting for us!

These are all the tools you need to delpoy the smart contracts and interact with it!

## Deployment

- Create ethereum account using MetaMask. Make sure to choose "Ropsten Test Network"
- Request few ethers from the test [faucet](https://faucet.metamask.io/)
- Go to Remix solidity IDE and copy-paste the contents of opinion.sol file in the IDE.
- Click on "Start to compile" from the Compile tab in the top right corner.
- After compiling it, go to Run tab and click on "deploy". Metamask should bring up a popup asking you to confirm the transaction. If not, just open the Metamask extension and do it there.
- A message at the bottom of the Remix console will notify you when the contract is deployed. You can click on the link to explore the transaction on [ropsten.etherscan.io](https://ropsten.etherscan.io/). Note the contracts address!

## Interact with the contract via [Web3.py](https://github.com/ethereum/web3.py)

- Replace lines 6-10 of opinion.py accordingly. You can get your account's private key from the "menu" in the MetaMask extension.
