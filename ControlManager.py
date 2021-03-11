
import os, Methods, re

class _ControlRegister:
    
    def checkName(name):
        if len(name) < 3:
            raise Exception("Ad-Soyad girmelisiniz.")
        elif TypeError:
            raise Exception("Lutfen metin ifadesi giriniz.")
        else:
            Methods._Methods.timer(seconds=1)       #? 1 seconds waiting...

    def checkNickname(nick):
        if len(nick) < 4:
            raise Exception("Nickname en az 4 karakter olmalidir.")
        else:
            Methods._Methods.timer(seconds=1)

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
            Methods._Methods.timer(seconds=1)       #? 1 seconds waiting...
    
    def checkConfirmPassword(cpsw, psw):
        if psw != cpsw:
            raise Exception("Password ile ayni giriniz.")
        else:
            Methods._Methods.timer(seconds=2, writer="Password onaylandi...")      #? 2 seconds waiting and writing...
    
    def checkBirthday(birth):
        if len(birth) != 8:
            raise Exception("Dogum Tarihini dogru giriniz.")
        elif re.search("[a-z]", birth):
            raise Exception("Dogum Tarihi harf icermemelidir.")
        elif re.search("[A-Z]", birth):
            raise Exception("Dogum Tarihi harf icermemelidir.")
        elif not re.search("[0-9]", birth):
            raise Exception("Dogum Tarihi rakam icermelidir.")
        elif not re.search(".", birth):
            raise Exception("Dogum Tarihi nokta karakteri icermelidir.")
        elif TypeError:
            raise Exception("Lutfen dogru sekilde giriniz.")
        else:
            Methods._Methods.timer(seconds=2, writer='Dogum Tarihi onaylandi...')      #? 2 seconds waiting and writing...
    
    def checkGender(gender):
        if gender != "Erkek" or "Kadin":
            raise Exception("Cinsiyeti dogru giriniz.")
        else:
            Methods._Methods.timer(seconds=2, writer="Onaylandi...")        #? 2 seconds waiting and writing...


class _ControlLogin:
    pass


class _ControlUpdate:
    pass


