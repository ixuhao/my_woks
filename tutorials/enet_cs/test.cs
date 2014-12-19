/*
 * 由SharpDevelop创建。
 * 用户： lvp
 * 日期: 2014/12/19
 * 时间: 13:44
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;

class Test
{
	static void Main() {
		//int[] arr = new int[] {1,2,3,4};
		int[] arr = {1,2,3,4};
		for (int i = 0; i < arr.Length; i++)
			Console.WriteLine(arr[i]);
		
		foreach ( int i in arr)
			Console.WriteLine(i);
		
	}
}