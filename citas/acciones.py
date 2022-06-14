import citas.citas as modelo

class Acciones:
    def agregar(self, doctor):
        print(f"\n[{doctor[6].upper()}] {doctor[1]} {doctor[2]}  - Agregar nueva cita medica")

        nom_paciente = input("Nombre del paciente: ")
        genero = input("Genero (M/F): ")
        edad = input("Edad: ")
        telefono = input("Telefono: ")
        fecha_consulta = input("Fecha de tu consulta [yyyy-mm-dd]: ")

        consulta = modelo.Consulta(doctor[0], nom_paciente, genero, edad, telefono, fecha_consulta)
        guardar = consulta.agregar()
        if guardar[0] >= 1:
            print(f"\nYa tiene tu consulta medica  {consulta.nom_paciente}\n")
        else:
            print(f"\nUpss! Tuvimos un error al procesar tu acción {doctor[1]}")
    
    def listar(self, doctor):
        print(f"\n[{doctor[6].upper()}] {doctor[1]} {doctor[2]} - Mostrar citas medicas")
        consulta = modelo.Consulta(doctor[0])
        consultas = consulta.listar()

        for consulta in consultas:
            print(f"""
    Paciente: {consulta[2]}
    Genero: {consulta[3]}
    Edad: {consulta[4]}
    Telefono: {consulta[5]}
    Para el: {consulta[6]}
    Agendado el: {consulta[7]}
    -----------------------------------------""")

    def actualizar(self, doctor):
        print(f"\n[{doctor[6].upper()}] {doctor[1]} {doctor[2]} - Modificar una cita medica")

        nom_paciente = input("Nombre del paciente?: ")

        consulta = modelo.Consulta(doctor[0], nom_paciente)
        validar = consulta.validar()
        if validar[0] != 0:
            self.modificar(doctor, nom_paciente)
        else:
            print(f"\nError 404 no se localizo la cita medica de: [{nom_paciente}], intentelo de nuevo medico : {doctor[1]}")

    def modificar(self, doctor,nombre):
        print(f"\n[{doctor[6].upper()}] {doctor[1]} {doctor[2]} - Favor de llenar los nuevos datos del paciente: {nombre}")

        nom_paciente = input("Ingresar nombre: ")
        genero = input("Ingresar el genero (M/F): ")
        edad = input("Ingresar la edad: ")
        telefono = input("Ingresar su telefono: ")
        fecha_consulta = input("Ingresar la fecha [yyyy-mm-dd]: ")

        consulta = modelo.Consulta(doctor[0], nom_paciente, genero, edad, telefono, fecha_consulta, nombre)
        guardar = consulta.actualizar()
        if guardar[0] >= 1:
            print(f"\nSe han actualizado los datos de: {consulta.nom_paciente}")
        else:
            print(f"\nNo se han actualizado los datos, medico: {doctor[1]}")
    
    def eliminar(self, doctor):
        print(f"\n[{doctor[6].upper()}] {doctor[1]} {doctor[2]} - Borrar una cita medica")
        nom_paciente = input("Ingresa el nombre del paciente, para poder eliminar su cita medica: ")

        nota = modelo.Consulta(doctor[0], nom_paciente)
        eliminar = nota.eliminar()
        if eliminar[0] >= 1:
            print(f"\n Listo! Ya no tienes ninguna cita: {nota.nom_paciente}")
        else:
            print("\nError 404 Sigues teniendo una cita en el consultorio...")
        