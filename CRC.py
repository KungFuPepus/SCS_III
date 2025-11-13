def compute_crc_steps(data_bits: str, poly_bits: str):
    """
    Oblicza CRC dla ciągu bitów, wyświetlając stan reszty po każdej iteracji XOR.
    :param data_bits: ciąg bitów danych, np. "11010011101110"
    :param poly_bits: ciąg bitów wielomianu, np. "1011"
    """
    # Stopień wielomianu
    n = len(poly_bits) - 1

    # Dopisz n zer na końcu danych
    dividend = list(data_bits + "0" * n)
    divisor = list(poly_bits)
    length = len(dividend)

    print(f"Dane wejściowe z dopisanymi zerami: {''.join(dividend)}")
    print(f"Wielomian: {poly_bits} (stopień {n})")
    print()

    # Pozycja przesunięcia dzielnika
    pos = 0
    while pos <= length - len(divisor):
        # Jeżeli najbardziej znaczący bit reszty to 1, wykonaj XOR
        if dividend[pos] == '1':
            # Wyświetl przed XOR
            window = ''.join(dividend[pos:pos+len(divisor)])
            print(f"Iteracja pos={pos+1}: segment przed XOR: {window}")
            # Wykonaj XOR bit po bicie
            for i in range(len(divisor)):
                dividend[pos + i] = '0' if dividend[pos + i] == divisor[i] else '1'
            # Wyświetl po XOR
            window_after = ''.join(dividend[pos:pos+len(divisor)])
            print(f"             po  XOR: {window_after}")
            print()
        else:
            # Jeśli bit = 0, pomiń XOR
            print(f"Iteracja pos={pos+1}: wiodące 0, pomijamy XOR")
            print()
        pos += 1

    # Ostatnie n bitów to suma CRC
    crc = ''.join(dividend[-n:])
    print(f"Reszta (CRC) = {crc}")
    return crc

if __name__ == "__main__":
    # Przykład użycia
    data = input("Podaj dane bitowe (np. 11010011101110): ").strip()
    poly = input("Podaj wielomian CRC (np. 1011): ").strip()
    print()
    crc = compute_crc_steps(data, poly)
    print(f"\nSuma kontrolna CRC dla danych '{data}' i wielomianu '{poly}' to: {crc}")
