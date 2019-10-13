# computer assignment (1)readme

Q1. Write a program whose input is the training set, a user-specified value of k, and
an object, x. The output is the class label of x.

**Introduction**
-
This code is designed to classify what department the user belongs to by entering 10 of his/her friends' current locations[x, y].  The user then input his/her current location and can decide what "k" he /she would like to use to implement a k-n-n classifer. By doing the three steps, the computer will output department that the user belongs to.

The code is written in Python 3.7.0 64-bit

**Explanation of Code**
-
*  As a start, the user should *INPUT* 5 locations of people of the Department of Economics as training set. 

    For example,

     [2.3, 4.5], [4.5, 1.2], [3.4, 6.9], [4.9, 2.3], [8.1, 1.2]

 * Secondly, the user should *INPUT* 5 locations of people of the Department of Computer Science as training set. 
 
     For example,

    [0.3, 6.3], [5.9, 2.4], [2.4, 1.5], [7.7, 8.0], [6.2, 3.1]

*    The code below uses ”.append“ to form a training set, test_list, containing 10 examples in the type of [x, y, "econ/cs"]


    for i in range(len(e_dis)):
        e_dis[i].append("econ")
        c_dis[i].append("cs")

    test_list=[]
    for j in range(len(e_dis)):
        test_list.append(e_dis[j])
    for l in range(len(c_dis)):
        test_list.append(c_dis[l])

*    The code below is a function that calculate the square of distances between the user and examples.(Here I use distance^2, not distance, but it won't affect the classfication result.)  


    def dis(a, b):
        return (a - test_list[t][0])**2 + (b - test_list[t][1])**2


*  Following, the user should enter his/her current location in order to classfy which department he/she belongs to.

    For example, 

    [3.3, 5.6]

*    The code below is to rearange the example from the lowest distance to the highest one.


    k_n_n = sorted(test_you)

* Then, the user should decide what k he/she would like to use as a k-n-n classfier. Here the computer asks the user to enter an odd number because we're in a two-class domain.

* Finally, the computer counts how many "econ" or "cs" are there in k-n-n and print out the output.

