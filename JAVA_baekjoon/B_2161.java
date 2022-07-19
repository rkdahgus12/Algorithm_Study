package org.algorithm_test.java_test_baekjoon.eclipse;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class B_2161 {

	public static void main(String[] args) {
		Queue<Integer> queue = new LinkedList<Integer>();
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		int[] arr = new int[T];
		for (int i = 1; i <= T; i++) {
			queue.add(i);
		}
		String a = "";
		while (queue.size() != 1) {
			a += queue.poll().toString() + " ";
			queue.add(queue.poll());
		}
		System.out.print(a + queue.poll());
	}

}
