mon = monitors.Monitor('myMonitor', width=31.4, distance=60) 
mon.setSizePix([1280,800])
mon.save()
thisSize = mon.getSizePix()
thisWidth = thisSize[0]
thisHeight = thisSize[1]


win = visual.Window(monitor=mon, size= (400,400), color = [-1,-1,-1], fullscr=True)

#1) Changing the units for pixel size changes what is used as units for stimuli of window and its percentage of screen.
#2) Changing color space changes what method is used to define and code color. Colors can be coded by name web/X11 ColorSpace.
