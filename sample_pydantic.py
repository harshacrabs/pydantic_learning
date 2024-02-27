

#pip install pydantic

# Import the necessary libraries
from pydantic import BaseModel

#define a class 

class User(BaseModel):
    name:str
    id: int

# create instances of the object

user = User(name='random',id=1)
print(user)

user_2 = User(name='radmon', id= 2)
print(user_2)

#Convert the pydantic model to Json using model_dump_json() method

user_json_str = user.model_dump_json()
print(user_json_str)


user_2_json_str = user_2.model_dump_json()
print(user_2_json_str)

#Convert the json string back into the pydantic model using .parse_raw() method

json_str = '{"name": "mad", "id":3}'
user_3 = User.parse_raw(json_str)