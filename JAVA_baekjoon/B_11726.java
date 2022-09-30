package algo_class;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class B_11726 {

	static ArrayList<Integer> list;

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		list = new ArrayList<>();
		list.add(0);
		list.add(1);
		list.add(2);

		for (int i = 3; i < 1001; i++) {
			list.add((list.get(i - 2) + list.get(i - 1))%10007);
		}
		int soo = Integer.parseInt(br.readLine());
		System.out.println(list.get(soo));
		

	}

}
