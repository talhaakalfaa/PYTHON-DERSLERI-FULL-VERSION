# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
#kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w": (Write) yazma modu. 
#   ** Dosyayı konumda oluşturur.
#   ** Dosya içeriğini siler ve yeniden ekleme yapar.


# file = open("newfile.txt","w")
# file = open("C:/users/Talha/desktop/newfile.txt","w")
# file.close()

# file = open("newfile.txt","w",encoding='utf-8')
# file.write("talhakalfa")
# file.close()


# "a": (Append) ekleme. Dosyayı konumda yoksa oluşturur.

# file = open("newfile.txt","a",encoding='utf-8')
# # file.write("\nçağan kalfa")
# file.write("çağan kalfa\n")
# file.close()



# "x": (Create) oluşturma. Dosya zaten varsa hata verir.

# file = open("newfile2.txt","x",encoding='utf-8')




# "r": (Read) okuma. Varsayılan. Dosya konuöunda yoksa hata verir. 