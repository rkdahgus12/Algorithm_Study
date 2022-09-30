package algo_class;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_17070 {

	static int map[][];
	static int dp[][];
	static int t;

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		t = Integer.parseInt(br.readLine());
		map = new int[t][t];
		dp = new int[t][t];
		for (int i = 0; i < t; i++) {
			StringTokenizer tokenizer = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < t; j++) {
				map[i][j] = Integer.parseInt(tokenizer.nextToken());
			}
		}
		dfs(0, 1, 0);
		System.out.println(dp[t - 1][t - 1]);
	}

	public static void dfs(int r, int c, int rotate) {
		if (r >= t || c >= t || map[r][c] == 1)	return;
		if (rotate == 0) {// 가로
			dfs(r, c + 1, 0);
			dfs(r + 1, c + 1, 1);
		} else if (rotate == 1) {// 세로
			if (map[r - 1][c] == 1 || map[r][c - 1] == 1) return;
			dfs(r, c + 1, 0);
			dfs(r + 1, c + 1, 1);
			dfs(r + 1, c, 2);
		} else {// 대각선
			dfs(r + 1, c + 1, 1);
			dfs(r + 1, c, 2);

		}
		dp[r][c] ++;

	}

}
