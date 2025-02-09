def runner_up(scores1):
    scores2 = set(scores1)
    sorted_scores = sorted(scores2)
    runner_up = sorted_scores[-2]
    return runner_up




n = int(input("enter the n of scores: "))
scores=[]
for i in range(n):
    scores.append(int(input("enter scores: ")))

print(runner_up(scores))