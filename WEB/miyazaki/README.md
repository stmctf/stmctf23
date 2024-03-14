# STMCTF23 QUESTION

## Information
### Challenge name:

`Miyazaki`

### Challenge:

`Fuzzing, scripting, bypassing, file upload to command injeciton`

### Categories:

- `Web`

### Challenge message:

```
miyazaki.stmctf.com
```

## Solution:

1) Ip ile siteye giriş yapılır, yapım aşamasında olduğu görülür.
2) Dizin araması yapılarak 'files' dizinine ulaşılır.
3) Resimler indirilerek bazılarında bulunan URL metadası not edilir.
4) Basit bir script ile metadata verilerini alıp yerleri değiştirilerek url sayfası bulunmaya çalışılır ve 'FAmATeRYloUnTEnTeRiDepYrOnAlR' bulunur.
5) Sayfaya gidildiğinde yetkisiz erişim olduğu görülür.
6) Sayfa kaynağı incelendiğinde kullanıcı adı ve paroların olduğu dizin görülür.
7) Sayfaya 'X-Forwarded-For' header eklenince yetkisiz erişimi bypass edilebileceği görülür. Böylelikle giriş sayfasına ulaşılır.
8) Altıncı adımda edinilen bilgiler ile giriş sayfasına brute force yapılarak kullanıcı adı ve parolanın 'JOHNS':'lucky13' olduğu bulunur.
9) Site incelendikten sonra dosya yükleme kısmı bulunur ve zararlı bir png dosyası yüklenerek code injection zafiyeti ile flag okunur.
