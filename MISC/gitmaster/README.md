# STMCTF23 QUESTION

## Information
### Challenge name: 

`gitmaster`

### Categories:
 - `misc`

### Challenge message:
```
TR:
Git konusunda kendini biraz zorlaman gerekiyor.

EN:
You need to push yourself a little bit about git.
```

## Solution:

Verilen rpm dosyasının içerisinden bulundurduğu dosyalar çıkarılır:

```
$ rpm2cpio hello-1.0-1.fc38.x86_64.rpm | cpio -idmv
./usr/bin/hello
./usr/lib/.build-id
./usr/lib/.build-id/8f
./usr/lib/.build-id/8f/aa938f2793fa8903961162aba0e1be7727d26f
./usr/share/licenses/hello
./usr/share/licenses/hello/LICENSE
```

LICENSE dosyası içerisinde ipucu bulunmaktadır:
```
$ cat ./usr/share/licenses/hello/LICENSE
This is a license file.

See my git repo for further details.
```

İpucunda bir git reposundan bahsedilmektedir. rpm dosyaları metadata bilgilerinde paketin URL'si hakkında bilgi tutmaktadır. Bu bilgiye strings ile bakmak mümkündür. strings ile bakıldığında aşağıdaki URL görülür:

`http://husamettin.stmctf.com/husamettin/hello`

Bu URL'e tarayıcı üzerinden gidilip içinde bulunan tek dosya incelenir. 

```
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
```

git commit geçmişi incelendiğinde bir dosyanın 16'lık tabandaki çıktısının satırlarının bulunduğu görülür. İlk satırından da bu dosyanın bir PNG dosyası olduğu görülür. Öncelikle git commit geçmişinden satırlar çıkarılır:

```
$ git clone http://husamettin.stmctf.com/husamettin/hello.git
$ cd hello
$ for i in $(git rev-list master); do git checkout $i 2>/dev/null; cat mysterious_file >> ../dump; done
```
dump dosyasında xxd komutunun çıktısı bulunmaktadır fakat offset'lere bakıldığında sıralı değildir. Offset'lere göre sıralandığında xxd komutu ile tekrar binary formata çevrilir:
```
$ awk '{val="0x" $1; sub("^0x0x","0x",val); print strtonum(val),$0 ;}' dump | sort -n | sed 's/^[^ ]* //' | xxd -r > flag.png
```

flag.png açıldığında alt tarafta flag bulunmaktadır.