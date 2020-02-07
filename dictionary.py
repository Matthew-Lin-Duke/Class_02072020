def create_dictionary():
    new_dictionary = {"day": "between sunrise and sunset",
                      "food": "something to eat",
                      "night":  "when the moon is out",
                      "star": "Blinking lights in the night sky"}
    return new_dictionary


def create_patient():
    new_patient = { "last name": "Liu",
                    "age": 234,
                    "married": False,
                    "test result": [23,34,54,654]}
    return new_patient


def save_Json(patient):
    import json
    filename = "patient_data.txt"
    out_file = open(filename, 'w') #w stands for write
    json.dump(patient, out_file)
    out_file.close()
    return

def read_dictionary(my_dict):
    my_key = "food"
    y = my_dict[my_key]
    #print(y)
    print("The definition of {} is {}".format(my_key, y))
    return


def add_dictionary(my_dict):
    my_dict["lunch"] = "meal at noon"
    my_dict["star"] = "other planet and fixed stars in space"
    return my_dict


if __name__ == "__main__":
    y = create_patient()
    save_Json(y)
    """x = create_dictionary()
    y = create_patient()
    print(y)
    a = y.get("test result")
    b = y["test result"][2]
    print(a)
    print(b)
    #read_dictionary(x)
    #print(x)
    #x = add_dictionary(x)
    #print(x)
    #z = x.get("food")
    #print(z)
    #print(x)
    #print(type(x))
    """