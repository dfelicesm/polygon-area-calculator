class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    string_id = "Rectangle(width={}, height={})".format(self.width, self.height)
    return string_id

  def set_width(self, width):
    self.width = width
  
  def set_height(self, height):
    self.height = height

  def get_area(self):
    area = self.height * self.width
    return area
  
  def get_perimeter(self):
    perimeter = 2*self.width + 2*self.height
    return perimeter

  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.height**2)**0.5
    return diagonal

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      message = "Too big for picture."
      return message
    else:
      picture = ""
      for i in range(self.height):
        line = "*" * self.width
        picture += line + "\n"
      return picture

  def get_amount_inside(self, shape):
    contained_area = shape.get_area()
    container_area = self.get_area()

    return container_area // contained_area
    

    








class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    string_id = "Square(side={})".format(self.width)

    return string_id

  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, side):
    self.width = side
    self.height = side

  def set_height(self, side):
    self.width = side
    self.height = side