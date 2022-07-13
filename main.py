inicio = ('Olá', 'meu nome é Angêla', 'irei te auxiliar na sua jornada da saúde', 'vamos começar!')
import pyttsx3

speak = pyttsx3.init('sapi5')

while True:
    print(inicio)

    speak.say(inicio)
    speak.runAndWait()

    nome = input("Digite seu nome: ")
    idade = input('Digite sua idade: ')
    altura = float( input('Digite sua altura (ex:1.70): ') )
    peso = float( input('Digite seu peso (ex:55.500): ') )

    resultado = peso // (altura * altura)

    if resultado < 18.5:
        import pyttsx3

        speak = pyttsx3.init('sapi5')

        phrase = (nome, 'calculei seu imc, o resultado aparecerá na tela', resultado, 'Você está abaixo do peso ideal.', 'Irei montar o treino ideal para aumentar o seu peso, também passarei uma dieta ideal para sua semana, com o objetivo de aumentar seu ganho calórico.', 'Aqui vão algumas dicas para você engordar', 'Coma de 3 em 3 horas, beba pelo menos 2,5 litros de água por dia, inclua proteína em todas as refeições e coma frutas pelo menos 3 vezes ao dia', 'vou te mostrar um exemplo de dieta semanal para você seguir, junto com seu treino que já processei com base nas informações passadas')

        for phrase in phrase:
            print(phrase)

            speak.say(phrase)
            speak.runAndWait()
        if True:
            break
        else:
            pass

    if resultado < 24.9:
        import pyttsx3

        speak = pyttsx3.init('sapi5')

        phrase = (nome, 'calculei seu imc, o resultado aparecerá na tela', resultado, 'Você está no peso ideal.', 'Irei montar o treino ideal para manter o seu peso, também passarei uma dieta ideal para sua semana.')

        for phrase in phrase:
            print(phrase)

            speak.say(phrase)
            speak.runAndWait()
        if True:
            break
        else:
            pass


    elif resultado < 29.9:
        import pyttsx3

        speak = pyttsx3.init('sapi5')

        phrase = (nome, 'calculei seu imc, o resultado aparecerá na tela', resultado, 'Você está acima do peso.', 'Irei montar o treino ideal para diminuir o seu peso, também passarei uma dieta ideal com foco no seu emagrecimento.')

        for phrase in phrase:
            print(phrase)

            speak.say(phrase)
            speak.runAndWait()
        if True:
            break
        else:
            pass

    elif resultado < 34.9:
        import pyttsx3

        speak = pyttsx3.init('sapi5')

        phrase = (nome, 'calculei seu imc, o resultado aparecerá na tela', resultado, 'Você está em obesidade grau 1.', 'Irei montar o treino ideal para diminuir o seu peso, também passarei uma dieta ideal com foco no seu emagrecimento.')

        for phrase in phrase:
            print(phrase)

            speak.say(phrase)
            speak.runAndWait()
        if True:
            break
        else:
            pass

    elif resultado < 39.9:
        import pyttsx3

        speak = pyttsx3.init('sapi5')

        phrase = (nome, 'calculei seu imc, o resultado aparecerá na tela', resultado, 'Você está em obesidade grau 2.', 'Irei montar o treino ideal para diminuir o seu peso, também passarei uma dieta ideal com foco no seu emagrecimento.')

        for phrase in phrase:
            print(phrase)

            speak.say(phrase)
            speak.runAndWait()
        if True:
            break
        else:
            pass

    if resultado >= 40.0:
        import pyttsx3

        speak = pyttsx3.init('sapi5')

        phrase = (nome, 'calculei seu imc, o resultado aparecerá na tela', resultado, 'Você está em obesidade grau 3.', 'Irei montar o treino ideal para diminuir o seu peso, também passarei uma dieta ideal com foco no seu emagrecimento.')

        for phrase in phrase:
            print(phrase)

            speak.say(phrase)
            speak.runAndWait()
        if True:
            break

