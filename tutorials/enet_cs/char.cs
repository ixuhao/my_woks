/*
 * 由SharpDevelop创建。
 * 用户： lvp
 * 日期: 2014/12/23
 * 时间: 10:02
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;
class Test
{
	static void PrintCJK()
	{
		Console.WriteLine((int)'你');
		Console.WriteLine("\u4F60\u597D");
//		for (int i=0;i<65536;i++)
//		{
//			Console.WriteLine(i);
//		}
	}
	static void Main()
	{
		PrintCJK();
		char c='A';
		Console.WriteLine(c);
		Console.WriteLine((int)c);
		Console.WriteLine('\x41');
		Console.WriteLine((char)65); // this is better and faster for ascii char. 
		Console.WriteLine(Convert.ToChar(65));
		
		for (int i=0;i<128;i++)
		{
			if (i%10==0)
			{
				Console.WriteLine();
			}
			Console.Write("{0,3}:{1,-3}",i,(char)i);
		}
	}
}