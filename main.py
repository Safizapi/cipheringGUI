from cipher import encode, decode
import flet


def main(page: flet.page):
    page.title = "utf-8 ciphering by Safizapi"

    input_text = flet.TextField(label="Input", autofocus=True)
    output = flet.TextField(label="Output", read_only=True)

    def encode_clicked(e):
        output.value = flet.Text(encode(input_text.value)).value
        page.update()

    def decode_clicked(e):
        output.value = flet.Text(decode(input_text.value)).value
        page.update()

    def clear_clicked(e):
        input_text.value = ""
        page.update()

    buttons = [
        flet.ElevatedButton("Encode", on_click=encode_clicked),
        flet.ElevatedButton("Decode", on_click=decode_clicked),
        flet.ElevatedButton("Clear", on_click=clear_clicked)
    ]

    buttons = flet.Row(controls=buttons, alignment=flet.MainAxisAlignment.NONE)

    page.add(
        input_text,
        buttons,
        output
    )


if __name__ == "__main__":
    flet.app(target=main)
