package org.algorithm_test.java_test_baekjoon.eclipse;

import java.util.Scanner;

public class B_Test {
	static int[] dx = new int[] { 0, 1, 1, -1, }; // 아래, 오른, 우하, 우상
	static int[] dy = new int[] { 1, 0, 1, 1, };
	static int x_graph = 0;
	static int y_graph = 0;
	static int soo = 0;
	static int[] dx_re = new int[] { 0, -1, -1, 1 };
	static int[] dy_re = new int[] { -1, 0, -1, -1 };

	boolean chking(int arr[][], int index_i, int index_j, boolean flag) {
		int cnt = 1;

		for (int graph = 0; graph < 4; graph++) {

			int nx = index_i;
			int ny = index_j;

			if (nx + dx_re[graph] >= 0 && nx + dx_re[graph] < 19 && ny + dy_re[graph] >= 0 && ny + dy_re[graph] < 19
					&& arr[nx + dx_re[graph]][ny + dy_re[graph]] != arr[index_i][index_j]) {
				if(arr[nx + dx_re[graph]][ny + dy_re[graph]]== arr[index_i][index_j]) {
					comntinu
				}
			}
			for (int graph_index = 0; graph_index < 19; graph_index++) {
				nx += dx[graph];
				ny += dy[graph];
				if (nx < 0 || nx >= 19 || ny < 0 || ny >= 19 || arr[nx][ny] == 0
						|| arr[nx][ny] != arr[index_i][index_j]) {

					break;
				} else if (arr[nx][ny] == arr[index_i][index_j]) {
					cnt += 1;
				}
			}
			if (cnt == 5) {
				return true;
			}
		}

		return false;

	}

	public static void main(String[] args) {
		// TODO 자동 생성된 메소드 스텁
		Scanner sc = new Scanner(System.in);
		int arr[][] = new int[19][19];
		int x, y;
		boolean flag = false;
		B_Test fc = new B_Test();
		for (int i = 0; i < 19; i++) {
			for (int j = 0; j < 19; j++) {
				arr[i][j] = sc.nextInt();

			}
		}
		int flag_count = 0;

		for (int i = 0; i < 19; i++) {
			for (int j = 0; j < 19; j++) {
				if (arr[i][j] != 0) {
					// output Function
					flag = fc.chking(arr, i, j, flag);
					if (flag == true) {
						soo = arr[i][j];
						System.out.println(soo);
						System.out.printf("%d %d ", i + 1, j + 1);
						return;
					}

				}
			}
		}
		System.out.println("0");
	}

}
