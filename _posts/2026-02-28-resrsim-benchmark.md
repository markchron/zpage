---
layout: default
title: "Benchmark results of resrsim"
date: 2026-02-28
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

ipynb_folder path: /Users/mark/Documents/workspace/hatch/app

output_folder path: /Users/mark/Documents/workspace/hatch/app/build/test/data/

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

![png]({{ "/assets/images/benchmark_image_2.png" | relative_url }})

## stflu005.dat

steam injection in corner-point grid

```
Running simulation: Steam injection Corner point

    25  55.0000  1   3650.000   295.96             11.63              3.78                      52.49    0.010 5.642352 0.000137 0.014121



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  5.597s    94.85%

|- Newton                                 5.194s    92.81%

  |- Jacobian                             3.408s    65.62%

  |- Update                               1.669s    32.14%

  |- Residual                             0.046s     0.88%

  |- Solver                               0.028s     0.54%

  |- Logging                              0.001s     0.02%

|- Output                                 0.389s     6.96%

|- Input                                  0.000s     0.00%

Initialization                            0.304s     5.15%

------------------------------------------------------------

TOTAL                                     5.901s

============================================================



Time steps : 25/25, step size: 146.00, 129.48

```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data/stflu005.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/stflu005.dat\n', stderr='[MacBook-Air.local:18617] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/4271833088/sm_segment.MacBook-Air.501.fe9f0000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1   1.0000  1      1.000   440.38             12.88              2.84                      49.82    0.000 2423.151146 0.000002 0.001661\n     2   0.1360  1      1.136   440.35             12.88              2.84                      49.82    0.000 0.141787 0.000000 0.000213\n     3   0.3171  1      1.453   440.30             12.88              2.84                      49.82    0.000 0.292940 0.000001 0.000439\n     4   0.7384  1      2.192   440.20             12.88              2.84                      49.82    0.000 0.555772 0.000002 0.000841\n     5   1.7166  1      3.908   439.99             12.88              2.84                      49.82    0.000 0.997995 0.000004 0.001909\n     6   3.9789  1      7.887   439.59             12.88              2.85                      49.82    0.000 1.841844 0.000009 0.004292\n     7   9.1716  1     17.059   438.75             12.88              2.85                      49.82    0.001 3.619907 0.000021 0.009481\n     8  20.8960  1     37.955   437.03             12.88              2.86                      49.83    0.001 6.875903 0.000049 0.020354\n     9  46.6203  1     84.575   433.55             12.88              2.89                      49.85    0.002 13.772418 0.000110 0.041557\n    10  99.6328  1    184.208   426.80             12.88              2.93                      49.90    0.002 26.929067 0.000236 0.076872\n    11 197.0930  1    381.301   414.93             12.86              3.01                      50.00    0.003 46.714002 0.000468 0.122911\n    12 213.6993  1    595.000   403.27             12.82              3.08                      50.20    0.004 45.254621 0.000510 0.111687\n    13 365.0000  1    960.000   388.94             12.74              3.17                      50.39    0.005 54.389200 0.000715 0.126671\n    14 135.0000  1   1095.000   382.64             12.70              3.21                      50.65    0.005 23.965983 0.000325 0.055938\n    15 271.6048  1   1366.605   370.94             12.61              3.29                      50.75    0.006 43.739800 0.000655 0.099860\n    16 228.3952  1   1595.000   361.72             12.53              3.35                      50.96    0.007 34.183409 0.000554 0.077900\n    17 365.0000  1   1960.000   348.19             12.39              3.44                      51.12    0.007 49.412815 0.000887 0.112672\n    18 135.0000  1   2095.000   343.37             12.33              3.47                      51.40    0.008 17.659637 0.000330 0.040870\n    19 281.8210  1   2376.821   333.81             12.21              3.53                      51.48    0.008 34.507467 0.000691 0.079908\n    20 218.1790  1   2595.000   326.73             12.12              3.58                      51.68    0.009 25.506915 0.000536 0.059747\n    21 365.0000  1   2960.000   315.58             11.96              3.65                      51.82    0.009 40.074315 0.000898 0.094120\n    22 135.0000  1   3095.000   311.57             11.89              3.68                      52.08    0.009 14.558971 0.000334 0.034672\n    23 287.1311  1   3382.131   303.35             11.76              3.73                      52.15    0.010 29.851235 0.000711 0.071394\n    24 212.8689  1   3595.000   297.46             11.66              3.77                      52.34    0.010 21.906415 0.000529 0.052461\n    25  55.0000  1   3650.000   295.96             11.63              3.78                      52.49    0.010 5.642352 0.000137 0.014121\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                  5.597s    94.85%\n|- Newton                                 5.194s    92.81%\n  |- Jacobian                             3.408s    65.62%\n  |- Update                               1.669s    32.14%\n  |- Residual                             0.046s     0.88%\n  |- Solver                               0.028s     0.54%\n  |- Logging                              0.001s     0.02%\n|- Output                                 0.389s     6.96%\n|- Input                                  0.000s     0.00%\nInitialization                            0.304s     5.15%\n------------------------------------------------------------\nTOTAL                                     5.901s\n============================================================\n\nTime steps : 25/25, step size: 146.00, 129.48\n')
```

```
Found 26 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build/test/data/stflu005_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_3.png" | relative_url }})

# SPE4-b

* Steam flooding with water and dead oil

* VMod on 9x5x4 cartesian grid


### Load STARS

### Load ECL

### Load SMY File

Load the SMY file (`spe04b.smy`) into a pandas DataFrame, ensuring proper parsing of the data.

```
Running simulation: SPE4-b

    62   5.8732  1   3650.000     0.07             26.82             99.73                      29.50   44.786 0.276046 0.003309 0.162499



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                 10.909s    99.09%

|- Newton                                10.744s    98.49%

  |- Jacobian                             8.490s    79.02%

  |- Update                               2.031s    18.91%

  |- Solver                               0.129s     1.21%

  |- Residual                             0.040s     0.37%

  |- Logging                              0.004s     0.03%

|- Output                                 0.149s     1.37%

|- Input                                  0.000s     0.00%

Initialization                            0.100s     0.91%

------------------------------------------------------------

TOTAL                                    11.008s

============================================================



Time steps : 62/69, step size: 58.87, 75.02

```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//spe04b.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/spe04b.dat\n', stderr='[MacBook-Air.local:18649] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/486604800/sm_segment.MacBook-Air.501.1d010000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1   1.0000  1      1.000     3.96             3e-07             6e-06                       2.76    0.014 32.027775 0.000436 8.759806\n     2   1.8163  1      2.816     3.48              0.03              0.83                       3.74    0.013 33.908458 0.037628 19.839977\n     3   3.2564  1      6.073     3.26              0.04              1.19                       9.08    0.182 28.628680 0.043012 40.500000\n     4   5.5870  9     11.660     2.84              0.05              1.84                      32.55    0.187 111.872494 0.243517 208.205489\n     5   4.5730  4     16.233     2.68              0.06              2.05                      37.50    0.242 68.222908 0.096690 83.274481\n     6   6.1316  3     22.364     2.61              0.05              2.05                      37.50    0.332 49.418446 0.051039 91.651868\n     7   7.8841  5     30.248     2.70              0.05              1.72                      37.50    0.430 62.443773 0.175869 90.321951\n     8   8.4679  3     38.716     2.95              0.03              1.11                      37.50    0.665 43.645571 0.192218 76.660131\n     9   8.6605  3     47.377     3.35              0.02              0.71                      37.50    0.920 29.802829 0.072365 59.533557\n    10  13.2147  2     60.592     4.14              0.01              0.23                      37.50    1.254 33.553197 0.036348 69.704037\n    11  19.0383  3     79.630     5.59              0.02              0.27                      37.50    1.724 40.827397 0.200285 90.165746\n    12  19.0229  3     98.653     6.72              2.13             24.06                      37.50    2.373 41.940948 0.213177 76.215418\n    13  18.3327  2    116.985     7.49              4.21             35.97                      37.48    3.339 31.789209 0.181735 62.299366\n    14  19.3421  2    136.328     8.26              6.35             43.48                      37.50    3.977 30.454431 0.042761 63.592551\n    15  28.8331  4    165.161     9.24             11.24             54.88                      37.50    4.487 39.768303 0.184513 88.006644\n    16  30.1680  3    195.329    10.15             15.85             60.97                      37.50    5.376 33.801581 0.181517 67.456677\n    17  31.8500  4    227.179    11.06             20.24             64.66                      37.50    6.198 25.881275 0.150169 64.636937\n    18  37.1374  4    264.316    12.54             26.45             67.83                      37.50    7.031 20.398306 0.130180 97.218367\n    19  46.3918  4    310.708    15.61             35.46             69.43                      37.50    7.992 12.514471 0.180302 69.988731\n    20  49.1585  3    359.866    20.98             48.69             69.89                      37.50    9.383 54.108594 0.131288 87.803554\n    21  61.1667  6    421.033    24.44             49.65             67.01                      37.50   10.754 58.988887 0.174922 96.016315\n    22  65.8877  6    486.921    23.85             46.40             66.05                      37.50   12.444 43.343275 0.220603 109.821720\n    23  62.2249  7    549.146    22.96             43.39             65.40                      37.50   14.266 32.723952 0.196600 90.700738\n    24  62.8353  5    611.981    22.59             41.53             64.77                      37.50   15.913 23.798545 0.218206 120.543338\n    25  59.7284  6    671.709    24.50             43.12             63.77                      37.50   17.633 29.877958 0.208742 91.537571\n    26  58.2729 13    729.982    31.75             51.25             61.75                      37.50   19.419 38.645620 0.245179 113.123968\n    27  17.2037  5 1  747.186    29.77             48.06             61.75                      37.49   21.434 4.721127 0.121436 27.390963\n    28  22.1831  4    769.369    20.78             36.20             63.53                      37.50   21.924 5.363202 0.131307 43.989403\n    29  27.6000  4    796.969    19.38             36.44             65.28                      37.50   22.523 5.354638 0.116538 44.492630\n    30  36.2425  6    833.212    16.44             34.75             67.88                      37.49   23.185 4.153208 0.160419 68.011035\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31  40.8637  4    874.075    14.09             34.38             70.93                      37.52   24.076 4.881826 0.212232 48.178225\n    32  39.4839  5    913.559    13.95             34.92             71.46                      37.50   25.133 2.769258 0.112537 45.175812\n    33  52.6378  6    966.197    13.12             35.28             72.89                      37.50   25.974 3.425153 0.190247 60.861927\n    34  54.1466  5   1020.344    13.52             36.83             73.15                      37.50   27.040 3.580251 0.197191 85.811917\n    35  54.5848 11   1074.928    14.03             38.04             73.06                      37.50   27.847 5.133835 0.228097 102.969885\n    36  20.0716  4   1095.000    13.22             36.48             73.40                      37.51   29.395 2.897672 0.086578 24.406863\n    37  29.6944  5   1124.694    11.89             34.93             74.60                      37.50   29.492 5.483774 0.153192 35.422379\n    38  34.2787  4   1158.973    10.58             33.21             75.85                      37.49   29.808 6.183722 0.124555 48.762264\n    39  43.6982  4   1202.671     8.75             31.37             78.19                      37.51   30.043 7.558095 0.136348 50.079623\n    40  53.4119  4   1256.083     7.64             32.08             80.77                      37.48   30.388 10.115520 0.137936 72.305580\n    41  64.9247  5   1321.008     5.97             31.66             84.13                      37.50   30.734 14.796339 0.235320 49.126748\n    42  58.9734  3   1379.981     5.60             34.93             86.19                      37.49   31.493 12.466031 0.120085 49.772270\n    43  76.4229  4   1456.404     4.19             31.13             88.13                      37.51   31.707 17.972250 0.174416 21.378251\n    44  82.4498  3   1538.854     3.44             31.14             90.04                      37.50   32.231 20.042384 0.092425 18.812789\n    45 119.0366  2   1657.891     2.64             31.22             92.19                      37.49   32.260 31.441838 0.086770 15.665820\n    46 175.9632  5   1833.854     1.81             30.41             94.40                      37.50   32.140 52.732141 0.110461 21.981715\n    47 236.4539  3   2070.308     1.15             29.95             96.31                      37.50   32.380 81.744698 0.112824 27.476553\n    48 314.8829  5   2385.191     0.61             28.06             97.88                      37.50   32.833 129.789213 0.100887 33.929771\n    49 341.1492  4   2726.340     0.28             25.86             98.91                      37.51   34.081 171.832802 0.067076 34.617825\n    50 314.9537  5   3041.294     0.12             22.12             99.47                      37.50   35.800 192.349403 0.092375 30.779962\n    51  90.4004  3 1 3131.694     0.08             19.67             99.58                      37.50   39.590 60.852236 0.070619 8.512534\n    52 136.8895  3   3268.584     0.05             17.00             99.72                      37.50   39.350 105.118404 0.021393 13.733373\n    53  55.0406 10 1 3323.624     0.08             27.25             99.72                      37.38   41.174 5.626456 0.022786 4.254722\n    54   2.4463  1 3 3326.070     0.06             20.78             99.73                      37.50   42.039 2.772368 0.006433 0.279077\n    55   1.8244  3 1 3327.895     0.06             20.85             99.73                      24.42   42.041 1.541970 0.003184 0.198276\n    56   4.1685  1   3332.063     0.05             19.13             99.73                      32.78   42.028 0.785629 0.008069 0.194728\n    57   9.2299  1   3341.293     0.06             20.97             99.73                      31.45   42.009 0.426014 0.013177 0.503519\n    58  19.7973  1   3361.091     0.06             23.41             99.73                      30.93   41.986 0.190045 0.036864 0.930965\n    59  37.0807  2   3398.171     0.07             26.86             99.72                      30.60   42.013 0.142550 0.021947 1.505463\n    60  75.4781  1   3473.649     0.07             27.05             99.73                      30.51   42.150 0.026472 0.004961 2.437981\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    61 170.4774  1   3644.127     0.07             26.87             99.73                      30.29   42.550 0.091532 0.003102 5.272399\n    62   5.8732  1   3650.000     0.07             26.82             99.73                      29.50   44.786 0.276046 0.003309 0.162499\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                 10.909s    99.09%\n|- Newton                                10.744s    98.49%\n  |- Jacobian                             8.490s    79.02%\n  |- Update                               2.031s    18.91%\n  |- Solver                               0.129s     1.21%\n  |- Residual                             0.040s     0.37%\n  |- Logging                              0.004s     0.03%\n|- Output                                 0.149s     1.37%\n|- Input                                  0.000s     0.00%\nInitialization                            0.100s     0.91%\n------------------------------------------------------------\nTOTAL                                    11.008s\n============================================================\n\nTime steps : 62/69, step size: 58.87, 75.02\n')
```

## Select and Plot Columns

Select specific columns from the loaded DataFrames and plot them using matplotlib. For example, plot `TIME` vs `TEMP 1-1-4` from `stars_spe4b_special.csv`.

### Cell property

#### Block Pressure


```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_4.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_5.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_6.png" | relative_url }})

#### Block Temperature

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_7.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_8.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_9.png" | relative_url }})

#### Block Saturation

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_10.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_11.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_12.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_13.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_14.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_15.png" | relative_url }})

### vesus ECL

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_16.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_17.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_18.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_19.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_20.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_21.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_22.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_23.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_24.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_25.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_26.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_27.png" | relative_url }})

### Well property

#### Injector

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_28.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_29.png" | relative_url }})

#### Producer Corner

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_30.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_31.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_32.png" | relative_url }})

#### Producer Edge

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_33.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_34.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_35.png" | relative_url }})

# Buckley- Leverett



Two phase, isothermal problem

variable order: [Sw, P, T, So, X0, X1, Sg]



Acc w.r.t. [Sw, So, Sg, X0, X1, P, T]

```
Running simulation: Buckley-Leverett

    27   4.7429  1     10.000    5e-08              1.00            100.00                       1.00    7.850 0.000039 0.000004 0.000010



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  2.471s    94.79%

|- Newton                                 2.408s    97.45%

  |- Jacobian                             1.676s    69.61%

  |- Update                               0.663s    27.53%

  |- Solver                               0.032s     1.35%

  |- Residual                             0.017s     0.69%

  |- Logging                              0.001s     0.06%

|- Output                                 0.059s     2.39%

|- Input                                  0.000s     0.00%

Initialization                            0.136s     5.21%

------------------------------------------------------------

TOTAL                                     2.607s

============================================================



Time steps : 27/28, step size: 0.37, 1.06

```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//buckley.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/buckley.dat\n', stderr='[MacBook-Air.local:18698] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/2858549248/sm_segment.MacBook-Air.501.aa620000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1 2.33e-04 12 1  2.3e-04     1.00                                                           1.00    0.045 491.171671 0.333114 0.183300\n     2 1.27e-04  2    3.6e-04     1.00                                                           1.00    0.049 4.266051 0.084918 0.020162\n     3 1.90e-04  4    5.5e-04     1.00                                                           1.00    0.842 7.563638 0.133387 0.023583\n     4 2.34e-04  6    7.8e-04     1.00                                                           1.00    1.764 8.804959 0.136125 0.022117\n     5 2.87e-04  6      0.001     1.00                                                           1.00    2.652 10.956662 0.136092 0.021271\n     6 3.51e-04  9      0.001     1.00                                                           1.00    3.573 13.395261 0.149451 0.021327\n     7 4.10e-04  9      0.002     1.00                                                           1.00    4.521 15.202518 0.138501 0.021464\n     8 4.97e-04  9      0.002     1.00                                                           1.00    5.322 18.101438 0.146610 0.022303\n     9 5.87e-04 12      0.003     1.00                                                           1.00    6.175 21.523233 0.160440 0.022549\n    10 5.87e-04 11      0.004     1.00                                                           1.00    6.997 20.143348 0.145371 0.021692\n    11 6.40e-04 11      0.004     1.00                                                           1.00    7.673 22.191842 0.147499 0.021372\n    12 6.98e-04  8      0.005     0.89              0.12             12.26                       1.00    8.295 18.318887 0.157390 0.024958\n    13 7.95e-04  3      0.006     0.55              0.45             44.97                       1.00    8.975 35.724096 0.106987 0.039650\n    14 1.08e-03  2      0.007     0.33              0.67             67.17                       1.00    9.297 38.422569 0.066298 0.043385\n    15 1.75e-03  2      0.008     0.20              0.80             79.78                       1.00    9.188 37.572707 0.049343 0.047028\n    16 3.08e-03  2      0.012     0.12              0.88             87.80                       1.00    8.644 36.549276 0.043616 0.050338\n    17 5.56e-03  2      0.017     0.07              0.93             92.95                       1.00    7.557 34.059202 0.041107 0.049823\n    18   0.0102  3      0.027     0.04              0.96             96.26                       1.00    6.097 29.576786 0.040343 0.045213\n    19   0.0187  3      0.046     0.02              0.98             98.16                       1.00    4.280 23.453609 0.036815 0.038649\n    20   0.0351  3      0.081     0.01              0.99             99.17                       1.00    2.394 17.774347 0.032050 0.033459\n    21   0.0675  3      0.149     0.00              1.00             99.66                       1.00    0.886 12.839301 0.026266 0.009470\n    22   0.1340  3      0.283     0.00              1.00             99.87                       1.00    0.353 8.787769 0.018058 0.005493\n    23   0.2790  3      0.562    5e-04              1.00             99.95                       1.00    0.353 6.749280 0.019227 0.002199\n    24   0.5771  1      1.139    1e-04              1.00             99.99                       1.00    7.940 2.453664 0.011291 0.000736\n    25   1.2522  1      2.391    9e-06              1.00            100.00                       1.00    9.094 0.372011 0.002907 0.000203\n    26   2.8663  1      5.257    2e-07              1.00            100.00                       1.00    8.794 0.024839 0.000254 0.000033\n    27   4.7429  1     10.000    5e-08              1.00            100.00                       1.00    7.850 0.000039 0.000004 0.000010\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                  2.471s    94.79%\n|- Newton                                 2.408s    97.45%\n  |- Jacobian                             1.676s    69.61%\n  |- Update                               0.663s    27.53%\n  |- Solver                               0.032s     1.35%\n  |- Residual                             0.017s     0.69%\n  |- Logging                              0.001s     0.06%\n|- Output                                 0.059s     2.39%\n|- Input                                  0.000s     0.00%\nInitialization                            0.136s     5.21%\n------------------------------------------------------------\nTOTAL                                     2.607s\n============================================================\n\nTime steps : 27/28, step size: 0.37, 1.06\n')
```

### Load Benchmark

### Buckley Plot

![png]({{ "/assets/images/benchmark_image_36.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_37.png" | relative_url }})

# MISC

## spe04b_cw.dat

```
Running simulation: SPE4-b water flooding

    22 365.0000  1   3650.000     5.00             63.84             92.74                      67.50    0.352 4.589230 0.030057 0.008362



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  5.084s    98.52%

|- Newton                                 4.921s    96.80%

  |- Jacobian                             3.753s    76.27%

  |- Update                               1.102s    22.39%

  |- Solver                               0.027s     0.55%

  |- Residual                             0.020s     0.40%

  |- Logging                              0.002s     0.04%

|- Output                                 0.158s     3.10%

|- Input                                  0.000s     0.00%

Initialization                            0.076s     1.48%

------------------------------------------------------------

TOTAL                                     5.160s

============================================================



Time steps : 22/22, step size: 165.91, 161.56

```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//spe04b_cw.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/spe04b_cw.dat\n', stderr='[MacBook-Air.local:18718] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/2024144896/sm_segment.MacBook-Air.501.78a60000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1   1.0000  2      1.000    35.34              0.09              0.27                      67.50    0.001 100.258768 0.063589 0.157770\n     2   1.2338  1      2.234    28.03              0.11              0.40                      67.50    0.012 42.159207 0.044322 0.061142\n     3   2.0941  1      4.328    23.41              0.11              0.48                      67.50    0.014 44.433249 0.044318 0.074417\n     4   3.5028  1      7.831    20.29              0.11              0.54                      67.51    0.023 34.585489 0.056903 0.057828\n     5   5.9253  1     13.756    17.97              0.10              0.58                      67.50    0.038 37.176671 0.087304 0.064034\n     6   8.7393  2     22.495    16.52              0.10              0.60                      67.50    0.037 26.718989 0.063118 0.045043\n     7  14.3524  2     36.848    16.05              0.10              0.59                      67.50    0.037 23.652425 0.066121 0.044182\n     8  23.2431  2     60.091    17.08              0.09              0.54                      67.50    0.037 23.291685 0.085096 0.038900\n     9  34.6032  3     94.694    19.69              0.13              0.67                      67.50    0.052 22.358737 0.089161 0.039102\n    10  50.6401  3    145.334    22.58              2.55             10.15                      67.50    0.084 20.666951 0.071895 0.034595\n    11  79.8756  4    225.210    24.23             11.26             31.73                      67.50    0.082 23.283235 0.070177 0.038412\n    12 126.9727  3    352.182    23.83             26.16             52.33                      67.50    0.103 22.122105 0.066782 0.042852\n    13 205.0004  5    557.183    21.19             42.67             66.81                      67.50    0.103 13.019276 0.067743 0.042053\n    14 329.5184  4    886.701    16.89             55.66             76.71                      67.50    0.104 20.020690 0.055977 0.061329\n    15 208.2989  1   1095.000    14.67             59.71             80.27                      67.50    0.160 12.707967 0.031683 0.034261\n    16 365.0000  2   1460.000    11.76             62.11             84.08                      67.50    0.161 18.559474 0.053878 0.043989\n    17 365.0000  1   1825.000     9.66             62.52             86.61                      67.50    0.282 14.873558 0.060084 0.032388\n    18 365.0000  2   2190.000     8.17             63.01             88.52                      67.50    0.280 10.458133 0.045396 0.022063\n    19 365.0000  1   2555.000     7.07             64.21             90.08                      67.50    0.299 8.561221 0.028964 0.017066\n    20 365.0000  1   2920.000     6.20             63.26             91.07                      67.50    0.319 6.684098 0.043060 0.012972\n    21 365.0000  1   3285.000     5.55             64.08             92.03                      67.50    0.341 5.344473 0.029801 0.010069\n    22 365.0000  1   3650.000     5.00             63.84             92.74                      67.50    0.352 4.589230 0.030057 0.008362\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                  5.084s    98.52%\n|- Newton                                 4.921s    96.80%\n  |- Jacobian                             3.753s    76.27%\n  |- Update                               1.102s    22.39%\n  |- Solver                               0.027s     0.55%\n  |- Residual                             0.020s     0.40%\n  |- Logging                              0.002s     0.04%\n|- Output                                 0.158s     3.10%\n|- Input                                  0.000s     0.00%\nInitialization                            0.076s     1.48%\n------------------------------------------------------------\nTOTAL                                     5.160s\n============================================================\n\nTime steps : 22/22, step size: 165.91, 161.56\n')
```



## watfld_cw.dat

```
Running simulation: SPE4-b Water flooding without vmod

    38 203.0488  1   3650.000     6.58            496.71             98.69                     503.18    1.916 1.656646 0.017323 0.003640



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  6.158s    98.51%

|- Newton                                 5.904s    95.88%

  |- Jacobian                             4.339s    73.48%

  |- Update                               1.470s    24.90%

  |- Solver                               0.041s     0.69%

  |- Residual                             0.028s     0.47%

  |- Logging                              0.001s     0.02%

|- Output                                 0.245s     3.97%

|- Input                                  0.000s     0.00%

Initialization                            0.093s     1.49%

------------------------------------------------------------

TOTAL                                     6.251s

============================================================



Time steps : 38/38, step size: 96.05, 133.53

```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//watfld_cw.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/watfld_cw.dat\n', stderr='[MacBook-Air.local:18734] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/4238868480/sm_segment.MacBook-Air.501.fca80000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1   1.0000  1      1.000   201.20             7e-07             3e-07                     503.19    0.294 54.389200 0.000747 0.083690\n     2   1.1667  1      2.167   195.68              0.01              0.00                     503.19    0.584 54.389200 0.022808 0.082827\n     3   1.3611  5      3.528   172.50              0.03              0.02                     495.70    0.638 271.946000 0.083905 0.388665\n     4   0.5293  2      4.057   169.05              0.03              0.02                     503.18    0.637 65.599638 0.024844 0.105847\n     5   0.5598  1      4.617   172.44              0.03              0.02                     503.20    0.635 47.238961 0.021640 0.076821\n     6   0.6991  1      5.316   179.88              0.02              0.01                     503.19    0.679 34.975182 0.022316 0.057286\n     7   0.9928  1      6.309   192.17              0.02              0.01                     503.19    0.675 36.029296 0.025484 0.060001\n     8   1.3935  1      7.702   209.80              0.01              0.01                     503.18    0.671 44.040204 0.038743 0.073909\n     9   1.7967  1      9.499   231.76              0.00              0.00                     503.19    0.806 31.493639 0.031593 0.058322\n    10   2.6549  1     12.154   259.72             4e-07             1e-07                     503.19    0.798 40.854573 0.051178 0.069505\n    11   3.5376  2     15.691   292.79                                                         503.19    0.789 40.394259 0.046370 0.073412\n    12   4.7365  1     20.428   328.42                                                         503.19    0.868 43.722203 0.060402 0.073519\n    13   6.1267  2     26.555   367.80                                                         503.19    0.962 47.347430 0.067905 0.087276\n    14   7.6426  3     34.197   401.98                                                         503.18    0.945 40.064369 0.063742 0.067568\n    15  10.2687  2     44.466   392.20             25.11              6.02                     503.17    0.862 57.803664 0.072127 0.097822\n    16  11.6155  2     56.082   340.01            112.11             24.80                     503.19    0.852 42.022558 0.050075 0.093418\n    17  15.2897  1     71.371   284.00            302.51             51.58                     503.18    0.722 38.005898 0.060917 0.095596\n    18  21.0009  2     92.372   237.53            317.52             57.21                     503.19    0.739 64.287256 0.064462 0.192954\n    19  22.4576  2    114.830   189.65            367.18             65.94                     503.19    0.742 61.395952 0.037326 0.161976\n    20  24.6150  1    139.445   154.22            402.70             72.31                     503.18    0.803 54.168441 0.039597 0.146316\n    21  28.7759  1    168.221   124.14            410.00             76.76                     503.18    0.852 51.563826 0.031888 0.131706\n    22  34.4672  1    202.688   100.78            425.51             80.85                     503.18    0.894 41.182467 0.032061 0.113795\n    23  45.7684  1    248.456    81.09            432.61             84.21                     503.19    0.939 38.237792 0.033488 0.107811\n    24  62.7073  1    311.164    64.49            446.72             87.39                     503.18    1.009 33.009290 0.047836 0.098659\n    25  91.0550  1    402.219    50.12            455.17             90.08                     503.18    1.114 32.412321 0.066235 0.097133\n    26 133.1270  1    535.346    37.99            462.09             92.40                     503.18    1.424 29.222872 0.059862 0.072753\n    27 202.0630  2    737.409    28.31            477.42             94.40                     503.18    1.390 24.477770 0.063905 0.055571\n    28 325.1481  2   1062.557    20.35            484.40             95.97                     503.18    1.356 24.235546 0.072645 0.045562\n    29  32.4432  1   1095.000    19.70            484.81             96.10                     503.19    1.355 2.203231 0.006114 0.004198\n    30  72.7360  1   1167.736    18.43            485.58             96.34                     503.18    1.362 4.348224 0.015286 0.008100\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31 154.0213  1   1321.757    16.34            486.55             96.75                     503.18    1.435 7.290058 0.029575 0.014581\n    32 300.1939  1   1621.951    13.64            487.99             97.28                     503.18    1.703 9.700122 0.062832 0.020235\n    33 365.0000  2   1986.951    11.51            492.14             97.71                     503.18    1.675 7.683794 0.066315 0.018070\n    34 365.0000  1   2351.951     9.96            493.70             98.02                     503.18    1.657 6.156646 0.055446 0.012646\n    35 365.0000  1   2716.951     8.74            494.15             98.26                     503.18    1.734 5.074124 0.046998 0.009285\n    36 365.0000  1   3081.951     7.75            494.86             98.46                     503.18    1.840 4.282587 0.047769 0.007650\n    37 365.0000  1   3446.951     6.96            495.79             98.61                     503.18    1.918 3.496451 0.031947 0.006863\n    38 203.0488  1   3650.000     6.58            496.71             98.69                     503.18    1.916 1.656646 0.017323 0.003640\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                  6.158s    98.51%\n|- Newton                                 5.904s    95.88%\n  |- Jacobian                             4.339s    73.48%\n  |- Update                               1.470s    24.90%\n  |- Solver                               0.041s     0.69%\n  |- Residual                             0.028s     0.47%\n  |- Logging                              0.001s     0.02%\n|- Output                                 0.245s     3.97%\n|- Input                                  0.000s     0.00%\nInitialization                            0.093s     1.49%\n------------------------------------------------------------\nTOTAL                                     6.251s\n============================================================\n\nTime steps : 38/38, step size: 96.05, 133.53\n')
```

## stflu001.dat

Inverted 9 spot water flooding with area/block modifier, 5 point transmissibility


```
Running simulation: Inverted 9 spot water flooding

   166 351.7165  6   3650.000   122.82            762.12             86.12                     877.54   98.741 3.016056 0.042507 1.299531



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                 16.811s    99.41%

|- Newton                                16.416s    97.65%

  |- Jacobian                            13.083s    79.70%

  |- Update                               3.130s    19.06%

  |- Solver                               0.066s     0.40%

  |- Residual                             0.062s     0.38%

  |- Logging                              0.008s     0.05%

|- Output                                 0.370s     2.20%

|- Input                                  0.000s     0.00%

Initialization                            0.099s     0.59%

------------------------------------------------------------

TOTAL                                    16.910s

============================================================



Time steps : 166/167, step size: 21.99, 70.85

```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//stflu001.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/stflu001.dat\n', stderr='[MacBook-Air.local:18750] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/2181365760/sm_segment.MacBook-Air.501.82050000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1   1.0000  1      1.000     3.96             3e-07             6e-06                       0.16    0.007 6.646542 0.000026 0.643469\n     2   2.2343  1      3.234     3.41              0.03              0.93                       0.17    0.007 7.499518 0.002062 1.368895\n     3   4.9652  1      8.200     2.93              0.05              1.71                       0.17    0.007 6.614736 0.005469 3.027396\n     4  10.7200  1     18.920     2.59              0.06              2.14                       0.20    0.008 6.373987 0.013304 6.781300\n     5  21.1828  1     40.102     2.36              0.06              2.30                       0.26    0.016 4.603507 0.020562 15.678310\n     6  34.8543  2     74.957     2.19              0.05              2.36                       0.55    0.022 4.550397 0.053259 50.435588\n     7  34.6817  3    109.638     2.15              0.05              2.34                       2.83    0.759 14.940682 0.077914 121.500000\n     8  19.0858  7    128.724     2.21              0.05              2.08                      16.27    0.813 81.140045 0.321605 173.117472\n     9   2.6430 11 1  131.367     2.26              0.04              1.95                     426.26    0.944 401.725721 0.277497 270.203769\n    10   0.7516  2    132.119     2.28              0.04              1.90                     462.84    1.373 66.219318 0.065034 81.000000\n    11   0.5550  2    132.674     2.30              0.04              1.85                     429.55    1.435 83.540152 0.210089 62.501130\n    12   0.4856  2    133.159     2.32              0.04              1.80                     410.08    1.481 64.125803 0.195235 39.320559\n    13   0.4923  1    133.652     2.34              0.04              1.74                     419.41    1.526 54.335771 0.040116 34.366129\n    14   0.5994  1    134.251     2.38              0.04              1.64                     427.69    1.780 54.389200 0.031333 37.601526\n    15   0.6983  2    134.949     2.45              0.04              1.47                     414.77    1.830 58.100446 0.145322 51.808579\n    16   0.6842  1    135.634     2.53              0.03              1.31                     426.80    2.376 45.138192 0.044382 40.500000\n    17   0.7675  1    136.401     2.64              0.03              1.24                     438.27    3.069 46.648555 0.031994 40.500000\n    18   0.8610  1    137.262     2.80              0.03              1.13                     446.87    3.860 49.594099 0.028315 40.500000\n    19   0.9659  2    138.228     3.10              0.03              0.97                     408.18    4.456 66.134179 0.188457 50.621290\n    20   0.9591  2    139.187     3.56              0.03              0.74                     413.49    4.504 61.589140 0.059436 61.526612\n    21   0.8474  1    140.034     4.00              0.02              0.54                     430.38    5.119 47.207938 0.026362 40.500000\n    22   0.9506  2    140.985     4.70              0.02              0.39                     441.72    5.129 58.279173 0.024733 59.428335\n    23   0.8582  1    141.843     5.27              0.02              0.34                     459.31    5.957 42.744405 0.013887 40.500000\n    24   0.9627  1    142.806     6.06              0.02              0.28                     472.48    6.693 45.003337 0.020197 40.500000\n    25   1.0800  3    143.886     7.72              0.02              0.20                     475.68    6.658 53.081069 0.190451 58.876801\n    26   0.9805  2    144.866     9.55              0.01              0.13                     460.79    6.688 51.546753 0.151067 55.580296\n    27   0.9217  1    145.788    11.18              0.13              1.15                     470.83    7.092 49.169655 0.087549 40.500000\n    28   1.0340  2    146.822    12.62              1.42             10.11                     449.03    7.247 66.957394 0.208339 52.410874\n    29   1.0062  2    147.828    13.82              6.79             32.95                     451.91    7.277 61.630777 0.030591 42.823862\n    30   1.0961  1    148.924    14.88             12.48             45.62                     454.88    7.737 54.389200 0.017920 35.493414\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31   1.3140  3    150.238    16.50             18.79             53.25                     445.17    7.714 63.329594 0.181195 49.897181\n    32   1.3155  2    151.554    18.32             24.45             57.16                     441.55    7.749 55.483946 0.067684 44.165635\n    33   1.4095  1    152.963    20.48             29.71             59.20                     438.80    8.010 54.389200 0.030928 40.138862\n    34   1.5885  1    154.552    23.17             35.50             60.51                     434.66    8.564 54.389200 0.023212 36.301266\n    35   1.8834  2    156.435    28.47             44.40             60.93                     389.73    8.577 68.644778 0.169593 50.150198\n    36   1.8802  2    158.316    36.14             59.31             62.13                     378.04    8.656 60.398370 0.081447 48.279604\n    37   1.9179  1    160.233    46.93             83.66             64.06                     377.59    9.285 54.389200 0.028813 40.365333\n    38   2.1552  3    162.389   100.66            175.33             63.53                     359.65    9.329 73.907831 0.165723 76.349732\n    39   1.6564  3    164.045   146.37            349.28             70.47                     369.14    9.501 129.057002 0.154429 93.738756\n    40   1.1043  2    165.149   151.72            402.70             72.63                     383.65    9.702 69.775283 0.039340 58.574842\n    41   1.0058  1    166.155   152.86            425.29             73.56                     398.32    9.921 40.390413 0.016992 40.500000\n    42   1.1283  3    167.283   144.83            313.87             68.43                     403.23    9.976 122.925669 0.161756 26.781488\n    43   1.2667  1    168.550   131.73            351.10             72.72                     411.30   10.068 25.619154 0.016408 27.174142\n    44   1.7138  1    170.264   141.12            413.29             74.55                     427.02   10.198 30.499191 0.017675 40.500000\n    45   1.9225  4    172.186   297.11            796.20             72.82                     477.52   10.376 126.285167 0.228225 127.137878\n    46   1.0217  3    173.208   373.92           1017.09             73.12                     515.77   10.681 114.735345 0.202806 121.500000\n    47   0.5623  5    173.770   355.37            659.86             65.00                     513.85   10.850 104.815650 0.181365 36.254166\n    48   0.5939  1    174.364   268.34            674.73             71.55                     519.15   10.966 32.569342 0.047418 11.477388\n    49   1.0529  1    175.417   216.23            690.11             76.14                     537.37   11.062 26.483762 0.027197 20.311575\n    50   1.5936  1    177.011   183.24            695.35             79.14                     562.21   11.200 24.250862 0.018778 31.320204\n    51   2.0262  2    179.037   161.64            695.92             81.15                     580.34   11.392 23.937429 0.135250 37.136289\n    52   2.3754  1    181.412   149.00            692.15             82.29                     598.86   11.622 22.890073 0.064956 40.500000\n    53   2.6647  2    184.077   141.50            701.13             83.21                     602.82   11.850 17.007839 0.209086 51.896831\n    54   2.5973  2    186.674   137.71            694.53             83.45                     620.62   12.068 24.585272 0.040520 49.859962\n    55   2.6014  8    189.276   147.64            688.46             82.34                     627.83   12.128 17.275146 0.152741 67.645500\n    56   2.1649  3    191.441   141.15            686.83             82.95                     636.76   12.330 16.675532 0.092295 87.786549\n    57   1.5119  1    192.953   135.13            689.81             83.62                     641.39   12.771 7.354726 0.031596 40.500000\n    58   1.6961  1    194.649   128.41            691.29             84.33                     646.15   13.176 5.870277 0.024352 40.500000\n    59   1.9027  2    196.551   127.41            680.02             84.22                     637.70   13.280 33.399533 0.172528 31.485872\n    60   2.0647  2    198.616   119.74            681.72             85.06                     639.08   13.424 20.423009 0.117759 31.396935\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    61   2.6222  3    201.238   115.70            688.23             85.61                     640.63   13.564 16.070492 0.118322 56.633524\n    62   2.4375  2    203.676   115.03            695.93             85.82                     645.22   13.759 21.587699 0.077575 63.643298\n    63   2.1087  2    205.785   116.09            704.48             85.85                     652.73   13.927 22.616992 0.038819 56.662829\n    64   1.9595  1    207.744   120.33            715.74             85.61                     659.54   14.213 34.618445 0.017517 40.500000\n    65   2.1981  4    209.942   132.61            733.96             84.70                     667.44   14.297 62.797211 0.131737 88.481899\n    66   1.5267  3    211.469   128.24            714.11             84.78                     670.71   14.431 25.699888 0.136443 51.600991\n    67   1.4993  1    212.968   114.43            715.46             86.21                     673.89   14.483 8.454742 0.068942 25.814516\n    68   2.0720  1    215.040   107.66            707.66             86.80                     680.32   14.521 13.607829 0.047564 39.149753\n    69   2.3652  1    217.405   105.67            707.76             87.01                     687.02   14.690 9.623938 0.028440 40.500000\n    70   2.6533  1    220.059   108.23            715.71             86.86                     693.61   15.040 12.758446 0.020589 40.500000\n    71   2.9765  4    223.035   146.70            793.03             84.39                     703.38   15.094 71.813083 0.208777 121.467848\n    72   1.6383  5    224.673   181.88            846.41             82.31                     713.27   15.283 77.710338 0.122521 112.515847\n    73   0.9556  3    225.629   159.21            792.05             83.26                     715.45   15.380 43.632166 0.168714 35.243385\n    74   1.0494  1    226.678   123.02            810.58             86.82                     718.37   15.420 8.200035 0.073018 11.897290\n    75   1.6469  1    228.325   100.66            798.08             88.80                     725.26   15.504 14.856811 0.030655 17.335457\n    76   2.6279  1    230.953    84.88            787.20             90.27                     735.32   15.605 12.499751 0.026904 28.589608\n    77   3.4793  2    234.432    76.84            792.46             91.16                     740.78   15.753 12.605073 0.157150 48.147932\n    78   3.5545  6    237.987    72.51            782.18             91.52                     747.51   15.949 13.200336 0.065298 54.651552\n    79   3.3751  6    241.362    70.08            773.36             91.69                     753.18   16.120 12.732443 0.031344 49.007489\n    80   3.4138  6    244.776    68.55            768.25             91.81                     756.79   16.252 9.770184 0.114924 37.559019\n    81   3.9796  6    248.756    67.48            765.12             91.90                     760.24   16.338 8.926053 0.147936 48.916724\n    82   4.0295  6    252.785    67.23            764.28             91.91                     763.14   16.439 9.537491 0.137869 52.185941\n    83   3.9313  6    256.716    69.78            767.29             91.66                     765.63   16.523 9.548881 0.075473 50.890234\n    84   3.8917  6    260.608    76.15            775.38             91.06                     765.43   16.600 7.998614 0.121219 59.501058\n    85   3.5105  2    264.119    82.34            784.92             90.51                     760.90   16.806 11.282702 0.152071 81.000000\n    86   2.5922  2    266.711    81.51            782.81             90.57                     762.07   16.972 7.201116 0.055185 66.449771\n    87   2.1820  1    268.893    79.19            783.31             90.82                     763.82   17.332 3.671629 0.020332 40.500000\n    88   2.4477  4    271.341    83.14            778.80             90.35                     761.29   17.412 31.606137 0.203578 30.167331\n    89   2.4230  1    273.763    75.29            777.45             91.17                     761.30   17.562 11.752882 0.084673 25.833965\n    90   3.3475  6    277.111    65.82            776.04             92.18                     765.51   17.673 8.226572 0.038562 40.618966\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    91   3.7495  6    280.860    59.97            774.13             92.81                     769.14   17.833 9.635246 0.122966 46.583862\n    92   3.9018  6    284.762    56.86            774.04             93.16                     771.69   18.006 6.126484 0.130083 50.257796\n    93   3.8903  6    288.652    55.06            772.23             93.34                     775.16   18.169 8.792759 0.059383 46.900151\n    94   4.0332  6    292.686    54.82            774.41             93.39                     777.23   18.317 7.434064 0.114347 50.007519\n    95   4.0329  6    296.719    54.38            774.67             93.44                     779.09   18.473 5.939769 0.073423 60.911242\n    96   3.5857  1    300.304    53.93            773.28             93.48                     780.72   18.900 4.240548 0.020982 40.500000\n    97   4.0224  2    304.327    53.99            774.28             93.48                     781.18   19.004 13.098474 0.199341 55.937018\n    98   3.7669  3    308.094    54.52            781.95             93.48                     778.64   19.166 13.866501 0.167204 41.112324\n    99   4.1563  2    312.250    55.46            790.06             93.44                     777.87   19.330 10.201282 0.132042 43.111713\n   100   4.5115  2    316.761    58.53            797.79             93.16                     777.20   19.528 12.083614 0.132535 52.866328\n   101   4.3684  2    321.130    60.89            795.02             92.89                     778.82   19.743 9.043068 0.084866 61.187853\n   102   3.8731  2    325.003    61.76            791.01             92.76                     781.84   19.957 8.304664 0.035762 64.874812\n   103   3.3104  1    328.313    61.86            789.69             92.74                     784.03   20.412 6.117107 0.014226 40.500000\n   104   3.7136  3    332.027    66.36            787.03             92.22                     783.94   20.418 15.374262 0.165931 64.005550\n   105   3.2012  3    335.228    72.26            808.93             91.80                     783.39   20.574 44.619206 0.175151 74.420652\n   106   2.5027  3    337.731    77.16            830.90             91.50                     786.08   20.721 70.413308 0.067607 78.030376\n   107   1.8955  1    339.626    76.71            835.74             91.59                     788.48   20.927 32.979770 0.022519 40.500000\n   108   2.1263  3    341.753    74.46            817.31             91.65                     788.99   20.984 63.012697 0.148227 31.661915\n   109   2.4955  2    344.248    67.55            818.10             92.37                     791.17   21.046 11.562304 0.051405 37.752072\n   110   2.9016  1    347.150    65.26            817.30             92.61                     794.33   21.176 7.016915 0.030417 40.500000\n   111   3.2551  1    350.405    64.36            816.37             92.69                     797.31   21.412 5.812361 0.019696 40.500000\n   112   3.6515  3    354.056    66.48            826.44             92.55                     797.10   21.500 16.191138 0.181917 67.429744\n   113   3.0450  2    357.101    67.96            830.55             92.44                     797.59   21.656 11.711007 0.128155 44.998132\n   114   3.2296  3    360.331    72.58            836.24             92.01                     799.42   21.755 9.251731 0.161912 57.224944\n   115   2.9832  7    363.314    87.95            877.93             90.89                     803.10   21.853 21.693613 0.125109 74.590559\n   116   2.3288  6    365.643   121.62            937.04             88.51                     810.16   22.032 105.971405 0.125201 159.605046\n   117   1.0338  3    366.677   102.36            899.29             89.78                     812.48   22.216 39.674920 0.154469 17.348486\n   118   1.1884  2    367.865    91.06            901.03             90.82                     814.53   22.290 22.562464 0.092832 23.707385\n   119   1.6989  3    369.564    83.72            889.98             91.40                     817.75   22.368 8.610048 0.079329 47.081832\n   120   1.7575  2    371.321    74.61            883.14             92.21                     821.25   22.486 13.028013 0.108373 22.151549\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n   121   2.3808  1    373.702    66.99            877.93             92.91                     825.76   22.579 10.577721 0.035599 27.485471\n   122   3.2056  1    376.908    61.75            873.00             93.39                     831.59   22.678 9.280162 0.022072 39.867035\n   123   3.6255  3    380.533    64.03            875.26             93.18                     834.64   22.813 11.160558 0.161881 48.456176\n   124   3.6906  3    384.224    67.88            894.17             92.94                     840.10   22.994 25.513880 0.102259 86.818613\n   125   2.5976  5    386.821    74.76            890.72             92.26                     842.13   23.209 25.031044 0.154368 87.027642\n   126   1.8252  2    388.647    64.73            877.09             93.13                     842.82   23.358 31.579330 0.146607 39.455880\n   127   2.0753  2    390.722    53.93            878.52             94.22                     844.14   23.477 17.152039 0.154927 12.803435\n   128   2.3820  1    393.104    45.24            877.59             95.10                     846.14   23.606 10.255168 0.033892 14.771524\n   129   3.9874  2    397.091    37.45            881.52             95.92                     848.31   23.762 8.091295 0.156521 11.788405\n   130   4.5530  1    401.644    31.91            880.99             96.50                     851.05   24.014 8.789110 0.035971 13.829689\n   131   7.7614  1    409.406    26.77            874.37             97.03                     855.45   24.215 5.371084 0.053844 40.500000\n   132   8.7067  2    418.112    23.49            868.48             97.37                     859.11   24.579 5.072401 0.033859 51.056927\n   133   8.6027  1    426.715    22.15            865.85             97.51                     861.00   24.979 2.864426 0.017319 40.500000\n   134   9.6505  1    436.366    21.32            864.69             97.59                     862.40   25.369 3.344406 0.018943 40.500000\n   135  10.8259  3    447.192    21.53            866.88             97.58                     862.47   25.645 7.291181 0.196626 78.775203\n   136   8.1468  2    455.338    21.23            865.93             97.61                     863.50   26.065 4.470115 0.046440 74.876963\n   137   6.3433  4    461.682    23.07            868.44             97.41                     862.49   26.380 13.110900 0.181007 63.702018\n   138   5.4845  3    467.166    22.38            869.00             97.49                     862.50   26.615 5.807871 0.080076 95.137546\n   139   3.6181  1    470.784    21.55            869.52             97.58                     862.76   26.898 1.954948 0.021380 40.500000\n   140   4.0587  2    474.843    20.97            870.64             97.65                     862.11   27.026 11.910442 0.192558 24.670388\n   141   4.1469  2    478.990    19.19            874.43             97.85                     861.80   27.192 3.706411 0.070004 29.362796\n   142   5.4268  1    484.417    17.20            876.26             98.08                     862.38   27.340 3.387740 0.052251 38.968435\n   143   6.2097  2    490.626    15.75            875.17             98.23                     863.71   27.544 3.038652 0.042985 51.573263\n   144   6.1000  1    496.726    14.81            874.21             98.33                     864.71   27.779 2.700364 0.024431 40.500000\n   145   6.8430  1    503.569    13.84            873.88             98.44                     865.70   27.995 2.010659 0.017196 40.500000\n   146   7.6764  3    511.246    13.10            877.33             98.53                     865.49   28.254 9.593477 0.209889 32.593752\n   147   7.4655  1    518.711    11.48            877.51             98.71                     866.24   28.557 4.804993 0.045666 33.888018\n   148   9.1504  2    527.862     9.99            878.36             98.88                     867.87   28.832 3.419234 0.042011 39.946281\n   149  10.3383  1    538.200     8.66            878.65             99.02                     869.63   29.153 3.913612 0.023520 40.500000\n   150  11.5975  2    549.798     7.25            883.17             99.19                     870.38   29.550 6.484789 0.205475 36.568526\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n   151  11.4189  2    561.216     6.01            881.77             99.32                     871.64   29.983 5.057540 0.044356 1.662824\n   152  20.5633  2    581.780     4.82            881.35             99.46                     873.16   30.225 2.037948 0.027329 0.626937\n   153  40.5865  6    622.366     3.16            882.84             99.64                     875.99   30.632 3.338155 0.080705 1.401984\n   154  61.5732  6    683.939     2.16            883.92             99.76                     878.11   31.414 2.580615 0.084826 1.146443\n   155  91.7728  6    775.712     1.68            884.34             99.81                     879.16   32.410 3.005287 0.172971 1.274770\n   156  99.4532  6    875.165     3.01            859.88             99.65                     880.61   37.735 1.127692 0.134143 0.481821\n   157 122.5039  6    997.669    19.58            820.60             97.67                     880.15   47.590 5.904553 0.085392 2.480317\n   158  97.3307  6   1095.000    30.18            821.02             96.45                     878.92   53.680 7.348886 0.055193 3.010159\n   159 166.0183  6   1261.018    47.49            808.18             94.45                     878.55   85.013 3.455481 0.086664 1.387677\n   160 245.5224  6   1506.541    63.91            798.74             92.59                     878.31   92.577 3.080947 0.109035 1.223330\n   161 331.7428  6   1838.283    68.55            801.78             92.12                     878.20   95.179 2.433064 0.126884 0.956477\n   162 365.0000  6   2203.283    85.89            774.44             90.02                     878.43   96.842 1.911800 0.097439 0.746223\n   163 365.0000  6   2568.283    91.92            768.47             89.32                     878.15   97.684 2.683292 0.054513 1.202500\n   164 365.0000  6   2933.283   101.31            765.41             88.31                     877.88   98.186 3.487760 0.031544 1.543589\n   165 365.0000  6   3298.283   110.92            765.28             87.34                     877.65   98.513 3.431565 0.038131 1.497394\n   166 351.7165  6   3650.000   122.82            762.12             86.12                     877.54   98.741 3.016056 0.042507 1.299531\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                 16.811s    99.41%\n|- Newton                                16.416s    97.65%\n  |- Jacobian                            13.083s    79.70%\n  |- Update                               3.130s    19.06%\n  |- Solver                               0.066s     0.40%\n  |- Residual                             0.062s     0.38%\n  |- Logging                              0.008s     0.05%\n|- Output                                 0.370s     2.20%\n|- Input                                  0.000s     0.00%\nInitialization                            0.099s     0.59%\n------------------------------------------------------------\nTOTAL                                    16.910s\n============================================================\n\nTime steps : 166/167, step size: 21.99, 70.85\n')
```

## stflu002.dat

5000x5000x50, 2D diagonal water flooding in uniformed cartesian

```
Running simulation: Uniformed cartesian water flooding

    50  84.4290  1   3650.000  3931.68             69.90              1.75                    3998.10    6.171 40.742222 0.012726 0.012386



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  4.702s    98.02%

|- Newton                                 4.602s    97.87%

  |- Jacobian                             3.545s    77.04%

  |- Update                               0.946s    20.55%

  |- Solver                               0.060s     1.31%

  |- Residual                             0.021s     0.46%

  |- Logging                              0.002s     0.05%

|- Output                                 0.091s     1.94%

|- Input                                  0.000s     0.00%

Initialization                            0.095s     1.98%

------------------------------------------------------------

TOTAL                                     4.797s

============================================================



Time steps : 50/50, step size: 73.00, 128.50

```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//stflu002.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/stflu002.dat\n', stderr='unknown keyword: mxcnrpt\n[MacBook-Air.local:18797] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/2457862144/sm_segment.MacBook-Air.501.92800000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1 1.00e-05  1    1.0e-05  4000.00                                                        4000.00    0.000 0.011954 0.000000 0.000004\n     2 2.33e-05  1    3.3e-05  4000.00                                                        4000.00    0.000 0.027889 0.000000 0.000010\n     3 5.44e-05  1    8.8e-05  4000.00                                                        4000.00    0.000 0.065057 0.000000 0.000022\n     4 1.27e-04  1    2.1e-04  4000.00                                                        4000.00    0.000 0.151708 0.000001 0.000052\n     5 2.96e-04  1    5.1e-04  4000.00                                                        4000.00    0.000 0.353488 0.000002 0.000122\n     6 6.89e-04  1      0.001  4000.00                                                        4000.00    0.000 0.822105 0.000004 0.000283\n     7 1.60e-03  1      0.003  4000.00                                                        4000.00    0.000 1.903704 0.000010 0.000656\n     8 3.68e-03  1      0.006  4000.00                                                        3999.99    0.000 4.364766 0.000022 0.001505\n     9 8.35e-03  2      0.015  4000.00                                                        4000.00    0.000 9.787893 0.000050 0.003374\n    10   0.0183  2      0.033  4000.00                                                        4000.00    0.000 20.935872 0.000110 0.007218\n    11   0.0375  2      0.071  4000.00                                                        4000.00    0.000 40.898958 0.000224 0.014100\n    12   0.0687  2      0.139  3999.05                                                        3998.83    0.002 69.104790 0.000411 0.023822\n    13   0.1097  2      0.249  3999.50                                                        3999.43    0.000 97.934595 0.000656 0.033758\n    14   0.1549  2      0.404  3999.13                                                        3999.49    3.174 108.778400 0.000849 0.037492\n    15   0.2094  1      0.613  3999.07                                                        4003.76   22.521 54.389200 0.000503 0.018625\n    16   0.3586  5      0.972  4000.00                                                        4000.00   14.211 196.812978 0.002135 0.067521\n    17   0.3619  3      1.334  4000.55                                                        3998.77   10.356 155.674733 0.002145 0.053257\n    18   0.4144  4      1.748  4000.00                                                        4000.01    7.901 140.811432 0.002445 0.048268\n    19   0.4988  4      2.247  3999.99                                                        4000.01    6.147 134.463858 0.002924 0.046089\n    20   0.6137  4      2.861  4000.00                                                        4000.00    4.828 131.499342 0.003571 0.044918\n    21   0.7630  4      3.624  4000.00                                                        4000.00    3.812 129.884617 0.004398 0.044164\n    22   0.9542  4      4.578  4000.00                                                        4000.00    3.017 129.009154 0.005436 0.043604\n    23   1.1969  4      5.775  4000.00                                                        4000.00    2.392 128.539410 0.006723 0.043109\n    24   1.5040  4      7.279  4000.00                                                        4000.00    1.898 128.242592 0.008304 0.042582\n    25   1.8919  4      9.171  4000.00                                                        4000.00    1.506 127.861434 0.010229 0.041912\n    26   2.3831  4     11.554  4000.00                                                        4000.00    1.196 127.006583 0.012565 0.040935\n    27   3.0110  4     14.565  4000.00                                                        4000.00    0.948 125.050850 0.015407 0.040735\n    28   3.8315  4     18.396  4000.00                                                        4000.00    0.751 121.120235 0.018916 0.039673\n    29   4.9462  4     23.343  4000.01                                                        4000.00    0.592 114.183534 0.023195 0.037557\n    30   6.5530  4     29.895  4000.00                                                        4000.00    0.462 103.175593 0.028892 0.033614\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31   9.0591  1     38.955  3988.66                                                        4041.29    8.459 54.389200 0.024385 0.016813\n    32  15.5129  5     54.467  4000.00             5e-11             1e-12                    3999.99    6.054 88.674450 0.057569 0.030064\n    33  22.7487  4     77.216  4000.00             4e-11             1e-12                    4000.00    4.273 53.343146 0.072443 0.035617\n    34  35.7936  5    113.010  4000.00             3e-07             7e-09                    4000.00    2.920 91.757111 0.092283 0.066920\n    35  51.7071  5    164.717  4000.01             8e-10             2e-11                    3999.99    2.004 121.927146 0.103009 0.091810\n    36  66.5527  5    231.270  4000.02                                                        4000.01    1.428 120.644180 0.099562 0.100956\n    37  86.0667  5    317.336  4000.00                                                        4000.00    1.041 115.893751 0.093131 0.106900\n    38  47.6637  3    365.000  4000.00             2e-04             4e-06                    4000.00    0.905 54.545423 0.044597 0.055472\n    39  81.5579  5    446.558  4000.00             1e-04             3e-06                    4000.00    0.740 71.558012 0.068019 0.073812\n    40 128.8389  5    575.397  3999.99             3e-04             7e-06                    4000.00    0.704 83.502648 0.089790 0.083665\n    41 188.0542  6    763.451  3999.99             1e-03             2e-05                    4000.00    0.841 79.680089 0.102716 0.075142\n    42 260.4467  6   1023.898  3999.97              0.03             7e-04                    4000.00    1.023 92.582414 0.109207 0.085809\n    43 351.6733  7   1375.571  3999.70              0.30              0.01                    4000.00    1.291 126.363955 0.118677 0.097696\n    44 365.0000  6   1740.571  3998.05              1.79              0.04                    3999.76    1.668 134.754321 0.097694 0.090312\n    45 365.0000  4   2105.571  3995.90              4.35              0.11                    4000.02    2.163 138.823860 0.085074 0.083374\n    46 365.0000  3   2470.571  3990.11             10.61              0.27                    3999.88    2.808 144.696244 0.076058 0.078832\n    47 365.0000  3   2835.571  3981.27             21.14              0.53                    3998.08    3.564 143.031858 0.065263 0.069847\n    48 365.0000  4   3200.571  3959.91             40.08              1.00                    4000.02    4.354 165.147510 0.059786 0.061975\n    49 365.0000  3   3565.571  3938.23             62.83              1.57                    3999.72    5.240 162.896090 0.055656 0.055731\n    50  84.4290  1   3650.000  3931.68             69.90              1.75                    3998.10    6.171 40.742222 0.012726 0.012386\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                  4.702s    98.02%\n|- Newton                                 4.602s    97.87%\n  |- Jacobian                             3.545s    77.04%\n  |- Update                               0.946s    20.55%\n  |- Solver                               0.060s     1.31%\n  |- Residual                             0.021s     0.46%\n  |- Logging                              0.002s     0.05%\n|- Output                                 0.091s     1.94%\n|- Input                                  0.000s     0.00%\nInitialization                            0.095s     1.98%\n------------------------------------------------------------\nTOTAL                                     4.797s\n============================================================\n\nTime steps : 50/50, step size: 73.00, 128.50\n')
```



## stflu003.dat

5000x5000x50, 2D diagonal water flooding in uniformed corner point

```
Running simulation: uniformed corner grid

    49 172.0209  2   3650.000  3929.82             70.28              1.76                    4000.13    5.176 72.981950 0.025955 0.022246



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  3.611s    97.54%

|- Newton                                 3.509s    97.19%

  |- Jacobian                             2.662s    75.87%

  |- Update                               0.764s    21.77%

  |- Solver                               0.045s     1.29%

  |- Residual                             0.018s     0.51%

  |- Logging                              0.002s     0.06%

|- Output                                 0.092s     2.54%

|- Input                                  0.000s     0.00%

Initialization                            0.091s     2.46%

------------------------------------------------------------

TOTAL                                     3.702s

============================================================



Time steps : 49/49, step size: 74.49, 127.50

```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//stflu003.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/stflu003.dat\n', stderr='unknown keyword: mxcnrpt\n[MacBook-Air.local:18810] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/2482176000/sm_segment.MacBook-Air.501.93f30000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1 1.00e-05  1    1.0e-05  4000.00                                                        4000.00    0.000 0.011954 0.000000 0.000004\n     2 2.33e-05  1    3.3e-05  4000.00                                                        4000.00    0.000 0.027888 0.000000 0.000010\n     3 5.44e-05  1    8.8e-05  4000.00                                                        4000.00    0.000 0.065050 0.000000 0.000022\n     4 1.27e-04  1    2.1e-04  4000.00                                                        4000.00    0.000 0.151665 0.000001 0.000052\n     5 2.96e-04  1    5.1e-04  4000.00                                                        4000.00    0.000 0.353245 0.000002 0.000122\n     6 6.89e-04  1      0.001  4000.00                                                        4000.00    0.000 0.820783 0.000004 0.000283\n     7 1.60e-03  1      0.003  4000.00                                                        4000.00    0.000 1.896603 0.000010 0.000654\n     8 3.68e-03  1      0.006  4000.00                                                        3999.95    0.000 4.327555 0.000022 0.001492\n     9 8.35e-03  2      0.015  4000.00                                                        4000.00    0.000 9.603008 0.000050 0.003311\n    10   0.0183  2      0.033  4000.00                                                        4000.00    0.000 20.108730 0.000110 0.006933\n    11   0.0377  2      0.071  4000.00                                                        4000.00    0.000 37.854647 0.000226 0.013050\n    12   0.0702  2      0.141  3999.96                                                        3999.96    0.000 60.779024 0.000420 0.020952\n    13   0.1166  2      0.258  3999.53                                                        3999.46    0.001 81.564718 0.000697 0.028116\n    14   0.1762  1      0.434  3999.37                                                        4001.86   17.232 54.389200 0.000606 0.018743\n    15   0.3018  2      0.736  3996.77                                                        3997.71   15.687 108.778400 0.001555 0.037486\n    16   0.4082  3      1.144  3999.94                                                        3999.92   10.089 121.602927 0.002420 0.041625\n    17   0.5260  3      1.670  4000.00                                                        4000.00    6.911 107.152639 0.003098 0.036751\n    18   0.7160  4      2.386  3999.99                                                        4000.00    4.837 101.435386 0.004178 0.034647\n    19   0.9966  4      3.383  4000.01                                                        3999.99    3.412 98.715021 0.005744 0.033513\n    20   1.4025  4      4.785  4000.00                                                        4000.00    2.412 97.145853 0.007948 0.032685\n    21   1.9861  4      6.771  4000.00                                                        4000.01    1.704 95.135846 0.011000 0.031577\n    22   2.8357  4      9.607  4000.00                                                        4000.00    1.201 90.587113 0.015224 0.029815\n    23   4.1254  4     13.732  3999.99                                                        4000.01    0.840 81.078626 0.021238 0.027064\n    24   6.2484  4     19.981  4000.00                                                        4000.00    0.578 64.987656 0.030316 0.022076\n    25  10.1724  2     30.153  3998.35             7e-15                                      4000.12    0.383 44.230858 0.044800 0.015047\n    26  18.2770  3     48.430  4000.00             3e-10             7e-12                    4000.00    0.238 26.276075 0.069709 0.017057\n    27  29.1156  4     77.546  4000.00                                                        4000.00    0.149 48.646552 0.091301 0.031612\n    28  42.2313  4    119.777  4000.00             1e-05             3e-07                    4000.00    0.096 58.844470 0.103941 0.041107\n    29  58.2063  5    177.983  4000.00             1e-04             3e-06                    4000.00    0.113 60.184012 0.107982 0.047605\n    30  78.9676  5    256.951  4000.01             6e-05             2e-06                    4000.01    0.148 54.841814 0.106892 0.050995\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31 107.5887  4    364.540  4000.01             4e-05             1e-06                    3999.99    0.189 50.155721 0.099888 0.053726\n    32   0.4604  1    365.000  4002.04             4e-05             1e-06                    4002.22    0.246 0.143281 0.000428 0.000171\n    33   1.0713  1    366.071  4000.07             4e-05             1e-06                    4000.14    0.247 0.501732 0.000994 0.000593\n    34   2.4832  1    368.554  3999.97             4e-05             1e-06                    3999.99    0.248 1.002150 0.002295 0.001253\n    35   5.7068  1    374.261  4001.39             4e-05             9e-07                    4000.76    0.250 2.055652 0.005243 0.002669\n    36  12.8661  1    387.127  3999.91             3e-05             9e-07                    3999.85    0.255 4.582524 0.011613 0.005800\n    37  27.8637  1    414.991  4003.09             3e-05             8e-07                    4003.32    0.266 8.723347 0.024293 0.010243\n    38  55.9535  4    470.945  4000.00             2e-05             5e-07                    3999.99    0.288 17.925248 0.044889 0.022941\n    39 100.4866  5    571.431  4000.02             1e-05             3e-07                    4000.00    0.324 30.740512 0.070058 0.028503\n    40 159.8226  6    731.254  3999.97             7e-04             2e-05                    4000.01    0.384 48.917080 0.090523 0.039314\n    41 232.5680  5    963.822  4000.00              0.01             2e-04                    4000.00    0.478 71.536207 0.101109 0.049652\n    42 324.1574  5   1287.979  3999.86              0.14              0.00                    4000.00    0.631 101.700193 0.114468 0.061242\n    43 365.0000  4   1652.979  3999.12              0.89              0.02                    4000.00    0.908 118.169053 0.103884 0.063580\n    44 365.0000  3   2017.979  3996.55              3.51              0.09                    3999.89    1.362 123.165987 0.088721 0.060728\n    45 365.0000  3   2382.979  3992.10              7.94              0.20                    4000.05    1.949 127.811439 0.077862 0.056329\n    46 365.0000  3   2747.979  3981.63             18.44              0.46                    3999.37    2.661 134.954793 0.067678 0.046187\n    47 365.0000  3   3112.979  3965.41             34.73              0.87                    3999.90    3.460 142.810708 0.061456 0.045653\n    48 365.0000  3   3477.979  3942.87             57.73              1.44                    3999.20    4.322 145.256890 0.056359 0.043616\n    49 172.0209  2   3650.000  3929.82             70.28              1.76                    4000.13    5.176 72.981950 0.025955 0.022246\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                  3.611s    97.54%\n|- Newton                                 3.509s    97.19%\n  |- Jacobian                             2.662s    75.87%\n  |- Update                               0.764s    21.77%\n  |- Solver                               0.045s     1.29%\n  |- Residual                             0.018s     0.51%\n  |- Logging                              0.002s     0.06%\n|- Output                                 0.092s     2.54%\n|- Input                                  0.000s     0.00%\nInitialization                            0.091s     2.46%\n------------------------------------------------------------\nTOTAL                                     3.702s\n============================================================\n\nTime steps : 49/49, step size: 74.49, 127.50\n')
```

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_38.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_39.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_40.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_41.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_42.png" | relative_url }})



## stflu004.dat

2D diagonal water flooding for reduction of numerical dispersion and grid orientation effect


```
Running simulation: 2D diagonal flow: grid orientation

    88   2.9579  1   3650.000  3876.73            123.28              3.08                    4000.01   15.314 5.071071 0.001025 0.003036



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                 42.204s    99.67%

|- Newton                                41.876s    99.22%

  |- Jacobian                            30.100s    71.88%

  |- Update                              11.027s    26.33%

  |- Solver                               0.341s     0.81%

  |- Residual                             0.177s     0.42%

  |- Logging                              0.009s     0.02%

|- Output                                 0.309s     0.73%

|- Input                                  0.000s     0.00%

Initialization                            0.142s     0.33%

------------------------------------------------------------

TOTAL                                    42.346s

============================================================



Time steps : 88/108, step size: 41.48, 61.34

```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//stflu004.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/stflu004.dat\n', stderr='[MacBook-Air.local:18823] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/267321344/sm_segment.MacBook-Air.501.fef0000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1 1.00e-05  1    1.0e-05  4000.00                                                        3999.50    0.000 0.382064 0.000002 0.000132\n     2 2.33e-05  1    3.3e-05  4000.00                                                        3998.58    0.000 0.886792 0.000004 0.000306\n     3 5.40e-05  1    8.7e-05  4000.00                                                        3996.59    0.000 2.044133 0.000010 0.000705\n     4 1.24e-04  2    2.1e-04  4000.00                                                        4000.00    0.000 4.647771 0.000024 0.001602\n     5 2.81e-04  2    4.9e-04  4000.00                                                        4000.00    0.000 10.213621 0.000054 0.003521\n     6 6.14e-04  2      0.001  4000.00                                                        4000.00    0.000 20.965209 0.000118 0.007228\n     7 1.26e-03  2      0.002  4000.00                                                        4000.00    0.000 38.066294 0.000241 0.013123\n     8 2.34e-03  2      0.005  4000.00                                                        3999.99    0.000 57.857192 0.000448 0.019945\n     9 3.94e-03  3      0.009  4000.00                                                        4000.00    0.000 72.410581 0.000755 0.024961\n    10 6.20e-03  3      0.015  4000.00                                                        4000.00    0.000 77.305487 0.001187 0.026648\n    11 9.55e-03  3      0.024  4000.00                                                        4000.00    0.000 74.603912 0.001824 0.025718\n    12   0.0149  3      0.039  4000.00                                                        4000.00    0.000 68.770250 0.002834 0.023660\n    13   0.0238  3      0.063  4000.00                                                        4000.00    0.000 63.391857 0.004512 0.021788\n    14   0.0391  3      0.102  4000.00                                                        4000.00    0.000 60.111641 0.007346 0.020620\n    15   0.0651  2      0.167  4001.36                                                        3998.75    0.000 58.634521 0.012082 0.020039\n    16   0.1091  2      0.276  4000.77                                                        3999.69    0.000 58.546690 0.019857 0.019876\n    17   0.1832  2      0.460  4000.01                                                        3999.76    0.000 58.478408 0.032195 0.020107\n    18   0.3075  1      0.767  3998.63                                                        3996.52    2.283 54.389200 0.048101 0.019438\n    19   0.5266  2      1.294  3999.53                                                        3999.49    1.353 59.899392 0.079646 0.021973\n    20   0.8026  1      2.096  4001.27                                                        3999.34    0.831 50.492131 0.105213 0.019312\n    21   1.1006  1      3.197  4000.14                                                        3999.59    0.549 37.022579 0.119108 0.014832\n    22   1.4315  2      4.628  4000.00                                                        4000.00    0.380 23.799702 0.121541 0.010436\n    23   1.8451  1      6.473  3999.97                                                        3999.96    0.273 13.530273 0.115717 0.011630\n    24   2.4304  1      8.904  4000.00                                                        3999.89    0.203 7.343283 0.103962 0.019887\n    25   3.3494  1     12.253  4000.02                                                        3999.99    0.147 4.315913 0.093152 0.030576\n    26   4.8213  2     17.075  4000.00                                                        3999.99    0.106 3.511699 0.121175 0.051476\n    27   6.2227  2     23.297  4000.01                                                        4000.01    0.077 3.739505 0.129310 0.053356\n    28   7.7976  2     31.095  4000.00                                                        4000.00    0.058 4.511945 0.123220 0.045829\n    29   9.9889  2     41.084  4000.00                                                        4000.00    0.044 5.774136 0.110776 0.034280\n    30  13.4065  2     54.490  3999.97                                                        3999.99    0.033 7.731258 0.133628 0.022660\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31  16.5438  2     71.034  3999.99                                                        3999.97    0.025 9.498459 0.134068 0.025424\n    32  20.3835  3     91.417  4000.00                                                        3999.98    0.020 11.688763 0.123190 0.027376\n    33  26.1146  1    117.532  4000.00                                                        4000.00    0.025 14.931350 0.139017 0.023268\n    34  31.6247  3    149.157  4000.01                                                        3999.98    0.031 18.148831 0.134953 0.021668\n    35  38.8438  5    188.001  4000.00             3e-15                                      4000.00    0.039 22.383259 0.142002 0.016146\n    36  46.5590  5    234.560  4000.00             2e-13             4e-15                    4000.00    0.050 26.974994 0.138239 0.017422\n    37  18.8451  1 1  253.405  3999.88             3e-13             7e-15                    4000.23    0.068 11.028232 0.052300 0.006816\n    38  32.6040  5    286.009  3999.99             8e-13             2e-14                    4000.00    0.078 19.059369 0.085377 0.011170\n    39  48.4814  4    334.490  4000.00             1e-11             2e-13                    4000.00    0.094 28.565345 0.109100 0.015686\n    40  30.5099  5    365.000  4000.00             2e-11             6e-13                    4000.00    0.121 18.121127 0.065684 0.009977\n    41  49.5097  4    414.510  4000.00             2e-10             4e-12                    4000.00    0.144 29.632510 0.097295 0.016619\n    42  70.0718  7    484.581  3999.99             4e-09             1e-10                    4000.03    0.183 42.472066 0.119288 0.024275\n    43  30.3581  6 1  514.940  4000.00             8e-09             2e-10                    3999.97    0.249 18.597519 0.050228 0.011588\n    44  53.0662  2    568.006  4000.00             3e-08             6e-10                    4000.00    0.303 32.824213 0.080431 0.020657\n    45  80.6019  2    648.608  3999.99             3e-07             7e-09                    4000.00    0.402 50.621522 0.111371 0.032509\n    46  35.9779  4 1  684.585  4000.00             5e-07             1e-08                    3999.99    0.560 22.916427 0.047808 0.015630\n    47  63.6589  6    748.244  3999.99             1e-06             4e-08                    4000.00    0.663 41.050101 0.076944 0.027546\n    48  98.1767  3    846.421  4000.01             1e-05             3e-07                    4000.01    0.828 64.563176 0.109898 0.044581\n    49 132.2126  3    978.634  4000.00             2e-04             5e-06                    4000.00    1.087 89.550038 0.130791 0.062194\n    50 164.8000  6   1143.434  4000.00              0.00             7e-05                    4000.00    1.449 116.112718 0.140466 0.082878\n    51 198.5775  4   1342.011  3999.97              0.03             7e-04                    3999.97    1.932 147.119019 0.146433 0.104106\n    52 233.9201  8   1575.931  3999.82              0.20              0.00                    3999.99    2.556 184.510000 0.149995 0.133844\n    53 244.7521 10   1820.683  3999.16              0.86              0.02                    3999.99    3.365 207.604654 0.138983 0.151463\n    54   8.8722  5 3 1829.556  3999.11              0.89              0.02                    4000.00    4.391 7.888290 0.005014 0.006021\n    55   6.5558  1 1 1836.111  3999.10              0.91              0.02                    3999.95    4.441 5.796620 0.003692 0.003817\n    56  14.7278  5   1850.839  3999.05              0.95              0.02                    4000.01    4.470 13.095517 0.008263 0.009897\n    57  31.6056  7   1882.445  3998.96              1.05              0.03                    4000.01    4.535 28.311123 0.017685 0.021247\n    58  54.1810  8   1936.626  3998.75              1.26              0.03                    4000.00    4.679 49.194484 0.029994 0.036605\n    59  27.0906  6 1 1963.716  3998.63              1.38              0.03                    4000.01    4.951 24.921438 0.014894 0.018733\n    60  54.1811  7   2017.898  3998.35              1.65              0.04                    4000.02    5.074 50.526044 0.029209 0.037816\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    61  92.8819  6   2110.779  3997.73              2.27              0.06                    4000.00    5.325 88.701957 0.047925 0.066111\n    62 136.1894  3   2246.969  3996.32              3.69              0.09                    3999.99    5.800 134.968686 0.068064 0.095467\n    63 167.2685  4   2414.237  3993.45              6.55              0.16                    3999.97    6.479 174.683844 0.078119 0.125775\n    64 180.3107 12   2594.548  3988.35             11.66              0.29                    3999.99    7.320 200.112617 0.080403 0.147720\n    65 180.2527 11   2774.801  3980.45             19.57              0.49                    3999.99    8.279 213.391552 0.075656 0.155764\n    66 173.6101 10   2948.411  3969.40             30.61              0.77                    4000.00    9.294 219.301175 0.069975 0.160670\n    67 164.5366 10   3112.948  3955.08             44.93              1.12                    4000.00   10.324 221.379607 0.063005 0.161360\n    68 155.0645 11   3268.012  3937.49             62.52              1.56                    4000.01   11.346 221.680536 0.057879 0.161384\n    69 146.0194 12   3414.032  3916.74             83.27              2.08                    4000.00   12.350 221.151392 0.052294 0.161050\n    70   5.1000  6 3 3419.132  3916.01             84.00              2.10                    4000.00   13.593 7.988938 0.001824 0.005891\n    71  10.1999  6   3429.331  3914.52             85.47              2.14                    4000.00   13.619 16.002472 0.003638 0.011725\n    72  20.3998  6   3449.731  3911.49             88.52              2.21                    4000.00   13.672 32.196051 0.007237 0.023540\n    73  39.1882 13   3488.920  3905.33             94.68              2.37                    4000.00   13.780 62.553617 0.013817 0.045605\n    74  12.0579  6 1 3500.977  3903.39             96.61              2.42                    4000.00   14.116 19.452531 0.004248 0.014218\n    75  24.1159  6   3525.093  3899.41            100.59              2.51                    3999.99   14.177 39.180644 0.008480 0.028577\n    76  44.6164 11   3569.710  3891.61            108.40              2.71                    3999.99   14.308 73.431656 0.015609 0.053457\n    77   5.4081  6 2 3575.118  3890.65            109.35              2.73                    4000.00   14.717 8.993492 0.001891 0.006599\n    78   3.6054  6 1 3578.723  3889.99            109.99              2.75                    3999.99   14.761 6.013053 0.001260 0.004402\n    79   7.2108  6   3585.934  3888.72            111.28              2.78                    3999.99   14.780 12.044027 0.002517 0.008816\n    80   4.8072  6 1 3590.741  3887.85            112.14              2.80                    3999.98   14.838 8.050631 0.001677 0.005893\n    81   9.6144  6   3600.356  3886.11            113.89              2.85                    4000.00   14.863 16.145531 0.003350 0.011813\n    82  19.2288  9   3619.584  3882.53            117.48              2.94                    3999.98   14.912 32.466446 0.006686 0.023721\n    83   8.5461  6 1 3628.130  3880.91            119.09              2.98                    3999.99   15.079 14.512975 0.002969 0.010623\n    84   5.6974  1 1 3633.828  3879.86            120.17              3.00                    4000.00   15.161 9.685795 0.001978 0.005798\n    85   4.1626  6 1 3637.990  3879.02            120.96              3.02                    3999.98   15.207 7.112982 0.001444 0.005205\n    86   2.7750  5 1 3640.765  3878.49            121.49              3.04                    3999.99   15.241 4.743814 0.000963 0.003476\n    87   6.2766  7   3647.042  3877.30            122.70              3.07                    3999.98   15.254 10.742496 0.002175 0.007867\n    88   2.9579  1   3650.000  3876.73            123.28              3.08                    4000.01   15.314 5.071071 0.001025 0.003036\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                 42.204s    99.67%\n|- Newton                                41.876s    99.22%\n  |- Jacobian                            30.100s    71.88%\n  |- Update                              11.027s    26.33%\n  |- Solver                               0.341s     0.81%\n  |- Residual                             0.177s     0.42%\n  |- Logging                              0.009s     0.02%\n|- Output                                 0.309s     0.73%\n|- Input                                  0.000s     0.00%\nInitialization                            0.142s     0.33%\n------------------------------------------------------------\nTOTAL                                    42.346s\n============================================================\n\nTime steps : 88/108, step size: 41.48, 61.34\n')
```

![png]({{ "/assets/images/benchmark_image_43.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_44.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_45.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_46.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_47.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_48.png" | relative_url }})

## stflu007.dat

PEBI_GRID


```
Running simulation: 2D diagonal flow: pebi grid

    61 332.2013  4   3650.000  3928.62             71.59              1.79                    3999.99    3.653 179.567875 0.068498 0.094911



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                 39.901s    99.72%

|- Newton                                39.677s    99.44%

  |- Jacobian                            31.563s    79.55%

  |- Update                               6.999s    17.64%

  |- Solver                               0.847s     2.13%

  |- Residual                             0.131s     0.33%

  |- Logging                              0.006s     0.01%

|- Output                                 0.204s     0.51%

|- Input                                  0.002s     0.01%

Initialization                            0.111s     0.28%

------------------------------------------------------------

TOTAL                                    40.012s

============================================================



Time steps : 61/62, step size: 59.84, 107.86

```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//stflu007.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/stflu007.dat\n', stderr='[MacBook-Air.local:18999] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/271187968/sm_segment.MacBook-Air.501.102a0000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1 1.00e-05  1    1.0e-05  4000.00                                                        4000.00    0.000 0.049783 0.000000 0.000017\n     2 2.33e-05  1    3.3e-05  4000.00                                                        4000.00    0.000 0.116103 0.000001 0.000040\n     3 5.44e-05  1    8.8e-05  4000.00                                                        4000.00    0.000 0.270597 0.000001 0.000093\n     4 1.27e-04  1    2.1e-04  4000.00                                                        4000.00    0.000 0.629709 0.000003 0.000217\n     5 2.94e-04  1    5.1e-04  4000.00                                                        4000.00    0.000 1.460241 0.000007 0.000503\n     6 6.80e-04  1      0.001  4000.00                                                        3999.99    0.000 3.358784 0.000017 0.001158\n     7 1.55e-03  1      0.003  4000.00                                                        3999.84    0.000 7.585270 0.000039 0.002615\n     8 3.45e-03  2      0.006  4000.00                                                        4000.00    0.000 16.466738 0.000086 0.005677\n     9 7.25e-03  2      0.013  4000.00                                                        4000.00    0.000 33.045733 0.000181 0.011392\n    10   0.0139  2      0.027  3999.88                                                        3999.85    0.000 58.092367 0.000346 0.020026\n    11   0.0233  2      0.051  3999.88                                                        3999.88    0.000 85.870361 0.000581 0.029600\n    12   0.0346  2      0.085  3999.01                                                        3998.97    0.004 107.504640 0.000861 0.037054\n    13   0.0470  2      0.132  3997.24                                                        3997.94    3.291 108.778400 0.001060 0.037442\n    14   0.0636  3      0.196  3996.75                                                        3996.26    2.222 132.335767 0.001575 0.045553\n    15   0.0788  3      0.275  3999.32                                                        3996.87    1.582 131.620277 0.001946 0.045295\n    16   0.0980  4      0.373  4000.00                                                        4000.00    1.166 143.163830 0.002408 0.049286\n    17   0.1170  4      0.490  4000.00                                                        4000.00    0.887 150.138280 0.002858 0.051637\n    18   0.1364  3      0.626  3994.87                                                        3993.71    0.680 149.075250 0.003308 0.051206\n    19   0.1596  4      0.786  4000.00                                                        4000.00    0.541 146.284868 0.003844 0.050193\n    20   0.1886  4      0.974  3999.99                                                        4000.01    0.437 143.102667 0.004498 0.049038\n    21   0.2252  4      1.199  4000.00                                                        4000.00    0.355 140.363814 0.005312 0.048034\n    22   0.2714  4      1.471  3999.99                                                        4000.01    0.289 138.196270 0.006320 0.047225\n    23   0.3296  4      1.800  4000.00                                                        4000.01    0.236 136.477056 0.007558 0.046566\n    24   0.4027  3      2.203  3992.92                                                        3990.17    0.197 133.815504 0.009042 0.045571\n    25   0.4966  5      2.700  4000.00                                                        4000.01    0.161 134.515138 0.010940 0.045825\n    26   0.6109  5      3.310  3999.99                                                        4000.01    0.131 134.304598 0.013119 0.046437\n    27   0.7521  4      4.063  4000.00                                                        4000.00    0.107 135.199881 0.015677 0.046807\n    28   0.9229  5      4.985  3999.99                                                        4000.01    0.087 135.731294 0.018514 0.047609\n    29   1.1305  4      6.116  3999.99                                                        4000.01    0.071 136.405619 0.021632 0.048361\n    30   1.3816  5      7.498  4000.00                                                        4000.01    0.058 137.492538 0.025092 0.048899\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31   1.6819  5      9.179  4000.00                                                        4000.00    0.047 138.297516 0.028858 0.049026\n    32   2.0419  5     11.221  3999.99                                                        4000.02    0.039 138.457109 0.032666 0.048958\n    33   2.4776  5     13.699  4000.00                                                        4000.00    0.032 138.096841 0.036572 0.048303\n    34   3.0099  5     16.709  3999.99                                                        4000.00    0.026 137.016430 0.040892 0.047879\n    35   3.6704  5     20.379  4000.00                                                        4000.00    0.024 134.819612 0.044780 0.047319\n    36   4.5104  5     24.890  4000.02                                                        4000.00    0.032 130.931405 0.049342 0.046301\n    37   5.6193  5     30.509  4000.00                                                        4000.00    0.042 124.683136 0.053534 0.044737\n    38   7.1600  5     37.669  4000.00                                                        4000.00    0.055 115.392992 0.059085 0.042095\n    39   9.4427  3     47.112  3998.55             3e-15                                      4000.81    0.072 101.690429 0.064255 0.041440\n    40  13.1309  5     60.243  4000.00             1e-09             3e-11                    4000.00    0.092 86.806914 0.071904 0.073266\n    41  19.4075  5     79.650  4000.00             1e-09             4e-11                    4000.00    0.119 71.105248 0.078844 0.124518\n    42  29.6823  5    109.332  4000.00             8e-11             2e-12                    4000.01    0.153 121.164221 0.101143 0.186035\n    43  38.3119  6    147.644  3999.99             4e-06             1e-07                    3999.99    0.196 142.245895 0.107619 0.205630\n    44  45.8831  6    193.527  4000.00             2e-05             5e-07                    4000.00    0.246 141.082556 0.103314 0.183492\n    45  55.1703  6    248.698  3999.99             2e-05             6e-07                    4000.00    0.299 133.285544 0.094970 0.149698\n    46  68.1630  6    316.861  4000.00             2e-05             4e-07                    4000.00    0.357 127.920280 0.101505 0.169753\n    47  48.1394  4    365.000  4000.00             5e-11             1e-12                    4000.00    0.422 75.946249 0.064550 0.112732\n    48  74.5699  5    439.570  4000.01             1e-13             3e-15                    4000.00    0.471 91.591424 0.085821 0.133117\n    49 108.0315  5    547.601  4000.00             7e-06             2e-07                    4000.00    0.538 103.015550 0.101753 0.133209\n    50 149.4415  6    697.043  4000.00             2e-05             6e-07                    4000.00    0.626 102.707024 0.118376 0.159294\n    51 194.8925  6    891.935  4000.00             7e-04             2e-05                    4000.00    0.740 92.352025 0.120472 0.146764\n    52 252.1976  6   1144.133  3999.98              0.02             4e-04                    4000.00    0.882 98.187616 0.126787 0.139651\n    53 318.9068  7   1463.040  3999.81              0.18              0.00                    4000.00    1.067 125.582755 0.130792 0.123327\n    54 365.0000  6   1828.040  3998.78              1.22              0.03                    4000.00    1.312 147.935862 0.124018 0.131487\n    55 365.0000  4   2193.040  3996.47              4.43              0.11                    4000.00    1.630 152.715918 0.105121 0.124933\n    56 121.6669  2 1 2314.707  3994.75              5.77              0.14                    4000.52    2.006 53.009706 0.034476 0.041371\n    57 209.7605 14   2524.467  3990.68              9.31              0.23                    4000.00    2.171 93.833705 0.055636 0.069249\n    58 179.7947  2   2704.262  3987.60             13.48              0.34                    3999.10    2.465 79.821998 0.044463 0.057084\n    59 273.8126  3   2978.075  3976.43             23.52              0.59                    4000.12    2.740 132.094688 0.064774 0.085587\n    60 339.7242  3   3317.799  3958.94             43.69              1.09                    3998.45    3.163 160.412080 0.072786 0.097509\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    61 332.2013  4   3650.000  3928.62             71.59              1.79                    3999.99    3.653 179.567875 0.068498 0.094911\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                 39.901s    99.72%\n|- Newton                                39.677s    99.44%\n  |- Jacobian                            31.563s    79.55%\n  |- Update                               6.999s    17.64%\n  |- Solver                               0.847s     2.13%\n  |- Residual                             0.131s     0.33%\n  |- Logging                              0.006s     0.01%\n|- Output                                 0.204s     0.51%\n|- Input                                  0.002s     0.01%\nInitialization                            0.111s     0.28%\n------------------------------------------------------------\nTOTAL                                    40.012s\n============================================================\n\nTime steps : 61/62, step size: 59.84, 107.86\n')
```

![png]({{ "/assets/images/benchmark_image_49.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_50.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_51.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_52.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_53.png" | relative_url }})

# SPE4C

* Steam flood on three component live oil

* 'Water', 'LiteOil', 'Medm oil', 'Heavy oil'


## Run & Load

```
Running simulation: SPE4-C benchmark on live oil

   190 208.3182  3   3650.000     0.03             27.22             99.89                      27.02   42.160 0.550427 0.007453 6.941673



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                               1m 36.51s    99.86%

|- Newton                              1m 35.89s    99.36%

  |- Jacobian                          1m 21.67s    85.17%

  |- Update                              11.875s    12.38%

  |- Solver                               1.795s     1.87%

  |- Residual                             0.200s     0.21%

  |- Logging                              0.014s     0.01%

|- Output                                 0.565s     0.59%

|- Input                                  0.001s     0.00%

Initialization                            0.132s     0.14%

------------------------------------------------------------

TOTAL                                  1m 36.64s

============================================================



Time steps : 190/263, step size: 19.21, 52.46

```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//stspe003.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/stspe003.dat\n', stderr='[MacBook-Air.local:19128] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/499449856/sm_segment.MacBook-Air.501.1dc50000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1   0.1000  1      0.100   117.45             2e-07             2e-07                      37.50    0.032 28.512388 0.000862 11.674273\n     2   0.1779  1      0.278    98.27              0.03              0.03                      37.50    0.031 13.785685 0.043735 19.666961\n     3   0.2724  2      0.550    87.97              0.04              0.05                      37.50    0.031 6.461069 0.056349 28.238172\n     4   0.3625  2      0.913    82.29              0.05              0.06                      37.50    0.031 4.935756 0.050117 35.092279\n     5   0.4370  2      1.350    78.71              0.05              0.06                      37.50    0.031 3.994988 0.038890 39.383142\n     6   0.4973  2      1.847    76.13              0.05              0.07                      37.50    0.031 2.959249 0.029469 41.546896\n     7   0.5505  2      2.398    74.08              0.05              0.07                      37.50    0.031 1.749585 0.023320 42.357359\n     8   0.6032  4      3.001    72.52              0.05              0.08                      37.50    0.031 41.886928 0.208020 24.888480\n     9   0.5897  2      3.590    71.45              0.06              0.08                      37.50    0.034 5.890775 0.088087 14.498202\n    10   0.8668  2      4.457    70.23              0.06              0.08                      37.50    0.044 12.197645 0.039018 20.019427\n    11   1.3186  2      5.776    68.56              0.06              0.08                      37.50    0.060 8.801548 0.026696 27.647561\n    12   1.7711  2      7.547    66.37              0.06              0.09                      37.50    0.084 5.291881 0.030427 34.193550\n    13   2.1615  1      9.708    63.86              0.06              0.09                      37.50    0.132 4.681459 0.033757 37.906831\n    14   2.5082  1     12.217    61.25              0.06              0.09                      37.50    0.199 3.730047 0.025519 40.500000\n    15   2.8136  1     15.030    58.64              0.06              0.10                      37.51    0.288 3.508415 0.026698 40.500000\n    16   3.1563  3     18.187    59.98              0.06              0.10                      37.50    0.362 26.754642 0.271760 43.132002\n    17   2.6193  4     20.806    60.50              0.06              0.09                      37.50    0.455 10.182339 0.193884 28.339546\n    18   2.6659  2     23.472    59.87              0.06              0.10                      37.50    0.537 7.215549 0.091798 25.993796\n    19   3.6738  2     27.146    57.82              0.06              0.10                      37.50    0.622 8.380619 0.044713 32.180447\n    20   4.6133  2     31.759    54.91              0.06              0.10                      37.50    0.738 5.856750 0.023552 36.683482\n    21   5.4415  3     37.200    54.49              0.06              0.10                      37.50    0.882 5.952967 0.167910 34.223937\n    22   5.9907  2     43.191    54.26              0.06              0.11                      37.50    1.059 1.439639 0.106215 36.636157\n    23   7.0706  3     50.262    57.23              0.06              0.10                      37.50    1.259 12.095310 0.189502 31.703178\n    24   7.2893  2     57.551    56.56              0.08              0.15                      37.50    1.495 4.058648 0.113654 35.150551\n    25   8.7792  2     66.330    52.39              0.44              0.84                      37.50    1.736 6.707475 0.048668 43.415020\n    26   9.4936  4     75.824    47.70              2.02              4.07                      37.50    2.013 4.179038 0.183316 44.382303\n    27   9.9688  3     85.793    48.73              5.14              9.55                      37.50    2.318 10.188818 0.171764 36.692130\n    28  10.8436  3     96.636    48.77              9.10             15.72                      37.50    2.634 4.291327 0.162534 31.306867\n    29  12.1436  2    108.780    45.25             11.63             20.45                      37.50    2.978 4.011185 0.123891 42.589204\n    30  13.2672  3    122.047    41.64             13.84             24.94                      37.50    3.348 3.789874 0.133641 47.163871\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31  13.7117  5    135.759    41.23             17.43             29.71                      37.50    3.751 3.673843 0.241183 36.951012\n    32  12.2681  2    148.027    39.38             19.73             33.38                      37.50    4.202 2.294171 0.126232 36.121637\n    33  14.5808  3    162.608    36.56             21.17             36.68                      37.50    4.585 3.660821 0.170899 41.452749\n    34  15.9031  4    178.511    35.06             23.28             39.90                      37.50    5.043 4.752290 0.215226 43.764269\n    35  15.2401  4    193.751    34.83             26.45             43.16                      37.50    5.567 2.353555 0.160060 47.691210\n    36  15.6531  2    209.404    33.35             28.09             45.71                      37.50    6.118 3.167447 0.205597 48.701036\n    37  15.4067  4    224.811    31.69             29.49             48.20                      37.50    6.653 2.613089 0.232009 45.328339\n    38  14.1158  3    238.926    30.28             31.07             50.65                      37.50    7.211 1.458596 0.179384 26.082765\n    39  14.9993  2    253.926    28.78             32.41             52.97                      37.50    7.737 3.502400 0.197471 37.925939\n    40  15.1085  2    269.034    27.47             33.46             54.92                      37.50    8.302 3.739568 0.109830 50.199153\n    41  15.0742  3    284.108    26.47             33.44             55.81                      37.50    8.867 3.305402 0.243029 31.727405\n    42  13.4238  3    297.532    26.49             34.64             56.66                      37.50    9.446 2.537549 0.162762 31.774092\n    43  15.0221  3    312.554    26.46             36.40             57.91                      37.50    9.926 2.281722 0.152280 33.843937\n    44  17.3936  4    329.948    25.56             38.06             59.83                      37.50   10.458 2.246764 0.180306 35.843219\n    45  18.4306  2    348.379    24.36             40.02             62.16                      37.50   11.160 2.215980 0.189152 44.544821\n    46  19.0201  5    367.399    23.30             40.26             63.34                      37.50   11.852 2.793248 0.277735 47.670155\n    47  15.5635  3    382.962    24.20             42.35             63.64                      37.50   12.630 2.415418 0.135312 35.090220\n    48  18.7602  5    401.722    25.01             43.43             63.45                      37.50   13.196 3.458791 0.216852 24.644537\n    49  17.8984  3    419.621    23.71             43.32             64.63                      37.50   13.942 3.157383 0.192651 38.540056\n    50  18.2823  4    437.903    22.96             43.94             65.68                      37.50   14.628 2.772813 0.202934 45.547982\n    51  18.1303  4    456.033    24.68             43.45             63.77                      37.50   15.340 2.231357 0.231326 32.126415\n    52  16.6409  3    472.674    24.20             43.60             64.31                      37.50   16.067 2.533160 0.159517 31.945064\n    53  18.8174  4    491.492    23.83             43.81             64.77                      37.50   16.692 2.797316 0.243676 35.499603\n    54  16.7297  3    508.221    26.37             41.94             61.40                      37.50   17.460 3.823855 0.176664 37.801551\n    55  17.9248  5    526.146    23.50             37.32             61.36                      37.50   18.100 4.561380 0.210556 47.013607\n    56  17.4001  4    543.546    16.43             34.71             67.87                      37.48   18.788 8.230419 0.199561 19.251953\n    57  17.4219  4    560.968    13.54             33.99             71.51                      37.50   19.420 2.617098 0.110627 19.775881\n    58  23.3961  4    584.364    12.17             34.22             73.77                      37.50   19.937 2.642359 0.174882 26.196739\n    59  25.2050  4    609.569    12.17             34.59             73.98                      37.51   20.679 4.939528 0.167076 26.705594\n    60  27.8222  5    637.391    11.62             34.46             74.79                      37.50   21.429 3.081208 0.149726 35.442089\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    61  32.4889  4    669.880    11.52             36.68             76.10                      37.50   22.220 5.492216 0.190267 39.615130\n    62  33.4182  4    703.298    11.15             37.42             77.05                      37.50   23.172 3.899112 0.227169 41.194858\n    63  31.0109  4    734.309    11.02             37.67             77.37                      37.49   24.186 2.269262 0.220568 51.359525\n    64  29.2897  5    763.599    11.07             38.59             77.70                      37.49   25.107 2.899902 0.221794 29.324001\n    65  27.5728  5    791.172    11.13             40.68             78.53                      37.50   25.970 3.380037 0.125279 62.886385\n    66  24.0333  7    815.205    11.94             41.53             77.68                      37.49   26.813 4.149298 0.199089 45.111063\n    67   0.0992  4 5  815.304     9.20             33.52             78.46                      37.22   27.872 11.227261 0.013196 0.509256\n    68   0.0709  4 1  815.375     6.60             26.80             80.23                      37.09   27.879 11.662784 0.019060 0.508480\n    69   0.1468  4    815.522     7.81             31.63             80.19                      37.47   27.883 8.927368 0.008572 0.508704\n    70   0.1077  4 1  815.630     7.55             31.77             80.80                      37.45   27.890 0.350294 0.006516 0.474512\n    71   0.0803  4 1  815.710     7.06             30.44             81.17                      37.25   27.896 1.659878 0.006842 0.397670\n    72   0.0597  4 1  815.770     5.95             27.16             82.02                      37.09   27.902 4.407537 0.008652 0.364140\n    73   0.1318  4    815.902     6.93             31.35             81.89                      37.40   27.905 5.389747 0.008112 0.540885\n    74   0.0972  4 1  815.999     7.19             32.94             82.08                      37.25   27.912 1.411307 0.005981 0.362433\n    75   0.0727  4 1  816.072     6.54             30.81             82.49                      37.43   27.917 2.621193 0.004833 0.337055\n    76   0.1644  4    816.236     6.46             30.99             82.74                      37.39   27.922 0.810764 0.005541 0.550503\n    77   0.1233  4 1  816.359     6.66             32.14             82.83                      37.46   27.931 1.145982 0.002998 0.369220\n    78   0.0940  4 1  816.453     6.46             31.22             82.87                      37.47   27.937 0.814650 0.003174 0.351482\n    79   0.0716  4 1  816.525     5.24             26.96             83.74                      36.84   27.943 4.917221 0.010290 0.333154\n    80   0.1564  4    816.681     6.38             31.61             83.20                      37.42   27.947 5.499834 0.010204 0.447619\n    81   0.1139  4 1  816.795     6.59             32.80             83.26                      37.25   27.955 0.976177 0.006483 0.283386\n    82   0.0849  4 1  816.880     6.38             31.90             83.34                      37.36   27.961 1.039215 0.002132 0.214125\n    83   0.1953  6    817.075     5.77             30.35             84.02                      37.37   27.967 3.475116 0.005110 0.470992\n    84   0.1302  4 1  817.206     5.77             30.39             84.04                      37.39   27.978 0.559637 0.003471 0.213474\n    85   0.0990  4 1  817.305     6.14             31.43             83.65                      37.25   27.984 1.933361 0.002554 0.160254\n    86   0.0757  4 1  817.380     5.35             28.58             84.23                      37.04   27.990 3.420972 0.004783 0.190173\n    87   0.1712  4    817.552     5.83             30.56             83.99                      37.30   27.996 2.201759 0.004773 0.203517\n    88   0.1291  4 1  817.681     6.08             31.42             83.78                      37.45   28.004 1.190807 0.003512 0.104009\n    89   0.0981  4 1  817.779     5.57             29.23             84.00                      37.26   28.012 2.187404 0.004070 0.161318\n    90   0.2228  6    818.002     5.85             30.47             83.89                      37.36   28.018 2.031356 0.006110 0.200159\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    91   0.1485  4 1  818.150     6.21             31.69             83.61                      37.44   28.029 1.445265 0.003943 0.119006\n    92   0.1126  4 1  818.263     6.00             30.68             83.65                      37.29   28.037 1.250887 0.003512 0.090577\n    93   0.0856  4 1  818.348     4.75             26.12             84.61                      37.17   28.044 5.372761 0.013213 0.124320\n    94   0.1835  4    818.532     5.83             29.55             83.53                      37.41   28.050 5.440506 0.005064 0.148846\n    95   0.1377  4 1  818.669     5.05             27.08             84.27                      36.98   28.060 3.286714 0.007825 0.131060\n    96   0.3054  4    818.975     6.67             32.97             83.17                      37.31   28.067 6.752819 0.015540 0.250554\n    97   0.2152  4 1  819.190     6.52             32.49             83.28                      37.28   28.082 0.710963 0.005095 0.177689\n    98   0.1619  4 1  819.352     6.52             32.16             83.13                      37.39   28.093 0.777266 0.003762 0.133967\n    99   0.1228  4 1  819.475     5.31             27.49             83.81                      37.27   28.102 5.076061 0.014990 0.101851\n   100   0.2606  4    819.735     6.39             30.79             82.82                      37.43   28.109 4.677585 0.006149 0.217412\n   101   0.1947  4 1  819.930     5.53             27.66             83.33                      37.32   28.124 3.293130 0.011413 0.163069\n   102   0.4221  6    820.352     7.18             32.86             82.06                      37.44   28.133 6.037300 0.008470 0.357113\n   103   0.0938  4 2  820.446     4.48             23.70             84.09                      37.09   28.155 11.429234 0.024169 0.098859\n   104   0.1885  4    820.634     4.20             22.67             84.37                      37.22   28.163 1.294893 0.023441 0.160435\n   105   0.1268  3 1  820.761     4.22             22.65             84.30                      37.22   28.174 0.621417 0.013488 0.108548\n   106   0.0905  3 1  820.852     4.45             23.30             83.97                      37.27   28.181 1.084598 0.006736 0.079656\n   107   0.2021  3    821.054     4.82             24.22             83.39                      37.29   28.188 1.468700 0.009436 0.184358\n   108   0.1479  3 1  821.202     5.08             24.83             83.03                      37.40   28.198 0.920549 0.004446 0.136233\n   109   0.1117  3 1  821.313     5.23             25.19             82.82                      37.30   28.206 0.501344 0.002553 0.102997\n   110   0.2563  3    821.569     5.44             25.69             82.52                      37.40   28.213 0.710439 0.005072 0.234549\n   111   0.1928  3 1  821.762     5.58             26.00             82.34                      37.45   28.226 0.445006 0.003582 0.177498\n   112   0.1465  3 1  821.909     5.67             26.20             82.22                      37.48   28.236 0.281387 0.002585 0.135403\n   113   0.3359  3    822.245     5.82             26.50             82.00                      37.31   28.244 0.479544 0.005304 0.313298\n   114   0.2524  3 1  822.497     5.92             26.71             81.85                      37.48   28.261 0.340882 0.003710 0.237762\n   115   0.1915  3 1  822.689     6.00             26.85             81.75                      37.26   28.273 0.232332 0.002659 0.181148\n   116   0.1464  3 1  822.835     6.05             26.94             81.67                      37.45   28.283 0.164909 0.001956 0.139098\n   117   0.3372  3    823.172     6.15             27.13             81.51                      37.26   28.291 0.342704 0.004073 0.322837\n   118   0.2553  3 1  823.427     6.24             27.27             81.39                      37.25   28.307 0.264662 0.002870 0.246258\n   119   0.1948  3 1  823.622     6.30             27.38             81.30                      37.38   28.319 0.191558 0.002090 0.189186\n   120   0.4484  3    824.071     6.43             27.59             81.11                      37.28   28.329 0.408740 0.004212 0.440901\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n   121   0.3392  3 1  824.410     6.52             27.74             80.97                      37.35   28.350 0.304528 0.002889 0.335834\n   122   0.2589  3 1  824.669     6.59             27.85             80.86                      37.31   28.366 0.217206 0.002037 0.258001\n   123   0.1986  3 1  824.867     6.64             27.93             80.79                      37.41   28.378 0.158482 0.001492 0.199266\n   124   0.4589  3    825.326     6.75             28.09             80.62                      37.28   28.387 0.346133 0.002998 0.465471\n   125   0.3499  3 1  825.676     6.83             28.22             80.50                      37.39   28.408 0.263462 0.002067 0.357708\n   126   0.2685  3 1  825.945     6.90             28.31             80.41                      37.35   28.424 0.197818 0.001479 0.276580\n   127   0.6203  3    826.565     7.02             28.48             80.22                      37.31   28.435 0.416376 0.002884 0.647022\n   128   0.4734  3 1  827.038     7.12             28.61             80.08                      37.42   28.463 0.310499 0.001974 0.499531\n   129   0.3633  3 1  827.402     7.19             28.72             79.99                      37.37   28.483 0.223655 0.001467 0.385921\n   130   0.2797  3 1  827.682     7.24             28.79             79.92                      37.34   28.499 0.166728 0.001110 0.298841\n   131   0.6475  3    828.329     7.34             28.93             79.76                      37.34   28.510 0.351202 0.002482 0.701191\n   132   0.4944  3 1  828.823     7.43             29.09             79.66                      37.38   28.538 0.266477 0.001842 0.540568\n   133   0.3791  3 1  829.203     7.48             29.13             79.56                      37.35   28.559 0.194081 0.001384 0.417116\n   134   0.8748  3    830.077     7.61             29.31             79.39                      37.34   28.572 0.412115 0.003049 0.978094\n   135   0.6631  3 1  830.740     7.70             29.44             79.28                      37.37   28.608 0.410383 0.002111 0.749176\n   136   0.5056  3 1  831.246     7.76             29.55             79.20                      37.41   28.635 0.346002 0.002400 0.575316\n   137   0.3871  3 1  831.633     7.81             29.63             79.15                      37.37   28.656 0.222747 0.002283 0.442610\n   138   0.8896  3    832.523     7.91             29.84             79.06                      37.37   28.667 0.405263 0.008203 1.027968\n   139   0.6561  3 1  833.179     7.98             30.02             79.01                      37.38   28.703 0.253497 0.007238 0.763137\n   140   0.4868  3 1  833.666     8.03             30.17             78.98                      37.45   28.729 0.177403 0.005867 0.569213\n   141   1.0931  3    834.759     8.14             30.49             78.93                      37.41   28.742 0.369651 0.014591 1.290885\n   142   0.7748  3 1  835.533     8.22             30.73             78.91                      37.40   28.785 0.250772 0.010910 0.920885\n   143   0.5618  3 1  836.095     8.27             30.90             78.89                      37.42   28.815 0.175413 0.008093 0.670637\n   144   1.2437  3    837.339     8.38             31.26             78.85                      37.41   28.829 0.364213 0.017995 1.497832\n   145   0.8637  3 1  838.202     8.46             31.49             78.82                      37.41   28.877 0.242662 0.012261 1.045808\n   146   0.6210  3 1  838.823     8.52             31.66             78.80                      37.43   28.909 0.168629 0.008608 0.754724\n   147   1.3704  3    840.194     8.63             31.97             78.74                      37.42   28.923 0.346574 0.017566 1.678455\n   148   0.9541  3 1  841.148     8.70             32.17             78.70                      37.42   28.974 0.231115 0.011429 1.174406\n   149   2.0686  3    843.217     8.85             32.53             78.61                      37.45   28.993 0.459052 0.021095 2.575235\n   150   1.4106  3 1  844.627     8.94             32.76             78.56                      37.44   29.068 0.293781 0.012800 1.769909\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n   151   3.0325  4    847.660     9.11             33.21             78.47                      37.48   29.091 0.571990 0.022012 3.873385\n   152   2.0568  3 1  849.716     9.21             33.52             78.43                      37.47   29.197 0.356560 0.013148 2.656152\n   153   4.4124  3    854.129     9.42             34.28             78.45                      37.49   29.222 0.722749 0.022335 5.834266\n   154   8.9096  2    863.038     9.80             36.11             78.66                      37.47   29.273 2.198867 0.059538 11.400813\n   155  14.8820  3    877.920     9.10             35.49             79.60                      37.47   29.403 2.825593 0.117772 19.200708\n   156  19.4520  3    897.372     8.62             35.29             80.38                      37.47   29.576 5.650794 0.153645 15.321336\n   157  22.4216  3    919.794     8.10             35.31             81.34                      37.48   29.729 5.392311 0.136334 15.610681\n   158  27.4070  3    947.201     7.10             34.53             82.95                      37.50   29.851 4.931082 0.103796 21.805213\n   159  37.7960  4    984.997     6.40             35.21             84.62                      37.48   29.888 5.077980 0.176464 41.299094\n   160  40.5209  5   1025.518     6.02             35.69             85.57                      37.51   30.224 7.401063 0.162941 34.617892\n   161  45.3194  4   1070.837     5.07             34.40             87.16                      37.51   30.536 10.641106 0.210789 49.360820\n   162  24.1626  3   1095.000     3.77             32.77             89.68                      37.50   31.484 8.000326 0.153396 11.555049\n   163  27.8742  3   1122.874     4.42             35.34             88.89                      37.50   31.651 5.766486 0.085284 20.479621\n   164  41.4647  2   1164.339     3.31             34.29             91.19                      37.53   31.636 7.128059 0.046025 32.712668\n   165  51.6739  4   1216.013     2.99             34.62             92.06                      37.50   31.815 9.975867 0.193265 28.855933\n   166  52.6877  5   1268.701     2.41             33.94             93.37                      37.50   32.271 10.328890 0.158541 44.415304\n   167  56.2798  4   1324.980     1.68             33.85             95.28                      37.50   32.673 11.970452 0.156276 7.700787\n   168  64.3144  3   1389.295     1.86             34.11             94.82                      37.50   32.995 13.614599 0.080906 10.723215\n   169  97.4855  3   1486.780     1.24             33.44             96.43                      37.47   32.903 20.675703 0.054140 13.234878\n   170 167.1396  4   1653.920     0.88             30.44             97.18                      37.50   32.331 43.507919 0.108538 20.171564\n   171 226.2683  6   1880.188     0.98             28.40             96.68                      37.49   32.378 72.015719 0.212385 26.302637\n   172 218.5351  4   2098.723     0.95             28.34             96.74                      37.50   33.688 81.122126 0.114640 24.344475\n   173 289.0244  6   2387.748     0.81             26.67             97.05                      37.50   33.851 131.179292 0.122365 31.795538\n   174 359.7652  6   2747.513     0.38             24.20             98.46                      37.50   34.265 201.303954 0.086949 39.279794\n   175 358.4299  9   3105.943     0.13             17.39             99.28                      37.50   35.379 273.290133 0.111961 42.368556\n   176  10.9767  2 3 3116.919     0.12             16.62             99.26                      37.50   40.684 7.898596 0.005537 1.070395\n   177   8.1104  1 1 3125.030     0.12             18.43             99.35                      37.50   40.782 4.328067 0.004289 0.604137\n   178   6.1312  1 1 3131.161     0.12             19.03             99.39                      37.50   40.854 3.238906 0.002309 0.452519\n   179   4.6679  1 1 3135.829     0.11             19.33             99.41                      37.50   40.908 2.457600 0.001400 0.343937\n   180   3.5721  1 1 3139.401     0.11             19.49             99.42                      37.50   40.948 1.873258 0.000950 0.262296\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n   181   8.2321  6   3147.633     0.11             17.65             99.39                      37.50   40.923 1.919035 0.081179 2.575530\n   182   1.3848  6 2 3149.018     0.11             33.31             99.66                       1.75   41.017 3.796754 0.100525 1.901080\n   183   1.9347  2   3150.953     0.11             17.39             99.39                      31.55   41.021 1.854966 0.013847 0.252190\n   184   4.1327  2   3155.085     0.10             17.60             99.41                      31.54   41.011 0.057433 0.016144 0.347632\n   185   8.7060  2   3163.791     0.10             20.78             99.52                      31.54   40.998 0.156901 0.015484 0.649788\n   186  18.4132  2   3182.204     0.09             23.27             99.60                      31.49   40.979 0.124829 0.033535 1.125137\n   187  35.1137  2   3217.318     0.08             25.83             99.68                      31.05   40.999 0.147777 0.022538 1.644192\n   188  71.2296  2   3288.548     0.07             28.34             99.77                      30.48   41.057 0.176492 0.006003 3.200199\n   189 153.1341  3   3441.682     0.04             28.32             99.84                      28.65   41.193 0.558450 0.009140 6.438109\n   190 208.3182  3   3650.000     0.03             27.22             99.89                      27.02   42.160 0.550427 0.007453 6.941673\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                               1m 36.51s    99.86%\n|- Newton                              1m 35.89s    99.36%\n  |- Jacobian                          1m 21.67s    85.17%\n  |- Update                              11.875s    12.38%\n  |- Solver                               1.795s     1.87%\n  |- Residual                             0.200s     0.21%\n  |- Logging                              0.014s     0.01%\n|- Output                                 0.565s     0.59%\n|- Input                                  0.001s     0.00%\nInitialization                            0.132s     0.14%\n------------------------------------------------------------\nTOTAL                                  1m 36.64s\n============================================================\n\nTime steps : 190/263, step size: 19.21, 52.46\n')
```

#### Load CMG

### Load ECL

### Wells

![png]({{ "/assets/images/benchmark_image_54.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_55.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_56.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_57.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_58.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_59.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_60.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_61.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_62.png" | relative_url }})

### Block

#### Block Pressure


```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_63.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_64.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_65.png" | relative_url }})

#### Block Temperature

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_66.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_67.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_68.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_69.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_70.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_71.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_72.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_73.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_74.png" | relative_url }})

#### v.s. ECL

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_75.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_76.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_77.png" | relative_url }})

# Cyclic steam stimulation

## stspe001.dat Benchmark case in SPE4

Cyclic steam stimulation on radial grid

```
Running simulation: Cyclic steam stimulation in Radial grid

    80   0.7860  1   1095.000                                                                            2.703 5.544684 0.001009 0.070224



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  4.270s    95.20%

|- Newton                                 4.163s    97.50%

  |- Jacobian                             3.163s    75.99%

  |- Update                               0.927s    22.27%

  |- Residual                             0.024s     0.56%

  |- Solver                               0.019s     0.47%

  |- Logging                              0.003s     0.08%

|- Output                                 0.098s     2.30%

|- Input                                  0.000s     0.01%

Initialization                            0.216s     4.80%

------------------------------------------------------------

TOTAL                                     4.485s

============================================================



Time steps : 80/85, step size: 13.69, 24.36

```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//stspe001.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/stspe001.dat\n', stderr='[MacBook-Air.local:19405] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/85852160/sm_segment.MacBook-Air.501.51e0000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1   0.0200  1      0.020                                                                   86.35    0.000 38.437678 0.000127 9.923199\n     2   0.0348  1      0.055                                                                  113.45    0.000 41.853241 0.042020 22.990114\n     3   0.0592  1      0.114                                                                  260.07    0.007 30.346239 0.042901 40.500000\n     4   0.1015  8      0.215                                                                  783.84    0.007 123.461326 0.254414 207.288167\n     5   0.0833  4      0.299                                                                 1000.00    0.007 61.700608 0.090581 61.606961\n     6   0.1212  7      0.420                                                                 1000.84    0.008 71.867617 0.141723 110.371650\n     7   0.1427  3      0.563                                                                  999.77    0.009 91.945988 0.142364 46.309906\n     8   0.1709  3      0.734                                                                  999.99    0.011 70.151157 0.044474 69.792364\n     9   0.2456  3      0.979                                                                 1000.22    0.013 76.770296 0.046398 105.006938\n    10   0.2964  3      1.276                                                                 1000.95    0.016 59.803596 0.233301 57.558729\n    11   0.2706  2      1.546                                                                 1000.14    0.021 62.528595 0.084071 44.993461\n    12   0.4047  3      1.951                                                                 1000.61    0.026 86.028041 0.148753 55.914371\n    13   0.4741  3      2.425                                                                 1000.23    0.034 58.828384 0.087833 58.334718\n    14   0.6977  4      3.123                                                                  999.94    0.044 73.870665 0.172417 83.209564\n    15   0.7574  3      3.880                                                                  999.62    0.062 71.252161 0.102208 63.312542\n    16   1.0511  3      4.931                                                                 1000.30    0.085 67.475287 0.131271 83.317699\n    17   1.3079  4      6.239                                                                  999.96    0.119 80.451162 0.159967 107.144892\n    18   1.4768  5      7.716                                                                  999.14    0.165 73.013939 0.155354 74.825330\n    19   1.6927  3      9.409                                                                 1000.60    0.234 77.964916 0.130359 108.520725\n    20   0.5915  1     10.000                                                                  999.98    0.323 22.282214 0.062804 34.802533\n    21   0.9728  3     10.973                                                                            0.358 99.471752 0.025550 23.156089\n    22   1.2046  1     12.177                                                                            0.405 40.334601 0.029505 9.492903\n    23   2.0690  1     14.246                                                                            0.455 40.819320 0.040415 10.307955\n    24   2.7535  1     17.000                                                                            0.523 36.988411 0.052159 12.661329\n    25   4.7672  8     21.767   162.89            514.19             75.94                               0.602 235.833754 0.126229 106.794283\n    26   3.5925  1     25.360   128.86            333.20             72.11                               0.474 54.389200 0.025045 22.007220\n    27   5.6507  1     31.010    92.27            193.29             67.69                               0.392 49.492720 0.027103 20.199456\n    28   9.1566  3     40.167    60.43             99.81             62.29                               0.429 43.738537 0.033188 23.044950\n    29  15.3843  1     55.551    43.40             59.60             57.86                               0.384 37.699971 0.039197 20.049754\n    30  26.8867  4     82.438    27.31             30.68             52.90                               0.439 34.141787 0.089322 24.484269\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31  39.3208  3    121.759    20.58             17.57             46.06                               0.502 23.174227 0.090501 21.630967\n    32  57.2235  6    178.982    18.70             10.03             34.91                               0.569 14.137385 0.121926 18.759333\n    33  24.5511  5 1  203.534     7.80              4.68             37.49                               0.638 19.058470 0.013509 6.363896\n    34  48.9872  1    252.521    10.69              3.50             24.64                               0.665 3.815756 0.018092 9.030700\n    35  90.0000  1    342.521    10.87              2.76             20.28                               0.695 3.610377 0.009599 13.335430\n    36  22.4793  1    365.000    10.64              2.93             21.58                               0.764 0.839783 0.004595 3.264727\n    37   1.1111 12 2  366.111                                                                  999.16    0.781 173.988757 0.363130 182.501086\n    38   0.7579  3    366.869                                                                 1000.22    0.788 57.144249 0.157324 82.508821\n    39   0.8631  2    367.732                                                                 1000.26    0.811 41.506002 0.093206 79.873480\n    40   1.1778  5    368.910                                                                  999.96    0.805 62.211450 0.244603 95.544291\n    41   1.0446  2    369.955                                                                 1000.51    0.833 39.457173 0.085685 67.795424\n    42   1.5209  4    371.475                                                                 1000.13    0.840 52.966471 0.190896 76.227364\n    43   1.5615  3    373.037                                                                 1000.02    0.858 45.507916 0.077021 82.258560\n    44   1.9630  4    375.000                                                                 1000.14    0.870 53.694191 0.157778 74.996900\n    45   2.2323  3    377.232                                                                            0.907 89.422913 0.062822 24.843651\n    46   2.9020  1    380.134                                                                            0.937 34.908447 0.017439 10.443906\n    47   1.8657  1    382.000                                                                            0.982 15.705006 0.015803 5.594416\n    48   3.8200  7    385.820   125.25            562.95             81.80                               1.026 180.823745 0.181513 87.453512\n    49   3.4185  3    389.238   127.22            332.41             72.32                               1.081 46.456600 0.121570 26.617149\n    50   4.4058  1    393.644    98.05            210.66             68.24                               1.037 34.023295 0.022652 16.588578\n    51   7.8931  1    401.537    68.98            128.57             65.08                               0.988 35.657824 0.021509 17.573554\n    52  13.9847  1    415.522    43.95             73.78             62.67                               0.948 34.789266 0.035621 18.936438\n    53  24.9237  2    440.446    23.89             38.25             61.56                               1.046 30.870256 0.062303 28.327353\n    54  41.0889  4    481.535    15.08             20.41             57.51                               1.188 21.557822 0.099035 25.707893\n    55  57.7474  5    539.282    12.31             12.96             51.29                               1.345 12.072839 0.099221 18.264395\n    56  81.0991  5    620.381    11.91              8.32             41.11                               1.495 7.809656 0.154512 15.243827\n    57  90.0000  5    710.381    10.16              5.25             34.08                               1.639 4.975223 0.152203 11.952736\n    58  19.6188  4    730.000     5.44              2.93             34.97                               1.761 6.961983 0.139282 2.322077\n    59   1.1111  9 2  731.111                                                                  999.71    1.781 146.346931 0.345340 157.549479\n    60   0.7851  4    731.896                                                                  999.99    1.776 61.455229 0.161277 63.358469\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    61   0.8828  2    732.779                                                                 1000.23    1.799 35.932577 0.121739 67.032502\n    62   1.1370  4    733.916                                                                 1000.05    1.794 44.237741 0.184409 76.644722\n    63   1.1900  3    735.106                                                                  999.16    1.793 40.503933 0.158296 59.421397\n    64   1.3510  2    736.457                                                                  999.88    1.824 36.945573 0.097691 63.911294\n    65   1.9090  4    738.366                                                                 1000.30    1.809 48.808464 0.162539 74.522235\n    66   1.6340  3    740.000                                                                 1000.01    1.819 39.578217 0.135062 66.261545\n    67   2.0063  3    742.006                                                                            1.843 80.516589 0.058369 24.438357\n    68   2.7285  1    744.735                                                                            1.863 30.191123 0.018492 9.788840\n    69   2.2652  2    747.000                                                                            1.898 15.492789 0.142512 12.496776\n    70   2.7104  6    749.710   106.02            639.15             85.77                               1.949 159.089705 0.092875 78.785906\n    71   2.6197  2    752.330   106.62            380.91             78.13                               1.974 41.878069 0.039806 23.064028\n    72   4.4545  1    756.785    83.87            236.11             73.79                               1.875 35.549277 0.023630 17.317349\n    73   7.8981  2    764.683    60.32            135.19             69.15                               1.911 36.403982 0.027157 21.540834\n    74  13.9233  1    778.606    40.11             77.48             65.89                               1.839 33.717702 0.018950 17.050605\n    75  24.9961  1    803.602    25.53             43.38             62.95                               1.795 27.876924 0.021887 19.094494\n    76  46.7419  5    850.344    14.41             22.14             60.58                               1.946 19.973722 0.094994 24.813285\n    77  66.7756  6    917.120    10.79             13.35             55.31                               2.143 11.078126 0.118347 17.625682\n    78  87.0943  3   1004.214    10.41              8.73             45.59                               2.345 6.981908 0.188470 14.718727\n    79  90.0000  5   1094.214     8.43              5.71             40.39                               2.542 4.262629 0.150435 10.370215\n    80   0.7860  1   1095.000                                                                            2.703 5.544684 0.001009 0.070224\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                  4.270s    95.20%\n|- Newton                                 4.163s    97.50%\n  |- Jacobian                             3.163s    75.99%\n  |- Update                               0.927s    22.27%\n  |- Residual                             0.024s     0.56%\n  |- Solver                               0.019s     0.47%\n  |- Logging                              0.003s     0.08%\n|- Output                                 0.098s     2.30%\n|- Input                                  0.000s     0.01%\nInitialization                            0.216s     4.80%\n------------------------------------------------------------\nTOTAL                                     4.485s\n============================================================\n\nTime steps : 80/85, step size: 13.69, 24.36\n')
```

![png]({{ "/assets/images/benchmark_image_78.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_79.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_80.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_81.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_82.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_83.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_84.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_85.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_86.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_87.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_88.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_89.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_90.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_91.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_92.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_93.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_94.png" | relative_url }})



## stflu008.dat

Cyclic steam stimulation on cartesian grid


```
Running simulation: Cyclic steam stimulation in Cartesian

   171  31.0080  3   1095.000     9.46              7.85             45.33                               7.106 2.553129 0.065061 3.867607



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                               3m 21.23s    99.94%

|- Newton                              3m 18.91s    98.85%

  |- Jacobian                          2m 37.62s    79.24%

  |- Update                              38.387s    19.30%

  |- Solver                               1.281s     0.64%

  |- Residual                             0.789s     0.40%

  |- Logging                              0.014s     0.01%

|- Output                                 2.276s     1.13%

|- Input                                  0.002s     0.00%

Initialization                            0.128s     0.06%

------------------------------------------------------------

TOTAL                                  3m 21.36s

============================================================



Time steps : 171/189, step size: 6.40, 16.26

```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//stflu008.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/stflu008.dat\n', stderr='[MacBook-Air.local:19434] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/2694774784/sm_segment.MacBook-Air.501.a09f0000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1   0.0200  1      0.020                                                                   85.03    0.001 54.389200 0.000320 14.628505\n     2   0.0233  1      0.043                                                                  128.28    0.003 54.389200 0.049426 28.023317\n     3   0.0272  2      0.071                                                                  318.35    0.008 38.055378 0.073814 81.000000\n     4   0.0212  8      0.092                                                                 1000.00    0.008 184.837295 0.215796 186.631829\n     5 8.81e-03  3      0.101                                                                 1000.04    0.008 32.527011 0.074976 20.857273\n     6   0.0129  2      0.113                                                                  999.25    0.008 46.697326 0.032837 34.159003\n     7   0.0161  2      0.130                                                                  999.85    0.008 38.660892 0.042468 64.553595\n     8   0.0145  3      0.144                                                                 1000.00    0.009 42.280643 0.041324 80.010431\n     9   0.0114  2      0.155                                                                  999.99    0.009 72.284847 0.151674 24.073838\n    10   0.0114  1      0.167                                                                 1000.38    0.009 33.361781 0.080075 17.730934\n    11   0.0165  1      0.183                                                                  999.83    0.009 22.169960 0.035604 24.073533\n    12   0.0242  1      0.208                                                                  999.38    0.009 43.572144 0.028836 31.043922\n    13   0.0313  2      0.239                                                                 1000.00    0.009 49.327784 0.027429 39.049622\n    14   0.0372  2      0.276                                                                 1000.02    0.010 42.084303 0.090911 65.522046\n    15   0.0331  2      0.309                                                                  999.98    0.010 36.277566 0.088664 79.272344\n    16   0.0261  3      0.335                                                                 1000.09    0.011 75.742081 0.153933 28.354733\n    17   0.0255  2      0.361                                                                  999.97    0.011 31.267843 0.088294 24.373067\n    18   0.0371  1      0.398                                                                  999.38    0.012 39.102126 0.044546 29.180443\n    19   0.0504  2      0.448                                                                  999.84    0.012 54.935350 0.027758 33.627528\n    20   0.0585  3      0.507                                                                 1000.08    0.013 48.810410 0.023614 35.613833\n    21   0.0719  2      0.579                                                                 1000.06    0.014 48.612403 0.138438 39.292595\n    22   0.0851  2      0.664                                                                  999.97    0.015 35.473228 0.073921 41.809384\n    23   0.0978  1      0.762                                                                 1000.47    0.024 34.961889 0.029838 40.500000\n    24   0.1140  1      0.876                                                                  999.75    0.028 36.614864 0.023412 40.500000\n    25   0.1331  3      1.009                                                                 1000.01    0.031 61.435141 0.193053 46.429510\n    26   0.1357  2      1.144                                                                  999.96    0.034 41.451849 0.144094 38.580020\n    27   0.1616  1      1.306                                                                  999.79    0.045 39.167327 0.058232 40.500000\n    28   0.1885  1      1.494                                                                 1000.47    0.082 30.406717 0.026817 40.500000\n    29   0.2199  1      1.714                                                                 1000.51    0.153 24.166912 0.016883 40.500000\n    30   0.2565  3      1.971                                                                  999.99    0.159 53.853620 0.235007 45.813608\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31   0.2332  3      2.204                                                                  999.97    0.167 36.411899 0.088264 36.365400\n    32   0.2867  2      2.491                                                                  999.99    0.175 36.711831 0.041263 39.712373\n    33   0.3378  2      2.829                                                                 1000.00    0.187 33.174835 0.085255 43.503209\n    34   0.3800  2      3.209                                                                  999.98    0.201 32.962160 0.064519 47.509846\n    35   0.4080  5      3.617                                                                 1000.00    0.217 29.842083 0.121037 50.294920\n    36   0.4247  4      4.041                                                                  999.99    0.235 36.075168 0.165907 47.177688\n    37   0.4577  2      4.499                                                                  999.99    0.257 28.560822 0.075284 40.736209\n    38   0.1775  2 1    4.676                                                                  999.99    0.282 22.247296 0.082318 17.128070\n    39   0.0891  2 1    4.766                                                                  999.96    0.294 6.736927 0.049400 8.455360\n    40   0.1564  2      4.922                                                                  999.99    0.300 9.091679 0.029265 14.712981\n    41   0.2678  2      5.190                                                                  999.92    0.311 14.236731 0.026388 23.319804\n    42   0.3965  2      5.586                                                                 1000.01    0.356 18.644975 0.024759 29.153644\n    43   0.0598  2 2    5.646                                                                 1000.16    0.396 3.579723 0.004003 3.969706\n    44   0.1270  2      5.773                                                                 1000.00    0.421 5.259646 0.005419 8.929428\n    45   0.0809  2 1    5.854                                                                 1000.07    0.449 3.141201 0.004746 5.352505\n    46   0.1668  2      6.021                                                                 1000.00    0.486 6.307894 0.006361 10.696902\n    47   0.1026  2 1    6.123                                                                 1000.04    0.522 3.714675 0.005968 6.343085\n    48   0.0690  2 1    6.192                                                                 1000.05    0.545 2.539804 0.002284 4.362273\n    49   0.1454  2      6.338                                                                  999.99    0.577 5.309161 0.007762 9.002961\n    50   0.0925  2 1    6.430                                                                 1000.03    0.603 3.430707 0.002973 5.806325\n    51   0.1888  2      6.619                                                                  999.98    0.652 6.446224 0.007736 10.718907\n    52   0.1161  2 1    6.735                                                                  999.92    0.691 9.781262 0.040475 6.909474\n    53   0.2134  4      6.949                                                                  999.88    0.720 7.838923 0.058362 14.116391\n    54   0.1195  2 1    7.068                                                                  999.94    0.769 3.641899 0.022928 6.532383\n    55   0.2400  4      7.308                                                                  999.97    0.802 25.201159 0.111788 18.773891\n    56   0.3209 13      7.629                                                                 1000.00    0.816 20.160163 0.228937 38.084354\n    57   0.2962  1      7.925                                                                 1000.01    0.840 10.243623 0.027683 18.716388\n    58   0.4727  1      8.398                                                                 1000.03    0.863 15.432445 0.022453 28.806713\n    59   0.6446  2      9.043                                                                 1000.03    0.893 37.521590 0.155060 46.946299\n    60   0.2322  1 1    9.275                                                                 1000.01    0.945 8.005220 0.063475 13.813138\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    61   0.3807  1      9.655                                                                 1000.04    0.964 13.463820 0.042540 21.041205\n    62   0.3445  2     10.000                                                                 1000.01    0.996 11.718178 0.021048 17.047193\n    63   0.5657  4     10.566                                                                            1.026 126.373661 0.076684 30.517372\n    64   0.3972  4     10.963                                                                            1.070 27.168736 0.079875 7.110926\n    65   0.6047  9     11.568                                                                            1.100 30.580008 0.182085 28.302772\n    66   0.6374  1     12.205                                                                            1.140 21.453162 0.039950 9.036397\n    67   1.0665  2     13.271                                                                            1.179 28.608799 0.125703 14.771173\n    68   1.3539  2     14.625                                                                            1.236 27.180250 0.096322 16.453802\n    69   1.9238  1     16.549                                                                            1.299 28.118637 0.056008 21.379346\n    70   0.4508  2     17.000                                                                            1.374 6.789131 0.111820 5.742883\n    71   0.6027  7     17.603    74.26            792.07             91.43                               1.399 165.427944 0.099143 81.512005\n    72   0.3479  2     17.951    95.87            674.64             87.56                               1.417 24.393877 0.197030 16.435599\n    73   0.3509  1     18.302   106.24            530.83             83.32                               1.423 18.547515 0.035008 8.008990\n    74   0.6106  2     18.912   108.42            401.38             78.73                               1.437 22.161419 0.110905 10.523322\n    75   0.8191  1     19.731   104.29            319.69             75.40                               1.445 22.279962 0.030056 10.454627\n    76   1.3559  1     21.087    95.14            251.99             72.59                               1.451 27.032330 0.111645 11.839572\n    77   1.8137  6     22.901    84.61            198.97             70.16                               1.483 27.841835 0.051917 14.242656\n    78   2.7991  2     25.700    70.87            152.61             68.29                               1.518 29.658775 0.078488 16.389451\n    79   4.2265  3     29.927    59.10            114.67             65.99                               1.562 33.277013 0.062876 18.446818\n    80   6.1185  3     36.045    50.43             84.55             62.64                               1.612 31.679183 0.091864 19.334696\n    81   8.8540  4     44.899    42.52             60.72             58.82                               1.671 27.025306 0.099258 19.663263\n    82  12.4325  3     57.332    34.84             43.14             55.32                               1.739 22.777373 0.078623 19.095168\n    83  19.0331  5     76.365    30.71             30.29             49.66                               1.817 19.721464 0.090835 19.328009\n    84  27.6603  6    104.025    27.25             20.88             43.38                               1.908 15.326249 0.086173 18.436711\n    85  40.9916  5    145.017    24.39             13.60             35.80                               2.007 11.493202 0.064580 17.136450\n    86  66.8610  5    211.878    20.60              8.13             28.30                               2.115 9.655209 0.080755 17.504391\n    87  30.0001  9 1  241.878    11.97              4.69             28.16                               2.231 19.020027 0.006392 6.490603\n    88  40.0001  1    281.878    12.56              3.83             23.36                               2.276 3.611490 0.006505 6.643985\n    89  80.1801  1    362.058    11.30              3.12             21.66                               2.312 5.709488 0.007269 10.757929\n    90   2.9423  1    365.000    11.19              3.15             21.98                               2.412 0.209803 0.000856 0.411261\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    91   0.2517 11 3  365.252                                                                  999.77    2.411 208.812352 0.356281 195.592346\n    92   0.1008  2    365.352                                                                  999.97    2.411 47.103574 0.142185 42.386105\n    93   0.1149  2    365.467                                                                  999.99    2.410 22.462013 0.071484 43.355165\n    94   0.1295  2    365.597                                                                  999.97    2.409 36.486909 0.123000 46.535064\n    95   0.1406  1    365.737                                                                  999.99    2.417 16.370327 0.066233 40.348157\n    96   0.1643  2    365.902                                                                 1000.18    2.420 50.736858 0.213013 42.739946\n    97   0.1584  1    366.060                                                                  999.96    2.429 17.049921 0.050075 33.503694\n    98   0.2023  1    366.262                                                                  999.95    2.440 18.486713 0.035788 37.393749\n    99   0.2454  3    366.508                                                                 1000.01    2.437 52.901672 0.228689 42.454442\n   100   0.2268  2    366.735                                                                 1000.00    2.435 17.591273 0.063993 34.754250\n   101   0.2848  1    367.019                                                                  999.95    2.452 18.244162 0.033303 34.079968\n   102   0.3609  5    367.380                                                                 1000.00    2.444 36.119046 0.184920 37.206076\n   103   0.3771  2    367.757                                                                 1000.19    2.442 38.947306 0.161690 36.466000\n   104   0.4235  1    368.181                                                                 1000.10    2.469 22.701061 0.066613 39.240976\n   105   0.5019  1    368.683                                                                 1000.12    2.545 21.650799 0.025848 40.500000\n   106   0.5855  1    369.268                                                                  999.97    2.689 19.480487 0.019319 40.500000\n   107   0.6831  4    369.951                                                                 1000.03    2.681 34.439143 0.178486 56.578634\n   108   0.6649  8    370.616                                                                  999.98    2.683 24.861777 0.209111 45.687904\n   109   0.6481  6    371.264                                                                  999.99    2.680 22.241991 0.142037 33.629272\n   110   0.7767  9    372.041                                                                 1000.00    2.671 24.024092 0.234133 45.227762\n   111   0.7077  2    372.749                                                                 1000.00    2.675 20.337164 0.097660 38.500371\n   112   0.8465  1    373.595                                                                 1000.00    2.735 22.369649 0.035722 39.606403\n   113   0.9986  1    374.594                                                                  999.94    2.808 23.269821 0.025439 40.029550\n   114   0.4061  3    375.000                                                                  999.97    2.833 44.958309 0.186863 21.601371\n   115   0.4220  3    375.422                                                                            2.844 91.878350 0.066499 24.347135\n   116   0.3661  1    375.788                                                                            2.858 19.046136 0.028499 5.242349\n   117   0.6327  1    376.421                                                                            2.870 20.658444 0.022097 6.049905\n   118   1.0700  1    377.491                                                                            2.888 23.364133 0.017450 7.204597\n   119   1.7464  1    379.237                                                                            2.915 24.940056 0.016809 8.175923\n   120   2.7628  1    382.000                                                                            2.955 26.472733 0.018536 9.269741\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n   121   4.3361  8    386.336    59.55            324.72             84.50                               3.036 173.177327 0.158538 99.621719\n   122   2.4181  3    388.754    68.03            242.43             78.09                               3.134 30.468787 0.035771 22.947741\n   123   3.6016  2    392.356    60.18            165.97             73.39                               3.190 29.187109 0.032368 15.941122\n   124   5.4689  2    397.825    49.19            114.68             69.98                               3.263 29.622981 0.048078 18.781756\n   125   8.2613  2    406.086    37.62             77.96             67.45                               3.366 26.774269 0.076781 20.953708\n   126  12.7037  2    418.790    28.73             54.66             65.55                               3.490 24.493082 0.048641 22.238616\n   127  19.1350  6    437.925    20.40             37.41             64.71                               3.660 20.202283 0.108331 22.905344\n   128  25.9251  5    463.850    16.99             28.10             62.32                               3.858 14.748696 0.161980 19.587654\n   129  29.0844  7    492.934    15.48             21.93             58.63                               4.063 9.738187 0.079282 14.230223\n   130  44.3975  5    537.332    15.15             15.79             51.03                               4.249 8.701633 0.121352 13.748453\n   131  57.2656  4    594.597    14.40             11.44             44.27                               4.452 7.469555 0.136736 12.702890\n   132  69.9005  6    664.498    13.68              8.28             37.70                               4.645 7.113228 0.109606 11.048263\n   133  65.5023 11    730.000     9.70              5.34             35.53                               4.816 9.215428 0.077052 7.793723\n   134   0.3704 11 3  730.370                                                                 1000.01    4.928 196.523349 0.348595 176.853952\n   135   0.1610  2    730.531                                                                 1000.02    4.927 45.058554 0.133938 55.705956\n   136   0.1582  2    730.690                                                                  999.99    4.924 48.274683 0.183292 38.006618\n   137   0.1661  1    730.856                                                                  999.96    4.932 15.572728 0.069358 36.912134\n   138   0.2028  4    731.058                                                                  999.99    4.923 41.546252 0.164689 29.993794\n   139   0.2255  1    731.284                                                                  999.97    4.937 16.292646 0.080324 29.795760\n   140   0.3032  2    731.587                                                                  999.99    4.928 17.270921 0.157993 43.851766\n   141   0.3396  1    731.927                                                                  999.95    4.948 16.121573 0.060839 37.040215\n   142   0.4139  2    732.341                                                                 1000.06    4.949 51.645518 0.193972 40.313224\n   143   0.4212  2    732.762                                                                 1000.00    4.938 19.275213 0.085347 44.463193\n   144   0.4685  1    733.230                                                                 1000.09    4.969 18.096572 0.034972 40.500000\n   145   0.5465  3    733.777                                                                 1000.02    4.948 37.537421 0.170265 50.049274\n   146   0.5704  4    734.347                                                                 1000.00    4.926 23.372553 0.156909 39.051338\n   147   0.6505  1    734.998                                                                 1000.04    4.968 19.433890 0.102337 34.847076\n   148   0.8158  2    735.814                                                                 1000.04    5.011 21.417487 0.212417 43.863842\n   149   0.7879  2    736.601                                                                 1000.05    5.038 30.650367 0.208078 45.370386\n   150   0.7701  2    737.372                                                                 1000.00    5.025 23.729291 0.145464 42.426232\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n   151   0.8776  3    738.249                                                                 1000.04    5.002 20.191940 0.125444 45.990056\n   152   0.9588  1    739.208                                                                  999.91    5.073 20.641554 0.086524 37.518858\n   153   0.7920  2    740.000                                                                 1000.04    5.104 31.941190 0.210459 33.213425\n   154   0.7691  3    740.769                                                                            5.120 105.817357 0.064488 30.578164\n   155   0.6092  1    741.378                                                                            5.138 16.726727 0.023803 5.243424\n   156   1.0872  1    742.465                                                                            5.153 19.075087 0.023925 6.369905\n   157   1.8780  1    744.343                                                                            5.175 22.477067 0.023134 7.711066\n   158   2.6565  1    747.000                                                                            5.207 21.903501 0.020027 8.124001\n   159   4.4190 11    751.419    34.78            286.05             89.16                               5.330 159.977647 0.313024 96.990180\n   160   2.6161  2    754.035    46.49            206.69             81.64                               5.411 27.967585 0.140470 23.460155\n   161   3.1523  5    757.187    46.48            150.92             76.45                               5.474 23.032244 0.143893 12.527149\n   162   3.7541  1    760.941    42.51            119.39             73.74                               5.477 18.222918 0.019554 9.398636\n   163   6.5612  3    767.503    35.77             89.47             71.44                               5.546 22.307368 0.113230 15.088079\n   164   8.7240  1    776.227    29.45             67.56             69.64                               5.572 18.305630 0.036106 12.078511\n   165  15.2301  3    791.457    22.59             46.39             67.25                               5.695 18.411559 0.058392 20.425490\n   166  23.6230  1    815.080    18.38             34.19             65.04                               5.751 15.788885 0.042288 17.103182\n   167  38.7543  8    853.834    13.99             22.98             62.16                               5.982 13.360617 0.097656 23.098987\n   168  54.7695  7    908.604    11.83             16.68             58.50                               6.266 10.210954 0.143161 17.973838\n   169  65.3885  3    973.992    11.33             12.18             51.80                               6.559 7.841494 0.101120 13.035412\n   170  90.0000  5   1063.992     9.91              8.51             46.18                               6.838 8.032944 0.118746 12.652846\n   171  31.0080  3   1095.000     9.46              7.85             45.33                               7.106 2.553129 0.065061 3.867607\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                               3m 21.23s    99.94%\n|- Newton                              3m 18.91s    98.85%\n  |- Jacobian                          2m 37.62s    79.24%\n  |- Update                              38.387s    19.30%\n  |- Solver                               1.281s     0.64%\n  |- Residual                             0.789s     0.40%\n  |- Logging                              0.014s     0.01%\n|- Output                                 2.276s     1.13%\n|- Input                                  0.002s     0.00%\nInitialization                            0.128s     0.06%\n------------------------------------------------------------\nTOTAL                                  3m 21.36s\n============================================================\n\nTime steps : 171/189, step size: 6.40, 16.26\n')
```

![png]({{ "/assets/images/benchmark_image_95.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_96.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_97.png" | relative_url }})



## stflu009.dat

Cyclic steam stimulation on pebi grid


```
Running simulation: Cyclic steam stimulation in Pebi-grid

    62  11.6538  1   1095.000     5.97              7.33             55.13                               0.904 1.263891 0.004623 1.268033



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                 57.407s    99.63%

|- Newton                                56.653s    98.69%

  |- Jacobian                            44.519s    78.58%

  |- Update                              11.295s    19.94%

  |- Solver                               0.410s     0.72%

  |- Residual                             0.209s     0.37%

  |- Logging                              0.011s     0.02%

|- Output                                 0.716s     1.25%

|- Input                                  0.003s     0.00%

Initialization                            0.215s     0.37%

------------------------------------------------------------

TOTAL                                    57.622s

============================================================



Time steps : 62/62, step size: 17.66, 26.56

```

```
CompletedProcess(args=['build/bin/simuapp', '-f', '/Users/mark/Documents/workspace/hatch/app/build/test/data//stflu009.dat'], returncode=0, stdout='/Users/mark/Documents/workspace/hatch/app/build/test/data/stflu009.dat\n', stderr='[MacBook-Air.local:20235] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/4190175232/sm_segment.MacBook-Air.501.f9c10000.0 could be created.\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n     1   0.0200  1      0.020                                                                   89.33    0.000 1.173972 0.000000 0.242617\n     2   0.0457  1      0.066                                                                   89.81    0.000 2.664440 0.000646 0.547542\n     3   0.1016  1      0.167                                                                   91.00    0.000 5.863350 0.001490 1.231681\n     4   0.2140  1      0.381                                                                   93.77    0.000 12.066629 0.003387 2.681347\n     5   0.4087  1      0.790                                                                  100.18    0.000 22.225737 0.007482 5.507838\n     6   0.6770  1      1.467                                                                  114.86    0.000 34.523631 0.015868 10.601392\n     7   0.9663  1      2.433                                                                  164.76    0.001 34.769652 0.030323 22.598447\n     8   1.3754  1      3.809                                                                  382.32    0.159 36.761993 0.030083 40.500000\n     9   1.6047  5      5.413                                                                  898.82    0.063 129.632989 0.104630 192.735977\n    10   0.6502  4      6.064                                                                 1000.01    0.074 112.168665 0.180264 47.312181\n    11   0.4954  1      6.559                                                                 1000.40    0.085 40.879198 0.079374 17.125729\n    12   0.6599  2      7.219                                                                  999.77    0.093 46.884245 0.037241 26.811020\n    13   0.8269  1      8.046                                                                  999.87    0.108 53.764373 0.025940 32.592270\n    14   0.9703  1      9.016                                                                 1000.43    0.127 41.791633 0.021216 30.729456\n    15   0.9839  1     10.000                                                                  999.57    0.153 33.233864 0.018920 26.404230\n    16   1.3897  2     11.390                                                                            0.176 86.100748 0.016697 25.944832\n    17   1.2553  1     12.645                                                                            0.201 30.015075 0.004169 10.708232\n    18   1.8875  1     14.533                                                                            0.220 25.293061 0.012023 9.988911\n    19   2.4675  1     17.000                                                                            0.241 22.073520 0.020999 9.195247\n    20   4.0954  5     21.095   103.15            245.69             70.43                               0.262 157.649705 0.087698 87.822774\n    21   2.4511  1     23.547    74.20            151.23             67.09                               0.252 31.013510 0.033137 14.619210\n    22   3.6424  1     27.189    56.09             96.61             63.27                               0.243 26.441217 0.034590 10.901095\n    23   5.7187  1     32.908    44.71             66.33             59.74                               0.242 27.134996 0.039788 8.325716\n    24   8.9023  1     41.810    36.37             46.69             56.21                               0.246 24.487935 0.043253 8.549667\n    25  14.3233  1     56.133    29.14             32.72             52.89                               0.244 23.970361 0.050436 10.065471\n    26  23.1974  4     79.331    22.86             21.02             47.91                               0.265 21.753178 0.057863 13.407688\n    27  38.6636  1    117.994    21.06             12.95             38.09                               0.271 17.228823 0.021254 12.401044\n    28  68.5125  1    186.507    17.85              7.32             29.07                               0.272 13.541900 0.016608 13.657323\n    29  90.0000  1    276.507    14.80              4.30             22.50                               0.281 10.111261 0.009993 12.423218\n    30  88.4933  1    365.000    12.72              3.54             21.80                               0.295 6.952839 0.008151 10.459411\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    31  10.0000 12    375.000                                                                 1000.00    0.306 251.565046 0.346613 226.976347\n    32   3.5330  2    378.533                                                                            0.387 94.510082 0.097710 35.417960\n    33   3.0112  1    381.544                                                                            0.413 16.360065 0.059429 7.151572\n    34   0.4558  1    382.000                                                                            0.437 3.173738 0.008470 1.689586\n    35   1.0048  2    383.005   216.58            706.27             76.53                               0.355 98.660417 0.072850 40.566635\n    36   0.8332  1    383.838   201.49            484.31             70.62                               0.334 23.186003 0.056645 15.121151\n    37   1.3630  1    385.201   192.13            345.13             64.24                               0.318 25.823517 0.074118 14.615048\n    38   2.1286  1    387.330   154.82            239.08             60.70                               0.312 23.743985 0.058288 14.686684\n    39   3.4573  1    390.787   130.50            177.94             57.69                               0.302 23.079140 0.100871 15.969831\n    40   4.8235  1    395.610    95.12            116.41             55.03                               0.299 20.029453 0.050315 14.920158\n    41   8.2248  1    403.835    63.75             72.99             53.38                               0.290 21.950626 0.020458 16.358049\n    42  13.6699  1    417.505    41.68             45.70             52.30                               0.282 24.312864 0.035953 17.124505\n    43  22.0428  1    439.548    26.68             28.40             51.56                               0.281 21.585186 0.066486 17.263865\n    44  35.6374  3    475.185    13.62             16.41             54.65                               0.353 19.360220 0.104754 25.456784\n    45  48.9613  4    524.147    10.03             14.72             59.48                               0.424 13.303897 0.126440 20.103713\n    46  61.9898  2    586.136     9.84              9.25             48.46                               0.495 10.643755 0.164179 13.182821\n    47  69.0575  1    655.194    11.49              8.63             42.88                               0.540 7.358488 0.024197 10.208694\n    48  74.8062  1    730.000    11.09              6.21             35.90                               0.577 5.105536 0.012437 9.065569\n    49  10.0000 12    740.000                                                                  999.99    0.591 235.883997 0.330023 197.622345\n    50   3.9685  2    743.969                                                                            0.653 77.964828 0.148685 30.821715\n    51   3.0315  1    747.000                                                                            0.673 17.434407 0.044713 8.537593\n    52   5.3564  5    752.356   180.38            322.05             64.10                               0.680 94.191021 0.163872 62.362985\n    53   4.5751  2    756.932   125.59            192.74             60.55                               0.702 29.351207 0.087578 20.335639\n    54   6.7401  1    763.672    82.08            116.36             58.64                               0.662 22.960001 0.087550 16.397056\n    55   9.9306  1    773.602    57.83             75.34             56.58                               0.633 22.617041 0.081600 14.677597\n    56  15.0074  1    788.610    38.90             48.79             55.64                               0.608 19.788086 0.049700 14.876244\n    57  25.6103  1    814.220    25.22             30.84             55.01                               0.585 20.386117 0.056237 15.451820\n    58  43.2546  1    857.475    16.10             18.83             53.90                               0.570 16.833114 0.098732 18.093427\n    59  60.8651  3    918.340     8.14             10.13             55.44                               0.664 15.189136 0.118929 20.888110\n    60  79.2135  6    997.553     6.92              9.25             57.22                               0.757 11.511734 0.173159 15.853675\n\n=========================================================================================================================================\n------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----\n                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   \n        Size       U                                       ft3      Cut                                 err                              \n No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  \n------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------\n    61  85.7929  3   1083.346     5.40              7.17             57.01                               0.831 12.285752 0.079217 10.310655\n    62  11.6538  1   1095.000     5.97              7.33             55.13                               0.904 1.263891 0.004623 1.268033\n\n============================================================\n                WALL-TIME PERFORMANCE REPORT                \n============================================================\nCategory                              Total Time   % Total\n------------------------------------------------------------\nTimeloop                                 57.407s    99.63%\n|- Newton                                56.653s    98.69%\n  |- Jacobian                            44.519s    78.58%\n  |- Update                              11.295s    19.94%\n  |- Solver                               0.410s     0.72%\n  |- Residual                             0.209s     0.37%\n  |- Logging                              0.011s     0.02%\n|- Output                                 0.716s     1.25%\n|- Input                                  0.003s     0.00%\nInitialization                            0.215s     0.37%\n------------------------------------------------------------\nTOTAL                                    57.622s\n============================================================\n\nTime steps : 62/62, step size: 17.66, 26.56\n')
```

![png]({{ "/assets/images/benchmark_image_98.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_99.png" | relative_url }})

```
Script completed at: 2026-02-28 20:31:33

```
