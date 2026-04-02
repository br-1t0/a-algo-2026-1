"""
Cálculos de complexidade para:

TEOREMA MESTRE: T(n) = aT(n/b) + cn^d




MERGE SORT

Modelando a recorrência:
2T(n/2) + n
Aplicando o teorema mestre:
2 = 2^1
Logo, O(nlog n)





MULTIPLICAÇÃO DE MATRIZES

Considerando um loop triplamente aninhado, O(n) seria: O(n^3)








RECORRÊNCIAS:
    2T(n/4) + sqrt(n)
    Isso equivale a 2T(n/4) + n^1/2
    Aplicando o teorema mestre e verificando o primeiro caso:
    a = b^d?
    2 = 4^1/2?
    2 = 2
    Conclui-se que O(n) da recorrência é : O(n^1/2 * logn)



    2T(n/4) + n
    Aplicando o teorema mestre e verificando o segundo caso:
    a < b^d ?
    2 < 4^1 ?
    Conclui-se que O(n) da recorrência é: O(n)


    16T(n/4) + n^2
    Aplicando o teorema mestre e verificando o primeiro caso:
    a = b^d?
    16 = 4^2?
    16 = 16
    Conclui-se que O(n) da recorrêcia é: O(n^2 * logn)
"""
