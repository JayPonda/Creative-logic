// push and pop operation where stack is not flexible

import java.util.Scanner;
import java.util.Arrays;
public class push_pop {
    // inilation...
    public static int k, index;
    public static int[] arr;
    
    // main function...
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        k = -1;
        System.out.print("enter: index of stack ");
        index = sc.nextInt();
        arr = new int[index];
        System.out.printf("there are stack with size %d \naccording that your operation will be done...\n\n", index);
        while(true)
        {
            System.out.print("\nwhich operation you want to perform...\n1)push\n2)pop\n3)insertion_row\n4)deletion_row\n5)statument\n6)shorting\n0)default(exit)\nenter: choose operation ");
            int opt = sc.nextInt();
            switch(opt)
            {
                case 1:
                    push();
                    break;
                case 2:
                    pop();
                    break;
                case 3:
                    System.out.println("how many values you want to enter...");
                    int j = sc.nextInt();
                    if(k + j >= index)
                    {
                        System.out.println("out of range...");
                    }
                     else
                    {
                        for(int i = 0; i < j; i++)
                        {
                            push();
                        }
                    }
                    break;
                
                case 4:
                    System.out.println("how many values you want to delete...");
                    int j1 = sc.nextInt();
                    if(k - j1 < -1)
                    {
                        System.out.println("out of range...");
                    }
                     else
                    {
                        for(int i = 0; i < j1; i++)
                        {
                            pop();
                        }
                    }
                    break;
                    
                case 5:
                    System.out.print("array elements:: ");
                    for(int i = 0; i <= k; i++)
                        {
                            System.out.print(arr[i]+" ");
                        }
                    System.out.printf("\n%d array elements are presented so %d are empty\n", k + 1, index - (k + 1));
                    break;
                    
                case 6:
                    sort();
                    break;

                default:
                    System.out.println("exit");
                    return;
            
            }
        }
    }
    
        // other necassary functions
    public static void push()
        {   
            if (k  >= index - 1)
                {
                    System.out.println("your stack is overflow...");
                }
            else
            {
                System.out.println("enter: value for stack");
                Scanner sc_push = new Scanner(System.in);
                int val = sc_push.nextInt();
                k++;
                arr[k] = val;
                
            }
        }
        
    public static void pop()
        {   
            if (k  < 0 )
                {
                    System.out.println("your stack is underflow...");
                }
            else
            {
                System.out.printf("%d is poped...\n", arr[k]);
                arr[k] = 0;
                k--;
            }
        }
    public static void sort()
    {
        if (k  < 0 )
                {
                    System.out.println("your stack is underflow...");
                }
        else
                {
                    int[] cpyarr = new int[k + 1];
                    System.arraycopy(arr, 0, cpyarr, 0, (k + 1));
                    Arrays.sort(cpyarr);
                    System.out.printf("sorted array: %s\n", Arrays.toString(cpyarr));   
                }
    }
}
