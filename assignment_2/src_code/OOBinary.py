import sys
class Node:
  """left and right default values are None"""
  def __init__(self,item,left=None,right=None):
    self.item = item
    self.left = left
    self.right = right
    
class BinarySearchTree:

  def __init__(self):
    self.root = None
    
  def insert(self,item):
    """if tree empty, place as root"""
    if self.root == None:
      self.root = Node(item,None,None)
    else:
        ptr = self.root
        while ptr != None:
          parent = ptr
          if item < ptr.item:
            ptr = ptr.left
          else:
            ptr = ptr.right
            
        if item < parent.item:
          parent.left = Node(item, None, None)
        else:
          parent.right = Node(item, None, None)
                    
  def search(self,prt,item):
    if ptr == None:
      return False
    elif ptr.item == item:
      return True
    else:
      return self.search(ptr.left,item) or self.search(ptr.right,item)

  def inorder(self,ptr):
    """once the search has stopped, return nothing to exit the function"""
    if ptr == None:
      return
    if ptr.left != None:
      self.inorder(ptr.left) 
    print(ptr.item,end=' ') 
    if ptr.right != None:
      self.inorder(ptr.right)
  
  def preorder(self,ptr):
    if ptr == None:
      return
    print(ptr.item,end=' ')  
    if ptr.left != None:
      self.preorder(ptr.left)   
    if ptr.right != None:
      self.preorder(ptr.right) 
           
  def postorder(self,ptr):
    if ptr == None:
      return
    if ptr.left != None:
      self.postorder(ptr.left)   
    if ptr.right != None:
      self.postorder(ptr.right)     
    print(ptr.item,end=' ')  


def main():
    tree = BinarySearchTree()
    print('Please enter the node values for a tree')
    nodes = input()
    nodes = nodes.strip().split()
    
    for node in nodes:
        tree.insert(int(node))
     
    func = input(" To add a new value -> enter insert\n To check for an existing element in the tree -> enter search\n To view the elements in preorder -> enter preorder \n To view the elements in order -> enter inorder \n To view the elements in postorder -> enter postorder\n")
    while func.strip() != "exit":
      if func.strip() ==  "preorder": 
        print("The elements in pre order are...")
        tree.preorder(tree.root)
        print('\n',end='')
      if func.strip() ==  "inorder": 
        print("The elements in order are...")
        tree.inorder(tree.root)
        print('\n',end='')
      if func.strip() ==  "postorder":
        print("The elements in post order are...")
        tree.postorder(tree.root)
        print('\n',end='')
      if func.strip() ==  "insert":
        item =int(input("Enter the element you wish to add:")) 
        tree.insert(item)
      if func.strip() == "search":
        item =int(input("Enter the element you wish to search:")) 
        tree.search(tree.root,item)
      func = input() 

if __name__ == "__main__":
    main()