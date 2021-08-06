def wanderingtraveller(string):
    if len(string):
        coordinates = {
            "N": +1,
            "S": -1,
            "E": +1,
            "W": -1
        }
        points = [(0, 0)]
        for i in range(len(string)):
            character = string[i]
            if character == 'N' or character == 'S':
                last_point = points[-1]
                new_point = (
                    last_point[0], last_point[1]+coordinates[character])
                points.append(new_point)
            else:
                last_point = points[-1]
                new_point = (
                    last_point[0]+coordinates[character], last_point[-1])
                points.append(new_point)
        print(points)
        if points[0] == points[-1]:
            return True
        else:
            return False
    else:
        return False


print(wanderingtraveller("NE"))
print(wanderingtraveller("NES"))
print(wanderingtraveller("NEWS"))
print(wanderingtraveller("NEWS"))
print(wanderingtraveller(""))
print(wanderingtraveller("NENWNWSSWNWNSSEEES"))
print(wanderingtraveller("SWEN"))
print(wanderingtraveller("NESW"))
