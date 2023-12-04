def inverter(palavra):
    texto=palavra.split()
    texto_invertido=reversed(texto)
    texto_completo=' '.join(texto_invertido)
    print(texto_completo)

texto="python é incrivel"
inverter(texto)