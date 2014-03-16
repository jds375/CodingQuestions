# Coding Questions #
Here I have coded up solutions to many well-known interview questions from popular tech companies. Here I present the optimal solution and the reasoning behind it. Note that all of these interview questions were found online by a simple search. Any questions that I have been asked personally in interviews I have excluded. 

#### String-based Questions ####
Questions involving string manipulations are very common. They are often straight-forward and it is easy to find a decent solution to them. However, finding the best solutions is often quite tricky.

##### The Substring Search Problem #####
<i> Question: Substring Write a program to determine whether an input string x is a substring of another input string y. For example, "bat" is a substring of "abate", but not of "beat". </i>
<br>
<p>The obvious solution to this problem is a nested for-loop where we iterate about the string y and then iterate about the string x, checking letter by letter if we have a match. This solution is O(x·y), which is very good. But, we can still slightly improve our algorithm. There is room for improvement because the algorithm above doesn't use all of the information available to solve the problem. For example, suppose x is 1,000 characters where the first 999 characters are 'A' and the last character is 'B'. Suppose that y is 1 billion characters long and only contains the character 'A'. In the naive algorithm we would make about 1 trillion comparisons because we would iterate through the 1,000 characters in x one billion times (once for each starting index in y). However, consider just the first iteration. We find 999 matches to the character 'A' and then fail on the thousandth for the character 'B'. For the next iteration we shouldn't need to backtrack and retest the first 998 values because we already did the comparison and know that they will all be 'A's. If we use this logic for the entire string, then after the first iteration, we will only be making 2 comparisons for each step through y. Thus, it would only a couple billion comparisons as opposed to a trillion. The idea is that when we fail a match, we can often jump ahead in y by taking into account the comparisons we have already done on x.</p>
<p>We now propose an algorithm that generalizes this idea. We let <i>m</i> represent our position in y. We let <i>i</i> represent our position in x. We want the algorithm to terminate as soon as <i>m+i</i> exceeds the length of y since at this point finding a match is hopeless. We begin by checking if the character at index <i>i</i> in x matches the character at index <i>m+i</i> in y. Suppose it does. This means we have a match. We now check if <i>i</i> is the length of x. If it is, then we are done and return <i>True</i>. If it isn't the length of x, then we simply increment <i>i</i>. Now suppose that the match fails. We increment <i>m</i> by <i>i</i>. This is using our 'optimization' whereby we need not recheck the previous matches. We note, however, that there are cases where we may still have to backtrack a few steps. Let us create a table <i>t</i> that gives the number of spaces we need to backtrack in string y when at index <i>i</i> in x. We would then want to increment <i>m</i> by <i>i</i> and subtract it by <i>t[i]</i>. We later show how to construct this table. Lastly, we check if <i>t[i]</i> is larger than -1 and if so we set <i>i</i> to the value in <i>t[i]</i>. Otherwise, we set it to 0. We perform the check against -1 so that <i>i</i> cannot be negative. Lastly, if we make it through the outer loop then we have not found a match and we return false. We code this accordingly below:</p>
````python
def hasSubstring(x, y):
    t = buildBacktrackArray(x)
    m = 0
    i = 0
    while (m + i < len(y)):
        if x[i] == y[m + i]:
            if i == len(x) - 1:
                return True
            i += 1
        else:
            m += i - t[i]
            if t[i] > -1: 
                i = t[i]
            else:
                i = 0
    return False
````
<p>We now must construct the table building function. As per specification, the table is the length of x. We begin by initializing the value of <i>t[0]</i> to -1. This is because if we look at the above algorithm we see that in the case of a mismatch for <i>i = 0</i> we need <i>t[i]</i> to be -1 in order to increment <i>m</i> by 1 so that we still look ahead in the algorithm. Likewise, we initialize <i>t[1]</i> to 0. This is because if we have a mismatch on the second character when <i>i = 1</i> we still want to just increment <i>m</i> by 1 and can thus achieve this by letting <i>t[1]</i> be 0. We now do the rest, which depends on the contents of x. Ideally, every value in the rest of the table would be 0 because if we ever get a mismatch, we can just jump ahead in y by the number of characters in x we have already matched. However, there is the case where a pattern in the substring re-emerge. Consider "ABCDABDE". If we fail a match on the second "B" or the first "D", then we must by 1 or 2 because it could be the case that this second term is being mathed to in y. We code this as follows. We let <i>iT</i> represent our position in <i>t</i> and <i>iX</i> represent our position in analyzing x. We loop as long as <i>iT</i> is less than the length of x. If the value of x at <i>iX</i> is equal to the value of x at <i>iT - 1</i> then we have a repeated pattern occuring. We thus increment <i>iX</i> by 1. We set <i>t[iT]</i> to be <i>iX</i>. Lastly, we increment <i>iT</i> by 1. We now consider the case that there isn't a repetition, but our position in x is greater than 0. If so, we set <i>iX</i> to be the value at <i>t[iX]</i> because we still need our backtrack value for the end of the current repeating patern. Lastly, it must be the case that we simply have a 0. We thus set  <i>t[iT]</i> to 0 and increment <i>iT</i> by one.</p> We thus have: 
````python
def buildBacktrackArray(x):
    t = [None] * len(x);
    t[0] = -1
    t[1] = 0
    iT = 2
    iX = 0
    while (iT < len(x)):
        if x[iT - 1] == x[iX]:
            iW += 1
            t[iT] = iX;
            iT += 1
        elif iW > 0:
            iW = t[iX]
        else:
            t[iT] = 0
            iT += 1
    return t
````
We are now done. We observe that the running time is O(x + y) since building the table is O(x) and now the substring search is O(y). Most importantly, it avoids many of the worst-case scenarios that the naive algorithm encounters. Lastly, note that this can be easily modified to return the starting index where x occurs in y.
