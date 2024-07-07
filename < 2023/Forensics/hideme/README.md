Download the provided file, "flag.png"

Nothing found using file, exiftool, steghide. 
Binwalk is a tool for searching binary images for embedded files and executable code.
``` bash
binwalk flag.png
```
```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 512 x 504, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed
39739         0x9B3B          Zip archive data, at least v1.0 to extract, name: secret/
39804         0x9B7C          Zip archive data, at least v2.0 to extract, compressed size: 2869, uncompressed size: 3024, name: secret/flag.png
42908         0xA79C          End of Zip archive, footer length: 22
```

There looks to be an embedded zip file:

``` bash
unzip flag.png
```
```
Archive:  flag.png
warning [flag.png]:  39739 extra bytes at beginning or within zipfile
  (attempting to process anyway)
   creating: secret/
  inflating: secret/flag.png
```

``` bash
cd secret | eog flag.png
```
Gives us a picture of the flag:
```
picoCTF{Hiddinng_An_imag3_within_@n_ima9e_cda/2af0}
```
