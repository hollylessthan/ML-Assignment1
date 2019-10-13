e_dis = eval(input("Please enter 5 current coordinates of your friends from the Department of Economics: "))
c_dis = eval(input("Please enter 5 current coordinates of your friends from the Department of Computer Science: "))

for i in range(len(e_dis)):
    e_dis[i].append("econ")
    c_dis[i].append("cs")

test_list=[]
for j in range(len(e_dis)):
    test_list.append(e_dis[j])
for l in range(len(c_dis)):
    test_list.append(c_dis[l])


def dis(a, b):
    return (a - test_list[t][0])**2 + (b - test_list[t][1])**2

test_you=[]

you = eval(input("please enter your location: "))

for t in range(len(test_list)):
    t1 = dis(you[0], you[1])
    t2 = test_list[t][2]
    test_you.append([t1, t2])



k_n_n = sorted(test_you)

k = eval(input("Enter an odd number k , k<10 : "))

depa = [0, 0]
for m in range(k):
    if k_n_n[m][1] == "econ":
        depa[0] = depa[0] + 1
    else:
        depa[1] = depa[1] + 1



if depa[0] >= depa[1]: 
    print("You're a student in the Department of Economic.")
else:
    print("You're a student in the Department of Computer Science.")



print("\n")



