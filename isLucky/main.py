def solution(n):
    list_r = []
    sum_1, sum_2 = 0,0
    while(n/10!=0):
        list_r.append(n % 10)
        n = n//10

    for i in range(len(list_r)):
        if i < len(list_r)//2:
            sum_1 = sum_1 + list_r[i]
        else:
            sum_2 = sum_2 + list_r[i]

    return sum_1 == sum_2

if __name__ == '__main__':
    print(solution(239017))