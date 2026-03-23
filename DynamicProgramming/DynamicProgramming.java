// Dynamic Programming Examples in Java

class DynamicProgramming 
{

    // Fibonacci using Dynamic Programming (Memoization)
    public static int fibonacci(int n, int[] memo) 
    {
        // Base Cases
        if (n <= 1) return n;
        if (memo[n] != -1) return memo[n];
        
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
        
        return memo[n];
    }

    // Fibonacci using Dynamic Programming (Tabulation) - Iterative Approach
    public static int fibonacciTabulation(int n) 
    {
        if (n <= 1) return n; // Base Cases
        
        int[] dp = new int[n + 1];
        dp[0] = 0;
        dp[1] = 1;
        
        for (int i = 2; i <= n; i++) 
        {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        return dp[n];
    }

    // Longest Common Subsequence - length of the longest subsequence present in both strings
    public static int longestCommonSubsequence(String s1, String s2) 
    {
        int m = s1.length();
        int n = s2.length();
        int[][] dp = new int[m + 1][n + 1];

        for (int i = 1; i <= m; i++) 
        {
            for (int j = 1; j <= n; j++) 
            {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) 
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                else 
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }

        return dp[m][n];
    }

    // Assembler Problem (similar to Fibonacci) - number of ways to assemble a product with n parts
    public static int assembler(int n) 
    {
        if (n <= 1) return n; // Base Cases
        
        int[] dp = new int[n + 1];
        dp[0] = 0;
        dp[1] = 1;
        
        for (int i = 2; i <= n; i++) 
        {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        return dp[n];
    }

    // Coin Change Problem - number of ways to make change for a given amount using given denominations
    public static int coinChange(int[] coins, int amount) 
    {
        int[] dp = new int[amount + 1];
        dp[0] = 1; // Base Case: There's one way to make the amount 0 (using no coins)

        for (int coin : coins) 
        {
            for (int j = coin; j <= amount; j++) 
            {
                dp[j] += dp[j - coin];
            }
        }

        return dp[amount];
    }

    // Edit Distance (Levenshtein Distance) - minimum number of operations required to convert one string into another
    public static String editDistance(String s1, String s2) 
    {
        int m = s1.length();
        int n = s2.length();
        int[][] dp = new int[m + 1][n + 1]; // dp array to store edit distances

        for (int i = 0; i <= m; i++) 
            dp[i][0] = i; // Deletion cost
        for (int j = 0; j <= n; j++) 
            dp[0][j] = j; // Insertion cost

        for (int i = 1; i <= m; i++) 
        {
            for (int j = 1; j <= n; j++) 
            {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) 
                    dp[i][j] = dp[i - 1][j - 1]; // No operation needed
                else 
                    dp[i][j] = 1 + Math.min(dp[i - 1][j], // Deletion
                        Math.min(dp[i][j - 1], // Insertion
                        dp[i - 1][j - 1])); // Substitution
            }
        }

        return "Edit Distance: " + dp[m][n];
    }

    // Knapsack Problem - maximum value that can be put in a knapsack of given capacity
    public static int knapsack(int[] weights, int[] values, int capacity) 
    {
        int n = weights.length;
        int[][] dp = new int[n + 1][capacity + 1];

        for (int i = 0; i <= n; i++) 
        {
            for (int w = 0; w <= capacity; w++) 
            {
                if (i == 0 || w == 0) 
                    dp[i][w] = 0; // Base Case
                else if (weights[i - 1] <= w) 
                    dp[i][w] = Math.max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]);
                else 
                    dp[i][w] = dp[i - 1][w];
            }
        }

        return dp[n][capacity];
    }

    public static void main(String[] args) 
    {
        // Example usage of Fibonacci with Memoization
        int n = 10;
        int[] memo = new int[n + 1];
        for (int i = 0; i <= n; i++) 
        {
            memo[i] = -1;
        }
        System.out.println("Fibonacci of " + n + " is: " + fibonacci(n, memo));

        // Example usage of Fibonacci with Tabulation
        System.out.println("Fibonacci of " + n + " is: " + fibonacciTabulation(n));

        // Example usage of Longest Common Subsequence
        String s1 = "AGGTAB";
        String s2 = "GXTXAYB";
        System.out.println("Length of LCS is: " + longestCommonSubsequence(s1, s2));

        // Example usage of Coin Change        
        int[] coins = {1, 2, 3};
        int amount = 4;
        System.out.println("Number of ways to make change: " + coinChange(coins, amount));

        // Example usage of Edit Distance
        String str1 = "kitten";
        String str2 = "sitting";
        System.out.println(editDistance(str1, str2));

        // Example usage of Knapsack Problem
        int[] weights = {10, 20, 30};
        int[] values = {60, 100, 120};
        int capacity = 50;
        System.out.println("Maximum value in Knapsack: " + knapsack(weights, values, capacity));
    }
}