
'''
arr2bin([1,2]) == '11'
arr2bin([1,2,'a']) == '11'
arr2bin([]) == '0'
Test.assertEquals(arr2bin([1,2]), "11")
Test.assertEquals(arr2bin([1,2,3,4,5]), "1111")
Test.assertEquals(arr2bin([1,10,100,1000]), "10001010111")
Test.assertEquals(arr2bin([null]), "0")
Test.assertEquals(arr2bin([True,True,False,15]),"1111")
'''
def arr2bin(arr):
  return str(bin(sum( [x for x in arr if type(x)==type(1)] )))[2:]
  
# print arr2bin([1,2]), "11"

# print arr2bin([1,2,3,4,5]), "1111"
# print arr2bin([1,10,100,1000]), "10001010111"
# print arr2bin([None]), "0"
# print arr2bin([True,True,False,15]),"1111"
