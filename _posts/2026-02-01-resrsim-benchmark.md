---
layout: default
title: "Benchmark results of resrsim"
date: 2026-02-01
---

# Setup

1. select kernel before executing current jupyter book

2. Install `ipykernel` package. For a virtual environment, open a terminal, and active the environment. 



    ```bash

    python -m venv .venv

    source .venv/bin/activate

    ```



3. Run `which python` to make sure the right virtual environment activated

4. Install requirments by `pip install -r requirements.txt`

4. Install by `python -m pip install ipykernel -U --force-reinstall`. 

5. install dependent packages `python -m pip install pandas numpy matplotlib trame trame-vtk trame-vuetify vtk`

The following is optional:

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



3. `pip install jupyter` if needs

```
Current OS: Darwin

simuexe path: build/bin/simuapp

```

# 3D



```

python -m pip install --upgrade pip

python -m pip install pyvista

```

In Jupyter Notebook, `pyvista.set_jupyter_backend("trame")` must install trame by `pip install trame trame-vtk trame-vuetify`

![png]({{ "/assets/images/benchmark_image_1.png" | relative_url }})

```
[MacBook-Air.local:24992] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/2692874240/sm_segment.MacBook-Air.501.a0820000.0 could be created.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                       ft3      Cut                                 err                              

 No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   1.0000  6      1.000   440.56             12.88              2.84                      49.82    0.000 2.42e+03 6.71e-08 2.41e-05

     2   0.1360  6      1.136   440.56             12.88              2.84                      49.82    0.000   0.0049 1.08e-08 3.91e-06

     3   0.2720  6      1.408   440.56             12.88              2.84                      49.82    0.000   0.0098 2.16e-08 7.80e-06

     4   0.5441  6      1.952   440.56             12.88              2.84                      49.82    0.000   0.0195 4.30e-08 1.55e-05

     5   1.0882  6      3.040   440.56             12.88              2.84                      49.82    0.000   0.0385 8.50e-08 3.06e-05

     6   2.1764  6      5.217   440.56             12.88              2.84                      49.82    0.000   0.0736 1.63e-07 5.81e-05

     7   4.3528  6      9.570   440.56             12.88              2.84                      49.82    0.000   0.1291 2.86e-07 1.01e-04

     8   8.7055  6     18.275   440.56             12.88              2.84                      49.82    0.000   0.2075 4.60e-07 1.59e-04

     9  17.4111  6     35.686   440.56             12.88              2.84                      49.82    0.000   0.2984 6.63e-07 2.21e-04

    10  34.8222  6     70.508   440.56             12.88              2.84                      49.82    0.001   0.3837 8.58e-07 2.64e-04

    11  69.6443  6    140.153   440.56             12.88              2.84                      49.82    0.001   0.4509 1.02e-06 2.73e-04

    12 139.2887  6    279.441   440.56             12.88              2.84                      49.82    0.002   0.5000 1.15e-06 2.44e-04

    13 278.5774  6    558.019   440.55             12.88              2.84                      49.82    0.005   0.5387 1.28e-06 2.10e-04

    14  36.9813  6    595.000   440.55             12.88              2.84                      49.82    0.005   0.3899 8.72e-07 2.66e-04

    15  73.9626  6    668.963   440.55             12.88              2.84                      49.82    0.005   0.4554 1.03e-06 2.72e-04

    16 147.9252  6    816.888   440.55             12.88              2.84                      49.82    0.007   0.5031 1.16e-06 2.39e-04

    17 278.1122  6   1095.000   440.54             12.88              2.84                      49.82    0.009   0.5381 1.28e-06 2.10e-04

    18 365.0000  6   1460.000   440.54             12.88              2.84                      49.82    0.012   0.5512 1.33e-06 2.43e-04

    19 135.0000  6   1595.000   440.54             12.88              2.84                      49.82    0.013   0.4972 1.14e-06 2.45e-04

    20 270.0000  6   1865.000   440.53             12.88              2.84                      49.82    0.015   0.5362 1.27e-06 2.06e-04

    21 230.0000  6   2095.000   440.53             12.88              2.84                      49.82    0.017   0.5261 1.24e-06 2.01e-04

    22 365.0000  6   2460.000   440.53             12.88              2.84                      49.82    0.020   0.5506 1.32e-06 2.43e-04

    23 135.0000  6   2595.000   440.52             12.88              2.84                      49.82    0.021   0.4966 1.14e-06 2.45e-04

    24 270.0000  6   2865.000   440.52             12.88              2.84                      49.82    0.023   0.5356 1.27e-06 2.06e-04

    25 230.0000  6   3095.000   440.52             12.88              2.84                      49.82    0.025   0.5255 1.23e-06 2.01e-04

    26 365.0000  6   3460.000   440.51             12.88              2.84                      49.82    0.028   0.5500 1.32e-06 2.43e-04

    27 135.0000  6   3595.000   440.51             12.88              2.84                      49.82    0.029   0.4960 1.14e-06 2.45e-04

```

```
/Users/mark/Documents/workspace/hatch/app/build/test/data/stflu005.dat



```

```
    28  55.0000  6   3650.000   440.51             12.88              2.84                      49.82    0.029   0.4281 9.63e-07 2.73e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                 44.433s    99.63%

|- Newton                                43.976s    98.97%

  |- Jacobian                            33.748s    76.74%

  |- Update                               9.712s    22.08%

  |- Residual                             0.197s     0.45%

  |- Solver                               0.136s     0.31%

  |- Logging                              0.007s     0.02%

|- Output                                 0.442s     0.99%

|- Input                                  0.000s     0.00%

Initialization                            0.166s     0.37%

------------------------------------------------------------

TOTAL                                    44.599s

============================================================





```

```
Found 29 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build/test/data/stflu005_00000.vtu

```

```
Widget(value='<iframe src="http://localhost:53331/index.html?ui=P_0x17a609910_1&reconnect=auto" class="pyvista…
```

# SPE4-b


### Load STARS

### Load ECL

### Load SMY File

Load the SMY file (`spe04b.smy`) into a pandas DataFrame, ensuring proper parsing of the data.

```
    61 116.4646  1   3650.000     0.07             27.29             99.73                      29.97   43.162   0.0208   0.0020   3.4503



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                 10.909s    99.29%

|- Newton                                10.742s    98.47%

  |- Jacobian                             8.487s    79.01%

  |- Update                               2.040s    18.99%

  |- Solver                               0.121s     1.12%

  |- Residual                             0.042s     0.39%

  |- Logging                              0.003s     0.03%

|- Output                                 0.153s     1.40%

|- Input                                  0.000s     0.00%

Initialization                            0.078s     0.71%

------------------------------------------------------------

TOTAL                                    10.987s

============================================================





```

## Select and Plot Columns

Select specific columns from the loaded DataFrames and plot them using matplotlib. For example, plot `TIME` vs `TEMP 1-1-4` from `stars_spe4b_special.csv`.

### Cell property

#### Block Pressure


```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_2.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_3.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_4.png" | relative_url }})

#### Block Temperature

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_5.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_6.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_7.png" | relative_url }})

#### Block Saturation

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_8.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_9.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_10.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_11.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_12.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_13.png" | relative_url }})

### vesus ECL

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_14.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_15.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_16.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_17.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_18.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_19.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_20.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_21.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_22.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_23.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_24.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_25.png" | relative_url }})

### Well property

#### Injector

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_26.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_27.png" | relative_url }})

#### Producer Corner

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_28.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_29.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_30.png" | relative_url }})

#### Producer Edge

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_31.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_32.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_33.png" | relative_url }})

# Buckley- Leverett



Two phase, isothermal problem

variable order: [Sw, P, T, So, X0, X1, Sg]



Acc w.r.t. [Sw, So, Sg, X0, X1, P, T]

```
[MacBook-Air.local:25265] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MacBook-Air.501/jf.0/344784896/sm_segment.MacBook-Air.501.148d0000.0 could be created.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water    GOR      Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                       ft3      Cut                                 err                              

 No      day    IT T   day      bbl/d    ft3/d    bbl/d    /bbl      %      bbl/d    ft3/d    bbl/d      %        psi              degF  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1 2.33e-04 11 1  2.3e-04     1.00                                                           1.00    0.045 491.1717   0.3331   0.1833

     2 1.27e-04  2    3.6e-04     1.00                                                           1.00    0.049   4.2661   0.0849   0.0202

     3 1.90e-04  4    5.5e-04     1.00                                                           1.00    0.842   7.5636   0.1334   0.0236

     4 2.34e-04  6    7.8e-04     1.00                                                           1.00    1.764   8.8050   0.1361   0.0221

     5 2.87e-04  6      0.001     1.00                                                           1.00    2.652  10.9567   0.1361   0.0213

     6 3.51e-04  8      0.001     1.00                                                           1.00    3.573  13.3953   0.1495   0.0213

     7 4.10e-04  9      0.002     1.00                                                           1.00    4.521  15.2025   0.1385   0.0215

     8 4.97e-04  9      0.002     1.00                                                           1.00    5.403  18.1014   0.1466   0.0223

     9 5.87e-04 12      0.003     1.00                                                           1.00    6.285  21.5336   0.1617   0.0226

    10 5.87e-04 12      0.004     1.00                                                           1.00    7.184  20.8806   0.1476   0.0212

    11 5.87e-04 10      0.004     1.00                                                           1.00    7.970  20.0347   0.1326   0.0204

    12 7.04e-04  8      0.005     0.90              0.12             11.69                       1.00    8.511  20.2257   0.1531   0.0239

    13 8.13e-04  3      0.006     0.55              0.45             44.55                       1.00    9.197  37.4810   0.1093   0.0412

    14 1.10e-03  2      0.007     0.33              0.67             67.10                       1.00    9.517  39.0113   0.0673   0.0441

    15 1.77e-03  2      0.008     0.20              0.80             79.80                       1.00    9.394  37.8579   0.0497   0.0474

    16 3.10e-03  2      0.012     0.12              0.88             87.83                       1.00    8.829  36.6778   0.0438   0.0505

    17 5.60e-03  2      0.017     0.07              0.93             92.98                       1.00    7.713  34.1157   0.0412   0.0498

    18   0.0103  3      0.027     0.04              0.96             96.28                       1.00    6.232  29.5512   0.0404   0.0451

    19   0.0188  3      0.046     0.02              0.98             98.17                       1.00    4.403  23.4138   0.0368   0.0386

    20   0.0353  3      0.082     0.01              0.99             99.18                       1.00    2.515  17.7304   0.0320   0.0333

```

```
No text to display.

```

```
    21   0.0679  3      0.149     0.00              1.00             99.66                       1.00    1.028  12.8003   0.0262   0.0094

    22   0.1349  3      0.284     0.00              1.00             99.87                       1.00    0.398   8.7667   0.0180   0.0055

    23   0.2809  3      0.565    5e-04              1.00             99.95                       1.00    0.428   6.7160   0.0192   0.0022

    24   0.5810  1      1.146    1e-04              1.00             99.99                       1.00    7.539   2.4198   0.0112 7.54e-04

    25   1.2615  1      2.408    8e-06              1.00            100.00                       1.00    8.645   0.3641   0.0029 2.00e-04

    26   2.8887  1      5.296    2e-07              1.00            100.00                       1.00    8.344   0.0241 2.47e-04 3.21e-05

    27   4.7035  1     10.000    6e-08              1.00            100.00                       1.00    7.505 3.00e-05 3.54e-06 7.96e-06



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  2.567s    97.40%

|- Newton                                 2.513s    97.89%

  |- Jacobian                             1.742s    69.32%

  |- Update                               0.700s    27.87%

  |- Solver                               0.033s     1.30%

  |- Residual                             0.018s     0.72%

  |- Logging                              0.001s     0.05%

|- Output                                 0.050s     1.96%

|- Input                                  0.000s     0.00%

Initialization                            0.068s     2.60%

------------------------------------------------------------

TOTAL                                     2.636s

============================================================





```

### Load Benchmark

### Buckley Plot

![png]({{ "/assets/images/benchmark_image_34.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_35.png" | relative_url }})

# MISC

## spe04b_cw.dat



## watfld_cw.dat



## stflu001.dat

Inverted 9 spot water flooding with area/block modifier, 5 point transmissibility


```
/Users/mark/Documents/workspace/hatch/app/build/test/data/spe04b_cw.dat



    22 365.0000  1   3650.000     5.00             63.84             92.74                      67.50    0.352   4.5892   0.0301   0.0084



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  5.011s    98.57%

|- Newton                                 4.871s    97.21%

  |- Jacobian                             3.661s    75.16%

  |- Update                               1.142s    23.44%

  |- Solver                               0.027s     0.55%

  |- Residual                             0.021s     0.44%

  |- Logging                              0.001s     0.02%

|- Output                                 0.136s     2.71%

|- Input                                  0.000s     0.00%

Initialization                            0.073s     1.43%

------------------------------------------------------------

TOTAL                                     5.084s

============================================================





```

```
/Users/mark/Documents/workspace/hatch/app/build/test/data/watfld_cw.dat



    38 203.0488  1   3650.000     6.58            496.71             98.69                     503.18    1.916   1.6566   0.0173   0.0036



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  6.382s    98.78%

|- Newton                                 6.142s    96.23%

  |- Jacobian                             4.478s    72.92%

  |- Update                               1.565s    25.48%

  |- Solver                               0.040s     0.65%

  |- Residual                             0.030s     0.50%

  |- Logging                              0.001s     0.02%

|- Output                                 0.232s     3.64%

|- Input                                  0.000s     0.00%

Initialization                            0.079s     1.22%

------------------------------------------------------------

TOTAL                                     6.461s

============================================================





```

```
/Users/mark/Documents/workspace/hatch/app/build/test/data/stflu001.dat



   172 348.4941  6   3650.000   103.23            781.38             88.33                     877.97   98.744   2.0596   0.0450   0.8750



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                 18.732s    99.64%

|- Newton                                18.349s    97.96%

  |- Jacobian                            14.656s    79.87%

  |- Update                               3.472s    18.92%

  |- Solver                               0.073s     0.40%

  |- Residual                             0.069s     0.37%

  |- Logging                              0.007s     0.04%

|- Output                                 0.357s     1.91%

|- Input                                  0.000s     0.00%

Initialization                            0.067s     0.36%

------------------------------------------------------------

TOTAL                                    18.799s

============================================================





```

## stflu002.dat

5000x5000x50, 2D diagonal water flooding in uniformed cartesian

## stflu003.dat

5000x5000x50, 2D diagonal water flooding in uniformed corner point

## stflu004.dat

2D diagonal water flooding for reduction of numerical dispersion and grid orientation effect


```
/Users/mark/Documents/workspace/hatch/app/build/test/data/stflu002.dat



    50  84.4290  1   3650.000  3931.77             69.97              1.75                    3998.01    6.192  40.5650   0.0127   0.0123



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  4.589s    98.39%

|- Newton                                 4.500s    98.06%

  |- Jacobian                             3.413s    75.85%

  |- Update                               0.981s    21.80%

  |- Solver                               0.058s     1.29%

  |- Residual                             0.023s     0.51%

  |- Logging                              0.002s     0.05%

|- Output                                 0.080s     1.75%

|- Input                                  0.000s     0.00%

Initialization                            0.075s     1.61%

------------------------------------------------------------

TOTAL                                     4.664s

============================================================





```

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_36.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_37.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_38.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_39.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_40.png" | relative_url }})

```
Widget(value='<iframe src="http://localhost:53331/index.html?ui=P_0x312d76de0_2&reconnect=auto" class="pyvista…
```

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_41.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_42.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_43.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_44.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_45.png" | relative_url }})

## stflu005.dat

steam injection in corner-point grid

# SPE4C


## Run & Load

```
/Users/mark/Documents/workspace/hatch/app/build/test/data/stspe003.dat



   182   1.3848  6 2 3149.018     0.11             33.31             99.66                       1.75   41.017   3.7968   0.1005   1.9011

   183   1.9347  2   3150.953     0.11             17.39             99.39                      31.55   41.021   1.8550   0.0138   0.2522

   184   4.1327  2   3155.085     0.10             17.60             99.41                      31.54   41.011   0.0574   0.0161   0.3476

   185   8.7060  2   3163.791     0.10             20.78             99.52                      31.54   40.998   0.1569   0.0155   0.6498

   186  18.4132  2   3182.204     0.09             23.27             99.60                      31.49   40.979   0.1248   0.0335   1.1251

   187  35.1137  2   3217.318     0.08             25.83             99.68                      31.05   40.999   0.1478   0.0225   1.6442

   188  71.2296  2   3288.548     0.07             28.34             99.77                      30.48   41.057   0.1765   0.0060   3.2002

   189 153.1341  3   3441.682     0.04             28.32             99.84                      28.65   41.193   0.5584   0.0091   6.4381

   190 208.3182  3   3650.000     0.03             27.22             99.89                      27.02   42.160   0.5504   0.0075   6.9417



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                               1m 40.14s    99.92%

|- Newton                              1m 39.57s    99.43%

  |- Jacobian                          1m 24.66s    85.03%

  |- Update                              12.489s    12.54%

  |- Solver                               1.837s     1.84%

  |- Residual                             0.210s     0.21%

  |- Logging                              0.021s     0.02%

|- Output                                 0.521s     0.52%

|- Input                                  0.000s     0.00%

Initialization                            0.078s     0.08%

------------------------------------------------------------

TOTAL                                  1m 40.22s

============================================================





```

#### Load CMG

### Load ECL

### Wells

![png]({{ "/assets/images/benchmark_image_46.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_47.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_48.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_49.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_50.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_51.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_52.png" | relative_url }})

### Block

#### Block Pressure


```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_53.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_54.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_55.png" | relative_url }})

#### Block Temperature

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_56.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_57.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_58.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_59.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_60.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_61.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_62.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_63.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_64.png" | relative_url }})

#### v.s. ECL

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_65.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_66.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_67.png" | relative_url }})
