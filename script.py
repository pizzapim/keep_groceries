import pwd
import os
import gkeepapi
from gkeepapi.exception import LoginException
from random import choice
from sys import exit

file_name = os.path.join(os.path.dirname(__file__), 'environ')

vars = {}
with open(file_name) as f:
    for line in f:
        key, value = line.split('=')
        vars[key.strip()] = value.strip()

google_username = vars['GOOGLEUSERNAME']
google_password = vars['GOOGLEPASSWORD']
note_id = vars['NOTEID']

veggie = choice(['broccoli', 'worteltjes', 'snijbonen', 'sperziebonen', 'bloemkool'])
potato = choice(['aardappelen (als het op is)', 'krieltjes', 'patatjes (als het op is)', 'aardappelschijfjes', 'rosti (als het op is)', 'rijst (als het op is)'])
meat = choice(['vegetarische hamburger', 'kip', 'tofu', 'witvis'])

local_username = pwd.getpwuid(os.getuid()).pw_name
keep = gkeepapi.Keep()
list_end = gkeepapi.node.NewListItemPlacementValue.Bottom

if not google_username or not google_password or not note_id:
    print('One or more environmental variables were not set!')
    exit(1)

keep.login(google_username, google_password)

note = keep.get(note_id)
note.add(veggie, False, list_end)
note.add(potato, False, list_end)
note.add(meat, False, list_end)

keep.sync()
