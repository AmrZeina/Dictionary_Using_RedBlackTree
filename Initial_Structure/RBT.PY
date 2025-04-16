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
            self.insert_recursive(self,self.root,node)
            
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
        pass
    
    def print_tree_height(self):
        pass

    def print_black_height(self):
        pass


        

