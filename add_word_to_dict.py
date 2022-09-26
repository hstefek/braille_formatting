import csv
import AlgoritamSyllCro.slog2 as rastavi

def import_new_word(wordDict, syllableDict):
    while True:
        try:
            x = input("Unesi riječ: ")
            nova, korekcija = 0, 0
            if x in wordDict:
                print("Riječ \"" + x +"\" se nalazi u rječniku.\nRastav na slogove: " + wordDict[x][0] + "\n")
            else:
                rastav = list(*map(rastavi.rastavinaslogove, x.split()))
                #wordDict[x] = ['-'.join(map(str, rastav)), '1', '0']
                print("Riječ \"" + x +"\" nije u rječniku.\nRastav na slogove: " + '-'.join(map(str, rastav)) + "\n")
                nova = 1

            z = input("Želiš li urediti rastav? y/n ")
            if z=="y":
                z = input("Unesi rastav na slogove odvojen crticom: ")
                rastav = z.split('-')
                print("Rastav na slogove: " + '-'.join(map(str, rastav)) + "\n")
                korekcija = 1

            if nova == 1 or korekcija == 1:
                y = input("Želiš li dodati riječ u rječnik? y/n ")
                if y == "y":
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
        except Exception:
            print("Unesi samo jednu riječ.\n")
    return (wordDict, syllableDict)