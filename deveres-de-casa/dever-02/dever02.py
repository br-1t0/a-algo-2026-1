import time as t
import sys as s
import math as m

s.setrecursionlimit(10010)


def calcular_fatorial(n: int):

    if n == 0:
        return 1
    return n * calcular_fatorial(n - 1)


valores = [10, 100, 500, 1000]
tempo = []
results = []
for n in valores:
    start_time = t.perf_counter()
    results.append(calcular_fatorial(n))
    end_time = t.perf_counter()
    tempo.append(end_time - start_time)


print(
    f"Fatorial de 10, na escala de log10 é {m.log10(results[0])} e demorou {tempo[0]*1e6} micro segundos"
)

print(
    f"Fatorial de 100, na escala log10 é {m.log10(results[1])} e demorou {tempo[1]*1e6} micro segundos"
)

print(
    f"Fatorial de 500, na escala de log10 é {m.log10(results[2])} e demorou {tempo[2]*1e6} micro segundos"
)

print(
    f"Fatorial de 1000, na escala de log10  é {m.log10(results[3])} e demorou {tempo[3]*1e6} micro segundos"
)


"""
Em relação a análise assintótica, a função calcular_fatorial será chamada n vezes.
Logo, conclui-se que o BigO é O(n), linear. 
Consequentemente, percebe-se um crescimento próximo do linear no tempo de execução:
    Para o fatorial de 10 o tempo foi aproximadamente 2.4 10^-6 segundos.
    Para o fatorial de 100 (um aumento de 10x) o tempo foi aproximadamente 13 10^-6 segundos.
    Já para o fatorial de 500 (um aumento de 5x) o tempo foi aproximadamente 109 10^-6 segundos.
    E por fim, o fatorial de 1000 (aumento de 2x) retornou um tempo aproximado a 320 10^-6 segundos.

O aumento segue uma tendência linear. 
Em relação do crescimento não ser exatamente proporcional ao aumento de n, isso se deve a diversos fatores
como a pequena quantidade de n e as variações de tempo devido a variáveis da máquina e tempo de multiplicação 
de números grandes.

Podemos, mesmo com esses valores pequenos analisar a ordem de grandeza do cálculo do tempo/n para cada input.
E, assim como demonstrado a seguir, a ordem de grandeza é a mesma, contribuindo para a conclusão da análise 
assintótica ser O(n).

"""
n_valor = zip(valores, tempo)
for n, tempos in n_valor:
    print(f"Para {tempos } e n {n}: {tempos / n}")
