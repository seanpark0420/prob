a = input()
b = input()
count = 0
for i in range(int(a),int(b)+1):
    for x in range(i):
        if int(i) % int(x+1) == 0:
            count = count + 1
count
