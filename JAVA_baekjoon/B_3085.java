package org.algorithm_test.java_test_baekjoon.eclipse;

import java.util.Scanner;

class B_3085 {
	static int T;
	static int max;
	static char[][] arr;

	public static void chkarr(char[][] arr) {

		for (int i = 0; i < T; i++) {
			int count = 1;
			for (int j = 0; j < T - 1; j++) {
				if (arr[i][j] == arr[i][j + 1]) {
					count++;
				} else {
					count = 1;
				}
				max = Math.max(max, count);
			}
		}
		for (int i = 0; i < T; i++) {
			int count = 1;
			for (int j = 0; j < T - 1; j++) {
				if (arr[j][i] == arr[j + 1][i]) {
					count++;
				} else {
					count = 1;
				}
				max = Math.max(max, count);
			}
		}
	}

	public static void main(String[] args) {
		// TODO 자동 생성된 메소드 스텁
		Scanner sc = new Scanner(System.in);
		T = sc.nextInt();
		String st = sc.nextLine();
		arr = new char[T][T];
		for (int i = 0; i < T; i++) {
			arr[i] = (sc.nextLine()).toCharArray();
		}
		// 가로 체킹
		for (int i = 0; i < T; i++) {
			for (int j = 0; j < T - 1; j++) {
				if (arr[i][j] != arr[i][j + 1]) {

					char temp = arr[i][j];
					arr[i][j] = arr[i][j + 1];
					arr[i][j + 1] = temp;
					chkarr(arr);

					char temp1 = arr[i][j];
					arr[i][j] = arr[i][j + 1];
					arr[i][j + 1] = temp1;

				}

			}
		}

		// 세로 체킹
		for (int i = 0; i < T; i++) {
			for (int j = 0; j < T - 1; j++) {
				if (arr[j][i] != arr[j + 1][i]) {
					// swap(arr[j][i], arr[j + 1][i]);
					char temp = arr[j][i];
					arr[j][i] = arr[j + 1][i];
					arr[j + 1][i] = temp;
					chkarr(arr);
					char temp1 = arr[j][i];
					arr[j][i] = arr[j + 1][i];
					arr[j + 1][i] = temp1;
					// swap(arr[j + 1][i], arr[j][i]);

				}

			}
		}
		System.out.println(max);

//		for (int i = 0; i < T; i++) {
//			for (int j = 0; j < T; j++) {
//				System.out.printf("%s", arr[i][j]);
//			}
//			System.out.println();
//		}

	}

}
