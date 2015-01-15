/*
 * 由SharpDevelop创建。
 * 用户： IEUser
 * 日期: 1/6/2015
 * 时间: 10:35 PM
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;

interface IA
{
	void F();
}

class B:IA
{
	void IA.F()
	{
		Console.WriteLine("B.F");
	}
}

class C:B, IA
{
	public void F()
	{
		Console.WriteLine("C.F");
	}
}


class Test
{
	static void Main()
	{
		C c = new C();
		((IA)c).F();
	}
}