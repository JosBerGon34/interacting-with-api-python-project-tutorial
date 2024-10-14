import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
#ID#f7746b9e91554e798fea1845917d13a5
#PW#3806b002e6a44c26b58bcef052af59a4
# # load the .env file variables
load_dotenv()
import os
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
print(client_id,  ":", client_secret)
