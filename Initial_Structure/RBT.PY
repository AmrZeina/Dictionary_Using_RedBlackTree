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
            self.root=node
            node.parent=None
            node.color='BLACK'
            self.recolor_rotate(node)
        else:
            self.insert_recursive(self.root,node)
            self.recolor_rotate(node)

            
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

    def recolor_rotate (self,node):
        while (node != self.root and node.parent and node.parent.color=='RED'):
            if(node.parent==node.parent.parent.left): #inserting on the left side
                uncle=node.parent.parent.right
                if(uncle.color=='RED'): #3m a7mr 
                    node.parent.color='BLACK'
                    uncle.color='BLACK'
                    node.parent.parent.color='RED'
                    node=node.parent.parent #to check if this recoloring will be made again
                else: #3m black
                    if (node==node.parent.right): #triangle case
                        node=node.parent
                        self.rotate_left(node)
                    #performing line case
                    node.parent.color='BLACK'
                    node.parent.parent.color='RED'
                    self.rotate_right(node.parent.parent)

            else:   #inserting on the right side
                uncle=node.parent.parent.left
                if(uncle.color=='RED'):
                    node.parent.color='BLACK'
                    uncle.color='BLACK'
                    node.parent.parent.color='RED'
                    node=node.parent.parent #to check if this recoloring will be made again
                else:
                    if(node==node.parent.left): #triangle
                        node=node.parent
                        self.rotate_right(node)
                    #line case
                    node.parent.color='BLACK'
                    node.parent.parent.color='RED'
                    self.rotate_left(node.parent.parent)
        self.root.color='BLACK'
    

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y


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


if __name__ == "__main__":
    tree = RBT()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(1)
    tree.insert(7)
    tree.insert(12)
    tree.insert(18)
    print(tree.root.right.right.color)
    print(tree.root.color)
    print(tree.root.left.right.color)
    print("Tree created successfully!")



        

   


        

