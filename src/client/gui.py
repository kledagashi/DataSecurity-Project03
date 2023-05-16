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

 
    chatlog.place(x=6, y=6, height=386, width=390)
    textbox.place(x=6, y=401, height=20, width=265)
    sendbutton.place(x=300, y=401, height=20, width=50)
 
 
    textbox.bind("<KeyRelease-Return>", press)

   
    _thread.start_new_thread(receive, ())

    
    gui.mainloop()


if __name__ == '__main__':
    chatlog = textbox = None
    s = initialize_client()
    GUI()

