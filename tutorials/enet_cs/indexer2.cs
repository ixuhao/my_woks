/*
 * 由SharpDevelop创建。
 * 用户： IEUser
 * 日期: 12/25/2014
 * 时间: 1:14 AM
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;
using System.Collections;

class CourseScore
{
	private string name;
	private int courseID;
	private int score;
	public CourseScore(string name, int courseID, int score)
	{
		this.name = name;
		this.courseID = courseID;
		this.score = score;
	}
	public string Name
	{
		get { return name;}
		set { name=value; }
	}
	public int CourseID
	{
		get { return courseID; }
		set { courseID=value; }
	}
	public int Score
	{
		get { return score; }
		set { score=value; }
	}
}

class CourseScoreIndexer
{
	private ArrayList arrCourseScore;
	public CourseScoreIndexer()
	{
		arrCourseScore=new ArrayList();
	}
	public int this[string name, int courseID]
	{
		get
		{
			foreach (CourseScore cs in arrCourseScore)
			{
				if (cs.Name==name && cs.CourseID==courseID)
				{
					return cs.Score;
				}
			}
			return -1;
		}
		set 
		{
			arrCourseScore.Add(new CourseScore(name, courseID, value));
		}
	}
	public ArrayList this[string name]
	{
		get
		{
			ArrayList tempArr = new ArrayList();
			foreach (CourseScore cs in arrCourseScore)
			{
				if (cs.Name==name)
				{
					tempArr.Add(cs);
				}
			}
			return tempArr;
		}
	}
		
}

class Test
{
	static void Main()
	{
		CourseScoreIndexer csi = new CourseScoreIndexer();
		csi["张三", 1]=90;
		csi["张三", 2]=80;
		csi["张三", 3]=85;
		csi["李四", 1]=65;
		Console.WriteLine(csi["张三", 1]);
		
		Console.WriteLine("all 3's scores:");
		ArrayList tempArr;
		tempArr=csi["张三"];
		foreach (CourseScore cs in tempArr)
		{
			Console.WriteLine(cs.Name+", " + cs.CourseID + ", " + cs.Score);
		}
	}
}