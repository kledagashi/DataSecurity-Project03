def createDES():
    key = "12345678"
    k = pyDes.des(key, pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

    with open("server-des-key.pem", "wb") as f:
        f.write(key.encode('ascii'))
    return k
