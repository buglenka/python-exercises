#!/usr/bin/awk -f

{
  for (i = 1; i < NF; i++)
  {

    # IPv4 validation
    if ($i ~ /^[[:digit:]]{1,3}(\.[[:digit:]]{1,3}){3}$/) 
    {
      split($i, ipv4_parts, ".")

      if (ipv4_parts[0] >= 0 && ipv4_parts[0] < 256 \
          && ipv4_parts[1] >= 0 && ipv4_parts[1] < 256 \
          && ipv4_parts[2] >= 0 && ipv4_parts[2] < 256 \
          && ipv4_parts[3] >= 0 && ipv4_parts[3] < 256)
        print $i
    }
    else 
    {
      # IPv6 validation
      if ($i ~ /^[[:xdigit:]]{0,4}(:[[:xdigit:]]{0,4}){3,7}$/) 
      {
          print $i
      } 
      else 
      {
        # IPv6 dual validation
        if ($i ~ /^[[:xdigit:]]{0,4}(:[[:xdigit:]]{0,4}){3,5}:[[:digit:]]{1,3}(\.[[:digit:]]{1,3}){3}$/) 
        {
            print $i
        }
      }
    }
  }
}