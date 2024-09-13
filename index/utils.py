from enum import IntEnum

class CustomerTypes(IntEnum):
  ADMIN = 1
  USER = 2

  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]