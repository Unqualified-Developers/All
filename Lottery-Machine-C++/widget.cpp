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

int speakvar=0;

int generate(int min,int max)
{
    int r=min+rand()%(max-min+1)-49;
    return r;
}

void Widget::on_quib_clicked()
{
    close();
}

void Widget::on_genb_clicked()
{
    int mi=ui->mine->text().toInt();
    int ma=ui->maxe->text().toInt();
    int r=generate(mi,ma);
    char rc=r+'0';
    QMessageBox::information(this, tr("Generate"),tr("Number %1.").arg(rc+1),QMessageBox::Ok,QMessageBox::NoButton);
}

void Widget::on_gas_clicked()
{
    QTextToSpeech *speech;
    speakvar=speakvar+1;
    if(speakvar>=3)
    {
        ui->gas->setEnabled(false);
    }
    else
    {
        speech=new QTextToSpeech;
        int mi=ui->mine->text().toInt();
        int ma=ui->maxe->text().toInt();
        int r=generate(mi,ma)+48;
        QString sr=QString("%1").arg(r+1);
        speech->say(sr);
    }
}
