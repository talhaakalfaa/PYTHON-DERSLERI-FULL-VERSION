# with open("newfile.txt","r+", encoding="utf-8") as file:
#     file.seek(20)
#     file.write("deneme")

# with open("newfile.txt","r+", encoding="utf-8") as file:
#     print(file.read()) 


# ******* SAYFA SONUNDA GÜNCELLEME ******* #


# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nSelin Oğuz")


# ******* SAYFA BAŞINDA GÜNCELLEME ******* #


# with open("newfile.txt","r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "Minnoş Kalfa" + content
#     file.seek(0)
#     file.write(content)




# ******* SAYFA ORTASINDA GÜNCELLEME ******* #

with open("newfile.txt","r+", encoding="utf-8") as file:
   list = file.readlines() 
   list.insert(1,"meto sırlı\n")
   file.seek(0)
   file.writelines(list)

with open("newfile.txt","r", encoding="utf-8") as file:
   print(file.read())