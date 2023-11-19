def f(x):
    return x**3 - 2*x**2 - 5

def ikiye_bolme(a, b, iterasyon):
    if f(a) * f(b) > 0:
        print("Bu aralıkta kök yoktur.")
        return None

    for i in range(iterasyon):
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < 1e-10:
            # Eğer kök tam olarak bulunursa ya da aralık çok küçükse, işlemi sonlandır.
            return c

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

        print(f'{i+1}. Iterasyon : [{a}, {b}] Kokleri arasındaki yaklasik degeri: {c}')

    return (a + b) / 2

# Başlangıç aralığı
a = 2
b = 4

# İterasyon sayısı
iterasyon = 3

# İkili bölme metodu ile kökü bulma
root = ikiye_bolme(a, b, iterasyon=3)

print(f'Ikıye bolme metodu ile 4. iterasyonda bulunan kok: {root}')
