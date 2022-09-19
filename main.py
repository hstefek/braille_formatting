import syllable_dictionary_creator, add_word_to_dict, formatting, stats

def select1(wordDict, syllableDict):
    while True:
        x = input("Unesi ime tekstualne datoteke: \n")
        y = int(input("Unesi format stranice (30 ili 38): \n"))
        if y == 30 or y == 38:
            try:
                formatting.format_text(str(x), y)
                print("Formatirana datoteka: formatted_text_file.txt\n")
                break
            except:
                print("Nepostojeća datoteka.\n")
        else:
            print("Krivi format.\n")
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
        select = input("1 - Formatiraj tekst\n2 - Provjeri rijec\n3 - Statistika\n4 - Resetiraj bazu podataka\n5 - Zatvori\n")
        if select == "1":
            select1(wordDict, syllableDict)
        elif select == "2":
            select2(wordDict, syllableDict)
        elif select == "3":
            select3(wordDict, syllableDict)
        elif select == "4":
            select4(wordDict, syllableDict)
        elif select == "5":
            exit(0)
        else:
            print("Nepoznata naredba.")

def ucitaj_bazu():
    wordDict = {}
    with open("HR_dictionary.csv") as reader:
        for line in reader:
            temp = line.split(",")
            wordDict[temp[0]] = temp[1].split('\n')[0]
    syllableDict = {}
    with open("HR_syllable_frequency.csv", 'r') as writter:
        for line in writter:
            temp = line.split(",")
            syllableDict[temp[0]] = int(temp[1])
    return (wordDict, syllableDict)

print("Adaptacija resursa! v1.0\n")
wordDict, syllableDict = ucitaj_bazu()
main(wordDict, syllableDict)