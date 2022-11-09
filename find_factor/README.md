# find_factores

-   this program is for finding a factors and prime series whith two different approaches

1. create and store a series in list and then just use it

    - find the prime series until the number
    - find prime factors
    - made all possible factors by the prime factors
    - Ex. :-

        - number => 204
        - prime factors => [2, 2, 3, 17]
        - generate all factors => [1, 2, 3, 4, 6, 12, 17, 34, 51, 102, 204]

    - analyis said that, prime series generation takes long time
    - so here include file system in it to store the series, need to store configurations as well
    - because you can not say that what is the starting and ending number of prime series by looking we store configuration like min, max and line
    - conditions :-
        - max = 0 (initial) then write to file
        - number < max then copy series from file
        - number > max then generate series (from max to numbers) and append it to file for next time use
    - by using file operation you can spen time on series generation at initial and when needed

2. traverse it every time
    - it manually go with 2 to number
    - if any number devide by that it will store as factor
    - Ex. :-
        - number => 204
        - loop(2 to 204){if 204 % loopElement == 0 then store_it!} => [1, 2, 3, 4, 6, 12, 17, 34, 51, 102, 204]

## param to understand tables and graph

### Mode
- A -> Append (new generated series appended to pervious one)
- N -> New (new generated series from scratch write to file)
- S -> Stored (series is already generated just use it)

### Max_number and Test_cases
- Max_number is max number until series is used in.
- Test_cases is a test numbers with random integer between max and min to find factors

### Series_gen_time_unit, Prime_way, Series_gen_and_test, Conventional_way
- Series_gen_time_unit is denoting the time to generate prime series
- Prime_way is denoting the time to take to solve test cases (series is already generated)
- Series_gen_and_test is the total time to generate and test series
- Conventional_way is using second technique 'traverse it every time' (manually check)

---
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

![image based on above numbers](https://github.com/JayPonda/general-projects/blob/main/find_factor/testplot1.png)

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


![image based on above numbers](https://github.com/JayPonda/general-projects/blob/main/find_factor/testplot2.png)
