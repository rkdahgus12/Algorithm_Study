package org.algorithm_test.java_test.eclipse;

import java.util.Scanner;

class swea_1961 {
	public static int[][] case1(int[][] arr) {
		int[][] result = new int[arr.length][arr.length];
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr.length; j++) {
				result[i][j] = arr[arr.length - j - 1][i];
			}
		}
		return result;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		for (int i = 1; i < T + 1; i++) {
			int soo = sc.nextInt();
			int[][] arr = new int[8][8];
			for (int j = 0; j < soo; j++) {
				for (int k = 0; k < soo; k++) {
					arr[j][k] = sc.nextInt();
				}
			}
			int[][] arr90 = case1(arr);
			int[][] arr180 = case1(arr90);
			int[][] arr270 = case1(arr180);
			System.out.printf("#%d\n", i);
			for (int k = 0; k < soo; k++) {
				for (int j = 0; j < soo; j++) {
					System.out.print(arr90[k][j]);
				}
				System.out.print(" ");
				for (int j = 0; j < soo; j++) {
					System.out.print(arr180[k][j]);
				}
				System.out.print(" ");
				for (int j = 0; j < soo; j++) {
					System.out.print(arr270[k][j]);
				}
				System.out.println();
			}

		}
	}
}
