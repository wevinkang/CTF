Download the file, "trace.pcap"

I opened the file with Wireshark for analysis.
Immediately, wee some anomalous traffic. One of the packets shows info for a Malformed Packet:
```
0000   45 00 00 37 00 01 00 00 40 11 7c b3 7f 00 00 01   E..7....@.|.....
0010   7f 00 00 01 00 35 00 35 00 23 2e cd 69 42 77 61   .....5.5.#..iBwa
0020   57 4e 76 51 31 52 47 65 31 46 6c 61 67 20 69 73   WNvQ1RGe1Flag is
0030   20 63 6c 6f 73 65 3d                               close=
```
The packet following this one shows an FTP packet with the attempted credentials from the src, 172.16.0.2:
```
0000   45 00 00 4a 00 01 00 00 40 06 c3 98 ac 10 00 02   E..J....@.......
0010   0a fd 00 06 00 14 00 15 00 00 00 00 00 00 00 00   ................
0020   50 02 20 00 10 a4 00 00 20 20 20 20 75 73 65 72   P. .....    user
0030   6e 61 6d 65 20 72 6f 6f 74 20 20 20 20 70 61 73   name root    pas
0040   73 77 6f 72 64 20 74 6f 6f 72                     sword toor
```
Let's filter to see all traffic from the mentioned src IP:
```
ip.src == 172.16.0.2
```
Packet 507's packet bytes gives us the flag:
```
0000   45 00 00 52 00 01 00 00 40 06 c3 90 ac 10 00 02   E..R....@.......
0010   0a fd 00 06 00 14 00 15 00 00 00 00 00 00 00 00   ................
0020   50 02 20 00 b4 83 00 00 70 69 63 6f 43 54 46 7b   P. .....picoCTF{
0030   50 36 34 50 5f 34 4e 34 4c 37 53 31 53 5f 53 55   P64P_4N4L7S1S_SU
0040   35 35 33 35 35 46 55 4c 5f 33 31 30 31 30 63 34   55355FUL_31010c4
0050   36 7d                                             6}
```
Alternatively, we can simply brute force the challenge and filter for the flag:
``` 
frame contains "picoCTF"
```
