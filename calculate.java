package calculatorpack;

import java.util.*;

public class calculate {
	
	static Scanner input = new Scanner(System.in);
	
	static float temp = 0;
	
	public static void main(String[] args) {
		
		System.out.print("Welcome to my program\nPlease select one of the options below\n1.Simple calculation\n2.Trigonometric calculation\nyour choice: ");
		
		int question = input.nextInt();
		
		switch(question) {
		
		case 1: start(); break;
		
		case 2: start2(); break;
		
		default: System.out.println("Not Found"); break;
		
		}
	}
	
	public static void start() {
		
		System.out.print("enter the number one: ");
		
		float number1 = input.nextFloat();
		
		System.out.print("\n1. +\n2. -\n3. *\n4. /\n\nchoice your op: ");
		
		int op = input.nextInt();
		
		System.out.print("\nenter the number two: ");
		
		float number2 = input.nextFloat();
		
		if (op == 1) {
			
			temp = number1 + number2;
		}
		
		else if (op == 2) {
			
			temp = number1 - number2;
		}
		
		else if (op == 3) {
			
			temp = number1 * number2;
		}
		
		else if (op == 4) {
			
			  if (number2 == 0) {
				  
				  System.out.println("\nInvalid number!!!\nIt is better to terminate the program and start from the beginning, otherwise the program will not work properly.");
			  }
			
			temp = number1 / number2;
		}
		
		else {
			
			System.out.println("Invalid operation, please try again");
		}
		

		System.out.println("\nTotal : " + temp);
		
		cal(temp);
		
	}
	
	public static void cal(float temp) {
		
		while (true) {
			
			System.out.print("\n1. +\n2. -\n3. *\n4. /\n\nchoice your op:(0 for exit); ");
			
			int op2 = input.nextInt();
			
			if (op2 == 0) {
				
				System.out.println("Good bye");
				
				break;
			}
			
			System.out.print("\nenter the number two: ");
			
			float number2 = input.nextFloat();
			
			switch(op2) {
			
			case 1:
				
				temp += number2;break;
				
			case 2:
				
				temp -= number2;break;
				
			case 3:
				
				temp *= number2;break;
				
			case 4:
				
				if (number2 == 0) {
					
					System.out.println("Invalid number!!!\nIt is better to terminate the program and start from the beginning, otherwise the program will not work properly.");
					
				}
				
				temp /= number2;break;
				
			default:
				
				System.out.println("Invalid operation, please try again");break;
				
			}
			
			System.out.println("\nTotal : " + temp);
			
		}
			
	}
	
	public static void start2() {
		
		while (true) {
		
			System.out.print("\nSelect in oder options\n1.sqrt\n2.log\n3.sin\n4.cos\n5.tan\nYour choice(0 for exit):");
			
			int question2 = input.nextInt();
			
			if (question2 == 0) {
				
				System.out.println("Got it");
				
				break;
			}
			
			System.out.print("enter the your number: ");
			
			int number = input.nextInt();
			
			switch (question2) {
			
			case 1: System.out.println("\nsqrt(" + number + ") = " + Math.sqrt(number));break;
			
			case 2: System.out.println("\nsqrt(" + number + ") = " + Math.log(number));break;
			
			case 3: System.out.println("\nsqrt(" + number + ") = " + Math.sin(number));break;
			
			case 4: System.out.println("\nsqrt(" + number + ") = " + Math.cos(number));break;
			
			case 5: System.out.println("\nsqrt(" + number + ") = " + Math.tan(number));break;
			
			}
			
		}
		
	}
	
}
