desk ="/Users/lofangyu/Desktop/"
f = open(desk + "iris.data.txt", "r")
list = f.readlines()


new_list=[]
for i in range(len(list)-1):
    m = list[i]
    n = m.replace(","," ")
    new_list.append(n.split())

new_list_60 = []
for g in range(0,30):
    new_list_60.append(new_list[g])
for h in range(0,30):
    new_list_60.append(new_list[50+h])
for f in range(0, 30):
    new_list_60.append(new_list[100+f])

new_list_40 = []
for o in range (0,20):
    new_list_40.append(new_list[30+o])
for p in range (0,20):
    new_list_40.append(new_list[80+p])
for q in range (0,20):
    new_list_40.append(new_list[130+q])


def dis(a, b, c, d):
    return (a - eval(new_list_60[t][0]))**2 + (b - eval(new_list_60[t][1]))**2 + (c - eval(new_list_60[t][2]))**2 + (d - eval(new_list_60[t][3]))**2


test=[]
test_class = []
for r in range(len(new_list_40)):
    for t in range (len(new_list_60)):
        t1 = dis(eval(new_list_40[r][0]), eval(new_list_40[r][1]), eval(new_list_40[r][2]), eval(new_list_40[r][3]))
        t2 = new_list_60[t][4]
        test.append([t1, t2])
    
    k_n_n = sorted(test)

    if k_n_n[0][1] == "Iris-setosa":
        test_class.append("Iris-setosa")
    elif k_n_n[0][1] == "Iris-versicolor":
        test_class.append("Iris-versicolor")
    else:
        test_class.append("Iris-virginica")
    test = []
    k_n_n = []

print(test_class)

correct = 0
wrong = 0
for s in range(len(test_class)):
    if test_class[s] ==new_list_40[s][4]:
        correct += 1
    else:
        wrong += 1

correct_rate = correct / 60

print("\ncorrect classify: ")
print(correct)
print("\nwrong classify: ")
print(wrong)
print("correct rate: ")
print(correct_rate)

print("\n")


