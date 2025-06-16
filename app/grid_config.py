
grid = [
        [1, 1, 0, 1],
        [1, 0, "T", 0],
        [0, 0, 0, 0],
        [0, 0, 4, 3],
        ["C", 0, "G41", 0],
        ["F", 0, 0, 0],
        [2, 0, 0, "S"],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        ["F", 0, 0, "G43"],
        ["G42A", 0, 0, "S"],
        ["G42B", 0, 0, "G45"],
        ["F", "G44", 0, "S"],
        ["F", 1, 0, "S"],
        ["G46A", 4, 4, "G47"]
    ]

walkable = [0, 1, 2, 3, 4, "F", "S", "T", "G41", "G42A", "G42B", "G43", "G44", "G45", "G46A", "G47", "C"]
    
locations = {
        "tsa": (1, 2),
        "restroom": [(6, 0)],
        "currency exchange": [(3, 3)],
        "flight info": [(3, 2)],
        "gate 41": (4, 2),
        "gate 42a": (9, 0),
        "gate 42b": (11, 0),
        "gate 43": (9, 3),
        "gate 44": (12, 1),
        "gate 45": (11, 3),
        "gate 46a": (14, 0),
        "gate 47": (14, 3),
        "connector": (4, 0),
        "food court": [(5, 0), (9, 0), (12, 0), (13, 0)],
        "shop": [(6, 3), (10, 3), (12, 3), (13, 3)]
}

place_types = {
    "T": "TSA checkpoint",
    "S": "Shopping",
    "F": "Food court/shops",
    "R": "Restroom",
    "C": "Connector bus stop",
    "1": "Elevator/Escalator",
    "2": "Restroom",
    "3": "Currency exchange",
    "4": "Flight info"
}



