entrada = input()
Valor_temperatura, escala = entrada.split()

Valor_temperatura = float(Valor_temperatura)

if escala.upper() == 'C':
    print('Temperatura em Celsius: {:.2f} °C'.format(Valor_temperatura))
    print('Temperatura em Fahrenheit: {:.2f} °F'.format(Valor_temperatura * 1.8 + 32))
    print('Temperatura em Kelvin: {:.2f} K'.format(Valor_temperatura + 273.15))
elif escala.upper() == 'F':
    print('Temperatura em Celsius: {:.2f} °C'.format((Valor_temperatura - 32) / 1.8))
    print('Temperatura em Fahrenheit: {:.2f} °F'.format(Valor_temperatura))
    print('Temperatura em Kelvin: {:.2f} K'.format((Valor_temperatura - 32) / 1.8 + 273.15))
elif escala.upper() == 'K':
    print('Temperatura em Celsius: {:.2f} °C'.format(Valor_temperatura - 273.15))
    print('Temperatura em Fahrenheit: {:.2f} °F'.format((Valor_temperatura - 273.15) * 1.8 + 32))
    print('Temperatura em Kelvin: {:.2f} K'.format(Valor_temperatura))
else:
    print('Escala inválida.')
