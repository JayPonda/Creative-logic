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

<table style="width: 100%; text-align: center ;">
    <tr style="color: yellow;">
        <th>No.</th>
        <th>Index</th>
        <th>Mode</th>
        <th>Max_number</th>
        <th>Test_cases</th>
        <th>Series_gen_time_unit</th>
        <th>Prime_way</th>
        <th>Series_gen_and_test</th>
        <th>Conventional_way</th>
    </tr>
    <tr>
        <th>1</th>
        <td rowspan="3">1</td>
        <td>Append</td>
        <td>10000</td>
        <td>1000</td>
        <td>0.0528865</td>
        <td>0.7881502</td>
        <td>0.8400302</td>
        <td>0.7364731</td>
    </tr>
    <tr>
        <th>2</th>
        <td>New</td>
        <td>10000</td>
        <td>1000</td>
        <td>0.0538962</td>
        <td>0.7160755</td>
        <td>0.7679399</td>
        <td>0.5944165</td>
    </tr>
    <tr>
        <th>3</th>
        <td>Stored</td>
        <td>10000</td>
        <td>1000</td>
        <td>0.0009836</td>
        <td>0.7972804</td>
        <td>0.7972391</td>
        <td>0.8666262</td>
    </tr>
    <tr>
        <th>4</th>
        <td rowspan="3">2</td>
        <td>Append</td>
        <td>20000</td>
        <td>1000</td>
        <td>0.1406287</td>
        <td>1.0062507</td>
        <td>1.1448938</td>
        <td>1.4677092</td>
    </tr>
    <tr>
        <th>5</th>
        <td>New</td>
        <td>20000</td>
        <td>1000</td>
        <td>0.1677876</td>
        <td>0.981108</td>
        <td>1.1333212</td>
        <td>1.3452905</td>
    </tr>
    <tr>
        <th>6</th>
        <td>Stored</td>
        <td>20000</td>
        <td>1000</td>
        <td>0.0009967</td>
        <td>0.9184575</td>
        <td>0.918455</td>
        <td>1.5740479</td>
    </tr>
    <tr>
        <th>7</th>
        <td rowspan="3">3</td>
        <td>Append</td>
        <td>30000</td>
        <td>1000</td>
        <td>0.1763913</td>
        <td>1.2263351</td>
        <td>1.4027264</td>
        <td>2.3233395</td>
    </tr>
    <tr>
        <th>8</th>
        <td>New</td>
        <td>30000</td>
        <td>1000</td>
        <td>0.3449127</td>
        <td>1.3094783</td>
        <td>1.654391</td>
        <td>2.1606325</td>
    </tr>
    <tr>
        <th>9</th>
        <td>Stored</td>
        <td>30000</td>
        <td>1000</td>
        <td>0.0011792</td>
        <td>1.145371</td>
        <td>1.1465502</td>
        <td>2.2298343</td>
    </tr>
    <tr>
        <th>10</th>
        <td rowspan="3">4</td>
        <td>Append</td>
        <td>40000</td>
        <td>1000</td>
        <td>0.2258937</td>
        <td>1.4907274</td>
        <td>1.7166211</td>
        <td>3.031733</td>
    </tr>
    <tr>
        <th>11</th>
        <td>New</td>
        <td>40000</td>
        <td>1000</td>
        <td>0.5894926</td>
        <td>1.4511536</td>
        <td>2.0406462</td>
        <td>3.1078992</td>
    </tr>
    <tr>
        <th>12</th>
        <td>Stored</td>
        <td>40000</td>
        <td>1000</td>
        <td>0.0011269</td>
        <td>1.4892589</td>
        <td>1.4883631</td>
        <td>2.864977</td>
    </tr>
    <tr>
        <th>13</th>
        <td rowspan="3">5</td>
        <td>Append</td>
        <td>50000</td>
        <td>1000</td>
        <td>0.3021148</td>
        <td>1.8193708</td>
        <td>2.0741725</td>
        <td>3.9258817</td>
    </tr>
    <tr>
        <th>14</th>
        <td>New</td>
        <td>50000</td>
        <td>1000</td>
        <td>0.9040748</td>
        <td>1.7935983</td>
        <td>2.6976731</td>
        <td>3.6911278</td>
    </tr>
    <tr>
        <th>15</th>
        <td>Stored</td>
        <td>50000</td>
        <td>1000</td>
        <td>0.0021991</td>
        <td>1.6991925</td>
        <td>1.6993942</td>
        <td>3.7469348</td>
    </tr>
    <tr>
        <th>16</th>
        <td rowspan="3">6</td>
        <td>Append</td>
        <td>60000</td>
        <td>1000</td>
        <td>0.3647892</td>
        <td>2.0819719</td>
        <td>2.4467611</td>
        <td>4.8699722</td>
    </tr>
    <tr>
        <th>17</th>
        <td>New</td>
        <td>60000</td>
        <td>1000</td>
        <td>1.3266888</td>
        <td>2.0594434</td>
        <td>3.3841451</td>
        <td>4.8489232</td>
    </tr>
    <tr>
        <th>18</th>
        <td>Stored</td>
        <td>60000</td>
        <td>1000</td>
        <td>0.0020289</td>
        <td>2.148558</td>
        <td>2.1475944</td>
        <td>4.6574123</td>
    </tr>
    <tr>
        <th>19</th>
        <td rowspan="3">7</td>
        <td>Append</td>
        <td>70000</td>
        <td>1000</td>
        <td>0.5120686</td>
        <td>2.498537</td>
        <td>3.0106056</td>
        <td>5.8631154</td>
    </tr>
    <tr>
        <th>20</th>
        <td>New</td>
        <td>70000</td>
        <td>1000</td>
        <td>2.0111762</td>
        <td>2.235455</td>
        <td>4.2466312</td>
        <td>5.5635857</td>
    </tr>
    <tr>
        <th>21</th>
        <td>Stored</td>
        <td>70000</td>
        <td>1000</td>
        <td>0.0030148</td>
        <td>2.3291322</td>
        <td>2.3291179</td>
        <td>5.1903467</td>
    </tr>
    <tr>
        <th>22</th>
        <td rowspan="3">8</td>
        <td>Append</td>
        <td>80000</td>
        <td>1000</td>
        <td>0.4629436</td>
        <td>2.4825789</td>
        <td>2.9455225</td>
        <td>6.2381011</td>
    </tr>
    <tr>
        <th>23</th>
        <td>New</td>
        <td>80000</td>
        <td>1000</td>
        <td>2.2194864</td>
        <td>2.4913181</td>
        <td>4.7108045</td>
        <td>6.2734586</td>
    </tr>
    <tr>
        <th>24</th>
        <td>Stored</td>
        <td>80000</td>
        <td>1000</td>
        <td>0.0020044</td>
        <td>2.4677117</td>
        <td>2.4657191</td>
        <td>6.0882675</td>
    </tr>
    <tr>
        <th>25</th>
        <td rowspan="3">9</td>
        <td>Append</td>
        <td>90000</td>
        <td>1000</td>
        <td>0.4945009</td>
        <td>2.8254099</td>
        <td>3.3042918</td>
        <td>7.0003862</td>
    </tr>
    <tr>
        <th>26</th>
        <td>New</td>
        <td>90000</td>
        <td>1000</td>
        <td>2.6508678</td>
        <td>2.667953</td>
        <td>5.3188208</td>
        <td>7.0580779</td>
    </tr>
    <tr>
        <th>27</th>
        <td>Stored</td>
        <td>90000</td>
        <td>1000</td>
        <td>0.0029921</td>
        <td>2.7183748</td>
        <td>2.718376</td>
        <td>6.8748113</td>
    </tr>

</table>

#

<table style="width: 100%; text-align: center ;">
    <tr style="color: yellow;">
        <th>No.</th>
        <th>Index</th>
        <th>Mode</th>
        <th>Max_number</th>
        <th>Test_cases</th>
        <th>Series_gen_time_unit</th>
        <th>Prime_way</th>
        <th>Series_gen_and_test</th>
        <th>Conventional_way</th>
    </tr>
    <tr>
        <th>1</th>
        <td rowspan="3">1</td>
        <td>Append</td>
        <td>100000</td>
        <td>5000</td>
        <td>0.6778273</td>
        <td>15.2278957</td>
        <td>15.9017336</td>
        <td>39.2414358</td>
    </tr>
    <tr>
        <th>2</th>
        <td>New</td>
        <td>100000</td>
        <td>5000</td>
        <td>3.1814263</td>
        <td>15.0512899</td>
        <td>18.217093</td>
        <td>40.0710079</td>
    </tr>
    <tr>
        <th>3</th>
        <td>Stored</td>
        <td>100000</td>
        <td>5000</td>
        <td>0.0030177</td>
        <td>14.9258004</td>
        <td>14.9248015</td>
        <td>38.3154795</td>
    </tr>
    <tr>
        <th>4</th>
        <td rowspan="3">2</td>
        <td>Append</td>
        <td>200000</td>
        <td>5000</td>
        <td>7.7676573</td>
        <td>25.6460485</td>
        <td>33.4137058</td>
        <td>78.0638663</td>
    </tr>
    <tr>
        <th>5</th>
        <td>New</td>
        <td>200000</td>
        <td>5000</td>
        <td>11.3724906</td>
        <td>26.9263864</td>
        <td>38.2938994</td>
        <td>87.0987579</td>
    </tr>
    <tr>
        <th>6</th>
        <td>Stored</td>
        <td>200000</td>
        <td>5000</td>
        <td>0.0078533</td>
        <td>32.9824093</td>
        <td>32.9822853</td>
        <td>114.9277603</td>
    </tr>
    <tr>
        <th>7</th>
        <td rowspan="3">3</td>
        <td>Append</td>
        <td>300000</td>
        <td>5000</td>
        <td>16.8063414</td>
        <td>43.5165551</td>
        <td>60.313268</td>
        <td>154.6110116</td>
    </tr>
    <tr>
        <th>8</th>
        <td>New</td>
        <td>300000</td>
        <td>5000</td>
        <td>29.9398437</td>
        <td>41.3416238</td>
        <td>71.2658446</td>
        <td>132.5058354</td>
    </tr>
    <tr>
        <th>9</th>
        <td>Stored</td>
        <td>300000</td>
        <td>5000</td>
        <td>0.0089943</td>
        <td>38.0678179</td>
        <td>38.0648784</td>
        <td>115.6743067</td>
    </tr>
    <tr>
        <th>10</th>
        <td rowspan="3">4</td>
        <td>Append</td>
        <td>400000</td>
        <td>5000</td>
        <td>16.138266</td>
        <td>50.2407246</td>
        <td>66.3633755</td>
        <td>177.8148662</td>
    </tr>
    <tr>
        <th>11</th>
        <td>New</td>
        <td>400000</td>
        <td>5000</td>
        <td>53.685974</td>
        <td>52.0169731</td>
        <td>105.6929757</td>
        <td>171.5553992</td>
    </tr>
    <tr>
        <th>12</th>
        <td>Stored</td>
        <td>400000</td>
        <td>5000</td>
        <td>0.0109269</td>
        <td>51.5001343</td>
        <td>51.5000898</td>
        <td>173.3979866</td>
    </tr>
    <tr>
        <th>13</th>
        <td rowspan="3">5</td>
        <td>Append</td>
        <td>500000</td>
        <td>5000</td>
        <td>19.8319418</td>
        <td>60.6673779</td>
        <td>80.4993197</td>
        <td>214.3323073</td>
    </tr>
    <tr>
        <th>14</th>
        <td>New</td>
        <td>500000</td>
        <td>5000</td>
        <td>64.3516635</td>
        <td>59.6934039</td>
        <td>124.0366153</td>
        <td>204.755732</td>
    </tr>
    <tr>
        <th>15</th>
        <td>Stored</td>
        <td>500000</td>
        <td>5000</td>
        <td>0.0120008</td>
        <td>68.316702</td>
        <td>68.30378</td>
        <td>253.2795602</td>
    </tr>

</table>
