package javatest;
import java.util.*;
import java.util.regex.Pattern;

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
   // 求一个数的所有质数因子。
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
/*
Math.round():它表示四舍五入，算法为 Math.floor(x+0.5)，即将原来的数字加上 0.5 后再向下取整，所以，Math.round(11.5) 的结果为12，Math.round(-11.5) 的结果为-11。
Math.floor():地板值，返回小于等于（<=）给定参数的最大整数 。返回类型为双精度浮点型。
Math.ceil():天花板值，返回大于等于( >= )给定参数的的最小整数，返回类型为双精度浮点型。
*/
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
/*    对多条记录按照键值合并并排序！
      使用TreeMap数据结构！因为它是有序的！
*/
    public void mergeRecord(){
        Scanner scan = new Scanner(System.in);
        while(scan.hasNext())
        {
            int b = Integer.valueOf(scan.nextLine());
            Map<Integer,Integer> map = new TreeMap<>();
            for(int i=0; i< b; i++)
            {
                int key = scan.nextInt();
                int value = scan.nextInt();
                if(map.containsKey(key)){
                   int ori = map.get(key);
                   map.put(key, ori+value);
                }
                else
                    map.put(key, value);
            }
            for(int key:map.keySet())
            {
                int fin = map.get(key);
                System.out.println(key + " " + fin);
            }

        }
        scan.close();
    }
    //提取不重复的整数
    public void setint()
    {
        Scanner scan = new Scanner(System.in);
        while(scan.hasNext()){
            int s = scan.nextInt();
            int[] arr = new int[10];
            for(int i=0;i<10;i++)
                arr[i] = 0;
            while(s!=0)   //while只支持布尔类型判断
            {
                int mod = s % 10;
                if(arr[mod] == 0)   //不支持(!arr[mod])
                {
                    System.out.print(mod);
                    arr[mod] += 1;
                }
                s = s/10;
            }
        }
        scan.close();
    }
//字符个数统计，统计输入字符串中ascii码在0～127之间的不重复字符的个数
    public void charcunt()
    {
         Scanner scan = new Scanner(System.in);
        while(scan.hasNext()){
            String s = scan.nextLine();
            int[] flag = new int[128];
            int cunt = 0;
            for(int i=0; i<128;i++)
                flag[i] = 0;
            for(int i=0; i< s.length(); i++)
            {
                char ch = s.charAt(i);
                if(ch >= 0 && ch <= 127)
                {
                    if(flag[ch] == 0)
                    {
                        cunt += 1;
                        flag[ch] = 1;
                    }
                }
            }
            System.out.println(cunt);
        }
        scan.close();
    }
//数字颠倒
    public void strReverse()
    {
        Scanner s = new Scanner(System.in);
        while(s.hasNext())
        {
            String ipt = s.nextLine();
            // StringBuilder sb = new StringBuilder(ipt);
            // sb.reverse();
            // System.out.println(sb.toString());
            for(int i= ipt.length()-1; i >=0; i--)
            {
                System.out.print(ipt.charAt(i));
            }
        }
        s.close();
    }
//字符串反转
    public void senReverse()
    {
        Scanner s = new Scanner(System.in);
        while(s.hasNext())
        {
            String ipt = s.nextLine();
            String[] arr = ipt.split(" ");
            for(int i = arr.length-1; i >0; i--)
                System.out.print(arr[i] + " ");
            System.out.print(arr[0]);
        }
        s.close();
    }
//字串的连接最长路径查找
    public void strDic()
    {
        Scanner s = new Scanner(System.in);
        while(s.hasNext())
        {
            int ipt = Integer.valueOf(s.nextInt());   //s.nextInt()仅读取了整数值
            s.nextLine();   //把第一行的空格读取掉， 或者下面直接用s.next()。
            String[] sb = new String[ipt];
            for(int i=0; i < ipt; i ++)
            {
                sb[i] = s.nextLine();
            }
            Arrays.sort(sb);
            for(String st:sb)
            {
                System.out.println(st);
            }
        }
        s.close();
        List<Character> a = List.of('A','W');
        a.add('a');
        a.contains('a');
    }
 //求int型正整数在内存中存储时1的个数   
    public void int1()
    {
        Scanner s = new Scanner(System.in);
        while(s.hasNext())
        {
           int n = s.nextInt();
           int cunt = 0;
        //String s1 = Integer.toBinaryString(n);  将整数转化为对应进制的字符串。
           while(n!=0)
           {
               if(n % 2 == 1)
                   cunt +=1;
               n = n / 2;
           }
            System.out.println(cunt);
        }
        s.close();
        }
//坐标移动
        public boolean isValid(String word)
    {
        List<Character> list = List.of('A','W','D','S');
        if(word.length()>0 && list.contains(word.charAt(0)) && word.length()<=3)   //考虑分割后空字符串的情况
              {
                  for(int i =1; i< word.length(); i++)
                  {
                      if(word.charAt(i) >= '0' && word.charAt(i)<= '9')
                          continue;
                      else
                          return false;
                  }
                  return true;
              }
        else
              return false;
    }
    public void coordinate_move()
    {
        Scanner s = new Scanner(System.in);
        while(s.hasNext())
        {
          int x = 0, y=0;
          String ipt = s.nextLine();
          String[] arr = ipt.split("\\;");
          for(String ele:arr)
          {
              if(isValid(ele))
              {
                  int temp = Integer.valueOf(ele.substring(1));
                  char ch = ele.charAt(0);
                  switch(ch)
                  {
                          case 'A': x -=temp;break;
                          case 'D': x +=temp;break;
                          case 'W': y +=temp;break;
                          case 'S': y -=temp;break;
                  }
              }
          }
          System.out.println(x + "," + y);
          
        }
        s.close();
    }
//简单错误记录
    public void errorRecord(){
        Scanner scan = new Scanner(System.in);
        List<String> l = new ArrayList<>();
        Map<String, Integer> map = new HashMap<>();
        while(scan.hasNext())
        {
            String s = scan.nextLine();
            String[] s1 = s.split("\\\\");
            String[] re = s1[s1.length-1].split("\\s+");
            String record = "";
            if(re[0].length() > 16)
                record += re[0].substring(re[0].length() - 16) + " " + re[1];
            else
                record += re[0] + " " +  re[1];
            if(!l.contains(record))
            {
                l.add(record);
                map.put(record,1);
            }
            else{
                for(String st:map.keySet())   //map.containsKey(st)函数：判断map对象中是否存在以st为键值的参数！！
                {
                    if(st.equals(record))     //判断字符串相等最好用equals!!!
                    {
                        int cunt = map.get(st) + 1;
                        map.put(st, cunt);
                        break;
                    }
                }
            }
        }
        if(l.size()>8)
        {
            for(int i = l.size()-8; i < l.size(); i++)
            {
                for(String st: map.keySet())
                {
                    if(st.equals(l.get(i)))
                        System.out.println(st+ " " + map.get(st));
                }
            }
        }
        else
        {
            for(int i=0; i<l.size(); i ++)
            {
                for(String st: map.keySet())
                {
                    if(st.equals(l.get(i)))
                        System.out.println(st + " " + map.get(st));
                }
            }
        }
        scan.close();
    }
// LinkedHashMap是个好东西==将键值对按照存放时间排序，是有序的！！！
    public void errorRecord1(){
        Scanner scan = new Scanner(System.in);
        Map<String, Integer> map = new LinkedHashMap<>();
        while(scan.hasNext())
        {
            String s = scan.next();
            int col = scan.nextInt();
            String[] s1 = s.split("\\\\");
            String record = s1[s1.length-1];
            if(record.length()>16)
                record = record.substring(record.length()-16);
            String re = record + " " + col;
            if(map.containsKey(re))
                map.put(re, map.get(re)+1 );
            else
                map.put(re,1);
        }
        int cunt = 0;
        for(String st:map.keySet())   //输出最后八条记录！！大佬还是多。。。
        {
            cunt ++;
            if(cunt > map.size() - 8)
                System.out.println(st + " " + map.get(st));
        }
        scan.close();
    }
//密码验证合格程序
    public int symbol(String st)
    {
        char[] arr = st.toCharArray();
        int a=0,b=0,c=0,d=0;
        for(char  ch:arr)
        {
            if(ch >= '0' && ch <= '9')
                a = 1;
            else if(ch >= 'a' && ch <= 'z')
                b = 1;
            else if(ch >= 'A' && ch <= 'Z')
                c = 1;
            else 
                d = 1;
        }
        return (a+b+c+d);
    }
    
    public boolean substr(String st)
    {
        for(int i=0; i< st.length()-2; i++)
        {
            String s = st.substring(i,i+3);
            if(st.indexOf(s,i+1) != -1)   
                return false;
        }
        return true;
    }

    public void pwdValid(){
        Scanner scan = new Scanner(System.in);
        while(scan.hasNext())
        {
            String s = scan.next();
            if(s.length()>8)
            {
                if(symbol(s) >= 3)
                {
                    if(substr(s))
                    {
                        System.out.println("OK");
                        continue;
                    }
                }
            }
            System.out.println("NG");
        }
        scan.close();
    }

    public void pwdValid1(){
        Scanner scan = new Scanner(System.in);
            String p1 = ".*\\d.*";
            String p2 = ".*[a-z].*";
            String p3 = ".*[A-Z].*";
            String p4 = ".*[^\\dA-Za-z].*";
            String p5 = ".*(.{3,}).*\\1.*";    //正则表达式前向引用。\\双斜杠！
        while(scan.hasNext()){
            String s = scan.nextLine();
            int cunt = 0;
            if(s.matches(p1))
                cunt += 1;
            if(s.matches(p2))
                cunt += 1;
            if(s.matches(p3))
                cunt += 1;
            if(s.matches(p4))   
                cunt += 1;
            if(s.length() > 8)
            {
                if(cunt >= 3)
                {
                    if(!s.matches(p5))
                    {
                        System.out.println("OK");
                        continue;
                }
            }
                        }
            System.out.println("NG");
        }
        scan.close();
    }
 //简单密码破解
    public void simplePwd(){
        Scanner scan = new Scanner(System.in);
        while(scan.hasNext()){
            String s = scan.nextLine();
            char[] arr = s.toCharArray();
            for(char ch:arr){
                if(ch >= 'A' && ch < 'Z')
                    ch = (char)(ch + 33);
                else if(ch == 'Z')
                    ch = 'a';
                else if(ch >= 97 && ch <= 99)
                    ch = '2';
                else if(ch >= 100 && ch <= 102)
                    ch = '3';
                else if(ch >= 103 && ch <= 105)
                    ch = '4';
                else if(ch >= 106 && ch <= 108)
                    ch = '5';
                else if(ch >= 109 && ch <= 111)
                    ch = '6';
                else if(ch >= 112 && ch <= 115)
                    ch = '7';
                else if(ch >= 116 && ch <= 118)
                    ch = '8';
                else if(ch >= 119 && ch <= 122)
                    ch = '9';
                System.out.println();     
            }
         }
         scan.close();   
        }
//汽水瓶  
        public void bottle(){
            Scanner scan = new Scanner(System.in);
            while(scan.hasNext()){
                int s = scan.nextInt();
                scan.nextLine();
                System.out.println(s/2);
                }
            scan.close();
             }

             public void deleteLeast(){
                Scanner scan = new Scanner(System.in);
                while(scan.hasNext()){
                    String s = scan.nextLine();
                    Integer[] l = new Integer[26];
                    for(int i=0; i< 26; i++)
                    {
                        l[i] = 21;
                    }
                    char[] arr = s.toCharArray();
                    for(char ch:arr)
                    {
                        if(l[ch-97] == 21)
                            l[ch-97] = 1;
                        else
                            l[ch-97] += 1;
                    }
                    int index = (int) Collections.min(Arrays.asList(l)); //还不如自己直接写for循环找最小值==费了多大事儿==
                    for(char ch:arr)
                    {
                        if(l[(int)ch - 97] != index)
                            System.out.print(ch);
                    }
                    System.out.println();
                    }
                    scan.close();
                 }

                 public void deleteLeast1(){
                    Scanner scan = new Scanner(System.in);
                    while(scan.hasNext()){
                        String s = scan.nextLine();
                        Map<Character,Integer> map = new HashMap<>();
                        char[] arr = s.toCharArray();
                        for(char ch:arr)
                        {
                            if(!map.containsKey(ch))
                                map.put(ch,1);
                            else
                                map.put(ch,map.get(ch)+1);
                        }
                        int index = Collections.min(map.values());   //对map的键值进行排序！map.values()返回的是个Collection对象。
                        for(char ch:arr)
                        {
                            if(map.get(ch) != index)
                                System.out.print(ch);
                        }
                        System.out.println();
                        }
                        scan.close();
                    
                     }
//字符串排序！！忽略大小写对字符串进行排序Collections.sort(list,String.CASE_INSENSITIVE_ORDER);  或者可以重写Comparator的compare函数==
                     public void strSort(){
                        Scanner scan = new Scanner(System.in);
                        while(scan.hasNext())
                        {
                            String s = scan.next();
                            char[] arr = s.toCharArray();
                            List<String> list = new LinkedList<>();
                            for(char ch:arr)
                            {
                                 if((ch >='a' && ch<='z') || (ch >='A' && ch<='Z'))
                                     list.add(String.valueOf(ch));
                            }
                            Collections.sort(list,String.CASE_INSENSITIVE_ORDER);
                            /*
                            Collections.sort(list, new Comparator<Character> () {
                            @Override
                            public int compare(Character o1, Character o2) {
                                return Character.toLowerCase(o1)-Character.toLowerCase(o2);
                                    }      
                            });  */
                            int i = 0;
                            for(char ch:arr)
                            {
                                if((ch >='a' && ch<='z') || (ch >='A' && ch<='Z'))
                                {
                                    System.out.print(list.get(i));
                                    i += 1;
                                }
                                else
                                    System.out.print(ch);
                            }
                            System.out.println();
                        }
                        scan.close();
                    }

                    public void strSort1(){
                        Scanner scan = new Scanner(System.in);
                        while(scan.hasNext())
                        {
                            String s = scan.next();
                            char[] arr = s.toCharArray();
                            List<Character> list = new LinkedList<>();
                            for(int i=0;i<26; i++)            //基于计数排序思想对大小写字母进行排序。
                            {
                                for(char ch:arr)
                                {
                                    if(ch -'a' == i || ch-'A' == i)
                                        list.add(ch);
                                }
                            }
                            int k = 0;
                            for(char ch:arr)
                            {
                                if(Character.isLetter(ch))
                                {
                                    System.out.print(list.get(k));
                                    k += 1;
                                }
                                else
                                    System.out.print(ch);
                            }
                            System.out.println();
                        }
                        scan.close();
                    }
//查找兄弟单词，排序！
                 public void broWord(){
                        Scanner scan = new Scanner(System.in);
                        while(scan.hasNext())
                        {
                            String s = scan.nextLine();
                            String[] ss = s.split("\\ ");
                            int index = Integer.valueOf(ss[ss.length-1]);
                            char[] word = ss[ss.length-2].toCharArray();
                            Arrays.sort(word);
                            List<String> list = new LinkedList<>();
                            for(int i= 1; i < ss.length - 2; i ++)
                            {
                                char[] temp = ss[i].toCharArray();
                                Arrays.sort(temp);
                                if(Arrays.equals(temp,word) && !ss[i].equals(ss[ss.length-2]))    //Arrays.equals()和a.equals(b)的区别！！！
                                {
                                    list.add(ss[i]);
                                }
                            }
                            Collections.sort(list);
                            System.out.println(list.size());
                            if(index <= list.size())
                                System.out.println(list.get(index-1));
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
        // ma.hextoint1();
        // ma.primeNumber();
        // ma.rond();
        // ma.mergeRecord();
        // ma.setint();
        // ma.charcunt();
        // ma.strReverse();
        // ma.senReverse();
        //ma.strDic();
        //ma.int1();
        //ma.coordinate_move();
        //ma.errorRecord();
        //ma.pwdValid1();
        //ma.simplePwd();
        //ma.bottle();
        //ma.deleteLeast();
          ma.broWord();
         
    }
}

