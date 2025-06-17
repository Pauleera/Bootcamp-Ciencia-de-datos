
import pandas as pd 
# Crea un DataFrame con los siguientes datos:


df = pd.DataFrame(data = {
    "Jugador":['Lionel Messi'  , 'Cristiano Ronaldo', 'Kevin De Bruyne', 'Kylian Mbappé','Luka Modric' ],
    "Posicion":['Delantero', 'Delantero', 'Mediocampista', 'Delantero','Mediocampista'],
    "Edad":[36, 38, 31, 24, 37],
    "Goles":[20, 18, 8, 25, 3],
    "Asistencias":[10, 5, 15, 12, 8]
})

#2. Muestra la columna Jugador 
print("Columna Jugador:")
print(df['Jugador'])

#3. Filtrar jugadores con más de 10 goles 
print("\nJugadores con más de 10 goles:")
print(df[df['Goles']> 10 ][['Jugador','Goles']] )

# 4. Agregar una nueva columna 
df['Puntos'] = df['Goles'] + (df['Asistencias']*2)
print("\nDataFrame con la nueva columna Puntos:")
print(df)

# 5. Calcular promedio de goles 
print("\nPromedio de goles:")
print(df['Goles'].mean())

# 6. Máximo y mínimo de asistencias
print("\nMáximo de asistencias:")
print(df['Asistencias'].max())
print("\nMínimo de asistencias:")
print(df['Asistencias'].min())

# 7. Jugadores por posición 
print("\nJugadores por posición:")
print(df['Posicion'].value_counts())    

# 8. Ordenar por goles descendentes
print("\nDataFrame ordenado por goles descendentes:")
print(df.sort_values(by='Goles', ascending=False))
