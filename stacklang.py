class StackLang():
	def __init__(self):
		self.__stack = []
		self.__commands = {""}
		self.__commands.clear()

	def addCommand(self, command):
		self.__commands.add(command)

	def eval(self, program, debug=False):
		for i in program:
			command = [x for x in self.__commands if x.identifier == i][0]

			if debug: print(repr(command))

			args = [self.__stack.pop() for x in range(command.popAmount)]
			self.__stack.append(command.function(args))

			if debug: print("stack:\n" + str(self.__stack))

class Command():
	def __init__(self, identifier, function, pop = 1):
		self.__identifier = identifier
		self.__function = function
		self.__popAmount = pop

	@property
	def identifier(self):
		return self.__identifier

	@property
	def function(self):
		return self.__function

	@property
	def popAmount(self):
		return self.__popAmount

	def __repr__(self):
		return f"command: {self.__identifier}"