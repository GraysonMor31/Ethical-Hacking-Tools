import requests

def subdomain_scanner(domain, timeout=3):
    # Read subdomains from file
    with open("./TXT_FILES/subdomains.txt") as file:
        list_of_subdomains = file.read().splitlines()
    discovered_subdomains = []
    for subdomain in list_of_subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            requests.get(url, timeout=timeout)
        except requests.ConnectionError:
            pass
        else:
            print("[+] Discovered subdomain: ", url)
            discovered_subdomains.append(url)
            
    # Save discovered subdomains to file, if doesn't exist create it
    with open(f"./TXT_FILES/{domain}_subdomains.txt", "w") as file:
        for subdomain in discovered_subdomains:
            file.write(subdomain + "\n")
            
if __name__ == "__main__":
    domain = input("Enter domain name: ")
    subdomain_scanner(domain)
            