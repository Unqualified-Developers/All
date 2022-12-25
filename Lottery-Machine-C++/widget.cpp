#include "widget.h"
#include "ui_widget.h"
#include <QMessageBox>
#include <stdlib.h>
#include <QtTextToSpeech/QTextToSpeech>

int min,max;

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
    setWindowTitle("Lottery Machine");
    QIntValidator *validator = new QIntValidator(0, 100, this);
    ui->mine->setValidator(validator);
    ui->maxe->setValidator(validator);
    ui->noe->setValidator(validator);
}

Widget::~Widget()
{
    delete ui;
}

int generate(int min,int max,int n)
{
    int r=min+rand()%(max-min+1);
    int i=0;
    while (r==n)
    {
        r=min+rand()%(max-min+1);
        i++;
        if(i>=10000000)
        {
            return -1;
        }
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
    if(mi&&ma)
    {
        int r=generate(mi,ma,n);
        if(r==-1)
        {
            QMessageBox::warning(this, tr("Joke"),tr("This is not a joke."),QMessageBox::Ok,QMessageBox::NoButton);
        }
        else
        {
            char rc=r+'0';
            QMessageBox::information(this, tr("Generate"),tr("Number %1.").arg(rc+1),QMessageBox::Ok,QMessageBox::NoButton);
        }
    }
    else
    {
        QMessageBox::question(this, tr("Input"),tr("Where is the value?"),QMessageBox::Ok,QMessageBox::NoButton);
    }
}

void Widget::on_gas_clicked()
{
    QTextToSpeech *speech;
    speech=new QTextToSpeech;
    int mi=ui->mine->text().toInt();
    int ma=ui->maxe->text().toInt();
    int n=ui->noe->text().toInt();
    if(mi&&ma)
    {
        if(mi==min&&ma==max)
        {
            speech->say("The button is not available!");
        }
        else
        {
            int r=generate(mi,ma,n);
            if(r==-1)
            {
                speech->say("I'm not joking.");
            }
            else
            {
                min=mi;
                max=ma;
                QString sr=QString("%1").arg(r+49);
                speech->say(sr);
            }
        }
    }
    else
    {
        speech->say("What do you want to do?");
    }
}
