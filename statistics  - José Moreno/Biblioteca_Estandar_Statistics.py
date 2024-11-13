import statistics as st
from colorama import init, Back, Fore, Style

init ( )

numbers = [10, 20, 30, 40, 50, 60, 60, 60, 70, 80, 90, 100, 110, 130, 140, 140, 140, 150, 160, 170, 170, 170, 180, 190, 195]

print(f"\n\n\n{Style.BRIGHT}{Fore.CYAN}Librería Statistic y Análisis Estadístico\n\n\n")

print(f"{Style.NORMAL}{Fore.WHITE}Promedios y medidas de tendencia central\n")

#Media aritmética ("Promedio")
mean_numbers = st.mean(numbers)
print(f"{Style.DIM}{Fore.GREEN}La media es:{Fore.RED} {mean_numbers}")

#Valor central de los datos
median_numbers = st.median(numbers)
print(f"{Fore.GREEN}La mediana es:{Fore.RED} {median_numbers}")

#Valor central de los datos
medianLow_numbers = st.median_low(numbers)
print(f"{Fore.GREEN}La mediana es:{Fore.RED} {medianLow_numbers}")

#Valor más común
mode_numbers = st.mode(numbers)
print(f"{Fore.GREEN}La moda es:{Fore.RED} {mode_numbers}")

#Moda única (Valor más común)
mode_numbers = st.mode(numbers)
print(f"{Fore.GREEN}La moda es:{Fore.RED} {mode_numbers}")

#Lista de modas (Valores más comunes)
multimode_numbers = st.multimode(numbers)
print(f"{Fore.GREEN}La lista de modas:{Fore.RED} {multimode_numbers}")

#Datos en Intervalos equiprobables
quantiles_numbers = st.quantiles(numbers, n=5)
print (f"{Fore.GREEN}El conjunto de números agrupados en intervalos de 5 son:{Fore.RED} {quantiles_numbers}\n\n\n")

print(f"{Style.NORMAL}{Fore.WHITE}Medidas de dispersión de datos\n")

#Desviación estándar
stddev_numbers=st.stdev(numbers)
print(f"{Style.DIM}{Fore.GREEN}La variación estándar es: {Fore.RED}{stddev_numbers}")

max_numbers = max(numbers)
min_numbers = min(numbers)

print(f"{Fore.GREEN}El valor máximo es:{Fore.RED} {max_numbers}")
print(f"{Fore.GREEN}El valor mínimo es:{Fore.RED} {min_numbers}")


#Rango
range_numbers = max_numbers - min_numbers
print (f"{Fore.GREEN}Rango de ventas:{Fore.RED} {range_numbers}\n\n")