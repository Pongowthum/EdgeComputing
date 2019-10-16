import java.util.*;
public class Sury {

public static void main(String[] args) {
// TODO Auto-generated method stub

Scanner in = new Scanner(System.in);
int a=in.nextInt();
String[] arr=new String[a];
Integer[] arr1=new Integer[a];
int flag=0;
for(int i=0;i<a;i++)
{
arr[i]=in.next();
}
for(int i=0;i<a;i++)
{
arr1[i]=in.nextInt();
}
in.close();
HashMap <String,Integer>map = new HashMap<String,Integer>();
StringBuilder sb= new StringBuilder();
//ArrayList <Integer> al = new ArrayList<Integer>();
Integer [] na= new Integer[10];
int k=0;
for(int i=0;i<a;i++)
{
map.put(arr[i], arr1[i]);
}
Arrays.sort(arr1);
for(int i=0;i<a-1;i++)
{
if((arr1[i+1]-arr1[i])==1)
{
if(((arr1[i]-arr1[i-1])==1 && ((arr1[i+1])-(arr1[i])==1)))
{
na[k]=(arr1[i-1]);
k++;
na[k]=(arr1[i]);
k++;
na[k]=(arr1[i+1]);
k++;
flag=1;
break;
}
}
}


//Iterator itr = al.iterator();
for(int i=k;i>=0;i--) {
for(Map.Entry m:map.entrySet())
{


if(m.getValue().equals(na[i]))
{
sb.append(m.getKey()+" ");
}
}
}
String k1=sb.toString().trim();
String h=k1.replace(" ",":");
if(flag==0)
{
System.out.print(" NONE ");
}
else
{
System.out.println(h);
}

}
}