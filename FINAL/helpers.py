def get_registry_entry(roll_number, register_filename):
	"""
	Returns: str name, int frequency from register_filename. It requires roll_number integer.
	"""
	with open(register_filename, "r") as f:
		register = f.read()

	register_list = register.split("\n")[1:] #list slicing removes header
	register_list_list = [e.split(",") for e in register_list]
	register_entry_dict = {int(e[0]):(e[1],e[2]) for e in register_list_list}

	name, frequency = register_entry_dict[roll_number]

	return name, int(frequency)

def update_registry_entry(roll_number, name, frequency, register_filename):
	"""
	Updates entry corresponding to the roll_number in register_filename
	"""
	with open(register_filename, "r") as f:
		register = f.read()

	register_header = register.split("\n")[:1]
	register_list = register.split("\n")[1:]
	register_list_list = [e.split(",") for e in register_list]
	register_entry_dict = {e[0]:(e[1],e[2]) for e in register_list_list}

	#update register_entry_dict
	register_entry_dict[str(roll_number)] = (name, str(frequency))
	register_list_updated = [",".join([x, register_entry_dict[x][0], register_entry_dict[x][1]]) for x in register_entry_dict]
	register_updated = "\n".join(register_header+register_list_updated)
	
	with open(register_filename, "w") as f:
		f.write(register_updated)
