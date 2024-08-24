set1 ={1,2,3}
set2 ={2,3,4}

# Union : |  or union()
union_set = set1 | set2
print(union_set)
# {1, 2, 3, 4}

#Intersection : & or intersection()
intersection_set = set1 & set2
print(intersection_set)
# {2, 3}

# Difference : - or difference()
# The difference of two sets A and B is defined as the lists of all the elements that are in set A but that are not present in set B.
diff_sets = set1 - set2
print(diff_sets)
# {1}

# Symmetric Difference : ^ or symmetric_difference()
sym_diff = set1 ^ set2
print(sym_diff)
# {1, 4}