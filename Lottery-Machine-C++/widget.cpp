#include "widget.h"
#include "ui_widget.h"
#include <QMessageBox>
#include<QRandomGenerator>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
    setWindowTitle("Lottery Machine");
    QIntValidator *validator = new QIntValidator(0, 100, this);
    ui->mine->setValidator(validator);
    ui->maxe->setValidator(validator);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_quib_clicked()
{
    close();
}

void Widget::on_genb_clicked()
{
    int mi=ui->mine->text().toInt();
    int ma=ui->maxe->text().toInt()+1;
    int r=QRandomGenerator::global()->bounded(mi,ma)-49;
    char rc=r + '0';
    QMessageBox::information(this, tr("Generate"),tr("Number %1.").arg(rc+1),QMessageBox::Ok,QMessageBox::NoButton);
}
