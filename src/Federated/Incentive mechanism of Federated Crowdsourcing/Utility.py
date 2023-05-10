import numpy as np
import sympy
import random
import matplotlib.pyplot as plt


# random.seed(1)
np.random.seed(2)
alpha = 250
T_min = 1
T_max = 10

def r_min(gamma_list):  # r最小值
    return max(gamma_list)

def r_max(gamma_list):  # r MAX
    return 3*max(gamma_list)

def r_random(gamma_list):  # r Random
    return max(gamma_list)+random.random()*max(gamma_list)*1.4

def T_valid(T_list):  # 指示器函数
    T_list_valid = []
    for i in range(len(T_list)):
        if T_list[i] >= T_min and T_list[i] <= T_max:
            T_list_valid.append(1)
        else:
            T_list_valid.append(0)
    print('T_list--T_list_valid')
    print(T_list)
    print(T_list_valid)
    return T_list_valid

def r_cal(gamma_list, T_list):
    r_cal_list = []
    T_list_valid = T_valid(T_list)
    for i in range(len(gamma_list)):
        r_cal_list.append(gamma_list[i]*T_list_valid[i])
    return (1.0/sum(T_list_valid))*sympy.sqrt(alpha*sum(r_cal_list))

def a_cal(gamma, r):
    return (1-gamma/r)

def utility(gamma_list, T_list, num):
    a_list = []
    a_list_valid = []
    T_list_valid_list = []
    T_list_valid = T_valid(T_list)
    m = sum(T_list_valid)
    r = r_cal(gamma_list, T_list)
    for i in range(num):
        a_list.append(a_cal(gamma_list[i], r))
        T_list_valid_list.append(T_list_valid[i]*T_list[i])

    for i in range(num):
            a_list_valid.append(a_list[i]*T_list_valid[i])

    sum_cost = 0
    for i in range(num):
        sum_cost += r * a_list_valid[i]

    client_utility_list = []
    for i in range(num):
        client_utility_list.append((r * a_list[i] + gamma_list[i] * sympy.log(1 - a_list[i])) * T_list_valid[i])

    return (1/m) * (alpha * sum(a_list_valid)) - min(max(T_list_valid_list), T_max) -sum_cost, client_utility_list, m


def utility_max(gamma_list, T_list, num):
    a_list = []
    a_list_valid = []
    T_list_valid_list = []
    T_list_valid = T_valid(T_list)
    m = sum(T_list_valid)
    r = r_max(gamma_list)
    for i in range(num):
        a_list.append(a_cal(gamma_list[i], r))
        T_list_valid_list.append(T_list_valid[i] * T_list[i])

    for i in range(num):
        a_list_valid.append(a_list[i] * T_list_valid[i])

    sum_cost = 0
    for i in range(num):
        sum_cost += r * a_list_valid[i]

    client_utility_list = []
    for i in range(num):
        client_utility_list.append((r * a_list[i] + gamma_list[i] * sympy.log(1 - a_list[i])) * T_list_valid[i])

    return (1 / m) * (alpha * sum(a_list_valid)) - min(max(T_list_valid_list), T_max) - sum_cost, client_utility_list, m


def utility_random(gamma_list, T_list, num):
    a_list = []
    a_list_valid = []
    T_list_valid_list = []
    T_list_valid = T_valid(T_list)
    m = sum(T_list_valid)
    r = r_random(gamma_list)
    for i in range(num):
        a_list.append(a_cal(gamma_list[i], r))
        T_list_valid_list.append(T_list_valid[i] * T_list[i])

    for i in range(num):
        a_list_valid.append(a_list[i] * T_list_valid[i])

    sum_cost = 0
    for i in range(num):
        sum_cost += r * a_list_valid[i]

    client_utility_list = []
    for i in range(num):
        client_utility_list.append((r * a_list[i] + gamma_list[i] * sympy.log(1 - a_list[i])) * T_list_valid[i])

    return (1 / m) * (alpha * sum(a_list_valid)) - min(max(T_list_valid_list), T_max) - sum_cost, client_utility_list, m


num = 10
T_list = np.random.randint(0, 12, num)
gamma_list_list = []
for j in range(6):
    gamma_list_list.append([np.random.uniform(j+3, j+4) for i in range(num)])

##### iFedCrowd
Utility_list_gamma = []
client_utility_list_list = []
r_list = []
m_list = []
for j in range(6):
    res = utility(gamma_list_list[j], T_list, num)
    Utility_list_gamma.append(res[0])
    client_utility_list_list.append(res[1])
    m_list.append(res[2])
    r_list.append(r_cal(gamma_list_list[j], T_list))

client_utility_avg_gamma = []

for i in range(len(client_utility_list_list)):
    client_utility_avg_gamma.append(sum(client_utility_list_list[i]) / m_list[i])

# print('client_utility_avg_gamma')
# print(client_utility_avg_gamma)
# print('T_list')
# print(T_list)
# print('m_list')
# print(m_list)
# print('gamma_list_list')
# print(gamma_list_list)
# print('r_list')
# print(r_list)
# print('Utility_list_gamma')
# print(Utility_list_gamma)
# print('client_utility_list_list')
# print(client_utility_list_list)
# ##### max
Utility_max_list_gamma = []
client_utility_list_list = []
r_max_list = []
m_list = []
for j in range(6):
    res = utility_max(gamma_list_list[j], T_list, num)
    Utility_max_list_gamma.append(res[0])
    client_utility_list_list.append(res[1])
    m_list.append(res[2])
    r_max_list.append(r_max(gamma_list_list[j]))

client_utility_avg_gamma = []

for i in range(len(client_utility_list_list)):
    client_utility_avg_gamma.append(sum(client_utility_list_list[i]) / m_list[i])
#
#
# ##### random
Utility_random_list_gamma = []
client_random_utility_list_list = []
r_random_list = []
m_list = []
for j in range(6):
    res = utility_random(gamma_list_list[j], T_list, num)
    Utility_random_list_gamma.append(res[0])
    client_utility_list_list.append(res[1])
    m_list.append(res[2])
    r_random_list.append(r_random(gamma_list_list[j]))

client_utility_random_avg_gamma = []

# for i in range(len(client_utility_list_list)):
#     client_utility_random_avg_gamma.append(sum(client_utility_list_list[i]) / m_list[i])

plt.rcParams['font.sans-serif'] = ['STSong']  # 设置中文
c = ['1', '2', '3', '4', '5', '6']

bar_width = 0.2
x_7 = list(range(len(c)))
x_8 = [i+bar_width for i in x_7]
x_9 = [i+bar_width*2 for i in x_7]

plt.figure(figsize=(4, 4), dpi=150)
plt.bar(range(len(c)), Utility_list_gamma, width=bar_width, label='My')
plt.bar(x_8, Utility_max_list_gamma, width=bar_width, label='Max')
plt.bar(x_9, Utility_random_list_gamma, width=bar_width, label='Random')
plt.legend(loc='upper right')
plt.xlabel('F', fontsize=16)
plt.ylabel('Utility of publisher',  fontsize=16)
plt.xticks(x_8, c)

plt.show()


