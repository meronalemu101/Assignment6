from psychopy import gui, core, visual, monitors, event
from datetime import datetime
import os
import numpy as np

##-----
#Simultaneous images
##-----

fix_text = visual.TextStim(win, text='+')
my_image = visual.ImageStim(win, units = 'pix', size=(400,400))
nTrials = 10
image_dir = os.path.join(main_dir,'images')
stims = ['face01.jpg','face02.jpg','face03.jpg','face04.jpg','face05.jpg','face06.jpg','face07.jpg','face08.jpg','face09.jpg','face10.jpg']

horizMult = [-1, 1, 1, -1]
vertMult = [1, 1, -1, -1]
correctResponse = [True, True, True, True]

for trial in range(nTrials):
    my_image.image = os.path.join(image_dir,stims[trial])
    
    my_image.pos = (horizMult[trial] * thisWidth/4, vertMult[trial] * thisHeight/4)
    my_image.draw() #draw
    startTime = win.flip() #show
    key = event.waitKeys() #wait for keypress
    
    print(key)
    if key[0] == 'left':
        if horzMult[trial] == -1:
            correctResponse[trial] = True
        else:
            corectResponse[trial] = False
    if key[0] == 'right':
        if horzMult[trial] == 1:
            correctResponse[trial] = True
        else:
            corectResponse[trial] = False


win.close()

##---------
#Present stimuli
##---------

my_image = visual.ImageStim(win)
os.chdir('C:/PsycoPy')
main_dir = os.getcwd()
image_dir = os.path.join(main_dir,'images')

stims = ['face01.jpg','face02.jpg','face03.jpg','face04.jpg','face05.jpg','face06.jpg','face07.jpg','face08.jpg','face09.jpg','face10.jpg']

nTrials = 3

my_image = visual .ImageStim(win)

np.random.shuffle(stims)

for trial in range(nTrials):
    my_image.image = os.path.join(image_dir,stims[trial])
    my_image.draw() #draw
    win.flip() #show
    event.waitKeys() #wait for keypress

win.close()
