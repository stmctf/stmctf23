# STMCTF23 QUESTION

## Information
### Challenge name: 

`Värit`

### Categories:
 - `mobile`


## Solution - TR:

Uygullama çalıştırıldığında bir şey yapılamaz. Verilen apk dosyası jadx gibi bir araç ile decompile edilir ve projenin yapısına bakılır. AndroidManifest.xml dosyasında bir tane intent'in export edildiğini görülür. 
Bu inten'i görüntüleyebilmek için terminalde;

```
adb shell
am start -n com.example.palette/.FlagActivity
```

komutları yazılır. İntent artık emülatörde görünür hale gelir. Bu intent'de 6 tane renkten oluşur bir renk paleti vardır. Bu renk paletnin HEX kodları birleştirilerek flag elde edilir.


## Solution - EN:

Nothing can be done when the application is running. The given apk file is decompiled with a tool such as jadx and the structure of the project is examined. It is seen that one intent has been exported in the AndroidManifest.xml file.
To view this intent in the terminal;

```
adb shell
am start -n com.example.palette/.FlagActivity
```

commands are written. The intent is now visible in the emulator. This intent has a color palette consisting of 6 colors. The flag is obtained by combining the HEX codes of this color palette.

