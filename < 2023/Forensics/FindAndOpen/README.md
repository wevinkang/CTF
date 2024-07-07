The flag.zip file prompts for a password when trying to unzip it.

We'll have to look through the dump.pcap file with wireshark for hints:
This filter gives us many packets obfuscating the real flag/hint: 
```
frame contains "flag"
```
The following unique strings for the decoded packet bytes are as follows:
```
Looking at the packets, there's many MDNS packets which don't appear related. There are other unknown protocol packets that look to be better leads.
Looking at the decoded packet bytes for these packets, we find the following unique strings:
```
1. PBwaWUvQ1RGesabababkjaASKBKSBACVVAVSDDSSSSDSKJBJS
2. PBwaWUvQ1RGe1Maybe try checking the other file
3. AABBHHPJGTFRLKVGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=
4. iBwaWNvQ1RGe1Could the flag have been splitted?
```
Unique string #3 looks like it may be a lead as it appears base64 encoded:
``` 
$ echo 'AABBHHPJGTFRLKVGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=' | base64 -d 
As�1Q,�F��2�2F�R6V7&WC��6�5Dg�#3DD��u����Ebase64: invalid input
```

No luck. Got stuck here at a dead end for a while and hard to look through a write up of this flag challenge. 
The key was the missing knowledge of how base64 encoding works:
> … when the length of the unencoded input is not a multiple of three, the encoded output must have padding added so that its length is a multiple of four. The padding character is =, which indicates that no further bits are needed to fully encode the input.
> https://en.wikipedia.org/wiki/Base64#Output_padding

Added padding to string #3.
> aaAABBHHPJGTFRLKVGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=

Giving us: 
> *This is the secret: picoCTF{R34DING_LOKd_

The other part of the flag is likely in the password protected zip file. Let's try this first half of the flag as the password. 
Success!
``` 
└─$ cat flag    
picoCTF{R34DING_LOKd_fil56_succ3ss_b98dda6a}
```
