from flask import Flask, url_for, render_template, request
import pandas as pd
import numpy as np

##### Database things #####
fish = pd.read_csv("fish.csv")


# Get name that the user wants to find
fishName = input("Enter the name of the fish you are looking for: ")
print()

for i in range(len(fish.index)):
    if fish.iloc[i][0] == fishName:
        print("Name        : " + fish.iloc[i][0])
        print("Seasonality : " + fish.iloc[i][1])
        print("Location    : " + fish.iloc[i][3])
        print("Time        : " + fish.iloc[i][4])
        print("Price       : " + str(fish.iloc[i][6]))