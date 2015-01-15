/*
 * 由SharpDevelop创建。
 * 用户： IEUser
 * 日期: 1/7/2015
 * 时间: 4:42 PM
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;
using System.Collections;

class Student:IComparable
{
	private string _name;
	private int _age;
	public Student(string name, int age)
	{
		_name = name;
		_age = age;
	}
	public string Name
	{
		get { return _name; }
		set { _name=value; }
	}
	public int Age
	{
		get { return _age; }
		set { _age=value; }
	}
	int IComparable.CompareTo(object right)
	{
		if (!(right is Student))
		{
			throw new ArgumentException("Param must be Student type.");
		}
		return _name.CompareTo(((Student)right)._name);
	}
	public int CompareTo(Student right)
	{
		return _name.CompareTo(right._name);
	}
	private static AgeComparer _ageCom = null;
	public static IComparer AgeCom
	{
		get
		{
			if (_ageCom==null)
			{
				_ageCom = new AgeComparer();
			}
			return _ageCom;
		}
	}
	private class AgeComparer:IComparer
	{
		int IComparer.Compare(object left, object right)
		{
			if (!(left is Student) || !(right is Student))
			{
				throw new ArgumentException("Param must be Student type.");
			}
			return ((Student)left)._age.CompareTo(((Student)right)._age);
		}
	}
	public override string ToString()
	{
		return string.Format("[Student Name={0}]", _name);
	}
 
}


class Test
{
	static void Main()
	{
		Student[] arr = new Student[5];
		arr[0] = new Student("w5", 5);
		arr[1] = new Student("l4", 4);
		arr[2] = new Student("z3", 3);
		arr[3] = new Student("m6", 2);
		arr[4] = new Student("q7", 1);
		Array.Sort(arr);
		Console.WriteLine("sort by name.");
		foreach (Student s in arr)
		{
			Console.WriteLine(s);
//			Console.WriteLine(s.Name + " " + s.Age);
		}
		Console.WriteLine("sort by age.");
		Array.Sort(arr, Student.AgeCom);
		foreach (Student s in arr)
		{
			Console.WriteLine(s.Name + " " + s.Age);
		}
//		int[] arr={5, 3, 1, 4, 2};
//		Array.Sort(arr);
//		foreach (int i in arr)
//		{
//			Console.WriteLine(i);
//		}
	}
}