import os

from chop_words import chop
from record import rec
from dictionary import *
from transliteration import getInstance
from AnimatedGif import *

def load_dictionary(path):
    serialized = open(path + '/serialized.txt', 'r')
    is_serial = (serialized.read() == '1')
    serialized.close()
    if is_serial:
        with open(path + '/dictionary.pkl', 'rb') as input:
            dictionary = pickle.load(input)
    else:
        dictionary = Dictionary(path)
        with open(path + '/dictionary.pkl', 'wb') as output:
            pickle.dump(dictionary, output, 0)
        serialized = open(path + '/serialized.txt', 'w')
        serialized.write("1")
        serialized.close()

    return dictionary


# if __name__ == '__main__':
def start(audio_file):
    #
    # if len(sys.argv) < 1:
    #     print "Usage: python main.py [DICTIONARY] [AUDIO-FILE]"
    # else:
        dictionary = load_dictionary("dictionary1")
#        audio_file = "samples/sardi.wav"
#        file = rec(3)
#        audio_file = file

        word_cnt = chop('chopped-words', audio_file)
        if word_cnt < 1 or word_cnt > 1:
            print "Problem in Recognition"
            return ("Problem in Recognition","error")
            # quit()
        else:
            print "querying", word_cnt, "words"

        for i in xrange(word_cnt):
            w = Word('chopped-words/word' + str(i) + '.wav')
            rec_word = dictionary.find_match(w)
            t = getInstance()
            text = unicode(rec_word, "utf-8")
            t_text = t.transliterate_indic_en(text, "hi_IN")
            print t_text[2:]
            print rec_word + ' ',
            sys.stdout.flush()

        pic = t_text[2:]
        path_to_pic = './img' + '/' + pic + '.gif'

        return (text+" ("+t_text+")", path_to_pic)

def callByAudio():
    file = rec(3)
    audio_file = file

    return start(audio_file)

def callByName(word):
    audio_file = "samples/" + word + ".wav"
    if os.path.isfile(audio_file):
        print ("File exist")
    else:
        return ("Word Not Found","error")

    return start(audio_file)