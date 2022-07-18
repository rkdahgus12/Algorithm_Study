package org.algorithm_test.java_test.eclipse;

import java.util.Scanner;

class SWEA_H_햄버거다이어트 {
	static int score;
	static int max1;
	static int[] sc_arr;
	static int count;

	public static void main(String[] args) {
		// TODO 자동 생성된 메소드 스텁
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			int N, L;
			N = sc.nextInt();
			L = sc.nextInt();
			int[] score_arr = new int[N];
			int[] k_arr = new int[N];
			for (int i = 0; i < N; i++) {
				score_arr[i] = sc.nextInt();
				k_arr[i] = sc.nextInt();
			}
			int max = 0;
			count = 0;
			powerset(k_arr, 0, L, new boolean[k_arr.length], score_arr, max);

			System.out.printf("#%d %d", tc, count);

		}

	}

	private static void powerset(int[] arr, int idx, int L1, boolean[] sel, int[] brr, int max1) {
		score = 0;

		if (idx == arr.length) {
			int sum = 0;

			for (int i = 0; i < sel.length; i++) {
				if (sel[i])

					if (sum + arr[i] <= L1) {
						sum += arr[i];
						score += brr[i];

					} else {
						break;
					}

			}

			if (count < score) {
				count = score;

			}

			return;
		}

		sel[idx] = true;
		powerset(arr, idx + 1, L1, sel, brr, max1);
		sel[idx] = false;
		powerset(arr, idx + 1, L1, sel, brr, max1);
	}

}
