def receive():
    receiveFiles()
    while 1:
        try:
            data = s.recv(1024)
            msg = data.decode('ascii')

            if msg != "":
                update_chat(msg, 1)

        except:
            pass
