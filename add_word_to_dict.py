import csv
import AlgoritamSyllCro.slog2 as rastavi

def adapt_letters(string):
    u = 'ü'.encode()
    U = 'Ü'.encode()
    a = 'ä'.encode()
    A = 'Ä'.encode()
    o = 'ö'.encode()
    O = 'Ö'.encode()
    ss = 'ß'.encode()
    aa = 'å'.encode()
    AA = 'Å'.encode()
    aaa = 'â'.encode()
    AAA = 'Â'.encode()
    aaaa = 'ã'.encode()
    AAAA = 'Ã'.encode()
    aaaaa = 'á'.encode()
    AAAAA = 'Á'.encode()
    n = 'ñ'.encode()
    N = 'Ñ'.encode()
    i = 'í'.encode()
    ii = 'ī'.encode()
    iii = 'ì'.encode()
    e = 'ë'.encode()
    E = 'Ë'.encode()
    ee = 'é'.encode()
    EE = 'É'.encode()
    eee = 'è'.encode()
    oo = 'ø'.encode()
    ooo = 'ô'.encode()
    oooo = 'ó'.encode()
    OOOO = 'Ó'.encode()
    ooooo = 'ő'.encode()
    OOOOO = 'Ő'.encode()
    c = 'ç'.encode()


    string = string.encode()
    string = string.replace(u, b'u')
    string = string.replace(U, b'U')
    string = string.replace(a, b'a')
    string = string.replace(A, b'A')
    string = string.replace(o, b'o')
    string = string.replace(O, b'O')
    string = string.replace(ss, b'ss')
    string = string.replace(aa, b'a')
    string = string.replace(AA, b'A')
    string = string.replace(i, b'i')
    string = string.replace(ii, b'i')
    string = string.replace(iii, b'i')
    string = string.replace(aaa, b'a')
    string = string.replace(AAA, b'A')
    string = string.replace(aaaa, b'a')
    string = string.replace(AAAA, b'A')
    string = string.replace(aaaaa, b'a')
    string = string.replace(AAAAA, b'A')
    string = string.replace(n, b'n')
    string = string.replace(N, b'N')
    string = string.replace(ee, b'e')
    string = string.replace(eee, b'e')
    string = string.replace(EE, b'E')
    string = string.replace(oo, b'o')
    string = string.replace(e, b'a')
    string = string.replace(E, b'A')
    string = string.replace(ooo, b'o')
    string = string.replace(oooo, b'o')
    string = string.replace(OOOO, b'O')
    string = string.replace(ooooo, b'o')
    string = string.replace(OOOOO, b'O')
    string = string.replace(c, b'c')

    string = string.decode('utf-8')
    return (string)

def veliko_malo_slovo(x, y):
    j = 0
    list_y = list(y)
    for i in x:
        if i.isalpha() == True:
            if list_y[j] == '-':
                j += 1
            if i == 'ß':
                del list_y[j]
            if i != list_y[j]:
                list_y[j] = i
            j += 1
    return ("".join(list_y))

def import_new_word(wordDict, syllableDict):
    while True:
        try:
            x = input("Unesi riječ: ")
            nova, korekcija = 0, 0
            if x in wordDict:
                print("Riječ \"" + x +"\" se nalazi u rječniku.\nRastav na slogove: " + wordDict[x][0] + "\n")
            else:
                temp_x = adapt_letters(x)
                rastav = list(*map(rastavi.rastavinaslogove, temp_x.split()))
                #wordDict[x] = ['-'.join(map(str, rastav)), '1', '0']
                temp = veliko_malo_slovo(x, '-'.join(map(str, rastav)))
                print("Riječ \"" + x +"\" nije u rječniku.\nRastav na slogove: " + temp + "\n")
                nova = 1

            z = input("Želiš li urediti rastav? d/n ")
            if z=="d":
                z = input("Unesi rastav na slogove odvojen crticom: ")
                rastav = z.split('-')
                print("Rastav na slogove: " + '-'.join(map(str, rastav)) + "\n")
                korekcija = 1

            if nova == 1 or korekcija == 1:
                y = input("Želiš li dodati riječ u rječnik? d/n ")
                if y == "d":
                    wordDict[x] = ['-'.join(map(str, rastav)), str(nova), str(korekcija)]
                    for syllable in list(rastav):
                        if syllable not in syllableDict.keys():
                            syllableDict[syllable] = 1
                        else:
                            syllableDict[syllable] += 1

                    with open("HR_dictionary.csv", 'w', newline='', encoding='utf8') as file:
                        writer = csv.writer(file)
                        for word in wordDict:
                            writer.writerow([word, str(wordDict[word][0]), str(wordDict[word][1]), str(wordDict[word][2])])
                        print("Riječ \""+ x +"\" dodana u rječnik.")
                    with open("HR_syllable_frequency.csv", 'w', newline='', encoding='utf8') as file2:
                        writer2 = csv.writer(file2)
                        for syllable in syllableDict:
                            writer2.writerow([syllable, syllableDict[syllable]])
                        print("Slogovi riječi \""+ x +"\" ubrojani u učestalost slogova.")
                break
        except KeyboardInterrupt:
            print("\n\n")
            break
        except Exception as e:
            print(e)
            print("Unesi samo jednu riječ.\n")
    return (wordDict, syllableDict)