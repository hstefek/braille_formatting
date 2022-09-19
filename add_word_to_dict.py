import csv
import AlgoritamSyllCro.slog2 as rastavi

def import_new_word(wordDict, syllableDict):

    x = input("Unesi rijec: ")
    if x in wordDict:
        print("Rijec se nalazi u rjecniku: " + x + "\nRastav na slogove: " + wordDict[x] + "\n")
    else:
        rastav = list(*map(rastavi.rastavinaslogove, x.split()))
        wordDict[x] = '-'.join(map(str, rastav))
        print("Rijec nije u rjecniku: " + x + "\nRastav na slogove: " + wordDict[x] + "\n")
        for syllable in list(rastav):
            if syllable not in syllableDict.keys():
                syllableDict[syllable] = 1
            else:
                syllableDict[syllable] += 1
        y = input("Zelis li dodati rijec u rjecnik? y/n ")
        if y == "y":
            with open("HR_dictionary.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                for word in wordDict:
                    writer.writerow([word, str(wordDict[word])])
                print("Rijec \""+ x +"\" dodana u rjecnik.")
            with open("HR_syllable_frequency.csv", 'w', newline='') as file2:
                writer2 = csv.writer(file2)
                for syllable in syllableDict:
                    writer2.writerow([syllable, syllableDict[syllable]])
                print("Slogovi rijeci \""+ x +"\" ubrojani u cestnost.")
    return (wordDict, syllableDict)