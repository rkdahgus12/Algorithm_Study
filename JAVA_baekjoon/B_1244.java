package org.algorithm_test.java_test_baekjoon.eclipse;

import java.util.Scanner;

class B_1244 {
	static int arr_size;

	public static void main(String[] args) {
		// TODO 자동 생성된 메소드 스텁
		Scanner sc = new Scanner(System.in);
		arr_size = sc.nextInt();
		int[] arr = new int[arr_size];
		for (int i = 0; i < arr_size; i++) {
			arr[i] = sc.nextInt();
		}
		int soo = sc.nextInt();
		for (int i = 0; i < soo; i++) {
			int se, sw; // 학생 성별 스위치 번호

			se = sc.nextInt();
			sw = sc.nextInt();

			if (se == 1) {
				for (int x = sw; x <= arr_size; x += sw) {

					if (arr[x - 1] == 1) {
						arr[x - 1] = 0;
					} else {
						arr[x - 1] = 1;
					}

				}
			} else {
				if (arr_size / 2 >= sw) {
					int count = 0;
					int plus_soo = 1;
					for (int x = sw - 1; x >= 0; x--) {
						if (arr[x - 1] == arr[x + plus_soo]) {
							if (arr[x - 1] == 0) {
								arr[x - 1] = 1;
								arr[x + plus_soo] = 1;
								plus_soo++;
							} else if (arr[x - 1] == 1) {
								arr[x - 1] = 0;
								arr[x + plus_soo] = 0;
								plus_soo++;
							}
							count += 1;
						} else {
							for (int y = x; y < x * 2; y++) {
								if (arr[y] == 0) {
									arr[y] = 1;
								} else {
									arr[y] = 0;
								}
							}
							break;
						}
					}
//				} else {
//					for (int x = sw - 1; x < arr_size; x++) {
//
//					}
//				}
				}

			}
		}

		for (int k = 0; k < arr_size; k++) {
			System.out.print(arr[k] + " ");

		}

	}
}
/*
 * 8 0 1 0 1 0 0 0 1 1 1 3
 */