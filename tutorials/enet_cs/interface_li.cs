/*
 * 由SharpDevelop创建。
 * 用户： IEUser
 * 日期: 1/6/2015
 * 时间: 9:30 PM
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;

interface IDrivingLicenseB
{
	void GetLicense();
	
}
interface IDrivingLicenseA:IDrivingLicenseB
{
	new void GetLicense();
	
}

class Teacher:IDrivingLicenseA
{
	void IDrivingLicenseB.GetLicense()
	{
		Console.WriteLine("Teacher gets a driving license B.");
	}
	void IDrivingLicenseA.GetLicense()
	{
		Console.WriteLine("Teacher gets a driving license A.");
	}
	public void GetLicense()
	{
		Console.WriteLine("this is not a interface method.");
	}
}
class Student:IDrivingLicenseB
{
	public void GetLicense()
	{
		Console.WriteLine("Student gets a driving license B.");
	}
		
}

class Test
{
	static void DriveCar(string name, IDrivingLicenseB o)
	{
		IDrivingLicenseB dl = o as IDrivingLicenseB;
		if (dl != null)
		{
			Console.WriteLine(name + "kache is driving.");
		}
		else
		{
			Console.WriteLine(name + " have no license, can not drive kache.");
		}
	}
	static void DriveBus(string name, IDrivingLicenseB o)
	{
		IDrivingLicenseA dl = o as IDrivingLicenseA;
		if (dl != null)
		{
			Console.WriteLine(name + "Bus is driving.");
		}
		else
		{
			Console.WriteLine(name + " have no license, can not drive bus.");
		}
	}
	static void Main()
	{
		Teacher t = new Teacher();
		((IDrivingLicenseB)t).GetLicense();
		((IDrivingLicenseA)t).GetLicense();
		t.GetLicense();
		DriveCar("teacher", t);
		DriveBus("teacher", t);
		Student s = new Student();
		DriveCar("student", s);
		DriveBus("student", s);
	}
}