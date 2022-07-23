package org.algorithm_test.java_test_baekjoon.eclipse;

import java.util.Scanner;

public class B_2438 {

	public static void main(String[] args) {
		// TODO 자동 생성된 메소드 스텁
		Scanner sc = new Scanner(System.in);
		int soo = sc.nextInt();
		char a = '*';
		for (int i = 0; i < soo; i++) {
			for (int j = soo - i - 1; j > 0; j--) {
				System.out.print(" ");
			}
			for (int k = 0; k <= i; k++) {
				System.out.print("*");
			}
			System.out.println();
		}

	}

}
