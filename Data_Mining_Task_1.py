#---------TASK 1---------------
def get_user_input(Input):
     return input(Input)

def greet_user(name):
    print(f'Hello, {name}!')

def show_department(department):
      print(f'Your department is {department}!')

def PrintUserGrade(UserDegree):
    if UserDegree >= 90:   print('Excellent!')
    elif UserDegree >= 80: print('V.Good!') 
    elif UserDegree >= 70: print('Good!')
    elif UserDegree >= 60: print('Pass!')
    else:print('Fail!')


UserName = get_user_input('What is your name?')
UserDept  = get_user_input('What is your department?')
UserDegree = input('What is your degree?')


greet_user(UserName)
show_department(UserDept)
PrintUserGrade(int(UserDegree))


#---------TASK 2---------------
def CalculateBMI(weight, height):
    height_m = height / 100  # Convert height from cm to m
    bmi = weight / (height_m ** 2)  # Calculate BMI
    return bmi
def Check_BMI(bmi):
    if bmi <= 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"
UserName = get_user_input('What is your name?')
UserWeight = get_user_input('What is your weight(KG)?')
UserHeight = get_user_input('What is your height(Cm)?')

bmi = CalculateBMI(float(UserWeight), float(UserHeight))

greet_user(UserName)
print(f'Your BMI is: {bmi:.2f}')
print(f'Your BMI category is: {Check_BMI(bmi)}')

#-----------TASK 3---------------
import pandas as pd
df = pd.DataFrame({
    'Name': ['Ali', 'Sara', 'John', 'Emma'],
    'Age': [25, 30, 22, 28],
    'Department': ['IT', 'HR', 'Finance', 'Marketing'],
    'Salary': [50000, 60000, 55000, 70000]
})
print(f'The number of rows in the DataFrame is: {len(df)}')
print(df.sample(frac=0.5))
print(df.sort_values(by='Name', ascending=False))
print(df.nlargest(3, 'Age'))


