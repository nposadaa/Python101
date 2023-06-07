bud_jan = int(input("¿Cuál es el presupuesto de enero?"))
bud_feb = int(input("¿Cuál es el presupuesto de febrero?"))
bud_mar = int(input("¿Cuál es el presupuesto de marzo?"))

total_budget = bud_jan + bud_feb + bud_mar

avg_budgt = total_budget / 3

mensaje = f"El presupuesto de enero es {bud_jan}, febrero es {bud_feb} y marzo s {bud_mar}.Con esto, el presupuesto total es {total_budget}. Así calculamos un presupuesto promedio de {avg_budgt}"
print(mensaje)