linguagens = ["java", "python", "c", "javaScript", "csharp"]
print(sorted(linguagens, key= lambda x: len(x))) # sorted é estrutura built-in

inguagens = ["java", "python", "c", "javaScript", "csharp"]
print(sorted(linguagens, key= lambda x: len(x), reverse= True))

linguagens = ["java", "python", "c", "javaScript", "csharp"] # deixa em ordem alfabetica
print(sorted(linguagens))