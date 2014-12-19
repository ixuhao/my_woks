/*
 * 由SharpDevelop创建。
 * 用户： lvp
 * 日期: 2014/12/19
 * 时间: 16:08
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;
using System.Collections;
class ArrList
{
	static void Main()
	{
		ArrayList arr = new ArrayList();
		string str1;
		while (true)
		{
			Console.WriteLine("Please add a string to ArrayList: ");
			str1 = Console.ReadLine();
			if (str1=="end")
				break;
			arr.Add(str1);
			Console.WriteLine();
			for (int i=0; i<arr.Count;i++)
				Console.Write("{0}", arr[i]);
			Console.WriteLine("\n");
		}
	}
}