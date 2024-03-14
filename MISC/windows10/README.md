# STMCTF23 QUESTION

## Information
### Challenge name: 

`Windows 10`

### Categories:
 - `MISC`

### Challenge message:
```
windows10.stmctf.com
```

---

## Solution - TR:

Açıklamadaki linke gidilir. Karşımıza bir windows 10 giriş sayfası gelir.

![alt img1](solution/Screenshot_1.png "resim 1")

Herhangi bir yere tıklandığında ya da herhangi bir tuşa basıldığın şifre girme bölümü ve kullanıcı profil fotoğrafı açığa çıkar.

![alt img2](solution/Screenshot_2.png "resim 2")

Profil fotoğrafındaki qr code taratılır.

![alt img3](solution/Screenshot_3.png "resim 3")

QR Code dan çıkan base64 şifreli kod decode edilir.

![alt img4](solution/Screenshot_4.png "resim 4")

Bulunan sonuç ile windows'a giriş yapılır. Masaüstü gezilirken chrome açıldığında içeride giriş ve masaüstü ekranlarından farklı olarak STM Siber Füzyon Merkezinden bir fotoğraf görülür.

![alt img5](solution/Screenshot_5.png "resim 5")

Fotoğraf indirilerek exiftool çıktısı kontrol edildiğinde flag'e ulaşılır.

![alt img6](solution/Screenshot_6.png "resim 6")

---

## Solution - EN:

Go to the link in the description. A Windows 10 login page appears.

![alt img1](solution/Screenshot_1.png "resim 1")

When you click anywhere or press any button, the password entry section and user profile photo are revealed.

![alt img2](solution/Screenshot_2.png "resim 2")

The QR code in the profile photo is scanned.

![alt img3](solution/Screenshot_3.png "resim 3")

The base64 encrypted code resulting from the QR Code is decoded.

![alt img4](solution/Screenshot_4.png "resim 4")

You can log in to Windows with the result found. When Chrome is opened while browsing the desktop, a photo from the STM Cyber Fusion Center is displayed, unlike the login and desktop screens.

![alt img5](solution/Screenshot_5.png "resim 5")

The flag can be accessed by downloading the photo and checking the exiftool output.

![alt img6](solution/Screenshot_6.png "resim 6")
