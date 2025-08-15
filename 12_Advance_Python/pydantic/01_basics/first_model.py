from pydantic import BaseModel

# BaseModel is the main class for creating Pydantic models.
# Type Annotations are used to define the data types of the model attributes.
# Model init (Always unpack the dictionary)
# Automatic Validation

class User(BaseModel):
    id: int
    name: str
    isActive: bool

input_data = {'id': 101, 'name': 'John Doe', 'isActive': True}
# input_data = {'id': '101', 'name': 'John Doe', 'isActive': True} # here pydantic try to automatically convert id value str to int, if it fail to convert automatically it gives an error
# user = User(input_data) # the input_data dictionary is passed as a single argument so it gives an error so we have to unpack the dictionary
user = User(**input_data) # (**input_data) unpacks the dictionary
print(user)