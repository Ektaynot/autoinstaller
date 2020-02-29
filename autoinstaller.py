import os
system=input("Select Your Package Manager:\n1:APT\n2:Pacman\n3:Zypper")
def cod(ad):
    if system == "1":
        os.system("sudo apt update")
        os.system(("sudo apt -y install "+ad))
    elif system == "2":
        os.system("sudo pacman -Syy")
        os.system(("sudo pacman -Sy --noconfirm "+ad))
    elif system == "3":
        os.system("sudo zypper update")
        os.system(("sudo zypper -y install "+ad))
sayı="a"
while sayı != "q":
    sayı=input("Please write the things you want to install (write q to exit):")
    dosya = open("willdownload.txt","a")
    if sayı == "q":
        break
    else:
        dosya.write(sayı+" ")
oku=open("willdownload.txt","r")
select=input("If you are okay with the things down below write yes"+"\n"+oku.readline())
if select == "evet" or "yes":
    oku=open("willdownload.txt","r")
    cod((oku.readline()))
else:
    raise SystemExit
