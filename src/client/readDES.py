def readDES():
    with open("received-server-des-key.pem", "rb") as f:
        k = f.read()
    key = pyDes.des(k.decode('ascii'), pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    return key
