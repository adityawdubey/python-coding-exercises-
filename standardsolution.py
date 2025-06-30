def sol(input_token,token_dict):
  input_token_list = input_token.split(" ")
  #print(input_token_list)

  res = ""
  for i in input_token_list:
    if i in token_dict.keys():
      res = res + " " + sol(token_dict[i],token_dict)
    else:
      res = res + " " + i

  return res.strip()


input_token = "A B C D"
token_dict = {'A': 'B','F': 'K','Z':'F', 'B': 'E', 'C': 'B D', 'D': 'Z'}

print(sol(input_token,token_dict)) 


# import sympy

# input_token_list = []
# while True:
#     input_token_list = int(input())
#     if input_token_list == -1:
#         break
#     input_token_list.append(input_token_list)



# primelist=[i for i in input_token_list if sympy.isprime(i)]
# compositelist=[i for i in input_token_list if sympy.iscomposite(i)]


# print("Entered List: ", input_token_list)
# print("Prime Numbers: ", primelist)



