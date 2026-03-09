
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public abstract class Tree 
{
    /**
     * This class represents and houses helper methods to construct a Binary Search Tree (BST).
     * Helper methods include inserting values, traversing the tree, retrieving nodes based on specific criteria, and other operations.
     * The class also maintains a static list of trees that can be accessed by name, allowing for multiple trees to be managed simultaneously.
     */

    //---------------------- Fields ----------------------//
    public static final Map<String, Tree> list = new HashMap<>();
    public static final int MAX = 100;
    public TreeNode root;

    //---------------------- Constructors ----------------------//
    public Tree(ArrayList<Integer> arr) // Constructor to initialize the tree with an array of integers 
    {
        for (int value : arr) 
        {
            root = insertNodeRec(root, value);
        }
    }
    
    public class TreeNode // Inner class to represent a node in the tree
    {

        int value;
        TreeNode left, right;

        public TreeNode(int item) 
        {
            value = item;
            left = right = null;
        }
    }

    //---------------------- Core Functions ----------------------//
    public static void load(String name, ArrayList<Integer> arr) // Static method to load a tree with a given name and an array of integers
    {
        Tree tree = new Tree(arr) {};
        list.put(name, tree);
    }

    public void insertValue(int value) // Method to insert a value into the tree
    {
        root = insertNodeRec(root, value);
    }

    private TreeNode insertNodeRec(TreeNode root, int value) // Helper method to insert a value into the tree recursively
    {
        if (root == null) 
        {
            root = new TreeNode(value);
            return root;
        }

        if (value < root.value) root.left = insertNodeRec(root.left, value);
        else if (value > root.value) root.right = insertNodeRec(root.right, value);

        return root;
    }

    public Tree deleteNode(int value) // Method to delete a node with a specific value from the tree
    {
        root = deleteNodeRec(root, value);
        return this;
    }

    public TreeNode deleteNodeRec(TreeNode root, int value) // Helper method to delete a node with a specific value from the tree recursively
    {
        if (root == null) 
        {
            return root;
        }

        if (value < root.value) 
        {
            root.left = deleteNodeRec(root.left, value);
        } 
        else if (value > root.value) 
        {
            root.right = deleteNodeRec(root.right, value);
        } 
        else 
        {
            if (root.left == null) 
            {
                return root.right;
            } 
            else if (root.right == null) 
            {
                return root.left;
            }

            root.value = traverseRightMax().value; // Get the maximum value from the left subtree
            root.left = deleteNodeRec(root.left, root.value); // Delete the duplicate value from the left subtree
        }
        return root;
    }

    public void inorder() // Method to perform an inorder traversal of the tree
    {
        inorderRec(root);
    }

    public void inorderRec(TreeNode root) // Helper method to perform an inorder traversal of the tree recursively
    {
        if (root != null) 
        {
            inorderRec(root.left);
            System.out.print(root.value + " ");
            inorderRec(root.right);
        }
    }

    public boolean contains(int value) // Method to check if a value exists in the tree
    {
        return traverse(value) != null;
    }

    public Tree copyTree() // Method to create a copy of the tree via deep copying the nodes
    {
        Tree newTree = new Tree(new ArrayList<>()) {};
        newTree.setRoot(copyNode(root));
        return newTree;
    }

    public TreeNode copyNode(TreeNode node) // Helper method to copy a node and its children recursively for deep copying the tree
    {
        if (node == null) 
        {
            return null;
        }
        TreeNode newNode = new TreeNode(node.value);
        newNode.left = copyNode(node.left);
        newNode.right = copyNode(node.right);
        return newNode;
    }

    public TreeNode traverse(int value) // Method to traverse the tree to find a node with a specific value {"contains" similar}
    {
        TreeNode current = root;
        while (current != null) 
        {
            if (value < current.value) 
            {
                current = current.left;
            } 
            else if (value > current.value) 
            {
                current = current.right;
            } 
            else 
            {
                return current; // Value found
            }
        }
        return null; // Value not found
    }

    public TreeNode traverseRight(TreeNode node) // Method to traverse the tree to find the child node with height less than the current
    {
        return node.right;
    }

    public TreeNode traverseLeft(TreeNode node) // Method to traverse the tree to find the child node with height less than the current
    {
        return node.left;
    }

    public TreeNode traverseRightMax() // Method to traverse the tree to find the node with the maximum value
    {
        TreeNode current = root;
        while (current != null && current.right != null) 
        {
            current = current.right;
        }
        return current; // Node with maximum value
    }

    public TreeNode traverseLeftMin() // Method to traverse the tree to find the node with the minimum value
    {
        TreeNode current = root;
        while (current != null && current.left != null) 
        {
            current = current.left;
        }
        return current; // Node with minimum value
    }

    //---------------------- Getters and Setters ----------------------//
    public TreeNode getRoot() // Method to get the root of the tree
    {
        return root;
    }

    public void setRoot(TreeNode root) // Method to set the root of the tree
    {
        this.root = root;
    }

    public int getMax() // Method to get the maximum value allowed in the tree
    {
        return MAX;
    }

    public static Tree getTree(String name) // Method to get a tree by its name from the list of trees
    {
        return list.get(name);
    }

    public static ArrayList<String> getTreeNames() // Method to get the names of all available trees in the list
    {
        return new ArrayList<>(list.keySet());
    }

    public TreeNode getNode(int value) // Method to get a node by its value from the tree
    {
        return traverse(value);
    }

    public TreeNode getMaxNode() // Method to get the node with the maximum value in the tree
    {
        return traverseRightMax();
    }

    public TreeNode getMinNode() // Method to get the node with the minimum value in the tree
    {
        return traverseLeftMin();
    }
    
    public Tree getSubtree(int value) // Method to get a subtree rooted at a node with a specific value 
    {
        TreeNode node = traverse(value);
        if (node != null) 
        {
            Tree subtree = new Tree(new ArrayList<>()) {};
            subtree.setRoot(node);
            return subtree;
        }
        return null; // Value not found
    }

    public Tree getLeftSubtree(int value) // Method to get the left subtree of a node with a specific value 
    {
        TreeNode node = traverse(value);
        if (node != null && node.left != null) 
        {
            Tree subtree = new Tree(new ArrayList<>()) {};
            subtree.setRoot(node.left);
            return subtree;
        }
        return null; // Value not found or no left subtree
    }

    public Tree getRightSubtree(int value) // Method to get the right subtree of a node with a specific value
    {
        TreeNode node = traverse(value);
        if (node != null && node.right != null) 
        {
            Tree subtree = new Tree(new ArrayList<>()) {};
            subtree.setRoot(node.right);
            return subtree;
        }
        return null; // Value not found or no right subtree
    }
    
    //---------------------- Miscellaneous Methods ----------------------//

    public TreeNode findLowestCommonAncestor(int value1, int value2) // Method to find the lowest common ancestor of two values in the tree
    {
        return findLCARec(root, value1, value2);
    }

    private TreeNode findLCARec(TreeNode node, int value1, int value2) // Helper method to find the lowest common ancestor recursively
    {
        if (node == null) 
        {
            return null;
        }

        if (value1 < node.value && value2 < node.value) 
        {
            return findLCARec(node.left, value1, value2);
        }

        if (value1 > node.value && value2 > node.value) 
        {
            return findLCARec(node.right, value1, value2);
        }

        return node; // This is the lowest common ancestor
    }

    public TreeNode findGreatestCommonAncestor(int value1, int value2) // Method to find the greatest common ancestor of two values in the tree
    {
        return findGCARec(root, value1, value2);
    }

    private TreeNode findGCARec(TreeNode node, int value1, int value2) // Helper method to find the greatest common ancestor recursively
    {
        if (node == null) 
        {
            return null;
        }

        if (value1 < node.value && value2 < node.value) 
        {
            return findGCARec(node.left, value1, value2);
        }

        if (value1 > node.value && value2 > node.value) 
        {
            return findGCARec(node.right, value1, value2);
        }

        return node; // Return GCA
    }

    public Tree mergeTrees(Tree other) // Method to merge another tree into the current tree
    {
        Tree mergedTree = new Tree(new ArrayList<>()) {};
        mergeNodes(this.root, mergedTree);
        mergeNodes(other.root, mergedTree);
        return mergedTree;
    }

    private void mergeNodes(TreeNode node, Tree mergedTree) // Helper method to merge nodes from another tree into the merged tree recursively
    {
        if (node != null) 
        {
            mergedTree.insertValue(node.value);
            mergeNodes(node.left, mergedTree);
            mergeNodes(node.right, mergedTree);
        }
    }

}