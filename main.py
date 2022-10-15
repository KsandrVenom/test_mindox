def groups_from_scratch(n_customer):
    groups = {}

    for customer in range(n_customer):
        str_customer = str(customer)
        numbers = list(str_customer)
        sum = 0

        for number in numbers:
            sum += int(number)

        if sum in groups:
            groups[sum] += 1
        else:
            groups[sum] = 1

    return(groups)


def groups_from_id(n_customer, n_first_id):
    groups = {}

    for customer in range(n_first_id, n_customer):
        sum = 0
        while customer > 0:
            sum += customer % 10
            customer = customer // 10

        if sum in groups:
            groups[sum] += 1
        else:
            groups[sum] = 1

    return(groups)






#print(groups_from_scratch(100))
#print(groups_from_id(100, 50))