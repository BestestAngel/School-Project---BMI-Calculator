print('witaj w kalkulatorze bmi')
a = float(input('podaj wagę (kg)'))
b = float(input('podaj wzrost(m)'))

def bmi(a,b):
    return a/b**2 
print(bmi(a,b))

if bmi(a,b) < 16:
    print('Severe Thinness')
elif bmi(a,b) < 17: 
    print('Moderate Thinness')
elif bmi(a,b) < 18.5:
    print('Mild Thinness')
elif bmi(a,b) < 25:
    print('Normal')
elif bmi(a,b) < 30:
    print('Overweight')
elif bmi(a,b) < 35:
    print('Obese Class I')
elif bmi(a,b) < 40:
    print('Obese Class II')
else: 
    print('Obese Class III')