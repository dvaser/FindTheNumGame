
import os, Methods, re

class _ControlRegister:
    
    def checkName(name):
        if len(name) < 3:
            raise Exception("Ad-Soyad girmelisiniz.")
        else:
            Methods._Methods.timer(1)     #! 1 seconds waiting...

    def checkNickname(nick):
        pass

    def checkPassword(psw):
        if len(psw) < 8:
            raise Exception("Sifreniz en az 8 karakter olamlidir.")
        elif not re.search
    
    def checkConfirmPassword(cpsw):
        _ControlRegister.checkPassword(cpsw)
        else:
            Methods._Methods.timer(1)
    
    def checkAge(age):
        pass
    
    def checkGender(gender):
        pass


class _ControlLogin:
    pass


class _ControlUpdate:
    pass


