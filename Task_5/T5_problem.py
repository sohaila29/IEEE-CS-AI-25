def sample(count):
    n = sum(count)
    total_sum = 0 
    for i in range(len(count)):
        total_sum += i *count[i]

    mean = total_sum / n
    for i in range(len(count)):
        if count[i] > 0:
            minimum =i
            break

    for i in range(len(count)-1, -1,-1):
        if count[i] > 0:
            maximum =i
            break

    mode = 0
    freq = 0
    for i in range(256):
        if count[i] > freq:
            freq = count[i]
            mode = i

def calc_median(count, n):
    counting = 0
    median1 = (n +1)//2
    median2 = n//2+1
    
  #I’ve lost all motivation, and there are only ten minutes left until the deadline. It’s been an unbearable week.
  #sooooryyy