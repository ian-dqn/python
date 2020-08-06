"""

dico.pop[key]
del dico[key]

"""
import sys

def inverse(dict):
    inv_dic = [(date, name) for name, date in dict]
    return inv_dic

def sort(dic):
    sorted = False
    while sorted == False:
        sorted = True
        i = 0
        for i in range(len(dic) - 1):
            if dic[i] > dic[i + 1]:
                dic[i], dic[i + 1] = dic[i + 1], dic[i]
                sorted = False
    return dic

def dict():
    #fct qui transforme une liste en dico
    d = [
            ('Hendrix' , '1942'),
            ('Allman' , '1946'),
            ('King' , '1925'),
            ('Clapton' , '1945'),
            ('Johnson' , '1911'),
            ('Berry' , '1926'),
            ('Vaughan' , '1954'),
            ('Cooder' , '1947'),
            ('Page' , '1944'),
            ('Richards' , '1943'),
            ('Hammett' , '1962'),
            ('Cobain' , '1967'),
            ('Garcia' , '1942'),
            ('Beck' , '1944'),
            ('Santana' , '1947'),
            ('Ramone' , '1948'),
            ('White' , '1975'),
            ('Frusciante', '1970'),
            ('Thompson' , '1949'),
            ('Burton' , '1939')
            ]
    dict = {}
    tmp = sort(inverse(d))
#    print(tmp)
    for date, name in tmp:
        dict[date] = name
        print(dict)
    return dict

#(inverse([("der", "3"), ("prems", "0"), ("mid", "2")]))
dict()
