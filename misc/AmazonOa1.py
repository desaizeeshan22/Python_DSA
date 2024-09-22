def order(input_list):
    prime,prime_numeric, non_prime = [], [],[]
    for l in input_list:
        key = ""
        j = 0
        while l[j] != " ":
            key += l[j]
            j += 1

        is_prime = False
        temp = l[j:]
        for metadata in temp:
            if metadata != " " and not metadata.isnumeric():
                is_prime = True
                break
        if is_prime:
            if not key.isnumeric():
                prime.append((l, key))
            else:
                prime_numeric.append((l,key))
        else:
            non_prime.append(l)
    prime.sort(key=lambda x: x[1])
    for elem in prime_numeric:
        print(elem[0])
    for elem in prime:
        print(elem[0])
    for elem in non_prime:
        print(elem)


order(["zld 93 12", "fp kindle book", "10a echo book", "17g 12 25 6", "ab1 kindle book",
       "125 echo dot second generation"])
