#dictionary is a collection of key:value pair
#it is muttable
mydict={ 
    "fast":"in a quick manner",
    "marks":[1,2,5],
    "anotherdict":{"maaz":"player"},
    1:2
}
print(mydict['fast'])
print(mydict['marks'])
mydict['marks']=[3,5,6]   #muttable
print(mydict['marks'])
print(mydict['anotherdict']['maaz'])

#methods
print(mydict.keys())
print(mydict.values())
print(mydict.items())
updatedict={
    'dzt':'addy'
}
mydict.update(updatedict)
print(mydict)
print(mydict.get('dzt')) #it is not same as mydict['dzt] becoz it returns value but if dzt is not present in dictionsry it throws error where as get function also return value but if dzt is not present it returns none
