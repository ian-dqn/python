import sys
"""
take 2 dict and connect it

"""

def cap():
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        states = {
            "Oregon" : "OR",
            "Alabama" : "AL",
            "New Jersey": "NJ",
            "Colorado" : "CO"
            }
        capital_cities = {
            "OR": "Salem",
            "AL": "Montgomery",
            "NJ": "Trenton",
            "CO": "Denver"
            }
        for key in capital_cities:
            if arg == capital_cities[key]:
                initial = key
                for value in states:
                    if initial == states[value]:
                        print(value)
                        return
        print("Unknown capital city")

if __name__ == '__main__':
    cap()
