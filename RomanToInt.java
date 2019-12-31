/**
 * Author : Shweta Wahane
 *
 * THis program converts Roman numbers to Integers.
 *
 */


import java.util.HashMap;

public class RomanToInt {

    public int RomanToInt(String s) {
            HashMap<String, Integer> hi = new HashMap<>();
            hi.put("I",1);
            hi.put("V",5);
            hi.put("X",10);
            hi.put("L",50);
            hi.put("C",100);
            hi.put("D",500);
            hi.put("M",1000);

            int sum = 0;
            char next='A';

            for(int index=0; index < s.length(); index++)
            {
                char ch = s.charAt(index);

                try {
                    next = s.charAt(index+1);
                }

                catch(Exception e) {
                    next = 'A';
                }

                switch(ch) {

                    case 'I':
                        if( ( next == 'V' ) || ( next =='X' ) )
                        {
                            int i = hi.get("I");
                            sum = sum - i;
                            break;
                        }
                        else
                        {
                            int i = hi.get("I");
                            sum = sum + i;
                            break;
                        }
                    case 'V':
                        int v = hi.get("V");
                        sum = sum + v;
                        break;
                    case 'X':
                        if( ( next=='L' ) || ( next=='C' ) )
                        {
                            int x = hi.get("X");
                            sum = sum - x;
                            break;
                        }
                        else
                        {
                            int x = hi.get("X");
                            sum = sum + x;
                            break;
                        }
                    case 'L':
                        int l = hi.get("L");
                        sum = sum + l;
                        break;
                    case 'C':
                        if( ( next=='D' ) || ( next=='M' ) )
                        {
                            int c = hi.get("C");
                            sum = sum - c;
                            break;
                        }
                        else
                        {
                            int c = hi.get("C");
                            sum = sum + c;
                            break;
                        }
                    case 'D':
                        int d = hi.get("D");
                        sum = sum + d;
                        break;
                    case 'M':
                        int m = hi.get("M");
                        sum = sum + m;
                        break;
                }
            }
            return sum;
        }

    public static void main(String[] args) {
        RomanToInt rin = new RomanToInt();
        System.out.println(rin.RomanToInt("XX"));
        System.out.println(rin.RomanToInt("XXV"));
        System.out.println(rin.RomanToInt("XIX"));
    }

}
