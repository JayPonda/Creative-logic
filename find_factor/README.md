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

-   A -> Append (new generated series appended to pervious one)
-   N -> New (new generated series from scratch write to file)
-   S -> Stored (series is already generated just use it)

### Max_number and Test_cases

-   Max_number is max number until series is used in.
-   Test_cases is a test numbers with random integer between max and min to find factors

### Series_gen_time_unit, Prime_way, Series_gen_and_test, Conventional_way

-   Series_gen_time_unit is denoting the time to generate prime series
-   Prime_way is denoting the time to take to solve test cases (series is already generated)
-   Series_gen_and_test is the total time to generate and test series
-   Conventional_way is using second technique 'traverse it every time' (manually check)

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
        <th>0</th>
        <td rowspan="3">1</td>
        <td>Append</td>
        <td>10000</td>
        <td>1000</td>
        <td>0.0725873</td>
        <td>1.0084328</td>
        <<td >1.0800203</td>
        <td style="background: rgba(0, 255, 0, .5);">0.8472879</td>
    </tr>
        <tr>
        <th>1</th>
        td rowspan="2">1</td>
        <td>New</td>
        <td>10000</td>
        <td>1000</td>
        <td>0.0747988</td>
        <td>0.9678253</td>
        <td >1.0406294</td>
        <td style="background: rgba(0, 255, 0, .5);">0.8112329</td>
    </tr>
    <tr>
        <th>2</th>
        <td>Stored</td>
        <td>10000</td>
        <td>1000</td>
        <td>0.001035</td>
        <td>0.9974459</td>
        <td >0.9974816</td>
        <td style="background: rgba(0, 255, 0, .5);">0.6791498</td>
    </tr>
    <tr>
        <th>3</th>
        <td rowspan="3">2</td>
        <td>Append</td>
        <td>20000</td>
        <td>1000</td>
        <td>0.1247213</td>
        <td>1.4102185</td>
        <<td style="background: rgba(0, 255, 0, .5);">1.5329459</td>
        <td >1.6046381</td>
    </tr>
    <tr>
        <th>4</th>
        <td>New</td>
        <td>20000</td>
        <td>1000</td>
        <td>0.1660614</td>
        <td>1.2727117</td>
        <td style="background: rgba(0, 255, 0, .5);">1.4387731</td>
        <td >1.511102</td>
    </tr>
    <tr>
        <th>5</th>
        <td>Stored</td>
        <td>20000</td>
        <td>1000</td>
        <td>0.0019944</td>
        <td>1.4093418</td>
        <td >1.4103382</td>
        <td style="background: rgba(0, 255, 0, .5);">1.4024077</td>
    </tr>
    <tr>
        <th>6</th>
        <td rowspan="3">3</td>
        <td>Append</td>
        <td>30000</td>
        <td>1000</td>
        <td>0.1711054</td>
        <td>1.5281351</td>
        <<td style="background: rgba(0, 255, 0, .5);">1.6992405</td>
        <td >2.2484209</td>
    </tr>
    <tr>
        <th>7</th>
        <td>New</td>
        <td>30000</td>
        <td>1000</td>
        <td>0.3410967</td>
        <td>1.5118792</td>
        <td style="background: rgba(0, 255, 0, .5);">1.8529759</td>
        <td >2.3529115</td>
    </tr>
    <tr>
        <th>8</th>
        <td>Stored</td>
        <td>30000</td>
        <td>1000</td>
        <td>0.0022351</td>
        <td>1.6479179</td>
        <td style="background: rgba(0, 255, 0, .5);">1.6481752</td>
        <td >2.1794746</td>
    </tr>
    <tr>
        <th>9</th>
        <td rowspan="3">4</td>
        <td>Append</td>
        <td>40000</td>
        <td>1000</td>
        <td>0.2453593</td>
        <td>2.1011568</td>
        <<td style="background: rgba(0, 255, 0, .5);">2.3465161</td>
        <td >2.9113228</td>
    </tr>
    <tr>
        <th>10</th>
        <td>New</td>
        <td>40000</td>
        <td>1000</td>
        <td>0.650971</td>
        <td>2.1277774</td>
        <td style="background: rgba(0, 255, 0, .5);">2.7787484</td>
        <td >2.9756347</td>
    </tr>
    <tr>
        <th>11</th>
        <td>Stored</td>
        <td>40000</td>
        <td>1000</td>
        <td>0.0020218</td>
        <td>2.1139841</td>
        <td style="background: rgba(0, 255, 0, .5);">2.1129832</td>
        <td >2.8478522</td>
    </tr>
    <tr>
        <th>12</th>
        <td rowspan="3">5</td>
        <td>Append</td>
        <td>50000</td>
        <td>1000</td>
        <td>0.2903753</td>
        <td>2.1392421</td>
        <<td style="background: rgba(0, 255, 0, .5);">2.4296174</td>
        <td >3.6684164</td>
    </tr>
    <tr>
        <th>13</th>
        <td>New</td>
        <td>50000</td>
        <td>1000</td>
        <td>0.8774869</td>
        <td>2.0573285</td>
        <td style="background: rgba(0, 255, 0, .5);">2.9191939</td>
        <td >3.886542</td>
    </tr>
    <tr>
        <th>14</th>
        <td>Stored</td>
        <td>50000</td>
        <td>1000</td>
        <td>0.0030172</td>
        <td>2.4531743</td>
        <td style="background: rgba(0, 255, 0, .5);">2.4531627</td>
        <td >3.8732814</td>
    </tr>
    <tr>
        <th>15</th>
        <td rowspan="3">6</td>
        <td>Append</td>
        <td>60000</td>
        <td>1000</td>
        <td>0.3854113</td>
        <td>2.9517303</td>
        <<td style="background: rgba(0, 255, 0, .5);">3.3371416</td>
        <td >5.0393714</td>
    </tr>
    <tr>
        <th>16</th>
        <td>New</td>
        <td>60000</td>
        <td>1000</td>
        <td>1.6834033</td>
        <td>2.5500491</td>
        <td style="background: rgba(0, 255, 0, .5);">4.2334524</td>
        <td >4.984856</td>
    </tr>
    <tr>
        <th>17</th>
        <td>Stored</td>
        <td>60000</td>
        <td>1000</td>
        <td>0.0020147</td>
        <td>2.5888292</td>
        <td style="background: rgba(0, 255, 0, .5);">2.5878564</td>
        <td >4.6215791</td>
    </tr>
    <tr>
        <th>18</th>
        <td rowspan="3">7</td>
        <td>Append</td>
        <td>70000</td>
        <td>1000</td>
        <td>0.3870421</td>
        <td>2.148117</td>
        <<td style="background: rgba(0, 255, 0, .5);">2.5351591</td>
        <td >5.9192002</td>
    </tr>
    <tr>
        <th>19</th>
        <td>New</td>
        <td>70000</td>
        <td>1000</td>
        <td>1.7115484</td>
        <td>2.8686526</td>
        <td style="background: rgba(0, 255, 0, .5);">4.5772182</td>
        <td >5.291361</td>
    </tr>
    <tr>
        <th>20</th>
        <td>Stored</td>
        <td>70000</td>
        <td>1000</td>
        <td>0.0029902</td>
        <td>2.6509022</td>
        <td style="background: rgba(0, 255, 0, .5);">2.6499091</td>
        <td >5.2240322</td>
    </tr>
    <tr>
        <th>21</th>
        <td rowspan="3">8</td>
        <td>Append</td>
        <td>80000</td>
        <td>1000</td>
        <td>0.4857346</td>
        <td>3.6024705</td>
        <<td style="background: rgba(0, 255, 0, .5);">4.0882051</td>
        <td >6.5767905</td>
    </tr>
    <tr>
        <th>22</th>
        <td>New</td>
        <td>80000</td>
        <td>1000</td>
        <td>2.1791168</td>
        <td>3.6203965</td>
        <td style="background: rgba(0, 255, 0, .5);">5.7838851</td>
        <td >6.2879084</td>
    </tr>
    <tr>
        <th>23</th>
        <td>Stored</td>
        <td>80000</td>
        <td>1000</td>
        <td>0.0059831</td>
        <td>3.5999806</td>
        <td style="background: rgba(0, 255, 0, .5);">3.6019757</td>
        <td >6.2654432</td>
    </tr>
    <tr>
        <th>24</th>
        <td rowspan="3">9</td>
        <td>Append</td>
        <td>90000</td>
        <td>1000</td>
        <td>0.4815983</td>
        <td>3.251338</td>
        <<td style="background: rgba(0, 255, 0, .5);">3.7329363</td>
        <td >6.86165</td>
    </tr>
    <tr>
        <th>25</th>
        <td>New</td>
        <td>90000</td>
        <td>1000</td>
        <td>2.6450404</td>
        <td>3.3228175</td>
        <td style="background: rgba(0, 255, 0, .5);">5.9678579</td>
        <td >7.0286622</td>
    </tr>
    <tr>
        <th>26</th>
        <td>Stored</td>
        <td>90000</td>
        <td>1000</td>
        <td>0.0030194</td>
        <td>3.3311648</td>
        <td style="background: rgba(0, 255, 0, .5);">3.3287746</td>
        <td >7.3545357</td>
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
        <td>0.5362213</td>
        <td>17.2494803</td>
        <td>17.7857016</td>
        <td>39.2234179</td>
    </tr>
    <tr>
        <th>2</th>
        <td>New</td>
        <td>100000</td>
        <td>5000</td>
        <td>3.2880592</td>
        <td>18.0833416</td>
        <td>21.3714008</td>
        <td>38.490215</td>
    </tr>
    <tr>
        <th>3</th>
        <td>Stored</td>
        <td>100000</td>
        <td>5000</td>
        <td>0.0029903</td>
        <td>18.7907371</td>
        <td>18.7887065</td>
        <td>41.823286</td>
    </tr>
    <tr>
        <th>4</th>
        <td rowspan="3">2</td>
        <td>Append</td>
        <td>200000</td>
        <td>5000</td>
        <td>8.3838732</td>
        <td>34.355628</td>
        <td>42.7395012</td>
        <td>87.1461225</td>
    </tr>
    <tr>
        <th>5</th>
        <td>New</td>
        <td>200000</td>
        <td>5000</td>
        <td>12.6586403</td>
        <td>34.3598905</td>
        <td>47.0185308</td>
        <td>89.5409878</td>
    </tr>
    <tr>
        <th>6</th>
        <td>Stored</td>
        <td>200000</td>
        <td>5000</td>
        <td>0.0079965</td>
        <td>35.7716681</td>
        <td>35.7716548</td>
        <td>88.6045181</td>
    </tr>
    <tr>
        <th>7</th>
        <td rowspan="3">3</td>
        <td>Append</td>
        <td>300000</td>
        <td>5000</td>
        <td>12.9935768</td>
        <td>45.9693711</td>
        <td>58.9473284</td>
        <td>128.6630668</td>
    </tr>
    <tr>
        <th>8</th>
        <td>New</td>
        <td>300000</td>
        <td>5000</td>
        <td>26.1160532</td>
        <td>49.3625052</td>
        <td>75.4785584</td>
        <td>138.9119262</td>
    </tr>
    <tr>
        <th>9</th>
        <td>Stored</td>
        <td>300000</td>
        <td>5000</td>
        <td>0.0109721</td>
        <td>47.372365</td>
        <td>47.372366</td>
        <td>132.3338556</td>
    </tr>
    <tr>
        <th>10</th>
        <td rowspan="3">4</td>
        <td>Append</td>
        <td>400000</td>
        <td>5000</td>
        <td>16.3121231</td>
        <td>61.1627147</td>
        <td>77.4748378</td>
        <td>167.8638146</td>
    </tr>
    <tr>
        <th>11</th>
        <td>New</td>
        <td>400000</td>
        <td>5000</td>
        <td>39.8607987</td>
        <td>60.8464569</td>
        <td>100.6943003</td>
        <td>169.350185</td>
    </tr>
    <tr>
        <th>12</th>
        <td>Stored</td>
        <td>400000</td>
        <td>5000</td>
        <td>0.0149926</td>
        <td>64.2379981</td>
        <td>64.2360686</td>
        <td>194.6077195</td>
    </tr>
    <tr>
        <th>13</th>
        <td rowspan="3">5</td>
        <td>Append</td>
        <td>500000</td>
        <td>5000</td>
        <td>24.4615938</td>
        <td>66.371502</td>
        <td>90.8174739</td>
        <td>202.8988039</td>
    </tr>
    <tr>
        <th>14</th>
        <td>New</td>
        <td>500000</td>
        <td>5000</td>
        <td>71.9573476</td>
        <td>70.8139065</td>
        <td>142.755626</td>
        <td>226.8796614</td>
    </tr>
    <tr>
        <th>15</th>
        <td>Stored</td>
        <td>500000</td>
        <td>5000</td>
        <td>0.0129637</td>
        <td>74.1334226</td>
        <td>74.1304346</td>
        <td>228.9432848</td>
    </tr>
</table>

![image based on above numbers](https://github.com/JayPonda/general-projects/blob/main/find_factor/testplot2.png)
