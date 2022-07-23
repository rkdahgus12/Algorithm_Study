package org.algorithm_test.java_test_baekjoon.eclipse;

import java.util.Scanner;

public class B_2446 {

	public static void main(String[] args) {
		// TODO 자동 생성된 메소드 스텁
		Scanner sc = new Scanner(System.in);
		int soo = sc.nextInt();

		for (int i = 0; i < soo; i++) {
			for (int j = 0; j < i; j++) {
				System.out.print(" ");
			}
			for (int k = soo - i; k > 0; k--) {
				if (k > 1) {

					System.out.print("*");
				}

				System.out.print("*");
			}
			System.out.println();
		}
		for (int i = 1; i < soo; i++) {
			for (int j = soo - i - 1; j > 0; j--) {
				System.out.print(" ");
			}
			for (int k = 0; k <= i; k++) {
				if (k > 0) {

					System.out.print("*");
				}

				System.out.print("*");
			}
			System.out.println();
		}

	}

}
