if __name__ == '__main__':
    chatlog = textbox = None
    conn = initialize_server()
    createDES()
    send_file("server-des-key.pem", "received-server-des-key.pem")
    GUI()

