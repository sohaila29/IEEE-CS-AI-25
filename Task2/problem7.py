def common(set1, set2):
    commonSet = set()
    for i in set1:
        if i in set2:
            commonSet.add(i)
    return commonSet

set1 =(1,5,2,29,8,66)
set2 = (10,8,5,3,22,1)
print("Common Elements: ",common(set1, set2) )