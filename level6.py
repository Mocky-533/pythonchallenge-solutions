import zipfile
num = "90052"
comments = []
f = zipfile.ZipFile("assets/channel.zip")   # open zip file
try:
    while True:
        filepath = num + ".txt"
        line = f.read(filepath).decode("utf-8") # read txt file inside
        comment = f.getinfo(filepath).comment.decode("utf-8")     # comment of txt file
        num = line.split(" ")[-1]
        comments.append(comment)
except KeyError:
    print("".join(comments))
