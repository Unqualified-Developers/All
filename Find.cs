using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        int[] rl = { 1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 7,8, 9, 5 };

        List<int> duplicates = new List<int>();
        Random random = new Random();

        for (int i = 0; i < rl.Length; i++)
        {
            for (int j = i + 1; j < rl.Length; j++)
            {
                if (rl[i] == rl[j] && !duplicates.Contains(rl[i]))
                {
                    duplicates.Add(rl[i]);
                    rl[j] = random.Next(1, 6);
                }
            }
        }

        Console.WriteLine("重复的元素已替换为1到5之间的随机数：");
        foreach (int num in rl)
        {
            Console.Write(num + " ");
        }
    }
}
