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

        private void button2_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string mins = mint.Text.ToString();
            string maxs = maxt.Text.ToString();
            int mini, maxi;
            bool minb = int.TryParse(mins,out mini);
            bool maxb = int.TryParse(maxs, out maxi);
            if (minb==true&&maxb==true)
            {
                mini=int.Parse(mins);
                maxi=int.Parse(maxs);
                Random rd = new Random();
                int r = rd.Next(mini, maxi + 1);
                string rs = r.ToString();
                MessageBox.Show($"Number {rs}.", "Generate", 0, MessageBoxIcon.Information);
            }
            else
            {
                MessageBox.Show("Please enter correct numbers.");
            }
        }
    }
}
