import sys, glob, os
from WordCounter import Counter as wc

#
# Variables
#
stop_words,target_dir, file_paths = [],sys.argv[1],[]

# Check to make sure our target directory exists, else throw an error message and exit
try:
    assert os.path.isdir(target_dir)
except:
    print("Invalid Target Directory")
    exit(1)

# Load stop words into memory
# load raw stop words as utf-8
f = open('stopwords.txt','r',encoding='utf-8')
for word in f.read().strip().split('\n'):
    if word not in ['', ' ','\n']:
        stop_words.append(str(word).lower())


# get .txt paths for target directory
for filename in glob.iglob(os.path.join(target_dir,'**/*.txt'), recursive=True):
    file_paths.append(filename)

# Run the word count


WordCountEtl = wc(file_paths,swords=stop_words)

WordCountEtl.etlroutine()

WordCountEtl.writeoutputfiles()









