# open a file and read contents
# for each word in file
#   increment (word as key, count as value to dictionary)
# when that is done, print items in dictionary

from sys import argv

script, filename = argv

word_dict = {}

def normalize( filetext ):
    # do stuff to normalize list

    filetext = filetext.replace("--"," ")
    filelist = filetext.split()

    # strip punctuation 

    punctuation = ".?,\"!-;:_()/[]*$#"

    for i in range(len(filelist)):
        filelist[i] = filelist[i].strip(punctuation)
        filelist[i] = filelist[i].lower()

    return filelist

def main():
    open_file = open(filename)
    filetext = open_file.read()

    filelist = normalize( filetext )

    #for each word in filelist, increment value in dictionary where word = key
    for word in filelist:
        word_dict[word] = word_dict.get(word, 0) + 1

    # sort output from highest frequency to lowest frequency (values)
    # sort words with same frequency alphabetically (str.sort())

    new_dict = {}

    # make a new dictionary where the keys are the frequencies of words, and the values are lists of words
    for word, frequency in word_dict.iteritems():
        new_dict.setdefault(frequency, [])
        new_dict[frequency].append(word)

    for wordlist in new_dict.itervalues():
        wordlist.sort()

    sorted_keys = new_dict.keys()

    sorted_keys.sort()


    for key in reversed(sorted_keys):
        for words in new_dict[key]:
           print words, key

main()