package org.algorithm_test.java_test_baekjoon.eclipse;

import java.util.Scanner;

class B_2578 {
	static int[][] mat;
	static int count;

	public static void main(String[] args) {
		// TODO 자동 생성된 메소드 스텁
		Scanner sc = new Scanner(System.in);
		mat = new int[5][5];
		count = 0;

		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++) {
				mat[i][j] = sc.nextInt();
			}
		}
		for (int x = 1; x <= 25; x++) {
			int chk = sc.nextInt();
			for (int i = 0; i < 5; i++) {
				for (int j = 0; j < 5; j++) {
					if (mat[i][j] == chk)
						mat[i][j] = 0;
				}
			}
			if (x >= 10) {
				chk1();
				chk2();
				chk3();
				chk4();

			}
			if (count >= 3) {
				System.out.println(x);
				break;
			}
			count = 0;
		}
	}

	public static void chk1() {
		for (int i = 0; i < 5; i++) {
			int zeroC = 0;
			for (int j = 0; j < 5; j++)
				if (mat[i][j] == 0) {
					zeroC += 1;

				}
			if (zeroC == 5)
				count += 1;
		}
	}

	public static void chk2() {
		for (int i = 0; i < 5; i++) {
			int zeroC = 0;
			for (int j = 0; j < 5; j++) {
				if (mat[j][i] == 0)
					zeroC += 1;

			}
			if (zeroC == 5)
				count += 1;
		}
	}

	public static void chk3() {

		int zeroC = 0;
		for (int j = 0; j < 5; j++) {
			if (mat[j][j] == 0)
				zeroC += 1;

		}
		if (zeroC == 5)
			count += 1;
	}

	public static void chk4() {

		int zeroC = 0;
		for (int j = 0; j < 5; j++) {
			if (mat[j][4 - j] == 0) {
				zeroC += 1;
			}
		}
		if (zeroC == 5)
			count += 1;
	}

}
