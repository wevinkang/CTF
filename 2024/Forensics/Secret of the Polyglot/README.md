Downloading the supposed pdf file gives us what looks to be an incomplete flag:
```
1n_pn9_&_pdf_2a6a1ea8}
```

Went to the command line to further check the file's contents:
``` bash
cat flag2of2-final.pdf
```

The file shows a lot of gibberish, but the first word is, "PNG"
So pivot to changing the file extension of flag2of2-final.pdf to flag2of2-final.png then opening the file gives us the rest of the flag: 
```
picoCTF{f1u3n7_
```

Flag: picoCTF{f1u3n7_1n_pn9_&_pdf_2a6a1ea8}

# Lessons learned:

Looking at other's methods of completing this flag, I learned some new useful forensics commands.

file cmd lets us check the file type:
```
file flag2of2-final.pdf  
flag2of2-final.pdf: PNG image data, 50 x 50, 8-bit/color RGBA, non-interlaced
```
