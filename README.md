p2pefs
======

##Peer 2 Peer Encrypted File System##

Allows people to back up files distributed across a network.

Files are divided into chunks, encrypted on the client using a key the client specifies.

When file chunks are received by the host they generate a one-time key, send it to the client, and encrypt the file again with the one-time key.

* No host has more than one chunk of a file. 
* No host receives the initial encryption key. 
* Hosts only specify their space and connection constraints.
