import java.util.Scanner;
class FourPow{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		for(int i=1;i<=n;i++){
			int ans=printSeries(i);
		if(ans>n){
			System.out.println("Not Found");
			break;
		}
		else if(ans==n){
			System.out.println("Found at "+i);
			break;
		}
		}
	}
	public static int printSeries(int n){
		int i=0,sum=0;
		int ans=Integer.valueOf(Integer.toString(Integer.parseInt(String.valueOf(n),16),2));
		while(ans>0){
			if(ans%10==1)
			sum+=Math.pow(4*(ans%10),i);
			i++;
			ans/=10;
		}		
		return sum;
	}
}