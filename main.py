import flet as ft
from Irakaslea import Irakaslea
from IrakasleaController import IrakasleaController 

def main(page: ft.Page):
    controller = IrakasleaController()
    controller.kargatu()  # Irakasleak kargatu

    hautatua = None

    mezua = ft.Text()
    ordutegia_output = ft.Text()
    libre_komun_text = ft.Text()
    izena_input = ft.TextField(label="Irakaslearen izena eta abizena", width=200)
    ordua_input = ft.TextField(label="Ordua (HH:MM)", width=150)
    hautatu_dropdown = ft.Dropdown(
        label="Hautatu irakaslea",
        options=[ft.dropdown.Option(i.izen_abizena) for i in controller.irakasleak]
    )

    def eguneratu_ordutegia(): # Ordutegia eguneratzeko funtzioa
        if hautatua:
            ordutegia_output.value = f"{hautatua.izen_abizena} ordutegia: {', '.join(hautatua.ordutegia)}"
        else:
            ordutegia_output.value = "Ez da irakaslerik hautatu."
        page.update()

    def hautatu_irakaslea(e): # Irakaslea hautatzeko funtzioa
        nonlocal hautatua
        hautatua = next((i for i in controller.irakasleak if i.izen_abizena == hautatu_dropdown.value), None)
        eguneratu_ordutegia()

    def irakasle_gehitu(e): # Irakaslea gehitzeko funtzioa
        izena = izena_input.value.strip()
        if not izena:
            mezua.value = "Izena eta Abizena hutsik dago."
        elif any(i.izen_abizena == izena for i in controller.irakasleak):
            mezua.value = f"{izena} dagoeneko badago."
        else:
            if controller.irakasle_gehitu(izena):
                hautatu_dropdown.options.append(ft.dropdown.Option(izena))
                hautatu_dropdown.value = izena
                hautatua = next(i for i in controller.irakasleak if i.izen_abizena == izena)
                mezua.value = f"{izena} gehituta."
                controller.gorde()
            else:
                mezua.value = "Errorea irakaslea gehitzean."
        eguneratu_ordutegia()
        page.update()

    def irakasle_kendu(e):  # Irakaslea kentzeko funtzioa
        izena = izena_input.value.strip()
        if not izena:
            mezua.value = "Izena eta Abizena hutsik dago."
        else:
            if controller.irakasle_kendu(izena):
                mezua.value = f"{izena} kenduta."
                # Kendu dropdown-etik
                hautatu_dropdown.options = [opt for opt in hautatu_dropdown.options if opt.key != izena]
                hautatu_dropdown.value = None
                hautatua = None
                ordutegia_output.value = ""
                libre_komun_text.value = ""
                controller.gorde()
            else:
                mezua.value = f"{izena} ez da aurkitu."
        page.update()

    def gehitu_click(e): # Ordua gehitzeko funtzioa
        if not hautatua:
            mezua.value = "Lehenik hautatu irakasle bat."
            page.update()
            return
        ordua = ordua_input.value.strip()
        if hautatua.gehitu_ordua(ordua):
            mezua.value = f"{ordua} gehituta."
            controller.gorde()
        else:
            mezua.value = f"{ordua} ordutegian dago."
        eguneratu_ordutegia()
        page.update()

    def kendu_click(e): # Ordua kentzeko funtzioa
        if not hautatua:
            mezua.value = "Lehenik hautatu irakasle bat."
            page.update()
            return
        ordua = ordua_input.value.strip()
        if hautatua.kendu_ordua(ordua):
            mezua.value = f"{ordua} kenduta."
            controller.gorde()
        else:
            mezua.value = f"{ordua} ez dago ordutegian."
        eguneratu_ordutegia()
        page.update()

    def ordu_libre_komun():
        ordu_guztiak = [
            "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00"
        ]
        libre_komun = []
        for ordua in ordu_guztiak:
            if all(ordua not in irakasle.ordutegia for irakasle in controller.irakasleak):
                libre_komun.append(ordua)
        return libre_komun

    def erakutsi_libre_komun(e):
        orduak = ordu_libre_komun()
        if orduak:
            libre_komun_text.value = "Ordu libre komunak: " + ", ".join(orduak)
        else:
            libre_komun_text.value = "Ez dago ordu libre komunik."
        page.update()

    hautatu_dropdown.on_change = hautatu_irakaslea

    page.add(
        ft.Column([
            ft.Row([
                izena_input, ft.ElevatedButton("Irakaslea gehitu", on_click=irakasle_gehitu),]),
            hautatu_dropdown,
            ordutegia_output,
            ft.Row([
                ordua_input,
                ft.ElevatedButton("Ordua gehitu", on_click=gehitu_click),
                ft.ElevatedButton("Ordua kendu", on_click=kendu_click)
            ]),
            mezua,
            ft.ElevatedButton("Ordu libre komunak erakutsi", on_click=erakutsi_libre_komun),
            libre_komun_text,
        ])
    )

ft.app(target=main)
