from flask import Flask,request,jsonify
app = Flask(__name__)

keb_list = [
        {
            "id": 0,
            "name": "Monisha",
            "designation": "JEE",
            "place": "mangalore",

        },
        {
            "id": 1,
            "name": "Roopa",
            "designation": "AEE",
            "place": "mangalore",

        },
        {
            "id": 2,
            "name": "Ganesh",
            "designation": "JEE",
            "place": "madikeri",


        },
        {
            "id": 3,
            "name": "Yashika",
            "designation": "AEE",
            "place": "madikeri",

        },
        {
            "id": 4,
            "name": "Vanajakshi",
            "designation": "JEE",
            "place": "bangalore",

        },
        {
            "id": 5,
            "name": "Sundara",
            "designation": "AEE",
            "place": "bangalore",
            
         },
         {

            "id": 6,
            "name": "Tiga",
            "designation": "JEE",
            "place": "mangalore",

        }

    ]                                                                                                                                                                                         46,9          49%

@app.route('/keb',methods=['GET','POST'])
def keb():
    if request.method=='GET':
        if len(keb_list) >0:
            return jsonify(keb_list)
        else:
            'Nothing found', 404

    if request.method == 'POST':
        new_name = request.form['name']
        new_desg = request.form['designation']
        new_place = request.form['place']
        ID = keb_list[-1]['id']+1

        new_obj = {
                'id':ID,
                'name':new_name,
                'designation':new_place,
                'place':new_place
        }
        keb_list.append(new_obj)
        return jsonify(keb_list),201

@app.route('/keb/<int:id>',methods=['GET','PUT','DELETE'])
def single_keb(id):
    if request.method == 'GET':
        for mem in keb_list:
            if mem['id'] == id:
                return jsonify(mem)
            pass
    if request.method == 'PUT':
        for mem in keb_list:
            if mem['id'] == id:

                mem['name'] = request.form['name']
                mem['designation'] = request.form['designation']
                mem['place'] = request.form['place']
                updated_keb = {
                    'id':id,
                    'name':mem['name'],
                    'designation':mem['designation'],
                    'place':mem['place']
                }
                return jsonify(updated_keb)
                                                                                                                                                                                         101,9         83%
   if request.method == 'DELETE':
        for index, mem in enumerate(keb_list):
            if mem['id'] == id:
                keb_list.pop(index)
                return jsonify(keb_list)




if __name__=='__main__':
    app.run()

   
         
                               
