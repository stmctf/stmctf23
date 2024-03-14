# STMCTF23 QUESTION

## Information
### Challenge name: 

`Secure Downloader`

### Categories:
 - `Crypto`

### Challenge message:
```
TR:
http://securedownloader.stmctf.com adresinde bir dosya transfer uygulaması keşfettik. Dosyalar şifrelenmiş olarak paylaşılıyor. Çok gizli bir bilginin bu uygulama aracılığıyla paylaşıldığını düşünüyoruz. Bu bilgiyi bulmada bize yardım et.

EN:
At http://securedownloader.stmctf.com, we discovered a file transfer application. Files are shared encrypted. We think that a very confidential information is shared through this application. Help us find this information.
```

## Solution:

TR:

Uygulamanın kaynak dosyası incelendiğinde 

```<!-- TODO: Implement other modes --> ```

yorumu ile karşılaşılır. Uygulamanın önyüzde listelenenlerden daha fazla modu desteklediği anlaşılıyor. Dosya listesinde bazı görüntü dosyaları bulunuyor. ECB modunun da bu tip dosyalar için kullanılması bilgi sızıntısına neden olabilir. Gönderilecek olan formda `mode` değeri `ecb` yapılarak görüntü dosyaları indirilir. `922497.png` dosyası herhangi bir algoritma ile `ecb` modda indirildiğinde flag görüntü dosyasında okunabilir olarak bulunur.

EN:

When the source file of the application is inspected

``<!-- TODO: Implement other modes --> ```

encounters a comment. It appears that the app supports more modes than those listed on the frontend. There are some image files in the file list. Using the ECB mode for these types of files may cause information leakage. In the form to be sent, the `mode` value is set to `ecb` and the image files are downloaded. When the `922497.png` file is downloaded using `ecb` mode with any algorithm, the flag is found as readable in the image file.
