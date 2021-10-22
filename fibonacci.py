"""
Functie om planning-poker fibonacci-reeksen te maken

Author: Max Oostrom
"""

def fibonaccilijst(aantal_getallen):
    """Genereer een lijst van Fibbonaci-achtige aard voor planning-poker, [0.5, 1, 2, 3, 5, ...]

    Args:
        aantal_getallen (int): aantal getallen dat gegenereerd moeten worden

    Returns:
        list: lijst met de Fibbonaci-achtige getallen
    """
    assert isinstance(aantal_getallen, int), "Input moet integer zijn"
    assert aantal_getallen >= 0, "Input moet positief zijn"

    fibb_list = [];

    if (aantal_getallen == 0):
        fibb_list = [];
    elif (aantal_getallen == 1):
        fibb_list = [0.5];
    elif (aantal_getallen == 2):
        fibb_list = [0.5, 1];
    elif (aantal_getallen == 3):
        fibb_list = [0.5, 1, 2];    
    else:
        fibb_list = [0.5, 1, 2];
        for i in range(3, aantal_getallen):
            fibb_list.append(fibb_list[-2]+fibb_list[-1])
    return fibb_list

if __name__=="__main__":
    assert len(fibonaccilijst(50)) == 50, 'Fout: aantal retour waarden klopt niet'
    assert fibonaccilijst(0) == [], 'Fout: teruggegeven waarden kloppen niet'
    assert fibonaccilijst(1) == [0.5], 'Fout: teruggegeven waarden kloppen niet'
    assert fibonaccilijst(2) == [0.5, 1], 'Fout: teruggegeven waarden kloppen niet'
    assert fibonaccilijst(3) == [0.5, 1, 2], 'Fout: teruggegeven waarden kloppen niet'
    assert fibonaccilijst(4) == [0.5, 1, 2, 3], 'Fout: teruggegeven waarden kloppen niet'
    assert fibonaccilijst(5) == [0.5, 1, 2, 3, 5], 'Fout: teruggegeven waarden kloppen niet'
    print(fibonaccilijst(5))