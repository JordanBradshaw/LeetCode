package Fundamentals.codeSignal.dynamicProgramming;

public class q1climbingStairs {
    public static int climbingStairs(int n){
        if (n == 1) return 1;
        if (n == 2) return 2;

        return climbingStairs(n-1) + climbingStairs(n - 2);
    }
    public static void main(String[] args){
        climbingStairs(4);
    }
    
}
