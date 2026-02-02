---
layout: default
title: "Benchmark results of resrsim"
date: 2026-02-01
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
Current OS: Darwin

simuexe path: build/bin/simuapp

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

```
Found 29 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build/test/data/stflu005_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_2.png" | relative_url }})

```
Interactive view: /Users/mark/Documents/workspace/hatch/app/build/test/data/stflu005_00000.vtu

```

```
Widget(value='<iframe src="http://localhost:56454/index.html?ui=P_0x176845d90_6&reconnect=auto" class="pyvista…
```

# SPE4-b


### Load STARS

### Load ECL

### Load SMY File

Load the SMY file (`spe04b.smy`) into a pandas DataFrame, ensuring proper parsing of the data.

```
Running simulation: SPE4-b

    61 116.4646  1   3650.000     0.07             27.29             99.73                      29.97   43.162   0.0208   0.0020   3.4503



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                 10.830s    98.89%

|- Newton                                10.672s    98.54%

  |- Jacobian                             8.445s    79.13%

  |- Update                               2.009s    18.83%

  |- Solver                               0.123s     1.15%

  |- Residual                             0.041s     0.39%

  |- Logging                              0.003s     0.03%

|- Output                                 0.144s     1.33%

|- Input                                  0.000s     0.00%

Initialization                            0.122s     1.11%

------------------------------------------------------------

TOTAL                                    10.952s

============================================================





```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//spe04b.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/spe04b.dat\n', stderr='[MacBook-Air.local:21490] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/454426624/sm_segment.MacBook-Air.501.1b160000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1   1.0000  1      1.000     3.96             3e-07             6e-06                       2.76    0.014  32.0278 4.36e-04   8.7598\n     2   1.8163  1      2.816     3.48              0.03              0.83                       3.74    0.013  33.9085   0.0376  19.8400\n     3   3.2564  1      6.073     3.26              0.04              1.19                       9.08    0.182  28.6287   0.0430  40.5000\n     4   5.5870  9     11.660     2.84              0.05              1.84                      32.55    0.187 111.8725   0.2435 208.2055\n     5   4.5730  4     16.233     2.68              0.06              2.05                      37.50    0.242  68.2229   0.0967  83.2745\n     6   6.1316  3     22.364     2.61              0.05              2.05                      37.50    0.332  49.4184   0.0510  91.6519\n     7   7.8841  5     30.248     2.70              0.05              1.72                      37.50    0.430  62.4438   0.1759  90.3220\n     8   8.4679  3     38.716     2.95              0.03              1.11                      37.50    0.665  43.6456   0.1922  76.6601\n     9   8.6605  3     47.377     3.35              0.02              0.71                      37.50    0.920  29.8028   0.0724  59.5336\n    10  13.2147  2     60.592     4.14              0.01              0.23                      37.50    1.254  33.5532   0.0363  69.7040\n    11  19.0383  3     79.630     5.59              0.02              0.27                      37.50    1.724  40.8274   0.2003  90.1657\n    12  19.0229  3     98.653     6.72              2.13             24.06                      37.50    2.373  41.9409   0.2132  76.2154\n    13  18.3327  2    116.985     7.49              4.21             35.97                      37.48    3.339  31.7892   0.1817  62.2994\n    14  19.3421  2    136.328     8.26              6.35             43.48                      37.50    3.977  30.4544   0.0428  63.5926\n    15  28.8331  4    165.161     9.24             11.24             54.88                      37.50    4.487  39.7683   0.1845  88.0066\n    16  30.1680  3    195.329    10.15             15.85             60.97                      37.50    5.376  33.8016   0.1815  67.4567\n    17  31.8500  4    227.179    11.06             20.24             64.66                      37.50    6.198  25.8813   0.1502  64.6369\n    18  37.1374  4    264.316    12.54             26.45             67.83                      37.50    7.031  20.3983   0.1302  97.2184\n    19  46.3918  4    310.708    15.61             35.46             69.43                      37.50    7.992  12.5145   0.1803  69.9887\n    20  49.1585  3    359.866    20.98             48.69             69.89                      37.50    9.383  54.1086   0.1313  87.8036\n    21  61.1667  6    421.033    24.44             49.65             67.01                      37.50   10.754  58.9889   0.1749  96.0163\n    22  65.8877  6    486.921    23.85             46.40             66.05                      37.50   12.444  43.3433   0.2206 109.8217\n    23  62.2249  7    549.146    22.96             43.39             65.40                      37.50   14.266  32.7240   0.1966  90.7007\n    24  62.8353  5    611.981    22.59             41.53             64.77                      37.50   15.913  23.7985   0.2182 120.5433\n    25  59.7284  7    671.709    24.49             43.23             63.84                      37.50   17.618  29.8780   0.2087  91.5376\n    26  58.2729 13    729.982    32.13             51.55             61.60                      37.50   19.413  40.7365   0.2459 119.9557\n    27  17.1721  5 1  747.154    29.56             41.10             58.17                      37.51   21.557   6.2395   0.1295  27.2494\n    28  21.5030  4    768.657    20.59             36.02             63.63                      37.50   22.048   5.5628   0.1294  42.9025\n    29  26.9387  5    795.596    19.39             36.42             65.26                      37.50   22.627   5.2713   0.1155  44.2062\n    30  35.5096  6    831.106    16.48             34.74             67.83                      37.51   23.268   3.9704   0.1598  66.9752\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31  40.1163  4    871.222    13.91             34.21             71.09                      37.50   24.135   4.8089   0.2035  46.6854\n    32  39.7166  4    910.939    14.03             35.04             71.41                      37.53   25.154   2.7764   0.1304  44.4733\n    33  49.5674  4    960.506    13.18             35.23             72.77                      37.49   26.034   3.1633   0.1747  55.5549\n    34  53.4286  5   1013.935    13.35             36.49             73.21                      37.49   27.041   3.4171   0.1792  79.2456\n    35  56.7986 12   1070.733    14.14             38.23             72.99                      37.50   27.768   5.2842   0.2184 112.4700\n    36  24.2668  4   1095.000    13.18             36.48             73.45                      37.50   29.298   3.5034   0.1031  30.1496\n    37  33.5630  5   1128.563    11.75             34.67             74.68                      37.49   29.463   6.0531   0.1659  38.2572\n    38  37.1866  4   1165.750    10.30             32.98             76.20                      37.49   29.848   6.4859   0.1542  54.3382\n    39  42.7828  5   1208.532     8.91             31.89             78.17                      37.52   30.192   7.6493   0.1562  58.4402\n    40  48.9010  4   1257.433     7.53             31.86             80.89                      37.46   30.592   9.6618   0.1505  64.6516\n    41  56.9593  4   1314.393     6.01             31.41             83.93                      37.49   30.964  13.0391   0.2092  41.7167\n    42  55.4957  3   1369.888     5.85             34.13             85.38                      37.50   31.588  11.6556   0.1011  43.5318\n    43  77.3446  5   1447.233     4.26             31.28             88.03                      37.50   31.660  17.6488   0.1505  23.4316\n    44  90.0814  3   1537.314     3.44             31.17             90.07                      37.50   32.064  21.8691   0.1083  21.1203\n    45 122.0805  2   1659.395     2.62             31.21             92.24                      37.49   32.231  32.2700   0.0891  16.0815\n    46 178.7111  4   1838.106     1.79             30.34             94.43                      37.51   32.168  53.4741   0.1103  22.2268\n    47 240.2958  3   2078.402     1.12             29.83             96.37                      37.49   32.405  83.4108   0.1279  27.8840\n    48 302.6219  5   2381.024     0.60             28.04             97.89                      37.50   32.920 127.6939   0.0993  33.2351\n    49 330.7255  4   2711.749     0.29             25.91             98.89                      37.51   34.100 166.1732   0.0666  33.5823\n    50 311.5313  5   3023.281     0.12             22.20             99.45                      37.52   35.744 188.4667   0.0932  30.3799\n    51  90.5716  3 1 3113.852     0.09             20.01             99.56                      37.50   39.506  59.8300   0.0733   8.4490\n    52 137.9624  2   3251.815     0.06             19.39             99.69                      37.52   39.411  90.5350   0.0234  12.0622\n    53  59.4564  5 1 3311.271     0.06             21.78             99.72                      37.47   41.014  30.2371   0.0212   3.8996\n    54   1.3499  1 4 3312.621     0.05             17.25             99.73                      37.50   41.966   1.5764   0.0050   0.1590\n    55   3.0482  3   3315.669     0.05             17.42             99.73                      19.81   41.912   2.5398   0.0081   0.3152\n    56   6.7494  1   3322.418     0.05             17.68             99.73                      31.87   41.892   0.7723   0.0194   0.4935\n    57  13.9412  1   3336.360     0.06             21.06             99.73                      31.19   41.873   0.2793   0.0177   0.8791\n    58  29.0940  1   3365.454     0.07             24.50             99.73                      30.47   41.851   0.2381   0.0167   1.5387\n    59  61.0918  2   3426.546     0.07             27.01             99.72                      30.10   41.848   0.1126   0.0499   2.4238\n    60 106.9899  1   3533.535     0.07             27.18             99.73                      30.03   42.191   0.0232   0.0050   3.4198\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    61 116.4646  1   3650.000     0.07             27.29             99.73                      29.97   43.162   0.0208   0.0020   3.4503\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                 10.830s    98.89%\n|- Newton                                10.672s    98.54%\n  |- Jacobian                             8.445s    79.13%\n  |- Update                               2.009s    18.83%\n  |- Solver                               0.123s     1.15%\n  |- Residual                             0.041s     0.39%\n  |- Logging                              0.003s     0.03%\n|- Output                                 0.144s     1.33%\n|- Input                                  0.000s     0.00%\nInitialization                            0.122s     1.11%\n------------------------------------------------------------\nTOTAL                                    10.952s\n============================================================\n\n\n')
```

## Select and Plot Columns

Select specific columns from the loaded DataFrames and plot them using matplotlib. For example, plot `TIME` vs `TEMP 1-1-4` from `stars_spe4b_special.csv`.

### Cell property

#### Block Pressure


```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_3.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_4.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_5.png" | relative_url }})

#### Block Temperature

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_6.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_7.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_8.png" | relative_url }})

#### Block Saturation

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_9.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_10.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_11.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_12.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_13.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_14.png" | relative_url }})

### vesus ECL

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_15.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_16.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_17.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_18.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_19.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_20.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_21.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_22.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_23.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_24.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_25.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_26.png" | relative_url }})

### Well property

#### Injector

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_27.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_28.png" | relative_url }})

#### Producer Corner

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_29.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_30.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_31.png" | relative_url }})

#### Producer Edge

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
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

    27   4.7035  1     10.000    6e-08              1.00            100.00                       1.00    7.505 3.00e-05 3.54e-06 7.96e-06



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  2.736s    97.52%

|- Newton                                 2.671s    97.63%

  |- Jacobian                             1.817s    68.01%

  |- Update                               0.780s    29.18%

  |- Solver                               0.036s     1.33%

  |- Residual                             0.018s     0.69%

  |- Logging                              0.002s     0.07%

|- Output                                 0.061s     2.22%

|- Input                                  0.000s     0.00%

Initialization                            0.070s     2.48%

------------------------------------------------------------

TOTAL                                     2.806s

============================================================





```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//buckley.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/buckley.dat\n', stderr='[MacBook-Air.local:21544] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/1522794496/sm_segment.MacBook-Air.501.5ac40000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1 2.33e-04 11 1  2.3e-04     1.00                                                           1.00    0.045 491.1717   0.3331   0.1833\n     2 1.27e-04  2    3.6e-04     1.00                                                           1.00    0.049   4.2661   0.0849   0.0202\n     3 1.90e-04  4    5.5e-04     1.00                                                           1.00    0.842   7.5636   0.1334   0.0236\n     4 2.34e-04  6    7.8e-04     1.00                                                           1.00    1.764   8.8050   0.1361   0.0221\n     5 2.87e-04  6      0.001     1.00                                                           1.00    2.652  10.9567   0.1361   0.0213\n     6 3.51e-04  8      0.001     1.00                                                           1.00    3.573  13.3953   0.1495   0.0213\n     7 4.10e-04  9      0.002     1.00                                                           1.00    4.521  15.2025   0.1385   0.0215\n     8 4.97e-04  9      0.002     1.00                                                           1.00    5.403  18.1014   0.1466   0.0223\n     9 5.87e-04 12      0.003     1.00                                                           1.00    6.285  21.5336   0.1617   0.0226\n    10 5.87e-04 12      0.004     1.00                                                           1.00    7.184  20.8806   0.1476   0.0212\n    11 5.87e-04 10      0.004     1.00                                                           1.00    7.970  20.0347   0.1326   0.0204\n    12 7.04e-04  8      0.005     0.90              0.12             11.69                       1.00    8.511  20.2257   0.1531   0.0239\n    13 8.13e-04  3      0.006     0.55              0.45             44.55                       1.00    9.197  37.4810   0.1093   0.0412\n    14 1.10e-03  2      0.007     0.33              0.67             67.10                       1.00    9.517  39.0113   0.0673   0.0441\n    15 1.77e-03  2      0.008     0.20              0.80             79.80                       1.00    9.394  37.8579   0.0497   0.0474\n    16 3.10e-03  2      0.012     0.12              0.88             87.83                       1.00    8.829  36.6778   0.0438   0.0505\n    17 5.60e-03  2      0.017     0.07              0.93             92.98                       1.00    7.713  34.1157   0.0412   0.0498\n    18   0.0103  3      0.027     0.04              0.96             96.28                       1.00    6.232  29.5512   0.0404   0.0451\n    19   0.0188  3      0.046     0.02              0.98             98.17                       1.00    4.403  23.4138   0.0368   0.0386\n    20   0.0353  3      0.082     0.01              0.99             99.18                       1.00    2.515  17.7304   0.0320   0.0333\n    21   0.0679  3      0.149     0.00              1.00             99.66                       1.00    1.028  12.8003   0.0262   0.0094\n    22   0.1349  3      0.284     0.00              1.00             99.87                       1.00    0.398   8.7667   0.0180   0.0055\n    23   0.2809  3      0.565    5e-04              1.00             99.95                       1.00    0.428   6.7160   0.0192   0.0022\n    24   0.5810  1      1.146    1e-04              1.00             99.99                       1.00    7.539   2.4198   0.0112 7.54e-04\n    25   1.2615  1      2.408    8e-06              1.00            100.00                       1.00    8.645   0.3641   0.0029 2.00e-04\n    26   2.8887  1      5.296    2e-07              1.00            100.00                       1.00    8.344   0.0241 2.47e-04 3.21e-05\n    27   4.7035  1     10.000    6e-08              1.00            100.00                       1.00    7.505 3.00e-05 3.54e-06 7.96e-06\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                  2.736s    97.52%\n|- Newton                                 2.671s    97.63%\n  |- Jacobian                             1.817s    68.01%\n  |- Update                               0.780s    29.18%\n  |- Solver                               0.036s     1.33%\n  |- Residual                             0.018s     0.69%\n  |- Logging                              0.002s     0.07%\n|- Output                                 0.061s     2.22%\n|- Input                                  0.000s     0.00%\nInitialization                            0.070s     2.48%\n------------------------------------------------------------\nTOTAL                                     2.806s\n============================================================\n\n\n')
```

### Load Benchmark

### Buckley Plot

![png]({{ "/assets/images/benchmark_image_35.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_36.png" | relative_url }})

# MISC

## spe04b_cw.dat

```
Running simulation: SPE4-b water flooding

    22 365.0000  1   3650.000     5.00             63.84             92.74                      67.50    0.352   4.5892   0.0301   0.0084



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  4.971s    98.58%

|- Newton                                 4.824s    97.05%

  |- Jacobian                             3.621s    75.05%

  |- Update                               1.136s    23.55%

  |- Solver                               0.027s     0.55%

  |- Residual                             0.021s     0.44%

  |- Logging                              0.001s     0.02%

|- Output                                 0.143s     2.87%

|- Input                                  0.000s     0.00%

Initialization                            0.072s     1.42%

------------------------------------------------------------

TOTAL                                     5.042s

============================================================





```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//spe04b_cw.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/spe04b_cw.dat\n', stderr='[MacBook-Air.local:21559] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/1217462272/sm_segment.MacBook-Air.501.48910000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1   1.0000  2      1.000    35.34              0.09              0.27                      67.50    0.001 100.2588   0.0636   0.1578\n     2   1.2338  1      2.234    28.03              0.11              0.40                      67.50    0.012  42.1592   0.0443   0.0611\n     3   2.0941  1      4.328    23.41              0.11              0.48                      67.50    0.014  44.4332   0.0443   0.0744\n     4   3.5028  1      7.831    20.29              0.11              0.54                      67.51    0.023  34.5855   0.0569   0.0578\n     5   5.9253  1     13.756    17.97              0.10              0.58                      67.50    0.038  37.1767   0.0873   0.0640\n     6   8.7393  2     22.495    16.52              0.10              0.60                      67.50    0.037  26.7190   0.0631   0.0450\n     7  14.3524  2     36.848    16.05              0.10              0.59                      67.50    0.037  23.6524   0.0661   0.0442\n     8  23.2431  2     60.091    17.08              0.09              0.54                      67.50    0.037  23.2917   0.0851   0.0389\n     9  34.6032  3     94.694    19.69              0.13              0.67                      67.50    0.052  22.3587   0.0892   0.0391\n    10  50.6401  3    145.334    22.58              2.55             10.15                      67.50    0.084  20.6670   0.0719   0.0346\n    11  79.8756  4    225.210    24.23             11.26             31.73                      67.50    0.082  23.2832   0.0702   0.0384\n    12 126.9727  3    352.182    23.83             26.16             52.33                      67.50    0.103  22.1221   0.0668   0.0429\n    13 205.0004  5    557.183    21.19             42.67             66.81                      67.50    0.103  13.0193   0.0677   0.0421\n    14 329.5184  4    886.701    16.89             55.66             76.71                      67.50    0.104  20.0207   0.0560   0.0613\n    15 208.2989  1   1095.000    14.67             59.71             80.27                      67.50    0.160  12.7080   0.0317   0.0343\n    16 365.0000  2   1460.000    11.76             62.11             84.08                      67.50    0.161  18.5595   0.0539   0.0440\n    17 365.0000  1   1825.000     9.66             62.52             86.61                      67.50    0.282  14.8736   0.0601   0.0324\n    18 365.0000  2   2190.000     8.17             63.01             88.52                      67.50    0.280  10.4581   0.0454   0.0221\n    19 365.0000  1   2555.000     7.07             64.21             90.08                      67.50    0.299   8.5612   0.0290   0.0171\n    20 365.0000  1   2920.000     6.20             63.26             91.07                      67.50    0.319   6.6841   0.0431   0.0130\n    21 365.0000  1   3285.000     5.55             64.08             92.03                      67.50    0.341   5.3445   0.0298   0.0101\n    22 365.0000  1   3650.000     5.00             63.84             92.74                      67.50    0.352   4.5892   0.0301   0.0084\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                  4.971s    98.58%\n|- Newton                                 4.824s    97.05%\n  |- Jacobian                             3.621s    75.05%\n  |- Update                               1.136s    23.55%\n  |- Solver                               0.027s     0.55%\n  |- Residual                             0.021s     0.44%\n  |- Logging                              0.001s     0.02%\n|- Output                                 0.143s     2.87%\n|- Input                                  0.000s     0.00%\nInitialization                            0.072s     1.42%\n------------------------------------------------------------\nTOTAL                                     5.042s\n============================================================\n\n\n')
```



## watfld_cw.dat

```
Running simulation: SPE4-b Water flooding without vmod

    38 203.0488  1   3650.000     6.58            496.71             98.69                     503.18    1.916   1.6566   0.0173   0.0036



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  6.336s    99.04%

|- Newton                                 6.093s    96.18%

  |- Jacobian                             4.460s    73.19%

  |- Update                               1.535s    25.19%

  |- Solver                               0.040s     0.66%

  |- Residual                             0.030s     0.50%

  |- Logging                              0.001s     0.02%

|- Output                                 0.233s     3.68%

|- Input                                  0.000s     0.00%

Initialization                            0.061s     0.96%

------------------------------------------------------------

TOTAL                                     6.397s

============================================================





```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//watfld_cw.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/watfld_cw.dat\n', stderr='[MacBook-Air.local:21579] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/1865744384/sm_segment.MacBook-Air.501.6f350000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1   1.0000  1      1.000   201.20             7e-07             3e-07                     503.19    0.294  54.3892 7.47e-04   0.0837\n     2   1.1667  1      2.167   195.68              0.01              0.00                     503.19    0.584  54.3892   0.0228   0.0828\n     3   1.3611  5      3.528   172.50              0.03              0.02                     495.70    0.638 271.9460   0.0839   0.3887\n     4   0.5293  2      4.057   169.05              0.03              0.02                     503.18    0.637  65.5996   0.0248   0.1058\n     5   0.5598  1      4.617   172.44              0.03              0.02                     503.20    0.635  47.2390   0.0216   0.0768\n     6   0.6991  1      5.316   179.88              0.02              0.01                     503.19    0.679  34.9752   0.0223   0.0573\n     7   0.9928  1      6.309   192.17              0.02              0.01                     503.19    0.675  36.0293   0.0255   0.0600\n     8   1.3935  1      7.702   209.80              0.01              0.01                     503.18    0.671  44.0402   0.0387   0.0739\n     9   1.7967  1      9.499   231.76              0.00              0.00                     503.19    0.806  31.4936   0.0316   0.0583\n    10   2.6549  1     12.154   259.72             4e-07             1e-07                     503.19    0.798  40.8546   0.0512   0.0695\n    11   3.5376  2     15.691   292.79                                                         503.19    0.789  40.3943   0.0464   0.0734\n    12   4.7365  1     20.428   328.42                                                         503.19    0.868  43.7222   0.0604   0.0735\n    13   6.1267  2     26.555   367.80                                                         503.19    0.962  47.3474   0.0679   0.0873\n    14   7.6426  3     34.197   401.98                                                         503.18    0.945  40.0644   0.0637   0.0676\n    15  10.2687  2     44.466   392.20             25.11              6.02                     503.17    0.862  57.8037   0.0721   0.0978\n    16  11.6155  2     56.082   340.01            112.11             24.80                     503.19    0.852  42.0226   0.0501   0.0934\n    17  15.2897  1     71.371   284.00            302.51             51.58                     503.18    0.722  38.0059   0.0609   0.0956\n    18  21.0009  2     92.372   237.53            317.52             57.21                     503.19    0.739  64.2873   0.0645   0.1930\n    19  22.4576  2    114.830   189.65            367.18             65.94                     503.19    0.742  61.3960   0.0373   0.1620\n    20  24.6150  1    139.445   154.22            402.70             72.31                     503.18    0.803  54.1684   0.0396   0.1463\n    21  28.7759  1    168.221   124.14            410.00             76.76                     503.18    0.852  51.5638   0.0319   0.1317\n    22  34.4672  1    202.688   100.78            425.51             80.85                     503.18    0.894  41.1825   0.0321   0.1138\n    23  45.7684  1    248.456    81.09            432.61             84.21                     503.19    0.939  38.2378   0.0335   0.1078\n    24  62.7073  1    311.164    64.49            446.72             87.39                     503.18    1.009  33.0093   0.0478   0.0987\n    25  91.0550  1    402.219    50.12            455.17             90.08                     503.18    1.114  32.4123   0.0662   0.0971\n    26 133.1270  1    535.346    37.99            462.09             92.40                     503.18    1.424  29.2229   0.0599   0.0728\n    27 202.0630  2    737.409    28.31            477.42             94.40                     503.18    1.390  24.4778   0.0639   0.0556\n    28 325.1481  2   1062.557    20.35            484.40             95.97                     503.18    1.356  24.2355   0.0726   0.0456\n    29  32.4432  1   1095.000    19.70            484.81             96.10                     503.19    1.355   2.2032   0.0061   0.0042\n    30  72.7360  1   1167.736    18.43            485.58             96.34                     503.18    1.362   4.3482   0.0153   0.0081\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31 154.0213  1   1321.757    16.34            486.55             96.75                     503.18    1.435   7.2901   0.0296   0.0146\n    32 300.1939  1   1621.951    13.64            487.99             97.28                     503.18    1.703   9.7001   0.0628   0.0202\n    33 365.0000  2   1986.951    11.51            492.14             97.71                     503.18    1.675   7.6838   0.0663   0.0181\n    34 365.0000  1   2351.951     9.96            493.70             98.02                     503.18    1.657   6.1566   0.0554   0.0126\n    35 365.0000  1   2716.951     8.74            494.15             98.26                     503.18    1.734   5.0741   0.0470   0.0093\n    36 365.0000  1   3081.951     7.75            494.86             98.46                     503.18    1.840   4.2826   0.0478   0.0077\n    37 365.0000  1   3446.951     6.96            495.79             98.61                     503.18    1.918   3.4965   0.0319   0.0069\n    38 203.0488  1   3650.000     6.58            496.71             98.69                     503.18    1.916   1.6566   0.0173   0.0036\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                  6.336s    99.04%\n|- Newton                                 6.093s    96.18%\n  |- Jacobian                             4.460s    73.19%\n  |- Update                               1.535s    25.19%\n  |- Solver                               0.040s     0.66%\n  |- Residual                             0.030s     0.50%\n  |- Logging                              0.001s     0.02%\n|- Output                                 0.233s     3.68%\n|- Input                                  0.000s     0.00%\nInitialization                            0.061s     0.96%\n------------------------------------------------------------\nTOTAL                                     6.397s\n============================================================\n\n\n')
```

## stflu001.dat

Inverted 9 spot water flooding with area/block modifier, 5 point transmissibility


```
Running simulation: Inverted 9 spot water flooding

   172 348.4941  6   3650.000   103.23            781.38             88.33                     877.97   98.744   2.0596   0.0450   0.8750



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                 18.590s    99.61%

|- Newton                                18.195s    97.88%

  |- Jacobian                            14.550s    79.96%

  |- Update                               3.429s    18.85%

  |- Solver                               0.071s     0.39%

  |- Residual                             0.069s     0.38%

  |- Logging                              0.006s     0.03%

|- Output                                 0.369s     1.99%

|- Input                                  0.000s     0.00%

Initialization                            0.073s     0.39%

------------------------------------------------------------

TOTAL                                    18.663s

============================================================





```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//stflu001.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/stflu001.dat\n', stderr='[MacBook-Air.local:21595] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/1237450752/sm_segment.MacBook-Air.501.49c20000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1   1.0000  1      1.000     3.96             3e-07             6e-06                       0.16    0.007   6.6465 2.62e-05   0.6435\n     2   2.2343  1      3.234     3.41              0.03              0.93                       0.17    0.007   7.4995   0.0021   1.3689\n     3   4.9652  1      8.200     2.93              0.05              1.71                       0.17    0.007   6.6147   0.0055   3.0274\n     4  10.7200  1     18.920     2.59              0.06              2.14                       0.20    0.008   6.3740   0.0133   6.7813\n     5  21.1828  1     40.102     2.36              0.06              2.30                       0.26    0.016   4.6035   0.0206  15.6783\n     6  34.8543  2     74.957     2.19              0.05              2.36                       0.55    0.022   4.5504   0.0533  50.4356\n     7  34.6817  3    109.638     2.15              0.05              2.34                       2.83    0.759  14.9407   0.0779 121.5000\n     8  19.0858  7    128.724     2.21              0.05              2.08                      16.27    0.813  81.1400   0.3216 173.1175\n     9   2.6430 11 1  131.367     2.26              0.04              1.95                     426.26    0.944 401.7257   0.2775 270.2038\n    10   0.7516  2    132.119     2.28              0.04              1.90                     462.84    1.373  66.2193   0.0650  81.0000\n    11   0.5550  2    132.674     2.30              0.04              1.85                     429.55    1.435  83.5402   0.2101  62.5011\n    12   0.4856  2    133.159     2.32              0.04              1.80                     410.08    1.481  64.1258   0.1952  39.3206\n    13   0.4923  1    133.652     2.34              0.04              1.74                     419.41    1.526  54.3358   0.0401  34.3661\n    14   0.5994  1    134.251     2.38              0.04              1.64                     427.69    1.780  54.3892   0.0313  37.6015\n    15   0.6983  2    134.949     2.45              0.04              1.47                     414.77    1.830  58.1004   0.1453  51.8086\n    16   0.6842  1    135.634     2.53              0.03              1.31                     426.80    2.376  45.1382   0.0444  40.5000\n    17   0.7675  1    136.401     2.64              0.03              1.24                     438.27    3.069  46.6486   0.0320  40.5000\n    18   0.8610  1    137.262     2.80              0.03              1.13                     446.87    3.860  49.5941   0.0283  40.5000\n    19   0.9659  2    138.228     3.10              0.03              0.97                     408.18    4.456  66.1342   0.1885  50.6213\n    20   0.9591  2    139.187     3.56              0.03              0.74                     413.49    4.504  61.5891   0.0594  61.5266\n    21   0.8474  1    140.034     4.00              0.02              0.54                     430.38    5.119  47.2079   0.0264  40.5000\n    22   0.9506  2    140.985     4.70              0.02              0.39                     441.72    5.129  58.2792   0.0247  59.4283\n    23   0.8582  1    141.843     5.27              0.02              0.34                     459.31    5.957  42.7444   0.0139  40.5000\n    24   0.9627  1    142.806     6.06              0.02              0.28                     472.48    6.693  45.0033   0.0202  40.5000\n    25   1.0800  3    143.886     7.72              0.02              0.20                     475.68    6.658  53.0811   0.1905  58.8768\n    26   0.9805  2    144.866     9.55              0.01              0.13                     460.79    6.688  51.5468   0.1511  55.5803\n    27   0.9217  1    145.788    11.18              0.13              1.15                     470.83    7.092  49.1697   0.0875  40.5000\n    28   1.0340  2    146.822    12.62              1.42             10.11                     449.03    7.247  66.9574   0.2083  52.4109\n    29   1.0062  2    147.828    13.82              6.79             32.95                     451.91    7.277  61.6308   0.0306  42.8239\n    30   1.0961  1    148.924    14.88             12.48             45.62                     454.88    7.737  54.3892   0.0179  35.4934\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31   1.3140  3    150.238    16.50             18.79             53.25                     445.17    7.714  63.3296   0.1812  49.8972\n    32   1.3155  2    151.554    18.32             24.45             57.16                     441.55    7.749  55.4839   0.0677  44.1656\n    33   1.4095  1    152.963    20.48             29.71             59.20                     438.80    8.010  54.3892   0.0309  40.1389\n    34   1.5885  1    154.552    23.17             35.50             60.51                     434.66    8.564  54.3892   0.0232  36.3013\n    35   1.8834  2    156.435    28.47             44.40             60.93                     389.73    8.577  68.6448   0.1696  50.1502\n    36   1.8802  2    158.316    36.14             59.31             62.13                     378.04    8.656  60.3984   0.0814  48.2796\n    37   1.9179  1    160.233    46.93             83.66             64.06                     377.59    9.285  54.3892   0.0288  40.3653\n    38   2.1552  3    162.389   100.66            175.33             63.53                     359.65    9.329  73.9078   0.1657  76.3497\n    39   1.6564  3    164.045   146.37            349.28             70.47                     369.14    9.501 129.0570   0.1544  93.7388\n    40   1.1043  2    165.149   151.72            402.70             72.63                     383.65    9.702  69.7753   0.0393  58.5748\n    41   1.0058  1    166.155   152.86            425.29             73.56                     398.32    9.921  40.3904   0.0170  40.5000\n    42   1.1283  3    167.283   144.83            313.87             68.43                     403.23    9.976 122.9257   0.1618  26.7815\n    43   1.2667  1    168.550   131.73            351.10             72.72                     411.30   10.068  25.6192   0.0164  27.1741\n    44   1.7138  1    170.264   141.12            413.29             74.55                     427.02   10.198  30.4992   0.0177  40.5000\n    45   1.9225  4    172.186   297.11            796.20             72.82                     477.52   10.376 126.2852   0.2282 127.1379\n    46   1.0217  3    173.208   373.92           1017.09             73.12                     515.77   10.681 114.7353   0.2028 121.5000\n    47   0.5623  5    173.770   355.37            659.86             65.00                     513.85   10.850 104.8157   0.1814  36.2542\n    48   0.5939  1    174.364   268.34            674.73             71.55                     519.15   10.966  32.5693   0.0474  11.4774\n    49   1.0529  1    175.417   216.23            690.11             76.14                     537.37   11.062  26.4838   0.0272  20.3116\n    50   1.5936  1    177.011   183.24            695.35             79.14                     562.21   11.200  24.2509   0.0188  31.3202\n    51   2.0262  2    179.037   161.64            695.92             81.15                     580.34   11.392  23.9374   0.1353  37.1363\n    52   2.3754  1    181.412   149.00            692.15             82.29                     598.86   11.622  22.8901   0.0650  40.5000\n    53   2.6647  2    184.077   141.50            701.13             83.21                     602.82   11.850  17.0078   0.2091  51.8968\n    54   2.5973  2    186.674   137.71            694.53             83.45                     620.62   12.068  24.5853   0.0405  49.8600\n    55   2.6014  8    189.276   147.64            688.46             82.34                     627.83   12.128  17.2751   0.1527  67.6455\n    56   2.1649  3    191.441   141.15            686.83             82.95                     636.76   12.330  16.6755   0.0923  87.7865\n    57   1.5119  1    192.953   135.13            689.81             83.62                     641.39   12.771   7.3547   0.0316  40.5000\n    58   1.6961  1    194.649   128.41            691.29             84.33                     646.15   13.176   5.8703   0.0244  40.5000\n    59   1.9027  2    196.551   127.41            680.02             84.22                     637.70   13.280  33.3995   0.1725  31.4859\n    60   2.0647  2    198.616   119.74            681.72             85.06                     639.08   13.424  20.4230   0.1178  31.3969\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    61   2.6222  3    201.238   115.70            688.23             85.61                     640.63   13.564  16.0705   0.1183  56.6335\n    62   2.4375  2    203.676   115.03            695.93             85.82                     645.22   13.759  21.5877   0.0776  63.6433\n    63   2.1087  2    205.785   116.09            704.48             85.85                     652.73   13.927  22.6170   0.0388  56.6628\n    64   1.9595  1    207.744   120.33            715.74             85.61                     659.54   14.213  34.6184   0.0175  40.5000\n    65   2.1981  4    209.942   132.61            733.96             84.70                     667.44   14.297  62.7972   0.1317  88.4819\n    66   1.5267  3    211.469   128.24            714.11             84.78                     670.71   14.431  25.6999   0.1364  51.6010\n    67   1.4993  1    212.968   114.43            715.46             86.21                     673.89   14.483   8.4547   0.0689  25.8145\n    68   2.0720  1    215.040   107.66            707.66             86.80                     680.32   14.521  13.6078   0.0476  39.1498\n    69   2.3652  1    217.405   105.67            707.76             87.01                     687.02   14.690   9.6239   0.0284  40.5000\n    70   2.6533  1    220.059   108.23            715.71             86.86                     693.61   15.040  12.7584   0.0206  40.5000\n    71   2.9765  4    223.035   146.70            793.03             84.39                     703.38   15.094  71.8131   0.2088 121.4678\n    72   1.6383  5    224.673   181.88            846.41             82.31                     713.27   15.283  77.7103   0.1225 112.5158\n    73   0.9556  3    225.629   159.21            792.05             83.26                     715.45   15.380  43.6322   0.1687  35.2434\n    74   1.0494  1    226.678   123.02            810.58             86.82                     718.37   15.420   8.2000   0.0730  11.8973\n    75   1.6469  1    228.325   100.66            798.08             88.80                     725.26   15.504  14.8568   0.0307  17.3355\n    76   2.6279  1    230.953    84.88            787.20             90.27                     735.32   15.605  12.4998   0.0269  28.5896\n    77   3.4793  2    234.432    76.84            792.46             91.16                     740.78   15.753  12.6051   0.1571  48.1479\n    78   3.5545  6    237.987    72.51            782.18             91.52                     747.51   15.949  13.2003   0.0653  54.6516\n    79   3.3751  6    241.362    70.08            773.36             91.69                     753.18   16.120  12.7324   0.0313  49.0076\n    80   3.4138  6    244.776    68.55            768.25             91.81                     756.79   16.252   9.7702   0.1149  37.5590\n    81   3.9796  6    248.756    67.48            765.12             91.90                     760.24   16.338   8.9261   0.1479  48.9167\n    82   4.0295  6    252.785    67.23            764.28             91.91                     763.14   16.439   9.5375   0.1379  52.1859\n    83   3.9313  6    256.716    69.78            767.29             91.66                     765.63   16.523   9.5488   0.0755  50.8896\n    84   3.8918  6    260.608    76.15            775.38             91.06                     765.43   16.600   7.9987   0.1212  59.5016\n    85   3.5105  2    264.119    82.34            784.92             90.51                     760.90   16.806  11.2827   0.1521  81.0000\n    86   2.5922  2    266.711    81.51            782.81             90.57                     762.07   16.972   7.2011   0.0552  66.4500\n    87   2.1820  1    268.893    79.19            783.31             90.82                     763.82   17.332   3.6716   0.0203  40.5000\n    88   2.4477  4    271.341    83.14            778.80             90.35                     761.29   17.412  31.6063   0.2036  30.1667\n    89   2.4229  1    273.763    75.29            777.45             91.17                     761.30   17.562  11.7530   0.0847  25.8342\n    90   3.3474  6    277.111    65.82            776.04             92.18                     765.51   17.673   8.2265   0.0386  40.6189\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    91   3.7494  6    280.860    59.97            774.13             92.81                     769.14   17.833   9.6359   0.1230  46.5837\n    92   3.9018  6    284.762    56.86            774.04             93.16                     771.69   18.006   6.1267   0.1301  50.2576\n    93   3.8903  6    288.652    55.06            772.23             93.34                     775.16   18.169   8.7925   0.0594  46.9001\n    94   4.0332  6    292.686    54.82            774.41             93.39                     777.23   18.317   7.4340   0.1143  50.0077\n    95   4.0329  6    296.718    54.38            774.67             93.44                     779.09   18.473   5.9397   0.0734  60.9119\n    96   3.5857  1    300.304    53.93            773.28             93.48                     780.72   18.900   4.2405   0.0210  40.5000\n    97   4.0224  2    304.327    53.99            774.28             93.48                     781.18   19.004  13.0983   0.1993  55.9360\n    98   3.7669  3    308.093    54.52            781.95             93.48                     778.64   19.166  13.8674   0.1672  41.1086\n    99   4.1562  2    312.250    55.46            790.06             93.44                     777.87   19.330  10.2009   0.1320  43.1118\n   100   4.5114  2    316.761    58.53            797.79             93.16                     777.20   19.528  12.0830   0.1325  52.8654\n   101   4.3683  2    321.129    60.89            795.02             92.89                     778.82   19.743   9.0437   0.0849  61.1848\n   102   3.8732  2    325.003    61.76            791.01             92.76                     781.84   19.957   8.3046   0.0358  64.8753\n   103   3.3104  1    328.313    61.86            789.69             92.74                     784.03   20.412   6.1170   0.0142  40.5000\n   104   3.7136  3    332.027    66.36            787.03             92.22                     783.94   20.418  15.3737   0.1659  64.0062\n   105   3.2012  3    335.228    72.26            808.93             91.80                     783.39   20.574  44.6149   0.1751  74.4182\n   106   2.5028  3    337.731    77.16            830.90             91.50                     786.08   20.721  70.4155   0.0676  78.0314\n   107   1.8955  1    339.626    76.71            835.74             91.59                     788.48   20.927  32.9804   0.0225  40.5000\n   108   2.1264  3    341.752    74.46            817.31             91.65                     788.99   20.984  63.0081   0.1482  31.6658\n   109   2.4956  2    344.248    67.55            818.10             92.37                     791.17   21.046  11.5609   0.0514  37.7533\n   110   2.9017  1    347.150    65.26            817.30             92.61                     794.33   21.176   7.0168   0.0304  40.5000\n   111   3.2551  1    350.405    64.36            816.37             92.69                     797.31   21.412   5.8123   0.0197  40.5000\n   112   3.6515  3    354.056    66.48            826.44             92.55                     797.10   21.500  16.1911   0.1819  67.4281\n   113   3.0450  2    357.101    67.96            830.55             92.44                     797.59   21.656  11.7111   0.1282  44.9991\n   114   3.2296  3    360.331    72.58            836.24             92.01                     799.42   21.755   9.2523   0.1619  57.2276\n   115   2.9832  7    363.314    87.96            877.94             90.89                     803.10   21.853  21.7006   0.1251  74.6033\n   116   2.3285  6    365.643   121.35            938.42             88.55                     810.28   22.034 105.9628   0.1252 159.5947\n   117   1.0337  3    366.676   103.33            900.39             89.71                     812.51   22.215  40.3966   0.1501  17.3276\n   118   1.2057  2    367.882    91.69            900.45             90.76                     814.54   22.288  22.5674   0.0937  24.3033\n   119   1.7070  3    369.589    83.90            889.59             91.38                     817.74   22.368   9.0569   0.0813  46.6796\n   120   1.7743  2    371.363    74.68            882.87             92.20                     821.29   22.488  11.5956   0.1034  22.4239\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n   121   2.4504  1    373.814    66.90            877.66             92.92                     825.92   22.580   9.7047   0.0384  28.3753\n   122   3.2547  1    377.069    61.83            872.82             93.39                     831.80   22.681   9.0845   0.0220  40.4607\n   123   3.6530  4    380.722    64.16            877.84             93.19                     835.00   22.833  11.6372   0.1652  49.9819\n   124   3.6537  3    384.375    67.82            893.77             92.95                     840.40   23.016  25.0951   0.0901  84.4818\n   125   2.6209  5    386.996    74.15            889.90             92.31                     842.29   23.226  22.4587   0.1588  86.6631\n   126   1.8470  3    388.843    64.28            875.51             93.16                     843.08   23.397  23.7952   0.1338  33.6281\n   127   2.2721  2    391.115    52.86            877.58             94.32                     844.62   23.516   9.2304   0.1204  14.0370\n   128   2.9410  3    394.056    43.45            879.13             95.29                     846.40   23.671   8.8361   0.0968   6.2261\n   129   4.1711  1    398.227    36.27            881.54             96.05                     848.82   23.855   5.5186   0.0925  10.6390\n   130   6.0213  1    404.249    30.10            878.03             96.69                     852.70   24.087   8.2059   0.0360  26.7430\n   131   8.2012  1    412.450    26.36            872.46             97.07                     856.26   24.334   5.5419   0.0357  40.5000\n   132   9.2000  1    421.650    24.11            869.50             97.30                     858.76   24.691   3.2749   0.0198  40.5000\n   133  10.3205  2    431.970    21.80            866.11             97.54                     861.65   25.020   4.6042   0.0282  64.7241\n   134   8.8340  1    440.804    21.11            866.06             97.62                     863.04   25.487   2.4050   0.0224  40.5000\n   135   9.9099  4    450.714    21.34            868.39             97.60                     862.68   25.764  10.1831   0.2234  85.3763\n   136   7.0568  3    457.771    22.30            865.97             97.49                     862.68   26.157   4.6840   0.1092  57.9487\n   137   6.4692  3    464.240    23.06            868.73             97.41                     862.03   26.387   5.9452   0.1483  90.8963\n   138   4.4086  2    468.649    21.99            869.60             97.53                     862.40   26.664   4.2885   0.0489  76.5078\n   139   3.3836  1    472.033    21.00            869.89             97.64                     862.82   26.879   1.7211   0.0171  40.5000\n   140   3.7957  2    475.828    20.43            871.36             97.71                     862.11   27.004  13.6318   0.2099  25.0652\n   141   3.6913  1    479.520    18.79            874.13             97.90                     861.90   27.180   5.1068   0.0723  23.2463\n   142   5.3170  1    484.837    17.18            875.80             98.08                     862.40   27.304   3.2814   0.0500  38.9795\n   143   6.0832  2    490.920    15.76            874.85             98.23                     863.69   27.503   3.2854   0.0383  51.5949\n   144   5.9743  1    496.894    14.83            873.98             98.33                     864.70   27.733   2.6678   0.0227  40.5000\n   145   6.7020  1    503.596    13.85            873.63             98.44                     865.69   27.945   1.9789   0.0163  40.5000\n   146   7.5182  3    511.114    13.17            877.04             98.52                     865.50   28.197   9.4710   0.2066  31.7474\n   147   7.3794  1    518.494    11.76            877.35             98.68                     866.18   28.490   4.5477   0.0472  33.5092\n   148   9.0931  2    527.587    10.11            878.24             98.86                     867.77   28.762   3.3201   0.0430  39.8742\n   149  10.2831  3    537.870     8.76            880.58             99.02                     869.09   29.112   2.9283   0.1320   8.3098\n   150  12.7646  3    550.634     7.17            881.40             99.19                     870.61   29.486   2.5804   0.0818   0.8586\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n   151  19.2729  3    569.907     5.45            881.19             99.39                     872.42   29.860   2.6293   0.0497   0.8058\n   152  33.7814  6    603.689     3.62            882.19             99.59                     875.11   30.333   3.1368   0.0636   1.0862\n   153  55.3605  6    659.049     2.33            883.52             99.74                     877.58   31.009   3.0602   0.1079   1.3546\n   154  75.1431  6    734.192     1.69            884.18             99.81                     878.96   32.025   2.5624   0.1233   1.1474\n   155  96.2305  6    830.423     2.43            861.76             99.72                     880.68   36.775   2.3832   0.1597   1.0127\n   156 108.7503  6    939.173    19.78            818.89             97.64                     880.10   46.286   5.6488   0.0975   2.3844\n   157 153.7716  6   1092.945    35.90            808.02             95.75                     879.34   61.283   5.8612   0.0865   2.4203\n   158   2.0552  2   1095.000    11.58            870.57             98.69                     878.72   61.225   8.6758   0.0821   3.5146\n   159   3.0987  2   1098.099     4.93            878.91             99.44                     878.91   61.287   8.5969   0.0320   3.4824\n   160   5.9591  6   1104.058     2.80            877.20             99.68                     879.89   61.518   5.3457   0.0167   2.2054\n   161  11.9183  6   1115.976     2.98            866.46             99.66                     880.97   62.273   2.5911   0.0109   1.0847\n   162  23.8366  6   1139.813     8.99            853.60             98.96                     880.47   64.362   5.1074   0.0387   2.1281\n   163  44.2161  6   1184.029    19.21            840.39             97.77                     879.60   70.165   4.6908   0.0448   1.9198\n   164  79.4419  6   1263.471    35.28            822.75             95.89                     879.05   85.272   3.5492   0.0637   1.4301\n   165 130.1039  6   1393.575    51.52            811.62             94.03                     878.66   90.517   3.4138   0.0860   1.3592\n   166 192.9464  6   1586.521    63.12            800.88             92.69                     878.49   93.273   3.0713   0.1148   1.2085\n   167 254.9848  6   1841.506    82.70            775.97             90.37                     878.34   95.522   2.2838   0.0795   0.9385\n   168 365.0000  6   2206.506    98.43            764.23             88.59                     878.07   97.077   2.7854   0.0504   1.2425\n   169 365.0000  6   2571.506   103.59            766.55             88.10                     877.60   97.822   3.6707   0.0307   1.6161\n   170 365.0000  6   2936.506   112.36            766.17             87.21                     877.33   98.269   3.2131   0.0367   1.3951\n   171 365.0000  6   3301.506   107.55            774.94             87.81                     877.33   98.550   2.9484   0.0420   1.2648\n   172 348.4941  6   3650.000   103.23            781.38             88.33                     877.97   98.744   2.0596   0.0450   0.8750\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                 18.590s    99.61%\n|- Newton                                18.195s    97.88%\n  |- Jacobian                            14.550s    79.96%\n  |- Update                               3.429s    18.85%\n  |- Solver                               0.071s     0.39%\n  |- Residual                             0.069s     0.38%\n  |- Logging                              0.006s     0.03%\n|- Output                                 0.369s     1.99%\n|- Input                                  0.000s     0.00%\nInitialization                            0.073s     0.39%\n------------------------------------------------------------\nTOTAL                                    18.663s\n============================================================\n\n\n')
```

## stflu002.dat

5000x5000x50, 2D diagonal water flooding in uniformed cartesian

```
Running simulation: Uniformed cartesian water flooding

    50  84.4290  1   3650.000  3931.77             69.97              1.75                    3998.01    6.192  40.5650   0.0127   0.0123



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  4.580s    98.51%

|- Newton                                 4.485s    97.93%

  |- Jacobian                             3.415s    76.15%

  |- Update                               0.964s    21.49%

  |- Solver                               0.059s     1.31%

  |- Residual                             0.023s     0.51%

  |- Logging                              0.002s     0.05%

|- Output                                 0.086s     1.88%

|- Input                                  0.000s     0.00%

Initialization                            0.069s     1.49%

------------------------------------------------------------

TOTAL                                     4.649s

============================================================





```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//stflu002.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/stflu002.dat\n', stderr='unknown keyword: mxcnrpt\n[MacBook-Air.local:21656] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/3871408128/sm_segment.MacBook-Air.501.e6c10000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1 1.00e-05  1    1.0e-05  4000.00                                                        4000.00    0.000   0.0120 5.99e-08 4.12e-06\n     2 2.33e-05  1    3.3e-05  4000.00                                                        4000.00    0.000   0.0279 1.40e-07 9.62e-06\n     3 5.44e-05  1    8.8e-05  4000.00                                                        4000.00    0.000   0.0651 3.26e-07 2.24e-05\n     4 1.27e-04  1    2.1e-04  4000.00                                                        4000.00    0.000   0.1517 7.60e-07 5.23e-05\n     5 2.96e-04  1    5.1e-04  4000.00                                                        4000.00    0.000   0.3535 1.77e-06 1.22e-04\n     6 6.89e-04  1      0.001  4000.00                                                        4000.00    0.000   0.8221 4.13e-06 2.83e-04\n     7 1.60e-03  1      0.003  4000.00                                                        4000.00    0.000   1.9037 9.57e-06 6.56e-04\n     8 3.68e-03  1      0.006  4000.00                                                        3999.99    0.000   4.3648 2.21e-05   0.0015\n     9 8.35e-03  2      0.015  4000.00                                                        4000.00    0.000   9.7879 5.00e-05   0.0034\n    10   0.0183  2      0.033  4000.00                                                        4000.00    0.000  20.9359 1.10e-04   0.0072\n    11   0.0375  2      0.071  4000.00                                                        4000.00    0.000  40.8990 2.24e-04   0.0141\n    12   0.0687  2      0.139  3999.05                                                        3998.83    0.002  69.1048 4.11e-04   0.0238\n    13   0.1097  2      0.249  3999.50                                                        3999.43    0.000  97.9346 6.56e-04   0.0338\n    14   0.1549  2      0.404  3999.13                                                        3999.49    3.174 108.7784 8.49e-04   0.0375\n    15   0.2094  1      0.613  3999.07                                                        4003.76   22.521  54.3892 5.03e-04   0.0186\n    16   0.3586  5      0.972  4000.00                                                        4000.00   14.211 196.8130   0.0021   0.0675\n    17   0.3619  3      1.334  4000.55                                                        3998.77   10.356 155.6747   0.0021   0.0533\n    18   0.4144  4      1.748  4000.00                                                        4000.01    7.901 140.8114   0.0024   0.0483\n    19   0.4988  4      2.247  3999.99                                                        4000.01    6.147 134.4639   0.0029   0.0461\n    20   0.6137  4      2.861  4000.00                                                        4000.00    4.828 131.4993   0.0036   0.0449\n    21   0.7630  4      3.624  4000.00                                                        4000.00    3.812 129.8846   0.0044   0.0442\n    22   0.9542  4      4.578  4000.00                                                        4000.00    3.017 129.0092   0.0054   0.0436\n    23   1.1969  4      5.775  4000.00                                                        4000.00    2.392 128.5394   0.0067   0.0431\n    24   1.5040  4      7.279  4000.00                                                        4000.00    1.898 128.2426   0.0083   0.0426\n    25   1.8919  4      9.171  4000.00                                                        4000.00    1.506 127.8614   0.0102   0.0419\n    26   2.3831  4     11.554  4000.00                                                        4000.00    1.196 127.0066   0.0126   0.0409\n    27   3.0110  4     14.565  4000.00                                                        4000.00    0.948 125.0509   0.0154   0.0407\n    28   3.8315  4     18.396  4000.00                                                        4000.00    0.751 121.1202   0.0189   0.0397\n    29   4.9462  4     23.343  4000.01                                                        4000.00    0.592 114.1835   0.0232   0.0376\n    30   6.5530  4     29.895  4000.00                                                        4000.00    0.462 103.1756   0.0289   0.0336\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31   9.0591  1     38.955  3988.66                                                        4041.29    8.459  54.3892   0.0244   0.0168\n    32  15.5129  5     54.467  4000.00             5e-11             1e-12                    3999.99    6.054  88.6744   0.0576   0.0301\n    33  22.7487  4     77.216  4000.00             4e-11             1e-12                    4000.00    4.273  53.3431   0.0724   0.0356\n    34  35.7936  5    113.010  4000.00             3e-07             7e-09                    4000.00    2.920  91.7571   0.0923   0.0669\n    35  51.7071  5    164.717  4000.01             8e-10             2e-11                    3999.99    2.004 121.9271   0.1030   0.0918\n    36  66.5527  5    231.270  4000.02                                                        4000.01    1.428 120.6442   0.0996   0.1010\n    37  86.0667  5    317.336  4000.00                                                        4000.00    1.041 115.8938   0.0931   0.1069\n    38  47.6637  3    365.000  4000.00             2e-04             4e-06                    4000.00    0.905  54.5454   0.0446   0.0555\n    39  81.5579  5    446.558  4000.00             1e-04             3e-06                    4000.00    0.740  71.5580   0.0680   0.0738\n    40 128.8389  5    575.397  3999.99             3e-04             7e-06                    4000.00    0.704  83.5026   0.0898   0.0837\n    41 188.0542  6    763.451  3999.99             1e-03             2e-05                    4000.00    0.841  79.6801   0.1027   0.0751\n    42 260.4467  6   1023.898  3999.97              0.03             7e-04                    4000.00    1.023  92.5824   0.1092   0.0858\n    43 351.6733  7   1375.571  3999.70              0.30              0.01                    4000.00    1.291 126.3640   0.1187   0.0977\n    44 365.0000  7   1740.571  3998.47              1.54              0.04                    3999.98    1.703 134.7543   0.0977   0.0903\n    45 365.0000  4   2105.571  3996.26              3.96              0.10                    3999.97    2.194 138.3716   0.0851   0.0833\n    46 365.0000  3   2470.571  3990.49             10.25              0.26                    3999.81    2.836 144.3345   0.0761   0.0787\n    47 365.0000  3   2835.571  3981.36             21.02              0.53                    3998.11    3.590 143.2971   0.0653   0.0699\n    48 365.0000  4   3200.571  3959.95             40.04              1.00                    4000.02    4.378 165.1319   0.0598   0.0620\n    49 365.0000  3   3565.571  3938.16             62.90              1.57                    3999.72    5.262 163.0792   0.0557   0.0558\n    50  84.4290  1   3650.000  3931.77             69.97              1.75                    3998.01    6.192  40.5650   0.0127   0.0123\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                  4.580s    98.51%\n|- Newton                                 4.485s    97.93%\n  |- Jacobian                             3.415s    76.15%\n  |- Update                               0.964s    21.49%\n  |- Solver                               0.059s     1.31%\n  |- Residual                             0.023s     0.51%\n  |- Logging                              0.002s     0.05%\n|- Output                                 0.086s     1.88%\n|- Input                                  0.000s     0.00%\nInitialization                            0.069s     1.49%\n------------------------------------------------------------\nTOTAL                                     4.649s\n============================================================\n\n\n')
```



## stflu003.dat

5000x5000x50, 2D diagonal water flooding in uniformed corner point

```
Running simulation: uniformed corner grid

    49 172.0209  2   3650.000  3929.82             70.28              1.76                    4000.13    5.176  72.9820   0.0260   0.0222



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  3.731s    98.31%

|- Newton                                 3.639s    97.53%

  |- Jacobian                             2.737s    75.22%

  |- Update                               0.817s    22.46%

  |- Solver                               0.045s     1.24%

  |- Residual                             0.019s     0.53%

  |- Logging                              0.002s     0.05%

|- Output                                 0.083s     2.24%

|- Input                                  0.000s     0.00%

Initialization                            0.064s     1.69%

------------------------------------------------------------

TOTAL                                     3.795s

============================================================





```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//stflu003.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/stflu003.dat\n', stderr='unknown keyword: mxcnrpt\n[MacBook-Air.local:21671] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/2820145152/sm_segment.MacBook-Air.501.a8180000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1 1.00e-05  1    1.0e-05  4000.00                                                        4000.00    0.000   0.0120 5.99e-08 4.12e-06\n     2 2.33e-05  1    3.3e-05  4000.00                                                        4000.00    0.000   0.0279 1.40e-07 9.61e-06\n     3 5.44e-05  1    8.8e-05  4000.00                                                        4000.00    0.000   0.0650 3.26e-07 2.24e-05\n     4 1.27e-04  1    2.1e-04  4000.00                                                        4000.00    0.000   0.1517 7.60e-07 5.23e-05\n     5 2.96e-04  1    5.1e-04  4000.00                                                        4000.00    0.000   0.3532 1.77e-06 1.22e-04\n     6 6.89e-04  1      0.001  4000.00                                                        4000.00    0.000   0.8208 4.13e-06 2.83e-04\n     7 1.60e-03  1      0.003  4000.00                                                        4000.00    0.000   1.8966 9.57e-06 6.54e-04\n     8 3.68e-03  1      0.006  4000.00                                                        3999.95    0.000   4.3276 2.21e-05   0.0015\n     9 8.35e-03  2      0.015  4000.00                                                        4000.00    0.000   9.6030 5.00e-05   0.0033\n    10   0.0183  2      0.033  4000.00                                                        4000.00    0.000  20.1087 1.10e-04   0.0069\n    11   0.0377  2      0.071  4000.00                                                        4000.00    0.000  37.8546 2.26e-04   0.0131\n    12   0.0702  2      0.141  3999.96                                                        3999.96    0.000  60.7790 4.20e-04   0.0210\n    13   0.1166  2      0.258  3999.53                                                        3999.46    0.001  81.5647 6.97e-04   0.0281\n    14   0.1762  1      0.434  3999.37                                                        4001.86   17.232  54.3892 6.06e-04   0.0187\n    15   0.3018  2      0.736  3996.77                                                        3997.71   15.687 108.7784   0.0016   0.0375\n    16   0.4082  3      1.144  3999.94                                                        3999.92   10.089 121.6029   0.0024   0.0416\n    17   0.5260  3      1.670  4000.00                                                        4000.00    6.911 107.1526   0.0031   0.0368\n    18   0.7160  4      2.386  3999.99                                                        4000.00    4.837 101.4354   0.0042   0.0346\n    19   0.9966  4      3.383  4000.01                                                        3999.99    3.412  98.7150   0.0057   0.0335\n    20   1.4025  4      4.785  4000.00                                                        4000.00    2.412  97.1459   0.0079   0.0327\n    21   1.9861  4      6.771  4000.00                                                        4000.01    1.704  95.1358   0.0110   0.0316\n    22   2.8357  4      9.607  4000.00                                                        4000.00    1.201  90.5871   0.0152   0.0298\n    23   4.1254  4     13.732  3999.99                                                        4000.01    0.840  81.0786   0.0212   0.0271\n    24   6.2484  4     19.981  4000.00                                                        4000.00    0.578  64.9877   0.0303   0.0221\n    25  10.1724  2     30.153  3998.35             7e-15                                      4000.12    0.383  44.2309   0.0448   0.0150\n    26  18.2770  3     48.430  4000.00             3e-10             7e-12                    4000.00    0.238  26.2761   0.0697   0.0171\n    27  29.1156  4     77.546  4000.00                                                        4000.00    0.149  48.6466   0.0913   0.0316\n    28  42.2313  4    119.777  4000.00             1e-05             3e-07                    4000.00    0.096  58.8445   0.1039   0.0411\n    29  58.2063  5    177.983  4000.00             1e-04             3e-06                    4000.00    0.113  60.1840   0.1080   0.0476\n    30  78.9676  5    256.951  4000.01             6e-05             2e-06                    4000.01    0.148  54.8418   0.1069   0.0510\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31 107.5887  4    364.540  4000.01             4e-05             1e-06                    3999.99    0.189  50.1557   0.0999   0.0537\n    32   0.4604  1    365.000  4002.04             4e-05             1e-06                    4002.22    0.246   0.1433 4.28e-04 1.71e-04\n    33   1.0713  1    366.071  4000.07             4e-05             1e-06                    4000.14    0.247   0.5017 9.94e-04 5.93e-04\n    34   2.4832  1    368.554  3999.97             4e-05             1e-06                    3999.99    0.248   1.0022   0.0023   0.0013\n    35   5.7068  1    374.261  4001.39             4e-05             9e-07                    4000.76    0.250   2.0557   0.0052   0.0027\n    36  12.8661  1    387.127  3999.91             3e-05             9e-07                    3999.85    0.255   4.5825   0.0116   0.0058\n    37  27.8637  1    414.991  4003.09             3e-05             8e-07                    4003.32    0.266   8.7233   0.0243   0.0102\n    38  55.9535  4    470.945  4000.00             2e-05             5e-07                    3999.99    0.288  17.9252   0.0449   0.0229\n    39 100.4866  5    571.431  4000.02             1e-05             3e-07                    4000.00    0.324  30.7405   0.0701   0.0285\n    40 159.8226  6    731.254  3999.97             7e-04             2e-05                    4000.01    0.384  48.9171   0.0905   0.0393\n    41 232.5680  5    963.822  4000.00              0.01             2e-04                    4000.00    0.478  71.5362   0.1011   0.0497\n    42 324.1574  5   1287.979  3999.86              0.14              0.00                    4000.00    0.631 101.7002   0.1145   0.0612\n    43 365.0000  4   1652.979  3999.12              0.89              0.02                    4000.00    0.908 118.1691   0.1039   0.0636\n    44 365.0000  3   2017.979  3996.55              3.51              0.09                    3999.89    1.362 123.1660   0.0887   0.0607\n    45 365.0000  3   2382.979  3992.10              7.94              0.20                    4000.05    1.949 127.8114   0.0779   0.0563\n    46 365.0000  3   2747.979  3981.63             18.44              0.46                    3999.37    2.661 134.9548   0.0677   0.0462\n    47 365.0000  3   3112.979  3965.41             34.73              0.87                    3999.90    3.460 142.8107   0.0615   0.0457\n    48 365.0000  3   3477.979  3942.87             57.73              1.44                    3999.20    4.322 145.2569   0.0564   0.0436\n    49 172.0209  2   3650.000  3929.82             70.28              1.76                    4000.13    5.176  72.9820   0.0260   0.0222\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                  3.731s    98.31%\n|- Newton                                 3.639s    97.53%\n  |- Jacobian                             2.737s    75.22%\n  |- Update                               0.817s    22.46%\n  |- Solver                               0.045s     1.24%\n  |- Residual                             0.019s     0.53%\n  |- Logging                              0.002s     0.05%\n|- Output                                 0.083s     2.24%\n|- Input                                  0.000s     0.00%\nInitialization                            0.064s     1.69%\n------------------------------------------------------------\nTOTAL                                     3.795s\n============================================================\n\n\n')
```

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
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

    78  10.3832  1   3650.000  3876.28            123.81              3.10                    3999.97   15.288  17.7000   0.0036   0.0106



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                 31.789s    99.77%

|- Newton                                31.497s    99.08%

  |- Jacobian                            22.374s    71.04%

  |- Update                               8.572s    27.21%

  |- Solver                               0.252s     0.80%

  |- Residual                             0.132s     0.42%

  |- Logging                              0.010s     0.03%

|- Output                                 0.275s     0.87%

|- Input                                  0.000s     0.00%

Initialization                            0.074s     0.23%

------------------------------------------------------------

TOTAL                                    31.863s

============================================================





```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//stflu004.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/stflu004.dat\n', stderr='[MacBook-Air.local:21684] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/947453952/sm_segment.MacBook-Air.501.38790000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1 1.00e-05  1    1.0e-05  4000.00                                                        3999.50    0.000   0.3821 1.92e-06 1.32e-04\n     2 2.33e-05  1    3.3e-05  4000.00                                                        3998.58    0.000   0.8868 4.46e-06 3.06e-04\n     3 5.40e-05  1    8.7e-05  4000.00                                                        3996.59    0.000   2.0441 1.03e-05 7.05e-04\n     4 1.24e-04  2    2.1e-04  4000.00                                                        4000.00    0.000   4.6478 2.38e-05   0.0016\n     5 2.81e-04  2    4.9e-04  4000.00                                                        4000.00    0.000  10.2136 5.39e-05   0.0035\n     6 6.14e-04  2      0.001  4000.00                                                        4000.00    0.000  20.9652 1.18e-04   0.0072\n     7 1.26e-03  2      0.002  4000.00                                                        4000.00    0.000  38.0663 2.41e-04   0.0131\n     8 2.34e-03  2      0.005  4000.00                                                        3999.99    0.000  57.8572 4.48e-04   0.0199\n     9 3.94e-03  3      0.009  4000.00                                                        4000.00    0.000  72.4106 7.55e-04   0.0250\n    10 6.20e-03  3      0.015  4000.00                                                        4000.00    0.000  77.3055   0.0012   0.0266\n    11 9.55e-03  3      0.024  4000.00                                                        4000.00    0.000  74.6039   0.0018   0.0257\n    12   0.0149  3      0.039  4000.00                                                        4000.00    0.000  68.7703   0.0028   0.0237\n    13   0.0238  3      0.063  4000.00                                                        4000.00    0.000  63.3919   0.0045   0.0218\n    14   0.0391  3      0.102  4000.00                                                        4000.00    0.000  60.1116   0.0073   0.0206\n    15   0.0651  2      0.167  4001.36                                                        3998.75    0.000  58.6345   0.0121   0.0200\n    16   0.1091  2      0.276  4000.77                                                        3999.69    0.000  58.5467   0.0199   0.0199\n    17   0.1832  2      0.460  4000.01                                                        3999.76    0.000  58.4784   0.0322   0.0201\n    18   0.3075  1      0.767  3998.63                                                        3996.52    2.283  54.3892   0.0481   0.0194\n    19   0.5266  2      1.294  3999.53                                                        3999.49    1.353  59.8994   0.0796   0.0220\n    20   0.8026  1      2.096  4001.27                                                        3999.34    0.831  50.4921   0.1052   0.0193\n    21   1.1006  1      3.197  4000.14                                                        3999.59    0.549  37.0226   0.1191   0.0148\n    22   1.4315  2      4.628  4000.00                                                        4000.00    0.380  23.7997   0.1215   0.0104\n    23   1.8451  1      6.473  3999.97                                                        3999.96    0.273  13.5303   0.1157   0.0116\n    24   2.4304  1      8.904  4000.00                                                        3999.89    0.203   7.3433   0.1040   0.0199\n    25   3.3494  1     12.253  4000.02                                                        3999.99    0.147   4.3159   0.0932   0.0306\n    26   4.8213  2     17.075  4000.00                                                        3999.99    0.106   3.5117   0.1212   0.0515\n    27   6.2227  2     23.297  4000.01                                                        4000.01    0.077   3.7395   0.1293   0.0534\n    28   7.7976  2     31.095  4000.00                                                        4000.00    0.058   4.5119   0.1232   0.0458\n    29   9.9889  2     41.084  4000.00                                                        4000.00    0.044   5.7741   0.1108   0.0343\n    30  13.4065  2     54.490  3999.97                                                        3999.99    0.033   7.7313   0.1336   0.0227\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31  16.5438  2     71.034  3999.99                                                        3999.97    0.025   9.4985   0.1341   0.0254\n    32  20.3835  3     91.417  4000.00                                                        3999.98    0.020  11.6888   0.1232   0.0274\n    33  26.1146  1    117.532  4000.00                                                        4000.00    0.025  14.9313   0.1390   0.0233\n    34  31.6247  3    149.157  4000.01                                                        3999.98    0.031  18.1488   0.1350   0.0217\n    35  38.8438  5    188.001  4000.00             3e-15                                      4000.00    0.039  22.3833   0.1420   0.0161\n    36  46.5590  5    234.560  4000.00             2e-13             4e-15                    4000.00    0.050  26.9750   0.1382   0.0174\n    37  18.8451  1 1  253.405  3999.88             3e-13             7e-15                    4000.23    0.068  11.0282   0.0523   0.0068\n    38  32.6040  5    286.009  3999.99             8e-13             2e-14                    4000.00    0.078  19.0594   0.0854   0.0112\n    39  48.4814  4    334.490  4000.00             1e-11             2e-13                    4000.00    0.094  28.5653   0.1091   0.0157\n    40  30.5099  5    365.000  4000.00             2e-11             6e-13                    4000.00    0.121  18.1211   0.0657   0.0100\n    41  49.5097  4    414.510  4000.00             2e-10             4e-12                    4000.00    0.144  29.6325   0.0973   0.0166\n    42  70.0718  7    484.581  3999.99             4e-09             1e-10                    4000.03    0.183  42.4721   0.1193   0.0243\n    43  30.3581  6 1  514.940  4000.00             8e-09             2e-10                    3999.97    0.249  18.5975   0.0502   0.0116\n    44  53.0662  2    568.006  4000.00             3e-08             6e-10                    4000.00    0.303  32.8242   0.0804   0.0207\n    45  80.6019  2    648.608  3999.99             3e-07             7e-09                    4000.00    0.402  50.6215   0.1114   0.0325\n    46  35.9779  4 1  684.585  4000.00             5e-07             1e-08                    3999.99    0.560  22.9164   0.0478   0.0156\n    47  63.6589  6    748.244  3999.99             1e-06             4e-08                    4000.00    0.663  41.0501   0.0769   0.0275\n    48  98.1767  3    846.421  4000.01             1e-05             3e-07                    4000.01    0.828  64.5632   0.1099   0.0446\n    49 132.2126  3    978.634  4000.00             2e-04             5e-06                    4000.00    1.087  89.5501   0.1308   0.0622\n    50 164.8001  6   1143.434  4000.00              0.00             7e-05                    4000.00    1.449 116.1128   0.1405   0.0829\n    51 198.5775  4   1342.011  3999.97              0.03             7e-04                    3999.97    1.932 147.1191   0.1464   0.1041\n    52 233.9201  8   1575.931  3999.82              0.20              0.00                    3999.99    2.556 184.5100   0.1500   0.1338\n    53 244.7521 10   1820.684  3999.16              0.86              0.02                    3999.99    3.365 207.6047   0.1390   0.1515\n    54   8.8722  5 3 1829.556  3999.11              0.89              0.02                    4000.00    4.391   7.8883   0.0050   0.0060\n    55   6.5558  1 1 1836.112  3999.10              0.91              0.02                    3999.95    4.441   5.7966   0.0037   0.0038\n    56  14.7278  5   1850.839  3999.05              0.95              0.02                    4000.01    4.470  13.0955   0.0083   0.0099\n    57  31.6056  7   1882.445  3998.96              1.05              0.03                    4000.01    4.535  28.3111   0.0177   0.0212\n    58  54.1810  8   1936.626  3998.75              1.26              0.03                    4000.00    4.679  49.1945   0.0300   0.0366\n    59  27.0906  6 1 1963.717  3998.63              1.38              0.03                    4000.01    4.951  24.9214   0.0149   0.0187\n    60  54.1811  7   2017.898  3998.35              1.65              0.04                    4000.02    5.074  50.5260   0.0292   0.0378\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    61  92.8819  6   2110.780  3997.73              2.27              0.06                    4000.00    5.325  88.7020   0.0479   0.0661\n    62 136.1894  3   2246.969  3996.32              3.69              0.09                    3999.99    5.800 134.9687   0.0681   0.0955\n    63 167.2685  4   2414.238  3993.45              6.55              0.16                    3999.97    6.479 174.6838   0.0781   0.1258\n    64 180.3107 12   2594.548  3988.35             11.66              0.29                    3999.99    7.320 200.1126   0.0804   0.1477\n    65 180.2527 11   2774.801  3980.45             19.57              0.49                    3999.99    8.279 213.3916   0.0757   0.1558\n    66 173.6101 10   2948.411  3969.40             30.61              0.77                    4000.00    9.294 219.3012   0.0700   0.1607\n    67 164.5366 10   3112.948  3955.08             44.93              1.12                    4000.00   10.324 221.3796   0.0630   0.1614\n    68 155.0645 11   3268.012  3937.49             62.52              1.56                    4000.01   11.346 221.6805   0.0579   0.1614\n    69 146.0194 12   3414.032  3916.74             83.27              2.08                    4000.00   12.350 221.1514   0.0523   0.1611\n    70   5.1000  6 3 3419.132  3916.01             84.00              2.10                    4000.00   13.593   7.9889   0.0018   0.0059\n    71  10.1999  6   3429.332  3914.52             85.47              2.14                    4000.00   13.619  16.0025   0.0036   0.0117\n    72  20.3998  6   3449.731  3911.49             88.52              2.21                    4000.00   13.672  32.1961   0.0072   0.0235\n    73  39.1882 13   3488.920  3905.33             94.68              2.37                    4000.00   13.780  62.5536   0.0138   0.0456\n    74  12.0579  6 1 3500.978  3903.39             96.61              2.42                    4000.00   14.116  19.4525   0.0042   0.0142\n    75  24.1159  6   3525.093  3899.41            100.59              2.51                    4000.00   14.177  39.1806   0.0085   0.0286\n    76  44.6164  2   3569.710  3891.61            108.40              2.71                    3999.98   14.339  73.3790   0.0156   0.0497\n    77  69.9069  3   3639.617  3878.22            121.79              3.04                    4000.02   14.625 117.6288   0.0242   0.0828\n    78  10.3832  1   3650.000  3876.28            123.81              3.10                    3999.97   15.288  17.7000   0.0036   0.0106\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                 31.789s    99.77%\n|- Newton                                31.497s    99.08%\n  |- Jacobian                            22.374s    71.04%\n  |- Update                               8.572s    27.21%\n  |- Solver                               0.252s     0.80%\n  |- Residual                             0.132s     0.42%\n  |- Logging                              0.010s     0.03%\n|- Output                                 0.275s     0.87%\n|- Input                                  0.000s     0.00%\nInitialization                            0.074s     0.23%\n------------------------------------------------------------\nTOTAL                                    31.863s\n============================================================\n\n\n')
```

![png]({{ "/assets/images/benchmark_image_42.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_43.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_44.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_45.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_46.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_47.png" | relative_url }})

## stflu005.dat

steam injection in corner-point grid

```
Running simulation: Steam injection Corner point

    28  55.0000  6   3650.000   440.51             12.88              2.84                      49.82    0.029   0.4281 9.63e-07 2.73e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                 44.436s    99.68%

|- Newton                                43.976s    98.96%

  |- Jacobian                            33.727s    76.69%

  |- Update                               9.733s    22.13%

  |- Residual                             0.198s     0.45%

  |- Solver                               0.135s     0.31%

  |- Logging                              0.004s     0.01%

|- Output                                 0.445s     1.00%

|- Input                                  0.000s     0.00%

Initialization                            0.141s     0.32%

------------------------------------------------------------

TOTAL                                    44.578s

============================================================





```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//stflu005.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/stflu005.dat\n', stderr='[MacBook-Air.local:21804] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/2074345472/sm_segment.MacBook-Air.501.7ba40000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1   1.0000  6      1.000   440.56             12.88              2.84                      49.82    0.000 2.42e+03 6.71e-08 2.41e-05\n     2   0.1360  6      1.136   440.56             12.88              2.84                      49.82    0.000   0.0049 1.08e-08 3.91e-06\n     3   0.2720  6      1.408   440.56             12.88              2.84                      49.82    0.000   0.0098 2.16e-08 7.80e-06\n     4   0.5441  6      1.952   440.56             12.88              2.84                      49.82    0.000   0.0195 4.30e-08 1.55e-05\n     5   1.0882  6      3.040   440.56             12.88              2.84                      49.82    0.000   0.0385 8.50e-08 3.06e-05\n     6   2.1764  6      5.217   440.56             12.88              2.84                      49.82    0.000   0.0736 1.63e-07 5.81e-05\n     7   4.3528  6      9.570   440.56             12.88              2.84                      49.82    0.000   0.1291 2.86e-07 1.01e-04\n     8   8.7055  6     18.275   440.56             12.88              2.84                      49.82    0.000   0.2075 4.60e-07 1.59e-04\n     9  17.4111  6     35.686   440.56             12.88              2.84                      49.82    0.000   0.2984 6.63e-07 2.21e-04\n    10  34.8222  6     70.508   440.56             12.88              2.84                      49.82    0.001   0.3837 8.58e-07 2.64e-04\n    11  69.6443  6    140.153   440.56             12.88              2.84                      49.82    0.001   0.4509 1.02e-06 2.73e-04\n    12 139.2887  6    279.441   440.56             12.88              2.84                      49.82    0.002   0.5000 1.15e-06 2.44e-04\n    13 278.5774  6    558.019   440.55             12.88              2.84                      49.82    0.005   0.5387 1.28e-06 2.10e-04\n    14  36.9813  6    595.000   440.55             12.88              2.84                      49.82    0.005   0.3899 8.72e-07 2.66e-04\n    15  73.9626  6    668.963   440.55             12.88              2.84                      49.82    0.005   0.4554 1.03e-06 2.72e-04\n    16 147.9252  6    816.888   440.55             12.88              2.84                      49.82    0.007   0.5031 1.16e-06 2.39e-04\n    17 278.1122  6   1095.000   440.54             12.88              2.84                      49.82    0.009   0.5381 1.28e-06 2.10e-04\n    18 365.0000  6   1460.000   440.54             12.88              2.84                      49.82    0.012   0.5512 1.33e-06 2.43e-04\n    19 135.0000  6   1595.000   440.54             12.88              2.84                      49.82    0.013   0.4972 1.14e-06 2.45e-04\n    20 270.0000  6   1865.000   440.53             12.88              2.84                      49.82    0.015   0.5362 1.27e-06 2.06e-04\n    21 230.0000  6   2095.000   440.53             12.88              2.84                      49.82    0.017   0.5261 1.24e-06 2.01e-04\n    22 365.0000  6   2460.000   440.53             12.88              2.84                      49.82    0.020   0.5506 1.32e-06 2.43e-04\n    23 135.0000  6   2595.000   440.52             12.88              2.84                      49.82    0.021   0.4966 1.14e-06 2.45e-04\n    24 270.0000  6   2865.000   440.52             12.88              2.84                      49.82    0.023   0.5356 1.27e-06 2.06e-04\n    25 230.0000  6   3095.000   440.52             12.88              2.84                      49.82    0.025   0.5255 1.23e-06 2.01e-04\n    26 365.0000  6   3460.000   440.51             12.88              2.84                      49.82    0.028   0.5500 1.32e-06 2.43e-04\n    27 135.0000  6   3595.000   440.51             12.88              2.84                      49.82    0.029   0.4960 1.14e-06 2.45e-04\n    28  55.0000  6   3650.000   440.51             12.88              2.84                      49.82    0.029   0.4281 9.63e-07 2.73e-04\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                 44.436s    99.68%\n|- Newton                                43.976s    98.96%\n  |- Jacobian                            33.727s    76.69%\n  |- Update                               9.733s    22.13%\n  |- Residual                             0.198s     0.45%\n  |- Solver                               0.135s     0.31%\n  |- Logging                              0.004s     0.01%\n|- Output                                 0.445s     1.00%\n|- Input                                  0.000s     0.00%\nInitialization                            0.141s     0.32%\n------------------------------------------------------------\nTOTAL                                    44.578s\n============================================================\n\n\n')
```

# SPE4C


## Run & Load

```
Running simulation: SPE4-C benchmark on live oil

   190 208.3182  3   3650.000     0.03             27.22             99.89                      27.02   42.160   0.5504   0.0075   6.9417



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                               1m 40.31s    99.92%

|- Newton                              1m 39.69s    99.38%

  |- Jacobian                          1m 24.66s    84.93%

  |- Update                              12.612s    12.65%

  |- Solver                               1.830s     1.84%

  |- Residual                             0.210s     0.21%

  |- Logging                              0.023s     0.02%

|- Output                                 0.568s     0.57%

|- Input                                  0.000s     0.00%

Initialization                            0.078s     0.08%

------------------------------------------------------------

TOTAL                                  1m 40.38s

============================================================





```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//stspe003.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/stspe003.dat\n', stderr='[MacBook-Air.local:21994] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/238354432/sm_segment.MacBook-Air.501.e350000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1   0.1000  1      0.100   117.45             2e-07             2e-07                      37.50    0.032  28.5124 8.62e-04  11.6743\n     2   0.1779  1      0.278    98.27              0.03              0.03                      37.50    0.031  13.7857   0.0437  19.6670\n     3   0.2724  2      0.550    87.97              0.04              0.05                      37.50    0.031   6.4611   0.0563  28.2382\n     4   0.3625  2      0.913    82.29              0.05              0.06                      37.50    0.031   4.9358   0.0501  35.0923\n     5   0.4370  2      1.350    78.71              0.05              0.06                      37.50    0.031   3.9950   0.0389  39.3831\n     6   0.4973  2      1.847    76.13              0.05              0.07                      37.50    0.031   2.9592   0.0295  41.5469\n     7   0.5505  2      2.398    74.08              0.05              0.07                      37.50    0.031   1.7496   0.0233  42.3574\n     8   0.6032  4      3.001    72.52              0.05              0.08                      37.50    0.031  41.8869   0.2080  24.8885\n     9   0.5897  2      3.590    71.45              0.06              0.08                      37.50    0.034   5.8908   0.0881  14.4982\n    10   0.8668  2      4.457    70.23              0.06              0.08                      37.50    0.044  12.1976   0.0390  20.0194\n    11   1.3186  2      5.776    68.56              0.06              0.08                      37.50    0.060   8.8015   0.0267  27.6476\n    12   1.7711  2      7.547    66.37              0.06              0.09                      37.50    0.084   5.2919   0.0304  34.1935\n    13   2.1615  1      9.708    63.86              0.06              0.09                      37.50    0.132   4.6815   0.0338  37.9068\n    14   2.5082  1     12.217    61.25              0.06              0.09                      37.50    0.199   3.7300   0.0255  40.5000\n    15   2.8136  1     15.030    58.64              0.06              0.10                      37.51    0.288   3.5084   0.0267  40.5000\n    16   3.1563  3     18.187    59.98              0.06              0.10                      37.50    0.362  26.7546   0.2718  43.1320\n    17   2.6193  4     20.806    60.50              0.06              0.09                      37.50    0.455  10.1823   0.1939  28.3395\n    18   2.6659  2     23.472    59.87              0.06              0.10                      37.50    0.537   7.2155   0.0918  25.9938\n    19   3.6738  2     27.146    57.82              0.06              0.10                      37.50    0.622   8.3806   0.0447  32.1804\n    20   4.6133  2     31.759    54.91              0.06              0.10                      37.50    0.738   5.8568   0.0236  36.6835\n    21   5.4415  3     37.200    54.49              0.06              0.10                      37.50    0.882   5.9530   0.1679  34.2239\n    22   5.9907  2     43.191    54.26              0.06              0.11                      37.50    1.059   1.4396   0.1062  36.6362\n    23   7.0706  3     50.262    57.23              0.06              0.10                      37.50    1.259  12.0953   0.1895  31.7032\n    24   7.2893  2     57.551    56.56              0.08              0.15                      37.50    1.495   4.0586   0.1137  35.1506\n    25   8.7792  2     66.330    52.39              0.44              0.84                      37.50    1.736   6.7075   0.0487  43.4150\n    26   9.4936  4     75.824    47.70              2.02              4.07                      37.50    2.013   4.1790   0.1833  44.3823\n    27   9.9688  3     85.793    48.73              5.14              9.55                      37.50    2.318  10.1888   0.1718  36.6921\n    28  10.8436  3     96.636    48.77              9.10             15.72                      37.50    2.634   4.2913   0.1625  31.3069\n    29  12.1436  2    108.780    45.25             11.63             20.45                      37.50    2.978   4.0112   0.1239  42.5892\n    30  13.2672  3    122.047    41.64             13.84             24.94                      37.50    3.348   3.7899   0.1336  47.1639\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31  13.7117  5    135.759    41.23             17.43             29.71                      37.50    3.751   3.6738   0.2412  36.9510\n    32  12.2681  2    148.027    39.38             19.73             33.38                      37.50    4.202   2.2942   0.1262  36.1216\n    33  14.5808  3    162.608    36.56             21.17             36.68                      37.50    4.585   3.6608   0.1709  41.4527\n    34  15.9031  4    178.511    35.06             23.28             39.90                      37.50    5.043   4.7523   0.2152  43.7643\n    35  15.2401  4    193.751    34.83             26.45             43.16                      37.50    5.567   2.3536   0.1601  47.6912\n    36  15.6531  2    209.404    33.35             28.09             45.71                      37.50    6.118   3.1674   0.2056  48.7010\n    37  15.4067  4    224.811    31.69             29.49             48.20                      37.50    6.653   2.6131   0.2320  45.3283\n    38  14.1158  3    238.926    30.28             31.07             50.65                      37.50    7.211   1.4586   0.1794  26.0828\n    39  14.9993  2    253.926    28.78             32.41             52.97                      37.50    7.737   3.5024   0.1975  37.9259\n    40  15.1085  2    269.034    27.47             33.46             54.92                      37.50    8.302   3.7396   0.1098  50.1992\n    41  15.0742  3    284.108    26.47             33.44             55.81                      37.50    8.867   3.3054   0.2430  31.7274\n    42  13.4238  3    297.532    26.49             34.64             56.66                      37.50    9.446   2.5375   0.1628  31.7741\n    43  15.0221  3    312.554    26.46             36.40             57.91                      37.50    9.926   2.2817   0.1523  33.8439\n    44  17.3936  4    329.948    25.56             38.06             59.83                      37.50   10.458   2.2468   0.1803  35.8432\n    45  18.4306  2    348.379    24.36             40.02             62.16                      37.50   11.160   2.2160   0.1892  44.5448\n    46  19.0201  5    367.399    23.30             40.26             63.34                      37.50   11.852   2.7932   0.2777  47.6702\n    47  15.5635  3    382.962    24.20             42.35             63.64                      37.50   12.630   2.4154   0.1353  35.0902\n    48  18.7602  5    401.722    25.01             43.43             63.45                      37.50   13.196   3.4588   0.2169  24.6445\n    49  17.8984  3    419.621    23.71             43.32             64.63                      37.50   13.942   3.1574   0.1927  38.5401\n    50  18.2823  4    437.903    22.96             43.94             65.68                      37.50   14.628   2.7728   0.2029  45.5480\n    51  18.1303  4    456.033    24.68             43.45             63.77                      37.50   15.340   2.2314   0.2313  32.1264\n    52  16.6409  3    472.674    24.20             43.60             64.31                      37.50   16.067   2.5332   0.1595  31.9451\n    53  18.8174  4    491.492    23.83             43.81             64.77                      37.50   16.692   2.7973   0.2437  35.4996\n    54  16.7297  3    508.221    26.37             41.94             61.40                      37.50   17.460   3.8239   0.1767  37.8016\n    55  17.9248  5    526.146    23.50             37.32             61.36                      37.50   18.100   4.5614   0.2106  47.0136\n    56  17.4001  4    543.546    16.43             34.71             67.87                      37.48   18.788   8.2304   0.1996  19.2520\n    57  17.4219  4    560.968    13.54             33.99             71.51                      37.50   19.420   2.6171   0.1106  19.7759\n    58  23.3961  4    584.364    12.17             34.22             73.77                      37.50   19.937   2.6424   0.1749  26.1967\n    59  25.2050  4    609.569    12.17             34.59             73.98                      37.51   20.679   4.9395   0.1671  26.7056\n    60  27.8222  5    637.391    11.62             34.46             74.79                      37.50   21.429   3.0812   0.1497  35.4421\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    61  32.4889  4    669.880    11.52             36.68             76.10                      37.50   22.220   5.4922   0.1903  39.6151\n    62  33.4182  4    703.298    11.15             37.42             77.05                      37.50   23.172   3.8991   0.2272  41.1949\n    63  31.0109  4    734.309    11.02             37.67             77.37                      37.49   24.186   2.2693   0.2206  51.3595\n    64  29.2897  5    763.599    11.07             38.59             77.70                      37.49   25.107   2.8999   0.2218  29.3240\n    65  27.5728  5    791.172    11.13             40.68             78.53                      37.50   25.970   3.3800   0.1253  62.8864\n    66  24.0333  6    815.205    11.94             41.53             77.68                      37.49   26.813   4.1493   0.1991  45.1111\n    67   0.0992  4 5  815.304     9.20             33.52             78.46                      37.22   27.872  11.2273   0.0132   0.5093\n    68   0.0709  4 1  815.375     6.60             26.80             80.23                      37.09   27.879  11.6628   0.0191   0.5085\n    69   0.1468  4    815.522     7.81             31.63             80.19                      37.47   27.883   8.9274   0.0086   0.5087\n    70   0.1077  4 1  815.630     7.55             31.77             80.80                      37.45   27.890   0.3503   0.0065   0.4745\n    71   0.0803  4 1  815.710     7.06             30.44             81.17                      37.25   27.896   1.6599   0.0068   0.3977\n    72   0.0597  4 1  815.770     5.95             27.16             82.02                      37.09   27.902   4.4075   0.0087   0.3641\n    73   0.1318  4    815.902     6.93             31.35             81.89                      37.40   27.905   5.3897   0.0081   0.5409\n    74   0.0972  4 1  815.999     7.19             32.94             82.08                      37.25   27.912   1.4113   0.0060   0.3624\n    75   0.0727  4 1  816.072     6.54             30.81             82.49                      37.43   27.917   2.6212   0.0048   0.3371\n    76   0.1644  4    816.236     6.46             30.99             82.74                      37.39   27.922   0.8108   0.0055   0.5505\n    77   0.1233  4 1  816.359     6.66             32.14             82.83                      37.46   27.931   1.1460   0.0030   0.3692\n    78   0.0940  4 1  816.453     6.46             31.22             82.87                      37.47   27.937   0.8147   0.0032   0.3515\n    79   0.0716  4 1  816.525     5.24             26.96             83.74                      36.84   27.943   4.9172   0.0103   0.3332\n    80   0.1564  4    816.681     6.38             31.61             83.20                      37.42   27.947   5.4998   0.0102   0.4476\n    81   0.1139  4 1  816.795     6.59             32.80             83.26                      37.25   27.955   0.9762   0.0065   0.2834\n    82   0.0849  4 1  816.880     6.38             31.90             83.34                      37.36   27.961   1.0392   0.0021   0.2141\n    83   0.1953  6    817.075     5.77             30.35             84.02                      37.37   27.967   3.4751   0.0051   0.4710\n    84   0.1302  4 1  817.206     5.77             30.39             84.04                      37.39   27.978   0.5596   0.0035   0.2135\n    85   0.0990  4 1  817.305     6.14             31.43             83.65                      37.25   27.984   1.9334   0.0026   0.1603\n    86   0.0757  4 1  817.380     5.35             28.58             84.23                      37.04   27.990   3.4210   0.0048   0.1902\n    87   0.1712  4    817.552     5.83             30.56             83.99                      37.30   27.996   2.2018   0.0048   0.2035\n    88   0.1291  4 1  817.681     6.08             31.42             83.78                      37.45   28.004   1.1908   0.0035   0.1040\n    89   0.0981  4 1  817.779     5.57             29.23             84.00                      37.26   28.012   2.1874   0.0041   0.1613\n    90   0.2228  6    818.002     5.85             30.47             83.89                      37.36   28.018   2.0314   0.0061   0.2002\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    91   0.1485  4 1  818.150     6.21             31.69             83.61                      37.44   28.029   1.4453   0.0039   0.1190\n    92   0.1126  4 1  818.263     6.00             30.68             83.65                      37.29   28.037   1.2509   0.0035   0.0906\n    93   0.0856  4 1  818.348     4.75             26.12             84.61                      37.17   28.044   5.3728   0.0132   0.1243\n    94   0.1835  4    818.532     5.83             29.55             83.53                      37.41   28.050   5.4405   0.0051   0.1488\n    95   0.1377  4 1  818.669     5.05             27.08             84.27                      36.98   28.060   3.2867   0.0078   0.1311\n    96   0.3054  4    818.975     6.67             32.97             83.17                      37.31   28.067   6.7528   0.0155   0.2506\n    97   0.2152  4 1  819.190     6.52             32.49             83.28                      37.28   28.082   0.7110   0.0051   0.1777\n    98   0.1619  4 1  819.352     6.52             32.16             83.13                      37.39   28.093   0.7773   0.0038   0.1340\n    99   0.1228  4 1  819.475     5.31             27.49             83.81                      37.27   28.102   5.0761   0.0150   0.1019\n   100   0.2606  4    819.735     6.39             30.79             82.82                      37.43   28.109   4.6776   0.0061   0.2174\n   101   0.1947  4 1  819.930     5.53             27.66             83.33                      37.32   28.124   3.2931   0.0114   0.1631\n   102   0.4221  6    820.352     7.18             32.86             82.06                      37.44   28.133   6.0373   0.0085   0.3571\n   103   0.0938  4 2  820.446     4.48             23.70             84.09                      37.09   28.155  11.4292   0.0242   0.0989\n   104   0.1885  4    820.634     4.20             22.67             84.37                      37.22   28.163   1.2949   0.0234   0.1604\n   105   0.1268  3 1  820.761     4.22             22.65             84.30                      37.22   28.174   0.6214   0.0135   0.1085\n   106   0.0905  3 1  820.852     4.45             23.30             83.97                      37.27   28.181   1.0846   0.0067   0.0797\n   107   0.2021  3    821.054     4.82             24.22             83.39                      37.29   28.188   1.4687   0.0094   0.1844\n   108   0.1479  3 1  821.202     5.08             24.83             83.03                      37.40   28.198   0.9205   0.0044   0.1362\n   109   0.1117  3 1  821.313     5.23             25.19             82.82                      37.30   28.206   0.5013   0.0026   0.1030\n   110   0.2563  3    821.569     5.44             25.69             82.52                      37.40   28.213   0.7104   0.0051   0.2345\n   111   0.1928  3 1  821.762     5.58             26.00             82.34                      37.45   28.226   0.4450   0.0036   0.1775\n   112   0.1465  3 1  821.909     5.67             26.20             82.22                      37.48   28.236   0.2814   0.0026   0.1354\n   113   0.3359  3    822.245     5.82             26.50             82.00                      37.31   28.244   0.4795   0.0053   0.3133\n   114   0.2524  3 1  822.497     5.92             26.71             81.85                      37.48   28.261   0.3409   0.0037   0.2378\n   115   0.1915  3 1  822.689     6.00             26.85             81.75                      37.26   28.273   0.2323   0.0027   0.1811\n   116   0.1464  3 1  822.835     6.05             26.94             81.67                      37.45   28.283   0.1649   0.0020   0.1391\n   117   0.3372  3    823.172     6.15             27.13             81.51                      37.26   28.291   0.3427   0.0041   0.3228\n   118   0.2553  3 1  823.427     6.24             27.27             81.39                      37.25   28.307   0.2647   0.0029   0.2463\n   119   0.1948  3 1  823.622     6.30             27.38             81.30                      37.38   28.319   0.1916   0.0021   0.1892\n   120   0.4484  3    824.071     6.43             27.59             81.11                      37.28   28.329   0.4087   0.0042   0.4409\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n   121   0.3392  3 1  824.410     6.52             27.74             80.97                      37.35   28.350   0.3045   0.0029   0.3358\n   122   0.2589  3 1  824.669     6.59             27.85             80.86                      37.31   28.366   0.2172   0.0020   0.2580\n   123   0.1986  3 1  824.867     6.64             27.93             80.79                      37.41   28.378   0.1585   0.0015   0.1993\n   124   0.4589  3    825.326     6.75             28.09             80.62                      37.28   28.387   0.3461   0.0030   0.4655\n   125   0.3499  3 1  825.676     6.83             28.22             80.50                      37.39   28.408   0.2635   0.0021   0.3577\n   126   0.2685  3 1  825.945     6.90             28.31             80.41                      37.35   28.424   0.1978   0.0015   0.2766\n   127   0.6203  3    826.565     7.02             28.48             80.22                      37.31   28.435   0.4164   0.0029   0.6470\n   128   0.4734  3 1  827.038     7.12             28.61             80.08                      37.42   28.463   0.3105   0.0020   0.4995\n   129   0.3633  3 1  827.402     7.19             28.72             79.99                      37.37   28.483   0.2237   0.0015   0.3859\n   130   0.2797  3 1  827.682     7.24             28.79             79.92                      37.34   28.499   0.1667   0.0011   0.2988\n   131   0.6475  3    828.329     7.34             28.93             79.76                      37.34   28.510   0.3512   0.0025   0.7012\n   132   0.4944  3 1  828.823     7.43             29.09             79.66                      37.38   28.538   0.2665   0.0018   0.5406\n   133   0.3791  3 1  829.203     7.48             29.13             79.56                      37.35   28.559   0.1941   0.0014   0.4171\n   134   0.8748  3    830.077     7.61             29.31             79.39                      37.34   28.572   0.4121   0.0030   0.9781\n   135   0.6631  3 1  830.740     7.70             29.44             79.28                      37.37   28.608   0.4104   0.0021   0.7492\n   136   0.5056  3 1  831.246     7.76             29.55             79.20                      37.41   28.635   0.3460   0.0024   0.5753\n   137   0.3871  3 1  831.633     7.81             29.63             79.15                      37.37   28.656   0.2227   0.0023   0.4426\n   138   0.8896  3    832.523     7.91             29.84             79.06                      37.37   28.667   0.4053   0.0082   1.0280\n   139   0.6561  3 1  833.179     7.98             30.02             79.01                      37.38   28.703   0.2535   0.0072   0.7631\n   140   0.4868  3 1  833.666     8.03             30.17             78.98                      37.45   28.729   0.1774   0.0059   0.5692\n   141   1.0931  3    834.759     8.14             30.49             78.93                      37.41   28.742   0.3697   0.0146   1.2909\n   142   0.7748  3 1  835.533     8.22             30.73             78.91                      37.40   28.785   0.2508   0.0109   0.9209\n   143   0.5618  3 1  836.095     8.27             30.90             78.89                      37.42   28.815   0.1754   0.0081   0.6706\n   144   1.2437  3    837.339     8.38             31.26             78.85                      37.41   28.829   0.3642   0.0180   1.4978\n   145   0.8637  3 1  838.202     8.46             31.49             78.82                      37.41   28.877   0.2427   0.0123   1.0458\n   146   0.6210  3 1  838.823     8.52             31.66             78.80                      37.43   28.909   0.1686   0.0086   0.7547\n   147   1.3704  3    840.194     8.63             31.97             78.74                      37.42   28.923   0.3466   0.0176   1.6785\n   148   0.9541  3 1  841.148     8.70             32.17             78.70                      37.42   28.974   0.2311   0.0114   1.1744\n   149   2.0686  3    843.217     8.85             32.53             78.61                      37.45   28.993   0.4591   0.0211   2.5752\n   150   1.4106  3 1  844.627     8.94             32.76             78.56                      37.44   29.068   0.2938   0.0128   1.7699\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n   151   3.0325  4    847.660     9.11             33.21             78.47                      37.48   29.091   0.5720   0.0220   3.8734\n   152   2.0568  3 1  849.716     9.21             33.52             78.43                      37.47   29.197   0.3566   0.0131   2.6562\n   153   4.4124  3    854.129     9.42             34.28             78.45                      37.49   29.222   0.7227   0.0223   5.8343\n   154   8.9096  2    863.038     9.80             36.11             78.66                      37.47   29.273   2.1989   0.0595  11.4008\n   155  14.8820  3    877.920     9.10             35.49             79.60                      37.47   29.403   2.8256   0.1178  19.2007\n   156  19.4520  3    897.372     8.62             35.29             80.38                      37.47   29.576   5.6508   0.1536  15.3213\n   157  22.4216  3    919.794     8.10             35.31             81.34                      37.48   29.729   5.3923   0.1363  15.6107\n   158  27.4070  3    947.201     7.10             34.53             82.95                      37.50   29.851   4.9311   0.1038  21.8052\n   159  37.7960  4    984.997     6.40             35.21             84.62                      37.48   29.888   5.0780   0.1765  41.2991\n   160  40.5209  5   1025.518     6.02             35.69             85.57                      37.51   30.224   7.4011   0.1629  34.6179\n   161  45.3194  4   1070.837     5.07             34.40             87.16                      37.51   30.536  10.6411   0.2108  49.3608\n   162  24.1626  3   1095.000     3.77             32.77             89.68                      37.50   31.484   8.0003   0.1534  11.5550\n   163  27.8742  3   1122.874     4.42             35.34             88.89                      37.50   31.651   5.7665   0.0853  20.4796\n   164  41.4647  2   1164.339     3.31             34.29             91.19                      37.53   31.636   7.1281   0.0460  32.7127\n   165  51.6739  4   1216.013     2.99             34.62             92.06                      37.50   31.815   9.9759   0.1933  28.8559\n   166  52.6877  5   1268.701     2.41             33.94             93.37                      37.50   32.271  10.3289   0.1585  44.4153\n   167  56.2798  4   1324.980     1.68             33.85             95.28                      37.50   32.673  11.9705   0.1563   7.7008\n   168  64.3144  3   1389.295     1.86             34.11             94.82                      37.50   32.995  13.6146   0.0809  10.7232\n   169  97.4855  3   1486.780     1.24             33.44             96.43                      37.47   32.903  20.6757   0.0541  13.2349\n   170 167.1396  4   1653.920     0.88             30.44             97.18                      37.50   32.331  43.5079   0.1085  20.1716\n   171 226.2683  6   1880.188     0.98             28.40             96.68                      37.49   32.378  72.0157   0.2124  26.3026\n   172 218.5351  4   2098.723     0.95             28.34             96.74                      37.50   33.688  81.1221   0.1146  24.3445\n   173 289.0244  6   2387.748     0.81             26.67             97.05                      37.50   33.851 131.1793   0.1224  31.7955\n   174 359.7652  6   2747.513     0.38             24.20             98.46                      37.50   34.265 201.3040   0.0869  39.2798\n   175 358.4299  9   3105.943     0.13             17.39             99.28                      37.50   35.379 273.2901   0.1120  42.3686\n   176  10.9767  2 3 3116.919     0.12             16.62             99.26                      37.50   40.684   7.8986   0.0055   1.0704\n   177   8.1104  1 1 3125.030     0.12             18.43             99.35                      37.50   40.782   4.3281   0.0043   0.6041\n   178   6.1312  1 1 3131.161     0.12             19.03             99.39                      37.50   40.854   3.2389   0.0023   0.4525\n   179   4.6679  1 1 3135.829     0.11             19.33             99.41                      37.50   40.908   2.4576   0.0014   0.3439\n   180   3.5721  1 1 3139.401     0.11             19.49             99.42                      37.50   40.948   1.8733 9.50e-04   0.2623\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n   181   8.2321  6   3147.633     0.11             17.65             99.39                      37.50   40.923   1.9190   0.0812   2.5755\n   182   1.3848  6 2 3149.018     0.11             33.31             99.66                       1.75   41.017   3.7968   0.1005   1.9011\n   183   1.9347  2   3150.953     0.11             17.39             99.39                      31.55   41.021   1.8550   0.0138   0.2522\n   184   4.1327  2   3155.085     0.10             17.60             99.41                      31.54   41.011   0.0574   0.0161   0.3476\n   185   8.7060  2   3163.791     0.10             20.78             99.52                      31.54   40.998   0.1569   0.0155   0.6498\n   186  18.4132  2   3182.204     0.09             23.27             99.60                      31.49   40.979   0.1248   0.0335   1.1251\n   187  35.1137  2   3217.318     0.08             25.83             99.68                      31.05   40.999   0.1478   0.0225   1.6442\n   188  71.2296  2   3288.548     0.07             28.34             99.77                      30.48   41.057   0.1765   0.0060   3.2002\n   189 153.1341  3   3441.682     0.04             28.32             99.84                      28.65   41.193   0.5584   0.0091   6.4381\n   190 208.3182  3   3650.000     0.03             27.22             99.89                      27.02   42.160   0.5504   0.0075   6.9417\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                               1m 40.31s    99.92%\n|- Newton                              1m 39.69s    99.38%\n  |- Jacobian                          1m 24.66s    84.93%\n  |- Update                              12.612s    12.65%\n  |- Solver                               1.830s     1.84%\n  |- Residual                             0.210s     0.21%\n  |- Logging                              0.023s     0.02%\n|- Output                                 0.568s     0.57%\n|- Input                                  0.000s     0.00%\nInitialization                            0.078s     0.08%\n------------------------------------------------------------\nTOTAL                                  1m 40.38s\n============================================================\n\n\n')
```

#### Load CMG

### Load ECL

### Wells

![png]({{ "/assets/images/benchmark_image_48.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_49.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_50.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_51.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_52.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_53.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_54.png" | relative_url }})

### Block

#### Block Pressure


```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_55.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_56.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_57.png" | relative_url }})

#### Block Temperature

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_58.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_59.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_60.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_61.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_62.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_63.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_64.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_65.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_66.png" | relative_url }})

#### v.s. ECL

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_67.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_68.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_69.png" | relative_url }})
