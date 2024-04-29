import string

def process_file(filename):
    # open a file and read each line of text
    word_hist = dict()
    fin = open(filename, encoding='utf8')
    for line in fin:
        process_line(line, word_hist)
    return word_hist

def process_line(line, word_hist):
    # break a line of text into words
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        word_hist[word] = word_hist.get(word, 0) + 1

def total_words(word_hist):
    return len(word_hist)

def word_occurences(word_hist):
    return sum(word_hist.values())



def main():
    # this is where the main execution for the program
    word_hist = process_file('pg1513.txt')
    print(f'Total number of words: {total_words(word_hist):,}')
    print(f'Total word occurences: {word_occurences(word_hist):,}')
    #for word in word_hist:
     #   print(word)

if __name__ == '__main__':
    main()