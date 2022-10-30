from flask import Flask, url_for, render_template, request
import pandas as pd
import numpy as np
import math

##### Database things #####

# Read in the CSV
fish = pd.read_csv("fish2.csv")

#############################
###     Start the app     ###
#############################

app = Flask(__name__)

#############################
###       Home Page       ###
#############################

@app.route('/')
def index():
    return render_template('index.html')

# Route for grabbing search information
@app.route('/', methods=['POST'])
def getvalue():

    # Obtain the fish to search for (and sanitize it)
    searchItem = request.form['searchItem']
    searchItem = searchItem.lower()
    searchItem = searchItem.replace("-","")
    searchItem = searchItem.replace(" ","")
    print(searchItem)
    
    creatureFound = False
    
    for i in range(len(fish.index)):
    
        currentCreature = fish.iloc[i][0]
        currentCreature = currentCreature.lower()
        currentCreature = currentCreature.replace(" ","")
        currentCreature = currentCreature.replace("-","")
        
        creatureType = fish.iloc[i][6]
        
        if currentCreature == searchItem:
        
            creatureFound = True
            
            name        = fish.iloc[i][0]
            seasonality = fish.iloc[i][1]
            location    = fish.iloc[i][2]
            time        = fish.iloc[i][3]
            price       = fish.iloc[i][4]
            size        = fish.iloc[i][5]
            
            if creatureType == "fish":
                return render_template('index_success.html', name=name, seasonality=seasonality, location=location, time=time, price=price, size=size)
            elif creatureType == "bug":
                return render_template('index_success_bug.html', name=name, seasonality=seasonality, location=location, time=time, price=price)
    
    return render_template('index_fail.html')

#############################
###      Run the app      ###
#############################

if __name__ == '__main__':
    app.run(debug="True")