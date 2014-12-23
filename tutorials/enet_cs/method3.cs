/*
 * 由SharpDevelop创建。
 * 用户： lvp
 * 日期: 2014/12/23
 * 时间: 9:47
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;

class Method
{
	static int addi(params int[] values)
	{
		int sum=0;
		foreach (int i in values)
			sum+=i;
		return sum;
	}
	static void PrintArr(int[] arr)
	{
		for (int i=0;i<arr.Length;i++)
			arr[i]=i;
	}
	static void Main()
	{
		Console.WriteLine(addi(1));
		Console.WriteLine(addi(1,2,3,4,5));
		int[] arr={100, 200, 300, 400};
		PrintArr(arr);
		foreach (int i in arr)
			Console.Write(i+",");
	}
}
