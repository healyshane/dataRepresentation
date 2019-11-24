from flask import Flask, jsonify, request, abort

app = Flask(__name__, static_url_path='',static_folder='./')

BNs=[
    { "id":1, "Batch":"192J1234", "std_time": 38, "act_time": 42 },
    { "id":2, "Batch":"192J987H", "std_time": 38, "act_time": 46 },
    { "id":3, "Batch":"192J9877", "std_time": 38, "act_time": 32 },
    { "id":4, "Batch":"192J1099", "std_time": 38, "act_time": 48 },
    { "id":5, "Batch":"192J9888", "std_time": 38, "act_time": 60 },
    { "id":6, "Batch":"192K8756", "std_time": 38, "act_time": 55 }
]
nextId=7

#curl "http://127.0.0.1:5000/BNs"
@app.route('/BNs')
def getAll():
    return jsonify(BNs)

#curl "http://127.0.0.1:5000/BNs/1"
@app.route('/BNs/<int:id>')
def findById(id):
    foundBNs = list(filter(lambda b: b['id'] == id, BNs))
    #if len(foundBNs) ==0:
        #return jsonify ({}) ,204


    return jsonify(foundBNs[0])


#curl -i -H "Content-Type:application/json" -X POST -d "{\"Batch\":\"192f2345\",\"std_time\":38,\"act_time\":69}" "http://127.0.0.1:5000/BNs"

@app.route('/BNs', methods=['POST'])
def create():
    global nextId
    if not request.json:
        abort(400)

    # Other checks that correctly formatted

    BN={
        "id": nextId,
        "Batch": request.json['Batch'],
        "std_time": request.json['std_time'],
        "act_time": request.json['act_time']
    }
    nextId +=1
    BNs.append(BN)
    return jsonify(BN)


#curl -i -H "Content-Type:application/json" -X PUT -d "{\"act_time\":50}" "http://127.0.0.1:5000/BNs/1"
@app.route('/BNs/<int:id>', methods=['PUT'])
def update(id):
    foundBNs = list(filter(lambda t: t['id'] == id, BNs))
    if(len(foundBNs) == 0):
        abort(404)
    foundBN = foundBNs[0]
    if not request.json:
        abort(400)
    reqJson = request.json

    if ('std_time' in reqJson and type(reqJson['std_time']) is not int):
        abort(400)

    if ('act_time' in reqJson and type(reqJson['act_time']) is not int):
        abort(400)

    if 'Batch'in reqJson:
        foundBN['Batch'] = reqJson['Batch']
    if 'std_time' in reqJson:
        foundBN['std_time'] = reqJson['std_time']
    if 'act_time' in reqJson:
        foundBN['act_time'] = reqJson['act_time']
        #CHECK
        #Check if integer

    return jsonify(foundBN)
    

    return "In update for ID "+str(id)

#curl -X DELETE "http://127.0.0.1:5000/BNs/1"
@app.route('/BNs/<int:id>', methods=['DELETE'])
def delete(id):
    foundBNs = list(filter(lambda t: t['id'] == id, BNs))
    if(len(foundBNs) == 0):
        abort(404)
    BNs.remove(foundBNs[0])
    return jsonify({"done":True})


if __name__ =='__main__':
    app.run(debug=True)