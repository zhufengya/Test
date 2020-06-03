package javatest;

import java.util.*;

public class Helloworld {

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
    public static void main(String[] args) {
        System.out.println("Helloworld!");
        Helloworld he = new Helloworld();
        he.mergeRecord();        
    }
}

