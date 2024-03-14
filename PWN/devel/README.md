# STMCTF23 QUESTION

## Information
### Challenge name: 

`devel`

### Categories:
- `WEB/PWN`

### Challenge message:
```
devel.stmctf.com
```

## Solution:
#### 1.	BİLGİ TOPLAMA > Aktif Tarama
Hedef makinede çalışan servisleri bulmak ve varsa bilinen herhangi bir güvenlik açıklarını bulmak için, varsayılan betik (-sC) ve servis dökümü alma (-sV) bayraklarıyla çalışan nmap taramayla hedef hakkında bilgi toplamaya başlayalım:

![Image](solution/image.png)

Aktif tarama bize TCP/21 (FTP), TCP/22(SSH) ve TCP/80 (Apache Web Server) portlarının ve üzerinde çalışan servislerinin açık olduğunu gösteriyor.


#### 2.	KEŞİF YAPMA > Dosya ve Dizin Keşfi
Kutuda bulunan dosyaları ve dizinleri keşfetmek için gobuster kullanarak php, html ve txt uzantılarını kullanarak erişilebilir web uygulama dosyalarını ve dizinlerini tarıyoruz:

![Image](solution/image-1.png)

Dizin ve dosya taraması, _dev isimli ilginç bir dizin sağlar, böylece bu dizinin altındaki dizinleri ve dosyaları keşfetmek için tekrar gobuster'ı çalıştırabiliriz:

![Image](solution/image-2.png)

Bu sefer _dev dizini altında taramamız sonucu, geliştiricilerin kodlarını test etmeleri için bir test dizini gibi görünen başka bir dizini testing ismiyle ortaya çıkartıyor. Öyleyse FTP servisinin araştırılmasına devam edelim:

![Image](solution/image-3.png)

Nmap, FTP için anonim girişlerin etkinleştirildiğini ortaya çıkardığında, dosyaları yükleyebileceğimiz herhangi bir dizinimiz olup olmadığını kontrol ederiz. Şansımıza, web sunucusunda da bulduğumuz, yazılabilir olarak testing dizinimiz var:

![Image](solution/image-4.png)

Testing web sunucusundaki ile aynı dizin gibi görünüyor. Bu yüzden oraya bir php web shell yüklersek ve sonra bir reverse shell elde etmek için web sunucusundan bu reverse shell dosyasına erişebilir ve Kali’mize bağlantı tetikleyebiliriz.


#### 3.	KAYNAK GELİŞTİRME > Kabiliyet Elde Etme: Exploit’ler
Kısaca, testing dizini hem WEB hem de FTP hizmetlerine hizmet verecek şekilde yapılandırılmıştır! İstismarımızı başlatmak için, ilk önce FTP kullanarak sunucuya web shell dosyası yüklemeye başlayabiliriz:

![Image](solution/image-5.png)

PHP reverse shell (web shell) dosyasında IP ve port bilgilerini değiştiriyoruz:

![Image](solution/image-6.png)

reverse.php dosyasını testing dizinine yerleştiriyoruz:

![Image](solution/image-7.png)

Şimdi buna web tarayıcısından erişmeli ve netcat dinleyicimizde shell almalıyız. Bir dinleme soketi açın ve reverse.php dosyasını tıklayın:

![Image](solution/image-8.png)

Shell çalışıyor. Güzel! www-data kullanıcısı adıyla hedef sistemde standart kullanıcı yetkileriyle erişim kazandık:

![Image](solution/image-9.png)

Bir süre ilginç dosyalar için makineyi inceledikten sonra, alışılmadık bir şekilde /var/backups/ dizininde keys.zip dosyası olduğunu gördük:

![Image](solution/image-10.png)

Şimdi saldırgan makinemizde bir dinleyici başlatıp, çıktıyı bir dosyaya yönlendirip ardından zafiyetli makinede ise netcat kullanarak girdiyi keys.zip dosyası olarak alacak şekilde yönlendirerek görevi tamamlıyoruz:
Kali Linux’teki dinleme noktamız:

![Image](solution/image-11.png)

Keys.zip dosyasını zafiyetli kutudan Kali'ye aktarmak için netcat komutu:

![Image](solution/image-12.png)

Başarılı aktarımı test etmek için md5sum kullanabiliriz çünkü netcat bazen güvenilmez olabiliyor:

![Image](solution/image-13.png)

Zafiyetli kutudaki keys.zip dosyasının hash değeri, Kali Linux'ta indirilen keys.zip ile eşleşmelidir:

![Image](solution/image-14.png)


#### 4.	İLK ERİŞİM > Geçerli Hesaplar: Yerel Hesaplar
Zip dosyasını indirdikten sonra parola korumalı olduğunu görüyoruz, böylece johntheripper'ı parolayı kırmak için kullanabiliriz, böylece rockyou.txt parola listesini kullanarak zip içeriğini görebiliriz:

![Image](solution/image-15.png)

![Image](solution/image-16.png)

keys.zip dosyasının parolası: supermocel
Zip dosyasını çıkardıktan sonra, intern kullanıcısı için SSH anahtarları içerdiğini bulduk. Bu anahtarları kutuya giriş yapmak ve intern kullanıcısının sahip olduğu tüm yetkileri almak için kullanabiliriz ve dolayısıyla kutuda başka bir intern kullanıcı yetkilerine sahip olabiliriz.

![Image](solution/image-17.png)

İşte bu SSH açık anahtarının intern kullanıcı oturumu için olduğunun kanıtı:

![Image](solution/image-18.png)

Artık intern kullanıcı yetkisiyle user.txt dosyasını okuyabiliyoruz:

![Image](solution/image-19.png)


#### 5..	YETKİ YÜKSELTME > Yetki Yükseltme Kontrol Mekanizmasını Kötüye Kullanma: Setuid ve Setgid
Dizini Kali Linux'ta betiğimizin bulunduğu HTTP sunucusu olarak ayarlama komutu:

![Image](solution/image-20.png)

Betiği Kali'deki HTTP sunucusundan zafiyetli kutuya indirip çalıştırıyoruz:

![Image](solution/image-21.png)

Döküm alma betiğini çalıştırdıktan sonra, sed'in setuid bit setine sahip olduğunu görebiliriz, böylece sed'i root erişimi elde etmek için kullanabiliriz:

![Image](solution/image-22.png)

Find komutunu uygun parametrelerle çalıştırdığımızda, komut çıktısının sed binary’sinin gerçekten SUID bitinin ayarlandığını göstermektedir. Sh ile sed kullandığımızda şansımıza herhangi bir kodu çalıştırmamıza izin vermeden önce yetki düşmektedir:

![Image](solution/image-23.png)

Şimdi root yetkilerine sahip başka bir kullanıcı oluşturmak için /etc/passwd dosyasını değiştirmek gibi başka yollarla sed'i istismar etmemiz gerekir:

![Image](solution/image-24.png)

Yani temelde bu yöntemde openssl kullanarak bir parola hash değeri oluşturuyoruz ve sonra /etc/passwd dosyasını ürettiğimiz hash ile başka bir kullanıcı eklemek için güncelliyoruz. Öyleyse önce hash'i oluşturalım:

![Image](solution/image-25.png)

```
$1$xyz$cEUv8aN9ehjhMXG/kSFnM1
```

Artık /etc/passwd dosyasını sed kullanarak değiştirebiliriz ve kullanıcıyı yukarıda oluşturulan hash ile birlikte ekleyebiliriz. 
Secret_user oluşturduk ve şifresi aşağıdaki sed komutunda belirtilen şifredir. Şimdi root yetkilerini elde etmek için bu secret_user hesabını kullanarak giriş yapabiliriz. Ve şimdi kutuyu root seviyesi yetkileriyle tamamen ele geçirdik:

```
sed -i ‘$ a secret_user:\$1\$xyz\$cEUv8An9ehjhMXG\/kSFnM1:0:0:root:\/root:\/bin\/bash’ /etc/passwd
```

Bu da kanıt olarak root.txt dosyasının içeriğidir.

![Image](solution/image-26.png)

