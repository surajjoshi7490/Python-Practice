#  ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#  animal_crackers('Levelheaded Llama') --> True
#  animal_crackers('Crazy Kangaroo') --> False
def animal_crackers(word):
    new_word=word.split()
    word_1=new_word[0]
    word_2=new_word[1]
    return True if word_1[0]==word_2[0] else False
    
print(animal_crackers('Crazy Kangaroo'))