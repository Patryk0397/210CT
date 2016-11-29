class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)



    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
 
 
def in_order(tree):

    stack = []
    finished = False


    while (finished == False):  #Keeps the loop going until the else statement

        if tree != None:        #If tree isnt empty
            stack.append(tree)  #append the root node to the stack

            tree = tree.left    #pointer goes to the left value

        else:

            if (len(stack) > 0):#if the length of the stack is more than 0
                tree = stack.pop()#pop the most recent value from stack
                print(tree.value)#and print it
                tree = tree.right#pointer goes to the right value
            else:
                finished = True#if stack is empty, finish the loop

    

 
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)

