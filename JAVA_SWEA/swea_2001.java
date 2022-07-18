package org.algorithm_test.java_test.eclipse;

import java.util.Scanner;

class swea_2001 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int Max1 = 0;
		int T = sc.nextInt();
		for (int tc = 0; tc < T; tc++) {
			int n = sc.nextInt(), m = sc.nextInt();
			int[][] arr = new int[n][n];
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					arr[i][j] = sc.nextInt();

				}
			}
			int res = 0;
			// System.out.println(arr[0][0]);
			for (int i = 0; i < n - m + 1; i++) {

				for (int x = 0; x < n - m + 1; x++) {
					for (int k = 0 + i; k < m + i; k++) {
						for (int z = x; z < x + m; z++) {
							// System.out.print(arr[k][z]);
							res += arr[k][z];
						}

					}
//					System.out.println(res);
//					res = 0;
					Max1 = Math.max(res, Max1);
					res = 0;
				}

			}
			System.out.printf("#%d ", tc + 1);
			System.out.println(Max1);
			Max1 = 0;
		}
	}

}
