package org.algorithm_test.java_test.eclipse;

import java.util.Scanner;

class swea_10804 {

	public static String reverse(String str) {
		return new StringBuilder(str).reverse().toString();
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc = 1; tc < T + 1; tc++) {
			String str = sc.next();
			str = reverse(str);
			System.out.printf("#%d %s", tc, str);
		}

	}
}
