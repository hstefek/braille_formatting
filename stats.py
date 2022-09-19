def stats(wordDict, syllableDict):
    while True:
        x = input("1 - Broj riječi u bazi\n2 - Čestnost sloga\n3 - Nazad\n")
        if x == "1":
            print("Broj riječi u bazi: " + str(len(wordDict)))
        elif x == "2":
            while True:
                y = input("1 - Čestnost određenog sloga\n2 - Broj slogova u bazi\n3 - Rang lista slogova\n3 - Nazad\n")
                if y == "1":
                    i = input("Unesi slog: ")
                    if i in syllableDict:
                        print(syllableDict[i])
                        break
                    else:
                        print("Slog nije u bazi.\n")
                        break
                elif y == "2":
                    print("Broj slogova u bazi: " + str(len(syllableDict)))
                    break
                elif y == "3":
                    for k, v in sorted(syllableDict.items(), key=lambda p:p[1], reverse=True):
                        print (k, v)
                    break
                elif x == "4":
                    break
                else:
                    print("Nepoznata naredba.")
        elif x == "3":
            break
        else:
            print("Nepoznata naredba.")