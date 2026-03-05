public class Main 
{

    public static void main(String[] args) 
    {
        TreeRegistry.load(); // Load the tree registry with predefined trees
        System.out.println("Available trees: " + Tree.getTreeNames()); // Print the names of available trees
        System.out.println("Enter the name of the tree to traverse: " + args[0]); // Prompt the user to enter the name of the tree to traverse
        Tree myTree = Tree.getTree(args[0]); // Get a tree by its name from the registry
        if (myTree != null) 
        {
            System.out.println("Inorder traversal of " + args[0] + ":");
            myTree.inorder(); // Perform an inorder traversal of the tree
        } 
        else 
        {
            System.out.println("Tree not found.");
        }
    }
}