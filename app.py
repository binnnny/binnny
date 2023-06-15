from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"key": "value"}  # 이 부분을 실제 데이터로 대체하세요.
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
