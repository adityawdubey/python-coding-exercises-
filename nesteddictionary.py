mydict={
        1:{'title':'Antiques Roadkill: A Trash Treasures Mystery','author':'Barbara Allan,3.3,','rating':3.3,'publisher':'Kensington Publishing Corp.,','page_count':288, 'generes':'Fiction', 'language':'English'},
        2:{'title':'Getting Away Is Deadly: An Ellie Avery Mystery','author':'Sara Rosett','rating':4.0,'publisher':'Kensington Publishing Corp.','page_count':320, 'generes':'none', 'language':'English'},
        3:{'title':'The Painted Man (The Demon Cycle, Book 1)','author':'Peter V. Brett','rating':4.5,'publisher':'HarperCollins UK','page_count':544, 'generes':'Fiction', 'language':'English'},
        4:{'title':'A Feast for Crows (A Song of Ice and Fire, Book 4)','author':'George R.R. Martin','rating':4.5,'publisher':'HarperCollins UK','page_count':864, 'generes':'none', 'language':'English'},
        5:{'title':'God of War: The Official Novelization','author':'J.M. Barlog','rating':4.5,'publisher':'Titan Books','page_count':400, 'generes':'Fiction', 'language':'English'},
        6:{'title':'Edgedancer: From the Stormlight Archive','author':'Brandon Sanderson','rating':4.8,'publisher':'Tor Books','page_count':226, 'generes':'Fiction', 'language':'English'},
        7:{'title':'7,Sword of Destiny: Witcher 2: Tales of the Witcher','author':'Andrzej Sapkowski','rating':4.8,'publisher':'Hachette UK','page_count':400, 'generes':'Fiction', 'language':'English'}
      }

#function which returns a dictionary will all the books for the given rate
def pretty(d, indent=0):
  for key, value in d.items():
    print( str(key),end=" : ")
    if isinstance(value, dict): 
    # The isinstance() function checks if the object (first argument) is an instance or subclass of classinfo class (second argument).
      pretty(value, indent+1)
    else:
      print(str(value))
    
#function to pretty print nested
def get_books_by_rate(rate):
  for i in mydict.values(): #iterating through dictionary values
    if i['rating']>=rate and i['rating']< rate+1:
      pretty(i) #function call
    print()

#driver code
get_books_by_rate(4) #function call 

