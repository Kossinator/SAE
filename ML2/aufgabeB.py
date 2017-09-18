
import matplotlib.pyplot as plt

import pandas as pd


def read_csv(path):

    vehicle_typs = pd.read_csv(path)

    vehicle_typs = vehicle_typs.values

    new_vehicle_typs = []

    for type in vehicle_typs:

        type = str(type[0])

        kg = type.split(";")[0]

        wheels = type.split(";")[1]

        vehicle_type = type.split(";")[2]

        new_arr = [float(kg), float(wheels), vehicle_type]

        new_vehicle_typs.append(new_arr)

    return new_vehicle_typs


def column(type):

    bicycles_weight = []

    bicycles_wheels = []

    vehicle_typs = read_csv("../data/ML_2.csv")

    for v in vehicle_typs:

        if v[2] == type:

            bicycles_weight.append(v[0])

            bicycles_wheels.append(v[1])

    return {"weight": bicycles_weight, "wheels": bicycles_wheels}

def print_on_console():
    print(read_csv("../data/ML_2.csv"))

def plot_it():

    plt.plot(column("Fahrrad")["weight"], column("Fahrrad")["wheels"], 'ro')

    plt.plot(column("Motorrad")["weight"], column("Motorrad")["wheels"], 'bo')

    plt.plot(column("PKW")["weight"], column("PKW")["wheels"], 'go')

    plt.axis([-100, 1000, 0, 5])

    plt.show()