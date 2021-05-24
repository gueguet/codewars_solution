# https://www.codewars.com/kata/56af1a20509ce5b9b000001e/train/python

import re

def travel(r, zipcode):
  
  zip_str = "{}:".format(zipcode)
  street_and_town_str = ""
  number_str = ""

  address_list = r.split(",")

  for address in address_list:
    current_zipcode = re.search(r'\w{2} \d{5}',address).group(0)

    if (current_zipcode == zipcode):
      current_street_and_town = re.search('^(\d+)(.+?)\w{2} \d{5}', address).group(2)
      street_and_town_str += "{},".format(current_street_and_town[1:-1])

      current_number = re.search(r'^(\d+)',address).group(0)
      number_str += "{},".format(current_number)

  res = "{}{}/{}".format(zip_str,street_and_town_str[:-1],number_str[:-1])
  return res


ad = ("123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432,"
  "54 Holy Grail Street Niagara Town ZP 32908,3200 Main Rd. Bern AE 56210,1 Gordon St. Atlanta RE 13000,"
  "10 Pussy Cat Rd. Chicago EX 34342,10 Gordon St. Atlanta RE 13000,58 Gordon Road Atlanta RE 13000,"
  "22 Tokyo Av. Tedmondville SW 43098,674 Paris bd. Abbeville AA 45521,10 Surta Alley Goodtown GG 30654,"
  "45 Holy Grail Al. Niagara Town ZP 32908,320 Main Al. Bern AE 56210,14 Gordon Park Atlanta RE 13000,"
  "100 Pussy Cat Rd. Chicago EX 34342,2 Gordon St. Atlanta RE 13000,5 Gordon Road Atlanta RE 13000,"
  "2200 Tokyo Av. Tedmondville SW 43098,67 Paris St. Abbeville AA 45521,11 Surta Avenue Goodtown GG 30654,"
  "45 Holy Grail Al. Niagara Town ZP 32918,320 Main Al. Bern AE 56215,14 Gordon Park Atlanta RE 13200,"
  "100 Pussy Cat Rd. Chicago EX 34345,2 Gordon St. Atlanta RE 13222,5 Gordon Road Atlanta RE 13001,"
  "2200 Tokyo Av. Tedmondville SW 43198,67 Paris St. Abbeville AA 45522,11 Surta Avenue Goodville GG 30655,"
  "2222 Tokyo Av. Tedmondville SW 43198,670 Paris St. Abbeville AA 45522,114 Surta Avenue Goodville GG 30655,"
  "2 Holy Grail Street Niagara Town ZP 32908,3 Main Rd. Bern AE 56210,77 Gordon St. Atlanta RE 13000")


travel(ad, "OH 43071")