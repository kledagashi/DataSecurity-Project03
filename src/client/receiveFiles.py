def receiveFiles():

    filename = s.recv(1024).decode("ascii")
    print(f"[RECV] Receiving the filename.")
    file = open(filename, "w")
    s.send("Filename received.".encode("ascii"))

    data = s.recv(1024).decode("ascii")
    print(f"[RECV] Receiving the file data.")
    file.write(data)
    s.send("File data received".encode("ascii"))


    file.close()

