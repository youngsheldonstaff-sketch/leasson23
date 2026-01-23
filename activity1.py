studentdata = {"id1":
               {"name": "sara",
                "class": 5,
                "subjects":["math", "science", "computer"] },
               "id2":{"name": "davis",
                      "class":7,
                      "subjects":["english", "math", "science"] },
               "id3":{"name": "sara",
                      "class": 5,
                      "subjects":["math", "science", "computer"] },
               "id4":{"name": "Surya",
                            "class": 6,
                            "subjects":["english","math", "science"] }}


result = {}

for key, value in studentdata.items():
     if value not in result.values():
        result[key] = value


print(result)
