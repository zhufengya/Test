package javatest;
import java.util.*;

public class Dp {

    //购物单！01背包问题==难==只能写这么复杂了==
    public void shoppingList() {
        Scanner scan = new Scanner(System.in);
        while (scan.hasNext()) {
            int N = scan.nextInt();
            N = N/10;
            int m = scan.nextInt();
            int[][] price = new int[m][3];
            int[][] value = new int[m][3];
            int flag = 0,pri = 0, v = 0;
            for(int i = 0; i < m; i++)
            {
               pri = scan.nextInt()/10;
               v = scan.nextInt();
               flag = scan.nextInt();
               if(flag == 0){
                price[i][0] = pri;
                value[i][0] = v * pri;
                }
                else if(price[flag-1][1] == 0)
                {
                price[flag-1][1] = pri;
                value[flag-1][1] = v * pri; 
                }
                else
                {
                price[flag-1][2] = pri;
                value[flag-1][2] = v * pri;
                }
            }
            int[] dp = new int[N+1];
            for(int i = 0; i< m; i++)
            {
                if(price[i][0] == 0)
                    continue;
                for(int j =N; j >0; j--)
                {
                    if(j >= price[i][0])
                        dp[j] = Math.max(dp[j], dp[j-price[i][0]] + value[i][0]);
                    if(j >= price[i][0] + price[i][1])
                        dp[j] = Math.max(dp[j], dp[j-price[i][0]-price[i][1]] + value[i][0] + value[i][1]);
                    if(j >= price[i][0] + price[i][2])
                        dp[j] = Math.max(dp[j], dp[j-price[i][0]-price[i][2]] + value[i][0] + value[i][2]);
                    if(j >= price[i][0] + price[i][1] + price[i][2])
                        dp[j] = Math.max(dp[j], dp[j-price[i][0]-price[i][1]-price[i][2]] + value[i][0]+value[i][1] + value[i][2]);
                }
            }
            System.out.println(dp[N] * 10);
        }
        scan.close();
    }
//合唱队，找一个序列的最大递增子序列（可以是不连续的）动态规划可真难==只能写成这辣鸡样儿了。
       public int[] maxx(int[] ar)
       {
           int[] temp = new int[ar.length];
           for(int i=0; i< ar.length; i++)
               temp[i] = 0;
           for(int i=0; i<ar.length; i++)
           {
               for(int j=i-1; j>=0; j--)
               {
                   if(ar[i] > ar[j] && temp[i] < temp[j] + 1)
                       temp[i] = temp[j] + 1;
               }
           }
           return temp;
       }
       public void heChang(){
           Scanner s = new Scanner(System.in);
           while(s.hasNext())
           {
               int n = s.nextInt();
               int[] arr = new int[n];
               int[] arr1 = new int[n];
               for(int i =0; i<n; i++)
               {
                   arr[i] = s.nextInt();
                   arr1[n-i-1] = arr[i];
               }
               arr = maxx(arr);
               arr1 = maxx(arr1);
               int maximum = arr[0] + arr1[n-1];
               for(int i = 1; i < n; i++)
               {
                   if(arr[i] + arr1[n-i-1] > maximum)
                       maximum = arr[i] + arr1[n-i-1];
               }
               System.out.println(n - maximum -1);
           }
           s.close();
       }

    public static void main(String[] args) {
        Dp p = new Dp();
        p.shoppingList();
        p.heChang();
    }
    
}