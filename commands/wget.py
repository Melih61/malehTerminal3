import os
import wget
import requests

def download(url, output):
    if os.path.exists(output):
        try:
            response = requests.head(url, allow_redirects=True, timeout=10)
            if response.status_code == 200:
                file = wget.download(url, out=output)
                print("\nDownload completed")
            else:
                print(f"wget: URL does not exist: {response.status_code}")
                return
        except requests.RequestException as e:
            print(f"wget: Error: {e}")
            return
    else:
        print(f"wget: No such file or directory: {output}")
        return

def run(args):
    if not args:
        print("wget: Invalid arguments")
        return
    try:
        if len(args) == 1:
            url = args[0]
            output = os.getcwd()
        elif len(args) == 2:
            url = args[0]
            output = args[1]
        else:
            print("wget: Invalid arguments")
            return
        download(url, output)
    except Exception as e:
        print(f"wget: Error: {e}")
        return