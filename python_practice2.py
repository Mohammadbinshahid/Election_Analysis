# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')    
    
Counties= ["Arapahoe", "Denver","Jefferson"] 

if "Arapahoe" in Counties: 
    print("True") 
else: 
    print("False")

Counties= ["Arapahoe", "Denver","Jefferson"]
    
if "El Paso" not in Counties:  
    print("True") 
else:
    print("False")

Counties= ["Arapahoe", "Denver","Jefferson"]

if "El Paso" in Counties:
    print("El Paso is in the list of Counties")
else:
    print("El Paso is not in the list of Counties")

Counties= ["Arapahoe", "Denver","Jefferson"]
if "Arapahoe" in Counties and "El Paso" in Counties:
    print("Arapahoe and El Paso are in the list of Counties.")
else:
    print("Arapahoe or El Paso is not in the list of Counties.")

Counties= ["Arapahoe", "Denver","Jefferson"]
if "Arapahoe" in Counties and "El Paso" not in Counties:
    print("Only Arapahoe is in the list of Counties.")
else:
    print("Arapahoe is in the list of Counties and El Paso is not in the list of Counties.")