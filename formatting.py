import AlgoritamSyllCro.slog2 as rastavi
import time, os

def format_text(text_file, length):

    t = time.strftime('%Y%m%d%H%M', time.localtime())
    formatted_text = open('data/' + os.path.splitext(text_file)[0] + '_formatted_' + t + '.txt', 'w', encoding='utf8')

    def ispisi_sto_je_ostalo(counter):
        formatted_text.write(word)
        counter += len(word) + 1
        if counter < length:
            formatted_text.write(' ')
        else:
            formatted_text.write('\n')
            counter = 0
        return (counter)

    with open(text_file, 'r', encoding='utf8') as file:
        for line in file:
            counter = 0
            for word in line.split():
                if len(word) + counter < length:
                    counter = ispisi_sto_je_ostalo(counter)
                else:
                    rastav = list(*map(rastavi.rastavinaslogove, word.split()))
                    word = rastav[0]
                    if len(word) + counter > length - 1:
                        word = ''.join(map(str, rastav))
                        formatted_text.write('\n')
                        counter = 0
                        counter = ispisi_sto_je_ostalo(counter)
                    else:
                        for i in rastav[1:]:
                            if len(word) + len(i) + counter > length - 1:
                                formatted_text.write(word + '-' + '\n')
                                word = ''
                                counter = 0
                            word += i
                        counter = ispisi_sto_je_ostalo(counter)
            formatted_text.write('\n')
    formatted_text.close()
    print("Formatirana datoteka: " + os.path.splitext(text_file)[0] + "_formatted_" + t +".txt\n")

#format_text('lorem.txt', 30)
