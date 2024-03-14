from PIL import Image
from pyzbar.pyzbar import decode

import os

# Fotografi cekilen QR kodlarinin dizin adi
dir_in = "dir_in"

# FOtograf Dosya Tipi
filetype = ".png"

# Imajin boyutuna gore degistirilmesi gerekiyor
# QR kodundan biraz buyuk olmasi yeterli
img_size = 110 # iphone6s ile cekilen foto (1/4)
img_size = 140 # samsung_GT_S5660 ile cekilen foto (1/16)
img_size = 90

# QR kodlarinin uzerinde yururken her adimda ne kadar ilerlenecegi
# Kucuk olursa zaman uzuyor, buyuk olursa flag kacirilabiliyor
image_walk = 5

# dir_in klasorundeki tum dosyalari list olarak alir
resimler = next(os.walk(dir_in), (None, None, []))[2]
resimler.sort()

# Tum resimlerde deniyoruz
for resim in resimler:

    # Baska dosyalar varsa onlari islemesin
    if filetype not in resim:
        continue

    filenamepath = os.path.join(dir_in, resim)
    print ("Dosya ismi: ", filenamepath)

    img = Image.open(filenamepath)
    w, h = img.size

    # DEBUG
    # Acilan imajin boyutu
    # print ("imaj w, h: ", w, h)

    # Dikeyde yurume
    flagfound = False
    for walk_h in range(0, h, image_walk):

        # DEBUG
        # print ("walk_h: ",walk_h)

        # Yatayda yurume
        for walk_w in range(0, w, image_walk):

            # Belirlenen olculerde resmi buyuk resimden alma
            cropped = img.crop((walk_w, walk_h, walk_w+img_size, walk_h+img_size))

            # DEBUG
            # Islenen resimlerin ne oldugunu gormek icin
            # img_size degiskeninde verilen deger ile croplanan imaj, qr kodlarindan kucuk olmamalidir.
            # bu bilgiyi de asagidaki kodu calistirarak yapabiliriz.
            # save_path = os.path.join("dir_out","croped " + str(walk_w) + "-" +  str(walk_h) + ".png")
            # cropped.save(save_path,'PNG')

            # DEBUG
            # data = decode(Image.open(save_path))

            data = decode(cropped)
            if len(data) > 0:

                # # DEBUG
                # print(str(data[0]))

                if "STMCTF" in str(data[0]):
                    print(str(data[0]))
                    flagfound = True
                    break

        if flagfound:
            break

            # DEBUG
            # os.remove(save_path)
