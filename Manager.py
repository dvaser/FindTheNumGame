
import ControlManager, Methods, random

Guest = []

class _SaveOnFile():
    
    def saveUser(name, nick, psw, birth, gender, id):
        user = f"\nId: {id}\n     Name: {name}\n     Nickname: {nick}\n     Password: {psw}\n     Birthday: {birth}\n     Gender: {gender}\n"
        userFile = open("UserFile.txt", "a", encoding="utf-8")
        userFile.write(user)
        userFile.close()

    def saveGuest(name, birth, gender, heart, score):
        Guest.append(
            {
                'Name': name, 
                'Birthday': birth, 
                'Gender': gender, 
                'Heart': heart,
                'Score': score
            }
        )


class _Register:
    
    def guestRegister(numberOfUser):
        userGuestHeart = 5
        userGuestScore = 50
        for x in range(int(numberOfUser)):
            isBool = True
            while isBool:
                try:
                    userGuestName = str(input(f"\n{x+1}.Kullanıcının Adı-Soyadi: ")).title()
                    ControlManager._ControlRegister.checkName(name=userGuestName)
                    isBoolien = True
                    while isBoolien:
                        try:
                            userGuestBirthday = input(f"\n{x+1}.Kullanıcının Dogum Tarihi (gg.aa.yyyy): ")
                            ControlManager._ControlRegister.checkBirthday(birth=userGuestBirthday)
                            isbool = True
                            while isbool:
                                try:
                                    userGuestGender = input(f"\n{x+1}.Kullanıcının Cinsiyeti: ").title()
                                    ControlManager._ControlRegister.checkGender(gender=userGuestGender)
                                except Exception as ex:
                                    print(f'\nHatali deger girdiniz...\nError !! {ex}')
                                    Methods._Methods.timer(seconds=2)
                                else:
                                    isbool = False
                        except Exception as ex:
                            print(f'\nHatali deger girdiniz...\nError !! {ex}')
                            Methods._Methods.timer(seconds=2)
                        else:
                            isBoolien = False
                except Exception as ex:
                    print(f'\nHatali deger girdiniz...\nError !! {ex}')
                    Methods._Methods.timer(seconds=2)
                else:
                    _SaveOnFile.saveGuest(name=userGuestName, birth=userGuestBirthday, gender=userGuestGender, heart=userGuestHeart, score=userGuestScore)
                    print("\n"+("-"*50)+f"\n\nTebrikler, {x+1}.kullanıcı girişiniz başarılı.\n\n"+("-"*50))
                    isBool = False

    def userRegister():
        _Register.nameRegister()
        _Register.nicknameRegister()
        _Register.passwordRegister()
        _Register.confirmPasswordRegister()
        _Register.birthdayRegister()
        _Register.genderRegister()
        _Register.idRegister()
        _SaveOnFile.saveUser(name=userName, nick=userNickname, psw=userConfirmPassword, birth=userBirthday, gender=userGender, id=userId)
    
    def nameRegister():
        global userName
        isBool = True
        while isBool:
            try:
                userName = str(input('\nAd-Soyad: ')).title()
                ControlManager._ControlRegister.checkName(name=userName)
            except Exception as ex:
                print(f"\nHatali deger girdiniz...\nError: {ex}")
                Methods._Methods.timer(seconds=2)
            else:
                isBool = False
            finally:
                print("\n"+"-"*50)

    def nicknameRegister():
        global userNickname
        isBool = True
        while isBool:
            try:
                userNickname = input('\nNickname: ')
                ControlManager._ControlRegister.checkNickname(nick=userNickname)
            except Exception as ex:
                print(f"\nHatali deger girdiniz...\nError: {ex}")
                Methods._Methods.timer(seconds=2)
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
                Methods._Methods.timer(seconds=2)
            else:
                isBool = False
            finally:
                print("\n"+"-"*50)

    def confirmPasswordRegister():
        global userConfirmPassword
        isBool = True
        while isBool:
            try:
                print("\nPassword: "+"*"*len(userPassword))
                userConfirmPassword = input('\nPassword (Tekrar): ')
                ControlManager._ControlRegister.checkConfirmPassword(cpsw=userConfirmPassword, psw=userPassword)
            except Exception as ex:
                print(f"\nHatali deger girdiniz...\nError: {ex}")
                Methods._Methods.timer(seconds=2)
            else:
                isBool = False
            finally:
                print("\n"+"-"*50)

    def birthdayRegister():
        global userBirthday
        isBool = True
        while isBool:
            try:
                userBirthday = input('\nDogum Tarihi (gg.aa.yyyy): ')
                ControlManager._ControlRegister.checkBirthday(birth=userBirthday)
            except Exception as ex:
                print(f"\nHatali deger girdiniz...\nError: {ex}")
                Methods._Methods.timer(seconds=2)
            else:
                isBool = False
            finally:
                print("\n"+"-"*50)

    def genderRegister():
        global userGender
        isBool = True
        while isBool:
            try:
                userGender = str(input('\nCinsiyet: ')).title()
                ControlManager._ControlRegister.checkGender(gender=userGender)
            except Exception as ex:
                print(f"\nHatali deger girdiniz...\nError: {ex}")
                Methods._Methods.timer(seconds=2)
            else:
                isBool = False
            finally:
                print("\n"+"-"*50)

    def idRegister():
        global userId
        userId = 1
        isBool = True
        while isBool:
            try:
                ControlManager._ControlRegister.checkId(id=userId)
            except Exception as ex:
                continue
            else:
                isBool = False


class _Login:
    
    def userLogin():
        isBool = True
        while isBool:
            try:
                userLogNickname = input('\nNickname: ')
                userLogPassword = input("\nPassword: ")
                ControlManager._ControlLogin.checkLogin(nick=userLogNickname, psw=userLogPassword)
            except Exception as ex:
                print(f"\nHatali deger girdiniz...\nError: {ex}")
                Methods._Methods.timer(seconds=2)
            else:
                isBool = False
            finally:
                print("\n"+"-"*50)


class _Update:
    pass


class _Game:
    
    def gameGuest():
        print("\n"+("-"*50)+"\n")
        for x in range(int(Methods.numberOfUser)):
            print(f"{Guest[x]['Name']} kalan canın: {Guest[x]['Heart']}\n")
        print(("-"*50))
        
        number = random.randint(1,100)
        remainingHeart = 5
        guessNum = 0
        for hearts in range(remainingHeart):
            for gamer in range(int(Methods.numberOfUser)):
                
                def message(direction='', point=0):
                    print(f"\nAradigin sayının {direction}sindasin.")
                    Guest[gamer]['Heart'] = Guest[gamer]['Heart']-1
                    print(f"\n{Guest[gamer]['Name']} kalan canın: {Guest[gamer]['Heart']}")
                    print(f"\nPuanın: {Guest[gamer]['Score']} iken {Guest[gamer]['Score']-point} oldu.\n")
                    Guest[gamer]['Score'] = Guest[gamer]['Score']-point
                
                isBool = True
                while isBool:    
                    try:
                        guessNum = int(input(f"{Guest[gamer]['userName']}, sence sayı kaçtır? : "))
                        ControlManager._ControlGame.checkGuessNum(guessNum=guessNum)
                    except (TypeError):
                        print(f"\nHatali deger girdiniz...\nError: Sayi degeri girmelisiniz.")
                    except Exception as ex:
                        print(f"\nHatali deger girdiniz...\nError: {ex}")
                    else:
                        isBool = False
                        if guessNum == number:
                            print("\n"+("*"*50)+"\n")
                            Guest[gamer]['Heart'] = Guest[gamer]['Heart']-1
                            print(f"{Guest[gamer]['Name']}, oyunu kazandın.")
                            print("\n"+("*"*50)+"\n")
                            for x in range(Methods.numberOfUser):
                                print(f"{Guest[x]['Name']}\nKalan canın: {Guest[x]['Heart']}\nPuanın: {Guest[x]['Score']}\n")
                            Methods._Methods.timer(seconds=2, writer='Guzel oyundu...')
                            Methods._Main.menu()
                        elif guessNum in range(number-99,number+99):
                            if guessNum in range(number-50,number+50):
                                if guessNum in range(number-35,number+35):
                                    if guessNum in range(number-20,number+20):
                                        if guessNum in range(number-10,number+10):
                                            if guessNum in range(number-5,number+5):
                                                if number-5 <= guessNum < number:
                                                    message(direction='aşağı', point=1)
                                                elif number < guessNum <= number+5:
                                                    message(direction='yukarı', point=1)
                                            else:
                                                if number-10 <= guessNum < number-5:
                                                    message(direction='aşağı', point=2)
                                                elif number+5 < guessNum <= number+10:
                                                    message(direction='yukarı', point=2)
                                        else:
                                            if number-20 <= guessNum < number-10:
                                                message(direction='aşağı', point=4)
                                            elif number+10 < guessNum <= number+20:
                                                message(direction='yukarı', point=4)
                                    else:
                                        if number-35 <= guessNum < number-20:
                                            message(direction='aşağı', point=7)
                                        elif number+20 < guessNum <= number+35:
                                            message(direction='yukarı', point=7)
                                else:
                                    if number-50 <= guessNum < number-35:
                                        message(direction='aşağı', point=10)
                                    elif number+35 < guessNum <= number+50:
                                        message(direction='yukarı', point=10)
                            else:
                                if number-99 <= guessNum < number-50:
                                    message(direction='aşağı', point=20)
                                elif number+50 < guessNum <= number+99:
                                    message(direction='yukarı', point=20)

    def gameUser():
        pass