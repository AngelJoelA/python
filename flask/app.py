import math
from tabulate import tabulate

def calculate_bmi(peso, estatura):
    bmi = peso / (math.pow(estatura, 2))
    bmi = round(bmi, 1)
    return bmi

if __name__ == "__main__":
    peso = float(input("Ingrese su peso en Kilogramos: "))
    estatura = float(input("Ingrese su estatura en metros: "))
    bmi = calculate_bmi(peso, estatura)
    print("Su BMI es de " + str(bmi))

    bmi_categories = [
        ["Categoría", "BMI rangos (kg/m²)"],
        ["Bajo peso", "< 18,5"],
        ["Saludable", "18,5 - 24,9"],
        ["Sobrepeso", "25,0 - 29,9"],
        ["Obesidad", ">= 30,0"],
    ]
    print(tabulate(bmi_categories, headers=["Categoría", "BMI rangos"]))
    