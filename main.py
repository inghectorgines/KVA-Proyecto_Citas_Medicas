from medicos import acciones

print("""
Seleccione una acción:
    - Registro 
    - Login 
    - Salir  
""")
hazEl = acciones.Acciones()

accion = input("¿Qué quiere hacer?: ")
if accion == "Registro":
    hazEl.registro()
elif accion == "Login":
    hazEl.login()
elif accion == "Salir":
    print("\n Has salido del sistema de citas medicas.")