N = int(input())

def query(x):
    print(x, flush=True)
    response = input()
    if response == "Vacant":
        exit()
    return response

lb = 0
ub = N - 1

l_query = query(lb)
u_query = query(ub)

while True:
    m = (lb + ub) // 2
    m_query = query(m)
    if (m_query == l_query) == (m % 2 == lb % 2):
        lb = m
        l_query = m_query
    else:
        ub = m
