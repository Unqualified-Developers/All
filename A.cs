// 确定字体和每行高度
var font = new Font(richTextBox.Font.FontFamily, richTextBox.Font.Size);
var lineHeight = font.Height;
// 绘制行号
for(int i = 0; i < richTextBox.Lines.Length; i++)
{
    e.Graphics.DrawString((i + 1).ToString(), font, Brushes.White, new Point(0, i * lineHeight));
}

tableLayoutPanel1.Controls.Add(panelLineNumber, 0, 0);
tableLayoutPanelpanelLineNumber.Controls.Add(pictureBoxLineNumbers, 0, 0);
tableLayoutPanelpanelLineNumber.Controls.Add(richTextBox, 1, 0);

private void richTextBox_Scroll(object sender, EventArgs e)
{
    pictureBoxLineNumbers.Top = -richTextBox.VerticalScroll.Value;
}
