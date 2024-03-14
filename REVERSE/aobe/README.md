# STMCTF23 QUESTION

## Information
### Challenge name:

`aobe`

### Categories:
`Reverse`

### Challenge message:fexe
```
TR:
Çalıştırılabilir bir ELF dosyasıydı, bir bitini değiştirdik, artık çalışmıyor.

EN:
It was an executable ELF file; we changed one bit, and now it doesn't work.
```


## Solution:
```
./aobe
bash: ./aobe: cannot execute binary file: Exec format error
```

```
file aobe
aobe: ELF 32-bit LSB no file type, Intel 80386, version 1 (SYSV)
```

![](solution/writeup-cd89a2a7.png)

https://en.wikipedia.org/wiki/Executable_and_Linkable_Format

e_type  0x10  2 bytes

0x00	ET_NONE	Unknown.

0x02	ET_EXEC	Executable file.

![](solution/writeup-89639bba.png)


![](solution/writeup-9da4a9ea.png)

```
file aobe
aobe: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, not stripped
```
---![](solution/writeup-85b3bd2b.png)
