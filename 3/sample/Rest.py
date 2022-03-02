from flask import Flask, make_response ,request
from waitress import serve

api = Flask(__name__)

#アノテーション
@api.route('/', methods=['GET'])
def get():
      print('アクセスがありました。')
      return make_response('処理が正常に実行されました。')

# if....の行はお作法　この処理がメインだよということを示す
if __name__ == '__main__':
      serve(api, host='0.0.0.0', port=3000)
