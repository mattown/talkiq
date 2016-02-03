import re, statistics

class Counter:
    def __init__(self, paths, swords=[]):
        self.unique_words ={}
        self.unique_word_counts =[]
        self.stop_words = swords
        self.file_paths = paths
        self.trailing_word_counter = set()
        self.f1, self.f2 = open('feature1.txt','w',encoding='utf-8'),open('feature2.txt','w',encoding='utf-8')

    def etlroutine(self):
        for path in self.file_paths:
            self.parsefile(path)
            self.unique_word_counts.append( len(self.trailing_word_counter))
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
        # process feature1.txt
        words = list(self.unique_words.keys())
        words.sort()
        f1output = []
        for w in words:
            f1output.append('%s %s' % (self.unique_words[w], w)  )
        self.f1.write('\n'.join(f1output))

        # process feature2.txt
        f2output = []
        for i in range(len(self.unique_word_counts)):
            median_array = self.unique_word_counts[0:i+1]
            median_array.sort()
            f2output.append('%.1f' % float(statistics.median(median_array)))
        self.f2.write('\n'.join(f2output))
        self.f1.close()
        self.f2.close()



