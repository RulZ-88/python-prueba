
#Diccionario vacio
dictionary_empty= {}


print(f"Diccionario vacio : { dictionary_empty}")
print()


#Diccionario homogéneo
dictionary_ages = {"Juan" : 32 ,
                    "Gerardo" : 21 ,
                      "luis" : 25
                      
                      }

print(f" Diccionario de edades : {dictionary_ages}")
print()
#Diccionario heterogéneo
dictionary_dates = {"name": "brenda",
                    "last_name": "Flores",
                    "age" : 22
                    }


print(f" Diccionario de edades : {dictionary_dates}")
print()

#un diccionario para almacenar listas y diccionarios
dictionary_list= { "a " : {"a": 1},
                  "b": [0,1,2]
                  }

print(f" diccionario con lista y diccionario : {dictionary_list}")
print()

#un diccionario puede tener claves numéricas
dictionary_keys_num= {4:1,
                      5:2,
                      6:3
                      }

print(f"diccionario con claves numéricas {dictionary_keys_num}")
print()

#un diccionario no puede tener claves repetidas
dictionary_repeated_keys= {"juan":20,
                           "gerardo" :30 ,
                           "juan" : 15
                           }

print(f"diccionario con claves repetidas : {dictionary_repeated_keys}")
#un diccionario puede tener claves numericas o de tipo texto
dictionary= {1:23,
             "juan":5,
             -2 :"hola"
             }

print(f"diccionario con claves de distintos tipos de dato: {dictionary}")
print()
                      
