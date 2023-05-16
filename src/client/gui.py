
def press(event):
    send()

def GUI():
    global chatlog
    global textbox


    gui = Tk()
    
    gui.title("Client Chat")
   
    gui.geometry("400x430")

    chatlog = Text(gui, bg='white')
    chatlog.config(state=DISABLED)

    sendbutton = Button(gui, bg='orange', fg='red', text='SEND', command=send)
  
    textbox = Text(gui, bg='white')

    

