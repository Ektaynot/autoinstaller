import os
def cod(ad):
    os.system("sudo apt update")
    os.system(("sudo apt -y install"+" "+ad))
sayı="a"
while sayı != "q":
    sayı=input("lütfen indirmek istediğiniz şeyi yazın(durmak için q yazın):")
    dosya = open("willdownload.txt","a")
    if sayı == "q":
        break
    else:
        dosya.write(sayı+" ")
oku=open("willdownload.txt","r")
select=input("Aşağıdaki ürünler indirilicek kabul ediyorsanız evet yazın"+"\n"+oku.readline())
if select == "evet":
    oku=open("willdownload.txt","r")
    cod((oku.readline()))
else:
    raise SystemExit
