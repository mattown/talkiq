import sys, glob, os, re
#
# Variables
#
stop_words, unique_words, target_dir, file_paths = [], {}, sys.argv[0],[]
target_dir ='test_data'
# Load stop words into memory
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
