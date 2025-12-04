package 每日打卡.Day_2;
import java.util.Scanner;

public class Main {
    public static void main(String [] args){
        Scanner sc = new Scanner( System.in ); 
        int n = sc.nextInt(), m = sc.nextInt();
        int[][] grid = new int[n][m];
        int total = 0;
        
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                grid[i][j] = sc.nextInt();
                total += grid[i][j];
            }
        }

        int minDiff = Integer.MAX_VALUE; 

        // 横切：
        int rowSum = 0; 
        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < m; j++){
                rowSum += grid[i][j];
            }
            int diff = Math.abs(total - 2 * rowSum);
            minDiff = Math.min(minDiff, diff); 
        }

        // 竖切：
        int colSum = 0;
        for (int j = 0; j < m; j++) {
            for (int i = 0; i < n; i++){
                colSum += grid[i][j];
            }
            int diff = Math.abs(total - 2 * colSum);
            minDiff = Math.min(minDiff, diff);
        }

        System.out.println(minDiff);


    }
}