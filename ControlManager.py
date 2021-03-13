
import os, Methods, re

class _ControlMenu:
    
    def checkMenu(helloMenu):
        if helloMenu not in range(1,5):
            raise Exception("Tuslamayi dogru yapiniz.")
        else:
            Methods._Methods.timer(seconds=1)       #? 1 seconds waiting...

class _ControlRegister:
    
    def checkName(name):
        if len(name) < 3:
            raise Exception("Ad-Soyad girmelisiniz.")
        else:
            Methods._Methods.timer(seconds=1)       #? 1 seconds waiting...

    def checkNickname(nick):
        if len(nick) < 4:
            raise Exception("Nickname en az 4 karakter olmalidir.")
        elif re.search("\s", nick):
            raise Exception("Nickname bosluk icermemelidir.")
        elif not re.search("[a-z]", nick) or re.search("[A-Z]", nick):
            raise Exception("Nickname harf icermelidir.")
        else:
            Methods._Methods.timer(seconds=2, writer="Nickname onaylandi...")

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
        if len(birth) != 10:
            raise Exception("Dogum Tarihini dogru giriniz.")
        elif not re.search("[0-9]", (birth[0] or birth[1] or birth[3] or birth[4] or birth[6] or birth[7] or birth[8] or birth[9])):
            raise Exception("Dogum Tarihini ornekteki gibi giriniz.")
        elif re.search("[a-z]", birth):
            raise Exception("Dogum Tarihi harf icermemelidir.")
        elif re.search("[A-Z]", birth):
            raise Exception("Dogum Tarihi harf icermemelidir.")
        elif not re.search("[0-9]", birth):
            raise Exception("Dogum Tarihi rakam icermelidir.")
        elif not re.search(".", birth):
            raise Exception("Dogum Tarihi nokta karakteri icermelidir.")
        else:
            Methods._Methods.timer(seconds=2, writer='Dogum Tarihi onaylandi...')      #? 2 seconds waiting and writing...
    
    def checkGender(gender):
        if gender != ("Erkek" or "Kadin"):
            raise Exception("Cinsiyeti dogru giriniz.")
        else:
            Methods._Methods.timer(seconds=2, writer="Onaylandi...")        #? 2 seconds waiting and writing...


class _ControlLogin:
    pass


class _ControlUpdate:
    pass


