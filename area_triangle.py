# function for calculating area of a Triangle
def calc_area(base, height):
    # calculates area
    area = (base * height) / 2
    # displays it to the user
    print(f"The area for {base} * {height}/2 = {area}")
 
 
def main():
    # gets base and height from the user
    base_from_user = input("Please Enter the Base of the triangle: ")
    height_from_user = input("Please Enter the Height of the triangle: ")
 
    try:
        # tries casting base and height as a float
        base_from_user = float(base_from_user)
        height_from_user = float(height_from_user)
        if base_from_user or height_from_user < 0:
                print("Please enter a number above 0")
                main()
    except ValueError:
        # exception thrown if user inputs a string
        print("Please enter a number")
    else:
        # arguments getting passed as parameters
        calc_area(base_from_user, height_from_user)
 
 
if __name__ == "__main__":
    main()
 
