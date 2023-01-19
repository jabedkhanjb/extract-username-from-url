# Regular Expression Library
import re 

url = input("URL: ").strip() # strip is used for ignore white space from input

if match:= re.search(r"^(?:https?://)?(?:www\.)?(?:[a-z0-9]+)\.(?:com|net|org|edu|bd|it|to)/(?:@)?([a-z0-9._]+)", url, re.IGNORECASE):
    print(f"Username: {match.group(1)}")
else:
    print("Invalid URL")
    

# r"" is raw string, it consider .+\ these signs as a regular expression
    # ?: is used to unidentify the parethesis, so that it could match the exact group with index number. 
# note has given in readme.md file on this repository. 
