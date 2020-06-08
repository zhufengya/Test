package javatest;

import java.util.*;

public class Complex{
    
    public boolean isValidMask(String word)  
    {
        try
        {
            String[] wp = word.split("\\.");
            int summ = 0;
            if(wp.length != 4 || Integer.valueOf(wp[0]) == 0 || Integer.valueOf(wp[3]) == 255) //0.0.0.0 和255.255.255.255为无效掩码。
                return false;
            for(int i=0; i < 4; i++)
            {
                summ += Integer.valueOf(wp[i]) << (24 - 8 * i);
            }
            if((summ | (summ-1)) == -1)   //判断掩码最简单方式！进行按位异或操作。
                return true;
            else
                return false;
        }
        catch(Exception e)
        {
            return false;
        }
    }
    
    public char ipClass(String ip)
    {
       try
        {
            String[] iplist = ip.split("\\.");
            if(iplist.length != 4)
                return 'r';
            if(Integer.valueOf(iplist[0]) == 10)
                return '1';
            else if(Integer.valueOf(iplist[0]) == 172 && Integer.valueOf(iplist[1]) >= 16 && Integer.valueOf(iplist[1])<32)
                return '2';
            else if(Integer.valueOf(iplist[0]) == 192 && Integer.valueOf(iplist[1]) == 168)
               return '3';
            else if(Integer.valueOf(iplist[0]) >= 1 && Integer.valueOf(iplist[0]) < 127)
                return 'a';
            else if(Integer.valueOf(iplist[0]) >= 128 && Integer.valueOf(iplist[0]) < 192)
                return 'b';
           else if(Integer.valueOf(iplist[0]) >= 192 && Integer.valueOf(iplist[0]) < 224)
                return 'c';
           else if(Integer.valueOf(iplist[0]) >= 224 && Integer.valueOf(iplist[0]) < 240)
                return 'd';
           else if(Integer.valueOf(iplist[0]) >= 240 && Integer.valueOf(iplist[0]) < 256)
                return 'e';
           else
                return 'i';
        }
        catch(Exception e)
        {
            return 'r';
        }
    }
    
    public void main(){
        int a= 0, b= 0, c= 0, d = 0, e = 0, err = 0, p = 0;
        Scanner scan = new Scanner(System.in);
        while(scan.hasNext())
        {
            String s = scan.nextLine();
            String[] sp = s.split("\\~");
            if(isValidMask(sp[1]))
            {
                if(ipClass(sp[0]) == '1')
                {
                    a += 1;
                    p += 1;
                }
                else if(ipClass(sp[0]) == '2')
                {
                    b += 1;
                    p += 1;
                }
                else if(ipClass(sp[0]) == '3')
                {
                    c += 1;
                    p += 1;
                }
                else if (ipClass(sp[0]) == 'a')
                    a += 1;
                else if (ipClass(sp[0]) == 'b')
                    b += 1;
                else if (ipClass(sp[0]) == 'c')
                    c += 1;
                else if (ipClass(sp[0]) == 'd')
                    d += 1;
                else if (ipClass(sp[0]) == 'e')
                    e += 1;
                else if (ipClass(sp[0]) == 'r')
                    err += 1;
            }
            else
                err += 1;
        }
       System.out.println(a + " "+b+" "+c+" "+d+" "+e+" "+err+" "+p);
       scan.close();
    }
    
    
    public boolean isValidMask1(String word)
    {
        try
        {
            String[] wp = word.split("\\.");
            String code = "";
            for(String w:wp)
            {
                String temp = Integer.toBinaryString(Integer.valueOf(w));
                for(int i=0; i< 8 - temp.length();i++)
                    temp = "0" + temp;
                code += temp;
            }
            String mask = "(1+0+)";
            return code.matches(mask);
        }
        catch(Exception e)
        {
            return false;
        }
        //return true;
    }
   // 空格空格空格！！！！写匹配字符串注意空格！！！多余的空格也会被编译到匹配模式里面的！！！
    static String tmp2 = "(\\.((\\d)|([1-9]\\d)|(1\\d\\d)|(2[0-4]\\d)|((25)[0-5]))){2}";
    static String tmp3 = "(\\.((\\d)|([1-9]\\d)|(1\\d\\d)|(2[0-4]\\d)|((25)[0-5]))){3}";
    static String typea = "(([1-9])|([1-9]\\d)|([1][0-1]\\d)|(12[0-6]))" + tmp3;
    static String typeb = "((12[89])|(1[3-8]\\d)|(19[01]))" + tmp3;
    static String typec = "((19[2-9])|(2[01]\\d)|(22[0-3]))" + tmp3;
    static String typed = "((22[4-9])|(23\\d))" + tmp3;
    static String typee = "((24\\d)|(25[0-5]))" + tmp3;
    static String p1 = "10" + tmp3;
    static String p2 ="172\\.((1[6-9])|(2\\d)|(3[01]))" +tmp2;
    static String p3 = "192\\.168" + tmp2;
    static String ig = "([0]|(127))"+ tmp3;

    
    public void main1(){
        int a= 0, b= 0, c= 0, d = 0, e = 0, err = 0, p = 0;
        Scanner scan = new Scanner(System.in);
        while(scan.hasNext())
        {
            String s = scan.nextLine();
            String[] sp = s.split("\\~");
            if(isValidMask1(sp[1]))
            {
                String ip = sp[0];
        if(ip.matches(p1))
        {
            a ++;
            p ++;
        }
        else if(ip.matches(p2))
        {
            b ++;
            p ++;
        }
        else if(ip.matches(p3))
        {
            c ++;
            p ++;
        }
        else if(ip.matches(typea))
            a ++;
         else if(ip.matches(typeb))
            b ++;
         else if(ip.matches(typec))
            c ++;
         else if(ip.matches(typed))
            d ++;
         else if(ip.matches(typee))
            e ++;
         else if(ip.matches(ig))
            e += 0;
         else
             err ++;
        }
        else
            err ++;
        }
       System.out.println(a + " "+b+" "+c+" "+d+" "+e+" "+err+" "+p);
       scan.close();
    }
//数据分类处理    TreeSet排序去重利器！！！
    public void dataProcess(){
        Scanner scan = new Scanner(System.in);
        while(scan.hasNext())
        {
            scan.nextInt();
            String si = scan.nextLine().trim();
            scan.nextInt();
            String sr = scan.nextLine().trim();
            String[] iarr = si.split("\\ ");
            String[] rarr = sr.split("\\ ");
            Set<Integer> set = new TreeSet<Integer>();
            for(String rach:rarr)
            {
                int ele = Integer.valueOf(rach);
                set.add(ele);
            }
            String fin = "";
            int num = 0;
            for(int ele: set)
            {
                String re = "";
                int cunt = 0;
                for(int i=0; i < iarr.length; i++)
                {
                    if(iarr[i].contains(String.valueOf(ele)))
                    {
                        re += i + " ";
                        re += iarr[i] + " ";
                        cunt += 1;
                    }
                }
                if(cunt !=0)
                {
                    fin =fin + ele + " " + cunt + " " + re;
                    num += 2 + cunt * 2;
                }
            }
            fin = num +" " + fin;
            System.out.println(fin);
        }
        scan.close();
    }

    public static void main(String[] args)
    {
        Complex ma = new Complex();
        //ma.main();
        ma.dataProcess();
        
        
    }
}