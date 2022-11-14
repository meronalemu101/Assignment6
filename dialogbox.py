rom psychopy import gui, core, visual, #monitors, event
from datetime import datetime
import os
import numpy as np

#setup the dictionary for the gui
exp_info = {    'subject_nr':0, 
                'age':0, 
                'handedness':('right','left','ambi'), 
                'gender':('male','female','other','prefer not to say'), 
                'session': 1}


print(exp_info)

print("All variables have been created! Now ready to show the dialog box!")

my_dlg = gui.DlgFromDict(dictionary=exp_info, 
                        title="subject info",
                        fixed=['session'],
                        order=['session', 'subject_nr', 'age', 'gender', 'handedness'])

date = datetime.now() #what time is it right now?
exp_info['date'] =  str(date.hour) + '-' + str(date.day) + '-' + str(date.month) + '-' + str(date.year)
print(exp_info['date'])

filename = str(exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv'

main_dir = os.getcwd()
sub_dir = os.path.join(main_dir, 'sub_info', filename)

#2) Creating a fixed session sets the vales to be displayed in non-editable fields.
