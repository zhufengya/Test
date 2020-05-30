package javatest;
import java.util.*;

public class Main{
    /* 求字符串最后一个单词的长度 */
    public void worldLength()
    {
        Scanner s = new Scanner(System.in);
        while(s.hasNext()){   //多组测试用例
            String ipt = s.nextLine();
            String[] sp = ipt.split("\\ ");
            System.out.println(sp[sp.length-1].length()); //数组求长度用length属性，对象求长度用length()方法。
        }
        s.close();
    }
    //计算字符个数
    /*String转char，1.可以使用str.charAt()方法；   2.可以使用str.toCharArray()方法返回字符数组；
      char转String: 1.String.valueOf(ch);  2. String s = ch + ""类型转换成String.
    */
    public void wordCunt()
    {
        Scanner s1 = new Scanner(System.in);
        while(s1.hasNext())
        {
            String ipt = s1.nextLine();
            String ch = s1.nextLine();
            int cunt = 0;
            // char[] ip = ipt.toCharArray();  //不能直接对String进行索引，转化成字符数组！！
            // for(char c: ip)
            // {
            //     if(ch.equalsIgnoreCase(String.valueOf(c)))   //将char转换成String!!!同类型才能equals！！！
            //         cunt += 1;
            // }
            for(int i =0; i< ipt.length();i++)
            {
                if(ipt.charAt(i) == ch.charAt(0))
                    cunt += 1;
            }
            System.out.println(cunt);     
        }
        s1.close();
    }
    /*明明的随机数，对一组数进行去重排序；

    */
    public void mingMing()
    {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNext()){
            int n = sc.nextInt();
            int[] arr = new int[n];
            for(int i=0; i <n;i++)
            {
                arr[i] = sc.nextInt();
            }
            Arrays.sort(arr);      //数组排序，在原数组基础上进行排序。
            for(int i=0;i<n-1;i++)
            {
                if(arr[i+1] != arr[i])
                    System.out.println(arr[i]);
            }
            System.out.println(arr[n-1]);
        }
        sc.close();
    }
   //采用计数排序的思想！！先对输入数据进行标记。
    public void mingMing1()
    {
        Scanner sc = new Scanner(System.in);
        int[] flag = new int[1000];
        while(sc.hasNext()){
            for(int i=0;i<1000; i++)
                flag[i] = 0;
            int n = sc.nextInt();
            for(int i=0; i <n;i++)
            {
                flag[sc.nextInt()]=1;
            }
            for(int i=0;i<1000;i++)
            {
                if(flag[i]==1)
                    System.out.println(i);
            }

        }
        sc.close();
    }
    //字符串分隔！  求一个字符串的子串 str.substring().
    public void strSplit(){
        Scanner scan = new Scanner(System.in);
        while(scan.hasNext())
        {
            String input = scan.nextLine();
            int len = input.length();
            StringBuilder sb = new StringBuilder();
            if(len <= 8)
            {
                sb.append(input);
                for(int i=0; i< 8- len;i++)
                    sb.append("0");
                System.out.println(sb.toString());
            }
            else{
                int i = 0;
                for(i = 0; i< (int)(len/8); i++)
                    System.out.println(input.substring(i*8, (i+1)*8));
                if(len % 8 !=0)
                {
                    sb.append(input.substring(i*8,len));
                    for(int j=0; j< 8*(i+1) - len;j++)
                        sb.append("0");
                    System.out.println(sb.toString());
                }
            }
        }
        scan.close();
    }

    public void strSplit1()    //太机智了==
    {
        Scanner scan = new Scanner(System.in);
        while(scan.hasNext())
        {
            String input = scan.nextLine();
            if(input.length() %8 !=0)
                input = input + "00000000";
            while(input.length()>=8)
            {
                System.out.println(input.substring(0, 8));
                input = input.substring(8);
            }

        }
        scan.close();
    }
/* 进制转换：十六进制转十进制。
     n进制转十进制:Integer.parseInt(String a, int b)    b为要转换成的进制。
     十进制转n进制：Integer.toBinaryString(int a)  
*/
    public void hextoint()
    {
        Scanner scan = new Scanner(System.in);
        while(scan.hasNext()){
            String sc = scan.nextLine();
            System.out.println(Integer.parseInt(sc.substring(2),16));    //parseInt函数不能识别十六进制开头的0x!!!!
        }
        scan.close();
    }

    public void hextoint2()
    {
        Scanner scan = new Scanner(System.in);
        while(scan.hasNext()){
            String sc = scan.nextLine().substring(2);
            int summ = 0;
            char[] scarr = sc.toCharArray();
            for(char le:scarr)
            {
                int b = switch(le){
                        case 'A' -> 10;
                        case 'B'->11;
                        case 'C'->12;
                        case 'D'->13;
                        case 'E'->14;
                        case 'F'->15;
                        default-> {
                            int c = Integer.valueOf(le)-48;    //char型变量转int型时得到的是该字符的ASCII码，String转int得到的就是该数值！
                            yield c;
                        }
                };
                summ = summ * 16 + b;
            }
            System.out.println(summ);
            
        }
        scan.close();
    }

    public void hextoint1()
    {
        Scanner scan = new Scanner(System.in);
        while(scan.hasNext()){
            String sc = scan.nextLine().substring(2);
            int summ = 0;
            char[] scarr = sc.toCharArray();
            for(char le:scarr)
            {
                int b = 0;
                //与c语言一样，java支持字符之间直接进行加减或大小比较。
                if(le >= 'A' && le <= 'F')
                    b = le - 'A' + 10;
                else if(le >= 'a' && le <= 'f')
                    b = le - 'a' + 10;
                else
                    b = le -'0';                    
                summ = summ * 16 + b;
            }
            System.out.println(summ);
        }
        scan.close();
    }

    public boolean isPrime(long n)
    {
        int i = 2;
        while(i*i<=n)
        {
            if (n % i == 0)
            {
                return false;
            }
            else{
                i = i + 1;
            }
        }
        return true;
    }
    
    public void primeNumber(){
        Scanner scan = new Scanner(System.in);
        while(scan.hasNext())
        {
            long s = Integer.valueOf(scan.nextLine());
            if(isPrime(s)){
                System.out.println(s + " ");
                continue;
            }
            else{
                int i = 2;
                long t = s;
                while(i <= (int)t/2){
                    if(s % i == 0){
                        System.out.print(i + " ");
                        s = s/i;
                        if(s == 1)
                          break;
                    }
                    else{
                        i = i + 1;
                    }
                }
            }
        }
        scan.close();
    }

    public void rond()
    {
        Scanner scan = new Scanner(System.in);
        while(scan.hasNext())
        {
            double s = Double.valueOf(scan.nextLine());
            System.out.println((int)(s+0.5));
        }
        scan.close();
    }
    
    public static void main(String[] args)
    {
        Main ma = new Main();
        // ma.worldLength();
        // ma.wordCunt();
        // ma.mingMing();
        // ma.mingMing1();
        // ma.strSplit();
        // ma.strSplit1();
        // ma.hextoint();
       // ma.hextoint2();
       //ma.hextoint1();
       ma.primeNumber();
      
       
         
    }
}