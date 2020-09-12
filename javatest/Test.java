package javatest;

import java.lang.reflect.*;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.*;
import java.util.regex.*;
// import org.apache.commons.logging.Log;
// import org.apache.commons.logging.LogFactory;
public class Test {



/**
 * @author hhh
 * @param args
 * 写在类和方法的定义处，用于自动创建文档。
 * 用于java练习及笔记
 */ 
    public static void main(String[] args) throws Exception
    {
        float a = 10.1f;  //但是定义小数一定要加f
        float b = 10; //浮点数定义整数可以不加f
        final double PI = 3.14;
        // PI = 5.6;   常量在初始化之后就不允许再次赋值，不然会编译出错
        char c = '中';
        //System.out.println("" + c);
        byte b2 = 2,b1 = 3,b3;
        // b3 = b1 + b2;    这样是不对的！！b3 = (byte) (b1 + b2);
        b3 = (byte) (b1 +b2);
        // System.out.println(~0 + "");  >>结果是-1，因为int是4个字节，所以取反是FF FF FF FF
        double d = 1.2 + 24/5;
        // int x = 1<2 ? 1.5:8;     b?x:y中x和y的类型必须一致！！
        // System.out.println("" + d);
        String s = """
                    枯藤老树昏鸦
                      小桥流水人家
                        古道西风瘦马
                          断肠人在天涯""";
        // System.out.println(s);
        int[] arr = new int[]{1,2,3,4,5};
        int last;
        double fin;
        Scanner scan = new Scanner(System.in);
        //last = scan.nextInt();
        //fin = scan.nextInt();
        //double ratio = (fin-last)/fin * 100;
        // System.out.printf("%.2f%%",ratio);
        // String fruit = "apple";
        // switch(fruit){
        //     case "apple" ->  System.out.println("Selected apple"); 
        //     case "orange" -> System.out.println("Selected orange");
        //     case "mango" -> {
        //                      System.out.println("selected mabgo");
        //                      System.out.println("good choice");}
        //     default -> System.out.println("no fruit selected!");
        // }
        // int opt = switch (fruit) {
        //     case "apple" -> 1;
        //     case "orange" -> 2;
        //     default  -> 0;
        // };
    //      System.out.println(opt);
    //     System.out.println("请输入(1--石头，2--剪刀，3--布):");
    //     while(scan.hasNext()){
    //     int p = scan.nextInt();
    //     int c1 = 1 + (int)Math.random() * 3;
    //     switch(p){
    //         case 1 : if(c1 == 1)
    //                     System.out.println("平局！");
    //                 else if(c == 2)
    //                     System.out.println("你赢了！");
    //                 else
    //                     System.out.println("你输了！");
    //                 break;
    //         case 2 : if(c1 == 1)
    //                 System.out.println("你输了！");
    //             else if(c == 2)
    //                 System.out.println("平局！");
    //             else
    //                 System.out.println("你赢了！");
    //             break;
    //         case 3 : if(c1 == 1)
    //                     System.out.println("你赢了！");
    //                 else if(c == 2)
    //                     System.out.println("你输了！");
    //                 else
    //                     System.out.println("平局！");
    //                  break;
    //         default: break;
    //     }
    // }
    //System.out.println(Arrays.toString(arr));   //可直接将数组内容以list的形式打印出来
    //Arrays.sort(arr);    //对数组进行排序，排完之后原数组发生变化
    int[][] ar = {{1,2,3},{2,3,4},{3,4,5}};
    //System.out.println(Arrays.deepToString(ar));   //打印多维数组必须用Arrays.deepToString()
    //System.out.println(Arrays.toString(ar));  这样打印出来的是多维数组的地址。
    int[] a1[] = new int[1][];
    Income[] incomes = new Income[]{
        new Salary(7500),
        new State(15000)
    };
    System.out.println(totalTax(incomes));
    
		Person p1 = new Person("小明");
		System.out.println(Person.getCount()); // 1
		Person p2 = new Person("小红");
		System.out.println(Person.getCount()); // 2
		Person p3 = new Person("小军");
        System.out.println(Person.getCount()); // 3
        String st = "hi!%s, my name is %s";
        // System.out.println(st.formatted("Alice", "gjs"));
        // System.out.println(String.format("hi!%s, my name is %s","Alice", "gjs" ));
        // StringBuilder sb = new StringBuilder();
        // String[] names = {"Bob", "Alice", "Grace"};
        // sb.append("Hello ");
        // for(String name:names)
        // {
        //     sb.append(name).append(", ");
        // }
        // sb.delete(sb.length()-2, sb.length());
        // sb.append("!");
        // System.out.println(sb.toString());
        // StringJoiner sj = new StringJoiner(",", "Hello ", "!");
        // for(String name:names)
        //     sj.add(name);
        // System.out.println(sj.toString());
        
        Weekday day = Weekday.SUN;
        if(day.dayValue == 6 || day.dayValue == 0 )
            System.out.println("Work at home!");
        else
            System.out.println("Work at office!");
        System.out.println(Weekday.SUN.name());   //返回常量的名
        System.out.println(Weekday.SUN.ordinal());   //返回常量的顺序，但是这个顺序是根据enum中枚举值的顺序变化的，为了保持不变可以修改enum类

        // Point p = new Point(123,456);
        // System.out.println(p.x());
        // System.out.println(p.y());
        // System.out.println(p);
        BigInteger bi = new BigInteger("9999");
        BigInteger bi2 = new BigInteger("12345667");
        BigInteger sum = bi.add(bi2);
        BigDecimal bd = new BigDecimal("123.456");
        System.out.println(bd.scale());
        BigDecimal d3 = new BigDecimal("100");
        BigDecimal d4 = d3.stripTrailingZeros();
        System.out.println(d3 + " " + d4);
        System.out.println(d3.scale()); // 0
        System.out.println(d4.scale()); // -2
        bd.equals(d3);
        bd.compareTo(d3);
        Stu stu = new Stu();
        Class cls = Stu.class;
        System.out.println(cls.getField("score"));
        System.out.println(cls.getField("name"));
        System.out.println(cls.getDeclaredField("grade"));
        Field f = cls.getField("score");
        System.out.println(f.getName());
        System.out.println(f.getType());
        int m = f.getModifiers();
        System.out.println(Modifier.isPublic(m));
        System.out.println(Modifier.isFinal(m));
        f.setAccessible(true);
        Object o= f.get(stu);

        System.out.println(o);
        f.set(stu,100);
        o= f.get(stu);
        System.out.println(o);
        
        Constructor cons1 = Integer.class.getConstructor(int.class);
        Integer n1 = (Integer)cons1.newInstance(123);
        System.out.println(n1);
        
        Class i = Integer.class;
        Class n = i.getSuperclass();
        System.out.println(n);
        Class o1 = n.getSuperclass();
        System.out.println(o1);
        System.out.println(o1.getSuperclass());
        Class[] is = i.getInterfaces();
        for(Class iss:is)
            {
                System.out.println(iss);
            }
        List<Number> la = new ArrayList<Number>();
        // List<String> list = List.of("apple", "pear", "banana");
        //List<Integer> list = List.of(3,4,1);
        List<Integer> list = new ArrayList<>();
        list.add(4);
        list.add(3);
        list.add(5);
        List<String> list1 = new ArrayList<>();
        list1.add("apple");
        list1.add("pear");
        list1.add("banana");
        Object[] array = list.toArray();
        for (Object ss : array) {
            System.out.println(ss);
        }
        System.out.println(list.contains("apple"));
        System.out.println(list.indexOf("apple"));
        list.sort(new Comparator<Integer>() {
            public int compare(Integer x, Integer y)
            {
                return x.compareTo(y);
            }
        });
        list1.sort(new Comparator<String>() {
            public int compare(String x, String y)
            {
                return -x.compareTo(y);
            }
        });
        System.out.println(list);
        System.out.println(list1);
        Map<String, Integer> map = new HashMap<>();
        map.put("abc",444);
        int ma = map.put("abc",123);  // put有返回值！！返回旧的value值
        System.out.println(ma);
        map.put("bcd",234);
        for(String str:map.keySet())
        {
            System.out.println(str + "=" + map.get(str));
        }
        for(Map.Entry<String,Integer> entry: map.entrySet())
        {
            System.out.println(entry.getKey() + "=" + entry.getValue());
        }
        char cs[] = "1314520".toCharArray();
        int v1=0, v2=0, v3=0, v4=0;
        for(int ik=0; ik<cs.length; ik++)
        {
            switch(cs[ik])
            {
                default: v4++;
                case '1':v1++;
                case '2':v2++;
                case '3':v3++;
            }
        }
        System.out.println(""+v4+v1+v2+v3);

        Queue<User> q = new PriorityQueue<>(new Comparator<User>(){
            public int compare(User a, User b)
            {
                if(a.number.charAt(0) == b.number.charAt(0))
                    return a.number.compareTo(b.number);
                if(a.number.charAt(0) == 'V')
                    return -1;
                else
                    return 1;
            }
        });
        // 添加3个元素到队列:
        q.offer(new User("Bob", "A1"));
        q.offer(new User("Alice", "A2"));
        q.offer(new User("Boss", "V1"));
        System.out.println(q.poll()); // Boss/V1
        System.out.println(q.poll()); // Bob/A1
        System.out.println(q.poll()); // Alice/A2
        System.out.println(q.poll()); // null,因为队列为空
    
        String hex = itoHex(12500);
        if (hex.equalsIgnoreCase("30D4")) {
            System.out.println("测试通过");
        }
         else 
            System.out.println("测试失败");
        
        Pattern p = Pattern.compile("([01][0-9]|2[0-4]):([0-5]\\d|60):([0-5]\\d|60)");
        Matcher mp = p.matcher("23:01:59");
        if(mp.matches())
        {
            System.out.println(mp.group(1) + "  " + mp.group(2) + " " + mp.group(3));
        }
        String s11 = "the quick brown fox jumps over the lazy dog.";
        String r = s11.replaceAll("\\s([a-z]{4})\\s(the)", " <b>$2</b> ");
        System.out.println(r);

        Template t = new Template("Hello, ${name}! You are learning ${lang}!");
		Map<String, Object> data = new HashMap<>();
		data.put("name", "Bob");
		data.put("lang", "Java");
		//assertEquals("Hello, Bob! You are learning Java!", t.render(data));
		String s1 = "Hello, Bob! You are learning Java!";
		if(s1.equals(t.render(data)))
			System.out.println("测试成功");

    }

    static String itoHex(int n) {    //利用栈结构来实现int_hex的转化！！
        Deque<String> stack = new LinkedList<>();
        while(n != 0)
        {
            int temp = n % 16;
            switch(temp){
                case 10: stack.push("A");break;
                case 11: stack.push("B");break;
                case 12: stack.push("C");break;
                case 13: stack.push("D");break;
                case 14: stack.push("E");break;
                case 15: stack.push("F");break;
                default: stack.push(String.valueOf(temp));
            }
            n = n/16;
        }
        String s = "";
        while(stack.peek()!= null)
        {
            s += stack.pop();
        }
        return s;
    }


        
    
    public static double totalTax(Income[] incomes)
    {
        double summ = 0;
        for(Income income:incomes)
        {
            summ += income.getTax();
        }
        return summ;
    }
    
}
// interface Peer{
//     void run();
// }



class Template {

	final String template;
	final Pattern pattern = Pattern.compile("\\$\\{(\\w+)\\}");

	public Template(String template) {
		this.template = template;
	}

	public String render(Map<String, Object> data) {
        Matcher m = pattern.matcher(template);
        String r = template;
		// TODO:
		while (m.find()) {
            String sub = template.substring(m.start(),m.end());
            String sub1 = template.substring(m.start()+2,m.end()-1);
			r = r.replace(sub,(String)data.get(sub1));
		}
		return r;
	}

}
class User {
    public final String name;
    public final String number;

    public User(String name, String number) {
        this.name = name;
        this.number = number;
    }

    public String toString() {
        return name + "/" + number;
    }
}

class Stu extends Per{
    public int score;
    private int grade = 0;
    public Stu()
    {
        
    }
}
class Per{
    public String name;
}
// record Point(int x, int y)  //记录类
// {
//     public Point{
//         if(x <0 || y <0){
//             throw new IllegalArgumentException();
//         }
//     }
// }

enum Weekday{   //枚举类，每个枚举都是本类的一个实例。
    SUN(0),MON(1),TUE(2),WED(3),THU(4),FRI(5),SAT(6);
    public final int dayValue;
    private Weekday(int dayValue)
        {
            this.dayValue = dayValue;
        }
}

class Person {

	// TODO
    static int count = 0;
	String name;

	public Person(String name) {
        this.name = name;
        count += 1;
    }
    public static int getCount()
        {return count;}

}




// abstract class Person{
//     public abstract void run();
// }

// class Student extends Person{
//     @Override
//     public void run()
//     {

//     }
// }
abstract class Income{
    protected double income;
    public Income(double income)
    {
        this.income = income;
    }
    public abstract double getTax();
}
class Salary extends Income{
    public Salary(double income)
    {
        super(income);
    }
    @Override
    public double getTax()
    {
        if (this.income <= 5000)
        return 0;
        else
            return (this.income-5000) * 0.2;
    }
}

class State extends Income{
    public State(double income)
    {
        super(income);
    }
    @Override
    public double getTax()
    {
        return 0;
    }
}
