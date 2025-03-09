def PD(data):
    freq ={}
    for i in data:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
        
    count = len(data)

    result ={}
    for key, i in freq.items():
        result[key] = i/count
    return result
    
 

values = input(" Enter the list separated with spaces: ")
data = list(map(int, values.split()))
print(PD(data))