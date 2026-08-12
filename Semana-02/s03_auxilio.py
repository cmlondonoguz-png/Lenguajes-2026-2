SMMLV = 1423500
AUXILIO = 200000
salarios = [1200000, 3500000, 1800000, 2600000, 1423500]

total = 0
for salario in salarios:          # REPETICIÓN
    pago = salario
    if salario < 2 * SMMLV:       # DECISIÓN
        pago += AUXILIO
    total += pago                 # SECUENCIA

print("Total nómina:", total)
