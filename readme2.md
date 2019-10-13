# computer assignment (2)readme

Q.2. Apply the program implemented in the previous assignment to some of the benchmark domains from the UCI repository.5 Always take 40% of the examples out and reclassify them with the 1-NN classifier that uses the remaining 60%.

**Introduction**
-

This code is written in Python 3.7.0 64-bit

**Explanation of the Code**
-

* First of all, I open the data file and then split and arrange the data to form a orderly list, new_list. I use a series of for-loops to take 60% of the examples as training set and 40% of the examples as testing set.

*    Secondly, I create a function, dis(a, b, c, d), to calculate the distance between testing example and training example.(Here I use distance^2, not distance, but it won't affect the classfication result.) 

    def dis(a, b, c, d):
    return (a - eval(new_list_60[t][0]))**2 + (b - eval(new_list_60[t][1]))**2 + (c - eval(new_list_60[t][2]))**2 + (d - eval(new_list_60[t][3]))**2

*    Below is 2 for-loops to class the testing examples according to training example. 
      
        As a start, the computer takes 1 testing example to calculate the distance between 90 training examples and put them into a list, test. 
      
      Then we sorts the list from the nearest one to the farther one. Further, we use 1-n-n classfier to see the nearest one is Iris-setosa, Iris-versicolor or Iris-virginica.

      After these steps, we class the testing example to a certain class. The another 59 testing example will continue the same testing process.

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


* In the end, we compare the final classfication result to the original data to see how many examples we class correctly, wrongly and also calculate the correcy rate.