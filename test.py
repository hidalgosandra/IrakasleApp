import flet
from flet import Page, Text

def main(page: Page):
    page.title = "Mi app"
    page.add(Text("Hola Flet!"))

flet.app(target=main)
