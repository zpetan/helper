import typer
import helper.cli.fix as fix

app = typer.Typer()

app.add_typer(fix.app, name="fix", help="Fix things, e.g. slow CPU due to Battery setting.")

if __name__ == "__main__":
    app()
    