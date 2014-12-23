/*
 * 由SharpDevelop创建。
 * 用户： lvp
 * 日期: 2014/12/23
 * 时间: 9:35
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;

class Method
{
	public static void ValueMethod(int i)
	{
		i++;
	}
	public static void ReferenceMethod(ref int i)
	{
		i++;
	}
	public static void OutputMethod(out int i)
	{
		i=0;
		i++;
	}
	static void Main()
	{
		int i=0;
		ValueMethod(i);
		Console.WriteLine("i="+i);
		int j=0;
		ReferenceMethod(ref j);
		Console.WriteLine("j="+j);
		int k;
		OutputMethod(out k);
		Console.WriteLine("k="+k);
	}
}