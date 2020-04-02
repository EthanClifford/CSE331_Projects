from Project6.BinarySearchTree import BinarySearchTree

bst = BinarySearchTree()

bst.insert(14)
bst.insert(7)
bst.insert(21)
bst.insert(3)
bst.insert(10)
bst.insert(17)
bst.insert(25)

bst.remove(14)
bst.remove(17)
bst.remove(10)
bst.remove(21)
bst.remove(16)
bst.remove(7)
bst.remove(12)
print(bst.root)
print(bst.root.left)
print(bst.root.right)

gen1 = bst.preorder(bst.root)
gen2 = bst.postorder(bst.root)
gen3 = bst.inorder(bst.root)

pre = [14,7,3,10,21,17,25]
post = [3,10,7,17,25,21,14]
inorder = [3,7,10,14,17,21,25]

for i in range(7):
#    print(i)
    print("preorder ",i," : ",next(gen1, None)) #pre[i]
    print("postoder ",i," : ",next(gen2, None)) #post[i]
    print("inorder ",i," : ",next(gen3, None)) #inorder[i]
print(bst.is_perfect(bst.root)) #True
print(bst.is_degenerate()) #False


print("size: ",bst.get_size())
print("min: ",bst.min(bst.root))
print("max: ",bst.max(bst.root))
print("depth: ",bst.depth(14))
print("height: ",bst.height(bst.root))
print("search 13: ", bst.search(13, bst.root))
#print("search 13: ", bst.search(13, bst.root.left))
#print(bst.root)  #13
#print(bst.root.left)  #13
#print(bst.root.left.left)  #7
#print(bst.root.left.right)  #9
#print(bst.root.right.value)  #12
#print(bst.root.right.right.value)  #13
#print(bst.root.right.left.value)  #11