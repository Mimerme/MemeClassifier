# MemeClassifier
Classifies Memes. Yeah....

## So what else?
Stuff used includes
- Python2
- Sci-Kit Learn
- Pickle
- NumPy and a bunch of other dependencies

## Hey, that's pretty good. I wanna run in!
Errrrr, kinda hard to run on windows. On Linux/OSX just run download.sh, and it'll download all the training and testing images (Straight from Google Images). On Windows perhaps cygwin, or the Ubuntu Windows Bash Terminal (idk what it's offically called). The memes and their corresponding text files are just the list of urls, and any program/script that can download from the text files will do as well. Note that ```[meme_name]_test.txt``` need to stored in their appropriate ```[meme_name]_test``` directory. This is because when training our classifier the test and training data must be different

Edit the ```__TESTING__``` and ```__TRAINING__``` boolean variables to set whether or not you want to train and/or test. Training saves the classifier as ```maymay_classifier.pkl``` with Pickle. To feed it an image just run ```python maymay.py [meme_image_path]``` Right now it only detects "What if I Told You", "Awkward Seal" (In the code its referenced as Innocent Otter, I'm sorry, ok), "Bad Luck Brian", and "Confession Bear".

## WAOW, WUT 4N 4MAZING PROGRAM. WUTS WR0NG WIT IT?
Well it started ass just a 5 day project for me to do over winter break to learn machine learning (It also helped me leran Python). So there's a lot of useless files as you can see here (if they aren't there I probably got off my lazy ass and removed them), and the following

- Needs more comments and better documentation (probably never happening)
- Horrible algorithm, I'm just guessing and checking (highest test was 40% with the Decision Tree)
- Doesn't utilizes the GPU
- No dependency list ;_;
