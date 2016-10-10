import hashlib

def registered(username, password):
    file=open("data/info.csv", "r")
    temp=file.read()
    temp=temp.split("\n")
    temp=temp[:-1]
    file.close()

    dict={}
    for line in temp:
        dict[line.split(",")[0]] = line.split(",")[1]
    if username in dict.keys():
        return False
    else:
        tempPass = hashlib.sha1(password).hexdigest()
        filee=open("data/info.csv", "a")
        filee.write(username+","+tempPass+"\n")
        print "done"
        filee.close()
        return True

def verifyUser(username):
    file=open("data/info.csv", "r")
    temp=file.read()
    temp=temp.split("\n")
    temp=temp[:-1]
    file.close()

    dict={}
    for line in temp:
        dict[line.split(",")[0]] = line.split(",")[1]
    if username in dict.keys():
        return True
    return False

def verifyPass(username, password):
    file=open("data/info.csv", "r")
    temp=file.read()
    temp=temp.split("\n")
    temp=temp[:-1]
    file.close()

    dict={}
    for line in temp:
        dict[line.split(",")[0]] = line.split(",")[1]
    if verifyUser(username):
        if dict[username] == hashlib.sha1(password).hexdigest():
            return True
        return False
    return False
