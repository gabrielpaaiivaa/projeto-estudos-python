# Importando as bibliotecas.
from PyQt5 import uic,QtWidgets
import mysql.connector
# Conectando ao banco de dados.
banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "cadastro_produtos"
)
# Função Principal.
def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    categoria = ""
# Estrutura de Decisão para definir o botão escolhido.
    if formulario.radioButton.isChecked():
        print("Categoria Informatica foi selecionada.")
        categoria = "Informatica"
    elif formulario.radioButton_2.isChecked():
        print("Categoria Alimentos foi selecionada.")
        categoria = "Alimentos"
    else:
        print("Categoria Eletrônicos foi selecionada.")
        categoria = "Eletronicos"
# Monstrar na tela os comandos da variáveis linha1, linha2 e linha3
    print("Código: ", linha1)
    print("Descrição: ", linha2)
    print("Preço: ", linha3)
# Funções para incluir os dados digitados no banco de dados.
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo, descricao, preco, categoria) VALUES (%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3),categoria)
# Código para executar o comando_SQL
    cursor.execute(comando_SQL,dados)
    banco.commit()
# Apaga o texto quando clica em enviar
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")

def chama_segunda_tela():
    segunda_tela.show()


app=QtWidgets.QApplication([])
# Acessar o arquivo UI
formulario=uic.loadUi("formulario.ui")
segunda_tela=uic.loadUi("listar_dados.ui")

formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)


formulario.show()
app.exec()
