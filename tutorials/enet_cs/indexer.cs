/*
 * 由SharpDevelop创建。
 * 用户： IEUser
 * 日期: 12/24/2014
 * 时间: 9:10 PM
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;
using System.Collections;

class IsndexClass
{
	private Hashtable name = new Hashtable();
	
	public string this[int index] {
		get { return name[index].ToString(); }
		set { name.Add(index, value); }
	}
	public int this[string searchName] {
		get
		{
			foreach (DictionaryEntry de in name)
			{
				if (de.Value.ToString()==searchName)
				{
					//Console.WriteLine(de.Value.ToString());
					return Convert.ToInt32(de.Key);
				}
			}
			return -1;
		}
		
		set { name.Add(value, searchName); }
		
	}
}

class Test
{
	static void Main()
	{
		IsndexClass user = new IsndexClass();
		user[100] = "tom";
		user[200] = "peter";
		user[300] = "jerry";
		Console.WriteLine(user[100]);
		
		Console.WriteLine(user["peter"]);
		user["ala"] = 400;
		user["qqq"] = 500;
		Console.WriteLine(user[400]);
		Console.WriteLine(user["qqq"]);
		Console.WriteLine(user["www"]);
	}
}