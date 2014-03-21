"""
An integer array contains elements in (strictly) increasing order till 
some point and then (strictly) decreasing order , return the index of
maximum number. Solution should be less than O(n). The array is
non-empty. Ex - {1,2,3,4,5,3,1}
"""
def ternarySearch(a):
    if len(a) == 1:
        return a[0]
    elif len(a) == 2:
        return max(a[0], a[1])
    else:
        return rTernarySearch(a, (len(a)-1)/3, 2*(len(a)-1)/3, 0, len(a)-1)

def rTernarySearch(a, s, t, l, r):
    if s == t:
        return a[s]
    elif a[s] <= a[t]:
        return rTernarySearch(a, s+1, r, s+1, r)
    else:
        return rTernarySearch(a, l, t-1, l, t-1)
