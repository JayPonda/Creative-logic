import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import os
import csv
import time
from find_factores import MathMagic


def printTest(ar, tn):

    arcs = ar
    tests = np.zeros(arcs, dtype=int)
    testNumber = tn

    testResults1 = np.zeros(arcs, dtype=float)
    testResults2 = np.zeros(arcs, dtype=float)
    interwal: int = testNumber / arcs
    obj = MathMagic()

    for i in range(arcs):

        xNumber = random.randint((i * interwal) + 1, (i + 1) * interwal)
        tests[i] = xNumber
        # print(xNumber)

        # test 1
        # print("\ntest 1: find prime factors, comparing and dividing with prime")
        k = time.time_ns()
        s1 = set(obj.findAllFactorsByPrime(testNumber))
        k1 = time.time_ns()

        testResults1[i] = (k1 - k) * (10 ** -9)

        # test 2
        # print("\ntest 2: find prime factors, checking for prime from all factors set")
        k = time.time_ns()
        lis = obj.findAllFactors(testNumber)
        k1 = time.time_ns()

        testResults2[i] = (k1 - k) * (10 ** -9)

    del s1
    del lis
    del obj

    # avg1 = np.round(np.mean(testResults1), 5)
    sum = np.sum(testResults1)
    first = testResults1[0]
    testResults1[0] = testResults1[1]
    # plt.axes()
    # plt.plot(tests, testResults1, '-.', label=f"testResults1: {avg1} sec")
    # avg = np.round(np.mean(testResults2), 5)
    # plt.plot(tests, testResults2, '-o', label=f"testResults2: {avg} sec")
    # plt.title(
    #     f"find prime series gen ({np.sum(testResults1)} sec) + gen factors vs try all factors ({np.sum(testResults2)} sec)")
    print(f"secondary avg: {(first + np.mean(testResults1)) / 2}")

    # plt.legend()
    return (np.round(first, 7),
            np.round(np.sum(testResults1), 7),
            np.round(sum, 7),
            np.round(np.sum(testResults2), 7))
    # plt.show()
    # plt.savefig('testplot' + str(np.random.randint(1, 1000)) + '.png')


if __name__ == "__main__":
    sz = 2

    f1 = open(f'table {sz}.txt', 'x')
    f2 = open(f'table {sz}.csv', 'x')
    f2Writter = csv.writer(f2)
    f2Writter.writerow(['No', 'Index', 'Mode', 'Max_number', 'Test_cases',
                        'Series_gen_time_unit', 'Prime_way', 'Series_gen_and_test', 'Conventional_way'])
    no = 1
    for i in range(1, 6):
        # Append
        k = printTest(5000, i * 100000)
        os.remove('PrimeList.txt')
        os.remove('PrimeConfig.json')
        # New
        k1 = printTest(5000, i * 100000)
        # Stored
        k2 = printTest(5000, i * 100000)
        max_num = i * 100000
        f1.write(f"""
    <tr>
        <th>{no + 0}</th>
        <td rowspan="3">{i + 1}</td>
        <td>Append</td>
        <td>{max_num}</td>
        <td>1000</td>
        <td>{k[0]}</td>
        <td>{k[1]}</td>
        <td>{k[2]}</td>
        <td>{k[3]}</td>
    </tr>
    <tr>
        <th>{no + 1}</th>
        <td>New</td>
        <td>{max_num}</td>
        <td>1000</td>
        <td>{k1[0]}</td>
        <td>{k1[1]}</td>
        <td>{k1[2]}</td>
        <td>{k1[3]}</td>
    </tr>
    <tr>
        <th>{no + 2}</th>
        <td>Stored</td>
        <td>{max_num}</td>
        <td>1000</td>
        <td>{k2[0]}</td>
        <td>{k2[1]}</td>
        <td>{k2[2]}</td>
        <td>{k2[3]}</td>
    </tr>""")

        f2Writter.writerow(
            [no, i + 1, "Append",  str(max_num) + " A", 1000, k[0], k[1], k[2], k[3]])
        f2Writter.writerow(
            [no + 1, i + 1, "New",  str(max_num) + " N", 1000, k1[0], k1[1], k1[2], k1[3]])
        f2Writter.writerow(
            [no + 2, i + 1, "Stored",  str(max_num) + " S", 1000, k2[0], k2[1], k2[2], k2[3]])
        no += 3

    f1.close()
    f2.close()
    plt.figure()
    df = pd.read_csv(f'table {sz}.csv')
    df.plot(x="Max_number", y=['Series_gen_time_unit', 'Conventional_way',
                               'Series_gen_and_test', 'Prime_way'], kind="bar")
    fig = plt.gcf()
    plt.ylabel("time in unit seconds")
    fig.set_size_inches(32, 18)
    plt.savefig(f'testplot{sz}.png', bbox_inches="tight")
    plt.show()
