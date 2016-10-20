from section2_1.classifier import classifier
from section2_1.docclass import getwords


words = getwords('application apple')

cl = classifier(words)
cl.train('the quick brown fox jumps over the lazy dog', 'good')
cl.train('make quick money in the online casino', 'bad')
cl.fcout('quick','good')

cl.fcout('quick','bad')
