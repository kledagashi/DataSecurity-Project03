def receive():
    while 1:
        try:
            data = conn.recv(1024)
            msg = data
            if msg != "":
                decrypted_data = createDES().decrypt(msg)
                update_chat(decrypted_data, 1)
        except:
            pass
