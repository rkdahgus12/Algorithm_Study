package algo_class;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class B_1600 {
	static int K;
	static int W, H;
	static int[][] map;
	static int res = -1;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		K = sc.nextInt();
		W = sc.nextInt();
		H = sc.nextInt();
		map = new int[H][W];
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				map[i][j] = sc.nextInt();
			}
		}
//        �ַ��
		bfs();
		System.out.println(res);

	}

	static int[] dx = { 0, 0, -1, 1 }; // �����¿�
	static int[] dy = { -1, 1, 0, 0 };
	static int[] hdx = { -2, -1, 1, 2, 2, 1, -1, -2 };
	static int[] hdy = { -1, -2, -2, -1, 1, 2, 2, 1 };

	private static void bfs() {
		Queue<Data> q = new LinkedList<Data>();
//        ť����
		boolean[][][] v = new boolean[K + 1][H][W]; // k, x, y
//        �湮üũ �ʱ�ȭ

		q.offer(new Data(0, 0, 0, 0));
		v[0][0][0] = true;

//        ť �ݺ�
		Data cur;
		while (!q.isEmpty()) {
//            ������ Ȯ��
			cur = q.poll();
			if (cur.x == W - 1 && cur.y == H - 1) {
				res = cur.cnt;
				break;
			}
//            ������ �̵�
			int nx, ny;
			for (int d = 0; d < 4; d++) {
				nx = cur.x + dx[d];
				ny = cur.y + dy[d];
//                ����üũ
				if (nx < 0 || nx >= W || ny < 0 || ny >= H) {
					continue;
				}
//                �湮üũ
				if (v[cur.k][ny][nx]) {
					continue;
				}
//                ��ֹ�üũ
				if (map[ny][nx] == 1) {
					continue;
				}
//                ť�� ����
				q.offer(new Data(nx, ny, cur.cnt + 1, cur.k)); // ġƮŰ ������
				v[cur.k][ny][nx] = true;

			}
//            �� �̵�(if k)
			if (cur.k + 1 <= K) { // ġƮŰ ��밡���ϸ� ���̵�
				for (int d = 0; d < 8; d++) {
					nx = cur.x + hdx[d];
					ny = cur.y + hdy[d];
//                    ����üũ
					if (nx < 0 || nx >= W || ny < 0 || ny >= H) {
						continue;
					}
//                    �湮üũ
					if (v[cur.k + 1][ny][nx]) {
						continue;
					}
//                    ��ֹ�üũ
					if (map[ny][nx] == 1) {
						continue;
					}
//                    ť�� ����
					q.offer(new Data(nx, ny, cur.cnt + 1, cur.k + 1)); // ġƮŰ ��� ��
					v[cur.k + 1][ny][nx] = true;
				}
			}
		}

	}

	static class Data {
		int x, y;
		int cnt;
		int k; // ġƮŰ Ƚ��

		public Data(int x, int y, int cnt, int k) {
			this.x = x;
			this.y = y;
			this.cnt = cnt;
			this.k = k;
		}

	}

}
