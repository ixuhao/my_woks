/*
 * 由SharpDevelop创建。
 * 用户： IEUser
 * 日期: 1/7/2015
 * 时间: 15:40 PM
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;

interface IEmployee
{

	void StartWork();
}

class Manager:IEmployee
{
	private string _name;
	public Manager(string name)
	{
		_name = name;
	}
	
	public void StartWork()
	{
		Console.WriteLine(_name + " set tasks.");
	}
}

class Secretary:IEmployee
{
	private string _name;
	public Secretary(string name)
	{
		_name=name;
	}
	public void StartWork()
	{
		Console.WriteLine(_name + " assist the manager.");
	}
}

class Sale:IEmployee
{
	private string _name;
	public Sale(string name)
	{
		_name = name;
	}
	public void StartWork() 
	{
		Console.WriteLine(_name + " sale the product.");
	}
}

class Worker:IEmployee
{
	private string _name;
	public Worker(string name)
	{
		_name =name;
	}
	public void StartWork()
	{
		Console.WriteLine(_name + " working hard...");
	}
}

class Test
{
	static void Main()
	{
		IEmployee[] emp = new IEmployee[4];
		emp[0] = new Manager("z3");
		emp[1] = new Secretary("li4");
		emp[2] = new Sale("wang5");
		emp[3] = new Worker("zhao6");
		Console.WriteLine("it is 8 am, start working");
		foreach (IEmployee e in emp)
		{
			e.StartWork();
		}
	}
}

