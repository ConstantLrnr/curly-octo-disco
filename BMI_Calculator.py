height= input()    #enter in meters e.g: 1.65
weight= input()    #enter in kilograms e.g 89

height_as_float = float(height)
weight_as_int = int(weight)     # whole number

#using the exponent operater **

BMI= weight_as_int/height_as_float ** 2

# or using multiplication or PEMDAS-LR

BMI= weight_as_int/ (height_as_float * height_as_float)


BMI_as_int = int(BMI)
print(BMI_as_int)




 


