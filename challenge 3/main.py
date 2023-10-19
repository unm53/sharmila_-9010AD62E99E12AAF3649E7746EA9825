def linearsearchproduct(productlist,targetproduct):
  indices=[]
  for index,product in enumerate(productlist):
    if product==targetproduct:
      indices.append(index)

  return indices

#example usage:

products=["shoes","boot","loafer","shoes","sandle","shoes"]
target="shoes"
target2="apple"
result=linearsearchproduct(products,target2)
print(result)

l1=['shoes','cars','laptop']
for i,j in enumerate(l1):
  print(i,j)