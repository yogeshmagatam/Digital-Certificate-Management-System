// services/blockchain.js
import { ethers } from "ethers";
import contractABI from "./contractABI.json";

const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();
const contractAddress = "0xYourContractAddress";
const contract = new ethers.Contract(contractAddress, contractABI, signer);

export const anchorCertificate = async (hash) => {
  const tx = await contract.storeCertificateHash(hash);
  await tx.wait();
};
