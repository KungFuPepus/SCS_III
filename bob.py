import numpy as np
from collections import Counter

# Tekst do analizy
text = "AABCBAD"

print("=" * 80)
print("OBLICZANIE ENTROPII SHANNONA DLA TEKSTU: \"AABCBAD\"")
print("=" * 80)

# Krok 1: Zlicz częstości
freq = Counter(text)
n_total = len(text)

print(f"\nTekst: {text}")
print(f"Długość tekstu: {n_total} znaków")

# Krok 2: Oblicz prawdopodobieństwa
print("\n" + "-" * 80)
print("Krok 1: Zliczenie częstości wystąpień symboli")
print("-" * 80)

probabilities = {}
for char in sorted(freq.keys()):
    count = freq[char]
    prob = count / n_total
    probabilities[char] = prob
    print(f"Symbol '{char}': {count} wystąpień, p('{char}') = {count}/{n_total} = {prob:.4f}")

# Krok 3: Oblicz entropię
print("\n" + "-" * 80)
print("Krok 2: Obliczanie entropii H(X) = -Σ p(xi) * log₂(p(xi))")
print("-" * 80)

entropy = 0
contributions = []

for char in sorted(probabilities.keys()):
    prob = probabilities[char]
    if prob > 0:
        # Oblicz informację własną: -log₂(p)
        self_info = -np.log2(prob)
        # Oblicz wkład do entropii: p * (-log₂(p))
        contribution = prob * self_info
        entropy += contribution
        contributions.append((char, prob, self_info, contribution))
        
        print(f"\nSymbol '{char}':")
        print(f"  p('{char}') = {prob:.4f}")
        print(f"  -log₂({prob:.4f}) = {self_info:.4f} bitów")
        print(f"  Wkład do entropii = {prob:.4f} × {self_info:.4f} = {contribution:.4f} bitów")

print("\n" + "=" * 80)
print("WYNIK KOŃCOWY")
print("=" * 80)

print(f"\nEntropia H(X) = {entropy:.4f} bitów/symbol")
print(f"              ≈ {entropy:.2f} bitów/symbol")

# Porównanie z maksymalną entropią
n_symbols = len(probabilities)
max_entropy = np.log2(n_symbols)
efficiency = (entropy / max_entropy) * 100

print(f"\n" + "-" * 80)
print("DODATKOWA ANALIZA")
print("-" * 80)

print(f"\nLiczba unikalnych symboli: {n_symbols}")
print(f"Maksymalna możliwa entropia (rozkład równomierny): log₂({n_symbols}) = {max_entropy:.4f} bitów")
print(f"Stosunek entropii rzeczywistej do maksymalnej: {efficiency:.2f}%")

# Interpretacja
print(f"\n" + "-" * 80)
print("INTERPRETACJA")
print("-" * 80)

print(f"\nEntropia H(X) = {entropy:.4f} bitów/symbol oznacza:")
print(f"  • Średnio potrzeba {entropy:.4f} bitów do zakodowania jednego symbolu")
print(f"  • Minimalna średnia długość kodu prefiksowego wynosi {entropy:.4f} bitów/symbol")
print(f"  • Teoretyczna kompresja całego tekstu: {n_total} × {entropy:.4f} = {n_total * entropy:.2f} bitów")
print(f"  • W porównaniu do ASCII (8 bitów/znak): oszczędność {((8 - entropy) / 8 * 100):.1f}%")

# Szczegółowe podsumowanie
print(f"\n" + "=" * 80)
print("SZCZEGÓŁOWE OBLICZENIA KROK PO KROKU")
print("=" * 80)

print("\nWzór entropii Shannona:")
print("H(X) = -Σ p(xi) * log₂(p(xi))")
print("     = ", end="")

terms = []
for char, prob, self_info, contribution in contributions:
    terms.append(f"-({prob:.4f} × log₂({prob:.4f}))")

print(" + ".join(terms))

print("\n     = ", end="")
terms2 = []
for char, prob, self_info, contribution in contributions:
    terms2.append(f"({contribution:.4f})")
print(" + ".join(terms2))

print(f"\n     = {entropy:.4f} bitów/symbol")

print("\n" + "=" * 80)

# Sprawdzenie, czy rozkład jest równomierny
is_uniform = len(set(probabilities.values())) == 1
if is_uniform:
    print("\n✓ Rozkład jest RÓWNOMIERNY - entropia jest maksymalna")
else:
    print("\n✗ Rozkład jest NIERÓWNOMIERNY - entropia jest mniejsza niż maksymalna")
    print(f"  Różnica: {max_entropy - entropy:.4f} bitów ({(max_entropy - entropy)/max_entropy * 100:.1f}%)")