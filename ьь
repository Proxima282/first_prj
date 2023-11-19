def write_file():
    with open('quotes.txt', 'a',encoding='utf-8') as f:
        text = input('Введи текст або цитату відомого українскього поета -> ')
        author = input('Введи автора данних рядків -> ')
        last_line = f'({author})\n----------\n'
        text+= '\n'
        f.writelines([text,last_line])

#write_file()
#i = 'Так'
#while i != 'ні':
    #write_file()
#i = input('Працюємо далі?')
    

    
with open('quotes.txt', 'r',encoding='utf-8') as f:
    for l in f:
        print(l)
