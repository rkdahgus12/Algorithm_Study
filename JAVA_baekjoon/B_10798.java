package org.algorithm_test.java_test_baekjoon.eclipse;

import java.util.Arrays;
import java.util.Scanner;

public class B_10798 {

	public static void main(String[] args) {
		// TODO 자동 생성된 메소드 스텁
		Scanner sc = new Scanner(System.in);
		String[][] arr = new String[5][15];
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < arr.length; j++) {
				arr[i][j] = sc.next();
			}
		}
		System.out.print(Arrays.toString(arr));
	}

}
