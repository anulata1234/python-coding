


# Non greedy alogorithm to reach the end of array if possible       
# increment each i with 1 and then furthest_reached = max(furthestreached+A[i]+i)
# this will tell in non greedy way if we can reach or not 
def array_advance(A):
    import pdb
    pdb.set_trace()
    furthest_reached = 0
    last_index=len(A)-1
    i=0
    while i <= furthest_reached and furthest_reached < last_index:
        furthest_reached = max(furthest_reached, A[i]+i)
        if furthest_reached == last_index:
            return(A[i])
        i = i+1
    return furthest_reached >= last_index

A1 = [3,3,1,0,2,0,1]
print(array_advance(A1))
