def fonction(x):
    y = 0.3 * x**2 - 7
    return y

def dychotomie(f, a, b, k, epsilon):
    # cas d'une fonction croissante monotone sur l'intervalle
    debut = a
    fin = b
    ecart = b - a
    iteration = 0
    while ecart > epsilon:
        milieu = (debut + fin) / 2
        if f(milieu) > k:
            # la solution est inférieure à m
            fin = milieu
        else:
            # la solution est supérieure à m
            debut = milieu
        ecart = fin - debut
        iteration += 1
    return milieu, iteration

result, iteration = dychotomie(fonction, 0, 10, 0, 0.001)
print('résultat :',result, '(en', iteration, 'itérations, avec une précision au millième)')
