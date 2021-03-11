
import ControlManager, Methods

class _SaveOnFile:
    
    def saveUser():
        userFile = open("UserFile.txt", "a", encoding="utf-8")
        userFile.write()  #! Yazilacak seyi ekle
        userFile.close()


class _Register:
    
    def userRegister():
        _Register.nameRegister()
        _Register.nicknameRegister()
        _Register.passwordRegister()
        _Register.confirmPasswordRegister()
        _Register.birthdayRegister()
        _Register.genderRegister()
    
    def nameRegister():
        isBool = True
        while isBool:
            try:
                userName = str(input('\nAd-Soyad: ')).title()
                ControlManager._ControlRegister.checkName(name=userName)
            except Exception as ex:
                print(f"\nHatali deger girdiniz...\nError: {ex}")
            else:
                isBool = False
            finally:
                print("\n"+"-"*50)

    def nicknameRegister():
        isBool = True
        while isBool:
            try:
                userNickname = input('\nNickname: ')
                ControlManager._ControlRegister.checkNickname(nick=userNickname)
            except Exception as ex:
                print(f"\nHatali deger girdiniz...\nError: {ex}")
            else:
                isBool = False
            finally:
                print("\n"+"-"*50)

    def passwordRegister():
        global userPassword
        isBool = True
        while isBool:
            try:
                userPassword = input('\nPassword: ')
                ControlManager._ControlRegister.checkPassword(psw=userPassword)
            except Exception as ex:
                print(f"\nHatali deger girdiniz...\nError: {ex}")
            else:
                isBool = False
            finally:
                print("\n"+"-"*50)

    def confirmPasswordRegister():
        isBool = True
        while isBool:
            try:
                print("\nPassword: "+"*"*len(userPassword))
                userConfirmPassword = input('\nPassword (Tekrar): ')
                ControlManager._ControlRegister.checkConfirmPassword(cpsw=userConfirmPassword, psw=userPassword)
            except Exception as ex:
                print(f"\nHatali deger girdiniz...\nError: {ex}")
            else:
                isBool = False
            finally:
                print("\n"+"-"*50)

    def birthdayRegister():
        isBool = True
        while isBool:
            try:
                userBirthday = str(input('\nDogum Tarihi (gg.aa.yy): '))
                ControlManager._ControlRegister.checkBirthday(birth=userBirthday)
            except Exception as ex:
                print(f"\nHatali deger girdiniz...\nError: {ex}")
            else:
                isBool = False
            finally:
                print("\n"+"-"*50)
        
    def genderRegister():
        isBool = True
        while isBool:
            try:
                userGender = str(input('\nCinsiyet: ')).title()
                ControlManager._ControlRegister.checkGender(gender=userGender)
            except Exception as ex:
                print(f"\nHatali deger girdiniz...\nError: {ex}")
            else:
                isBool = False
            finally:
                print("\n"+"-"*50)


class _Login:
    
    def nicknameLog():
        pass

    def passwordLog():
        pass


class _Update:
    pass