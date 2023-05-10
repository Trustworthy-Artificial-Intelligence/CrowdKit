# coding=utf-8
import numpy as np
import sympy
import random
import matplotlib.pyplot as plt


# random.seed(1)
np.random.seed(2)
alpha = 110
T_min = 0.1
T_max = 1.0

def r_min(gamma_list):  # r最小值
    return max(gamma_list)

def r_max(gamma_list):  # r MAX
    return (max(gamma_list)+6)

def r_random(gamma_list):  # r Random
    return (max(gamma_list)+random.random()*6)

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

    return (1/m) * (alpha * sum(a_list_valid)) - min(max(T_list_valid_list), T_max) - sum_cost+130, client_utility_list, m, r


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

    return (1/m) * (alpha * sum(a_list_valid)) - min(max(T_list_valid_list), T_max) - sum_cost+130, client_utility_list, m, r


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

    return (1/m) * (alpha * sum(a_list_valid)) - min(max(T_list_valid_list), T_max) - sum_cost+130, client_utility_list, m, r


num_list = [5, 10, 15, 20, 25, 30]
gamma_range = [3, 5]
# T_min = 2


##### iFedCrowd
Utility_list_iFed = []
r_list_iFed = []
client_utility_list_list_iFed = []
for j in range(6):
    worker_number = num_list[j]
    gamma_list = []
    T_list = []
    for i in range(worker_number):
        gamma_list.append(random.uniform(gamma_range[0], gamma_range[1]))
        T_list.append(0.2)
    res = utility(gamma_list, T_list, worker_number)
    Utility_list_iFed.append(res[0])
    client_utility_list_list_iFed.append(res[1])
    r_list_iFed.append(res[3])


client_utility_avg_iFed = []
for utility_list in client_utility_list_list_iFed:
    client_utility_avg_iFed.append(sum(utility_list)/len(utility_list))


##### MAX
Utility_list_MAX = []
r_list_MAX = []
client_utility_list_list_MAX = []
for j in range(6):
    worker_number = num_list[j]
    gamma_list = []
    delta_list = []
    T_list = []
    for i in range(worker_number):
        gamma_list.append(random.uniform(gamma_range[0], gamma_range[1]))
        T_list.append(0.2)
    res = utility_max(gamma_list, T_list, worker_number)
    Utility_list_MAX.append(res[0])
    client_utility_list_list_MAX.append(res[1])
    r_list_MAX.append(res[3])

client_utility_avg_MAX = []
for utility_list in client_utility_list_list_MAX:
    client_utility_avg_MAX.append(sum(utility_list)/len(utility_list))


##### Random
Utility_list_random = []
r_list_random = []
client_utility_list_list_random = []
for j in range(6):
    worker_number = num_list[j]
    gamma_list = []
    delta_list = []
    T_list = []
    for i in range(worker_number):
        gamma_list.append(random.uniform(gamma_range[0], gamma_range[1]))
        T_list.append(0.2)
    res = utility_random(gamma_list, T_list, worker_number)
    Utility_list_random.append(res[0])
    client_utility_list_list_random.append(res[1])
    r_list_random.append(res[3])

client_utility_avg_random = []
for utility_list in client_utility_list_list_random:
    client_utility_avg_random.append(sum(utility_list)/len(utility_list))

# plt.plot(x, y, linewidth='3.0', linestyle=':', color='r', marker='o', markerfacecolor='r', markersize='10')

plt.plot(num_list, r_list_iFed, color='r', marker='*', markerfacecolor='r', markersize='10', label='My')
plt.plot(num_list, r_list_MAX, color='b', marker='.', markerfacecolor='b', markersize='10', label='Max')
plt.plot(num_list, r_list_random, color='g', marker='s', markerfacecolor='g', markersize='10', label='Random')
plt.legend(loc='best')
plt.xlabel('Number of workers', fontsize=16)
plt.ylabel('Reward rate(r)', fontsize=16)
plt.show()

plt.plot(num_list, client_utility_avg_iFed, color='r', marker='*', markerfacecolor='r', markersize='10', label='My')
plt.plot(num_list, client_utility_avg_MAX, color='b', marker='.', markerfacecolor='b', markersize='10', label='Max')
plt.plot(num_list, client_utility_avg_random, color='g', marker='s', markerfacecolor='g', markersize='10', label='Random')
plt.legend(loc='best')
plt.xlabel('Number of workers', fontsize=16)
plt.ylabel('Average utility of workers', fontsize=16)
plt.show()

plt.plot(num_list, Utility_list_iFed, color='r', marker='*', markerfacecolor='r', markersize='10', label='My')
plt.plot(num_list, Utility_list_MAX, color='b', marker='.', markerfacecolor='b', markersize='10', label='Max')
plt.plot(num_list, Utility_list_random, color='g', marker='s', markerfacecolor='g', markersize='10', label='Random')
plt.legend(loc='best')
plt.xlabel('Number of workers', fontsize=16)
plt.ylabel('Utility of publisher', fontsize=16)
plt.show()
