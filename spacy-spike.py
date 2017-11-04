import spacy
nlp = spacy.load('en')
doc = nlp(u'hello this is some text I hope you like reading it')
print([(w.text, w.pos_) for w in doc])
