

for i in range (10, 100):
  for l in range(10, 100):
    result = l * i
    THdigit = int(result / 1000)
    HUdigit = int(result / 100) - (THdigit * 10)
    TNdigit = int(result / 10)  - ((THdigit * 100) + (HUdigit * 10))
    ONdigit = int(result)       - ((THdigit * 1000) + (HUdigit * 100) + (TNdigit * 10))

    result_palin = (ONdigit * 1000) + (TNdigit * 100) + (HUdigit * 10) + (THdigit)

    if(result == result_palin):
      print("palindrome: " ,result)
      print("NUmber1: {:d} & NUmber2: {:d}" .format(i, l))


