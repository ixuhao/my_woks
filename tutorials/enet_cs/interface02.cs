/*
 * 由SharpDevelop创建。
 * 用户： IEUser
 * 日期: 1/6/2015
 * 时间: 10:39 PM
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;

interface IA
{
	void F();
}


interface IB:IA
{
	new void F();
}

interface IC:IA
{
	void G();
}

interface IBC:IB, IC
{
	
}

class Derive: IBC
{
	public void F()
	{
		Console.WriteLine("IB.F()");
	}
	
	public void G()
	{
		Console.WriteLine("IC.G()");
	}
}

class Test
{
	static void Main()
	{
		Derive d = new Derive();
		d.F();
		((IA)d).F();
		((IB)d).F();
		((IC)d).F();
		((IBC)d).F();
	}
}