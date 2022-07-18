package org.algorithm_test.java_test.eclipse;

import java.util.Scanner;

public class SWEA_H_원재의메모리복구하기 {

	public static void main(String[] args) {
		// TODO 자동 생성된 메소드 스텁
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			String s = sc.next();
			int[] arr = new int[s.length()];
			for (int i = 0; i < s.length(); i++) {
				arr[i] = s.charAt(i) - '0';
				System.out.println(arr[i]);
			}
			int res = arr[0];
			for (int i = 1; i < arr.length; i++) {
				if (arr[i] != arr[i - 1])
					res++;
			}

			System.out.println("#" + tc + " " + res);
		}

	}
}