# Question 1

# favorite_fruit = ["fraise", "coco"]
# favorite_fruit .append("mangue")
# favorite_fruit .pop(1)
# favorite_fruit .sort()
# new_list = favorite_fruit[:3]
# print("favorite_fruit=", (favorite_fruit))
# print("new_lsit=", (new_list))

# Question 2

# colors = ("bleu", "rouge", "noir")
# print(colors.count("bleu"))
# print(colors.index("bleu"))
# colors2 = ("blue", "red", "black")
# concatenate = colors + colors2
# print(concatenate)

# Question 3

dictionnaire = dict(prenom="Theo", age="22", ville="Paris")
dictionnaire["métier"] = "étudiant"
dictionnaire["age"] = "23"
del dictionnaire["ville"]
print("Clés :", dictionnaire.keys())
print("Valeurs :", type(dictionnaire.values()))


# Question 4

set1 = set {1, 2, 5, 6}
set2 = set {3,8, 9, 7}
set_total = set1 + set2
print(set_total)