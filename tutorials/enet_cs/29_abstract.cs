/*
 * 由SharpDevelop创建。
 * 用户： IEUser
 * 日期: 1/6/2015
 * 时间: 6:28 PM
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;

abstract class A
{
	protected int _x;
	public abstract void F();
	public abstract int X
	{
		get;
		set;
	}
}

class B: A
{
	public override void F()
	{
		
	}
	public override int X
	{
		get 
		{
			return _x;
		}
		set
		{
			_x = value;
		}
	}
}

class Test
{
	static void Main()
	{
		B b = new B();
		b.X = 10;
		Console.WriteLine(b.X);
	}
}