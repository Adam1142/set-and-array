import array as arr
var1 = arr.array("i",[1, 3, 5, 3, 7, 9, 3])
print("original array:"+str(var1))
print("number of occurrance of the number 3:"+str(var1.count(3)))
var1.reverse()
print("reverse the order of items:")
print(str(var1))