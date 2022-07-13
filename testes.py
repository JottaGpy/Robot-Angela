nome = input("Digite seu nome: ")
altura = float( input('Digite sua altura (ex:1.70): ') )
peso = float( input('Digite seu peso (ex:55.500): ') )

resultado = peso / (altura * altura)

if resultado < 18.5:
    phrase = (nome, 'your BMI is:', resultado, 'You are underweight.')

    for phrase in phrase:
            print(phrase)

    if not True:
        pass
    else:


if resultado < 24.9:
    phrase = (nome, 'your BMI is:', resultado, 'You are in the ideal weight.')

    for phrase in phrase:
        print(phrase)

    if not True:
        pass
    else:
        break


elif resultado < 29.9:
    phrase = (nome, 'your BMI is:', resultado, 'You are overweight.')

    for phrase in phrase:
        print(phrase)

    if not True:
        pass
    else:
        break

elif resultado < 34.9:
    phrase = (nome, 'your BMI is:', resultado, 'You are in obesity degree 1.')

    for phrase in phrase:
        print(phrase)

    if not True:
        pass
    else:
        break

elif resultado < 39.9:
    phrase = (nome, 'your BMI is:', resultado, 'You are in obesity degree 2.')

    for phrase in phrase:
        print(phrase)

    if not True:
        pass
    else:
        break

if resultado >= 40.0:
    phrase = (nome, 'your BMI is:', resultado, 'You are obesity degree 3.')

    for phrase in phrase:
        print(phrase)

    if True:
        break
