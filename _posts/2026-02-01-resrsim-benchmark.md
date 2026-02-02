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
    28  55.0000  6   3650.000   440.51             12.88              2.84                      49.82    0.029   0.4281 9.63e-07 2.73e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                 44.492s    99.67%

|- Newton                                44.029s    98.96%

  |- Jacobian                            33.734s    76.62%

  |- Update                               9.773s    22.20%

  |- Residual                             0.199s     0.45%

  |- Solver                               0.141s     0.32%

  |- Logging                              0.004s     0.01%

|- Output                                 0.447s     1.00%

|- Input                                  0.001s     0.00%

Initialization                            0.148s     0.33%

------------------------------------------------------------

TOTAL                                    44.640s

============================================================





```

```
Found 29 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build/test/data/stflu005_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_2.png" | relative_url }})

```
Interactive view: /Users/mark/Documents/workspace/hatch/app/build/test/data/stflu005_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_3.png" | relative_url }})

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

Timeloop                                 10.902s    99.13%

|- Newton                                10.750s    98.60%

  |- Jacobian                             8.488s    78.96%

  |- Update                               2.048s    19.05%

  |- Solver                               0.119s     1.11%

  |- Residual                             0.042s     0.39%

  |- Logging                              0.005s     0.05%

|- Output                                 0.139s     1.27%

|- Input                                  0.000s     0.00%

Initialization                            0.095s     0.87%

------------------------------------------------------------

TOTAL                                    10.998s

============================================================





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
    27   4.7035  1     10.000    6e-08              1.00            100.00                       1.00    7.505 3.00e-05 3.54e-06 7.96e-06



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time   % Total

------------------------------------------------------------

Timeloop                                  2.582s    97.51%

|- Newton                                 2.521s    97.64%

  |- Jacobian                             1.721s    68.26%

  |- Update                               0.727s    28.84%

  |- Solver                               0.035s     1.39%

  |- Residual                             0.018s     0.72%

  |- Logging                              0.001s     0.05%

|- Output                                 0.057s     2.22%

|- Input                                  0.000s     0.00%

Initialization                            0.066s     2.49%

------------------------------------------------------------

TOTAL                                     2.648s

============================================================





```

### Load Benchmark

### Buckley Plot

![png]({{ "/assets/images/benchmark_image_36.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_37.png" | relative_url }})

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

Timeloop                                  4.987s    98.63%

|- Newton                                 4.848s    97.21%

  |- Jacobian                             3.602s    74.30%

  |- Update                               1.179s    24.32%

  |- Solver                               0.026s     0.54%

  |- Residual                             0.021s     0.44%

  |- Logging                              0.001s     0.02%

|- Output                                 0.135s     2.71%

|- Input                                  0.000s     0.00%

Initialization                            0.069s     1.37%

------------------------------------------------------------

TOTAL                                     5.056s

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

Timeloop                                  6.414s    98.95%

|- Newton                                 6.168s    96.16%

  |- Jacobian                             4.537s    73.55%

  |- Update                               1.534s    24.87%

  |- Solver                               0.039s     0.64%

  |- Residual                             0.030s     0.49%

  |- Logging                              0.001s     0.02%

|- Output                                 0.237s     3.70%

|- Input                                  0.000s     0.00%

Initialization                            0.068s     1.05%

------------------------------------------------------------

TOTAL                                     6.482s

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

Timeloop                                 18.389s    99.65%

|- Newton                                17.996s    97.87%

  |- Jacobian                            14.394s    79.98%

  |- Update                               3.394s    18.86%

  |- Residual                             0.068s     0.38%

  |- Solver                               0.067s     0.37%

  |- Logging                              0.006s     0.03%

|- Output                                 0.368s     2.00%

|- Input                                  0.000s     0.00%

Initialization                            0.065s     0.35%

------------------------------------------------------------

TOTAL                                    18.453s

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

Timeloop                                  4.507s    98.47%

|- Newton                                 4.414s    97.93%

  |- Jacobian                             3.356s    76.03%

  |- Update                               0.952s    21.57%

  |- Solver                               0.055s     1.26%

  |- Residual                             0.023s     0.52%

  |- Logging                              0.006s     0.13%

|- Output                                 0.085s     1.89%

|- Input                                  0.000s     0.00%

Initialization                            0.070s     1.53%

------------------------------------------------------------

TOTAL                                     4.577s

============================================================





```

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_38.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_39.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_40.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_41.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_42.png" | relative_url }})

```
Widget(value='<iframe src="http://localhost:55264/index.html?ui=P_0x3030765a0_3&reconnect=auto" class="pyvista…
```

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

Timeloop                               1m 38.70s    99.92%

|- Newton                              1m 38.07s    99.36%

  |- Jacobian                          1m 23.36s    85.00%

  |- Update                              12.339s    12.58%

  |- Solver                               1.812s     1.85%

  |- Residual                             0.207s     0.21%

  |- Logging                              0.015s     0.02%

|- Output                                 0.577s     0.58%

|- Input                                  0.000s     0.00%

Initialization                            0.077s     0.08%

------------------------------------------------------------

TOTAL                                  1m 38.78s

============================================================





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
