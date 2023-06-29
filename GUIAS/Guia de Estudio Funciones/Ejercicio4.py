def calcular_vuelto(precio_carro, pago):
    while  pago < precio_carro:
        pago = int(input(f"El pago es insuficiente, porfavor ingrese al menos ${precio_carro}: "))
    vuelto = pago - precio_carro
    billetes = [20000, 10000, 5000, 2000, 1000]
    monedas = [500, 100, 50, 10]

    print(f"Vuelto total: {vuelto}")
    for i in billetes:
        if vuelto >= i:
            cantidad = vuelto // i
            vuelto -= i * cantidad
            print(f"{cantidad} billetes de ${i}")

    for j in monedas:
        if vuelto >= j:
            cantidad = vuelto // j
            vuelto -= j * cantidad
            print(f"{cantidad} monedas de ${j}")

precio_carro = int(input("Ingrese el total de su compra: "))
pago = int(input("Ingrese con cuanto va a pagar: "))

calcular_vuelto(precio_carro, pago)