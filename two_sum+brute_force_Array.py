


A=[-2,1,2,4,7,11]
target = 20



def two_sum_brute_force(A,target):
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i]+A[j] == target:
                print(A[i],A[j])
                return True
    return False

two_sum_brute_force(A,13)
