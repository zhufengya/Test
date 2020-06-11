package javatest;
import java.util.*;

public class Hhhard {
    public boolean prime(int a, int b)
    {
          int sum = a +b;
        int i = 2;
        while( i* i <= sum)
        {
            if(sum % i == 0)
                return false;
            i += 1;
        }
        return true;
    }
    
      public boolean part(int index, List<Integer> jii, List<Integer> ouu, int[] us, int[] re)
      {
          for(int i = 1; i <= jii.size(); i++)
          {
              if(prime(ouu.get(index-1), jii.get(i-1)) && us[i] == 0)
              {
                  us[i] = 1;
                  if(re[i] == 0 || part(re[i],jii,ouu,us,re))
                  {
                      re[i] = index;
                      return true;
                  }
              }
          }
          return false;
      }
//素数伴侣    二分图匹配！匈牙利算法！增广路径！！  
      public void primePart(){
            Scanner sc = new Scanner(System.in);
            while(sc.hasNext()){
            int n = sc.nextInt();
          int[] l = new int[n];
          for(int i=0; i<n; i++)
          {
              l[i] = sc.nextInt();
          }
          List<Integer> ji = new ArrayList<>();
          List<Integer> ou = new ArrayList<>();
          for(int num:l)
          {
              if(num % 2 == 0)
                  ou.add(num);
              else
                  ji.add(num);
          }
            int[] result = new int[ji.size() + 1];
          for(int i=0; i <= ji.size(); i++)
              result[i] = 0;
            int[] used = new int[ji.size() + 1];
          int cunt = 0;
          for(int x = 1; x <= ou.size(); x++)
          {
              for(int i=0; i<= ji.size(); i++)
                  used[i] = 0;
              if(part(x,ji,ou,used,result))
                  cunt += 1;
          }
          System.out.println(cunt);
        }
        sc.close();
        }
    
        public static void main(  String[] args)
        {
              Hhhard h = new Hhhard();
            h.primePart();
        }
    
}