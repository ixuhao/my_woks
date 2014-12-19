/*
 * 由SharpDevelop创建。
 * 用户： lvp
 * 日期: 2014/12/19
 * 时间: 16:21
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;
class Matrix
{
	static void Main()
	{
		int[,] arr=new int[4,6];
		for (int i=0;i<4;i++)
		{
			for (int j=0;j<6;j++)
			{
				arr[i,j]=(i+1)*10+j+1;
			}
		}
		
		for (int i=0;i<4;i++)
		{
			for (int j=0;j<6;j++)
			{
				Console.Write("{0}    ", arr[i, j]);
			}
			Console.WriteLine();
		}
	}
}