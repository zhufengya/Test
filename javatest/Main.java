package javatest;
import java.util.Scanner;
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
    }
    public static void main(String[] args)
    {
        Main ma = new Main();
        ma.worldLength();
        ma.wordCunt();
    }
}