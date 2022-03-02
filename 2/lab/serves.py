from flask import Flask, make_response ,request
from waitress import serve
import subprocess

api = Flask(__name__)

@api.route('/create', methods=['GET'])
def create():
    subprocess.run(['python3','convertE2Y'],shell=False)
    print('yamlファイルを作成しました')
    return make_response('success')

@api.route('/ansible', methods=['GET'])
def ansible():
    subprocess.run(['ansible-playbook','main.yaml'],shell=False)
    print('ansibleを実行しました')
    return make_response('success')

if __name__ == '__main__':
    serve(api, host='0.0.0.0', port=3000)