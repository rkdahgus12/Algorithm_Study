package org.algorithm_test.java_test_baekjoon.eclipse;

import java.util.Scanner;

public class B_2072 {
	static int[][] arr = new int[19][19];
	static boolean flag = false;
	static boolean chking;
	static int[] dx = new int[] { 0, 1, 1, 1, 0, -1, -1, -1 }; // 오,오아대,아,왼아대,왼,왼위대,위,오위대
	static int[] dy = new int[] { 1, 1, 0, -1, -1, -1, 0, 1 };

	public static boolean chk(int arr[][], int tc) {

		for (int i = 0; i < 19; i++) {
			for (int j = 0; j < 19; j++) {
				if (arr[i][j] == 0) {
					continue;
				} else if (arr[i][j] == tc) {

					for (int x = 0; x < 8; x++) {
						int cnt = 0;
						int nx = i, ny = j;

						for (int y = 0; y < 19; y++) {
							nx += dx[x];
							ny += dy[x];

							if (nx < 0 || nx >= 19 || ny < 0 || ny >= 19) {
								break;
							} else if (arr[nx][ny] == tc) {
								cnt++;
							} else if (arr[nx][ny] != tc) {
								break;
							}
						}
						if (cnt == 5) {
							flag = true;
							break;
						}

					}
				}

			}

		}

		return flag;
	}

	public static void main(String[] args) {
		// TODO 자동 생성된 메소드 스텁
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		int a, b;

		for (int tc = 0; tc < T; tc++) {
			a = sc.nextInt();
			b = sc.nextInt();
			if (tc >= 9) {
				chking = chk(arr, (tc % 2) + 1);
			}
			if (chking == true) {
				System.out.print(tc);
				break;
			}

			if (tc % 2 == 1) {
				arr[a][b] = 1;

			} else if (tc % 2 == 0) {
				arr[a][b] = 2;
			}
		}
//		for (int i = 0; i < 19; i++) {
//			for (int j = 0; j < 19; j++) {
//				System.out.print(arr[i][j]);
//			}
//			System.out.println();
//		}
	}

}
