from tkinter import *

window = Tk() #Create a window
window.wm_title('Database')   # Give the window a name

toolbar = Frame(window)      # create a frame for the toolbar
bottomFrame = Frame(window)  # create another frame for text input
lastFrame = Frame(window)

toolbar.pack(side=TOP,fill=X) #pack the toolbar
bottomFrame.pack(side=TOP, fill=X,pady=20) #pack the bottom frame
lastFrame.pack(side=TOP, fill=X,pady=30)
	
add = Label(toolbar, text='Add')                   ##
delete = Label(toolbar, text='Delete')             ##
search = Label(toolbar, text='Search')             ## creating lables
add_details = Label(toolbar, text='Add Details')   ##
ask_q = Label(toolbar, text='Ask Questions')       ##

add.grid(row=0, column=0, padx=5)                  ##
delete.grid(row=0, column=1, padx=5)               ##
search.grid(row=0, column=2, padx=5)               ## putting all lables in a grid layout
add_details.grid(row=0, column=3, padx=5)          ##
ask_q.grid(row=0, column=4, padx=5)                ##

addValue= IntVar()        ##
deleteValue = IntVar()    ##
searchValue = IntVar()    ## creating variables to store the state of checkbox
AddDValue =IntVar()       ##
AskQVlaue =IntVar()       ##
	
addCheck = Checkbutton(toolbar, onvalue=1,offvalue=0,variable=addValue)        ##
deleteCheck = Checkbutton(toolbar, onvalue=1,offvalue=0,variable=deleteValue)  ##
searchCheck = Checkbutton(toolbar, onvalue=1,offvalue=0,variable=searchValue)  ## creating checkboxes
AddDCheck = Checkbutton(toolbar, onvalue=1,offvalue=0,variable=AddDValue)      ##
AskQCheck = Checkbutton(toolbar, onvalue=1,offvalue=0,variable=AskQVlaue)      ##

addCheck.grid(row=1,column=0)     ##
deleteCheck.grid(row=1,column=1)  ##
searchCheck.grid(row=1,column=2)  ## putting all checkboxes in a grid layout
AddDCheck.grid(row=1,column=3)    ##
AskQCheck.grid(row=1,column=4)    ##

def submitInput():
	import AI_C
	if addValue.get() == 1:
		AI_C.add_file(userEntry.get())
	elif deleteValue.get() == 1:
		AI_C.delete(userEntry.get())
	elif searchValue.get() == 1:
		AI_C.search_file(userEntry.get())
	elif AddDValue.get() == 1:
		AI_C.add_details(userEntry.get())
	elif AskQVlaue.get() == 1:
		AI_C.ask_Q(userEntry.get())

userLabel = Label(bottomFrame, text='Enter here:') # creaing a label for user entry
userEntry = Entry(bottomFrame)                     # creating entry
submit = Button(lastFrame,text='Submit', command=submitInput)              # creating submit button
quitButton = Button(lastFrame, text='Quit', command=lastFrame.quit)
statusBar = Label(window, text='5 items', bd=1, relief= SUNKEN, anchor=W) # bd=border, SUNKEN= its an effect

userLabel.pack(side=LEFT)                          ##
userEntry.pack(fill=X)                             ##
quitButton.pack(side=RIGHT, fill=X)                ##  paking all the three things
submit.pack(fill=X) 
statusBar.pack(side=BOTTOM, fill=X)                ##

window.mainloop()      # main loop
