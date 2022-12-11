#include "widget.h"
#include "ui_widget.h"
#include <QMessageBox>
#include <stdlib.h>
#include <QtTextToSpeech/QTextToSpeech>

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

int generate(int min,int max,int n)
{
    int r=min+rand()%(max-min+1);
    while (r==n)
    {
        r=min+rand()%(max-min+1);
    }
    return r-49;
}

void Widget::on_quib_clicked()
{
    close();
}

void Widget::on_genb_clicked()
{
    int mi=ui->mine->text().toInt();
    int ma=ui->maxe->text().toInt();
    int n=ui->noe->text().toInt();
    int r=generate(mi,ma,n);
    char rc=r+'0';
    QMessageBox::information(this, tr("Generate"),tr("Number %1.").arg(rc+1),QMessageBox::Ok,QMessageBox::NoButton);
}

void Widget::on_gas_clicked()
{
    QTextToSpeech *speech;
    speech=new QTextToSpeech;
    int mi=ui->mine->text().toInt();
    int ma=ui->maxe->text().toInt();
    int n=ui->noe->text().toInt();
    int r=generate(mi,ma,n)+48;
    QString sr=QString("%1").arg(r+1);
    speech->say(sr);
    ui->gas->setEnabled(false);
}
