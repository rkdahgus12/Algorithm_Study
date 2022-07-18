package org.algorithm_test.java_test_baekjoon.eclipse;

import java.util.Scanner;

class B_1010 {
	static double n;
	static double m;

	public static void main(String[] args) {
		// TODO 자동 생성된 메소드 스텁
		Scanner sc = new Scanner(System.in);
		int tc = sc.nextInt();
		for (int i = 0; i < tc; i++) {
			n = sc.nextDouble();
			m = sc.nextDouble();
			System.out.printf("%.0f\n", Combi(m, n));
		}
	}

	public static double Combi(double n, double r) {
		double a = 1;
		double b = 1;
		for (double j = n; j > n - r; j--) {
			a *= j;
		}
		for (double j = r; j > 0; j--) {
			b *= j;
		}
		return a / b;
	}
}
