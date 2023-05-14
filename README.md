# Data Security Project 03 - Grupi 24 

### General Info 
A [university](https://fiek.uni-pr.edu) team project organised by Data Security Subject.  

## What's the project about?
The Client and the Server communicate with each other exchanging encrypted messages
1. Exchanging keys
* The client and the server exchange their keys where the private key is protected with their public key.
  * Before the communicating begins the two parts do some sort of handshake!
2. The algorythm which we're going to implement for encrypting messages is [Data Encryption Standard - CBC Mode](https://https://en.wikipedia.org/wiki/Des)
* How does DES CBC work? 
  * The DES CBC encryption process requires a 64-bit cryptographic key. Of the 64 bits, 56 are used directly by the DES CBC process, and 8 are odd parity bits, with    one parity bit occupying the right-most bit of each octet
4. After the messages are exchanged between the Client and the Server then they are decrypted using their private keys.

### Technologies 
The implementation of the program was made using [Java](https://www.java.com/en/) Programming Language.

### Contributors

- [Gentrit Kryeziu](https://github.com/Gentrit851)

- [Klajdi Gashi](https://github.com/KlajdiGashi)

- [Kleda Gashi](https://github.com/kledagashi)

- [Krenare Kryeziu](https://github.com/Krenare158)
