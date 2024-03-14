# STMCTF23 QUESTION

## Information
### Challenge name: 

`elbilge`

### Categories:
 - `crypto`

### Challenge message:
```
TR:
Bir şirkette yazılım mühendisi olarak çalışan Hüsamettin'den bir şifreleme algoritmasını kodlaması istenmiştir. Şirketin kriptografi uzmanı Bilge, Hüsamettin'e algoritmanın adımlarının tek tek açıklayan güzel ama biraz uzun bir e-posta atar. Hüsamettin ise uzun e-postayı okumak yerine wikipedia'dan algoritmayı bulup oradan geliştirir fakat mod almayı unutur. Doğruluğunu test etmek için Bilge'ye geliştirme ortamının linkini gönderir. Hüsamettin'in geliştirdiği web arayüzünü kullanarak algoritmayı kırmalısın.

EN:
Hüsamettin, who works as a software engineer in a company, was asked to code an encryption algorithm. Bilge, the company's cryptography expert, sends Hüsamettin a nice but long e-mail explaining the steps of the algorithm one by one. Instead of reading the long e-mail, Hüsamettin finds the algorithm on Wikipedia and implements it from there, but forgets to use the modulo operation. He sends the link of his development environment to Bilge to test its accuracy. You must crack the algorithm using the web interface developed by Hüsamettin.

```

## Solution:

Verilere bakıldığında 2 şifrelenmiş değer gelmektedir. soru adı da göz önüne alındığında elgamal algoritması olduğu anlaşılır. c1 değeri sabit, c2 değerinin her sayfa yenilendiğinde değiştiği görülür.

Soru metninde mod alınmadığı bilgisi verilmiştir. Bu bilgi ışığında c2 değerlerinin en büyük çarpanı alındığında flag ortaya çıkar.
