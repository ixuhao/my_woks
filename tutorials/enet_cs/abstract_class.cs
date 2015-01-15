/*
 * 由SharpDevelop创建。
 * 用户： IEUser
 * 日期: 1/6/2015
 * 时间: 6:40 PM
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;

abstract class Employee
{
	protected string _name;
	protected Employee () {}
	protected Employee (string name)
	{
		_name = name;
	}
	public abstract void StartWork();
}

class Manager:Employee
{
	public Manager(string name): base(name) {}
	public override void StartWork()
	{
		Console.WriteLine(_name + " set tasks.");
	}
}

class Secretary:Employee
{
	public Secretary(string name): base(name) {}
	public override void StartWork()
	{
		Console.WriteLine(_name + " assist the manager.");
	}
}

class Sale:Employee
{
	public Sale(string name): base(name) {}
	public override void StartWork() 
	{
		Console.WriteLine(_name + " sale the product.");
	}
}

class Worker:Employee
{
	public Worker(string name): base(name) {}
	public override void StartWork()
	{
		Console.WriteLine(_name + " working hard...");
	}
}

class Test
{
	static void Main()
	{
		Employee[] emp = new Employee[4];
		emp[0] = new Manager("z3");
		emp[1] = new Secretary("li4");
		emp[2] = new Sale("wang5");
		emp[3] = new Worker("zhao6");
		Console.WriteLine("it is 8 am, start working");
		foreach (Employee e in emp)
		{
			e.StartWork();
		}
	}
}