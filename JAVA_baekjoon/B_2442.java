package org.algorithm_test.java_test_baekjoon.eclipse;

import java.util.Scanner;

public class B_2442 {

	public static void main(String[] args) {
		// TODO 자동 생성된 메소드 스텁
		Scanner sc = new Scanner(System.in);
		int soo = sc.nextInt();
		for (int i = 0; i < soo; i++) {
			for (int j = soo - i; j > 1; j--) {
				System.out.print(" ");
			}

			for (int j = 0; j <= i; j++) {
				System.out.print("*");
				if (j > 0) {
					System.out.print("*");
				}
			}

			System.out.println();
		}
	}

}
