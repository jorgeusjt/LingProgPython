def ten_33 (lista):
        status = "Nada"
        for simbolo in lista:
            if simbolo == 3:
                if status == "Nada":
                    staus = "Tres"
                elif status == "Tres":
                    return True
                else:
                    if status == "Tres":
                        status = "Nada"
        return False
print(tem_33 ([3,3,1]))
print(tem_33 ([3,1,3,1,3]))
print(tem_33([1,1,1,3,1,1,1,3,1,1,1,3,3]))