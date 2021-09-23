from tkinter import Tk, Button
import routeros_api
import config


class MyApp:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("250x100")
        self.root.title("Кнопка")
        self.connection = routeros_api.RouterOsApiPool(
            config.connection["ip"],
            username=config.connection["login"],
            password=config.connection["password"],
            plaintext_login=True,
        )
        button = Button(
            self.root,
            width="30",
            height="5",
            text="Нажми",
            bg="#E34234",
            foreground="white",
            font="Arial 20",
            command=self.button_handler,
        ).pack(padx=8, pady=8)

    def button_handler(self):
        try:
            api = self.connection.get_api()
            res = api.get_resource("/log").call("info", {"message": "TEST FROM PYTHON"})
        except Exception as err:
            print(err)

        self.connection.disconnect()


app = MyApp()
app.root.mainloop()
