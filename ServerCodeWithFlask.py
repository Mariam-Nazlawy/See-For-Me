from flask import Flask, request, jsonify, send_file

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify(
            {
                "msg": "success",
            }
        )

@app.route('/post', methods=["POST"])
def testpost():
     input_json = request.get_json(force=True)
     dictToReturn = {'text':input_json['text']}
     return jsonify(dictToReturn)


@app.route('/img', methods=["POST"])
def recImg():
    try:
        file = request.files['image']
        name = file.filename

        return jsonify(
            {
                "msg": "success",
                "name": name
            }
        )
    except Exception as e:
        return jsonify({"msg": str(e)})


@app.route('/audio', methods=['GET'])
def audio():
    mp3FilePath = 'Info.mp3'
    return send_file(mp3FilePath, mimetype='audio/mpeg', as_attachment=True)
