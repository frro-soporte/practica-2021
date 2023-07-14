from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import register


class CreateScreen(Screen):
   
   estadoUser = False
   estadoPass = False
   estadoConfirm = False
   estadoEmail = False


   def valido(self):
       print(self.estadoUser)
       print(self.estadoPass)
       print(self.estadoConfirm)
       print(self.estadoEmail)

       if self.estadoUser and self.estadoConfirm and self.estadoPass and self.estadoEmail:
           return True
       else:
           return False

   def changeScreen(self):
      user = self.ids.user.text
      password = self.ids.password.text
      email = self.ids.email.text
      register.registrar_persona(user,password, email)
      self.estadoUser = False
      self.estadoPass = False
      self.estadoConfirm = False
      self.estadoEmail = False



class UpdateScreen(Screen):
    
    estadoUser = False
    estadoPass = False
    estadoConfirm = False
    estadoEmail = False
    estadoId = False
    

    def validarId(self):
        id = int(self.ids.user_id.text)
        print(id)
        ids = register.ids()
        print(ids)
        if (id,) in ids :
            print("IdFound")
            return True
        else:
            return False
        
        

    def mostrarListado(self):
        personas = register.listado()
        word=""
        for p in personas:
            word = f'´{word}\{p}'
        self.ids.per_label.text = f'{word}'
        print(word)
    
    def valido(self):
       print(self.estadoUser)
       print(self.estadoPass)
       print(self.estadoConfirm)
       print(self.estadoEmail)

       if self.estadoUser and self.estadoConfirm and self.estadoPass and self.estadoEmail and self.estadoId:
           return True
       else:
           return False

    def updatePersona(self):
        id = self.ids.user_id.text
        user = self.ids.user.text
        password = self.ids.password.text
        email = self.ids.email.text
        register.actualizar_persona(id,user,email,password)
        self.estadoUser = False
        self.estadoPass = False
        self.estadoConfirm = False
        self.estadoEmail = False
        self.estadoId = False
        


class DeleteScreen(Screen):
   
    def mostrarListado(self):

        personas = register.listado()
        word=""
        for p in personas:
            word = f'´{word}\{p}'
        self.ids.per_label.text = f'{word}'
        print(word)

    def eliminarPersona(self):
       id = self.ids.user_id.text
       register.borrar_persona(id)


class HomeScreen(Screen):
    pass

class ScreenManager(ScreenManager):
    pass

    
kv = Builder.load_file("my.kv")

class MyApp(App):
    def build(self):
        register.crear_tabla()
        return kv

if __name__ == "__main__":
    MyApp().run()