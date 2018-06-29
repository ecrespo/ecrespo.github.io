#Importar módulo gconf
import gconf

#Creando la clase Conf
class Conf:
    def __init__(self):
        #Se asocia al cliente de gconf
        self.gconfClient = gconf.client_get_default()
        #variable aplicaciones que contiene las aplicaciones a asociar
        self.aplicaciones = ("orca",
                                "gnome-terminal",
                                "oowriter",
                                "iceweasel",
                                "nautilus",
                                "ooimpress",
                                "pidgin",
                                "oocalc",
                                "gedit",
                                "gnome-calculator",
                                "rhythmbox")
        #Asignación de las rutas de configuración del gconf
        self.comando = "/apps/metacity/keybinding_commands/command_"
        self.asignacion_teclado = "/apps/metacity/global_keybindings/run_command_"
        #Asociación de las teclas rápidas con las aplicaciones
        self.teclas = {"orca":"o",
                        "gnome-terminal":"t",
                        "oowriter":"w",
                        "iceweasel":"n",
                        "nautilus":"h",
                        "ooimpress":"i",
                        "pidgin":"p",
                        "oocalc":"x",
                        "gedit":"e",
                        "gnome-calculator":"c",
                        "rhythmbox":"m"}

    #Modificación de la configuración de gconf
    def modificar(self):
        cont = 1
        for aplicacion in self.aplicaciones:
            ruta1 =  "%s%s" %(self.comando,cont)
            ruta2 = "%s%s"  %(self.asignacion_teclado,cont)
            self.gconfClient.set_string(ruta1, "%s" %aplicacion)
            self.gconfClient.set_string(ruta2, "%s" %self.teclas[aplicacion])
            cont = cont +1

    #Listar las configuraciones de gconf relacionadas con las aplicaciones a
    #ejecutar con los accesos rápidos
    def listar(self):
        cont = 1
        for aplicacion in self.aplicaciones:
            ruta1 =  "%s%s" %(self.comando,cont)
            ruta2 = "%s%s"  %(self.asignacion_teclado,cont)
            print self.gconfClient.get_string(ruta1),self.gconfClient.get_string(ruta2)
            cont = cont +1


if __name__ == "__main__":


    def mensaje():
        #Mensaje de ayuda del comando
        print "pyconfig-orca options "
        print "option : --help    : Print this help"
        print "option : --list    : List gconf for gnome-orca"
        print "option : --change  : Change gconf for gnome-orca"

    #Importar módulo sys y instanciar la clase Conf
    import sys
    config = Conf()
    #Si hay un argumento solamente (nombre del programa), muestra la ayuda
    if len(sys.argv) == 1 :
        mensaje()
    #Si hay 2 argumentos (nombre del comando y acción)
    elif len(sys.argv) == 2:
        #Si argumento es --list se lista la configuración, sí es --change se
        #cambia la configuración del gconf
        if sys.argv[1] == "--list" :
            config.listar()
        elif sys.argv[1] == "--change":
            config.modificar()
        elif sys.argv[1] == "--help" :
            mensaje()
        else:
            mensaje()
    else:
        mensaje()
