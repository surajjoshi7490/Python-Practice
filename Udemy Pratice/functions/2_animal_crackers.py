#  ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#  animal_crackers('Levelheaded Llama') --> True
#  animal_crackers('Crazy Kangaroo') --> False
def animal_crackers():
    a=str(input("First Word :"))
    b=str(input("Second Word : "))
    if a[0]==b[0]:
        return True
    else :
        return False
    
print(animal_crackers())