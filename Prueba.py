# Autenticación
def login():
    usuario = input("Usuario: ")
    password = input("Password: ")
    if usuario == "Docente" and password == "1234":
        print("¡Acceso concedido!")
        return True
    else:
        print("Credenciales incorrectas.")
        return False

# Registro de estudiantes
estudiantes = {"A": [], "B": []}

def ingresar_estudiante():
    nombre = input("Nombre del estudiante: ")
    curso = input("Curso (A/B): ").upper()
    if curso not in estudiantes:
        print("Curso no válido.")
        return

    try:
        cantidad_notas = int(input("¿Cuántas notas desea ingresar para este estudiante?: "))
    except ValueError:
        print("Número inválido.")
        return

    notas = []
    for i in range(cantidad_notas):
        try:
            nota = float(input(f"Ingrese nota {i+1}: "))
            notas.append(nota)
        except ValueError:
            print("Entrada no válida.")
            return

    promedio = sum(notas) / len(notas)
    estudiantes[curso].append({
        "nombre": nombre,
        "notas": notas,
        "promedio": promedio
    })
    print(f"Estudiante {nombre} registrado en curso {curso} con promedio {promedio:.2f}")

def ver_estudiantes():
    for curso, lista in estudiantes.items():
        print(f"\n--- Curso {curso} ---")
        if not lista:
            print("Sin estudiantes registrados.")
            continue
        for est in lista:
            notas_str = ", ".join(str(n) for n in est["notas"])
            print(f"{est['nombre']}: Notas: {notas_str} | Promedio: {est['promedio']:.2f}")

# Exportar a PDF
def exportar_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for curso, lista in estudiantes.items():
        pdf.set_font("Arial", 'B', size=14)
        pdf.cell(200, 10, f"Curso {curso}", ln=True)
        pdf.set_font("Arial", size=12)

        if not lista:
            pdf.cell(200, 10, "Sin estudiantes registrados.", ln=True)
            continue

        for estudiante in lista:
            notas_str = ", ".join(str(nota) for nota in estudiante["notas"])
            pdf.cell(200, 10, f"{estudiante['nombre']} - Notas: {notas_str} - Promedio: {estudiante['promedio']:.2f}", ln=True)

    pdf.output("promedios_estudiantes.pdf")
    print("PDF generado como 'promedios_estudiantes.pdf'.")

# Menú principal
def menu():
    while True:
        print("\n1. Ingresar estudiante")
        print("2. Ver estudiantes y promedios")
        print("3. Exportar PDF")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_estudiante()
        elif opcion == "2":
            ver_estudiantes()
        elif opcion == "3":
            exportar_pdf()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

# Ejecución
if __name__ == "__main__":
    if login():
        menu()
