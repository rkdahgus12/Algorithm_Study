package org.algorithm_test.java_test.eclipse;

import java.util.Scanner;

class swea_11315 {
	static int[] dx = { 0, 1, 1, 1 };
	static int[] dy = { 1, 0, 1, -1 };
//	static int[] dx = { 1 };
//	static int[] dy = { -1 };

	public static void main(String[] args) {
		// TODO 자동 생성된 메소드 스텁
		Scanner sc = new Scanner(System.in);
		int tc = sc.nextInt();
		for (int T = 1; T <= tc; T++) {
			int N = sc.nextInt();
			String st = sc.nextLine();
			char[][] arr = new char[N][N];
			for (int i = 0; i < N; i++) {
				arr[i] = (sc.nextLine()).toCharArray();
			}
			int cnt = 0;
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (arr[i][j] == 'o') {
						for (int x = 0; x < dx.length; x++) {
							cnt = 0;
							int nx = 0, ny = 0;

							for (int xx = 0; xx < 5; xx++) {
								if (i + nx < 0 || i + nx >= N || j + ny < 0 || j + ny >= N) {
									break;
								} else {

									if (arr[i + nx][j + ny] == 'o') {
										cnt += 1;
									}
									nx += dx[x];
									ny += dy[x];
								}
							}
							if (cnt >= 5) {
								break;
							}
						}
					}
					if (cnt >= 5) {
						break;
					}
				}
				if (cnt >= 5) {
					break;

				}
			}
			if (cnt >= 5) {

				System.out.printf("#%d YES\n", T);

			} else {

				System.out.printf("#%d NO\n", T);
			}
		}
	}
}

/*
 * 1 5 ....o ...o. ..o.. .o... o....
 */
