from fun import fun_map, fun_reduce, fun_filter

#Test implementation of filter function
print (fun_filter(lambda x: True if type(x) is str else False, ['unni','krishnan', 12]))

#Test implementation of map function
print (fun_map(lambda x,y: x+y, [10,11,12,34], [20,21,22,64]))

#Test implementation of reduce funtion
print (fun_reduce(lambda x,y: x*y, [1,2,3,4,5,6], 10))
