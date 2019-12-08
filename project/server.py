from flask import Flask, jsonify, request, abort
from batchDAO import batchDAO
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__, static_url_path='',static_folder='./')

# @app.route('/plot')
# def build_plot():

#     img = io.BytesIO()

   
#     y = [1,2,3,4,5]
#     x = [0,2,1,3,4]
#     plt.plot(x,y)
#     plt.savefig(img, format='png')
#     img.seek(0)

#     plot_url = base64.b64encode(img.getvalue()).decode()

#     return '<img src="data:image/png;base64,{}">'.format(plot_url)



#curl "http://127.0.0.1:5000/batches"
@app.route('/batches')
def getAll():
    results = batchDAO.getAll()
    return jsonify(results)


#curl "http://127.0.0.1:5000/batches/1"
@app.route('/batches/<int:id>')
def findById(id):
    foundBatch = batchDAO.findByID(id)
    if len(foundBatch) == 0:
        return jsonify({ 'error' : 'No Data' }),204
    else:
        return jsonify(foundBatch)


#curl -i -H "Content-Type:application/json" -X POST -d "{\"Batch\":\"192f2345\",\"yield\":38,\"time\":69}" "http://127.0.0.1:5000/batches"

@app.route('/batches', methods=['POST'])
def create():
    if not request.json:
        abort(400)

    # Other checks that correctly formatted

    batch={
        "Batch": request.json['Batch'],
        "yield": request.json['yield'],
        "time": request.json['time']
    }
   
    values = (batch['Batch'],batch['yield'],batch['time'])
    newId = batchDAO.create(values)
    batch['id'] = newId
    return jsonify(batch)


#curl -i -H "Content-Type:application/json" -X PUT -d "{\"time\":50}" "http://127.0.0.1:5000/batches/1"
@app.route('/batches/<int:id>', methods=['PUT'])
def update(id):
    foundBatch = batchDAO.findByID(id)
    
    if not foundBatch:
        abort(404)

    if not request.json:
        abort(400)
    reqJson = request.json

    if ('yield' in reqJson and type(reqJson['yield']) is not int):
        abort(400)

    if ('time' in reqJson and type(reqJson['time']) is not int):
        abort(400)

    if 'Batch'in reqJson:
        foundBatch['Batch'] = reqJson['Batch']

    if 'yield' in reqJson:
        foundBatch['yield'] = reqJson['yield']

    if 'time' in reqJson:
        foundBatch['time'] = reqJson['time']

    values = (foundBatch['batch'],foundBatch['yield'],foundBatch['time'],foundBatch['id']) 
    batchDAO.update(values)
    return jsonify(foundBatch)


#curl -X DELETE "http://127.0.0.1:5000/batches/1"
@app.route('/batches/<int:id>', methods=['DELETE'])
def delete(id):
    batchDAO.delete(id)
    return jsonify({"done":True})


if __name__ =='__main__':
    app.run(debug=True)