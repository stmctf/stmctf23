# STMCTF23 QUESTION

## Information
### Challenge name: 

`Dark`

### Categories:
 - `Stego`

### Challenge message:
```
TR:
Karanlığın içine gömülmüş bir dosya. Bakalım gün yüzüne çıkacak mı ?

EN:
A file plunged into darkness. Will it come to light?

```

## Solution:

Soruda  bize  secret.jpg  adlı  bir  doysa  veriliyor.  Dosyayı  açtığımızda  ise  siyah  bir  görüntü  ile karşılaşıyoruz. Dosya hakkında daha fazla bilgi elde etmek için file komutunu çalıştırıyoruz. 

![image](https://user-images.githubusercontent.com/74919981/191480132-d230f6af-4e4f-495b-82d0-2da646db94d4.png)

File komutu çıktısına bakarak dosyamızın uzantısından emin oluyoruz. Fotoğraf içerisine gizlenmiş bir verinin var olup olmadığını kontrol etmek için steghide aracından faydalanıyoruz. 

![image](https://user-images.githubusercontent.com/74919981/191480170-8797c1b8-d117-4da4-99c3-5467f9a28765.png)

steghide  info  secret.jpg  komutunu  çalıştırdığımızda  fotoğraf  içerisinde  1kblık  bir  veri  olduğunu görüyoruz ancak veriyi çıkartmak için parolaya ihtiyacımız var. Bir ipucu bulmak ümidiyle exiftool ile fotoğrafın meta verilerine bakıyoruz.

![image](https://user-images.githubusercontent.com/74919981/191480210-21cc5a67-3360-4e3e-83a9-b04441be3f62.png)

User Comment tagi bir kullanıcı tarafından oluşturulduğundan dikkatimizi çekiyor. İlk bakışta anlamsız görünen bu metinin dikkatli bakınca base64 ile kodlanmış bir metin olduğunu farkediyoruz. Base64 kodunu çözmek için cyberchef online aracını kullanıyoruz. 

![image](https://user-images.githubusercontent.com/74919981/191480257-feffcb7c-5535-49e9-be44-5ebce2f07b59.png)

Tahminimzde yanılmadık ve ilk ipucumuzu bulduk: [mod4...]. Ancak  bu  ipucunu  nerede  kullanacağımızı  henüz  bulamadık.  Fotoğrafın  diğer  meta  verilerine  de bakıyoruz ancak göze çarpan herhangi bir şey yok her şey normal görünüyor. Fotoğrafın ayarlarıyla oynayarak  bir  şeyler  bulup  bulamayacağımıza  bakıyoruz.  Herhangi  bir  online  editöre  yüklüyoruz fotoğrafı.  Işık  ayarlarıyla  biraz  oynadığımızda  arkaplanda  bir  şeylerin  değiştiğini  görüyorüz  ve netleşene kadar  ayarları değiştirmeye devam ediyoruz. 

![image](https://user-images.githubusercontent.com/74919981/191480309-312aa8b4-654f-45fb-a0f0-c74972eea12c.png)

Karşımıza iyi düşümemizi söyleyen kafa karıştırıcı bir metin çıkıyor. Ayrıca bir takım dizi işlemlerine işaret eden ikinci ipucumuzu da bulmuş olduk. İlk ipucumuzdan ( [mod4...] ) yola çıkarak fotoğraftaki cümleyi  bir  dizinin  elemanları  gibi  düşünerek  0.indxten  itibaren  dörder  dörder  ilerlemeye  karar veriyoruz. Bu işlem sonucunda “Senin bu soruda ihtiyacın olan anahtar burada” şeklinde bir cümleye ulaştık. İkinci ipucumuzu kullanmak için terminal üzerinde python geliştirme ortamını açıyoruz. İkinci ipucumuzu da kullanrak yazdığımız basit script sonucunda bir çıktı alıyoruz. 

![image](https://user-images.githubusercontent.com/74919981/191480349-315ec3c5-1b28-4985-938e-f1db797c3d75.png)

Elde  ettiğimiz  çıktıyı  steghide  aracında  dosyayı  extract  etmek  için  gereken  parola  kısmında kullanıyoruz. 

![image](https://user-images.githubusercontent.com/74919981/191480422-7bbe648c-4362-4bc1-9c42-f3406abed3a9.png)

Ve parola doğru ! Fotoğraf içerisinden congrat.txt adlı bir metin belgesi çıkarttık bunun içeriğini cat komutu ile görüntülediğimizde ise flagimize ulaştık: 



