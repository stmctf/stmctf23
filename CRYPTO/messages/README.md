# STMCTF23 QUESTION

## Information
### Challenge name: 

`messages`

### Categories:
 - `crypto`

### Challenge message:
```
TR:
Bilge'nin Hüsamettin'e attığı mesajları yakaladık. Şifreli olduğunu ve algoritmaya ait parametreleri de önceden yakalamıştık. Mesajını çözmemiz an meselesi. utf-8 şeklinde decode etmeyi unutma.


EN:
We've caught the messages Bilge sent to Hüsamettin. We already know the messages are encrypted and also got the parameters of algorithm. It's matter of time before we decipher the message. Don't forget to use utf-8 while decoding.
```

## Solution:
Verilen parametrelere göre RSA algoritması kullanılmıştır. Verilen mesajlar aşağıdaki yöntemle sayıya çevrilir:

```
message1=b'\x10j\xf5\xfd\xbb\xa1\xf5\x83\xfbo\xac\x87\xe3'
message2=b'\xae\x06#Wg\xb6\xdc\xbd\xd1\x95;\xb6\xff\x9d\xeb\x9aU+\x972\xdb\x91\xf1\xd7{\x84U\xdcQ\xa3E\x08\x87/\x15\xa1*\x04\xac\x95\xf7\xd8\x8c\xa9\x16\xd5Ck\x1fI\xf0\xf2QL\xf3L\\w\x07\x8cE7\xa9N\xa2\xe4_\xa6\x0f\x1b\x0c\x8d\x88P\xbe\x89\x99\x0b\xe3Ov\xfeN\xe8\xa1\xc7\x82|\xbf\x92-\xe0\x8a}\x97\xa6\xe6\x01\xfc\x92\x81\x15\xbaS\xab\xc0\x05\xe2\xba>\xd1!\xb0\x17\xd5'
m1 = int.from_bytes(message1, 'big')
m2 = int.from_bytes(message2, 'big')
```

Bu sayılar çarpılır:

```
7837185078475202203046545453191426242245635455407627444701534290260974392049060093213806626216967427989284256428725844722826510646726653260720898887751261328754925075921895654057886957415021091262028605613603992741075609343294003430495879297501816068158610845749576541441231898828836237789836750358104405215
```

 ve verilen RSA public key online tool ile açılır ve tamsayı hali aşağıdaki şekilde decode edilir:
 ```
 dec = 177990312927920155032321408976398315994273950338079707864327888093531098782768111457943558894264701
 dec.to_bytes((dec.bit_length() + 7) // 8, byteorder='big').decode('utf-8')
 ```
