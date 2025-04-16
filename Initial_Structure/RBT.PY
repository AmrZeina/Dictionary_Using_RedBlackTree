class Node:

    def __init__(self,value):  #this is the constructor and self is like "this" in java
        self.value=value
        self.color='RED'
        self.parent=None
        self.right=None
        self.left=None


class RBT:

    def __init__(self):
        self.nil=Node(None)
        self.nil.color='BLACK'
        self.root=self.nil


    def insert(self,value):
        node=Node(value)
        node.left=self.nil
        node.right=self.nil

        if(self.root==self.nil):  #checks if the tree is empty so insert the node at the root
            node.color='BLACK'
            self.root=node
        else:
            self.insert_recursive(self.root,node)


    def insert_recursive(self,current,new):
        if(new.value<current.value):
            if(current.left==self.nil):
                current.left=new
                new.parent=current
            else:
                self.insert_recursive(current.left,new)
        else:
            if(current.right==self.nil):
                current.right=new
                new.parent=current
            else:
                self.insert_recursive(current.right,new)


    def search(self,value):
        node= self.root

        while node!=self.nil and node.value!=value:
            if value<node.value:
                node = node.left
            else:
                node = node.right

        if node!=self.nil:
            return node
        else:
            return null


    def get_tree_height(self, node=None):
        if node is None:
            node=self.root

        if node == self.nil:
            return 0

        else :  #getting the left and right length and calculate the max recursively
            left_height=self.get_tree_height(node.left)
            right_height=self.get_tree_height(node.right)

        return 1+max(left_height,right_height)


    def get_black_height(self, node=None):
        if node is None:
            node = self.root

        black_height=0  #initialize black height with 0

        while node!=self.nil:
            if node.color=="Black":
                black_height+=1
            node=node.left  #does not matter left or right bec. it is fixed for all possible ways to nil

        black_height+=1 #for nil node
        return black_height

"""
#Main function
if __name__=='__main__':
    tree=RBT()
    tree.insert(50)
    tree.insert(60)
    tree.insert(70)
    tree.insert(20)
    print(tree.search(70).parent.value)
"""
        

