
import ControlManager, Methods

class _SaveOnFile:
    
    def saveUser():
        userFile = open("UserFile.txt","a",encoding="utf-8")
        userFile.write()
        userFile.close()

class _Shortcut:
    
    def exceptForTry():
        except Exception as ex:
            print(f"\nHatali deger girdiniz...\nError: {ex}")
        else:
            isBool = False
        finally:
            print("\n"+"-"*50)

class _Register:
    
    def nameRegister():
        isBool = True
        while isBool:
            try:
                userName = str(input('\nAd-Soyad: ')).title()
                ControlManager._ControlRegister.checkName(name=userName)
            _Shortcut.exceptForTry()

    def nicknameRegister():
        isBool = True
        while isBool:
            try:
                userNickname = input('\nNickname: ')
                ControlManager._ControlRegister.checkNickname(nick=userNickname)
            _Shortcut.exceptForTry()

    def passwordRegister():
        isBool = True
        while isBool:
            try:
                userPassword = input('\nPassword: ')
                ControlManager._ControlRegister.checkPassword(psw=userPassword)
            _Shortcut.exceptForTry()

    def confirmPasswordRegister():
        isBool = True
        while isBool:
            try:
                userConfirmPassword = input('\nPassword (Tekrar): ')
                ControlManager._ControlRegister.checkConfirmPassword(cpsw=userConfirmPassword)
            _Shortcut.exceptForTry()

    def ageRegister():
        isBool = True
        while isBool:
            try:
                userAge = int(input('\nYas: '))
                ControlManager._ControlRegister.checkAge(age=userAge)
            _Shortcut.exceptForTry()
        
    def genderRegister():
        isBool = True
        while isBool:
            try:
                userGender = str(input('\nCinsiyet: ')).title()
                ControlManager._ControlRegister.checkGender(gender=userGender)
            _Shortcut.exceptForTry()


class _Login:
    
    def nicknameLog():
        pass

    def passwordLog():
        pass


class _Update:
    pass