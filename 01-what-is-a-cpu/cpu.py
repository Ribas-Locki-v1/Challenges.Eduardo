# Create a list of all the components, registers and buses of a CPU
# Print the list, one per line
# Print a counter for the calculated total list elements

cpulist = ["CPU","ALU", "PC", "MAR", "MDR", "AC", "IR", "DATA BUS", "ADDRESS BUS", "CONTROL BUS"]

for components in cpulist:
    print(components) 

print("Total number of components, registers and buses in a CPU: ", len(cpulist))

#Hello world