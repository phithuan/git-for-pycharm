f=open("info.txt", "w", encoding="utf-8")
for i in range(10):
    f.write(f"dòng thứ {i} \n")
f.close()