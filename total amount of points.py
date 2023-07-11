games = ['1:2','2:3','3:3','4:0','2:1','3:1','4:1','3:3','4:6','4:3']
print (games)
def points(games):
    score = 0
    for i in games:
        if i[0] > i[-1]:
            score += 3
        elif i[0] < i[-1]:
            score += 0
        else: 
            score += 1
    print(score)
points(games)

