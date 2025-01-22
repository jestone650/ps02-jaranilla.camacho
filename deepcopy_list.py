import copy
nested_list=[[1,2,],[3,4]]
copy_list=copy.deepcopy(nested_list)
alias_nested=copy_list
alias_nested[0][1]=99
print("Original nested list:", nested_list)
print("Aliased nested list:", alias_nested)