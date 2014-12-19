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
	static void PrintArray(int ArrLength)
	{
		int[] arr=new int[ArrLength];
		for (int i=0;i<arr.Length;i++) 
			arr[i]=i;
		Console.WriteLine("Print Array's value");
		for (int i=0;i<arr.Length;i++)
			Console.WriteLine("arr[{0}]={1}", i, arr[i]);
	}
	static void Main() 
	{
		int i=1;
		while (i>0)
		{
			Console.WriteLine("Please enter the array's length:");
			try {
				i = Int32.Parse(Console.ReadLine());
				if (i <= 0)
					break;
				PrintArray(i);
			}
			catch (FormatException)
			{
				Console.WriteLine("Unable to convert {0}!", i);
			}
		}
	}
}