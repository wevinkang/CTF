Starting point:
``` bash
ssh -p 54801 ctf-player@rhea.picoctf.net
ls
```
We see the files and directories:
```
checksum.txt  decrypt.sh  files
```

The files directory has many files, too many to manually check the hashes, so let's use the wildcard for searching the directory and grep the given hash:
``` bash
sha256sum files/* | grep 55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a
```
```
55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a  files/2cdcb2de
```

Now that we have the filename, we can use the decrypt script given to us to decrypt the file and give us the flag:
``` bash
./decrypt.sh files/2cdcb2de 
```
# Flag
```
picoCTF{trust_but_verify_2cdcb2de}
```
