import whois
from domain_validator import is_registered

domain_name = input("Enter domain name: ")
if is_registered(domain_name):
    whois_info = whois.whois(domain_name)
    print("Domain registrar: ", whois_info.registrar)
    print("WHOIS Server: ", whois_info.whois_server)
    print("Domain creation date: ", whois_info.creation_date)
    print("Domain expiration date: ", whois_info.expiration_date)
    print("Name servers: ", whois_info.name_servers)
    print("DNSSSEC: ", whois_info.dnssec)
    print("Emails: ", whois_info.emails)
    print("Country: ", whois_info.country)
    print("Address: ", whois_info.address)
    print("Organization: ", whois_info.org)

