#!/usr/bin/awk -f

{
  split($0, IPv4_PARTS, ".")
  split($0, IPv6_PARTS, ":")

  IPv6_flag = false
  IPv4_flag = false

  # IPv6 validation
  print $0
  print length(IPv6_PARTS)
  print length(IPv4_PARTS)

  if (length(IPv6_PARTS) > 1) {
    IPv6_flag = true

    print "IPv6 might be"
  }

  # IPv4 or IPv6 dual validation 
  if (length(IPv4_PARTS) == 4) {
    if (IPv6_flag == true) {
      print "IPv6 dual might be"
    } else {
      print "IPv4 might be"
    }

#    for (i in IPv4_PARTS) {
#      octet = IPv4_PARTS[i]

#      if (octet >=0 && octet < 256) {
#        print $0
#      }
#    }
  }
}