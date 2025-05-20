import flet as ft
from Irakaslea import Irakaslea
from IrakasleaController import IrakasleaController 

def main(page: ft.Page):
    page.title = "Irakasleen Ordutegia"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30
    page.scroll = "auto"

    controller = IrakasleaController()
    controller.kargatu()

    hautatua = None

    mezua = ft.Text()
    ordutegia_output = ft.Text()
    libre_komun_text = ft.Text()
    izena_input = ft.TextField(label="Irakaslearen izena eta abizena", width=300)
    ordua_input = ft.TextField(label="Ordua (HH:MM)", width=200)
    hautatu_dropdown = ft.Dropdown(
        label="Hautatu irakaslea",
        options=[ft.dropdown.Option(i.izen_abizena) for i in controller.irakasleak],
        width=300
    )

    irakasle_checkboxak = []

    def sortu_checkboxak():
        irakasle_checkboxak.clear()
        checkbox_column.controls.clear()
        for irakasle in controller.irakasleak:
            cb = ft.Checkbox(label=irakasle.izen_abizena)
            irakasle_checkboxak.append(cb)
            checkbox_column.controls.append(cb)
        page.update()

    def eguneratu_ordutegia():
        if hautatua:
            ordutegia_output.value = f"{hautatua.izen_abizena} ordutegia: {', '.join(hautatua.ordutegia)}"
        else:
            ordutegia_output.value = "Ez da irakaslerik hautatu."
        page.update()

    def hautatu_irakaslea(e):
        nonlocal hautatua
        hautatua = next((i for i in controller.irakasleak if i.izen_abizena == hautatu_dropdown.value), None)
        eguneratu_ordutegia()

    def irakasle_gehitu(e):
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
                sortu_checkboxak()
            else:
                mezua.value = "Errorea irakaslea gehitzean."
        eguneratu_ordutegia()
        page.update()

    def irakasle_kendu(e):
        izena = izena_input.value.strip()
        if not izena:
            mezua.value = "Izena eta Abizena hutsik dago."
        else:
            if controller.irakasle_kendu(izena):
                mezua.value = f"{izena} kenduta."
                hautatu_dropdown.options = [opt for opt in hautatu_dropdown.options if opt.key != izena]
                hautatu_dropdown.value = None
                hautatua = None
                ordutegia_output.value = ""
                libre_komun_text.value = ""
                controller.gorde()
                sortu_checkboxak()
            else:
                mezua.value = f"{izena} ez da aurkitu."
        page.update()

    def gehitu_click(e):
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

    def kendu_click(e):
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

    def erakutsi_libre_komun(e):
        hautatutako_irakasleak = [
            i for i in controller.irakasleak
            if any(cb.label == i.izen_abizena and cb.value for cb in irakasle_checkboxak)
        ]
        if not hautatutako_irakasleak:
            libre_komun_text.value = "Ez da irakaslerik hautatu."
        else:
            ordu_guztiak = [
                "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00"
            ]
            libre_komun = []
            for ordua in ordu_guztiak:
                if all(ordua not in i.ordutegia for i in hautatutako_irakasleak):
                    libre_komun.append(ordua)
            if libre_komun:
                libre_komun_text.value = "Ordu libre komunak: " + ", ".join(libre_komun)
            else:
                libre_komun_text.value = "Ez dago ordu libre komunik."
        page.update()

    def garbitu_hautapena():
        for cb in irakasle_checkboxak:
            cb.value = False
        libre_komun_text.value = ""
        page.update()

    hautatu_dropdown.on_change = hautatu_irakaslea

    checkbox_column = ft.Column(spacing=5)
    sortu_checkboxak()

    page.add(
        ft.Column([
            ft.Text("Irakasleen Ordutegia", size=30, weight=ft.FontWeight.BOLD),
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        izena_input,
                        ft.ElevatedButton("Gehitu", icon=ft.Icons.PERSON_ADD, on_click=irakasle_gehitu),
                        ft.ElevatedButton("Kendu", icon=ft.Icons.PERSON_REMOVE, on_click=irakasle_kendu),
                    ], spacing=10),
                    hautatu_dropdown,
                    ordutegia_output,
                    ft.Row([
                        ordua_input,
                        ft.ElevatedButton("Ordua gehitu", icon=ft.Icons.ADD, on_click=gehitu_click),
                        ft.ElevatedButton("Ordua kendu", icon=ft.Icons.REMOVE, on_click=kendu_click)
                    ], spacing=10),
                    mezua
                ]),
                padding=20,
                border_radius=10,
                bgcolor=ft.Colors.BLUE_50
            ),
            ft.Divider(),
            ft.Text("Hautatu irakasleak (ordu libre komunak kalkulatzeko):", weight=ft.FontWeight.BOLD),
            ft.Container(checkbox_column, padding=10, bgcolor=ft.Colors.GREY_100, border_radius=5),
            ft.Row([
                ft.ElevatedButton("Erakutsi ordu libre komunak", icon=ft.Icons.SEARCH, on_click=erakutsi_libre_komun),
                ft.ElevatedButton("Garbitu hautapena", icon=ft.Icons.CLEAR_ALL, on_click=lambda e: garbitu_hautapena())
            ]),
            libre_komun_text
        ], spacing=25)
    )

ft.app(target=main)
