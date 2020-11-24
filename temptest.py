import unicodedata
 
def strip_accents(text):
 
    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass
 
    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")
 
    return str(text)
 
s = strip_accents('àéêöhello')

with open('val1.csv','r',encoding='utf-8') as train:
    with open('val.csv','w',encoding='utf-8') as train1:
        for line in train.readlines():
            line = strip_accents(line)
            train1.write(line)

print(s)