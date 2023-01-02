using System;
using System.Windows.Forms;

namespace Lottery_Machine
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public int generate(int min, int max, int n)
        {
            int i = 0;
            Random r = new Random();
            int re = r.Next(min, max + 1);
            while((re==n) && i<=10000000)
            {
                re = r.Next(min, max + 1);
                i++;
            }
            if(i>=10000000)
            {
                return -2147483648;
            }
            else
            {
                return re;
            }
        }
        private void button2_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string mins = mint.Text.ToString();
            string maxs = maxt.Text.ToString();
            string dwss = dwst.Text.ToString();
            int mini, maxi, dwsi;
            bool minb = int.TryParse(mins,out mini);
            bool maxb = int.TryParse(maxs, out maxi);
            bool dwsb = int.TryParse(dwss, out dwsi);
            if (minb==true && maxb==true)
            {
                mini = int.Parse(mins);
                maxi = int.Parse(maxs);
                if (mini<=maxi)
                {
                    if (dwsb == false)
                    {
                        dwsi = -2147483648;
                    }
                    else
                    {
                        dwsi = int.Parse(dwss);
                    }
                    Random rd = new Random();
                    int r = generate(mini, maxi, dwsi);
                    if (mini == -2147483648 || maxi == -2147483648)
                    {
                        MessageBox.Show("The value you entered is not in the valid range.\nValid range: - 2147483647~2147483648.", "Range", 0, MessageBoxIcon.Warning);
                    }
                    else
                    {
                        if (r == -2147483648)
                        {
                            MessageBox.Show("This is not a joke.", "Joke", 0, MessageBoxIcon.Warning);
                        }
                        else
                        {
                            MessageBox.Show($"Number {r}.", "Generate", 0, MessageBoxIcon.Information);
                        }
                    }
                }
                else
                {
                    MessageBox.Show("Why did 'Minimum' < 'Maximum'?", "Check", 0, MessageBoxIcon.Warning);
                }
            }
            else
            {
                MessageBox.Show("Please enter correct numbers.", "Check", 0, MessageBoxIcon.Warning);
            }
        }
    }
}
