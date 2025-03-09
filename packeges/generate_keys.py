import pickle 
from pathlib import Path 

import streamlit_authenticator as stauth

name = ["Ganesh Borkar", "Mangesh Hagare"]
usernames = ["ganeshb", "mangeshh"]
#passwords = ["gan123","man123"]
passwords = ["xxx","xxx"]

hashed_password = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent/ "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_password, file)
    
    

