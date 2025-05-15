import flet
from flet import Page, Text

def main(page: Page):
    page.title = "Iraskasle App"
    page.add(Text("Hola Flet!"))

flet.app(target=main)
