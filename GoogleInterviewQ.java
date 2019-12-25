import java.lang.Math;
import java.util.*;

public class GoogleInterviewQ
{
    static int X;
    static int temp;

    static int size;
    static int D;

    public static void main(String[] args) {
        System.out.println(reverse(2134236469));

    }

    public static double myMethod(int a)
    {
        temp = 0;
        size = 0;

        ArrayList<Integer> arr = new ArrayList();

        temp = a;
        while(temp!=0)
        {

            int k = temp % 10;
            arr.add(k);
            temp = temp /10;

        }
        size = arr.size();
        double sum=0;
        int y;
        double z;
        double p =0;
        for(int i = 0 ; i<size; i++)
        {
            y =  arr.get(i);
            z = Math.pow(10, size-(i+1));
            p = ((double)y)*z;
            sum = sum +  p;

        }

        return sum;

    }
    public static int reverse(int x) {
        D = 0;
        X = 0;
        X = x;
        double result;
        int min = (int)Math.pow(-2, 31);
        int max =((int) Math.pow(2,31)) - 1;
        if(  (X > min &&  X < max ))
        {
            if(X == 0)
            {
                D = 0 ;
            }
            else if(X<0)
            {
                X = X * -1;
                result =  myMethod(X);
                result = result*(-1);

                if(  result > min && result < max )
                {
                    D = (int) result;
                }
                else
                {
                    D=0;
                }

            }
            else if(X>0){
                result = myMethod(X);
                if(  result > min &&  result < max )
                {
                    D = (int) result;
                }
                else
                {
                    D=0;
                }

            }
            return D;
        }
        else{
            return D;
        }
    }

}
