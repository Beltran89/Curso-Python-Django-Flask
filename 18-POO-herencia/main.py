import clases

persona = clases.Persona()
persona.setNombre("Ruben")
persona.setApellido("Beltran")
persona.setAltura("190cm")
persona.setEdad(31)

print(f"La Persona es:  {persona.getNombre()} {persona.getApellido()}")
print(persona.hablar())

informatico = clases.Informatico()
informatico.setNombre("Steve")
informatico.setApellido("Jobs")

print(f"EL informatico es : {informatico.getNombre()} {informatico.getApellido()}")
print(informatico.getLenguajes())
print(informatico.programar())
informatico.setLenguajes("Java")
print(informatico.getLenguajes())

tecnico = clases.TecnicoRedes()
print(tecnico.auditarRedes)
print(tecnico.getLenguajes())