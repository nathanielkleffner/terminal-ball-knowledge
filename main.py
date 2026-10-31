from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button, Footer, Header, Input, Static


class StarterApp(App):
	"""A minimal starting point for a Textual TUI."""

	TITLE = "My Textual App"
	CSS = """
	Screen {
		align: center middle;
	}

	#main {
		width: 60;
		height: auto;
		padding: 1 2;
		border: round $accent;
	}

	#result {
		margin-top: 1;
	}
	"""

	BINDINGS = [("q", "quit", "Quit")]

	def compose(self) -> ComposeResult:
		yield Header()
		with Static(id="main"):
			yield Static("Welcome! Enter your name to get started.")
			yield Input(placeholder="Your name", id="name")
			yield Button("Say hello", variant="primary", id="greet")
			yield Static("", id="result")
		yield Footer()

	def on_mount(self) -> None:
		self.query_one("#name", Input).focus()

	@on(Button.Pressed, "#greet")
	def greet(self) -> None:
		name = self.query_one("#name", Input).value.strip() or "there"
		self.query_one("#result", Static).update(f"Hello, {name}!")

	@on(Input.Submitted, "#name")
	def greet_on_enter(self) -> None:
		self.greet()


if __name__ == "__main__":
	app = StarterApp()
	app.run()
