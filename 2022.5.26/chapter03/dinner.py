names = ['迈克尔杰克逊', '霍金', '桥本环奈']
print("\n\t晚宴邀请")
print("邀请 " + names[0] + " 参加晚宴")
print("邀请 " + names[1] + " 参加晚宴")
print("邀请 " + names[2] + " 参加晚宴")

cant_attend = "桥本环奈"
print("\n! " + cant_attend + " 无法参加晚宴")
names.remove(cant_attend)
new_guest = "石原里美"
names.append(new_guest)
print("\n\t晚宴邀请")
print("邀请 " + names[0] + " 参加晚宴")
print("邀请 " + names[1] + " 参加晚宴")
print("邀请 " + names[2] + " 参加晚宴")

names.insert(0, "成龙")
names.insert(2, "贝多芬")
names.append("爱因斯坦")

print("\n\t晚宴邀请")
print("邀请 " + names[0] + " 参加晚宴")
print("邀请 " + names[1] + " 参加晚宴")
print("邀请 " + names[2] + " 参加晚宴")
print("邀请 " + names[3] + " 参加晚宴")
print("邀请 " + names[4] + " 参加晚宴")
print("邀请 " + names[5] + " 参加晚宴")

print("\n晚宴名单人数限制为两位")
names.pop()
names.pop()
names.pop()
names.pop()
print(names[1] + " 仍在受邀人之列")
print(names[0] + " 仍在受邀人之列")

del names[1]
del names[0]
print("清空后的名单：" + str(names))
