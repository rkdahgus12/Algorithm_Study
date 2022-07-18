package org.algorithm_test.java_test.eclipse;

import java.util.Scanner;

class swea_1974 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		// Arrays.stream(arr).sum();
		int T = sc.nextInt();
		for (int tc = 1; tc < T + 1; tc++) {
			int[][] arr = new int[9][9];
			for (int i = 0; i < 9; i++) {
				for (int j = 0; j < 9; j++) {
					arr[i][j] = sc.nextInt();
				}
			}
			System.out.printf("#%d ", tc);
			boolean flag = true;

			for (int i = 0; i < 9; i++) {
				int sum_1 = 0;
				int sum_2 = 0;
				for (int j = 0; j < 9; j++) {
					sum_1 += arr[i][j];
					sum_2 += arr[j][i];

				}
				if ((sum_1 != 45) || (sum_2 != 45)) {

					flag = false;
					break;
				}
				sum_1 = 0;
				sum_2 = 0;

			}
			if (flag == false) {
				System.out.println("0");

			} else if (flag == true) {
				boolean flag_2 = true;
				int sum_3 = 0;
				for (int k = 0; k < 9; k += 3) {
					for (int x = 0; x < 9; x += 3) {
						for (int i = k; i < k + 3; i++) {
							for (int j = x; j < x + 3; j++) {
								sum_3 += arr[i][j];
								// System.out.print(arr[i][j]);
							}

						}
						// System.out.println(sum_3);
						if (sum_3 != 45) {
							flag_2 = false;
							break;

						}
						sum_3 = 0;
					}
				}
				if ((flag == true) && (flag_2 == true)) {
					System.out.println("1");

				}
				if (flag_2 == false) {
					System.out.println("0");

				}
			}
		}
	}
}