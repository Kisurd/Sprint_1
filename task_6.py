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
tickets_by_type ={}

def delete_double():
    seen = []
    for k,v in tickets.items():
        ticket_list = []
        for i in v:
            if i not in seen:
                ticket_list.append(i)
                seen.append(i)
        tickets[k] = ticket_list

def link_ticket_to_type(types, tickets):
    for k,v in tickets.items():
        tickets_by_type[types[k]] = tickets[k]