# 

class Node:                               # define the Node
    def __init__(self,nodeValue):
        self.data = nodeValue             # initialise the data field to the value provided by the caller
        self.right = None                 # initialise the pointer to the RHS node
        self.left = None                  # initialise the pointer to the LHS node
        
class Tree:                               # define the binary Tree and some methods that can be inherited
    
    def createNode(self,nodeValue):
        return Node(nodeValue)            # return Node after a call to the function above
    
    def insertNode(self,node,nodeValue):  # insert a new node carrying nodeValue into the proper location
        
        if node is None:
            return self.createNode(nodeValue)  # reached either a leaf, or the root of the tree, insert the node
        
        if nodeValue < node.data:
            node.left = self.insertNode(node.left,nodeValue)   #if the data < the data of the current node, call the function again assigning the result at the left node pointer
        elif nodeValue > node.data:
            node.right = self.insertNode(node.right,nodeValue) #if the data > the data of the current node, call the function again assigning the result at the right node pointer
                                                               #duplicate entries are not permitted, hence the absence of the = case
        return node

    def traverseInOrder(self,root):                            #in order traversal prints the value of the left child, followed by the value of the node, and the value of the right child
        if root is not None:                                   #print the values if pointer is not null
            self.traverseInOrder(root.left)                    #first call the function recursively to print the LHS child
            print (root.data)                                  #print the value of the node
            self.traverseInOrder(root.right)                   #finally call the function recursively to printthe RHS child

    def traversePreOrder(self,root):                           #pre order traversal prints the value of node, followed by the LHS child and the RHS child
        if root is not None:                                   #print the values if pointer is not null
            print (root.data)                                  #first print the value of the node
            self.traversePreOrder(root.left)                   #then call the function recursively to print the LHS child
            self.traversePreOrder(root.right)                  #finally call the function recursively to printthe RHS child

    def traversePostOrder(self,root):                          #post order traversal prints the value of the LHS child, the value of the RHS child and the value of the node
        if root is not None:                                   #print the values if pointer is not null
            self.traversePostOrder(root.left)                  #first call the function recursively to print the LHS child
            self.traversePostOrder(root.right)                 #then call the function recursively to printthe RHS child
            print (root.data)                                  #finally print the value of the node


#
# Build the binary tree presented in the notes and then traverse it in the three different manners available
#
     
root = None                              # initialise the variable root so that the interpreter will know what to do with it     
ExampleTree = Tree()                     # create a new Tree object from the Tree class defined above
root = ExampleTree.insertNode(root,20)   # insert node A, with value 20.  This will be the root of the tree
ExampleTree.insertNode(root,5)           # all subsequent nodes are inserted by providing the pointer to the root and the value to be inserted
ExampleTree.insertNode(root,3)
ExampleTree.insertNode(root,1)
ExampleTree.insertNode(root,4)
ExampleTree.insertNode(root,15)
ExampleTree.insertNode(root,9)
ExampleTree.insertNode(root,30)
ExampleTree.insertNode(root,25)
ExampleTree.insertNode(root,23)
ExampleTree.insertNode(root,21)
ExampleTree.insertNode(root,26)
ExampleTree.insertNode(root,40)          # all nodes of example tree have now been inserted

ExampleTree.traverseInOrder(root)
print()
ExampleTree.traversePreOrder(root)
print()
ExampleTree.traversePostOrder(root)







    

