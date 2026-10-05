def converter(valor, origem, destino):
    if origem == "pe":
        metros = valor * 0.3048
    elif origem == "metro":
        metros = valor
    elif origem == "jarda":
        metros = valor * 0.9144
    else:
        return None

    if destino == "pe":
        return metros / 0.3048
    elif destino == "metro":
        return metros
    elif destino == "jarda":
        return metros / 0.9144
    else:
        return None