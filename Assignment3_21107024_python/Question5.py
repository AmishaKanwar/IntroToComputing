print("Caclulating total molecular wt. of any carbohydrate in grams/mole")
# The molar wt. of all the atoms and molecule is in grams/mole.
molar_wt_H = 1.00794
molar_wt_C = 12.0107
molar_wt_O = 15.9994

num_H_atoms = int(input("Enter no. of Hydrogen atoms: "))
num_C_atoms = int(input("Enter no. of Carbon atoms: "))
num_O_atoms = int(input("Enter no. of Oxygen atoms: "))

molecular_wt = (num_H_atoms * molar_wt_H) + (num_C_atoms * molar_wt_C) + (num_O_atoms * molar_wt_O)
print(f"The total molecular weight of the given carbohydrate is {molecular_wt} grams/mole.")