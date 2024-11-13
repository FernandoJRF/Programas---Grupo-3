import statistics as st

numbers = [10, 20, 30, 40, 50, 60, 60, 60, 70, 80, 90, 100, 110, 130, 140, 140, 140, 150, 160, 170, 170, 170, 180, 190, 195]

#Promedios y medidas de tendencia central

#Media aritmética ("Promedio")
mean_numbers = st.mean(numbers)
print("La media es: {:.2f}".format(mean_numbers))

#Valor central de los datos
median_numbers = st.median(numbers)
print(f"La mediana es: {median_numbers}")

#Valor central de los datos
medianLow_numbers = st.median_low(numbers)
print(f"La mediana es: {medianLow_numbers}")

#Valor más común
mode_numbers = st.mode(numbers)
print(f"La moda es: {mode_numbers}")

#Moda única (Valor más común)
mode_numbers = st.mode(numbers)
print(f"La moda es: {mode_numbers}")

#Lista de modas (Valores más comunes)
multimode_numbers = st.multimode(numbers)
print(f"La lista de modas: {multimode_numbers}")

#Datos en Intervalos equiprobables
quantiles_numbers = st.quantiles(numbers, n=5)
print (f"El conjunto de números agrupados en intervalos de 5 son: {quantiles_numbers}")

#Medidas de dispersión de datos

#Desviación estándar
print(st.stdev(numbers))

max_numbers = max(numbers)
min_numbers = min(numbers)

print(f"El valor máximo es: {max_numbers}")
print(f"El valor mínimo es: {min_numbers}")


#Rango
range_numbers = max_numbers - min_numbers
print (f"Rango de ventas: {range_numbers}")