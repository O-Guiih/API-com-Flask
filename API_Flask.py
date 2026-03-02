# Importação de dados
# Request permite capturar os dados enviados via pelo metodo "POST"
from flask import Flask, request

app = Flask(__name__)

# Definindo uma rota básica que responde a requisições GET
# Decorador (@app.route())
@app.route("/") # / significa a rota inicial da aplicação (Raiz do Servidor)
def root(): #Função
    return 'Olá mundo!'

# ----- NOVA ROTA ------

#Para chamar essa outra rota é preciso colocar o /submit no final da url já que a rota foi definida para como /submite através do código (@app.route)

# Criação de uma nova rota e um formulário no metodo POST em html
# Criação de um campo sendo um input do tipo "text" para que o úsuário coloque o nome dele
# Criação de outro campo sendo um input submit, que vai fazer a ação de enviar para o servidor
# value = texto que vai estar escrito dentro do botão

@app.route("/submit", methods=["GET", "POST"])

# Sempre ao criar uma rota no flask, por padrão ela sempre vai receitar requisições do tipo GET

# GET = Solicitar os dados do site sem enviar nenhuma informação para ele. solicita os dados, recebe a informação e exibe na tela.
# POST = Serve para enviar uma informação para o site (como exemplo o formulário)

# Na rota principal usando a função methods é possível definir quais metodos a rota principal vai receber.
# Definindo a rota para os metodos POST e GET eu estou enviando as informações para o site através do formulário e estou pedindo para receber as informações que o usuário preencher. 

# ---//---

# Utilizando o decorador para falar qual que será a rota em que esse formulário será acessivel e chamando a rota de submit
# Toda rota deve começar com um barra inicialmente (Ex: /submit)
def submit(): #Função submit que está retornando uma string que é o formulário em html
# --- // ---

# - Buscando a informação colocada pelo usuário: -
    if request.method == "POST":  
#Interpretação : Se o meu request.method (Metodo de qual a requisição foi feita) for igual a POST significa que estou recebendo alguma informação do usuário

# -- Capturando os dados   

# .form = para indicar que estou recebendo esses dados via formulário
# ["name"] = Indicando o nome do campo que quero capturar. No caso do formulário temos o primeiro input em que o name dele é igual a (name)
        data = request.form["name"]
        return f"Você enviou: {data}"


    return '''
        <form method="POST">
            Nome: <input type="text" name="name">
            <input type="submit" value="Enviar">
        </form>   
    '''

if __name__ == "__main__":
    app.run(debug=True, port=5152)