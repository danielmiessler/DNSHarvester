DNSHarvester
============

This tool will harvest valid DNS subdomains from a given domain. It uses two techniques to do this:

1. Google queries through the custom search engine API
2. Dictionary search using a provided wordlist

Results are put into an array and then checked for validity using socket.gethostaddr. Names that don't resolve are removed from the array.
