'''
5
Harsh
20
Beria
20
Varun
19
Kakunami
19
Vikas
21
'''

if __name__ == '__main__':
    names = []
    scores = []
    # students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
        # students.append([name, score])


    _min = min(scores)  
    i = 0 
    while _min in scores:
        if scores[i] == _min:
            names.pop(i)
            scores.pop(i)
            i-=1
        i+=1
        
    result_names = []
    _min = min(scores)  

    for i in range(len(names)):
        if scores[i] == _min:
            result_names.append(names[i])

    for result_name in sorted(result_names):
        print(result_name)
    


    