def update_chat(msg, state):
    global chatlog

    chatlog.config(state=NORMAL)

    if state == 0:
        chatlog.insert(END, msg)
    else:
        chatlog.insert(END, msg, END)
    chatlog.config(state=DISABLED)

    chatlog.yview(END)
