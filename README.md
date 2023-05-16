# Data Security Project 03 - Grupi 24 

### General Info 
A [university](https://fiek.uni-pr.edu) team project organised by Data Security Subject.  

## What's the project about?
The Client and the Server communicate with each other exchanging encrypted messages.
1. First the client sends the encrypted message to the server 
* The private key is shared between the two parts (Client and Server) through a file which containts the private key.
2. The algorythm which we're going to implement for encrypting messages is [Data Encryption Standard](https://https://en.wikipedia.org/wiki/Des)
* How does DES work? 
  * DES uses a 64-bit key to encrypt 64-bit blocks. Of these 64 bits in the key, eight specific bits (known as parity bits) are used to check for errors in the           ciphertext. Every eighth bit is used as a parity bit, leaving 56 effective bits in the key. 
  * After the verification of the ciphertext, these eight parity bits are dropped.
3. Afterwards the server recieves the message and decrypts it using the private key from the file and the result containts the plaintext.

### Technologies 
The implementation of the program was made using [Python](https://www.python.org/) Programming Language.
The execution of the code was made using a simple GUI. 

### Contributors

- [Gentrit Kryeziu](https://github.com/Gentrit851)

- [Klajdi Gashi](https://github.com/KlajdiGashi)

- [Kleda Gashi](https://github.com/kledagashi)

- [Krenare Kryeziu](https://github.com/Krenare158)
