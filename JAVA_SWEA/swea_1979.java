package org.algorithm_test.java_test.eclipse;

import java.util.Scanner;

class swea_1979 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc = 1; tc < T + 1; tc++) {
			int n = sc.nextInt(), k = sc.nextInt();
			int[][] arr = new int[n][n];
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					arr[i][j] = sc.nextInt();
				}
			}
			int res = 0;
			for (int i = 0; i < n; i++) {
				int count = 0;
				for (int j = 0; j < n; j++) {
					if (arr[i][j] == 0) {
						if (count == k) {
							res += 1;
						}
						count = 0;
					} else {
						count += 1;
					}
				}
				if (count == k) {
					res += 1;

				}
				count = 0;

			}
//			System.out.println(res);
			int res1 = 0;
			for (int i = 0; i < n; i++) {
				int count_1 = 0;
				for (int j = 0; j < n; j++) {
					if (arr[j][i] == 0) {
						if (count_1 == k) {
							res1 += 1;
						}
						count_1 = 0;
					} else {
						count_1 += 1;
					}
				}
				if (count_1 == k) {
					res1 += 1;

				}
				count_1 = 0;

			}
			System.out.printf("#%d ", tc);
			System.out.println(res1 + res);
		}

	}

}
