filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

newfilenames = [name.replace(".c", ".h").replace(".hpp", ".h") for name in filenames]

print(newfilenames)
