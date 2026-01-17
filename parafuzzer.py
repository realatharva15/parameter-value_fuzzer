import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #this line will disable all the warnings that will appear while fuzzing

#getting the base url from the user along with the default response size

def para_fuzzer():
    base_url=input("Enter the target url path (eg. http://10.10.10.10/index.php ): ")
    if not base_url.startswith(('http://','https://')):
        base_url="http://"+base_url

#getting the defualt size of the error page:
    try:
        error_size=int(input("Input the default error page size: ")or "0")
    except:
        error_size=0


#load the parameter-value pair wordlist:

    try:
        with open("para_val.txt",'r') as f:
            pairs=[line.strip() for line in f if line.strip()]
    except:
        print(f"[-] Create the parameter-value pair file first! ")
        return
    print(f"Fuzzing on {base_url}")
    print(f"[*] Loaded {len(pairs)} parameters")
    print("[*] Press Ctrl+C to stop fuzzing")
    
#sending requests to the website in order to find the normal response size
    try:
        normal_resp=requests.get(base_url,verify=False,timeout=3)
        normal_size=len(normal_resp.content)
        print(f"The normal size of the webpage is {normal_size}")
    except:
        print("[-] Cannot connect to the target")
        return

#fetching the parameter-value pairs from the wordlist. make sure that the words get split into parameter and value while the separation factor is the "="
#word on the left of "=" to be stored in para while the word on the right of the "=" to be stored in val.

    for pair in pairs:
        try:
            if '=' not in pair:
                continue
            para,val=pair.split('=',1)
            if '?' in base_url:
                target_url=f"{base_url}&{para}={val}"
            else:
                target_url=f"{base_url}?{para}={val}" #exact format of parameter and values in the url

#send request to the url for the actual fuzzing and not just for finding out the normal page size

            response=requests.get(target_url,timeout=3,verify=False)
            response_size=len(response.content)

            if response_size!=normal_size and response_size != error_size:
                print(f"[+] Found a HIT!!! at {para}={val}")
                print(f"The response size is {response_size}")
            
        except KeyboardInterrupt:
            print("[-] Interrupted by the user")
            break
        except:
            continue
if __name__== "__main__":
    para_fuzzer()

