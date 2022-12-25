QT       += core gui
QT       += texttospeech
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets
TARGET = Lottery-Machine
TEMPLATE = app
DEFINES += QT_DEPRECATED_WARNINGS
SOURCES += \
        main.cpp \
        widget.cpp

HEADERS += \
        widget.h

FORMS += \
        widget.ui
