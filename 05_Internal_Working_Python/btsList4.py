h1 = [1,2,3]

h2 = h1[:]
# h2 = h1[0:2]
# [0:2] is slicing from 0 index till 2 index
#  Slicing create a copy of List

# h1
# [1, 2, 3]

# h2
# [1, 2, 3]

h1[0]= 55
# h1
# [55, 2, 3]

# h2
# [1, 2, 3]