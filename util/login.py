import hashlib

file=open("data/info.csv", "r")
temp=file.read()
temp=temp.split("\n")
temp=temp[:-1]
file.close()

dict={}
for line in temp:
    dict[line.split(",")[0]] = line.split(",")[1]


def registered(username, password):
    if username in dict.keys():
        return False
    else:
        tempPass = hashlib.sha1(password).hexdigest()
        file=open("data/info.csv", "a")
        file.write(username+","+tempPass+"\n")
        print "done"
        file.close()
        return True

def verifyUser(username):
    if username in dict.keys():
        return True
    return False

def verifyPass(username, password):
    if verifyUser(username):
        if dict[username] == hashlib.sha1(password).hexdigest():
            return True
        return False
    return False
