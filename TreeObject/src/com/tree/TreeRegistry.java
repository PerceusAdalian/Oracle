import java.util.ArrayList;
import java.util.Arrays;

public class TreeRegistry 
{
    public static void load()
    {
        Tree.load("myTree_1", new ArrayList<>(Arrays.asList(5, 3, 7, 2, 4, 6, 8)));
        Tree.load("myTree_2", new ArrayList<>(Arrays.asList(1, 9, 0, 5, 3, 7, 2)));
        Tree.load("myTree_3", new ArrayList<>(Arrays.asList(10, 5, 15, 3, 7, 13, 17)));
        Tree.load("myTree_4", new ArrayList<>(Arrays.asList(20, 10, 30, 5, 15, 25, 35)));

        ColoredTree coloredTree = new ColoredTree(new ArrayList<>(Arrays.asList(5, 3, 7, 2, 4, 6, 8)));
        Tree.list.put("myTree_colored", coloredTree.buildTree());
    }
}