name = input("camelCase: ")
snake_name = name
prev_is_lower = False
for c in name:
    if c.isupper() and prev_is_lower:
        snake_name = snake_name.split(c)
        snake_name = snake_name[0] + '_' + c.lower() + snake_name[1]
    prev_is_lower = True



print("snake_case: " + snake_name)