/*
 * 由SharpDevelop创建。
 * 用户： lvp
 * 日期: 2014/12/19
 * 时间: 16:57
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;
class Method
{
	static void Main()
	{
		Console.WriteLine("Now is {0}.", MyMethod());
		string TempName="";
		while (TempName != "end")
		{
			TempName = Console.ReadLine();
			MyMethod1(TempName);
		}
	}
	
	public static DateTime MyMethod()
	{
		return DateTime.Now;
	}
	
	public static void MyMethod1(string Aname)
	{
		Console.WriteLine("the name is " + Aname + "\n");
	}
}