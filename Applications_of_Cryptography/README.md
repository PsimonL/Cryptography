# Selected application topics of Cryptography in modern Information and Communication Technology


## Contents
1. Asymmetric vs Symmetric Ciphers
2. Hashes and fingerprints
3. SSH vs Telnet
4. SSL/TLS
5. PKI
6. Coding vs Ciphers vs Hashes
7. Diffie - Hellman Key Exchange

## 1. Asymmetric vs Symmetric Ciphers
A **cipher** is an algorithm used to transform plaintext into ciphertext (encoded data) using a specific **encryption function**. The key properties of an encryption function are:
- **Reversible**: Unlike a hash, encryption is designed to be reversible. The original plaintext can be recovered from the ciphertext using the correct decryption function and key.
- **Key-dependent**: Encryption requires a secret key, which is used both to encrypt and decrypt the data. The same key or a paired key (in the case of asymmetric encryption) is necessary to reverse the encryption process.
- **Confidentiality**: The main goal of encryption is to ensure that only authorized parties can read the encrypted data. Without the correct decryption key, the data is incomprehensible.
- **Variable output**: In most encryption algorithms, especially in those using an initialization vector (IV), the encrypted output (ciphertext) can differ even when the same plaintext is encrypted multiple times. This prevents patterns in ciphertext from being easily analyzed.
### Symmetric Ciphers
- **Definition**:  
    + The most important characteristic of symmetric cryptography is that it uses the **same key** for both encryption and decryption of the message.  
    + As a result, the key must be known to both the sender and the recipient.  
    + Operations are performed relatively quickly, which also implies lower computational requirements.  
    + However, the key distribution poses a problem because the key must be delivered to the recipient through a pre-defined **secure channel**.  
- **Examples of popular symmetric algorithms**:  
    - **DES (Data Encryption Standard)**  
    - **AES (Advanced Encryption Standard)**, the successor of DES  
    - **3DES (Triple DES)**, an enhanced version of DES  
    - **Blowfish**  
    - **Twofish**
---
#### DES
# TODO: to describe
---
#### AES
# TODO: to describe
---
### Asymmetric Ciphers
- **Definition**:  
    + Unlike symmetric cryptography, it uses **two keys**: a public key and a private key. The public key is publicly available, while the private key remains confidential.  
    + The **private key MUST NOT be disclosed**! Cause it's being used to DECRYPT data. 
    + The public key can be freely distributed and it's being used in ENCRYPTION process.
    + Encryption and decryption are significantly slower, requiring higher computational power.  
- **Examples of popular asymmetric algorithms**:  
    - **RSA (Rivest–Shamir–Adleman)**  
    - **ECC (Elliptic Curve Cryptography)**, which is more efficient than RSA  
    - **DSA (Digital Signature Algorithm)**   
    - **ElGamal**
    - **Diffie - Hellman Key Exchange**
---
#### RSA
# TODO: to describe
---
#### DSA
# TODO: to describe
---
#### Diffie-Hellman
Section number 7 is directly for that algorithm. :)

## 2. Hashes and fingerprints
A **hash** is a fixed-length string of characters that is generated from an input using a **hash function**. The key properties of a hash function are:
- **Deterministic**: The same input will always produce the same output hash. 
- **Fast to compute**: Hash functions are designed to quickly generate the hash from the input.
- **Pre-image resistance**: It should be computationally infeasible to reverse-engineer the original input from the hash value.
- **Small changes in input change the hash significantly**: Even a small change in the input (e.g., changing one character) results in a completely different hash value.
- **Collision resistance**: It is very difficult to find two different inputs that produce the same hash value.
- **Fixed length**: Regardless of the input size, the output hash is always of a fixed length (e.g., SHA-256 always produces a 256-bit hash).

### Common Hashing Algorithms:
1. **MD5 (Message Digest Algorithm 5)**:
   - Produces a 128-bit hash value.
   - Previously popular, but now considered broken and not suitable for cryptographic use due to vulnerabilities.
2. **SHA-1 (Secure Hash Algorithm 1)**:
   - Produces a 160-bit hash value.
   - While more secure than MD5, SHA-1 is also deprecated due to collision vulnerabilities.
3. **SHA-256**:
   - Part of the SHA-2 family of algorithms.
   - Produces a 256-bit hash value and is widely used for cryptographic purposes, including in SSL/TLS certificates and Bitcoin.
4. **SHA-3**:
   - A more recent cryptographic hash function with improved security and efficiency over SHA-2.
### Uses of Hashes:
- **Data Integrity**: Hashes are used to verify the integrity of data. By comparing the hash of the original data to the hash of the received data, one can confirm that the data has not been altered.
- **Digital Signatures**: Hashes are used in the creation of digital signatures. A hash of the message is signed by the sender's private key.
- **Password Storage**: Hashes are used to securely store passwords. The password is hashed before being stored, and the system compares the hashes during authentication, not the passwords themselves.
---

### What is a Fingerprint?
A **fingerprint** is essentially a shorter version of a hash value, typically used to identify a certificate or file in a more human-readable way.
The term **fingerprint** is commonly used in the context of **digital certificates** (e.g., SSL/TLS certificates) and files. A certificate fingerprint is a hash of the certificate, often represented as a sequence of hexadecimal characters. Key Properties of a Fingerprint:
- **Unique**: Each fingerprint corresponds to a unique certificate or file.
- **Compact**: A fingerprint is a shorter representation of a larger object (e.g., a certificate).
- **Readable**: It is easier to work with and share, especially in contexts where the actual certificate or file may be too large.


## 3. SSH vs Telnet


## 4. SSL/TLS
Transport Layer Security (TLS), as well as its predecessor, Secure Sockets Layer (SSL), uses both symmetric as well as asymmetric encryption.
Works in 6th OSI/ISO model layer - presentation layer. It ensures that protocols of 7th application layer are secured like: HTTP (HTTPS), FTP (SFTP) or TELNET (SSH).  
Key Features of SSL:  
- Encryption: The SSL uses encryption algorithms to protect data during transmission.
- Authentication: The SSL verifies the identity of the server to ensure that data is sent to the correct destination.
- Data Integrity: The SSL ensures that data has not been altered during the transmission.
---
TLS procedure:  
1. It all starts with TLS handshake procedure. Client sends message which includes TLS version and list of algorithms handled by user. That's the asymmetric algorithm usage part to establish secure connection. It can be RSA algo.
Server shares his public key wit user after initial request from user.
2. Client uses server public key to:   
a) encrypt data necessary to generate session key.  
b) OPTIONAL: prove clients identity.
Finally, sends info back.
3. The server uses its to decrypt the data sent by the client. This data is used by both the server and the client to generate the same **session key**.
4. The exchanged session key is used for **symmetric encryption**, enabling secure communication for the rest of the session. The algorithm used for symmetric can be AES.
---
In every exchanged message are being used hashing functions to make sure that nothing has been altered during transmission (Man-in-the-Middle Attack).

## 5. PKI
**Public Key Infrastructure (PKI)** is a set of roles, policies, hardware, software, and procedures needed to create, manage, distribute, use, store, and revoke digital certificates and manage public-key encryption (asymmetric cryptography).
The purpose of a PKI is to provide a more secure method of authentication and identity verification than simple passwords, ensuring the involved parties' identities in secure communication.
A PKI system enables the creation, storage, and distribution of digital certificates, which are used to verify that a particular public key belongs to a specific entity. PKI maps public keys to entities via certificates, securely stores these certificates in a central repository, and can revoke them if necessary.
---
Main Components of PKI:  
1. **Public Key**:
   - Can be publicly shared.
   - Used to encrypt data or verify the identity of an entity via digital signatures.
2. **Private Key**:
   - Stored securely by its owner and **never shared publicly**.
   - Used to decrypt data or to create digital signatures.
3. **Certificate Authority (CA)**:
   - An organization responsible for issuing, managing, renewing, and revoking digital certificates.
4. **Registration Authority (RA)**:
   - Acts as a mediator between users and the CA.
   - Verifies the identity of entities before a certificate is issued by the CA.
5. **Certification Repository**:
   - A centralized storage system for issued certificates and Certificate Revocation Lists (CRLs), which list invalid or compromised certificates.
---
Sample Process for Acquiring an SSL Certificate:  
1. **Requesting a Certificate**:
   - The website owner generates a key pair (public and private keys).
   - A Certificate Signing Request (CSR) containing the public key and website details is submitted to a Certificate Authority (CA).
2. **Validation by the CA**:
   - The CA verifies the identity of the requester (e.g., the domain ownership or organizational details).
3. **Issuing the Certificate**:
   - If validation is successful, the CA issues a digital certificate linking the public key with the website’s domain.
4. **Installation**:
   - The issued SSL certificate is installed on the website's server.
   - The server is now capable of establishing secure connections via HTTPS.
---
HTTPS vs HTTP - SSL Certificate Validation Process:

**HTTP (Hypertext Transfer Protocol)**:
- Communication is unencrypted.
- Data sent over HTTP can be intercepted and read by third parties.
- No authentication mechanism to confirm the identity of the website.

- **HTTPS (HTTP Secure)**:
- Utilizes SSL/TLS encryption to secure communication.
- Steps in HTTPS involving SSL certificate validation:
  1. **Handshake**: The browser connects to the server and requests a secure connection.
  2. **Certificate Verification**: 
     - The server provides its SSL certificate.
     - The browser verifies the certificate against a trusted list of CAs and checks for expiration or revocation.
  3. **Session Encryption**:
     - Once verified, the browser and server negotiate a shared session key for encrypting further communication.

- Ensures:
  - Confidentiality: Data is encrypted.
  - Integrity: Prevents data tampering.
  - Authenticity: Verifies the server's identity.
---
Using PKI and SSL/TLS ensures secure and trustworthy communication in modern web applications and services.

## 6. Coding vs Ciphers vs Hashes
**Coding**:  
They server to transform data into a different format for representation or transmission, often in a reversible manner.
Not focused on security; primarily for efficiency or compatibility.  
Examples include:  
> Morse Code

> Base64 

> ASCII or UNICODE

> UTF-8 

> URL encoding

_Use Case_: Storing or transmitting data in a standardized format.  

---
**Ciphers**:
Aim is to transform data (plaintext) into an unreadable format (ciphertext) for security purposes, making it unusable without a proper key.  
Used for encryption and decryption.
Focused on confidentiality, ensuring that only authorized parties can access the information.
Reversible if the correct key is provided.
Ciphers are not always deterministic. Different instances of may produce different outputs especially when used with initialization vector, IV methods.
Can be divided into two categories:
> Symmetric ciphers (e.g., AES, DES): Use the same key for encryption and decryption.

> Asymmetric ciphers (e.g., RSA, ECC): Use a public key for encryption and a private key for decryption.

_Use Case_: Securing communications, protecting sensitive data.  

---
**Hashes**:
 To transform data into a fixed-size string (hash value) that represents the original data in a unique way. The transformation ment to be irreversible.
One-way function: You cannot derive the original data from the hash value.
Focused on integrity and data verification, not confidentiality.
Commonly used for verifying data integrity or generating digital signatures.  
Hashes are always deterministic. The same input to hash function will always produce the same output.
Examples:  
> MD5

> SHA-1
 
> SHA-2

> SHA-3

> SHA-256

_Use Case_: Ensuring data has not been changed e.g. blockchain blocks or digital identities.

## 7. Diffie - Hellman Key Exchange
Diffie-Hellman Key Exchange algorithm (DH) is part of asymmetric cryptography. But whole point of that algorithm is not to encrypt/decrypt communication or to authenticate someone's digital identity.
It's main purpose is to safely exchange key for symmetric methods - session key.
But from definition of asymmetric algos; every side of connection have its own private and public key.

### Procedure overview explained on colors
![image](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.comparitech.com%2Fwp-content%2Fuploads%2F2019%2F03%2Fdiffie-hellman-2.jpg&f=1&nofb=1&ipt=0e7b56d0cf324ce56f3c0659408e215ec2cb921499542287593214db653d1907&ipo=images)

### Mathematical notation:
1. Setting up public parameters:
- Alice and Bob publicly agree to use **p and q non-secret** values:
   + ```p => modulus``` - large prime number
   + ```g => base``` - primitive root of modulo p

Where: $g < p$

2. Choosing secret **private keys**
- Alice chooses integer ```a``` (**secret private key of Alice, should not be shared**)
- Bob chooses integer ```b``` (**secret private key of Bob, should not be shared**)

3. Calculating **public keys**
- Alice calculates public key, based on settled public parameters and her own private key: $A = g^a mod (p)$

- Bob calculates public key, based on settled public parameters and his own private key: $B = g^b mod (p)$

Those keys are going to be **exchanged** during process between Alice and Bob.

4. Calculating **session key** based on **received public key** and already **calculated private key**:
- Alice calculates: $K_A = B^a mod (p) => (g^b)^a mod(p) = K$

- Bob calculates: $K_B = A^b mod (p) => (g^a)^b mod(p) = K$

So $K = K_A = K_B$. Both Alice and Bob have arrived at the same values because under ```mod p```.

### Why is it so safe?
- The security relies on the difficulty of solving the [discrete logarithm problem](http://ramanujan.math.trinity.edu/rdaileda/teach/s18/m3341/lectures/discrete_log.pdf): even if an attacker knows ```g```, ```p```, ```A``` and ```B```, they cannot efficiently determine ```a``` or ```b```, and thus cannot reconstruct ```K```.  


- [Secrecy state](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange):
![image](https://i.ytimg.com/vi/SmcFWbdv_Hk/maxresdefault.jpg)


https://www.youtube.com/watch?v=NmM9HA2MQGI&ab_channel=Computerphile  
> Worth noticing: in described procedure, session key is never being sent over the network.