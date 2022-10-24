import time

def stats(wordDict, syllableDict):
    while True:
        #x = input("1 - Broj riječi u bazi\n2 - Učestalost sloga\n3 - Nazad\n")
        print("----------------------\n")
        x = input("1 - Broj riječi u bazi\n2 - Broj slogova u bazi\n3 - Učestalost sloga\n\t1 - Učestalost određenog sloga\n\t2 - Rang lista slogova\n4 - Ispis novih rastava\n5 - Ispis korigiranih slogova\n6 - Nazad\n")
        if x == "1":
            print("Broj riječi u bazi: " + str(len(wordDict)))
        elif x == "2":
            print("Broj slogova u bazi: " + str(len(syllableDict)))
        elif x == "3":
            while True:
                #y = input("1 - Učestalost određenog sloga\n2 - Broj slogova u bazi\n3 - Rang lista slogova\n3 - Nazad\n")
                print("----------------------\n")
                y = input("1 - Učestalost određenog sloga\n2 - Rang lista slogova\n3 - Nazad\n")
                if y == "1": #ucestalost odredenog sloga
                    i = input("Unesi slog: ")
                    if i in syllableDict:
                        print(syllableDict[i])
                    else:
                        print("Slog nije u bazi.\n")
                    break
                elif y == "2": #rang lista slogova
                    t = time.strftime('%Y%m%d%H%M', time.localtime())
                    rang_lista = open('data/rang_lista_slogova_' + t + '.txt', 'w', encoding='utf8')
                    for k, v in sorted(syllableDict.items(), key=lambda p: p[1], reverse=True):
                        #print(k, v)
                        rang_lista.write(k + ' - ' + v + '\n')
                    rang_lista.close()
                    print('Rang lista slogova spremljena u rang_lista_' + t + '.txt')
                    break
                elif y == "3":
                    break
                else:
                    print("Nepoznata naredba.")
        elif x == "4": #ispis novih rastava
            t = time.strftime('%Y%m%d%H%M', time.localtime())
            nove_rijeci = open('data/nove_rijeci_' + t + '.txt', 'w',encoding='utf8')
            #print("Nove riječi:\n")
            for k,v in wordDict.items():
                if v[1] == '1':
                    #print (k, v[0])
                    nove_rijeci.write(k + ',' + v[0] + '\n')
            nove_rijeci.close()
            print('Nove riječi spremljene u nove_rijeci_' + t + '.txt')
        elif x == "5": #ispis korigiranih rastava
            t = time.strftime('%Y%m%d%H%M', time.localtime())
            korigirani_rastavi = open('data/korigirani_rastavi_' + t + '.txt', 'w', encoding='utf8')
            #print("Korigirane riječi:\n")
            for k, v in wordDict.items():
                if v[2] == '1':
                    #print(k, v[0])
                    korigirani_rastavi.write(k + ',' + v[0] + '\n')
            korigirani_rastavi.close()
            print('Korigirani rastavi spremljeni u korigirani_rastavi_' + t + '.txt')
        elif x == "6":
            break
        else:
            print("Nepoznata naredba.")