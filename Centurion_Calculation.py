#ask for name and age
#when will you turn 100 yrs old
#calculation:
#current_yr=2024
#age=A
#duration= 100-age
#year= current_yr-duration
#The year {name} turns 100 years old is {year} 
#should calculate what year the person will turn 100 yrs old

def centurion_calculation (name, age):
      
    current_yr = 2024
    difference = 100-age
    duration = current_yr + difference
    print(name + ", You will be 100 years old in " + str(duration))

centurion_calculation("Robert Bonar",25)
