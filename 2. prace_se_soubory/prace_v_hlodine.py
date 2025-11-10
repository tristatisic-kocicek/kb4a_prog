cesta_k_citatum = r"C:\Users\nejme\kb4a_prog\2. prace_se_soubory\data\citaty.txt"
emoji_1 = ["🌺", "🌼", "🌞", "🐻", "❤️‍", "🔥"]
emoji_2 = ["💥", "🔥", "❤️‍", "😎", "🤣"]


with open(cesta_k_citatum, "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        slovo = line.strip()
        print(slovo)
        
print("-----")

emoji_1.