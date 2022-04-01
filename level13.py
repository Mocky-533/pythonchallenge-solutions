import xmlrpc.client

post = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(post.system.methodHelp("system.multicall"))
print(post.system.listMethods())
print(post.phone("Bert"))
