from flask import Flask, render_template, request, jsonify, Response
import requests

app = Flask(__name__)

output = [("message stark", {"text":"Hi, how may I assist you?"})]

@app.route('/')
def home():
    print("output at home",output)
    return render_template('index.html', result=output)


@app.route('/result',methods=["POST","GET"])
def Result():
    global output
    if request.method=="POST":
        print('happened!')
        print(list(request.form.values()))
        result=list(request.form.values())[0]
        if request.args.get('game') != None:
            result = request.args.get('game')
        print(result)
        if result.lower()=="restart":
            output = [("message stark", {"text":"Hi, how may I assist you?"})]
        else:
            try:
                r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": result})
                li = []
                for i in r.json():
                    if 'image' in i:
                        li.append({"pic": i['image']})
                    if 'text' in i:
                        li.append(i['text'])
                    if 'buttons' in i:
                        for x in i['buttons']:
                            li.append((x['title'], "button"))
                sample = [("message parker",{"text":result})] 
                buttons = []
                for count, msg in enumerate(li): 
                    if count != len(li)-1 and type(li[count+1]) is dict:
                        sample.append(("message stark", {"text":msg, "pic": li[count+1]["pic"]}))
                    elif type(li[count]) is tuple:
                        buttons.append(msg[0])
                    elif type(li[count]) is not dict:
                        sample.append(("message stark", {"text":msg}))
                if buttons != []:
                    sample.append(("message stark", {"button":buttons}))
                output.extend(sample)
                print("output at here", output)
            except:
                output.extend([("message parker", result), ("message stark", "We are unable to process your request at the moment. Please try again...")])
        return render_template("index.html",result=output)

@app.route('/test')
def test():
    result = [("message parker", "Action game"), ("message stark", {"game_name":"GTAV", "game_picture":"https://upload.wikimedia.org/wikipedia/en/thumb/a/a5/Grand_Theft_Auto_V.png/220px-Grand_Theft_Auto_V.png"})]
    return render_template('test12.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)