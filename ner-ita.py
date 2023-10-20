# a guide to create a python virtual environment (venv) in vscode
# guide: https://code.visualstudio.com/docs/python/python-tutorial

# install spacy and the model
# python3 -m pip install spacy
# python3 -m spacy download it_core_news_sm
# python3 -m spacy download it_core_news_lg

import spacy
from spacy.lang.it.examples import sentences
import pandas as pd
import sys

args = sys.argv[1:]

inputfile = args[0]
column = args[1]
outputfile = args[2]
model = args[3]

# check if model is not either "sm" or "lg"
if model != "sm" and model != "lg":
    model = "sm"

# here you can load different models, e.g., it_core_news_sm or it_core_news_lg
nlp = spacy.load("it_core_news_"+model)


def perform_ner(text):
    doc = nlp(text)

    # extract a list containing all the text properties of each ent in doc.ents
    entities = [(ent.label_ + ":"+ent.text) for ent in doc.ents]

    # convert entities to a set to remove duplicates, convert to a comma separated string
    return ', '.join(set(entities))


# read csv
df = pd.read_csv(inputfile, escapechar='\\')
df[column] = df[column].astype(str)

# perform NER
df['ner'] = df[column].apply(lambda x: perform_ner(x))

# save csv
df.to_csv(outputfile, index=False)
