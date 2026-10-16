types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def remove_duplicates(tickets, checked):
    new_tickets = []

    for ticket in tickets:
        if ticket not in checked:
            new_tickets.append(ticket)
            checked.append(ticket)

    return new_tickets

def tickets_by_type(types, tickets):
    new_tickets = {}
    checked = []

    for i in range(1, 6):
        new_tickets[types[i]] = remove_duplicates(tickets[i], checked)

    return new_tickets

print('tickets_by_type = ', tickets_by_type(types, tickets))
