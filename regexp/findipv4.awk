#!/usr/local/bin/awk -f

{
  split($0, IPv4_PARTS, ".")

  # IPv4 validation 
  if (length(IPv4_PARTS) == 4) {
    validity = 1

    for (i in IPv4_PARTS) 
    {
      octet = IPv4_PARTS[i]

      validity = (validity && octet >= 0 && octet < 256)
    }
    
    if (validity)
      print $0
  }
}