#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging, sys, csv
import AlgoritamSyllCro.slog2 as rastavi


# Function for importing dictinary from file
def importDict(filename, braille):
    with open(filename, 'r', encoding='utf8') as data:
        for line in data:
            line = line.strip('\n')
            # print (repr(line))
            (key, uni, value) = line.split(' ')
            if key.isnumeric():
                braille[key] = '⠼' + value
            else:
                braille[key] = value
    return (braille)


def translate2braille(strg):
    strg = strg.lower()

    # Translating letters with two graphemes...
    try:
        strg = strg.replace('dž', braille['dž'])
    except:
        logger.info('Letter \"dž\" not in word.')
    try:
        strg = strg.replace('lj', braille['lj'])
    except:
        logger.info('Letter \"lj\" not in word.')
    try:
        strg = strg.replace('nj', braille['nj'])
    except:
        logger.info('Letter \"nj\" not in word.')

    # Translating letters with one graphemes
    for letter in strg:
        try:
            strg = strg.replace(letter, braille[letter])

        except:
            if letter in braille.values():
                pass
            else:
                if letter not in missing:
                    missing.append(letter)
                    logger.error('Char %s not in dictionary!', letter)

    logger.debug('Word %s translated', letter)
    return (strg)


# Logger
logging.basicConfig(
    # level=logging.INFO,
    filename='err_log.log',
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

logger = logging.getLogger()
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
console_handler.setLevel(logging.WARNING)
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)

logger.debug('Importing dictionary...')
try:
    braille = importDict('braille.csv', braille={' ': ' ', '\n': '\n'})
except:
    logger.exception('Error when importing dictionary!')
    sys.exit()
logger.debug('Imported!')


def reset_dictionary():
    print("Baza se resetira...\n")
    syllableDict = {}
    w = csv.writer(open("HR_dictionary.csv", "w", encoding='utf8'))
    with open('HR_Txt-624.txt', 'r', encoding='utf8') as data:
        for line in data:
            key = line.split(None, 1)[0]

            # KEY is the word, VALUE is the same word translated to braille
            # value = translate2braille(key)
            # braille[key] = value

            # RASTAV is list of syllables taken from KEY
            rastav = list(*map(rastavi.rastavinaslogove, key.split()))
            w.writerow([key, '-'.join(map(str, rastav)), 0, 0])
            # file.write(key + ',' + ','.join(map(str, rastav)) + '\n')

            # add new syllables to the syllables dictionary, if syllable exists increment its frequency
            for syllable in list(rastav):
                if syllable not in syllableDict.keys():
                    syllableDict[syllable] = 1
                    # syllableDict[syllable] = [translate2braille(syllable), 1]
                else:
                    syllableDict[syllable] += 1

            # write everything to the file ex. "aachenski - a, a, chen, ski - ⠁⠁⠉⠓⠑⠝⠎⠅⠊"
            # file.write(key + ' - ' + ' '.join(map(str, rastav)) + ' - ' + value + '\n')
    # file.close()

    # print syllables dictionary to file
    freq = csv.writer(open("HR_syllable_frequency.csv", "w", encoding='utf8'))
    for syllable in sorted(syllableDict.keys()):
        # freq.write(syllable + ' - ' + syllableDict[syllable][0] + ' - ' + str(syllableDict[syllable][1]) + '\n')
        freq.writerow([syllable, syllableDict[syllable]])
