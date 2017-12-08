import nltk
from nltk.tokenize import word_tokeize
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np
import pandas as pd

lemmatizer = WordNetLemmatizer()

def init_process(fin,fout):
    outfile = open(fout, 'a')
    #read only a a part at a time
    with open(fin, buffering = 200000, encoding = 'latin-1') as f:
        try:
            for line in f:
                line = line.replace('"', '')
                initial_polarity = line.split(',')[0]
                if initial_polarity == 0:
                    initial_polarity = [1,0]
                elif initial_polarity == 4:
                    initial_polarity = [0,1]
                # the last entry of the csv is actually the tweet
                tweet = line.split()[-1]
                outline = str(initial_polarity) + '::' + tweet
                outfile.write(outline)
        except Exception as e:
            prit(str(e))
    outfile.close()



def create_lexicon(fin):
    lexicon =[]
    with open(fin, buffering=100000, encoding='latin-1') as f:
        try:
            counter = 1
            content = ''
            for line in f:
                counter += 1
                # For creation of bag of words we take
                # random samples from every 2500 lines
                if (counter/2500.0).is_integer():
                    tweet = line.split('::')[1]
                    words = word_tokeize(content)
                    words = [lemmatizer.lemmatize(i) for i in words]
                    lexicon = list(set(lexicon + words))
                    print counter , len(lexicon)

        except Exception as e:
            print str(e)

    woth open('lexicon.pickle', 'wb') as f:
    pickle.dump(lexicon, 'f')


def create_test_data_pickle(fin):
    feature_sets = []
    labels = []
    counter = 0

    with open(fin, buffering=200000) as f:
        for line in f:
            try :
                features = list(eval(line.split('::')[0]))
                label = list(eval(line.split('::')[1]))
                feature_sets.append(features)
                labels.append(labels)
                counter += 1

            except:
                pass

        print counter
        feature_sets = np.array(feature_sets)
        labels = np.array(labels)

    with open('feature_set.pickle', 'wb') as f:
        pickle.dump([feature_sets, labels], f)
