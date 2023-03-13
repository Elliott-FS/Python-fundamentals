import cars

print('My old car was a', cars.car_model1, cars.car_year1)

print('My new car is a', cars.car_model2, cars.car_year2)

# essentially the import statement in a file(if __name__ == '__main__':) says only run
# this file if it is the main script being used. You can then import the file using import file_name
# to acess variables functions and other code from that script or module with dot notation. 

# Essentially a module is a scipt that will be imported and used by other scripts and possibly other modules, 
# scripts are just files that store python code to be ran.