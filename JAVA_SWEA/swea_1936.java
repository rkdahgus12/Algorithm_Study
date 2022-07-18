package org.algorithm_test.java_test.eclipse;

import java.util.Scanner;

class swea_1936 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		if ((a == 1) && (b == 3)) {
			System.out.println("A");
		} else if ((a == 2) && (b == 1)) {
			System.out.println("A");
		} else if ((a == 3) && (b == 2)) {
			System.out.println("A");
		} else {
			System.out.println("B");
		}
		sc.close();
	}
}
