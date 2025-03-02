import numpy as np

num_estudiantes=6500

year_est=np.random.randint(1975, 2026, size=num_estudiantes)
carrera_est=np.random.randint(10, 51, size=num_estudiantes)
final_est=np.random.randint(0, 100, size=num_estudiantes)

nombres=np.array(["Estudiante_" + str(i) for i in range(num_estudiantes)])
codigo_est=(year_est*10000)+(carrera_est*100)+final_est

prom=   np.round(np.random.uniform(0.0, 5.0, size=num_estudiantes), 2)

# ------------------------- FILTER BY CAREER X -------------------------
carrera_x = int(input("Ingrese el còdigo de la carreara (10-50): "))  # User inputs career code

# Get students in career X with GPA >= 4.0
filtro_carrera_x = (carrera_est == carrera_x) & (prom >= 4.0)
cods_filtros = codigo_est[filtro_carrera_x]
nombres_filtrados = nombres[filtro_carrera_x]
                            
print("\nStudents in career", carrera_x, "with GPA >= 4.0:")
for code, name in zip(cods_filtros, nombres_filtrados):
    print(f"Code: {code}, Name: {name}")

print("Total students in career", carrera_x, "with GPA >= 4.0:", len(cods_filtros))

# ------------------------- FILTER BY YEAR <1990 -------------------------

# Get students in career X with GPA >= 4.0
filtro_condicional = (year_est <1990) & (prom < 3.0)
cods_filtros = codigo_est[filtro_condicional]
nombres_filtrados = nombres[filtro_condicional]
                            
print("\nStudents who entered before 1990 and are conditional (GPA < 3.0):  ")
for code, name in zip(cods_filtros, nombres_filtrados):
    print(f"Code: {code}, Name: {name}")

print("Total students before 1990 and conditional:", len(cods_filtros))
