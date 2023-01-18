def calculate_volume(width, depth, height):
  return width * depth * height

if __name__ == "__main__":
  width = float(input("Enter the width of the box: "))
  depth = float(input("Enter the depth of the box: "))
  height = float(input("Enter the height of the box: "))
  volume = calculate_volume(width, depth, height)
  print(f"The volume of the box is: {volume}")