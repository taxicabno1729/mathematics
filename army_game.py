# Reference: https://www.hackerrank.com/challenges/game-with-cells/problem?isFullScreen=true

# Luke is daydreaming in Math class. He has a sheet of graph paper with n rows and m columns, 
# and he imagines that there is an army base in each cell for a total of  bases. He wants to drop 
# supplies at strategic points on the sheet, marking each drop point with a red dot. If a base contains 
# at least one package inside or on top of its border fence, then it's considered to be supplied.

# Given  and , what's the minimum number of packages that Luke must drop to supply all of his bases?

# Example:

# n = 2 and m =3 
# The given cells can be represented by (0,0), (0,1), (0,2), (1,0), (1,1) and (1,2). 

# Packages can be dropped at the corner between cells (0, 0), (0, 1), (1, 0) and (1, 1) to supply 4 bases. 
# Another package can be dropped at a border between (0, 2) and (1, 2). This supplies all bases using 2 packages.

def gameWithCells(n, m):
    count = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i%2 == 1 and j%2 == 1:
                count += 1
    
    return count
