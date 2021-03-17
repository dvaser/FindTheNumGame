
import os, Methods, re

class _ControlMenu:
    
    def checkMenu(helloMenu):
        if helloMenu not in range(1,5):
            raise Exception("Tuslamayi dogru yapiniz.")
        else:
            Methods._Methods.timer(seconds=0.5)  

    def checkGameMenu(gameMenu):
        if gameMenu not in range(1,3):
            raise Exception("Tuslamayi dogru yapiniz.")
        else:
            Methods._Methods.timer(seconds=0.5)  

    def checkNumOfUser(numOfUser):
        if not 0 < len(numOfUser):
            raise Exception("Oyuncu sayisi giriniz.")
        elif 0 == int(numOfUser):
            raise Exception("Oyuncu sayisi giriniz.")
        elif re.search("\s", numOfUser):
            raise Exception("Bosluk icermemelidir.")
        elif re.search("[a-z]", numOfUser):
            raise Exception("Harf icermemelidir.")
        elif re.search("[A-Z]", numOfUser):
            raise Exception("Harf icermemelidir.")
        elif not re.search("[0-9]", numOfUser):
            raise Exception("Rakam icermelidir.")
        elif re.search("[_@$]", numOfUser):
            raise Exception("_@$ karakter icermemelidir.")
        else:
            Methods._Methods.timer(seconds=0.1)


class _ControlRegister:
    
    def checkName(name):
        if len(name) < 3:
            raise Exception("Ad-Soyad girmelisiniz.")
        elif re.search("[0-9]", name):
            raise Exception("Rakam icermemelidir.")
        elif re.search("[_@$]", name):
            raise Exception("_@$ karakter icermemelidir.")
        elif not re.search("\s", name):
            raise Exception("Ad-Soyad arasinda bosluk icermelidir.")
        else:
            Methods._Methods.timer(seconds=1, writer="Ad-Soyad kaydedildi...")      

    def checkNickname(nick):
        if len(nick) < 4:
            raise Exception("Nickname en az 4 karakter olmalidir.")
        elif re.search("\s", nick):
            raise Exception("Nickname bosluk icermemelidir.")
        elif not re.search("[a-z]", nick) or re.search("[A-Z]", nick):
            raise Exception("Nickname harf icermelidir.")
        else:
            Methods._Methods.timer(seconds=1, writer="Nickname onaylandi...")

    def checkPassword(psw):
        if len(psw) < 8:
            raise Exception("Sifreniz en az 8 karakter olmalidir.")
        elif not re.search("[a-z]", psw):
            raise Exception("Parola kucuk harf icermelidir.")
        elif not re.search("[A-Z]", psw):
            raise Exception("Parola buyuk harf icermelidir.")
        elif not re.search("[0-9]", psw):
            raise Exception("Parola rakam icermelidir.")
        elif not re.search("[_@$]", psw):
            raise Exception("Parola _@$ karakter icermelidir.")
        elif re.search("\s", psw):
            raise Exception("Parola bosluk icermemelidir.")
        else:
            Methods._Methods.timer(seconds=0.5)       
    
    def checkConfirmPassword(cpsw, psw):
        if psw != cpsw:
            raise Exception("Password ile ayni giriniz.")
        else:
            Methods._Methods.timer(seconds=1, writer="Password onaylandi...")      
    
    def checkBirthday(birth):
        Order = [birth[0], birth[1], birth[3], birth[4], birth[6], birth[7], birth[8], birth[9]]
        for x in Order:
            if not re.search("[0-9]", x):
                raise Exception("Dogum Tarihini ornekteki gibi giriniz.")
            else:
                continue
        if len(birth) != 10:
            raise Exception("Dogum Tarihini dogru giriniz.")
        elif re.search("[a-z]", birth):
            raise Exception("Dogum Tarihi harf icermemelidir.")
        elif re.search("[A-Z]", birth):
            raise Exception("Dogum Tarihi harf icermemelidir.")
        elif not re.search("[0-9]", birth):
            raise Exception("Dogum Tarihi rakam icermelidir.")
        elif not re.search(".", birth):
            raise Exception("Dogum Tarihi nokta karakteri icermelidir.")
        elif re.search("[_@$]", birth):
            raise Exception("Dogum Tarihi _@$ karakter icermemelidir.")
        else:
            Methods._Methods.timer(seconds=1, writer='Dogum Tarihi onaylandi...')      
    
    def checkGender(gender):
        Gender = ["Erkek", "Kadin", "Diger"]
        if gender not in Gender:
            raise Exception("Cinsiyeti dogru giriniz.")
        elif re.search("[_@$]", gender):
            raise Exception("_@$ karakter icermemelidir.")
        elif re.search("[0-9]", gender):
            raise Exception("Rakam icermemelidir.")
        elif re.search("\s", gender):
            raise Exception("Bosluk icermemelidir.")
        else:
            Methods._Methods.timer(seconds=1, writer="Cinsiyet kaydedildi...")        

    def checkId(id):
        userFile = open("UserFile.txt", "r", encoding="utf-8")
        while f"Id: {id}" in userFile.read():
            raise Exception("Id daha once tanimlanmis")
            id += 1
        else:
            userFile.close()
            Methods._Methods.timer(seconds=1, writer="Id olusturuldu...")


class _ControlLogin:
    
    def checkLogin(nick, psw):
        userFile = open("UserFile.txt", "r", encoding="utf-8")
        if f"Nickname: {nick}\n" not in userFile.read():
            raise Exception("Nickname bulunamadi.")
        userFile.seek(0)
        if f"Nickname: {nick}\n     Password: {psw}\n" not in userFile.read():
            raise Exception("Nickname/Password uyusmazligi.")
        else:
            userFile.close()
            Methods._Methods.timer(seconds=1)


class _ControlUpdate:
    pass


class _ControlGame:

    def checkGuessNum(guessNum):
        if not 0 < guessNum < 100:
            raise Exception("Sayi araliginiz [1-99] olmalidir.")
        elif re.search("\s", guessNum):
            raise Exception("Bosluk olamamalidir.")
        else:
            Methods._Methods.timer(seconds=0.1)