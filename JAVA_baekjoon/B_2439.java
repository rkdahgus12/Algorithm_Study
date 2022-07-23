package org.algorithm_test.java_test_baekjoon.eclipse;

import java.util.Scanner;

public class B_2439 {

	public static void main(String[] args) {
		// TODO 자동 생성된 메소드 스텁
		Scanner sc = new Scanner(System.in);
		int soo = sc.nextInt();
		for (int i = 0; i < soo; i++) {
			for (int j = 0; j <= i; j++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}

}
