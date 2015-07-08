#!/usr/bin/python

### System Path Modifications for importing modules
import sys
print (sys.version)
print sys.path
sys.path.append('/home/ren/Desktop/gspreadtest/oauth2clientmaster/oauth2client')   ### This is for oauth2 interaction
sys.path.append('/home/ren/Desktop/gspreadtest/gspreadmaster')  ### This is for google spreadsheet interaction
sys.path.append('/home/ren/Desktop/gspreadtest/client-python-master')   ### This is for blockchain interaction
print sys.path

### Importing modules for Google SpreadSheets
import json
import gspread
from client import SignedJwtAssertionCredentials

### Importing modules for Blockchain Interaction, Referance: https://github.com/blockchain/api-v1-client-python
from blockchain import blockexplorer
from blockchain import statistics


### Gaining access to 1 google spreadsheet, in this case name = "BTC"
json_key = json.load(open('gspreadtest-2f9b2a153d04.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
gc = gspread.authorize(credentials)

btc = gc.open("BTC").sheet1


### Pulling data from Bitcoin Blockchain
address = blockexplorer.get_address('16RyYkFi7fkqFD9KP6NdYcSsZj77EHABaf')

### Putting data onto Google Spreadhseets
### btc.update_acell('A2', address.final_balance )
print address.total_received

for x in address.transactions:
	pos = address.transactions.index(x)
	btc.update_acell('A' + str(pos + 1), address.transactions[pos].outputs[0].value)
	print x.outputs[0].value



