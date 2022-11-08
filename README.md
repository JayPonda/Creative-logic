# general-projects

-   This repo has programs with pure logic which does not contain any Ui if not necessary.

### Push_pop

-   push_pop.java is the program for simulate the stack operation
-   it has method like push, pop etc.
-   tech-stack: `Java`

### Find_words

-   find_words.py is the program for finding word from matrix
-   it's use human approach for the soluation (Regex is not used)
-   tech-stack: `Python`

### Oop_with_python

-   oop_with_python.py is the program for simulate the bank tranjection
-   it has many methods like credit, debit, block money , unblock money etc.
-   tech-stack: `Python`

### Tree

-   I am trying to create the word suggestion builder.
-   it is based on tree Structure. So, I make two classes, Node and Tree
-   Node.py has node class with three attributes title, isword (if that node is ending of word then True), child and various methods to support operation on them.
-   Tree.py has node class with two attributes root, wordset and various methods to support operation on them.
-   here some methods based on nth child tree. and all methods are bit logical to understand but i provide all necessary details case so you can understand .
-   tech-stack: `Python`

> thanks for helping me
> https://www.geeksforgeeks.org/preorder-traversal-of-n-ary-tree-without-recursion/ > https://stackoverflow.com/questions/71115301/convert-object-structure-of-n-child-tree-to-nested-list-in-python

### Calculator

-   calculator.js is the program for simulating the basic accumulator based calculator
-   tech-stack: `JavaScript`

### socket

-   socket is the program learning the communication between two languages like python as backend and javascript as frontend
-   main motive is to learning communication with websockets and json
-   more details are at socket/README.md
-   tech-stack: `Python` and `JavaScript`

### socket_1

-   socket_1 is the program which uses general socket for communication using ports
-   tech-stack: `Python`

### find_factores

-   this program is for finding a factors and prime series whith two different approaches

1. create and store a series in list and then just use it
2. traverse it every time

-   for the average you can say approach 2 is best, where for long tearm use of same series approach 1 is best
-   tech-stack: `Python`

<table style="width: 100%;">
    <tr style="color: yellow;">
        <th>no.</th>
        <th>If data status</th>
        <th>Max val</th>
        <th>Tests</th>
        <th>series gen (sec)</th>
        <th>My way (sec)</th>
        <th>Conventional way (sec)</th>
    </tr>
    <tr>
        <th rowspan="3">1</th>
        <td>New</td>
        <td>10000</td>
        <td>1000</td>
        <td>0.0624952</td>
        <td>0.7790849</td>
        <td>0.7768679</td>
    </tr>
    <tr>
        <td>Append</td>
        <td>10000</td>
        <td>1000</td>
        <td>0.0538906</td>
        <td>0.7275436</td>
        <td>0.7040222</td>
    </tr>
    <tr>
        <td>Stored</td>
        <td>10000</td>
        <td>1000</td>
        <td>0.0009926</td>
        <td>0.6826711</td>
        <td>0.9253692</td>
    </tr>
    <tr>
        <th rowspan="3">2</th>
        <td>New</td>
        <td>20000</td>
        <td>1000</td>
        <td>0.2348461</td>
        <td>1.1134726</td>
        <td>1.6557513</td>
    </tr>
    <tr>
        <td>Append</td>
        <td>20000</td>
        <td>1000</td>
        <td>0.1237549</td>
        <td>1.1398732</td>
        <td>1.6983864</td>
    </tr>
    <tr>
        <td>Stored</td>
        <td>20000</td>
        <td>1000</td>
        <td>0.000999</td>
        <td>1.1579521</td>
        <td>1.5254924</td>
    </tr>
    <tr>
        <th rowspan="3">3</th>
        <td>New</td>
        <td>30000</td>
        <td>1000</td>
        <td>0.5220158</td>
        <td>1.3830338</td>
        <td>2.7015932</td>
    </tr>
    <tr>
        <td>Append</td>
        <td>30000</td>
        <td>1000</td>
        <td>0.208784</td>
        <td>1.5261743</td>
        <td>2.394605</td>
    </tr>
    <tr>
        <td>Stored</td>
        <td>30000</td>
        <td>1000</td>
        <td>0.0020559</td>
        <td>1.4563242</td>
        <td>2.547935</td>
    </tr>
    <tr>
        <th rowspan="3">4</th>
        <td>New</td>
        <td>40000</td>
        <td>1000</td>
        <td>1.3806075</td>
        <td>3.0270143</td>
        <td>6.2135168</td>
    </tr>
    <tr>
        <td>Append</td>
        <td>40000</td>
        <td>1000</td>
        <td>0.4548412</td>
        <td>2.9764715</td>
        <td>6.5435798</td>
    </tr>
    <tr>
        <td>Stored</td>
        <td>40000</td>
        <td>1000</td>
        <td>0.0</td>
        <td>2.7670014</td>
        <td>6.4506761</td>
    </tr>
    <tr>
        <th rowspan="3">5</th>
        <td>New</td>
        <td>50000</td>
        <td>1000</td>
        <td>1.9779806</td>
        <td>3.1805483</td>
        <td>7.0680908</td>
    </tr>
    <tr>
        <td>Append</td>
        <td>50000</td>
        <td>1000</td>
        <td>0.5969372</td>
        <td>3.3745529</td>
        <td>7.7364838</td>
    </tr>
    <tr>
        <td>Stored</td>
        <td>50000</td>
        <td>1000</td>
        <td>0.0043832</td>
        <td>3.2571447</td>
        <td>6.9415021</td>
    </tr>
    <tr>
        <th rowspan="3">6</th>
        <td>New</td>
        <td>60000</td>
        <td>1000</td>
        <td>1.5351643</td>
        <td>2.2002053</td>
        <td>5.3187425</td>
    </tr>
    <tr>
        <td>Append</td>
        <td>60000</td>
        <td>1000</td>
        <td>0.481937</td>
        <td>2.4627816</td>
        <td>6.0297753</td>
    </tr>
    <tr>
        <td>Stored</td>
        <td>60000</td>
        <td>1000</td>
        <td>0.0</td>
        <td>2.720808</td>
        <td>6.0032304</td>
    </tr>
    <tr>
        <th rowspan="3">7</th>
        <td>New</td>
        <td>70000</td>
        <td>1000</td>
        <td>1.787838</td>
        <td>2.6912392</td>
        <td>5.9058399</td>
    </tr>
    <tr>
        <td>Append</td>
        <td>70000</td>
        <td>1000</td>
        <td>0.5968434</td>
        <td>2.9165111</td>
        <td>6.1391765</td>
    </tr>
    <tr>
        <td>Stored</td>
        <td>70000</td>
        <td>1000</td>
        <td>0.0029918</td>
        <td>2.8164238</td>
        <td>5.1174691</td>
    </tr>
    <tr>
        <th rowspan="3">8</th>
        <td>New</td>
        <td>80000</td>
        <td>1000</td>
        <td>2.4399638</td>
        <td>2.7754747</td>
        <td>6.6696392</td>
    </tr>
    <tr>
        <td>Append</td>
        <td>80000</td>
        <td>1000</td>
        <td>0.4953332</td>
        <td>2.7972398</td>
        <td>7.2380914</td>
    </tr>
    <tr>
        <td>Stored</td>
        <td>80000</td>
        <td>1000</td>
        <td>0.0039756</td>
        <td>3.0047801</td>
        <td>7.161904</td>
    </tr>
    <tr>
        <th rowspan="3">9</th>
        <td>New</td>
        <td>90000</td>
        <td>1000</td>
        <td>2.8056207</td>
        <td>3.3490964</td>
        <td>8.3229709</td>
    </tr>
    <tr>
        <td>Append</td>
        <td>90000</td>
        <td>1000</td>
        <td>0.5143566</td>
        <td>2.9878113</td>
        <td>7.2868422</td>
    </tr>
    <tr>
        <td>Stored</td>
        <td>90000</td>
        <td>1000</td>
        <td>0.0039944</td>
        <td>3.239448</td>
        <td>7.8315097</td>
    </tr>

</table>

---

<table style="width: 100%;">
    <tr style="color: yellow;">
        <th>no.</th>
        <th>If data status</th>
        <th>Max val</th>
        <th>Tests</th>
        <th>series gen (sec)</th>
        <th>My way (sec)</th>
        <th>Conventional way (sec)</th>
    </tr>
    <tr>
        <th rowspan="3">1</th>
        <td>New</td>
        <td>1,00,000</td>
        <td>10,000</td>
        <td>3.8002620</td>
        <td>40.5087662</td>
        <td>92.8625092</td>
    </tr>
    <tr>
        <td>Append</td>
        <td>1,00,000</td>
        <td>10,000</td>
        <td>3.4065963</td>
        <td>10.9461754</td>
        <td>96.9054788</td>
    </tr>
    <tr>
        <td>Stored</td>
        <td>1,00,000</td>
        <td>10,000</td>
        <td>0.0009058</td>
        <td>8.1455738</td>
        <td>92.6213722</td>
    </tr>
    <tr>
        <th rowspan="3">2</th>
        <td>New</td>
        <td>2,00,000</td>
        <td>10,000</td>
        <td>11.7305014</td>
        <td>67.9597961</td>
        <td>195.4355649</td>
    </tr>
    <tr>
        <td>Append</td>
        <td>2,00,000</td>
        <td>10,000</td>
        <td>12.7713555</td>
        <td>40.8974730</td>
        <td>188.5963687</td>
    </tr>
    <tr>
        <td>Stored</td>
        <td>2,00,000</td>
        <td>10,000</td>
        <td>0.0029816</td>
        <td>40.4113516</td>
        <td>194.489869</td>
    </tr>
    <tr>
        <th rowspan="3">3</th>
        <td>New</td>
        <td>3,00,000</td>
        <td>10,000</td>
        <td>25.3248275</td>
        <td>90.8939934</td>
        <td>290.4183016</td>
    </tr>
    <tr>
        <td>Append</td>
        <td>3,00,000</td>
        <td>10,000</td>
        <td>23.9335336</td>
        <td>65.9452268</td>
        <td>284.675661</td>
    </tr>
    <tr>
        <td>Stored</td>
        <td>3,00,000</td>
        <td>10,000</td>
        <td>0.00600560</td>
        <td>65.5271990</td>
        <td>290.2362730</td>
    </tr>
    <tr>
        <th rowspan="3">4</th>
        <td>New</td>
        <td>4,00,000</td>
        <td>10,000</td>
        <td>44.1673321</td>
        <td>110.7451073</td>
        <td>386.6782653</td>
    </tr>
    <tr>
        <td>Append</td>
        <td>4,00,000</td>
        <td>10,000</td>
        <td>40.3358079</td>
        <td>93.3689912</td>
        <td>396.7433406</td>
    </tr>
    <tr>
        <td>Stored</td>
        <td>4,00,000</td>
        <td>10,000</td>
        <td>0.0156172</td>
        <td>94.0845033</td>
        <td>417.7910897</td>
    </tr>
    <tr>
        <th rowspan="3">5</th>
        <td>New</td>
        <td>5,00,000</td>
        <td>10,000</td>
        <td>25.3248275</td>
        <td>90.8939934</td>
        <td>290.4183016</td>
    </tr>
    <tr>
        <td>Append</td>
        <td>5,00,000</td>
        <td>10,000</td>
        <td>21.7938066</td>
        <td>136.1609919</td>
        <td>479.2451510</td>
    </tr>
    <tr>
        <td>Stored</td>
        <td>5,00,000</td>
        <td>10,000</td>
        <td>0.0139983</td>
        <td>134.1260118</td>
        <td>474.6456566</td>
    </tr>

</table>
