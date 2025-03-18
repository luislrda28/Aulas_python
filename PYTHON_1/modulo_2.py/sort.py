linguagens = ["java", "python", "c", "javaScript", "csharp"]
linguagens.sort()
print(linguagens)

inguagens = ["java", "python", "c", "javaScript", "csharp"]
linguagens.sort(reverse= True)
print(linguagens)

inguagens = ["java", "python", "c", "javaScript", "csharp"]
linguagens.sort(key=lambda x: len(x))
print(linguagens)

inguagens = ["java", "python", "c", "javaScript", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse= True)
print(linguagens)