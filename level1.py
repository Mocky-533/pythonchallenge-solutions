

# string1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
label1 = "abcdefghijklmnopqrstuvwxyz"
label2 = "cdefghijklmnopqrstuvwxyzab"
trans = str.maketrans(label1, label2)
# print("map".translate(trans))
line = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# list1 = []
# for i in list(line):
#     if i.isalpha():
#         j = ord(i)+2
#         s = chr(j) if j<123 else chr(j-26)
#     else:
#         s = i
#     list1.append(s)
# print("".join(list1))

print(line.translate(trans))