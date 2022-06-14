import medicos.medico as modelo
import citas.acciones

class Acciones:
    def registro(self):

        print("\nIngrese los siguientes datos de favor")
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        cedula = input("Cedula: ")
        especialidad = input("Especialidad: ")
        telefono = input("Numero de telefono: ")
        nconsultorio = input("Nombre del consultorio: ")
        email = input("Correo: ")
        password = input("Contraseña: ")

        doctor = modelo.Doctor(nombre, apellidos, cedula, especialidad, telefono, nconsultorio, email, password)
        registro = doctor.registrar()
        if registro[0] >= 1:
            print(f"\nRegistro exitoso {registro[1].nombre} {registro[1].apellidos} tu correo es: {registro[1].email}")
        else:
            print("\n Error 404 Algo salio mal en el proceso de registro.")

    def login(self):
        print("\nIngrese sus datos para entrar al sistema")
        # try:
        email = input("Introduzca su Email: ")
        password = input("Introduzca su contraseña: ")

        doctor = modelo.Doctor('','','','','', '',email, password)
        login = doctor.login()
        if email == login[7]:
            print(f"Consultorio:\n[{login[6].upper()}] Hola {login[1]} {login[2]}, ha iniciado sesión en el sistema con el correo {login[7]}")
            self.proximasAcciones(login)
        # except Exception as e:
        #     print(type(e)) - print(type(e).__name__)
        #     print("\nLogin incorrecto!! Intentalo más tarde")

    def proximasAcciones(self, doctor):
        print("""
        Acciones disponibles:
        - Agendar cita medica [Agendar]
        - Mostrar cita medica [Mostrar]
        - Modificar cita medica [Modificar]
        - Eliminar cita medica [Eliminar]
        - Salir 
        """ 
        )

        accion = input("Ingresa una opcion: ")
        hazEl = citas.acciones.Acciones()
        if accion == "Agendar":
            hazEl.agregar(doctor)
            self.proximasAcciones(doctor) 
        elif accion == "Mostrar":
            hazEl.listar(doctor)
            self.proximasAcciones(doctor)
        elif accion == "Modificar":
            hazEl.actualizar(doctor)
            self.proximasAcciones(doctor)
        elif accion == "Eliminar":
            hazEl.eliminar(doctor)
            self.proximasAcciones(doctor)
        elif accion == "Salir":
            print("\nHaz salido del sistema")
            exit()