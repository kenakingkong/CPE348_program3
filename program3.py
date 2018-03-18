#Makena Kong
#mkong02

# Program 3 : Generating Permutations

#string of lower case letters -> list of permutations in lexicographic order
#why don't you just say alphabetical????
def get_perm_lex(string):
   if len(string) == 1:
      return [string]
   else:
      result = []
      for index in range(len(string)):
         str_list = list(string)
         char = str_list.pop(index)
         rest = get_perm_lex("".join(str_list))
         for item in rest:
            perm = char + item
            result.append(perm)
      return result
   return [string]



#print(get_perm_lex("a"))
#print(get_perm_lex("ab"))
#print(get_perm_lex("abc"))
#print(get_perm_lex("abcd"))
