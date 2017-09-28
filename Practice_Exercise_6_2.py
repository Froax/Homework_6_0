list_a = ["boter", "kaas", "bier", "pizza", "thee", "drop", "koek", "cola", "boterham", "stamppot"]

new_list = []
for i in list_a:
    if len(i) == 4:
        new_list.append(i)

print(new_list)

