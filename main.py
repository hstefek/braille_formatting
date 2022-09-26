import syllable_dictionary_creator, add_word_to_dict, formatting, stats

def select1(wordDict, syllableDict):
    try:
        while True:
            x = input("Unesi ime tekstualne datoteke: \n")
            y = input("Unesi broj znakova u retku (obično 30 ili 38): \n")
            if y == '30' or y == '38':
                try:
                    formatting.format_text(str(x), int(y))
                    break
                except:
                    print("Nepostojeća datoteka.\n")
            else:
                print("Krivi format.\n")
    except KeyboardInterrupt:
        print("\n\n")
        pass
    main(wordDict, syllableDict)

def select2(wordDict, syllableDict):
    wordDict, syllableDict = add_word_to_dict.import_new_word(wordDict, syllableDict)
    main(wordDict, syllableDict)

def select3(wordDict, syllableDict):
    stats.stats(wordDict, syllableDict)
    main(wordDict, syllableDict)

def select4(wordDict, syllableDict):
    x = input("Potvrdi resetiranje baze? y/n ")
    if x == 'y':
        syllable_dictionary_creator.reset_dictionary()
        wordDict, syllableDict = ucitaj_bazu()
        print("Baza podataka resetirana!\n")
    main(wordDict, syllableDict)

def main(wordDict, syllableDict):
    while True:
        print("----------------------\n")
        select = input("1 - Formatiraj tekst\n2 - Provjeri riječ\n3 - Statistika\n\t1 - Broj riječi u bazi\n\t2 - Broj slogova u bazi\n\t3 - Učestalost sloga\n\t\t1 - Učestalost određenog sloga\n\t\t2 - Rang lista slogova\n\t\t3 - Detaljna statistika određenog sloga\n\t4 - Ispis novih rastava\n\t5 - Ispis korigiranih slogova\n4 - Resetiraj bazu podataka\n5 - Zatvori\n")
        if select == "1":
            select1(wordDict, syllableDict)
        elif select == "2":
            select2(wordDict, syllableDict)
        elif select == "3":
            select3(wordDict, syllableDict)
        elif select == "4":
            select4(wordDict, syllableDict)
        elif select == "5":
            print("Bye bye!!\n")
            exit(0)
        else:
            print("Nepoznata naredba.")

def ucitaj_bazu():
    wordDict = {}
    with open("HR_dictionary.csv", encoding='utf8') as reader:
        for line in reader:
            temp = line.split(",")
            wordDict[temp[0]] = [temp[1], temp[2], temp[3].split('\n')[0]]
    syllableDict = {}
    with open("HR_syllable_frequency.csv", 'r', encoding='utf8') as writter:
        for line in writter:
            temp = line.split(",")
            syllableDict[temp[0]] = int(temp[1])
    return (wordDict, syllableDict)

print("\nAdaptacija resursa! v1.1\nSvaka ulazna datoteka mora biti kodirana UTF-8 formatom.\nIzlazne datoteke kodirane su istim formatom.\n")
wordDict, syllableDict = ucitaj_bazu()
main(wordDict, syllableDict)