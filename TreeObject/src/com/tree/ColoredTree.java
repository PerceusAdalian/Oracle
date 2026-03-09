/**
 * Colored Tree Implementation in Java
 * This class represents a colored tree data structure where each node can have a color and multiple children.
 * The tree supports operations such as adding children, changing colors, and traversing the tree.
 * Extends the basic TreeNode class to include color properties and methods for managing colors.
 */

import java.util.ArrayList;
import java.util.HashMap;

public class ColoredTree extends Tree
{
    private final HashMap<TreeNode, String> colorMap; // Map to store the color of each node
    
    //---------------------- Constructors ----------------------//
    public ColoredTree(ArrayList<Integer> arr) // Constructor to initialize the colored tree with an array of integers
    {
        super(arr); // Call the constructor of the base Tree class
        colorMap = new HashMap<>(); // Initialize the color map
    }
    
    //---------------------- Color Management Functions ----------------------//
    public void setColor(TreeNode node, String color) // Method to set the color of a specific node
    {
        if (node != null) 
        {
            colorMap.put(node, color);
        }
    }
    
    public String getColor(TreeNode node) // Method to get the color of a specific node
    {
        return colorMap.getOrDefault(node, "No Color");
    }
    
    public void changeColor(TreeNode node, String newColor) // Method to change the color of a specific node
    {
        if (node != null && colorMap.containsKey(node)) 
        {
            colorMap.put(node, newColor);
        }
    }
    
    public void printColoredTree() // Method to print the tree with colors (for demonstration purposes)
    {
        printColoredNode(root, 0);
    }
    
    public void printColoredNode(TreeNode node, int level) // Helper method to print a node and its children with indentation
    {
        if (node != null) 
        {
            String color = getColor(node);
            System.out.println(" ".repeat(level * 2) + "Node Value: " + node.value + ", Color: " + color);
            printColoredNode(node.left, level + 1); // Print left child
            printColoredNode(node.right, level + 1); // Print right child
        }
    }

    public Tree copyColoredTree() // Method to create a copy of the colored tree via deep copying the nodes and colors
    {
        ColoredTree newTree = new ColoredTree(new ArrayList<>()); // Create a new instance of ColoredTree
        newTree.setRoot(copyNode(root)); // Copy the structure of the tree
        copyColors(root, newTree); // Copy the colors of the nodes
        return newTree;
    }

    public void copyColors(TreeNode originalNode, ColoredTree newTree) // Helper method to copy colors from the original tree to the new tree
    {
        if (originalNode != null) 
        {
            String color = getColor(originalNode);
            TreeNode newNode = newTree.findNode(newTree.getRoot(), originalNode.value); // Find the corresponding node in the new tree
            if (newNode != null) 
            {
                newTree.setColor(newNode, color); // Set the color of the corresponding node in the new tree
            }
            copyColors(originalNode.left, newTree); // Copy colors for left child
            copyColors(originalNode.right, newTree); // Copy colors for right child
        }
    }

    public TreeNode findNode(TreeNode node, int value) // Helper method to find a node with a specific value in the tree
    {
        if (node == null) 
        {
            return null;
        }
        if (node.value == value) 
        {
            return node;
        }
        TreeNode leftResult = findNode(node.left, value); // Search in left subtree
        return (leftResult != null) ? leftResult : findNode(node.right, value); // Search in right subtree if not found in left
    }

    public ColoredTree mergeColoredTrees(ColoredTree other) // Method to merge another colored tree into the current tree
    {
        ColoredTree mergedTree = new ColoredTree(new ArrayList<>()); // Create a new instance of ColoredTree for the merged tree
        mergeNodes(this.root, mergedTree); // Merge nodes from the current tree
        mergeNodes(other.root, mergedTree); // Merge nodes from the other tree
        copyColors(this.root, mergedTree); // Copy colors from the current tree
        copyColors(other.root, mergedTree); // Copy colors from the other tree
        return mergedTree;
    }

    public TreeNode mergeNodes(TreeNode node, ColoredTree mergedTree) // Helper method to merge nodes from a tree into the merged tree
    {
        if (node != null) 
        {
            mergedTree.addNode(node.value); // Add the node value to the merged tree
            mergeNodes(node.left, mergedTree); // Merge left child
            mergeNodes(node.right, mergedTree); // Merge right child
        }
        return null; // Return null as this method is used for side effects (merging nodes)
    }

    public void addNode(int value) // Method to add a node with a specific value to the tree (for demonstration purposes)
    {
        TreeNode newNode = new TreeNode(value); // Create a new node with the given value
        if (root == null) 
        {
            root = newNode; // If the tree is empty, set the new node as the root
        } 
        else 
        {
            addColoredNodeRec(root, newNode); // Otherwise, add the node recursively
        }
    }

    public void addColoredNodeRec(TreeNode current, TreeNode newNode) // Helper method to add a node to the tree recursively
    {
        if (newNode.value < current.value) 
        {
            if (current.left == null) 
            {
                current.left = newNode; // Add as left child if the value is smaller
            } 
            else 
            {
                addColoredNodeRec(current.left, newNode); // Recur on the left subtree
            }
        } 
        else 
        {
            if (current.right == null) 
            {
                current.right = newNode; // Add as right child if the value is larger
            } 
            else 
            {
                addColoredNodeRec(current.right, newNode); // Recur on the right subtree
            }
        }
    }

    public ColoredTree deleteColoredNode(int value) // Method to delete a node with a specific value from the colored tree
    {
        root = deleteNodeRec(root, value); // Call the recursive delete method
        colorMap.remove(findNode(root, value)); // Remove the color mapping for the deleted node
        return this; // Return the current instance of ColoredTree after deletion
    }

    public ColoredTree changeNodeColor(int value, String newColor) // Method to change the color of a node with a specific value
    {
        TreeNode node = findNode(root, value); // Find the node with the given value
        if (node != null) 
        {
            changeColor(node, newColor); // Change the color of the found node
        }
        return this; // Return the current instance of ColoredTree after changing the color
    }

    public void printInorderColored() // Method to perform an inorder traversal of the tree and print nodes with their colors
    {
        printInorderColoredRec(root); // Call the recursive helper method for inorder traversal
    }

    public void printInorderColoredRec(TreeNode node) // Helper method to perform an inorder traversal and print nodes with their colors recursively
    {
        if (node != null) 
        {
            printInorderColoredRec(node.left); // Traverse left subtree
            String color = getColor(node); // Get the color of the current node
            System.out.println("Node Value: " + node.value + ", Color: " + color); // Print the node value and its color
            printInorderColoredRec(node.right); // Traverse right subtree
        }
    }
    
    public ColoredTree buildTree()
    {
        // Builds the tree based on initialization of values in the constructor and sets default colors for each node (red/black)
        setColor(root, "Red"); // Set the color of the root node to red
        setColor(root.left, "Black"); // Set the color of the left child of the root node to black
        setColor(root.right, "Black"); // Set the color of the right child of the root node to black
    
        return this; // Return the current instance of ColoredTree after building the tree
    }
}