CURL= "curl"
def get_curl(): 
	print("get_curl")
	url = input("URL: ? \n")
	res = f"curl {url}"
	headers = input("HEADER? split by |: \n")
	if headers.strip(): 
		headers = headers.split('|')
		for h in headers:
			res += f'  -H "{h}"'
	print(res)


def main():
	""" Main program """
  # Code goes over here.
	print("This script generate the curl command for you")
	action = input("Type of request: \n")
	if action.lower()  == "get":
		get_curl()

if __name__ == "__main__":
  main()

