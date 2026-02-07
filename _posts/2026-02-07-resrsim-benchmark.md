---
layout: default
title: "Benchmark results of resrsim"
date: 2026-02-07
---

# Setup

Read the following notes to run current notebook for the first time. Uncomment the content.

<!-- 1. select kernel before executing current jupyter book

2. Install `ipykernel` package. For a virtual environment, open a terminal, and active the environment. 



    ```bash

    python -m venv .venv

    source .venv/bin/activate

    ```



3. Run `which python` to make sure the right virtual environment activated

4. Install requirments by `pip install -r requirements.txt`

4. Install by `python -m pip install ipykernel -U --force-reinstall`. 

5. install dependent packages `python -m pip install pandas numpy matplotlib trame trame-vtk trame-vuetify vtk` -->

Uncomment the following if you see errors.



<!-- The following is optional:

1. > ModuleNotFoundError: No module named 'distutils.cmd' 



    ```bash

    sudo apt-get install python3-distutils

    ```



2. > ERROR: Could not install packages due to an OSError: Could not find a suitable TLS CA certificate bundle, invalid path: /etc/ssl/certs/ca-certificates.crt



    It indicates that your system is missing the CA certificates    required for secure HTTPS connections. Install CA certificates by

    ```bash

    sudo apt-get install --reinstall ca-certificates

    ```

    After installing the certificates, update them

    ```bash

    sudo update-ca-certificates

    ```



3. `pip install jupyter` if needs -->

```
Current OS: Windows

simuexe path: build/Release/simuapp.exe

RUN_SIMULATIONS: True

```

# 3D



In Jupyter Notebook, `pyvista.set_jupyter_backend("trame")` must install `pyvista` and `trame` 

<!-- 

```bash

python -m pip install --upgrade pip

python -m pip install pyvista

pip install trame trame-vtk trame-vuetify

``` -->


![png]({{ "/assets/images/benchmark_image_1.png" | relative_url }})

## stflu005.dat

steam injection in corner-point grid

```
Running simulation: Steam injection Corner point

    25  55.0000  1   3650.000   295.97             11.63              3.78                      52.49    0.010 5.641890 0.000137 0.014120



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  1.671s    97.03%

|- Newton                                 1.543s    92.33%

  |- Jacobian                             0.825s    53.47%

  |- Update                               0.641s    41.55%

  |- Solver                               0.040s     2.59%

  |- Residual                             0.018s     1.17%

  |- Logging                              0.004s     0.24%

|- Output                                 0.108s     6.47%

|- Input                                  0.001s     0.04%

Initialization                            0.051s     2.97%

------------------------------------------------------------

TOTAL                                     1.722s

============================================================



Time steps : 25/25, step size: 146.00, 129.48

```

```
CompletedProcess(args=['build/Release/simuapp.exe', '-f', 'c:\\Users\\hechr\\source\\hatch\\app/build/test/data//stflu005.dat'], returncode=0, stdout='c:\\Users\\hechr\\source\\hatch\\app/build/test/data\\stflu005.dat\n', stderr='\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1   1.0000  1      1.000   440.38             12.88              2.84                      49.82    0.000 2423.151149 0.000002 0.001661\n     2   0.1360  1      1.136   440.35             12.88              2.84                      49.82    0.000 0.141784 0.000000 0.000213\n     3   0.3171  1      1.453   440.30             12.88              2.84                      49.82    0.000 0.292937 0.000001 0.000439\n     4   0.7384  1      2.192   440.20             12.88              2.84                      49.82    0.000 0.555786 0.000002 0.000841\n     5   1.7166  1      3.908   439.99             12.88              2.84                      49.82    0.000 0.997984 0.000004 0.001909\n     6   3.9789  1      7.887   439.59             12.88              2.85                      49.82    0.000 1.841789 0.000009 0.004292\n     7   9.1716  1     17.059   438.75             12.88              2.85                      49.82    0.001 3.619846 0.000021 0.009481\n     8  20.8960  1     37.955   437.03             12.88              2.86                      49.83    0.001 6.875933 0.000049 0.020354\n     9  46.6203  1     84.575   433.55             12.88              2.89                      49.85    0.002 13.772407 0.000110 0.041556\n    10  99.6329  1    184.208   426.80             12.88              2.93                      49.90    0.002 26.927784 0.000236 0.076860\n    11 197.0946  1    381.302   414.93             12.86              3.01                      50.00    0.003 46.715228 0.000468 0.122866\n    12 213.6976  1    595.000   403.27             12.82              3.08                      50.20    0.004 45.254725 0.000510 0.111648\n    13 365.0000  1    960.000   388.94             12.74              3.17                      50.39    0.005 54.389200 0.000715 0.126704\n    14 135.0000  1   1095.000   382.65             12.70              3.21                      50.65    0.005 23.963498 0.000325 0.055937\n    15 271.6087  1   1366.609   370.94             12.61              3.29                      50.75    0.006 43.737365 0.000655 0.099810\n    16 228.3913  1   1595.000   361.73             12.53              3.35                      50.96    0.007 34.179643 0.000554 0.077891\n    17 365.0000  1   1960.000   348.20             12.39              3.44                      51.12    0.007 49.409416 0.000887 0.112718\n    18 135.0000  1   2095.000   343.37             12.33              3.47                      51.40    0.008 17.658028 0.000330 0.040876\n    19 281.8237  1   2376.824   333.82             12.21              3.53                      51.48    0.008 34.505289 0.000691 0.079882\n    20 218.1763  1   2595.000   326.74             12.12              3.58                      51.68    0.009 25.505492 0.000536 0.059753\n    21 365.0000  1   2960.000   315.59             11.96              3.65                      51.82    0.009 40.075396 0.000899 0.094064\n    22 135.0000  1   3095.000   311.57             11.89              3.68                      52.08    0.009 14.560743 0.000334 0.034701\n    23 287.1280  1   3382.128   303.36             11.76              3.73                      52.15    0.010 29.844489 0.000711 0.071385\n    24 212.8720  1   3595.000   297.47             11.66              3.77                      52.34    0.010 21.905270 0.000529 0.052464\n    25  55.0000  1   3650.000   295.97             11.63              3.78                      52.49    0.010 5.641890 0.000137 0.014120\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                  1.671s    97.03%\n|- Newton                                 1.543s    92.33%\n  |- Jacobian                             0.825s    53.47%\n  |- Update                               0.641s    41.55%\n  |- Solver                               0.040s     2.59%\n  |- Residual                             0.018s     1.17%\n  |- Logging                              0.004s     0.24%\n|- Output                                 0.108s     6.47%\n|- Input                                  0.001s     0.04%\nInitialization                            0.051s     2.97%\n------------------------------------------------------------\nTOTAL                                     1.722s\n============================================================\n\nTime steps : 25/25, step size: 146.00, 129.48\n')
```

```
Found 26 VTU files

Loading: c:\Users\hechr\source\hatch\app/build/test/data\stflu005_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_2.png" | relative_url }})

```
Interactive view: c:\Users\hechr\source\hatch\app/build/test/data\stflu005_00000.vtu

```

```
Widget(value='<iframe src="http://localhost:51613/index.html?ui=P_0x22a55ec9bd0_12&reconnect=auto" class="pyvi…
```

# SPE4-b

* Steam flooding with water and dead oil

* VMod on 9x5x4 cartesian grid


### Load STARS

### Load ECL

### Load SMY File

Load the SMY file (`spe04b.smy`) into a pandas DataFrame, ensuring proper parsing of the data.

```
Running simulation: SPE4-b

    63  39.9310  1   3650.000     0.08             28.63             99.72                      28.95   44.264 0.256486 0.002692 1.056554



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  3.310s    99.68%

|- Newton                                 3.111s    93.99%

  |- Jacobian                             2.130s    68.47%

  |- Update                               0.755s    24.26%

  |- Solver                               0.152s     4.90%

  |- Logging                              0.027s     0.88%

  |- Residual                             0.018s     0.59%

|- Output                                 0.183s     5.54%

|- Input                                  0.000s     0.00%

Initialization                            0.011s     0.32%

------------------------------------------------------------

TOTAL                                     3.321s

============================================================



Time steps : 63/68, step size: 57.94, 76.06

```

```
CompletedProcess(args=['build/Release/simuapp.exe', '-f', 'c:\\Users\\hechr\\source\\hatch\\app/build/test/data//spe04b.dat'], returncode=0, stdout='c:\\Users\\hechr\\source\\hatch\\app/build/test/data\\spe04b.dat\n', stderr='\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1   1.0000  1      1.000     3.96             3e-07             6e-06                       2.76    0.014 32.028377 0.000436 8.759995\n     2   1.8163  1      2.816     3.48              0.03              0.83                       3.74    0.013 33.910669 0.037631 19.841697\n     3   3.2564  1      6.073     3.26              0.04              1.19                       9.08    0.182 28.609198 0.043015 40.500000\n     4   5.5869  9     11.660     2.84              0.05              1.84                      32.55    0.185 112.117770 0.243479 208.248430\n     5   4.5723  4     16.232     2.68              0.06              2.05                      37.50    0.240 68.178722 0.096747 83.253089\n     6   6.1313  3     22.363     2.61              0.05              2.05                      37.50    0.331 49.380233 0.051061 91.630646\n     7   7.8846  5     30.248     2.69              0.05              1.73                      37.51    0.457 62.448420 0.168726 94.203310\n     8   8.6582  3     38.906     2.95              0.03              1.10                      37.47    0.716 44.294146 0.194138 77.468034\n     9   8.8057  2     47.712     3.35              0.02              0.68                      37.50    1.000 30.236768 0.068072 60.014834\n    10  13.3988  2     61.110     4.15              0.01              0.22                      37.48    1.352 33.899422 0.038157 71.010058\n    11  19.1662  3     80.277     5.63              0.00              0.03                      37.49    1.816 40.841941 0.200002 90.431784\n    12  19.1660  4     99.443     6.77              1.77             20.69                      37.50    2.402 41.213685 0.215449 76.178335\n    13  18.3558  2    117.798     7.58              4.31             36.28                      37.50    3.093 33.331401 0.080041 65.846640\n    14  27.0171  5    144.815     8.61              7.74             47.32                      37.49    3.593 40.807191 0.115550 94.361727\n    15  34.2837  5    179.099     9.75             13.28             57.67                      37.48    4.307 43.060223 0.156284 82.045367\n    16  39.1769  4    218.276    10.90             18.93             63.47                      37.50    5.237 35.591869 0.117243 75.394063\n    17  51.3088  5    269.585    13.08             27.61             67.86                      37.50    6.209 25.464568 0.131321 129.400968\n    18  55.6780  5    325.263    17.53             39.90             69.48                      37.51    7.609 30.842855 0.237124 82.829828\n    19  50.3387  5    375.602    22.08             48.85             68.87                      37.51    9.307 53.439050 0.161282 84.754562\n    20  56.6000  6    432.202    24.65             49.15             66.60                      37.49   10.811 47.519718 0.210181 82.521844\n    21  55.0002  4    487.202    23.52             45.05             65.70                      37.53   12.639 35.541445 0.189868 89.072536\n    22  56.6398  6    543.842    22.79             43.11             65.42                      37.50   14.154 29.682843 0.200147 83.512492\n    23  56.6160  5    600.458    22.57             41.51             64.77                      37.49   15.657 20.901108 0.210022 106.250678\n    24  55.0400  6    655.498    23.78             42.52             64.13                      37.50   17.191 28.503433 0.205317 82.435338\n    25  54.2164  7    709.714    25.23             43.70             63.39                      37.50   18.617 18.938674 0.215205 90.966480\n    26  17.3197  3 1  727.034    26.17             44.71             63.08                      37.50   20.549 5.091992 0.148639 26.275267\n    27  20.2985  3    747.332    27.28             46.54             63.04                      37.51   21.065 9.049278 0.109983 35.026857\n    28  27.3266 12    774.659    28.07             43.14             60.58                      37.50   21.733 14.312874 0.165388 63.146117\n    29  27.3266  4    801.985    20.03             36.65             64.66                      37.50   22.572 7.232620 0.147600 52.679996\n    30  32.1382 14    834.124    17.70             35.62             66.80                      37.50   23.309 4.998799 0.150308 82.754348\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31  27.5470  4    861.671    15.03             34.70             69.77                      37.50   24.235 6.731213 0.178464 30.474833\n    32  29.3532  2    891.024    14.41             34.66             70.63                      37.52   24.971 2.760835 0.090354 36.495970\n    33  42.7437  4    933.767    13.19             34.16             72.13                      37.50   25.599 3.201054 0.193017 57.150830\n    34  43.6139  4    977.381    12.98             35.51             73.23                      37.50   26.709 2.277698 0.216955 51.157507\n    35  41.5987  4   1018.980    13.08             36.55             73.65                      37.50   27.567 3.060209 0.197006 63.805138\n    36  41.9576 12   1060.938    13.93             38.40             73.38                      37.50   28.202 5.639820 0.197182 115.451430\n    37  34.0624  3   1095.000    12.68             36.86             74.40                      37.50   29.016 4.900927 0.167462 46.470974\n    38  37.5536  7   1132.554    11.71             35.06             74.96                      37.50   29.444 7.505952 0.171843 43.996711\n    39  40.8390  4   1173.393     9.98             32.86             76.70                      37.50   29.886 7.089446 0.152881 62.905102\n    40  47.1924  4   1220.585     8.59             32.11             78.89                      37.50   30.277 8.427639 0.177956 69.549457\n    41  50.3645  4   1270.950     7.11             31.05             81.36                      37.50   30.755 9.937122 0.184868 62.903066\n    42  52.6403  2   1323.590     6.53             33.16             83.55                      37.48   31.295 11.570740 0.185544 39.482908\n    43  54.9082  4   1378.498     5.41             32.84             85.85                      37.50   31.788 10.956322 0.124348 47.195948\n    44  70.0493  3   1448.547     4.22             31.03             88.03                      37.51   32.030 15.787670 0.145126 19.861449\n    45  83.0739  2   1531.621     3.39             31.06             90.17                      37.50   32.421 19.787770 0.109435 23.400782\n    46 112.0739  2   1643.695     2.69             31.08             92.02                      37.50   32.570 29.370688 0.118807 14.763643\n    47 145.9256  3   1789.621     1.97             30.62             93.96                      37.50   32.808 42.078446 0.089374 18.096852\n    48 213.3644  3   2002.985     1.30             30.15             95.87                      37.52   32.756 70.573047 0.065309 25.142734\n    49 305.9334  5   2308.919     0.71             28.53             97.59                      37.50   32.743 122.188234 0.116768 33.923639\n    50 342.1880  4   2651.107     0.33             26.44             98.75                      37.50   33.813 167.015114 0.069532 35.486951\n    51 321.3578  5   2972.464     0.14             22.95             99.38                      37.49   35.489 188.745989 0.101514 31.549369\n    52 280.0250 10   3252.489     0.05             18.15             99.71                      37.50   37.129 204.423647 0.088202 28.043827\n    53  25.7710  9 2 3278.260     0.07             24.94             99.71                      37.50   41.249 5.698572 0.074962 4.666292\n    54  34.3613  8   3312.622     0.10             31.45             99.68                      37.47   41.537 20.264390 0.151833 20.641144\n    55  13.2816  2 1 3325.903     0.09             30.23             99.71                      37.50   42.005 20.221277 0.198253 20.591412\n    56  13.3482  6   3339.251     0.05             18.64             99.72                      37.49   42.073 5.001556 0.100859 3.984083\n    57   6.2079  9 1 3345.459     0.10             33.15             99.71                      50.89   42.337 1.843159 0.092053 3.288723\n    58   8.2771  1   3353.736     0.06             21.87             99.72                      33.06   42.356 1.844386 0.017978 0.303782\n    59  17.2463  1   3370.983     0.07             24.03             99.72                      31.21   42.341 0.660952 0.021325 0.728772\n    60  35.2326  1   3406.215     0.08             27.16             99.72                      30.49   42.341 0.244712 0.017339 1.088444\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    61  73.6910  2   3479.906     0.08             28.34             99.72                      29.72   42.370 0.223694 0.048151 2.652654\n    62 130.1627  1   3610.069     0.08             29.12             99.72                      29.70   42.736 0.050743 0.002460 3.873942\n    63  39.9310  1   3650.000     0.08             28.63             99.72                      28.95   44.264 0.256486 0.002692 1.056554\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                  3.310s    99.68%\n|- Newton                                 3.111s    93.99%\n  |- Jacobian                             2.130s    68.47%\n  |- Update                               0.755s    24.26%\n  |- Solver                               0.152s     4.90%\n  |- Logging                              0.027s     0.88%\n  |- Residual                             0.018s     0.59%\n|- Output                                 0.183s     5.54%\n|- Input                                  0.000s     0.00%\nInitialization                            0.011s     0.32%\n------------------------------------------------------------\nTOTAL                                     3.321s\n============================================================\n\nTime steps : 63/68, step size: 57.94, 76.06\n')
```

## Select and Plot Columns

Select specific columns from the loaded DataFrames and plot them using matplotlib. For example, plot `TIME` vs `TEMP 1-1-4` from `stars_spe4b_special.csv`.

### Cell property

#### Block Pressure


```
<module 'matplotlib.pyplot' from 'c:\\Users\\hechr\\source\\hatch\\app\\.venv\\Lib\\site-packages\\matplotlib\\pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_3.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_4.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_5.png" | relative_url }})

#### Block Temperature

```
<module 'matplotlib.pyplot' from 'c:\\Users\\hechr\\source\\hatch\\app\\.venv\\Lib\\site-packages\\matplotlib\\pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_6.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_7.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_8.png" | relative_url }})

#### Block Saturation

```
<module 'matplotlib.pyplot' from 'c:\\Users\\hechr\\source\\hatch\\app\\.venv\\Lib\\site-packages\\matplotlib\\pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_9.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_10.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_11.png" | relative_url }})

```
<module 'matplotlib.pyplot' from 'c:\\Users\\hechr\\source\\hatch\\app\\.venv\\Lib\\site-packages\\matplotlib\\pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_12.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_13.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_14.png" | relative_url }})

### vesus ECL

```
<module 'matplotlib.pyplot' from 'c:\\Users\\hechr\\source\\hatch\\app\\.venv\\Lib\\site-packages\\matplotlib\\pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_15.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_16.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_17.png" | relative_url }})

```
<module 'matplotlib.pyplot' from 'c:\\Users\\hechr\\source\\hatch\\app\\.venv\\Lib\\site-packages\\matplotlib\\pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_18.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_19.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_20.png" | relative_url }})

```
<module 'matplotlib.pyplot' from 'c:\\Users\\hechr\\source\\hatch\\app\\.venv\\Lib\\site-packages\\matplotlib\\pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_21.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_22.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_23.png" | relative_url }})

```
<module 'matplotlib.pyplot' from 'c:\\Users\\hechr\\source\\hatch\\app\\.venv\\Lib\\site-packages\\matplotlib\\pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_24.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_25.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_26.png" | relative_url }})

### Well property

#### Injector

```
<module 'matplotlib.pyplot' from 'c:\\Users\\hechr\\source\\hatch\\app\\.venv\\Lib\\site-packages\\matplotlib\\pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_27.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_28.png" | relative_url }})

#### Producer Corner

```
<module 'matplotlib.pyplot' from 'c:\\Users\\hechr\\source\\hatch\\app\\.venv\\Lib\\site-packages\\matplotlib\\pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_29.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_30.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_31.png" | relative_url }})

#### Producer Edge

```
<module 'matplotlib.pyplot' from 'c:\\Users\\hechr\\source\\hatch\\app\\.venv\\Lib\\site-packages\\matplotlib\\pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_32.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_33.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_34.png" | relative_url }})

# Buckley- Leverett



Two phase, isothermal problem

variable order: [Sw, P, T, So, X0, X1, Sg]



Acc w.r.t. [Sw, So, Sg, X0, X1, P, T]

```
Running simulation: Buckley-Leverett

    27   5.1762  0     10.000    1e-05              1.00            100.00                       1.00   21.729 0.000000 0.000000 0.000000



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  0.807s    98.80%

|- Newton                                 0.732s    90.64%

  |- Jacobian                             0.460s    62.84%

  |- Update                               0.225s    30.74%

  |- Solver                               0.020s     2.69%

  |- Logging                              0.009s     1.19%

  |- Residual                             0.008s     1.05%

|- Output                                 0.071s     8.75%

|- Input                                  0.000s     0.01%

Initialization                            0.010s     1.20%

------------------------------------------------------------

TOTAL                                     0.817s

============================================================



Time steps : 27/28, step size: 0.37, 1.10

```

```
CompletedProcess(args=['build/Release/simuapp.exe', '-f', 'c:\\Users\\hechr\\source\\hatch\\app/build/test/data//buckley.dat'], returncode=0, stdout='c:\\Users\\hechr\\source\\hatch\\app/build/test/data\\buckley.dat\n', stderr='\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1 2.33e-04 11 1  2.3e-04     1.00                                                           1.00    0.101 491.327015 0.333114 0.183359\n     2 1.27e-04  2    3.6e-04     1.00                                                           1.00    0.110 3.987489 0.083768 0.020148\n     3 1.91e-04  4    5.5e-04     1.00                                                           1.00    0.783 7.054601 0.133420 0.023883\n     4 2.35e-04  6    7.9e-04     1.00                                                           1.00    1.707 9.384579 0.135701 0.021840\n     5 2.88e-04  6      0.001     1.00                                                           1.00    2.584 10.889508 0.136546 0.021447\n     6 3.52e-04  8      0.001     1.00                                                           1.00    3.471 13.152204 0.150380 0.021553\n     7 4.11e-04  8      0.002     1.00                                                           1.00    4.381 15.154596 0.137443 0.021456\n     8 5.00e-04 10      0.002     1.00                                                           1.00    5.250 18.359504 0.146093 0.022177\n     9 5.91e-04 11      0.003     1.00                                                           1.00    6.079 21.717885 0.151451 0.022459\n    10 6.45e-04 12      0.004     1.00                                                           1.00    6.860 22.666504 0.156218 0.022709\n    11 6.45e-04 13      0.004     1.00                                                           1.00    7.655 21.882397 0.151006 0.021875\n    12 5.95e-04  5      0.005     0.90              0.11             11.20                       1.00    8.387 15.780928 0.129086 0.021802\n    13 7.46e-04  3      0.006     0.57              0.43             43.26                       1.00    8.981 33.811885 0.106498 0.037667\n    14 1.02e-03  2      0.007     0.34              0.66             65.75                       1.00    9.309 37.724984 0.066335 0.042300\n    15 1.65e-03  2      0.008     0.21              0.79             78.78                       1.00    9.234 37.323166 0.049593 0.046379\n    16 2.89e-03  2      0.011     0.13              0.87             87.10                       1.00    8.724 36.751092 0.043757 0.050197\n    17 5.22e-03  2      0.016     0.07              0.93             92.53                       1.00    7.693 34.427290 0.041264 0.050195\n    18 9.55e-03  3      0.026     0.04              0.96             95.98                       1.00    6.281 30.108641 0.040150 0.045920\n    19   0.0176  3      0.043     0.02              0.98             98.01                       1.00    4.493 24.185273 0.037400 0.039355\n    20   0.0328  3      0.076     0.01              0.99             99.09                       1.00    2.589 18.371340 0.032655 0.035285\n    21   0.0629  3      0.139     0.00              1.00             99.62                       1.00    0.999 13.313079 0.026729 0.009911\n    22   0.1246  3      0.264     0.00              1.00             99.86                       1.00    0.363 9.054179 0.019095 0.005920\n    23   0.2578  2      0.522    6e-04              1.00             99.94                       1.00    2.815 7.102084 0.019041 0.002453\n    24   0.5338  1      1.055    1e-04              1.00             99.99                       1.00   11.455 2.835932 0.012557 0.000837\n    25   1.1494  1      2.205    1e-05              1.00            100.00                       1.00   12.669 0.472871 0.003602 0.000240\n    26   2.6190  0      4.824    1e-05              1.00            100.00                       1.00   15.713 0.000000 0.000000 0.000000\n    27   5.1762  0     10.000    1e-05              1.00            100.00                       1.00   21.729 0.000000 0.000000 0.000000\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                  0.807s    98.80%\n|- Newton                                 0.732s    90.64%\n  |- Jacobian                             0.460s    62.84%\n  |- Update                               0.225s    30.74%\n  |- Solver                               0.020s     2.69%\n  |- Logging                              0.009s     1.19%\n  |- Residual                             0.008s     1.05%\n|- Output                                 0.071s     8.75%\n|- Input                                  0.000s     0.01%\nInitialization                            0.010s     1.20%\n------------------------------------------------------------\nTOTAL                                     0.817s\n============================================================\n\nTime steps : 27/28, step size: 0.37, 1.10\n')
```

### Load Benchmark

### Buckley Plot

![png]({{ "/assets/images/benchmark_image_35.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_36.png" | relative_url }})

# MISC

## spe04b_cw.dat

```
Running simulation: SPE4-b water flooding

    25  59.3982  1   3650.000     4.98             63.95             92.78                      67.50    0.494 0.665228 0.004121 0.001269



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  1.577s    99.00%

|- Newton                                 1.485s    94.12%

  |- Jacobian                             0.944s    63.59%

  |- Update                               0.432s    29.09%

  |- Solver                               0.086s     5.81%

  |- Residual                             0.009s     0.61%

  |- Logging                              0.005s     0.35%

|- Output                                 0.087s     5.49%

|- Input                                  0.000s     0.01%

Initialization                            0.016s     1.00%

------------------------------------------------------------

TOTAL                                     1.593s

============================================================



Time steps : 25/25, step size: 146.00, 153.32

```

```
CompletedProcess(args=['build/Release/simuapp.exe', '-f', 'c:\\Users\\hechr\\source\\hatch\\app/build/test/data//spe04b_cw.dat'], returncode=0, stdout='c:\\Users\\hechr\\source\\hatch\\app/build/test/data\\spe04b_cw.dat\n', stderr='\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1   1.0000  2      1.000    35.34              0.09              0.27                      67.50    0.001 100.263145 0.063591 0.157776\n     2   1.2338  1      2.234    28.03              0.11              0.40                      67.46    0.012 42.096413 0.044286 0.061044\n     3   2.0949  2      4.329    23.39              0.11              0.48                      67.50    0.012 42.175591 0.038504 0.071270\n     4   3.5553  1      7.884    20.26              0.11              0.54                      67.47    0.024 37.098757 0.060908 0.062022\n     5   5.8999  2     13.784    17.96              0.10              0.58                      67.50    0.030 32.478809 0.060470 0.054841\n     6   9.8112  2     23.595    16.46              0.10              0.60                      67.50    0.035 25.573755 0.052714 0.049457\n     7  16.9397  2     40.535    16.18              0.09              0.58                      67.50    0.058 25.077194 0.061387 0.044670\n     8  28.0476  2     68.582    17.70              0.09              0.51                      67.51    0.079 23.768911 0.084876 0.040384\n     9  41.7951  3    110.377    20.77              0.78              3.61                      67.51    0.091 21.404664 0.077297 0.040143\n    10  64.3575  4    174.735    23.33              5.45             18.94                      67.50    0.091 23.502108 0.071407 0.038712\n    11 101.7365  4    276.471    24.51             16.92             40.84                      67.50    0.094 24.115204 0.062416 0.041455\n    12 167.6324  4    444.104    22.78             33.99             59.88                      67.50    0.095 20.179682 0.067518 0.041410\n    13 269.7312  4    713.835    19.03             50.28             72.54                      67.50    0.097 14.608424 0.058477 0.055293\n    14 365.0000  2   1078.835    14.89             59.04             79.86                      67.50    0.097 22.183385 0.051403 0.060437\n    15  16.1649  1   1095.000    14.72             59.39             80.14                      67.50    0.097 0.984608 0.002007 0.002640\n    16  37.2201  1   1132.220    14.34             60.08             80.73                      67.50    0.098 2.265853 0.004656 0.005915\n    17  84.2322  1   1216.452    13.53             61.05             81.85                      67.50    0.105 5.027470 0.010094 0.012759\n    18 184.1495  1   1400.602    12.03             61.83             83.71                      67.50    0.150 9.889459 0.022776 0.023773\n    19 365.0000  1   1765.602     9.87             62.41             86.35                      67.50    0.360 15.310750 0.041078 0.033995\n    20 365.0000  1   2130.602     8.32             62.47             88.25                      67.50    0.530 11.105741 0.047668 0.023644\n    21 365.0000  1   2495.602     7.20             63.87             89.87                      67.50    0.443 8.562003 0.049829 0.017612\n    22 365.0000  2   2860.602     6.30             63.54             90.97                      67.50    0.439 6.731390 0.035898 0.013198\n    23 365.0000  1   3225.602     5.62             63.97             91.93                      67.50    0.436 5.652237 0.027554 0.010609\n    24 365.0000  1   3590.602     5.06             63.82             92.66                      67.50    0.494 4.670956 0.031940 0.008586\n    25  59.3982  1   3650.000     4.98             63.95             92.78                      67.50    0.494 0.665228 0.004121 0.001269\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                  1.577s    99.00%\n|- Newton                                 1.485s    94.12%\n  |- Jacobian                             0.944s    63.59%\n  |- Update                               0.432s    29.09%\n  |- Solver                               0.086s     5.81%\n  |- Residual                             0.009s     0.61%\n  |- Logging                              0.005s     0.35%\n|- Output                                 0.087s     5.49%\n|- Input                                  0.000s     0.01%\nInitialization                            0.016s     1.00%\n------------------------------------------------------------\nTOTAL                                     1.593s\n============================================================\n\nTime steps : 25/25, step size: 146.00, 153.32\n')
```



## watfld_cw.dat

```
Running simulation: SPE4-b Water flooding without vmod

    38 268.1457  1   3650.000     6.59            496.55             98.69                     503.18    1.678 2.339230 0.023797 0.004597



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  1.873s    99.13%

|- Newton                                 1.735s    92.66%

  |- Jacobian                             1.050s    60.53%

  |- Update                               0.536s    30.88%

  |- Solver                               0.123s     7.07%

  |- Residual                             0.011s     0.64%

  |- Logging                              0.006s     0.35%

|- Output                                 0.128s     6.82%

|- Input                                  0.000s     0.01%

Initialization                            0.017s     0.87%

------------------------------------------------------------

TOTAL                                     1.889s

============================================================



Time steps : 38/38, step size: 96.05, 134.12

```

```
CompletedProcess(args=['build/Release/simuapp.exe', '-f', 'c:\\Users\\hechr\\source\\hatch\\app/build/test/data//watfld_cw.dat'], returncode=0, stdout='c:\\Users\\hechr\\source\\hatch\\app/build/test/data\\watfld_cw.dat\n', stderr='\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1   1.0000  1      1.000   201.19             7e-07             3e-07                     503.18    0.294 54.389200 0.000747 0.083690\n     2   1.1667  1      2.167   195.66              0.01              0.00                     503.18    0.584 54.389200 0.022810 0.082827\n     3   1.3611  5      3.528   172.48              0.03              0.02                     495.70    0.638 271.946000 0.083905 0.388665\n     4   0.5293  2      4.057   169.02              0.03              0.02                     503.18    0.637 65.595135 0.024844 0.105840\n     5   0.5599  1      4.617   172.41              0.03              0.02                     503.16    0.635 47.232295 0.021645 0.076810\n     6   0.6992  1      5.316   179.86              0.02              0.01                     503.18    0.679 34.974126 0.022321 0.057284\n     7   0.9929  1      6.309   192.15              0.02              0.01                     503.20    0.675 36.036415 0.025479 0.060012\n     8   1.3935  1      7.703   209.75              0.01              0.01                     503.17    0.671 44.109744 0.038768 0.074024\n     9   1.7955  1      9.498   231.69              0.00              0.00                     503.21    0.806 31.422343 0.031550 0.058458\n    10   2.6553  1     12.153   259.67             4e-07             1e-07                     503.17    0.798 40.807431 0.051164 0.069432\n    11   3.5399  2     15.693   292.73                                                         503.19    0.790 40.441429 0.046394 0.073317\n    12   4.7373  1     20.431   328.37                                                         503.18    0.868 43.751522 0.060417 0.073546\n    13   6.1259  2     26.556   367.79                                                         503.20    0.962 47.383682 0.067927 0.087202\n    14   7.6388  3     34.195   401.95                                                         503.19    0.945 40.049983 0.063731 0.067537\n    15  10.2651  2     44.460   391.92             24.31              5.84                     503.08    0.875 57.019791 0.072106 0.096436\n    16  11.6932  2     56.154   339.59            112.10             24.82                     503.18    0.866 42.319039 0.050369 0.092954\n    17  15.3447  1     71.498   283.27            304.47             51.80                     503.18    0.709 37.859836 0.060953 0.095087\n    18  21.1099  2     92.608   236.51            318.94             57.42                     503.19    0.727 64.841175 0.064754 0.193961\n    19  22.4693  2    115.078   189.10            367.64             66.03                     503.19    0.730 61.222365 0.037253 0.161614\n    20  24.6648  1    139.742   153.85            403.06             72.37                     503.18    0.791 54.063711 0.039700 0.146010\n    21  28.8620  1    168.604   123.87            410.22             76.81                     503.17    0.839 51.474680 0.032113 0.131685\n    22  34.5994  1    203.204   100.53            425.87             80.90                     503.18    0.876 41.155758 0.032201 0.113702\n    23  45.9569  1    249.161    80.84            432.83             84.26                     503.18    0.922 38.286511 0.033709 0.107904\n    24  62.9324  1    312.093    64.29            447.05             87.43                     503.19    0.991 32.898971 0.047921 0.098507\n    25  91.4973  1    403.590    49.95            455.33             90.11                     503.18    1.101 32.390863 0.066735 0.096988\n    26 133.8068  1    537.397    37.85            462.38             92.43                     503.18    1.384 29.168511 0.060122 0.072431\n    27 203.2269  2    740.624    28.18            477.57             94.43                     503.19    1.348 24.510696 0.064448 0.055388\n    28 326.8844  2   1067.508    20.27            484.68             95.99                     503.19    1.288 24.142130 0.072743 0.045353\n    29  27.4915  1   1095.000    19.71            484.85             96.09                     503.18    1.286 1.915673 0.005180 0.003618\n    30  61.9645  1   1156.964    18.60            485.45             96.31                     503.19    1.293 3.788610 0.012611 0.007079\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31 133.3705  1   1290.335    16.71            486.51             96.68                     503.18    1.340 6.561598 0.025146 0.013182\n    32 266.5193  1   1556.854    14.12            487.61             97.19                     503.19    1.570 9.282289 0.052584 0.019256\n    33 365.0000  2   1921.854    11.83            491.93             97.65                     503.19    1.532 8.228473 0.068380 0.018876\n    34 365.0000  1   2286.854    10.18            493.10             97.98                     503.19    1.570 6.492720 0.055396 0.013377\n    35 365.0000  1   2651.854     8.93            494.33             98.23                     503.18    1.599 5.124817 0.050491 0.009844\n    36 365.0000  1   3016.854     7.93            495.22             98.42                     503.18    1.634 4.302440 0.048077 0.008089\n    37 365.0000  1   3381.854     7.11            496.05             98.59                     503.18    1.661 3.614400 0.032463 0.006996\n    38 268.1457  1   3650.000     6.59            496.55             98.69                     503.18    1.678 2.339230 0.023797 0.004597\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                  1.873s    99.13%\n|- Newton                                 1.735s    92.66%\n  |- Jacobian                             1.050s    60.53%\n  |- Update                               0.536s    30.88%\n  |- Solver                               0.123s     7.07%\n  |- Residual                             0.011s     0.64%\n  |- Logging                              0.006s     0.35%\n|- Output                                 0.128s     6.82%\n|- Input                                  0.000s     0.01%\nInitialization                            0.017s     0.87%\n------------------------------------------------------------\nTOTAL                                     1.889s\n============================================================\n\nTime steps : 38/38, step size: 96.05, 134.12\n')
```

## stflu001.dat

Inverted 9 spot water flooding with area/block modifier, 5 point transmissibility


```
Running simulation: Inverted 9 spot water flooding

   165   9.2472  6   3650.000    15.59            872.82             98.25                     881.28   98.766 18.007891 0.166827 7.053193



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  4.778s    99.79%

|- Newton                                 4.329s    90.60%

  |- Jacobian                             3.008s    69.49%

  |- Update                               1.078s    24.90%

  |- Solver                               0.154s     3.55%

  |- Logging                              0.033s     0.75%

  |- Residual                             0.025s     0.57%

|- Output                                 0.420s     8.79%

|- Input                                  0.000s     0.00%

Initialization                            0.010s     0.21%

------------------------------------------------------------

TOTAL                                     4.788s

============================================================



Time steps : 165/166, step size: 22.12, 71.15

```

```
CompletedProcess(args=['build/Release/simuapp.exe', '-f', 'c:\\Users\\hechr\\source\\hatch\\app/build/test/data//stflu001.dat'], returncode=0, stdout='c:\\Users\\hechr\\source\\hatch\\app/build/test/data\\stflu001.dat\n', stderr='\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1   1.0000  1      1.000     3.96             3e-07             6e-06                       0.16    0.007 6.646716 0.000026 0.643545\n     2   2.2343  1      3.234     3.41              0.03              0.93                       0.17    0.007 7.499932 0.002064 1.370125\n     3   4.9652  1      8.200     2.93              0.05              1.71                       0.17    0.007 6.612593 0.005469 3.026815\n     4  10.7201  1     18.920     2.59              0.06              2.14                       0.20    0.008 6.373297 0.013305 6.781809\n     5  21.1828  1     40.102     2.36              0.06              2.30                       0.26    0.016 4.597040 0.020566 15.681151\n     6  34.8524  2     74.955     2.19              0.05              2.36                       0.55    0.022 4.552576 0.053252 50.441722\n     7  34.6774  3    109.632     2.15              0.05              2.34                       2.83    0.759 14.899723 0.077917 121.500000\n     8  19.0835  7    128.716     2.21              0.05              2.08                      16.27    0.813 81.217025 0.321598 173.100506\n     9   2.6429 11 1  131.359     2.26              0.04              1.95                     426.22    0.943 401.700162 0.277476 270.165969\n    10   0.7516  2    132.110     2.28              0.04              1.90                     462.83    1.372 66.213502 0.065026 81.000000\n    11   0.5550  2    132.665     2.30              0.04              1.85                     429.54    1.434 83.535294 0.210085 62.519423\n    12   0.4855  2    133.151     2.32              0.04              1.80                     410.03    1.478 64.175109 0.195262 39.329471\n    13   0.4922  1    133.643     2.34              0.04              1.74                     419.36    1.522 54.332243 0.040122 34.384937\n    14   0.5991  1    134.242     2.38              0.04              1.64                     427.57    1.772 54.389200 0.031317 37.623099\n    15   0.6978  2    134.940     2.45              0.04              1.47                     414.75    1.825 58.059365 0.145210 51.756010\n    16   0.6841  1    135.624     2.53              0.03              1.31                     426.90    2.374 45.123560 0.044478 40.500000\n    17   0.7674  1    136.391     2.64              0.03              1.24                     438.51    3.070 46.676230 0.032060 40.500000\n    18   0.8609  1    137.252     2.80              0.03              1.13                     447.27    3.866 49.519178 0.028371 40.500000\n    19   0.9657  2    138.218     3.10              0.03              0.97                     408.53    4.466 66.071256 0.188490 50.606987\n    20   0.9591  2    139.177     3.56              0.03              0.74                     413.68    4.512 61.577960 0.059462 61.530988\n    21   0.8474  1    140.025     4.00              0.02              0.55                     430.73    5.132 47.221534 0.026354 40.500000\n    22   0.9506  2    140.975     4.69              0.02              0.39                     442.01    5.141 58.228329 0.024737 59.420578\n    23   0.8582  1    141.833     5.27              0.02              0.34                     459.65    5.973 42.760150 0.013885 40.500000\n    24   0.9628  1    142.796     6.06              0.02              0.28                     473.01    6.715 45.007265 0.020194 40.500000\n    25   1.0800  3    143.876     7.72              0.02              0.20                     476.21    6.685 53.008927 0.190454 58.811913\n    26   0.9812  2    144.857     9.55              0.01              0.13                     461.20    6.713 51.542439 0.151593 55.619825\n    27   0.9220  1    145.779    11.18              0.13              1.15                     471.31    7.114 49.206396 0.087890 40.500000\n    28   1.0343  2    146.814    12.61              1.41             10.07                     449.00    7.277 66.781935 0.208852 52.377665\n    29   1.0069  2    147.821    13.82              6.78             32.91                     451.99    7.306 61.680063 0.030358 42.898213\n    30   1.0959  1    148.916    14.88             12.47             45.60                     454.79    7.760 54.389200 0.017857 35.520826\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31   1.3132  3    150.230    16.49             18.78             53.24                     445.26    7.739 63.335849 0.181264 49.925308\n    32   1.3143  2    151.544    18.32             24.44             57.17                     441.62    7.772 55.474761 0.067775 44.146788\n    33   1.4085  1    152.952    20.47             29.70             59.20                     438.79    8.026 54.389200 0.031002 40.122370\n    34   1.5877  1    154.540    23.16             35.48             60.51                     434.59    8.575 54.389200 0.023186 36.244435\n    35   1.8839  2    156.424    28.46             44.41             60.94                     389.47    8.582 68.723003 0.170226 50.200939\n    36   1.8796  2    158.304    36.14             59.31             62.14                     378.00    8.660 60.443755 0.079793 48.291975\n    37   1.9170  1    160.221    46.93             83.65             64.06                     377.67    9.290 54.389200 0.028851 40.296418\n    38   2.1561  3    162.377   101.16            176.05             63.51                     359.86    9.340 74.556366 0.166068 77.059046\n    39   1.6468  3    164.023   146.39            349.78             70.50                     368.98    9.503 128.492669 0.154562 93.372386\n    40   1.1011  2    165.125   151.64            402.81             72.65                     383.64    9.706 69.660612 0.039143 58.430297\n    41   1.0043  1    166.129   152.74            425.20             73.57                     398.49    9.928 40.434386 0.016985 40.500000\n    42   1.1266  3    167.255   144.73            313.63             68.42                     403.19    9.981 122.976030 0.161717 26.743478\n    43   1.2650  1    168.520   131.48            350.36             72.71                     411.23   10.076 25.598692 0.016480 27.160226\n    44   1.7118  1    170.232   140.65            412.50             74.57                     427.03   10.196 30.710618 0.017474 40.500000\n    45   1.9203  4    172.152   296.58            792.04             72.76                     477.14   10.351 126.101826 0.226932 126.622639\n    46   1.0238  3    173.176   374.53           1014.63             73.04                     515.68   10.657 113.887682 0.201902 121.500000\n    47   0.5634  5    173.740   356.67            659.81             64.91                     513.86   10.825 102.806634 0.179478 37.010838\n    48   0.5985  1    174.338   271.16            684.50             71.63                     518.77   10.892 30.215940 0.050020 11.587243\n    49   1.0473  1    175.385   217.71            690.77             76.04                     536.84   10.992 27.497888 0.026955 20.138896\n    50   1.5898  1    176.975   183.57            695.97             79.13                     561.97   11.135 24.380626 0.018643 31.195484\n    51   2.0250  2    179.000   161.79            696.53             81.15                     580.15   11.324 23.962521 0.135165 37.109811\n    52   2.3748  1    181.375   148.99            692.43             82.29                     598.78   11.553 22.957658 0.065123 40.500000\n    53   2.6641  2    184.039   141.50            702.11             83.23                     602.41   11.770 16.973602 0.209292 52.156499\n    54   2.5952  2    186.634   137.78            695.05             83.46                     620.56   11.992 25.061917 0.040330 49.918886\n    55   2.5976  8    189.232   150.04            692.72             82.20                     627.70   12.013 18.848864 0.157275 76.092515\n    56   2.0009  3    191.233   142.43            687.30             82.83                     635.93   12.228 14.843308 0.088159 81.038855\n    57   1.4770  1    192.710   135.90            689.50             83.54                     640.51   12.631 7.733858 0.029912 40.500000\n    58   1.6569  1    194.367   129.02            691.25             84.27                     645.27   13.008 5.947743 0.026454 40.500000\n    59   1.8587  2    196.225   127.82            680.37             84.18                     637.08   13.110 34.004605 0.171494 30.751360\n    60   2.0235  1    198.249   115.43            680.93             85.51                     641.18   13.249 14.553604 0.037312 32.476738\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    61   2.5302  2    200.779   115.77            685.38             85.55                     640.32   13.409 26.067586 0.149240 49.612927\n    62   2.5414  2    203.321   116.35            696.50             85.69                     643.84   13.591 23.517000 0.084526 64.654843\n    63   2.1769  2    205.497   116.60            703.11             85.77                     651.46   13.777 25.019982 0.036950 57.802476\n    64   1.9986  1    207.496   121.08            714.34             85.51                     658.32   14.070 33.533068 0.017928 40.500000\n    65   2.2421  2    209.738   128.16            749.12             85.39                     668.23   14.346 57.013596 0.041503 81.000000\n    66   1.6555  4    211.394   132.58            717.01             84.40                     670.06   14.475 43.239193 0.165632 62.108525\n    67   1.4543  2    212.848   118.77            708.76             85.65                     672.26   14.575 11.744486 0.079671 23.955146\n    68   2.0706  1    214.919   110.25            705.54             86.49                     678.03   14.611 12.615739 0.056272 39.313635\n    69   2.3587  1    217.277   107.08            705.24             86.82                     684.71   14.766 9.877400 0.031795 40.500000\n    70   2.6459  1    219.923   106.89            708.75             86.89                     691.01   15.062 9.633803 0.025100 40.500000\n    71   2.9682  3    222.891   130.35            749.63             85.19                     696.31   15.100 30.499874 0.188766 94.119043\n    72   1.9733  3    224.865   164.21            887.77             84.39                     713.76   15.202 85.201319 0.137446 116.271981\n    73   1.1228  5    225.987   175.61            798.69             81.98                     713.91   15.331 57.792375 0.192454 78.692460\n    74   0.8456  2    226.833   138.07            800.15             85.28                     715.48   15.423 17.706090 0.086708 9.973737\n    75   1.2503  2    228.083   111.29            796.27             87.74                     720.85   15.497 14.764817 0.037054 13.544212\n    76   2.1432  1    230.226    92.76            790.63             89.50                     729.86   15.580 12.913434 0.024559 21.705119\n    77   3.1675  2    233.394    80.89            794.82             90.76                     736.80   15.712 11.044160 0.137075 42.605656\n    78   3.4598  2    236.854    74.80            785.72             91.31                     744.07   15.902 12.776671 0.073719 51.169744\n    79   3.4142  1    240.268    71.97            778.36             91.54                     749.52   16.141 11.764318 0.030393 40.500000\n    80   3.8300  1    244.098    70.25            772.14             91.66                     754.38   16.415 10.200660 0.019922 40.500000\n    81   4.2965  2    248.394    68.33            767.90             91.83                     757.98   16.520 18.101597 0.162007 49.954078\n    82   4.2988  2    252.693    67.32            765.56             91.92                     761.88   16.649 13.396110 0.177567 55.280933\n    83   4.0541  2    256.747    67.31            765.10             91.91                     765.04   16.765 11.358490 0.168068 52.521133\n    84   3.9405  4    260.688    74.29            772.50             91.23                     765.95   16.831 13.407376 0.165825 55.860094\n    85   3.6932  2    264.381    80.19            784.17             90.72                     761.64   16.966 9.036559 0.130726 80.902055\n    86   2.7293  2    267.110    82.23            783.72             90.50                     760.79   17.128 8.333674 0.079799 65.778303\n    87   2.3123  3    269.423    83.45            779.17             90.33                     761.67   17.234 13.840605 0.112857 66.425935\n    88   1.9469  3    271.370    85.16            779.25             90.15                     760.62   17.338 16.059592 0.139287 46.295577\n    89   2.0329  2    273.402    79.10            780.90             90.80                     759.77   17.440 7.465083 0.108583 22.435597\n    90   2.7516  1    276.154    68.42            781.29             91.95                     762.62   17.549 7.068989 0.042212 28.046801\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    91   3.6732  1    279.827    61.28            776.16             92.68                     767.90   17.735 6.753611 0.023208 40.500000\n    92   4.1206  2    283.948    57.20            775.73             93.13                     770.56   17.889 21.000676 0.182612 53.591793\n    93   3.9581  6    287.906    54.97            774.42             93.37                     773.42   18.080 14.138332 0.103389 50.125015\n    94   3.9525  6    291.858    54.10            773.77             93.47                     776.35   18.238 8.563509 0.053195 45.774972\n    95   4.1530  6    296.011    53.87            776.22             93.51                     778.05   18.387 7.197534 0.114486 56.153206\n    96   3.8801  6    299.892    53.44            774.63             93.55                     779.77   18.558 5.088794 0.120094 62.503664\n    97   3.3950  1    303.287    53.19            773.76             93.57                     781.05   18.940 3.675724 0.085283 40.500000\n    98   3.8085  6    307.095    53.21            773.49             93.56                     781.92   19.035 7.327462 0.124167 54.258875\n    99   3.6317  6    310.727    53.82            781.77             93.56                     779.07   19.188 14.934027 0.165272 34.072826\n   100   4.0318  6    314.759    54.94            790.58             93.50                     778.28   19.323 10.694864 0.110143 43.457289\n   101   4.3576  6    319.116    58.02            798.64             93.23                     777.36   19.495 14.410960 0.123603 51.130797\n   102   4.3020  6    323.418    60.70            795.17             92.91                     779.24   19.686 7.154592 0.061989 62.341579\n   103   3.7702  6    327.188    62.07            790.61             92.72                     782.33   19.877 9.357432 0.030012 62.481761\n   104   3.2995  1    330.488    62.54            791.06             92.67                     784.41   20.319 8.123598 0.013702 40.500000\n   105   3.7014  6    334.189    70.42            797.89             91.89                     784.84   20.427 26.230136 0.184642 68.648282\n   106   3.0511  2    337.240    77.87            821.40             91.34                     785.11   20.655 73.168332 0.131914 78.955518\n   107   2.2925  2    339.533    78.50            833.51             91.39                     788.01   20.804 50.662123 0.046490 67.831989\n   108   1.9044  3    341.437    76.04            810.39             91.42                     789.54   20.901 67.540252 0.150489 25.770458\n   109   2.2182  1    343.656    69.44            813.50             92.14                     790.21   20.957 12.411136 0.092840 28.358622\n   110   2.9471  1    346.603    66.22            816.03             92.49                     792.91   21.035 8.110116 0.038108 40.500000\n   111   3.3060  1    349.909    64.98            815.69             92.62                     795.91   21.229 6.231376 0.033843 40.500000\n   112   3.7087  3    353.617    66.26            821.51             92.54                     797.05   21.302 13.170803 0.164965 75.954366\n   113   2.8603  3    356.478    67.57            827.72             92.45                     797.27   21.472 8.510583 0.124014 41.942992\n   114   3.1504  4    359.628    70.72            832.14             92.17                     798.26   21.559 14.236714 0.137011 47.019768\n   115   3.2614  2    362.889    79.23            849.18             91.47                     802.06   21.680 16.982982 0.081940 65.317977\n   116   2.7755  7    365.665   121.51            940.45             88.56                     810.86   21.850 121.339781 0.207121 159.979681\n   117   1.2298  3    366.895   108.37            893.02             89.18                     813.61   22.065 38.957078 0.180829 43.297900\n   118   1.3011  2    368.196    93.11            895.04             90.58                     815.31   22.148 25.833740 0.117451 39.396349\n   119   1.4805  3    369.676    84.57            888.23             91.31                     817.57   22.235 31.633471 0.122152 25.711241\n   120   1.9040  1    371.580    73.80            886.60             92.32                     820.84   22.317 9.048183 0.078383 21.476226\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n   121   2.8248  1    374.405    65.84            876.09             93.01                     826.06   22.412 15.541947 0.034422 33.215449\n   122   3.4953  1    377.900    61.80            872.73             93.39                     831.67   22.537 11.199816 0.025839 40.500000\n   123   3.9210  1    381.821    59.81            877.99             93.62                     836.51   22.711 7.618475 0.022591 40.500000\n   124   4.3985  5    386.220    66.90            898.38             93.07                     840.49   22.894 30.930014 0.226883 99.705227\n   125   2.8051  5    389.025    73.69            891.05             92.36                     842.36   23.156 24.596714 0.152084 88.521574\n   126   1.9476  2    390.973    63.60            877.07             93.24                     843.25   23.332 26.525652 0.139017 40.686667\n   127   2.1796  3    393.152    53.34            877.67             94.27                     844.78   23.460 12.111983 0.125086 13.182206\n   128   2.7732  2    395.925    44.71            879.58             95.16                     846.22   23.608 7.656144 0.115267 6.581170\n   129   3.6590  1    399.584    37.65            881.74             95.90                     848.37   23.786 5.762334 0.056737 9.840349\n   130   6.1947  1    405.779    31.04            878.13             96.59                     852.37   23.972 6.444935 0.051883 27.240202\n   131   8.3725  2    414.152    26.06            871.49             97.10                     856.72   24.272 6.622972 0.042024 47.197002\n   132   8.6495  1    422.801    23.87            868.54             97.33                     859.13   24.646 3.477831 0.018359 40.500000\n   133   9.7030  1    432.504    22.54            866.50             97.47                     861.01   25.046 3.166937 0.017726 40.500000\n   134  10.8848  1    443.389    21.73            866.88             97.55                     862.39   25.496 2.319306 0.019997 40.500000\n   135  12.2105  4    455.599    21.54            866.74             97.58                     862.76   25.833 7.347430 0.213272 97.104546\n   136   7.9375  3    463.537    22.66            865.74             97.45                     862.61   26.321 5.919742 0.127888 63.873156\n   137   6.8512  3    470.388    23.02            868.71             97.42                     862.13   26.588 7.035081 0.140301 105.932121\n   138   4.1795  2    474.568    21.77            870.15             97.56                     862.44   26.881 3.705468 0.043054 73.260207\n   139   3.3018  2    477.869    21.48            867.76             97.58                     862.43   27.048 11.053308 0.182620 21.528806\n   140   3.4743  2    481.344    19.95            873.04             97.77                     861.84   27.174 6.994524 0.099187 22.383557\n   141   4.8799  1    486.224    17.94            877.36             98.00                     861.84   27.289 3.129526 0.068844 32.541850\n   142   6.0963  2    492.320    16.24            876.32             98.18                     863.06   27.470 3.356028 0.051568 50.302789\n   143   6.0752  1    498.395    15.18            875.15             98.29                     864.06   27.692 3.033857 0.029700 40.500000\n   144   6.8152  1    505.210    14.28            874.20             98.39                     865.15   27.907 2.121422 0.020372 40.500000\n   145   7.6452  3    512.856    13.72            875.61             98.46                     865.35   28.149 6.507451 0.188230 31.135029\n   146   7.9113  1    520.767    12.36            877.28             98.61                     865.89   28.429 1.864606 0.074726 35.872755\n   147   9.4345  1    530.201    10.50            878.78             98.82                     867.28   28.702 3.541085 0.041884 40.500000\n   148  10.5836  3    540.785     8.98            880.82             98.99                     868.79   29.068 2.989671 0.121511 12.353423\n   149  13.6431  2    554.428     7.27            881.88             99.18                     870.51   29.444 2.525564 0.086953 1.044650\n   150  20.1521  3    574.580     5.50            881.36             99.38                     872.42   29.843 2.790033 0.052828 0.854775\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n   151  34.7743  5    609.355     3.77            882.24             99.57                     874.96   30.307 2.891669 0.057836 0.928513\n   152  58.5606  6    667.915     2.60            883.28             99.71                     877.14   30.953 3.122679 0.105543 1.380017\n   153  80.2064  6    748.121     1.99            883.80             99.78                     878.34   31.991 2.645886 0.107142 1.183211\n   154 109.1700  6    857.291     1.28            885.68             99.86                     880.28   33.239 1.414170 0.112185 0.637826\n   155 145.7349  6   1003.026    13.57            826.54             98.38                     880.64   45.353 1.035063 0.159245 0.440912\n   156  91.9736  6   1095.000    26.73            820.31             96.84                     879.44   52.132 7.637938 0.045846 3.161523\n   157 164.3680  6   1259.368    42.74            809.77             94.99                     878.89   76.115 4.461185 0.099166 1.805904\n   158 230.8850  6   1490.253    56.97            802.69             93.37                     878.53   91.780 3.366397 0.098264 1.343633\n   159 325.4999  6   1815.753    66.62            800.54             92.32                     878.47   94.853 2.529747 0.125277 0.999281\n   160 365.0000  6   2180.753    79.69            779.56             90.73                     878.64   96.651 1.876030 0.111068 0.735377\n   161 365.0000  6   2545.753    93.80            764.41             89.07                     878.50   97.611 2.616659 0.064998 1.176044\n   162 365.0000  6   2910.753    99.31            764.49             88.50                     878.10   98.144 3.409564 0.031684 1.513262\n   163 365.0000  6   3275.753   105.70            767.11             87.89                     877.74   98.479 3.754803 0.037417 1.642540\n   164 365.0000  6   3640.753   116.74            764.83             86.76                     877.58   98.719 3.053769 0.043095 1.317969\n   165   9.2472  6   3650.000    15.59            872.82             98.25                     881.28   98.766 18.007891 0.166827 7.053193\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                  4.778s    99.79%\n|- Newton                                 4.329s    90.60%\n  |- Jacobian                             3.008s    69.49%\n  |- Update                               1.078s    24.90%\n  |- Solver                               0.154s     3.55%\n  |- Logging                              0.033s     0.75%\n  |- Residual                             0.025s     0.57%\n|- Output                                 0.420s     8.79%\n|- Input                                  0.000s     0.00%\nInitialization                            0.010s     0.21%\n------------------------------------------------------------\nTOTAL                                     4.788s\n============================================================\n\nTime steps : 165/166, step size: 22.12, 71.15\n')
```

## stflu002.dat

5000x5000x50, 2D diagonal water flooding in uniformed cartesian

```
Running simulation: Uniformed cartesian water flooding

    50 169.2914  2   3650.000  3928.77             71.23              1.78                    3999.18    6.011 81.415280 0.025572 0.026018



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  0.932s    98.98%

|- Newton                                 0.805s    86.35%

  |- Jacobian                             0.518s    64.31%

  |- Update                               0.229s    28.45%

  |- Solver                               0.033s     4.16%

  |- Logging                              0.009s     1.11%

  |- Residual                             0.007s     0.89%

|- Output                                 0.115s    12.35%

|- Input                                  0.000s     0.02%

Initialization                            0.010s     1.02%

------------------------------------------------------------

TOTAL                                     0.942s

============================================================



Time steps : 50/50, step size: 73.00, 127.39

```

```
CompletedProcess(args=['build/Release/simuapp.exe', '-f', 'c:\\Users\\hechr\\source\\hatch\\app/build/test/data//stflu002.dat'], returncode=0, stdout='c:\\Users\\hechr\\source\\hatch\\app/build/test/data\\stflu002.dat\n', stderr='unknown keyword: mxcnrpt\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1 1.00e-05  1    1.0e-05  4000.00                                                        4000.00    0.000 0.011954 0.000000 0.000004\n     2 2.33e-05  1    3.3e-05  4000.00                                                        4000.00    0.000 0.027889 0.000000 0.000010\n     3 5.44e-05  1    8.8e-05  4000.00                                                        4000.00    0.000 0.065057 0.000000 0.000022\n     4 1.27e-04  1    2.1e-04  4000.00                                                        4000.00    0.000 0.151708 0.000001 0.000052\n     5 2.96e-04  1    5.1e-04  4000.00                                                        4000.00    0.000 0.353488 0.000002 0.000122\n     6 6.89e-04  1      0.001  4000.00                                                        4000.00    0.000 0.822106 0.000004 0.000283\n     7 1.60e-03  1      0.003  4000.00                                                        4000.00    0.000 1.903705 0.000010 0.000656\n     8 3.68e-03  1      0.006  4000.00                                                        4000.00    0.000 4.364780 0.000022 0.001505\n     9 8.35e-03  2      0.015  4000.00                                                        4000.00    0.000 9.787885 0.000050 0.003374\n    10   0.0183  2      0.033  4000.00                                                        4000.00    0.000 20.935862 0.000110 0.007218\n    11   0.0375  2      0.071  4000.00                                                        4000.00    0.000 40.898954 0.000224 0.014100\n    12   0.0687  2      0.139  4000.00                                                        3999.74    0.000 69.122013 0.000411 0.023828\n    13   0.1097  2      0.249  4000.00                                                        3998.09    0.000 97.886905 0.000656 0.033741\n    14   0.1549  1      0.404  4000.00                                                        3998.00   20.743 54.389200 0.000425 0.018745\n    15   0.2652  4      0.669  4000.00                                                        3997.89   12.522 175.231175 0.001582 0.060169\n    16   0.2854  1      0.954  4000.00                                                        4000.01   27.895 54.389200 0.000613 0.018638\n    17   0.4887  4      1.443  4000.00                                                        4004.14   18.446 217.440687 0.002901 0.074455\n    18   0.4655  3      1.909  4000.00                                                        4001.07   13.946 158.622403 0.002746 0.054333\n    19   0.5279  2      2.437  4000.00                                                        4003.58   15.887 108.778400 0.002387 0.037267\n    20   0.7140  2      3.151  4000.00                                                        4000.46   19.037 108.778400 0.002917 0.037145\n    21   0.9657  3      4.116  4000.00                                                        4000.37   15.410 163.167600 0.005368 0.055502\n    22   1.0793  3      5.196  4000.00                                                        3999.25   12.202 146.761073 0.006143 0.049608\n    23   1.2730  3      6.469  4000.00                                                        3999.95    9.800 135.188197 0.007136 0.045319\n    24   1.5622  3      8.031  4000.00                                                        3999.88    7.892 130.652828 0.008602 0.043341\n    25   1.9483  3      9.979  4000.00                                                        3999.78    6.347 128.552005 0.010502 0.042075\n    26   2.4480  3     12.427  4000.00                                                        3999.64    5.086 126.959569 0.012864 0.040885\n    27   3.0936  3     15.521  4000.00                                                        4000.10    4.076 124.554155 0.015757 0.040573\n    28   3.9437  3     19.464  4000.00                                                        4000.18    3.257 120.307430 0.019365 0.039392\n    29   5.1063  3     24.571  4000.00                                                        4000.01    2.579 112.978123 0.023773 0.037147\n    30   6.7961  2     31.367  4000.00                                                        3999.89    2.017 101.428430 0.029693 0.032798\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31   9.4605  2     40.827  4000.00                                                        3999.93    1.555 84.717985 0.038302 0.027152\n    32  14.1070  2     54.934  4000.00                                                        3999.99    1.156 62.967388 0.051002 0.022054\n    33  23.1840  1     78.118  4000.00                                                        4018.39    2.105 54.389200 0.068181 0.037701\n    34  37.1912  2    115.309  4000.00             3e-14                                      3998.61    1.433 92.398243 0.093387 0.065783\n    35  53.4823  3    168.792  4000.00             1e-11             3e-13                    4001.78    0.959 119.092974 0.104353 0.091295\n    36  69.5627  4    238.354  4000.00             1e-09             3e-11                    3998.62    0.679 125.511246 0.100358 0.105298\n    37  88.3700  3    326.724  4000.00             6e-08             1e-09                    4000.42    0.495 113.943402 0.092303 0.106546\n    38  38.2756  2    365.000  4000.00             1e-07             3e-09                    4000.05    0.560 43.436826 0.035752 0.045080\n    39  69.2550  2    434.255  4000.00             4e-07             1e-08                    3999.74    0.613 62.394474 0.058821 0.064640\n    40 114.1237  2    548.379  4000.00             8e-06             2e-07                    4001.43    0.695 76.126608 0.083554 0.075981\n    41 171.0237  3    719.402  4000.00             3e-04             9e-06                    3999.83    0.816 80.180393 0.098483 0.075676\n    42 240.8952  3    960.298  3999.99              0.01             2e-04                    3999.70    0.979 85.386424 0.105177 0.082297\n    43 330.4110  3   1290.709  3999.83              0.17              0.00                    3999.06    1.237 117.146216 0.116545 0.094411\n    44 365.0000  3   1655.709  3998.97              1.03              0.03                    3999.13    1.658 132.647231 0.104203 0.091857\n    45 365.0000  3   2020.709  3996.46              3.54              0.09                    3999.81    2.194 138.322035 0.088748 0.084787\n    46 365.0000  3   2385.709  3990.95              9.05              0.23                    3998.89    2.803 142.497935 0.077890 0.079436\n    47 365.0000  3   2750.709  3980.84             19.16              0.48                    3999.35    3.500 151.369024 0.068278 0.075753\n    48 365.0000  3   3115.709  3964.63             35.36              0.88                    3999.30    4.288 159.637730 0.061666 0.062125\n    49 365.0000  4   3480.709  3941.21             58.79              1.47                    4000.03    5.096 170.461283 0.056543 0.060493\n    50 169.2914  2   3650.000  3928.77             71.23              1.78                    3999.18    6.011 81.415280 0.025572 0.026018\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                  0.932s    98.98%\n|- Newton                                 0.805s    86.35%\n  |- Jacobian                             0.518s    64.31%\n  |- Update                               0.229s    28.45%\n  |- Solver                               0.033s     4.16%\n  |- Logging                              0.009s     1.11%\n  |- Residual                             0.007s     0.89%\n|- Output                                 0.115s    12.35%\n|- Input                                  0.000s     0.02%\nInitialization                            0.010s     1.02%\n------------------------------------------------------------\nTOTAL                                     0.942s\n============================================================\n\nTime steps : 50/50, step size: 73.00, 127.39\n')
```



## stflu003.dat

5000x5000x50, 2D diagonal water flooding in uniformed corner point

```
Running simulation: uniformed corner grid

    42 142.1889  2   3650.000  3927.16             72.84              1.82                    3999.93    5.123 60.446435 0.021367 0.018801



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  0.715s    98.41%

|- Newton                                 0.607s    84.86%

  |- Jacobian                             0.392s    64.62%

  |- Update                               0.169s    27.88%

  |- Solver                               0.027s     4.46%

  |- Logging                              0.007s     1.17%

  |- Residual                             0.005s     0.88%

|- Output                                 0.098s    13.66%

|- Input                                  0.000s     0.02%

Initialization                            0.012s     1.59%

------------------------------------------------------------

TOTAL                                     0.727s

============================================================



Time steps : 42/42, step size: 86.90, 137.53

```

```
CompletedProcess(args=['build/Release/simuapp.exe', '-f', 'c:\\Users\\hechr\\source\\hatch\\app/build/test/data//stflu003.dat'], returncode=0, stdout='c:\\Users\\hechr\\source\\hatch\\app/build/test/data\\stflu003.dat\n', stderr='unknown keyword: mxcnrpt\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1 1.00e-05  1    1.0e-05  4000.00                                                        4000.00    0.000 0.011954 0.000000 0.000004\n     2 2.33e-05  1    3.3e-05  4000.00                                                        4000.00    0.000 0.027888 0.000000 0.000010\n     3 5.44e-05  1    8.8e-05  4000.00                                                        4000.00    0.000 0.065050 0.000000 0.000022\n     4 1.27e-04  1    2.1e-04  4000.00                                                        4000.00    0.000 0.151665 0.000001 0.000052\n     5 2.96e-04  1    5.1e-04  4000.00                                                        4000.00    0.000 0.353245 0.000002 0.000122\n     6 6.89e-04  1      0.001  4000.00                                                        4000.00    0.000 0.820783 0.000004 0.000283\n     7 1.60e-03  1      0.003  4000.00                                                        4000.00    0.000 1.896606 0.000010 0.000654\n     8 3.68e-03  1      0.006  4000.00                                                        3999.99    0.000 4.327597 0.000022 0.001492\n     9 8.35e-03  2      0.015  4000.00                                                        4000.00    0.000 9.602980 0.000050 0.003311\n    10   0.0183  2      0.033  4000.00                                                        4000.00    0.000 20.108694 0.000110 0.006933\n    11   0.0377  2      0.071  4000.00                                                        4000.02    0.000 37.854855 0.000226 0.013050\n    12   0.0702  2      0.141  4000.00                                                        3999.64    0.000 60.773262 0.000420 0.020950\n    13   0.1166  2      0.258  4000.00                                                        3996.71    0.001 81.491755 0.000697 0.028091\n    14   0.1763  1      0.434  4000.00                                                        4003.41   17.281 54.389200 0.000606 0.018743\n    15   0.3019  3      0.736  4000.00                                                        4001.31   10.191 125.978864 0.001798 0.043423\n    16   0.3829  2      1.119  4000.00                                                        3998.22    7.283 108.778400 0.002230 0.037167\n    17   0.5179  2      1.637  4000.00                                                        3999.83    4.975 104.373630 0.003050 0.035790\n    18   0.7125  2      2.349  4000.00                                                        3999.97    3.466 100.407134 0.004159 0.034289\n    19   0.9959  2      3.345  4000.00                                                        3999.80    2.430 98.382048 0.005741 0.033394\n    20   1.4034  2      4.749  4000.00                                                        4000.12    1.718 97.054110 0.007952 0.032649\n    21   1.9882  2      6.737  4000.00                                                        4000.49    1.234 95.126258 0.011003 0.031570\n    22   2.8388  2      9.575  4000.00                                                        4000.23    0.858 90.638817 0.015246 0.029755\n    23   4.1289  2     13.704  4000.00                                                        3999.95    0.595 81.086976 0.021255 0.026986\n    24   6.2536  2     19.958  4000.00                                                        3999.98    0.412 64.965666 0.030395 0.022023\n    25  10.1818  1     30.140  4000.00                                                        3999.57    0.264 44.234128 0.044439 0.014762\n    26  18.3278  1     48.468  4000.00                                                        3999.81    0.165 26.230580 0.069363 0.015626\n    27  29.2425  1     77.710  4000.00                                                        4016.47    2.125 54.389200 0.084733 0.029823\n    28  43.6022  2    121.312  4000.00             3e-13             8e-15                    3998.26    1.362 49.996060 0.108966 0.037438\n    29  58.9295  3    180.242  4000.00             6e-11             2e-12                    4002.76    0.918 61.206765 0.109585 0.048579\n    30  79.4551  4    259.697  4000.00             7e-09             2e-10                    4000.99    0.638 55.137488 0.107540 0.051639\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31 105.3032  2    365.000  4000.00             4e-07             1e-08                    3999.35    0.457 50.060507 0.098176 0.053031\n    32 148.5079  2    513.508  4000.00             3e-05             7e-07                    4000.88    0.320 46.046554 0.113287 0.050181\n    33 197.4183  2    710.926  4000.00             1e-03             2e-05                    3999.28    0.336 60.045680 0.116209 0.050566\n    34 259.5566  2    970.483  3999.98              0.02             5e-04                    4000.60    0.462 80.277095 0.111553 0.056444\n    35 347.3283  3   1317.811  3999.74              0.26              0.01                    3998.97    0.632 108.099594 0.120446 0.065444\n    36 365.0000  3   1682.811  3998.69              1.31              0.03                    3999.97    0.939 118.601332 0.102717 0.063705\n    37 365.0000  3   2047.811  3995.82              4.18              0.10                    3999.88    1.402 123.624556 0.087486 0.060801\n    38 365.0000  3   2412.811  3989.77             10.23              0.26                    3999.12    1.978 127.860618 0.077220 0.056174\n    39 365.0000  3   2777.811  3978.97             21.03              0.53                    3999.49    2.668 135.422594 0.067008 0.046302\n    40 365.0000  3   3142.811  3961.96             38.03              0.95                    3999.34    3.433 142.075115 0.060728 0.045494\n    41 365.0000  3   3507.811  3937.68             62.31              1.56                    3999.68    4.260 150.319909 0.055987 0.045385\n    42 142.1889  2   3650.000  3927.16             72.84              1.82                    3999.93    5.123 60.446435 0.021367 0.018801\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                  0.715s    98.41%\n|- Newton                                 0.607s    84.86%\n  |- Jacobian                             0.392s    64.62%\n  |- Update                               0.169s    27.88%\n  |- Solver                               0.027s     4.46%\n  |- Logging                              0.007s     1.17%\n  |- Residual                             0.005s     0.88%\n|- Output                                 0.098s    13.66%\n|- Input                                  0.000s     0.02%\nInitialization                            0.012s     1.59%\n------------------------------------------------------------\nTOTAL                                     0.727s\n============================================================\n\nTime steps : 42/42, step size: 86.90, 137.53\n')
```

```
<module 'matplotlib.pyplot' from 'c:\\Users\\hechr\\source\\hatch\\app\\.venv\\Lib\\site-packages\\matplotlib\\pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_37.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_38.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_39.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_40.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_41.png" | relative_url }})



## stflu004.dat

2D diagonal water flooding for reduction of numerical dispersion and grid orientation effect


```
Running simulation: 2D diagonal flow: grid orientation

    58   3.6663  1   3650.000  3857.80            142.20              3.55                    4000.00   14.978 6.256055 0.001212 0.003768



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  2.930s    99.49%

|- Newton                                 2.767s    94.46%

  |- Jacobian                             1.557s    56.28%

  |- Update                               1.022s    36.93%

  |- Solver                               0.136s     4.93%

  |- Residual                             0.019s     0.69%

  |- Logging                              0.013s     0.45%

|- Output                                 0.148s     5.06%

|- Input                                  0.000s     0.01%

Initialization                            0.015s     0.51%

------------------------------------------------------------

TOTAL                                     2.945s

============================================================



Time steps : 58/58, step size: 62.93, 83.50

```

```
CompletedProcess(args=['build/Release/simuapp.exe', '-f', 'c:\\Users\\hechr\\source\\hatch\\app/build/test/data//stflu004.dat'], returncode=0, stdout='c:\\Users\\hechr\\source\\hatch\\app/build/test/data\\stflu004.dat\n', stderr='\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1 1.00e-05  1    1.0e-05  4000.00                                                        4000.00    0.000 0.382112 0.000002 0.000132\n     2 2.33e-05  1    3.3e-05  4000.00                                                        4000.00    0.000 0.887108 0.000004 0.000306\n     3 5.40e-05  1    8.7e-05  4000.00                                                        4000.00    0.000 2.045879 0.000010 0.000705\n     4 1.24e-04  1    2.1e-04  4000.00                                                        4000.00    0.000 4.647623 0.000024 0.001602\n     5 2.81e-04  1    4.9e-04  4000.00                                                        3999.99    0.000 10.213131 0.000054 0.003521\n     6 6.14e-04  2      0.001  4000.00                                                        4000.00    0.000 20.964891 0.000118 0.007228\n     7 1.26e-03  2      0.002  4000.00                                                        4000.00    0.000 38.065835 0.000241 0.013123\n     8 2.34e-03  2      0.005  4000.00                                                        4000.00    0.000 57.857027 0.000448 0.019945\n     9 3.94e-03  2      0.009  4000.00                                                        3999.96    0.003 72.411372 0.000755 0.024961\n    10 6.20e-03  1      0.015  4000.00                                                        3999.97   12.364 54.389200 0.000835 0.018741\n    11   0.0106  1      0.025  4000.00                                                        3999.98   23.447 54.389200 0.001239 0.018732\n    12   0.0182  2      0.044  4000.00                                                        4000.17   13.680 98.380260 0.003465 0.033839\n    13   0.0256  1      0.069  4000.00                                                        4000.12   18.167 54.389200 0.003605 0.018634\n    14   0.0439  1      0.113  4000.00                                                        4000.23   22.156 54.389200 0.005911 0.018555\n    15   0.0752  1      0.188  4000.00                                                        4000.01   25.611 54.389200 0.009673 0.018419\n    16   0.1287  1      0.317  4000.00                                                        4000.03   28.723 54.389200 0.015659 0.018189\n    17   0.2204  1      0.537  4000.00                                                        4000.00   31.594 54.389200 0.024988 0.018318\n    18   0.3774  1      0.915  4000.00                                                        4000.00   34.214 54.389200 0.039107 0.018840\n    19   0.6463  2      1.561  4000.00                                                        3999.99   20.045 89.771192 0.098611 0.032243\n    20   0.9099  1      2.471  4000.00                                                        4000.01   16.322 54.389200 0.106446 0.020552\n    21   1.2418  1      3.713  4000.00                                                        4000.01   10.895 43.371799 0.132378 0.017147\n    22   1.5392  1      5.252  4000.00                                                        4000.00    7.703 25.040573 0.126796 0.010564\n    23   1.9463  1      7.198  4000.00                                                        4000.00    5.627 13.664188 0.116714 0.011961\n    24   2.5540  1      9.752  4000.00                                                        4000.00    4.157 7.216266 0.102827 0.021022\n    25   3.5357  1     13.288  4000.00                                                        4000.00    3.052 4.238518 0.097224 0.032096\n    26   5.0056  1     18.294  4000.00                                                        4000.00    2.215 3.524426 0.122888 0.043693\n    27   6.4200  1     24.714  4000.00                                                        4000.00    1.641 3.825487 0.128827 0.048698\n    28   8.0588  1     32.772  4000.00                                                        4000.00    1.236 4.655990 0.121528 0.045418\n    29  10.3878  1     43.160  4000.00                                                        4000.00    0.938 5.997142 0.114201 0.036191\n    30  13.7611  1     56.921  4000.00                                                        4000.00    0.710 7.911701 0.134154 0.024590\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31  16.9499  1     73.871  4000.00                                                        4000.00    0.546 9.717215 0.132654 0.022912\n    32  20.9885  1     94.860  4000.00                                                        4000.00    0.426 12.016177 0.123912 0.026329\n    33  26.8188  1    121.679  4000.00                                                        4000.00    0.332 15.338546 0.139614 0.026768\n    34  32.4107  1    154.089  4000.00                                                        4000.00    0.263 18.554370 0.133337 0.022550\n    35  40.0362  6    194.125  4000.00             5e-15                                      4000.00    0.212 22.989294 0.143336 0.017879\n    36  47.7701  1    241.896  4000.00             3e-13             7e-15                    4000.00    0.170 27.521507 0.136744 0.017680\n    37  58.3082  1    300.204  4000.00             2e-11             4e-13                    4000.00    0.137 33.825600 0.145215 0.019724\n    38  64.7962  2    365.000  4000.00             3e-10             8e-12                    4000.00    0.113 38.021361 0.135297 0.020324\n    39  79.4914  3    444.491  4000.00             1e-08             3e-10                    4000.00    0.144 47.194911 0.142580 0.026261\n    40  95.0919  3    539.583  4000.00             2e-07             6e-09                    4000.00    0.200 58.007529 0.146345 0.033587\n    41 112.3090  3    651.892  4000.00             5e-06             1e-07                    4000.00    0.299 70.227773 0.147209 0.043769\n    42 132.2576  6    784.150  4000.00             7e-05             2e-06                    4000.00    0.488 85.041561 0.146104 0.054396\n    43 156.3310  2    940.481  4000.00             9e-04             2e-05                    4000.00    0.846 103.940647 0.149267 0.063153\n    44 182.8327  4   1123.314  3999.99              0.01             2e-04                    4000.00    1.248 127.594693 0.151180 0.087733\n    45 212.4692  8   1335.783  3999.95              0.05              0.00                    4000.00    1.760 156.329836 0.151934 0.110477\n    46 242.7587  4   1578.542  3999.69              0.31              0.01                    4000.00    2.464 191.115955 0.150620 0.132108\n    47 249.0811  6   1827.623  3998.80              1.20              0.03                    4000.00    3.295 210.907719 0.137016 0.151969\n    48 241.5531  5   2069.176  3996.82              3.18              0.08                    4000.00    4.268 221.040128 0.120761 0.158119\n    49 227.8557 11   2297.031  3992.74              7.26              0.18                    4000.00    5.306 225.454566 0.105312 0.164470\n    50 212.4078  5   2509.439  3986.80             13.20              0.33                    4000.00    6.406 226.695011 0.091490 0.161876\n    51 197.3552  7   2706.794  3977.25             22.75              0.57                    4000.00    7.495 226.389715 0.080233 0.165190\n    52 183.5181  5   2890.313  3965.06             34.94              0.87                    4000.00    8.601 225.271601 0.071516 0.160413\n    53 171.1596  6   3061.472  3949.78             50.22              1.26                    4000.00    9.670 224.502146 0.063656 0.163300\n    54 159.9613  5   3221.434  3931.34             68.66              1.72                    4000.00   10.735 222.643747 0.057650 0.158247\n    55 150.2413  5   3371.675  3909.94             90.06              2.25                    4000.00   11.773 222.155727 0.052530 0.158558\n    56 141.2969  7   3512.972  3885.51            114.49              2.86                    4000.00   12.767 220.824280 0.047550 0.159954\n    57 133.3621  5   3646.334  3858.58            141.42              3.54                    4000.00   13.747 219.087736 0.044127 0.155627\n    58   3.6663  1   3650.000  3857.80            142.20              3.55                    4000.00   14.978 6.256055 0.001212 0.003768\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                  2.930s    99.49%\n|- Newton                                 2.767s    94.46%\n  |- Jacobian                             1.557s    56.28%\n  |- Update                               1.022s    36.93%\n  |- Solver                               0.136s     4.93%\n  |- Residual                             0.019s     0.69%\n  |- Logging                              0.013s     0.45%\n|- Output                                 0.148s     5.06%\n|- Input                                  0.000s     0.01%\nInitialization                            0.015s     0.51%\n------------------------------------------------------------\nTOTAL                                     2.945s\n============================================================\n\nTime steps : 58/58, step size: 62.93, 83.50\n')
```

![png]({{ "/assets/images/benchmark_image_42.png" | relative_url }})

```
<module 'matplotlib.pyplot' from 'c:\\Users\\hechr\\source\\hatch\\app\\.venv\\Lib\\site-packages\\matplotlib\\pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_43.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_44.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_45.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_46.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_47.png" | relative_url }})

# SPE4C

* Steam flood on three component live oil

* 'Water', 'LiteOil', 'Medm oil', 'Heavy oil'


## Run & Load

```
Running simulation: SPE4-C benchmark on live oil

   166  22.7735  2   3650.000     0.03             28.43             99.89                      28.06   44.647 0.361650 0.002851 0.580231



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                 19.930s    99.94%

|- Newton                                19.421s    97.44%

  |- Jacobian                            14.433s    74.32%

  |- Update                               3.341s    17.20%

  |- Solver                               1.386s     7.14%

  |- Logging                              0.078s     0.40%

  |- Residual                             0.067s     0.35%

|- Output                                 0.470s     2.36%

|- Input                                  0.000s     0.00%

Initialization                            0.012s     0.06%

------------------------------------------------------------

TOTAL                                    19.942s

============================================================



Time steps : 166/223, step size: 21.99, 53.30

```

```
CompletedProcess(args=['build/Release/simuapp.exe', '-f', 'c:\\Users\\hechr\\source\\hatch\\app/build/test/data//stspe003.dat'], returncode=0, stdout='c:\\Users\\hechr\\source\\hatch\\app/build/test/data\\stspe003.dat\n', stderr='\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1   0.1000  1      0.100   117.45             2e-07             2e-07                      37.50    0.032 28.511705 0.000862 11.673974\n     2   0.1779  1      0.278    98.26              0.03              0.03                      37.50    0.031 13.785749 0.043727 19.663927\n     3   0.2724  2      0.550    87.97              0.04              0.05                      37.50    0.031 6.462878 0.056353 28.240896\n     4   0.3625  2      0.913    82.29              0.05              0.06                      37.50    0.031 4.932198 0.050120 35.089183\n     5   0.4370  2      1.350    78.71              0.05              0.06                      37.50    0.031 3.993458 0.038891 39.385616\n     6   0.4973  2      1.847    76.13              0.05              0.07                      37.50    0.031 2.961047 0.029469 41.548082\n     7   0.5505  2      2.398    74.08              0.05              0.07                      37.50    0.031 1.749764 0.023319 42.359210\n     8   0.6032  4      3.001    72.52              0.05              0.08                      37.50    0.031 41.886056 0.208020 24.885697\n     9   0.5896  2      3.590    71.44              0.06              0.08                      37.50    0.034 5.888233 0.088097 14.498921\n    10   0.8668  2      4.457    70.23              0.06              0.08                      37.50    0.044 12.202675 0.039004 20.018987\n    11   1.3186  2      5.776    68.55              0.06              0.08                      37.50    0.060 8.802436 0.026695 27.645529\n    12   1.7710  2      7.547    66.37              0.06              0.09                      37.50    0.085 5.292406 0.030425 34.192733\n    13   2.1615  2      9.708    63.86              0.06              0.09                      37.50    0.120 4.377827 0.031526 38.436391\n    14   2.4907  2     12.199    61.23              0.06              0.09                      37.50    0.169 3.991683 0.027998 40.521183\n    15   2.7933  1     14.992    58.60              0.06              0.10                      37.53    0.249 3.594044 0.026856 40.500000\n    16   3.1335  3     18.126    59.97              0.06              0.10                      37.51    0.324 27.027165 0.272447 42.925374\n    17   2.5961  4     20.722    60.50              0.06              0.09                      37.50    0.416 10.319539 0.191367 28.120218\n    18   2.6617  2     23.384    59.87              0.06              0.10                      37.50    0.499 7.195750 0.093074 25.968077\n    19   3.6696  2     27.053    57.83              0.06              0.10                      37.50    0.585 8.408242 0.045467 32.148244\n    20   4.6102  2     31.663    54.92              0.06              0.10                      37.50    0.701 5.888330 0.023533 36.653457\n    21   5.4399  3     37.103    54.54              0.06              0.10                      37.50    0.845 5.978035 0.168119 34.237954\n    22   5.9851  2     43.088    54.33              0.06              0.11                      37.50    1.023 1.354392 0.105878 36.654956\n    23   7.0622  3     50.151    57.26              0.06              0.10                      37.51    1.226 11.949207 0.188118 31.600191\n    24   7.3104  2     57.461    56.57              0.08              0.15                      37.50    1.462 4.047419 0.114571 35.233335\n    25   8.7946  2     66.256    52.39              0.45              0.84                      37.50    1.704 6.705935 0.048825 43.498606\n    26   9.5005  4     75.756    47.70              2.03              4.08                      37.50    1.982 4.187846 0.182765 44.414402\n    27   9.9925  3     85.749    48.74              5.16              9.57                      37.50    2.289 10.206611 0.172058 36.787367\n    28  10.8595  3     96.608    48.77              9.12             15.75                      37.51    2.606 4.304045 0.163387 31.359828\n    29  12.1282  2    108.736    45.24             11.65             20.47                      37.50    2.951 4.026760 0.123132 42.542890\n    30  13.2581  3    121.994    41.65             13.85             24.96                      37.50    3.321 3.752061 0.133448 47.125639\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31  13.7084  5    135.703    41.23             17.44             29.73                      37.50    3.725 3.656561 0.241029 36.939534\n    32  12.2701  2    147.973    39.35             19.73             33.40                      37.50    4.180 2.334186 0.125849 36.163494\n    33  14.5748  3    162.548    36.52             21.18             36.71                      37.48    4.562 3.650872 0.171041 41.428495\n    34  15.8895  4    178.437    35.04             23.28             39.92                      37.49    5.021 4.770871 0.215004 43.708962\n    35  15.2363  4    193.673    34.81             26.45             43.18                      37.50    5.544 2.357504 0.159989 47.676332\n    36  15.6520  2    209.325    33.34             28.11             45.74                      37.46    6.096 3.171667 0.205497 48.611777\n    37  15.4100  4    224.735    31.67             29.50             48.23                      37.50    6.632 2.544517 0.232414 45.191228\n    38  14.1038  3    238.839    30.26             31.09             50.68                      37.50    7.189 1.453470 0.178560 25.988814\n    39  15.0241  2    253.863    28.75             32.36             52.95                      37.51    7.722 3.469906 0.197515 38.013559\n    40  15.1316  2    268.995    27.45             33.46             54.93                      37.50    8.289 3.739622 0.110419 50.244748\n    41  15.0894  3    284.084    26.46             33.44             55.83                      37.50    8.855 3.333164 0.243402 31.823620\n    42  13.4246  3    297.509    26.47             34.63             56.68                      37.50    9.435 2.512718 0.161836 31.776343\n    43  15.0676  3    312.576    26.43             36.39             57.92                      37.50    9.915 2.293192 0.152460 33.976856\n    44  17.4358  4    330.012    25.56             38.09             59.84                      37.50   10.449 2.202547 0.181359 35.852308\n    45  18.4167  4    348.429    24.81             40.54             62.03                      37.51   11.087 2.652564 0.176537 29.587092\n    46  19.7401  4    368.169    23.17             40.20             63.44                      37.50   11.769 4.497916 0.145543 48.701356\n    47  20.0374  3    388.206    24.54             42.58             63.43                      37.50   12.522 2.999616 0.161335 36.692432\n    48  22.5259  4    410.732    24.51             43.62             64.02                      37.51   13.262 2.366921 0.177404 38.731323\n    49  24.0806  3    434.813    21.81             43.08             66.39                      37.52   14.121 5.131543 0.188151 57.774194\n    50  22.1156  4    456.929    24.72             43.73             63.89                      37.51   15.054 3.708393 0.260774 37.340270\n    51  18.8436  3    475.772    24.53             43.80             64.10                      37.50   15.945 2.668214 0.174609 31.514131\n    52  20.3176  4    496.090    25.17             43.32             63.25                      37.50   16.656 3.660764 0.179504 42.109486\n    53  21.5814  4    517.671    25.17             39.89             61.31                      37.50   17.412 2.866806 0.161049 47.815776\n    54  22.1339  4    539.805    18.45             36.31             66.32                      37.50   18.233 7.155783 0.190356 33.031694\n    55  22.7611  3    562.566    13.71             33.98             71.25                      37.50   19.014 4.751170 0.126967 25.615309\n    56  28.7629  4    591.329    12.36             34.35             73.55                      37.50   19.705 3.150871 0.215925 28.744645\n    57  27.5112  3    618.840    11.93             34.30             74.20                      37.50   20.645 4.336974 0.157170 32.385147\n    58  31.3472  4    650.187    11.65             35.35             75.21                      37.50   21.446 4.751923 0.187444 38.586745\n    59  32.5136  3    682.701    11.44             36.86             76.32                      37.50   22.390 5.304762 0.207926 37.912132\n    60  31.7936  3    714.495    11.08             37.69             77.28                      37.50   23.391 3.960185 0.204184 44.440394\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    61  31.4180  5    745.913    10.99             38.01             77.57                      37.50   24.319 2.432553 0.252081 49.289310\n    62  27.3485  4    773.261    11.13             39.12             77.85                      37.50   25.293 3.426715 0.233850 35.597364\n    63  24.9368  2    798.198    11.26             41.93             78.83                      37.49   26.162 4.523803 0.127564 59.621792\n    64  22.4663  6    820.664    11.99             41.71             77.67                      37.50   26.908 6.388333 0.218531 42.417105\n    65   0.2634  4 4  820.928    11.24             40.94             78.46                      37.50   27.892 4.385629 0.010770 0.742244\n    66   0.1912  4 1  821.119    10.42             39.86             79.28                      37.50   27.904 1.920081 0.009638 0.546965\n    67   0.1397  4 1  821.259     9.72             38.86             79.99                      37.50   27.912 1.708531 0.007312 0.504835\n    68   0.1036  4 1  821.362     8.12             34.11             80.77                      37.50   27.920 5.111619 0.012600 0.574359\n    69   0.2230  4    821.585     8.74             37.75             81.20                      37.50   27.924 4.185354 0.009621 0.846657\n    70   0.1630  4 1  821.748     8.49             37.91             81.70                      37.50   27.934 0.819052 0.006681 0.558153\n    71   0.1214  4 1  821.870     7.85             35.69             81.97                      37.50   27.942 2.265854 0.009016 0.484661\n    72   0.0890  4 1  821.959     5.81             28.13             82.89                      37.50   27.950 7.994769 0.022604 0.441036\n    73   0.0602  4 1  822.019     4.86             25.43             83.97                      37.50   27.957 7.353174 0.022837 0.314679\n    74   0.1219  4    822.141     4.58             24.21             84.08                      37.50   27.963 2.312358 0.024658 0.594952\n    75   0.0814  3 1  822.222     4.54             23.80             83.98                      37.50   27.970 1.758043 0.013049 0.378103\n    76   0.1748  4    822.397     4.94             24.58             83.26                      37.50   27.977 3.768310 0.013659 0.708644\n    77   0.1246  3 1  822.521     5.21             25.26             82.91                      37.50   27.986 1.165950 0.007037 0.452068\n    78   0.0926  3 1  822.614     5.37             25.68             82.70                      37.50   27.993 0.688191 0.003727 0.308442\n    79   0.2107  3    822.825     5.54             26.04             82.47                      37.50   28.000 0.702264 0.006044 0.576887\n    80   0.1576  3 1  822.982     5.63             26.25             82.35                      37.50   28.011 0.386806 0.004385 0.367800\n    81   0.1191  3 1  823.101     5.66             26.33             82.30                      37.50   28.019 0.190566 0.003245 0.245128\n    82   0.0906  3 1  823.192     5.68             26.36             82.27                      37.50   28.026 0.105843 0.002434 0.169592\n    83   0.2081  3    823.400     5.70             26.37             82.23                      37.50   28.032 0.172163 0.005410 0.310034\n    84   0.1562  3 1  823.556     5.72             26.40             82.19                      37.50   28.043 0.118045 0.003963 0.189580\n    85   0.1184  3 1  823.675     5.73             26.41             82.17                      37.50   28.051 0.082607 0.002947 0.120388\n    86   0.0903  3 1  823.765     5.74             26.43             82.15                      37.50   28.057 0.062201 0.002215 0.080677\n    87   0.2077  3    823.973     5.78             26.49             82.10                      37.50   28.063 0.155399 0.004911 0.187474\n    88   0.1564  3 1  824.129     5.81             26.56             82.05                      37.50   28.074 0.145585 0.003592 0.142304\n    89   0.1188  3 1  824.248     5.84             26.62             82.01                      37.50   28.082 0.118381 0.002666 0.108733\n    90   0.2723  3    824.520     5.91             26.77             81.91                      37.50   28.089 0.283524 0.005760 0.252607\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    91   0.2040  3 1  824.724     5.98             26.91             81.82                      37.50   28.103 0.239434 0.004114 0.191049\n    92   0.1544  3 1  824.879     6.03             27.01             81.75                      37.50   28.113 0.183721 0.002999 0.145664\n    93   0.1178  3 1  824.996     6.07             27.09             81.70                      37.50   28.121 0.139012 0.002219 0.111664\n    94   0.2708  3    825.267     6.16             27.26             81.58                      37.50   28.128 0.305116 0.004748 0.259736\n    95   0.2041  3 1  825.471     6.23             27.40             81.49                      37.50   28.141 0.233084 0.003385 0.197497\n    96   0.1553  3 1  825.627     6.28             27.50             81.42                      37.50   28.151 0.171317 0.002463 0.151160\n    97   0.3564  4    825.983     6.39             27.71             81.26                      37.50   28.160 0.382205 0.005101 0.351683\n    98   0.2681  3 1  826.251     6.47             27.85             81.15                      37.50   28.177 0.264587 0.003542 0.267089\n    99   0.2037  3 1  826.455     6.53             27.97             81.07                      37.50   28.190 0.207956 0.002532 0.204384\n   100   0.1558  3 1  826.611     6.58             28.06             81.00                      37.50   28.200 0.160242 0.001856 0.157149\n   101   0.3591  3    826.970     6.69             28.24             80.86                      37.50   28.207 0.354762 0.003866 0.366281\n   102   0.2723  3 1  827.242     6.77             28.39             80.75                      37.50   28.224 0.273588 0.002708 0.279948\n   103   0.2080  3 1  827.450     6.83             28.50             80.67                      37.50   28.237 0.201325 0.001945 0.215129\n   104   0.4792  4    827.929     6.97             28.73             80.49                      37.50   28.247 0.459580 0.003891 0.501603\n   105   0.3633  3 1  828.293     7.06             28.89             80.35                      37.50   28.268 0.316032 0.002646 0.383567\n   106   0.2777  3 1  828.570     7.14             29.01             80.26                      37.50   28.285 0.242181 0.001859 0.295004\n   107   0.2133  3 1  828.784     7.19             29.10             80.18                      37.50   28.297 0.178802 0.001339 0.227702\n   108   0.4933  3    829.277     7.31             29.28             80.03                      37.50   28.306 0.388225 0.002685 0.532045\n   109   0.3770  3 1  829.654     7.39             29.41             79.91                      37.50   28.328 0.289527 0.001865 0.409540\n   110   0.2896  3 1  829.943     7.46             29.51             79.83                      37.50   28.344 0.211979 0.001368 0.316351\n   111   0.6696  3    830.613     7.59             29.71             79.65                      37.50   28.355 0.451732 0.002857 0.740450\n   112   0.5107  3 1  831.124     7.68             29.86             79.53                      37.50   28.384 0.327869 0.002027 0.569787\n   113   0.3913  3 1  831.515     7.75             29.96             79.45                      37.50   28.405 0.235815 0.001470 0.439432\n   114   0.9024  4    832.417     7.89             30.17             79.27                      37.50   28.418 0.490939 0.003019 1.027513\n   115   0.6832  3 1  833.101     7.99             30.33             79.16                      37.50   28.455 0.444080 0.003330 0.784841\n   116   0.5198  3 1  833.620     8.06             30.47             79.09                      37.50   28.483 0.278280 0.003492 0.600965\n   117   0.3951  3 1  834.015     8.11             30.57             79.04                      37.50   28.504 0.189270 0.003285 0.458909\n   118   0.9021  3    834.918     8.21             30.82             78.96                      37.50   28.515 0.391072 0.009780 1.058046\n   119   0.6587  3 1  835.576     8.29             31.02             78.91                      37.50   28.551 0.271369 0.007996 0.777435\n   120   0.4864  3 1  836.063     8.34             31.17             78.88                      37.50   28.577 0.189498 0.006245 0.576626\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n   121   1.0896  3    837.152     8.46             31.50             78.84                      37.50   28.589 0.394986 0.015123 1.303532\n   122   0.7698  3 1  837.922     8.53             31.73             78.81                      37.50   28.631 0.265848 0.011023 0.926209\n   123   0.5578  3 1  838.480     8.59             31.90             78.78                      37.50   28.661 0.184216 0.008072 0.673646\n   124   1.2350  3    839.715     8.70             32.23             78.74                      37.50   28.674 0.382361 0.017566 1.503113\n   125   0.8599  3 1  840.575     8.78             32.46             78.71                      37.50   28.720 0.253361 0.011858 1.051284\n   126   1.8593  3    842.434     8.93             32.86             78.63                      37.50   28.739 0.496983 0.022967 2.294371\n   127   1.2541  3 1  843.688     9.03             33.11             78.57                      37.50   28.807 0.312626 0.014133 1.557583\n   128   2.6743  4    846.362     9.21             33.56             78.47                      37.50   28.830 0.598060 0.024475 3.368882\n   129   1.7883  3 1  848.151     9.31             33.84             78.42                      37.50   28.925 0.367085 0.014169 2.273735\n   130   3.8125  3    851.963     9.50             34.46             78.38                      37.50   28.950 0.713324 0.023950 4.943535\n   131   7.6710  3    859.634     9.91             36.14             78.48                      37.50   28.993 1.277634 0.033154 10.050459\n   132  14.1159  2    873.750     9.37             35.84             79.27                      37.50   29.092 3.608251 0.123509 17.821510\n   133  18.0636  3    891.814     8.58             35.39             80.49                      37.50   29.379 4.093241 0.134291 15.464045\n   134  22.2387  2    914.052     8.35             35.68             81.03                      37.49   29.527 4.717189 0.161766 14.581860\n   135  24.9660  2    939.018     7.40             34.77             82.46                      37.50   29.725 4.799062 0.109053 18.564019\n   136  33.7309  3    972.749     6.61             34.94             84.10                      37.50   29.777 4.797665 0.123737 34.812915\n   137  40.8150  3   1013.564     6.17             35.64             85.25                      37.49   29.975 6.381053 0.138426 39.550254\n   138  46.3504  4   1059.915     5.30             34.65             86.73                      37.50   30.272 10.462362 0.173363 39.646112\n   139  35.0853  4   1095.000     3.99             33.42             89.33                      37.50   31.003 8.786891 0.162688 24.853466\n   140  39.2720  2   1134.272     4.10             35.00             89.51                      37.50   31.281 8.123180 0.118708 29.032616\n   141  51.1529  2   1185.425     3.16             34.38             91.59                      37.50   31.424 9.033703 0.083746 32.982169\n   142  63.5037  4   1248.929     2.73             34.22             92.62                      37.50   31.661 12.147242 0.151866 37.786682\n   143  73.6297  4   1322.558     1.58             33.77             95.52                      37.50   32.043 15.210590 0.168652 29.229687\n   144  80.8732  3   1403.431     1.84             34.03             94.87                      37.50   32.519 17.531864 0.129674 13.571385\n   145 101.2093  3   1504.641     1.19             33.12             96.53                      37.50   32.786 21.811883 0.070673 13.746690\n   146  17.8360  4 2 1522.477     1.00             22.50             95.73                      37.50   35.074 5.083194 0.103695 2.374805\n   147  24.6067  2   1547.083     1.01             28.73             96.61                      37.50   35.072 6.163236 0.034225 3.131370\n   148  46.7492  2   1593.833     0.96             30.32             96.92                      37.50   34.834 11.433880 0.034217 5.684493\n   149  88.8203  2   1682.653     0.93             30.62             97.04                      37.50   34.409 23.489263 0.055960 10.597418\n   150 150.9374  4   1833.590     0.97             29.71             96.84                      37.50   33.899 45.963940 0.082254 17.323795\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n   151 227.4581  4   2061.048     0.98             28.58             96.68                      37.50   33.577 81.658545 0.133325 25.650275\n   152 280.9856  5   2342.034     0.85             27.12             96.96                      37.50   33.992 121.712043 0.138958 30.878070\n   153 340.3432  5   2682.377     0.47             24.92             98.16                      37.50   34.497 182.753810 0.085712 37.203137\n   154 357.9827  8   3040.360     0.16             19.39             99.20                      37.50   35.428 249.975578 0.125340 39.860995\n   155 104.4182  3 1 3144.778     0.10             16.25             99.37                      37.50   39.525 82.862944 0.019944 11.639311\n   156   5.8128  1 3 3150.591     0.10             17.67             99.43                      37.50   41.191 3.226872 0.003594 0.436842\n   157  13.2457  7   3163.837     0.10             18.91             99.50                      37.51   41.150 2.786101 0.084080 2.700993\n   158   2.2006  6 2 3166.037     0.10             28.83             99.66                      35.53   41.350 4.060631 0.093218 1.871809\n   159   3.1667  3   3169.204     0.09             18.01             99.48                      34.32   41.352 1.359235 0.009065 0.187640\n   160   6.9680  2   3176.172     0.09             18.30             99.50                      32.33   41.333 0.634614 0.017115 0.517109\n   161  14.5935  2   3190.765     0.09             21.51             99.60                      31.72   41.314 0.207686 0.023951 1.071529\n   162  29.3629  2   3220.128     0.08             24.08             99.68                      31.24   41.300 0.149082 0.044128 1.731366\n   163  52.9394  2   3273.068     0.07             27.26             99.76                      30.66   41.372 0.194890 0.007149 2.357772\n   164 116.2181  3   3389.286     0.05             28.49             99.83                      29.45   41.427 0.342812 0.007221 5.237872\n   165 237.9408  3   3627.226     0.03             27.23             99.88                      27.05   41.753 0.789471 0.011161 8.680452\n   166  22.7735  2   3650.000     0.03             28.43             99.89                      28.06   44.647 0.361650 0.002851 0.580231\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                 19.930s    99.94%\n|- Newton                                19.421s    97.44%\n  |- Jacobian                            14.433s    74.32%\n  |- Update                               3.341s    17.20%\n  |- Solver                               1.386s     7.14%\n  |- Logging                              0.078s     0.40%\n  |- Residual                             0.067s     0.35%\n|- Output                                 0.470s     2.36%\n|- Input                                  0.000s     0.00%\nInitialization                            0.012s     0.06%\n------------------------------------------------------------\nTOTAL                                    19.942s\n============================================================\n\nTime steps : 166/223, step size: 21.99, 53.30\n')
```

#### Load CMG

### Load ECL

### Wells

![png]({{ "/assets/images/benchmark_image_48.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_49.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_50.png" | relative_url }})

```
<module 'matplotlib.pyplot' from 'c:\\Users\\hechr\\source\\hatch\\app\\.venv\\Lib\\site-packages\\matplotlib\\pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_51.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_52.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_53.png" | relative_url }})

```
<module 'matplotlib.pyplot' from 'c:\\Users\\hechr\\source\\hatch\\app\\.venv\\Lib\\site-packages\\matplotlib\\pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_54.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_55.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_56.png" | relative_url }})

### Block

#### Block Pressure


```
<module 'matplotlib.pyplot' from 'c:\\Users\\hechr\\source\\hatch\\app\\.venv\\Lib\\site-packages\\matplotlib\\pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_57.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_58.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_59.png" | relative_url }})

#### Block Temperature

```
<module 'matplotlib.pyplot' from 'c:\\Users\\hechr\\source\\hatch\\app\\.venv\\Lib\\site-packages\\matplotlib\\pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_60.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_61.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_62.png" | relative_url }})

```
<module 'matplotlib.pyplot' from 'c:\\Users\\hechr\\source\\hatch\\app\\.venv\\Lib\\site-packages\\matplotlib\\pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_63.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_64.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_65.png" | relative_url }})

```
<module 'matplotlib.pyplot' from 'c:\\Users\\hechr\\source\\hatch\\app\\.venv\\Lib\\site-packages\\matplotlib\\pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_66.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_67.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_68.png" | relative_url }})

#### v.s. ECL

```
<module 'matplotlib.pyplot' from 'c:\\Users\\hechr\\source\\hatch\\app\\.venv\\Lib\\site-packages\\matplotlib\\pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_69.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_70.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_71.png" | relative_url }})
