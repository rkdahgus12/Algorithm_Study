package org.algorithm_test.java_test_baekjoon.eclipse;

import java.util.Scanner;

class B_2635 {

	public static void main(String[] args) {
		// TODO 자동 생성된 메소드 스텁
		Scanner sc = new Scanner(System.in);
		int[][] arr = new int[100][100];
		int T = sc.nextInt();
		int sum = 100 * T;
		for (int tc = 0; tc < T; tc++) {
			int x = sc.nextInt(), y = sc.nextInt();
			for (int i = x; i < x + 10; i++) {
				for (int j = y; j < 10 + y; j++) {
					arr[i][j] = 1;

				}
			}
		}

		int s_2 = 0;

		for (int i = 0; i < 100; i++) {

			for (int j = 0; j < 100; j++) {
//				System.out.print(arr[i][j]);
				if (arr[i][j] == 1) {
					s_2 += 1;
				}

			}

		}
		System.out.println(s_2);

	}

}
