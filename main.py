from PyQt5 import QtCore, QtGui, QtWidgets
from funciones import crearMensajeCodificado, crearMensajeDecodificado


class Ui_Register(object):

    mensajeDecodificado = ''
    mensajeCodificado = ''
    path = ''
    tipoOperacion = ''
    valorPosicionInicial = ''

    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(428, 600)
        Register.setFixedSize(428, 600)

        self.centralwidget = QtWidgets.QWidget(Register)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

        self.archivoOrigen()

        self.operacion()

        self.posicionInicial()

        self.textoDecodificado()

        self.textoCodificado()

        self.resultadoOperacion()

        Register.setCentralWidget(self.centralwidget)

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Software Lab"))
        self.label.setText(_translate("Register", "Archivo origen"))
        self.pushButton.setText(_translate("Register", "Decodificar"))
        self.label_2.setText(_translate("Register", "Operación"))
        self.pushButton_2.setText(_translate("Register", "Codificar"))
        self.label_3.setText(_translate("Register", "Posición inicial"))
        self.label_4.setText(_translate("Register", "Texto decodificado"))
        self.label_5.setText(_translate("Register", "Texto codificado"))
        self.label_6.setText(_translate(
            "Register", "Resultado de la operación"))

    def archivoOrigen(self):
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 40, 231, 20))
        self.lineEdit.setObjectName("lineEdit")
        # triggers
        # self.lineEdit.returnPressed.connect(self.showText)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")
        # trigger
        self.pushButton.clicked.connect(self.openPopUp)

    def openPopUp(self):
        responseOpenFileName = QtWidgets.QFileDialog.getOpenFileName(
            Register, 'Open a file', '', 'only text format (*.txt)')
        self.path = responseOpenFileName[0]
        if self.path != '':
            self.mensajeCodificado = open(self.path).read()
            self.lineEdit.setText(self.path)

            self.textEdit_2.setText(self.mensajeCodificado)

            self.mensajeDecodificado = crearMensajeDecodificado(
                self.mensajeCodificado
            )

            self.textEdit.setText(self.mensajeDecodificado['mensaje'])
            self.lineEdit_2.setText(self.mensajeDecodificado['operacion'])
            self.lineEdit_3.setText(
                self.mensajeDecodificado['posicionInicial']
            )
            self.textEdit_3.setText(self.mensajeDecodificado['valorOperacion'])

    # def showText(self):
    #     print(self.mensajeCodificado)

    def operacion(self):
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 71, 21))
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 80, 231, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 80, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        # trigger
        self.pushButton_2.clicked.connect(
            lambda: self.comportamientoBotonCodificar()
        )

    def comportamientoBotonCodificar(self,):
        # Este condicional evitara que la aplicacion haga CRASH al momento de
        # dar click y no haber abierto ningun archivo de texto previamente
        if self.path == '':
            return

        self.mensajeCodificado = crearMensajeCodificado(
            self.path,
            self.lineEdit_2.text(),
            self.lineEdit_3.text(),
            self.textEdit.toPlainText(),
            self.mensajeCodificado,
            self.mensajeDecodificado["mensaje"],
            self.mensajeDecodificado['valorOperacion'],
        )
        self.textEdit_2.setText(self.mensajeCodificado)

    def posicionInicial(self):
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 71, 21))
        self.label_3.setObjectName("label_3")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 120, 231, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

    def textoDecodificado(self):
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 111, 21))
        self.label_4.setObjectName("label_4")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 190, 400, 80))
        self.textEdit.setObjectName("textEdit")

    def textoCodificado(self):
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 290, 111, 21))
        self.label_5.setObjectName("label_5")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 320, 400, 150))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setEnabled(False)

    def resultadoOperacion(self):
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 490, 151, 21))
        self.label_6.setObjectName("label_6")

        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 520, 400, 60))
        self.textEdit_3.setObjectName("textEdit_3")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QMainWindow()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())
