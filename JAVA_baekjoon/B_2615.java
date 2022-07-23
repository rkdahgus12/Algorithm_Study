package org.algorithm_test.java_test_baekjoon.eclipse;

import java.util.Scanner;

public class B_2615 {
	private static final int MAX_VALUE = 0;
	static int arr[][] = new int[21][21];
	static boolean flag = false;
	static boolean flag1 = false;
	static int[] dx = new int[] { 0, 0, -1, 1, -1, 1, 1, -1 }; // 오,왼,위,아,오위대,왼아대,오아대,왼위대
	static int[] dy = new int[] { 1, -1, 0, 0, 1, -1, 1, -1 };
	static int x_graph = 0;
	static int y_graph = 0;
	static int x_graph1 = 0;
	static int y_graph1 = 0;

	public static boolean chking(int arr[][], int chk_i, int chk_j, int soo) {
		int min = 0;
		int cnt = 1;
		for (int x = 0; x < 8; x++) {

			int nx = chk_i;
			int ny = chk_j;
			x_graph = nx;
			y_graph = ny;
			min = nx + ny;
			for (int y = 0; y < 19; y++) {
				nx += dx[x];
				ny += dy[x];
				if (nx < 0 || nx >= 19 || ny < 0 || ny >= 19 || arr[nx][ny] == 0 || arr[nx][ny] != soo) {
					min = 40;

					break;
				} else if (arr[nx][ny] != 0 && arr[nx][ny] == soo) {
					if (min > ny) {
						min = ny;
						x_graph = nx;
						y_graph = ny;

					}

					cnt++;
				}

			}
			if (x % 2 == 1) {
				if (cnt == 5) {
					flag = true;
					break;
				} else {
					cnt = 1;
				}
			}
		}
		return flag;
	}

	public static boolean chking1(int arr[][], int chk_i, int chk_j, int soo) {
		int min = 0;
		int cnt = 1;
		for (int x = 0; x < 8; x++) {

			int nx = chk_i;
			int ny = chk_j;
			x_graph1 = nx;
			y_graph1 = ny;
			min = nx + ny;
			for (int y = 0; y < 19; y++) {
				nx += dx[x];
				ny += dy[x];
				if (nx < 0 || nx >= 19 || ny < 0 || ny >= 19 || arr[nx][ny] == 0 || arr[nx][ny] != soo) {
					min = 40;

					break;
				} else if (arr[nx][ny] != 0 && arr[nx][ny] == soo) {
					if (min > ny) {
						min = ny;
						x_graph1 = nx;
						y_graph1 = ny;

					}

					cnt++;
				}

			}
			if (x % 2 == 1) {
				if (cnt == 5) {
					flag1 = true;
					break;
				} else {
					cnt = 1;
				}
			}
		}
		return flag1;
	}

	public static void main(String[] args) {
		// TODO 자동 생성된 메소드 스텁
		Scanner sc = new Scanner(System.in);
		for (int i = 0; i < 19; i++) {
			for (int j = 0; j < 19; j++) {
				arr[i][j] = sc.nextInt();
			}
		}
		int x = 0;
		int y = 0;
		int soo = 0;
		int soo1 = 0;
		int x_ = 0;
		int y_ = 0;
		int x_1 = 0;
		int y_1 = 0;
		for (int i = 0; i < 19; i++) {
			for (int j = 0; j < 19; j++) {
				if (arr[i][j] == 1 && flag == false) {

					soo = arr[i][j];
					flag = chking(arr, i, j, soo);
					if (flag == true) {
						continue;

					}
				} else if (arr[i][j] == 2 && flag1 == false) {
					soo1 = arr[i][j];
					flag1 = chking1(arr, i, j, soo1);
					if (flag1 == true) {
						continue;

					}
				}
			}
			if (flag == true || flag1 == true) {
				break;
			}
		}
		if (flag == flag1) {
			System.out.println("0");
		} else if (flag == true) {
			x_ = x_graph;
			y_ = y_graph;
			System.out.println(soo);
			System.out.printf("%d %d", x_ + 1, y_ + 1);
		} else if (flag1 == true) {
			x_1 = x_graph1;
			y_1 = y_graph1;
			System.out.println(soo1);
			System.out.printf("%d %d", x_1 + 1, y_1 + 1);
		}

	}

}
