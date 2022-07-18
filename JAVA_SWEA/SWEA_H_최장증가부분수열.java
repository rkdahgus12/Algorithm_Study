package org.algorithm_test.java_test.eclipse;

import java.util.Arrays;
import java.util.Scanner;

public class SWEA_H_최장증가부분수열 {

	public static void main(String[] args) {
		// TODO 자동 생성된 메소드 스텁
		Scanner sc = new Scanner(System.in);
		int tc = sc.nextInt();
		for (int T = 1; T <= tc; T++) {
			int soo = sc.nextInt();
			int[] arr = new int[soo];
			int[] res = new int[soo];
			Arrays.fill(res, 1);
			for (int i = 0; i < soo; i++) {
				arr[i] = sc.nextInt();
			}
			for (int i = 0; i < soo; i++) {
				for (int j = 0; j < i; j++) {
					if (arr[j] < arr[i]) {
						res[i] = Math.max(res[i], res[j] + 1);
						// System.out.printf("%d", res[i]);
					}
				}

			}
			int max = res[0];
			for (int x : res) {
				if (x > max) {
					max = x;
				}
			}
			System.out.printf("#%d %d\n", T, max);
		}
	}

}
