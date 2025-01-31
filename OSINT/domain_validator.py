import whois

def is_registered(domain):
    """
    Use a boolean to check if a domain is registered or not
    
    Parameters: 
        domain (string)
        
    Returns: 
        boolean: true/false
        
    example:
        is_registered("google.com")
    """
    try:
        who = whois.whois(domain)
    except Exception:
        return False
    else:
        return bool(who.domain_name)
    
def main():
    domain = input("Enter a domain: ")
    print(is_registered(domain))
    
if __name__ == "__main__":
    main()