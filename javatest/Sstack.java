package javatest;

import java.util.*;

public class Sstack {
    public static void main(String[] args) {
        String hex = toHex(12500);
        if (hex.equalsIgnoreCase("30D4")) {
            System.out.println("测试通过");
        } else {
            System.out.println("测试失败");
        }
        
        String exp = "100 + 20 * (9 - 5)";
        SuffixExpression1 se = compile1(exp);
        int result = se.execute();
        System.out.println(exp + " = " + result + " " + (result == 100 + 20 * (9 - 5) ? "✓" : "✗"));
    }
    //中缀表达式变后缀表达式
    // 1.遇到数字直接加到后缀表达式字符串上
    // 2.遇到+-*/符号先放到栈上，若当前栈顶符号优先级>=当前符号，则将栈顶符号出栈，
    // 遇到(直接push入栈
    // 遇到） 则将栈中符号弹出直至遇到(
    static SuffixExpression compile(String exp) {
        // TODO:
        Deque<Character> stack = new LinkedList<Character>();
        String out = "";  //后缀表达式
        for(char ch:exp.toCharArray())
        {
            if(ch == ' ')
                continue;
            if(ch >= '0' && ch<='9')
            {
                out += ch;
                continue;
            }
            else if(ch =='+' || ch == '-' || ch == '*' || ch == '/')
            {
                if(stack.isEmpty())
                    stack.push(ch);
                else 
                {
                    while(pri(stack.peek()) >= pri(ch) && !stack.isEmpty())
                    {
                        out += stack.pop();
                    }
                    stack.push(ch);
                }
            }
            else if(ch == '(')
                {
                    stack.push(ch);
                }
            else
            {
                char temp = stack.pop();
                while(temp != '(')
                {
                    out += temp;
                    temp = stack.pop();
                }
            }
        }
        while(!stack.isEmpty())
            {
                out += stack.pop();
            }
        return new SuffixExpression(out);
    }

    //实现多位数的数字进行加减乘除操作.
    static SuffixExpression1 compile1(String exp) {
        // TODO:
        Deque<Character> stack = new LinkedList<Character>();
        String out = "";  //后缀表达式
        char[] exptoc = exp.toCharArray();
        for(int i=0; i < exptoc.length; i++)
        {
            char ch = exptoc[i];
            String num = "";
            int j = 1;
            if( ch == ' ')
                continue;
            if(ch >='0' && ch <= '9')
            {
            while(ch >= '0' && ch<='9')
            {
                num += ch;   
                ch = exptoc[i+j];
                j ++;
            }
            out +=num + " ";
            i = i + j -2 ;
        }
            else if(ch =='+' || ch == '-' || ch == '*' || ch == '/')
            {
                if(stack.isEmpty())
                    stack.push(ch);
                else 
                {
                    while(pri(stack.peek()) >= pri(ch) && !stack.isEmpty())
                    {
                        out += stack.pop();
                    }
                    stack.push(ch);
                }
            }
            else if(ch == '(')
                {
                    stack.push(ch);
                }
            else
            {
                char temp = stack.pop();
                while(temp != '(')
                {
                    out += temp;
                    temp = stack.pop();
                }
            }
        }
        while(!stack.isEmpty())
            {
                out += stack.pop();
            }
        return new SuffixExpression1(out);
    }

    static int pri(char t)
    {
        if(t == '(')
            return 1;
        if(t == '+' || t == '-')
            return 2;
        if(t == '*' || t == '/')
            return 3;
        else
            return 4;
    }


    static String toHex(int n) {    //利用栈结构来实现int_hex的转化！！
        Deque<String> stack = new LinkedList<>();
        //或者可以用String s1 = Integer.toHexString(temp);直接push该String.
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
}

class SuffixExpression {
    String suffix;
    public SuffixExpression(String suffix)
    {
        this.suffix = suffix;
    }
    int execute() {
        // TODO:
        Deque<Integer> stk = new LinkedList<>();
        for(char s:suffix.toCharArray())
        {
            if(s >='0' && s <= '9')
                stk.push(Integer.parseInt(""+s));
            else
            {
                int a1 = stk.pop();
                int a2 = stk.pop();
                switch(s)
                {
                    case '+': stk.push(a1+a2);break;
                    case '-': stk.push(a2-a1);break;
                    case '*': stk.push(a1*a2);break;
                    case '/': stk.push(a2/a1);break;
                }
            }
        }
        return stk.pop();

    }
}


class SuffixExpression1 {
    String suffix;
    public SuffixExpression1(String suffix)
    {
        this.suffix = suffix;
    }
    int execute() {
        // TODO:
        Deque<Integer> stk = new LinkedList<>();
        char[] su = suffix.toCharArray();
        for(int i=0;i<su.length;i++)
        {
            char s = su[i];
            int j = 0;
            if(s == ' ')
                continue;
            if(s >='0' && s<='9')
            {
                while(s >= '0' && s <='9')
                {
                    j += 1;
                    s = su[i+j];
                }
                stk.push(Integer.parseInt(suffix.substring(i, i+j)));
                i = i + j-1;
            }
            else
            {
                int a1 = stk.pop();
                int a2 = stk.pop();
                switch(s)
                {
                    case '+': stk.push(a1+a2);break;
                    case '-': stk.push(a2-a1);break;
                    case '*': stk.push(a1*a2);break;
                    case '/': stk.push(a2/a1);break;
                }
            }
        }
        return stk.pop();

    }
}

//在原有中缀表达式上进行改进，允许传入参数
class Mainn {
	public static void main(String[] args) {
		String exp = "x + 2 * (y - 5)";
		SuffixExpression2 se = compile(exp);
		Map<String, Integer> env = Map.of("x", 1, "y", 9);
		int result = se.execute(env);
		System.out.println(env);
		System.out.println(exp + " = " + result + " " + (result == 1 + 2 * (9 - 5) ? "✓" : "✗"));
	}

	static SuffixExpression2 compile(String exp) {
		// TODO:
		Deque<Character> stack = new LinkedList<Character>();
        String out = "";  //后缀表达式
        char[] exptoc = exp.toCharArray();
        for(int i=0; i < exptoc.length; i++)
        {
            char ch = exptoc[i];
            String num = "";
            int j = 1;
            if( ch == ' ')
                continue;
            if(ch == 'x' || ch == 'y')
            	{
            		out += ch;
            		continue;
            	}
            if(ch >='0' && ch <= '9')
            {
            while(ch >= '0' && ch<='9')
            {
                num += ch;   
                ch = exptoc[i+j];
                j ++;
            }
            out +=num + " ";
            i = i + j -2 ;
        }
            else if(ch =='+' || ch == '-' || ch == '*' || ch == '/')
            {
                if(stack.isEmpty())
                    stack.push(ch);
                else 
                {
                    while(pri(stack.peek()) >= pri(ch) && !stack.isEmpty())
                    {
                        out += stack.pop();
                    }
                    stack.push(ch);
                }
            }
            else if(ch == '(')
                {
                    stack.push(ch);
                }
            else
            {
                char temp = stack.pop();
                while(temp != '(')
                {
                    out += temp;
                    temp = stack.pop();
                }
            }
        }
        while(!stack.isEmpty())
            {
                out += stack.pop();
            }
        return new SuffixExpression2(out);
    }

    static int pri(char t)
    {
        if(t == '(')
            return 1;
        if(t == '+' || t == '-')
            return 2;
        if(t == '*' || t == '/')
            return 3;
        else
            return 4;
    }


}

class SuffixExpression2 {
	String suffix;
    public SuffixExpression2(String suffix)
    {
        this.suffix = suffix;
    }
    int execute(Map<String, Integer> env) {
        // TODO:
        Deque<Integer> stk = new LinkedList<>();
        char[] su = suffix.toCharArray();
        for(int i=0;i<su.length;i++)
        {
            char s = su[i];
            int j = 0;
            if(s == ' ')
                continue;
            if(s == 'x' || s == 'y')
            {
            	stk.push(env.get(""+s));   //注意key的数据类型.
            	continue;
            }
            if(s >='0' && s<='9')
            {
                while(s >= '0' && s <='9')
                {
                    j += 1;
                    s = su[i+j];
                }
                stk.push(Integer.parseInt(suffix.substring(i, i+j)));
                i = i + j-1;
            }
            else
            {
                int a1 = stk.pop();
                int a2 = stk.pop();
                switch(s)
                {
                    case '+': stk.push(a1+a2);break;
                    case '-': stk.push(a2-a1);break;
                    case '*': stk.push(a1*a2);break;
                    case '/': stk.push(a2/a1);break;
                }
            }
        }
        return stk.pop();


    }
}
