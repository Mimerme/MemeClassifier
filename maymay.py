#Meme identifier with sci-kit learn
#EggsDee plz halp
#Maybe I'll do it in OpenCV who knows :shrugface:
#I actually hate /r/AdviceAnimals
#I'll stop wrtting comments and actual work
#LETS DO THIS WITHOUT A TUTORIAL

from sklearn import tree
import numpy as np
from PIL import Image
import os
import pickle

__TRAINING__ = True
__TESTING__ = False

memes = [
    "badluckbrian",
    "whatifitoldyou",
    "confessbear",
    "innocentotter"
]

x = []
lables = []
#Unknown classifer, search up the algorithm later
classifier = tree.DecisionTreeClassifier()

#Don't want to get lost in this mess
def mainBlock():
    if __TRAINING__:
        beginTraining()
    if __TESTING__:
        classifier = loadClassifier()
        beginTesting()

    pass

def beginTraining():
    print "Starting Training..."
    loadTrainingImages()
    print x
    classifier.fit(x, lables)
    endTraining()
    return

def beginTesting():
    print "Starting Testing..."
    classifier = loadClassifier()
    return

def loadTrainingImages():
    meme_path = ""
    #Iterates over every meme in the array
    for meme in memes:
        meme_path = meme + "/"
        #Iterates over every file
        for filename in os.listdir(meme_path):
                #Pretty sure lables without onehotencoding works...
                print("Loading " + meme_path + filename + " into the training set")
                #Features for the images are their pixels on a single channel (geryscale)
                x.append(parseImage(meme_path + filename))
                #Append their lables to their corresponding features
                #The lables are converted into their numerical form
                lables.append(memes.index(meme))
                continue
    return

def loadTestingImages():
    print "TRUE : PREDICT"
    meme_path = ""
    #Iterates over every meme in the array
    for meme in memes:
        meme_path = meme + "_test/"
        #Iterates over every file
        for filename in os.listdir(meme_path):
                #Pretty sure lables without onehotencoding works...
                print("Loading " + meme_path + filename + " into the training set")
                #TODO: Insert print accuracy
                print meme + " : " + memes[classifier.predict(parseImage(meme_path + filename))]
                continue
    return


#Parse the Image as GreyScale (something, something, better with single channel)
def parseImage(image):
    return np.asarray(Image.open(image).convert('L'))
    pass

def saveClassifier(classifier):
    with open('maymay_classifier.pkl', 'wb') as fid:
        pickle.dump(classifier, fid)
    return

def loadClassifier():
    with open('maymay_classifier.pkl', 'rb') as fid:
        return pickle.load(fid)
    return

def endTraining():
    print "Saving new classifier..."
    saveClassifier(classifier)
    return

#Executed when the user wises to know a certain iamge
def predictImage(filepath):
    classfier = loadClassifier()
    print memes[classfier.predict(parseImage(filepath))]
    pass

mainBlock()
