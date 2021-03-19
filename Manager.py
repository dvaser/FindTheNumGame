
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
                    userGuestName = str(input(f"\n{x+1}.Kullanıcının Adı-Soyadi: ")).title().rstrip(' ')
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
                    Methods._Methods.timer(seconds=3)
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
            print(f"{Guest[x]['Name']}, canın: {Guest[x]['Heart']}\n")
        print(("-"*50))
        Methods._Methods.timer(seconds=5, writer='Sayi olusturuluyor, bekleyiniz...')

        winnerBool = False
        Eliminated = []
        eliminatedGuestIndex = []
        number = random.randint(1,100)
        remainingHeart = 5
        guessNum = 0
        Gamer = int(Methods.numberOfUser)
        for Hearts in range(remainingHeart):
            for gamer in range(Gamer): 

                def message(direction='', point=0):
                    print("\n"+("<^>"*30))
                    Guest[gamer]['Heart'] = Guest[gamer]['Heart']-1
                    print(f"\n  {Guest[gamer]['Name']}, kalan canın: {Guest[gamer]['Heart']}")
                    Guest[gamer]['Score'] = Guest[gamer]['Score']-point
                    if 0 > Guest[gamer]['Score']:
                        print(f"\n  Puanın: {Guest[gamer]['Score']+point} iken {0} oldu.")
                        Guest[gamer]['Score'] = 0
                    else:
                        print(f"\n  Puanın: {Guest[gamer]['Score']+point} iken {Guest[gamer]['Score']} oldu.")
                    print(f"\n          >> Puandaki azalma: -{point}")
                    print(f"\n          >> Aradigin sayının {direction}sindasin.\n")
                    Methods._Methods.timer(seconds=7)
                
                isBool = True
                while isBool:    
                    try:
                        print("\n"+("<^>"*30))
                        guessNum = int(input(f"\n{Guest[gamer]['Name']}, sence sayı kaçtır? : "))
                        ControlManager._ControlGame.checkGuessNum(guessNum=guessNum)
                    except Exception as ex:
                        print(f"\nHatali deger girdiniz...\nError: {ex}")
                    
                    else:
                        isBool = False
                        gap1 = [number-5, number+5]
                        gap2 = [number-10, number+10]
                        gap3 = [number-20, number+20]
                        gap4 = [number-35, number+35]
                        gap5 = [number-50, number+50]
                        gap6 = [number-99, number+99]
                        
                        if guessNum == number:
                            winner = Guest[gamer]['Name']
                            Guest[gamer]['Heart'] = Guest[gamer]['Heart']-1
                            winnerBool = True
                        
                        elif guessNum in range(gap6[0], gap6[1]):
                            if guessNum in range(gap5[0], gap5[1]):
                                if guessNum in range(gap4[0], gap4[1]):
                                    if guessNum in range(gap3[0], gap3[1]):
                                        if guessNum in range(gap2[0], gap2[1]):
                                            if guessNum in range(gap1[0], gap1[1]):
                                                if gap1[0] <= guessNum < number:
                                                    message(direction='aşağı', point=1)
                                                elif number < guessNum <= gap1[1]:
                                                    message(direction='yukarı', point=1)
                                            else:
                                                if gap2[0] <= guessNum < gap1[0]:
                                                    message(direction='aşağı', point=2)
                                                elif gap1[1] < guessNum <= gap2[1]:
                                                    message(direction='yukarı', point=2)
                                        else:
                                            if gap3[0] <= guessNum < gap2[0]:
                                                message(direction='aşağı', point=4)
                                            elif gap2[1] < guessNum <= gap3[1]:
                                                message(direction='yukarı', point=4)
                                    else:
                                        if gap4[0] <= guessNum < gap3[0]:
                                            message(direction='aşağı', point=7)
                                        elif gap3[1] < guessNum <= gap4[1]:
                                            message(direction='yukarı', point=7)
                                else:
                                    if gap5[0] <= guessNum < gap4[0]:
                                        message(direction='aşağı', point=10)
                                    elif gap4[1] < guessNum <= gap5[1]:
                                        message(direction='yukarı', point=10)
                            else:
                                if gap6[0] <= guessNum < gap5[0]:
                                    message(direction='aşağı', point=20)
                                elif gap5[1] < guessNum <= gap6[1]:
                                    message(direction='yukarı', point=20)
                
                if (0 == Guest[gamer]['Heart']) or (0 == Guest[gamer]['Score']) or (winnerBool == True):
                    Gamer -= 1
                    if winnerBool == True:
                        for x in range(len(Guest)):
                            Eliminated.append(Guest[x])
                            Guest.pop(x)
                        print("\n"+("<^>"*30))
                        winnerMassage = f"  {winner}, oyunu kazandın."
                        print(f"\n{winnerMassage}\n")
                        Methods._Methods.cupMassage(massage=winnerMassage)
                        for x in range(int(Methods.numberOfUser)):
                            print(f"\n\n{Eliminated[x]['Name']}\nKalan canın: {Eliminated[x]['Heart']}\nPuanın: {Eliminated[x]['Score']}")
                        Methods._Methods.timer(seconds=10, writer='\nGuzel oyundu... Menuye yonlendiriliyorsunuz...')
                        Methods._Main.menu()
                    elif 0 == Gamer:
                        Methods._Methods.timer(seconds=10)
                        Methods._Methods.ScreenWriter(seconds=5, writer="Bu oyunu kimse kazanamadı. Menuye yonlendiriliyorsunuz...")
                        Methods._Main.menu()
                    else:
                        Eliminated.append(Guest[gamer])
                        eliminatedGuestIndex.append(gamer)          #! Hep ilk kaydolan eleniyor... Range disina cikma sorunu aliyoz
                                                                    #*     Eliminated.append(Guest[x])
                                                                    #* IndexError: list index out of range
            
            def eliminatedGuest():
                for x in range(len(eliminatedGuestIndex)):
                    print(f"\n\n{Guest[x]['Name']} elendi...")
                    Guest.pop(eliminatedGuestIndex[x])
            eliminatedGuest()

    def gameUser():
        pass