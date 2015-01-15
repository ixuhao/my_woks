/*
 * Created by SharpDevelop.
 * User: IEUser
 * Date: 1/8/2015
 * Time: 5:16 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */

using System;
using System.Collections;
interface IName
{
	string Name
	{
		get; set;
	}
}
struct Person
{
	private string _name;
	public Person(string name)
	{
		_name = name;
	}
	public string Name
	{
		get { return _name; }
		set { _name=value; }
	}
}
class Test
{
	static void Main()
	{
		object o=100; // box
		int i = (int)o; // unbox
		
		int a = 123;
		object b = a; // box
		a = 456;
		Console.WriteLine(a.ToString() + //string.concate (object, object, object) nobox edition
		                  ",   " + 
		                  b);
		
		ArrayList arr = new ArrayList();
		
		Person p = new Person("z3"); // p is ValueType, because struct is ValueType.
		p.GetType(); // box -> Object.GetType()
		p.ToString(); //nobox -> ValueType.ToString()
		
		arr.Add(p); // box -> Add(object)
		p.Name = "li4";
		Console.WriteLine(p.Name);
		// To change (Person)arr[0] name
		Person p1 = new Person("li4");
		arr[0] = p1;
		Console.WriteLine(((Person)arr[0]).Name);
		
		// using array, becase array is type-safe.
		Person[] brr = new Person[1];
		Person p2 = new Person("z3");
		brr[0] = p2;
		Console.WriteLine(((Person)brr[0]).Name);
		brr[0].Name = "li4";
		Console.WriteLine(((Person)brr[0]).Name);
		
		
		// using Interface, not a good way, just example.
		// if define Person as class, not struct, will not have these troubles.
//		ArrayList crr = new ArrayList();
//		Person p3 = new Person("p3");
//		crr.Add(p3);
//		((IName)crr[0]).Name="li4";
//		Console.WriteLine(((Person)crr[0]).Name);
	}
}