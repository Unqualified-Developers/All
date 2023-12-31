using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        int[] rl = { 1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 7,8, 9, 5 };

        Random random = new Random();

        for (int i = 0; i < rl.Length; i++)
        {
            for (int j = i + 1; j < rl.Length; j++)
            {
                if (rl[i] == rl[j])
                {
                    rl[j] = random.Next(1, 6);
                }
            }
        }
    }
}
