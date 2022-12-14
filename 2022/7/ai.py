with open("test_input", "r") as f:
    lines = f.read()

input_lines = lines.splitlines()


class File:
  def __init__(self, name, size):
    self.name = name
    self.size = size

  def __str__(self):
    return f"  " * (len(self.name) - self.name.count('\n')) + f"{self.name} (file, size={self.size})"

class Directory:
  def __init__(self, name):
    self.name = name
    self.contents = []

  def __str__(self):
    return f"{self.name} (dir)\n{''.join(str(item) for item in self.contents)}"

  def add(self, item):
    self.contents.append(item)

# Parse the input into a list of commands and their output
commands = []
command = None
output = []
for line in input_lines:
  if line.startswith('$'):
    if command:
      commands.append((command, output))
    command = line[1:].strip()
    output = []
  else:
    output.append(line.strip())

# Create the initial directory structure
directories = [Directory('/')]

# Iterate over the commands and their output to build the directory structure
for command, output in commands:
  # Split the command into its parts
  parts = command.split(' ')
  
  # Handle the "cd" command by updating the current directory
  if parts[0] == 'cd':
    if parts[1] == '/':
      # Go to the root directory
      directories = [directories[0]]
    else:
      # Go to the specified subdirectory, if it exists
      found = False
      for directory in directories[-1].contents:
        if directory.name == parts[1] and isinstance(directory, Directory):
          directories.append(directory)
          found = True
          break
      if not found:
        print(f"Error: directory {parts[1]} does not exist in {directories[-1].name}")
  
  # Handle the "ls" command by adding the contents of the current directory
  elif parts[0] == 'ls':
    for line in output:
      # Parse the line into a name and a size
      parts = line.split(' ')
      name = parts[1]
      size = int(parts[0]) if parts[0].isdigit() else 0
      
      # Add the item to the current directory
      if size > 0:
        item = File(name, size)
      else:
        item = Directory(name)
      directories[-1].add(item)

# Print the directory structure
print(directories[0])