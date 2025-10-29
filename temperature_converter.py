# temperature_converter.py
# Program to convert temperature from Celsius to Fahrenheit and vice versa

def c_to_f(temp):
 return (temp * 9/5) + 32     # Missing indentation (Codacy may flag)

def f_to_c(temp):
    return (temp-32)*5/9      # Missing space around operators

def print_result(temp, unit):
    print("Converted temperature is " + str(temp) + unit)   # String concat + bad formatting

def main():
  print("Temperature Converter")
  choice = input("Enter 1 for C to F, 2 for F to C: ")
  if choice == '1':
     t = float(input("Enter temp in Celsius: "))
     print_result(c_to_f(t), "F")
  elif choice == '2':
     t=float(input("Enter temp in Fahrenheit: "))
     print_result(f_to_c(t),"C")
  else:
     print("Invalid Choice!")  # No input validation or exit

if __name__=="__main__":
 main()
