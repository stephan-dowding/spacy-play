import spacy

def custom_pipeline(nlp):
    return (nlp.tagger, nlp.parser, nlp.entity)

nlp = spacy.load('en', create_pipeline=custom_pipeline)

doc = nlp(u'hello this is some text I hope you like reading it')
print([(w.text, w.pos_) for w in doc])
print([w.lemma_ for w in doc])
print([w.lemma_ for w in doc if not w.is_stop])
