line1 = input().split(" ")
line2 = input().split(" ")

qdtProd1 = int(line1[1])
valProd1 = float(line1[2])

qdtProd2 = int(line2[1])
valProd2 = float(line2[2])


totalVal = (qdtProd1*valProd1) + (qdtProd2*valProd2)
print("VALOR A PAGAR: R$ %.2f" %totalVal)
