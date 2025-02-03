import dns.resolver

# Set target domain
target = input("Enter a domain name: ")
record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]

# Create a resolver object
resolver = dns.resolver.Resolver()

# Look up any records in the set list
for record in record_types:
    try:
        answers = resolver.resolve(target, record)
    except dns.resolver.NoAnswer:
        continue
    print(f"DNS Records for {target} ({record}):")
    for answer in answers:
        print(answer)