import sys
"""
take 2 dict and connect it

"""

def capitol():
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
        for key in states:
            if arg == key:
                initials = states[key]
                print(capital_cities[initials])
                return
        print("Unknown state")

if __name__ == '__main__':
    capitol()
