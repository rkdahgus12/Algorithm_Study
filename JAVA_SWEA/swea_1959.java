package org.algorithm_test.java_test.eclipse;

import java.util.Scanner;

class swea_1959 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int Tcase = sc.nextInt();
		for (int i = 0; i < Tcase; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			int[] a_arr = new int[a];
			int[] b_arr = new int[b];
			for (int ii = 0; ii < a_arr.length; ii++) {
				a_arr[ii] = sc.nextInt();
			}
			for (int ii = 0; ii < b_arr.length; ii++) {
				b_arr[ii] = sc.nextInt();
			}
			int Max = 0;
			if (a < b) {
				for (int j = 0; j < b - a + 1; j++) {
					int res = 0;
					for (int k = 0; k < a; k++) {
						res += a_arr[k] * b_arr[j + k];

					}
					Max = Math.max(Max, res);
				}
			} else if (a > b) {
				for (int j = 0; j < a - b; j++) {
					int res = 0;
					for (int k = 0; k < b; k++) {
						res += b_arr[k] * a_arr[j + k];

					}
					Max = Math.max(Max, res);
				}

			} else {
				int res = 0;
				for (int j = 0; j < a; j++) {
					res += a_arr[j] * b_arr[j];
				}
				Max = Math.max(Max, res);
			}
			System.out.printf("#%d %d\n", i + 1, Max);
		}
	}
}
