with open ('quotes.txt', 'r',encoding="utf-8") as file:
    for line in file:
        print(line)
autor = input()
with open ('quotes.txt', 'a',encoding="utf-8") as file:
    file.write(autor)
