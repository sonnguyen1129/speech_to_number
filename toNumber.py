import os
import pickle as cPickle
import numpy as np
from scipy.io.wavfile import read
from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")
import time
import CreateRecord

#path to training data
source   = "test/"   
modelpath = "gmm_models/"
test_file = "test.txt"
file_paths = open(test_file,'r')

gmm_files = [os.path.join(modelpath,fname) for fname in os.listdir(modelpath) if fname.endswith('.gmm')]

models = []
for i in range(len(gmm_files)):
    file = open(gmm_files[i], 'rb')
    models.insert(i, cPickle.load(file))

speakers   = [fname.split("/")[-1].split(".gmm")[0] for fname in gmm_files]
#Out file here
file_out =  open("number.txt","w")

# Read the test directory and get the list of test audio files 
print("Start.  ")
last = []
last.append("number received : \n")
while True:
    test = CreateRecord.Record()
    test.createRecord("test.wav")

    path = "test.wav"
    sr,audio = read(path)
    vector   = extract_features(audio,sr)
        
    log_likelihood = np.zeros(len(models)) 
        
    for i in range(len(models)):
        gmm    = models[i] 
        scores = np.array(gmm.score(vector))
        log_likelihood[i] = scores.sum()
        
    winner = np.argmax(log_likelihood)
    
    if speakers[winner] == "dung":
        break
    elif speakers[winner] == "tiep":
        last.append("\n")
    else :
        print(speakers[winner])
        last.append(speakers[winner])

    time.sleep(0)
    
#print("number received : ")
print("-------------------------------------------------")
print(' '.join(map(str, last)))
print("End! Recorded in Number.txt")
file_out.write("".join(last))