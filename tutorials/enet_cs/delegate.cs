/*
 * 由SharpDevelop创建。
 * 用户： IEUser
 * 日期: 12/25/2014
 * 时间: 6:49 PM
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;
delegate void EatDelegate(string food);

class Man
{
	private string name;
	public Man(string name)
	{
		this.name = name;
	}
	public void Eat(string food)
	{
		Console.WriteLine(name+" Eat "+food);
	}
}

class Party
{
	static void eatTogether(string food, params EatDelegate[] values)
	{
		if (values==null)
		{
			Console.WriteLine("Party is over.");
		}
		else
		{
			EatDelegate eatChain = null;
			foreach (EatDelegate ed in values)
				eatChain += ed;
			eatChain(food);
			Console.WriteLine();
		}
	}
	static void Main()
	{
		Man ZS=new Man("tom");
		Man LS=new Man("john");
		Man WW=new Man("hill");
		EatDelegate zs = new EatDelegate(ZS.Eat);
		EatDelegate ls = new EatDelegate(LS.Eat);
		EatDelegate ww = new EatDelegate(WW.Eat);
		
		Console.WriteLine("Party is begin.");
		eatTogether("apple", zs, ls, ww);
		
		Console.WriteLine("john is out.");
		eatTogether("tomato", zs, ww);
		
		Console.WriteLine("john is back.");
		eatTogether("orange", zs, ls, ww);
		
		eatTogether(null, null);
	}
}