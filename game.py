def tree_riddle():
    print("Ласкаво просимо до загадкового лісу!")
    print("Древні дерева зупиняють тебе і промовляють загадку:")
    print('"Я маю коріння, але не можу рости, я маю гілки, але не можу летіти. Що я?"')
    
    # Вибір користувача
    print("\n1. Птах\n2. Річка\n3. Дерево\n4. Будинок")
    відповідь = input("Твоя відповідь (вкажи номер): ")

    # Перевірка відповіді
    if відповідь == "3":
        print("\nПравильно! Древні дерева розступаються, вказуючи тобі шлях далі.")
    else:
        print("\nНеправильно. Дерево мовчить, але ти можеш спробувати знову.")
        tree_riddle()

# Початок гри
tree_riddle()
