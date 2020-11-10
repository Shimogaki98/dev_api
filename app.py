from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'id' : 0,
        'nome': 'Marcello',
        'habilidades': ['Python', 'Flask']
    },
    {
        'id' : 1,
        'nome': 'Bronzatti',
        'habilidades': ['Python', 'Django']
    }

]
# devolve um dev por ID, também altera e deleta um registro de dev
@app.route('/dev/<int:id>/', methods= ['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de id {} não existe'.format(id)
            response = {'status': 'Erro', 'Mensagem': mensagem}
        except Exception :
            mensagem = 'erro desconhecido, procure o administrador da API'
            response = {'status': 'Erro', 'Mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE' :
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucess', 'mensagem': 'registro excluido'})


# Lista todos os Devs e permite a inclusão de novos registros
@app.route('/dev/', methods = ['GET', 'POST'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)