import periodictable

try:
    # Prompt the user to enter the Atomic Number of the Element and convert it to an integer.
    Atomic_no = int(input("Enter the Atomic Number of the Element: "))

    # Retrieve information about the element with the given Atomic Number.
    element = periodictable.elements[Atomic_no]

    # Print various properties of the element.
    print("Atomic Number:", element.number)
    print("Symbol:", element.symbol)
    print("Name:", element.name)
    print("Atomic Mass:", element.mass)
    print("Density:", element.density)

# Handle the ValueError exception if the user doesn't enter a valid integer.
except ValueError:
    print("Please enter a valid atomic number as an integer.")

# Handle the KeyError exception if the entered atomic number doesn't exist in the periodic table.
except KeyError:
    print("The entered atomic number does not exist in the periodic table.")