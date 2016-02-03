import re

class Counter:
    def __init__(self, paths, swords=[]):
        self.unique_words ={}
        self.stop_words = swords
        self.file_paths = paths
        self.trailing_word_counter = set()
        self.f1, self.f2 = open('feature1.txt','w',encoding='utf-8'),open('feature2.txt','w',encoding='utf-8')

    def etlroutine(self):
        for path in self.file_paths:
            self.parsefile(path)
            outputline = '%.1f\n' % float(len(self.trailing_word_counter))
            self.f2.write(outputline)
            self.trailing_word_counter = set()

    def parsefile(self, filepath):
        f = open(filepath,'r',encoding='utf-8')
        for line in f:
            self.parseline(line)

    def parseline(self, line):
        # split on regex, utf-8 whitespace
        words =re.split('\s+', line.strip().lower())
        self.parsewords(words)

    def parsewords(self,words):
        for w in words:
            if len(w) > 0:
                if w not in self.stop_words:
                    self.trailing_word_counter.add(w)
                    if w in self.unique_words.keys():
                        self.unique_words[w] += 1
                    else:
                        self.unique_words[w] = 1
    def writeoutputfiles(self):
        words = list(self.unique_words.keys())
        words.sort()
        for w in words:
            self.f1.write('%s %s\n' % (self.unique_words[w], w)  )
        self.f1.close()
        self.f2.close()



