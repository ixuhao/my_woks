/*
 * 由SharpDevelop创建。
 * 用户： IEUser
 * 日期: 1/6/2015
 * 时间: 6:55 PM
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;

class Employee
{
	protected string _name;
	public Employee() {}
	public Employee(string name) 
	{
		_name = name;
	}
	public virtual void StartWork()
	{
		Console.Write(_name + " start work: ");
	}
}

class Manager:Employee
{
	public Manager(string name): base(name) {}
	public override void StartWork()
	{
		base.StartWork();
		Console.WriteLine(" set the tasks.");
	}
}

class Secretary:Employee
{
	public Secretary(string name):base(name) {}
	public override void StartWork()
	{
		base.StartWork();
		Console.WriteLine(" assist the manager.");
	}
}

class Seller:Employee
{
	public Seller(string name):base(name) {}
	public override void StartWork()
	{
		base.StartWork();
		Console.WriteLine(" sell the product.");
	}
}

class Test
{
	static void Main()
	{
		Employee[] emp = new Employee[4];
		emp[0] = new Manager("zhang3");
		emp[1] = new Secretary("li4");
		emp[2] = new Seller("wang5");
		emp[3] = new Seller("ma6");
		
		Console.WriteLine("it's 8 am, start working.");
		foreach (Employee e in emp)
		{
			e.StartWork();
		}
	}
}