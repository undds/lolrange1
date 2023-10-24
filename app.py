from flask import Flask, request, render_template
from functions import callWiki  
from functions import ingame

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_champion_info', methods=['POST'])
def get_champion_info():
    champion_name = request.form.get('champion_name')
    
    if champion_name:
        champ_info = callWiki(champion_name)
        if(champ_info == -1):
            return render_template('failure.html', message = "champ does not exist")
        else:
            return render_template('1champ.html', champ_info=champ_info)

# WIP

@app.route('/get_summoner_info', methods=['POST'])
def get_summoner_info():
    summoner_name = request.form.get('summoner_name')
    if summoner_name:
        champObjectList = ingame(summoner_name)
        if(champObjectList == -1):
            return render_template('failure.html', message = "person not ingame")
        elif(champObjectList == -2):
            return render_template('failure.html', message = "cannot find summoner name")
        else:
            return render_template('summoner.html', champList = champObjectList)

@app.route('/process_combined_form', methods=['POST'])
def process_combined_form():
    champ1_name = request.form.get('champ1')
    champ2_name = request.form.get('champ2')

    # Assuming callWiki returns champ objects
    champ1 = callWiki(champ1_name)
    champ2 = callWiki(champ2_name)

    #error checking

    if(champ1 == -1):
        print("champ1 does not exist")
        return render_template('failure.html', message = "champ1 does not exist")
    elif (champ2 == -1):
        print("champ2 DNE")
        return render_template('failure.html', message = "champ2 does not exist")

    return render_template('2champs.html', champ1 = champ1, champ2 = champ2)


if __name__ == '__main__':
    app.run(debug=True)
