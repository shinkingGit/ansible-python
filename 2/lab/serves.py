from flask import Flask, make_response ,request
from waitress import serve

api = Flask(__name__)

@api.route('/create', methods=['GET'])
def get():
    name = request.args.get('name')
    print('createからアクセスがありました。')
    return make_response('yamlファイルを作成しました')

@api.route('/ansible', methods=['GET'])
def get():
    name = request.args.get('name')
    print('ansibleからアクセスがありました。')
    return make_response('Ansibleを実行しました')

if __name__ == '__main__':
    serve(api, host='0.0.0.0', port=3000)