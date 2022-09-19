import AlgoritamSyllCro.slog2 as rastavi

def format_text(text_file, length):

    formatted_text = open('formatted_text_file.txt', 'w')

    def ispisi_sto_je_ostalo(counter):
        formatted_text.write(word)
        counter += len(word) + 1
        if counter < length:
            formatted_text.write(' ')
        else:
            formatted_text.write('\n')
            counter = 0
        return (counter)

    with open(text_file, 'r') as file:
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

#format_text('lorem.txt', 30)
