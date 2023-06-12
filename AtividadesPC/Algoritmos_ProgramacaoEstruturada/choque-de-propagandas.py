amarelox1 = float(input("Insira a coordenada x da pop-up amarela: "))
amarelox2 = float(input("Insira a coordenada x2 da pop-up amarela: "))
amareloy1 = float(input("Insira a coordenada y da pop-up amarela: "))
amareloy2 = float(input("Insira a coordenada y2 da pop-up amarela: "))
verdex1 = float(input("Insira a coordenada x da pop-up verde: "))
verdex2 = float(input("Insira a coordenada x da pop-up verde: "))
verdey1 = float(input("Insira a coordenada y da pop-up verde: "))
verdey2 = float(input("Insira a coordenada y2 da pop-up verde: "))

if max(amarelox1, verdex1) < min(amarelox2, verdex2) and max(amareloy1, verdey1) < min(amareloy2, verdey2):
    print("Existe uma intersecção")
else:
    print("Não há intersecção") 
