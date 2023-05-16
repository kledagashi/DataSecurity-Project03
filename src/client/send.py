def send():
    global textbox

    msg = textbox.get("0.0", END)
    encrypted_data = readDES().encrypt(msg)


    update_chat(encrypted_data, 0)


    s.send(encrypted_data)
    textbox.delete("0.0", END)
