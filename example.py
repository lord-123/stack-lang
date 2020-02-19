from stacklang import StackLang, Command

if __name__ == "__main__":
	lang = StackLang()

	lang.addCommand(Command("I", lambda x: input(), 0))
	lang.addCommand(Command("+", lambda s: s[0]+s[1], 2))
	lang.addCommand(Command("T", lambda x: 10, 0))

	lang.eval("II+", debug=True)

