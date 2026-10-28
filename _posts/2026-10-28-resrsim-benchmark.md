---
layout: default
title: "Benchmark results of resrsim"
date: 2026-10-28
---

# Catfish benchmark



`simuapp` (serial) and `simumpi` (MPI) share the same decks and

the same `.smy` columns, so every plot below works with either engine - see `ENGINE` in Setup.

## Setup

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

env: MallocStackLogging=0

simuexe path: build-release/bin/simuapp

ipynb_folder path: /Users/mark/Documents/workspace/hatch/app

output_folder path: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/

RUN_SIMULATIONS: True

UNIT_SYSTEM: SI

ENGINE: simuapp

simumpi available: True (build-release/bin/simumpi)

```

# 3D



In Jupyter Notebook, `pyvista.set_jupyter_backend("trame")` must install `pyvista` and `trame` 

<!-- 

```bash

python -m pip install --upgrade pip

python -m pip install pyvista

pip install trame trame-vtk trame-vuetify

``` -->


```
Loading: /Users/mark/Documents/workspace/hatch/app/test/data/pebi_resr_grid.vtk

```

![png]({{ "/assets/images/benchmark_image_1.png" | relative_url }})

```
Loading: /Users/mark/Documents/workspace/hatch/app/test/python/radial_grid.vtk

```

![png]({{ "/assets/images/benchmark_image_2.png" | relative_url }})

## stflu005.dat

steam injection in corner-point grid

```
Running simulation [simuapp]: Steam injection Corner point

Elapsed: 1.18s

    22  55.0000  1   3650.000    47.21              1.86              3.80                      30.05    0.000   39.404 4.29e-04    0.029



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Initialization                            0.267s  51.02%      

|- execution                              0.245s  |- 91.74%   

Timeloop                                  0.256s  48.98%      

|- Newton                                 0.228s  |- 89.21%   

  |- Update                               0.086s    |- 37.57% 

  |- FluxJac                              0.057s    |- 24.88% 

  |- ScdAcc                               0.029s    |- 12.51% 

  |- Solver                               0.020s    |- 8.63%  

  |- update_dev                           0.011s    |- 4.90%  

  |- Precond                              0.010s    |- 4.22%  

  |- Residual                             0.006s    |- 2.44%  

  |- PerfJac                              0.001s    |- 0.60%  

  |- alignvar                             0.001s    |- 0.60%  

  |- SanitizeJac                          0.001s    |- 0.54%  

  |- HeatLoss                             0.001s    |- 0.31%  

|- Output                                 0.016s  |- 6.08%    

|- Logging                                0.003s  |- 1.21%    

|- Input                                  0.000s  |- 0.05%    

------------------------------------------------------------

TOTAL                                     0.523s

============================================================



Time steps : 22/22, step size: 165.909, 124.408

```

```
Found 23 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu005_00000.vtu

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
Running simulation [simuapp]: SPE4-b

Elapsed: 0.99s

    46  85.0883  5   3650.000     0.06              4.42             98.56                       4.57   10.346    5.911   0.0086    1.523



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.662s  91.46%      

|- Newton                                 0.640s  |- 96.56%   

  |- Update                               0.161s    |- 25.22% 

  |- FluxJac                              0.159s    |- 24.79% 

  |- Solver                               0.117s    |- 18.24% 

  |- ScdAcc                               0.052s    |- 8.09%  

  |- Precond                              0.050s    |- 7.90%  

  |- update_dev                           0.030s    |- 4.67%  

  |- PerfJac                              0.025s    |- 3.84%  

  |- SanitizeJac                          0.015s    |- 2.41%  

  |- alignvar                             0.009s    |- 1.46%  

  |- Residual                             0.005s    |- 0.74%  

  |- HeatLoss                             0.004s    |- 0.59%  

|- Output                                 0.015s  |- 2.29%    

|- Logging                                0.005s  |- 0.79%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.062s  8.54%       

|- execution                              0.059s  |- 95.10%   

------------------------------------------------------------

TOTAL                                     0.724s

============================================================



Time steps : 46/46, step size: 79.3478, 84.4867

```

## Select and Plot Columns

Select specific columns from the loaded DataFrames and plot them using matplotlib. For example, plot `TIME` vs `TEMP 1-1-4` from `stars_spe4b_special.csv`.

### Cell property

#### Block Pressure


### (1,1,4) is wet steam from day 157 on



`sg` first leaves zero there at day 157.2, and from then on `P = Psat(T)` holds to within 45 kPa

for the rest of the run: that cell's pressure and temperature are one degree of freedom, not two,

so the curve can only rise where the cell heats and fall where it cools. The mid-run excursion is

that - 2559 kPa (497 K) at day 432, back down to 1220 kPa (460 K) by day 799 - not a solver

artefact. It ends at 6732 kPa (556 K) with the injector's BHP at 6895 kPa, exactly its

`*OPERATE *MAX *BHP 1000` psi limit, which is the expected endgame once both producers are choked

by `*MAX STEAM`. 49 steps marched of 50 attempted, closing to -0.23% water and -0.67% energy.



This deck deliberately sets no `*DTMAX`. The cap was a workaround for steps whose well constraint

never converged being accepted - and because the instantaneous material balance error is exactly

`dt * sum(cell residual)`, those steps are where mass went missing. That acceptance rule is gone,

so the workaround is not needed to close the balance.

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

### Corner grid

```
Running simulation [simuapp]: Corner Grid

Elapsed: 1.05s

    49 341.8934 15   3650.000     0.03              2.26             98.51                       2.44    9.454  1.1e+03   0.0922   15.244



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.808s  93.09%      

|- Newton                                 0.785s  |- 97.16%   

  |- Update                               0.203s    |- 25.82% 

  |- FluxJac                              0.188s    |- 23.92% 

  |- Solver                               0.129s    |- 16.46% 

  |- Precond                              0.067s    |- 8.59%  

  |- ScdAcc                               0.067s    |- 8.52%  

  |- update_dev                           0.038s    |- 4.86%  

  |- PerfJac                              0.033s    |- 4.15%  

  |- SanitizeJac                          0.019s    |- 2.42%  

  |- alignvar                             0.010s    |- 1.34%  

  |- Residual                             0.007s    |- 0.83%  

  |- HeatLoss                             0.005s    |- 0.65%  

|- Output                                 0.015s  |- 1.80%    

|- Logging                                0.008s  |- 0.94%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.060s  6.91%       

|- execution                              0.057s  |- 95.81%   

------------------------------------------------------------

TOTAL                                     0.868s

============================================================



Time steps : 49/55, step size: 74.4898, 98.6205

```

![png]({{ "/assets/images/benchmark_image_36.png" | relative_url }})

# Buckley- Leverett



Two phase, isothermal problem

variable order: [Sw, P, T, So, X0, X1, Sg]



Acc w.r.t. [Sw, So, Sg, X0, X1, P, T]

```
Running simulation [simuapp]: Buckley-Leverett

Elapsed: 0.89s

    81   3.9903  0     10.000    3e-08              0.16            100.00                       0.16   13.983                           



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.657s  93.22%      

|- Newton                                 0.631s  |- 95.99%   

  |- Update                               0.190s    |- 30.15% 

  |- FluxJac                              0.094s    |- 14.87% 

  |- Precond                              0.068s    |- 10.78% 

  |- ScdAcc                               0.067s    |- 10.61% 

  |- Solver                               0.066s    |- 10.53% 

  |- update_dev                           0.041s    |- 6.48%  

  |- PerfJac                              0.033s    |- 5.17%  

  |- SanitizeJac                          0.022s    |- 3.42%  

  |- alignvar                             0.012s    |- 1.96%  

  |- HeatLoss                             0.009s    |- 1.45%  

  |- Residual                             0.006s    |- 0.99%  

|- Output                                 0.018s  |- 2.73%    

|- Logging                                0.013s  |- 1.94%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.048s  6.78%       

|- execution                              0.045s  |- 95.06%   

------------------------------------------------------------

TOTAL                                     0.705s

============================================================



Time steps : 81/85, step size: 0.123457, 0.528462

```

### Load Benchmark

### Buckley Plot

![png]({{ "/assets/images/benchmark_image_37.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_38.png" | relative_url }})

# MISC

## spe04b_cw.dat

```
Running simulation [simuapp]: SPE4-b water flooding

Elapsed: 0.60s

    22 163.8815  2   3650.000     0.78             10.19             92.87                      10.73    0.001   13.764   0.0097    0.002



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.386s  88.11%      

|- Newton                                 0.374s  |- 97.04%   

  |- FluxJac                              0.117s    |- 31.29% 

  |- Update                               0.117s    |- 31.16% 

  |- Solver                               0.044s    |- 11.73% 

  |- ScdAcc                               0.032s    |- 8.48%  

  |- Precond                              0.023s    |- 6.25%  

  |- update_dev                           0.018s    |- 4.71%  

  |- PerfJac                              0.006s    |- 1.66%  

  |- SanitizeJac                          0.005s    |- 1.31%  

  |- Residual                             0.004s    |- 1.12%  

  |- alignvar                             0.003s    |- 0.91%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.008s  |- 2.12%    

|- Logging                                0.001s  |- 0.25%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.052s  11.89%      

|- execution                              0.050s  |- 95.60%   

------------------------------------------------------------

TOTAL                                     0.438s

============================================================



Time steps : 22/22, step size: 165.909, 155.033

```



## watfld_cw.dat

```
Running simulation [simuapp]: SPE4-b Water flooding without vmod

Elapsed: 0.84s

    35  33.3426  2   3650.000     1.04             79.00             98.70                      80.00    0.000    1.919   0.0029  3.2e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.611s  91.38%      

|- Newton                                 0.592s  |- 96.98%   

  |- Update                               0.178s    |- 30.11% 

  |- FluxJac                              0.177s    |- 29.89% 

  |- Solver                               0.074s    |- 12.57% 

  |- ScdAcc                               0.046s    |- 7.82%  

  |- PerfJac                              0.031s    |- 5.27%  

  |- Precond                              0.031s    |- 5.26%  

  |- update_dev                           0.027s    |- 4.51%  

  |- SanitizeJac                          0.008s    |- 1.30%  

  |- Residual                             0.006s    |- 1.04%  

  |- alignvar                             0.005s    |- 0.87%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.012s  |- 1.92%    

|- Logging                                0.002s  |- 0.31%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.058s  8.62%       

|- execution                              0.055s  |- 96.04%   

------------------------------------------------------------

TOTAL                                     0.668s

============================================================



Time steps : 35/35, step size: 104.286, 142.633

```

## stflu001.dat

Inverted 9 spot water flooding with area/block modifier, 5 point transmissibility


```
Running simulation [simuapp]: Inverted 9 spot water flooding

Elapsed: 16.04s

   816   1.3715  6   3650.000     0.06            142.24             99.96                     142.31   66.900    6.026   0.0010    0.205



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 15.807s  99.66%      

|- Newton                                15.516s  |- 98.16%   

  |- FluxJac                              4.775s    |- 30.78% 

  |- Update                               4.318s    |- 27.83% 

  |- ScdAcc                               1.645s    |- 10.60% 

  |- Precond                              1.369s    |- 8.82%  

  |- update_dev                           1.105s    |- 7.12%  

  |- Solver                               0.863s    |- 5.56%  

  |- SanitizeJac                          0.387s    |- 2.49%  

  |- PerfJac                              0.272s    |- 1.75%  

  |- alignvar                             0.248s    |- 1.60%  

  |- Residual                             0.137s    |- 0.88%  

  |- HeatLoss                             0.117s    |- 0.75%  

|- Output                                 0.216s  |- 1.37%    

|- Logging                                0.095s  |- 0.60%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.054s  0.34%       

|- execution                              0.052s  |- 95.52%   

------------------------------------------------------------

TOTAL                                    15.861s

============================================================



Time steps : 816/827, step size: 4.47304, 4.58921

```

## stflu002.dat

5000x5000x50, 2D diagonal water flooding in uniformed cartesian

```
Running simulation [simuapp]: Uniformed cartesian water flooding

Elapsed: 0.63s

    49 268.8942  6   3650.000   620.60             11.38              1.80                     635.95    0.007  1.1e+03   0.0405    0.028



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.365s  82.88%      

|- Newton                                 0.329s  |- 90.25%   

  |- Update                               0.083s    |- 25.20% 

  |- Solver                               0.067s    |- 20.27% 

  |- FluxJac                              0.061s    |- 18.53% 

  |- Precond                              0.027s    |- 8.09%  

  |- ScdAcc                               0.025s    |- 7.69%  

  |- update_dev                           0.013s    |- 3.95%  

  |- PerfJac                              0.012s    |- 3.78%  

  |- SanitizeJac                          0.008s    |- 2.50%  

  |- alignvar                             0.005s    |- 1.62%  

  |- HeatLoss                             0.003s    |- 1.05%  

  |- Residual                             0.003s    |- 0.84%  

|- Output                                 0.029s  |- 8.01%    

|- Logging                                0.018s  |- 4.90%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.075s  17.12%      

|- execution                              0.072s  |- 96.01%   

------------------------------------------------------------

TOTAL                                     0.440s

============================================================



Time steps : 49/49, step size: 74.4898, 130.04

```



## stflu003.dat

5000x5000x50, 2D diagonal water flooding in uniformed corner point

```
Running simulation [simuapp]: uniformed corner grid

Elapsed: 0.51s

    44 242.0923  6   3650.000   621.22             11.18              1.77                     635.95    0.005  850.791   0.0365    0.025



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.283s  85.37%      

|- Newton                                 0.268s  |- 94.82%   

  |- Update                               0.075s    |- 28.05% 

  |- FluxJac                              0.052s    |- 19.46% 

  |- Solver                               0.050s    |- 18.67% 

  |- Precond                              0.024s    |- 8.98%  

  |- ScdAcc                               0.022s    |- 8.14%  

  |- PerfJac                              0.011s    |- 4.09%  

  |- update_dev                           0.010s    |- 3.91%  

  |- SanitizeJac                          0.007s    |- 2.75%  

  |- alignvar                             0.005s    |- 1.72%  

  |- HeatLoss                             0.003s    |- 1.14%  

  |- Residual                             0.002s    |- 0.92%  

|- Output                                 0.010s  |- 3.36%    

|- Logging                                0.003s  |- 0.95%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.048s  14.63%      

|- execution                              0.046s  |- 93.99%   

------------------------------------------------------------

TOTAL                                     0.331s

============================================================



Time steps : 44/44, step size: 82.9545, 133.208

```

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_39.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_40.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_41.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_42.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_43.png" | relative_url }})



## stflu004.dat

2D diagonal water flooding for reduction of numerical dispersion and grid orientation effect


```
Running simulation [simuapp]: 2D diagonal flow: grid orientation

Elapsed: 0.89s

    61  22.1594  5   3650.000   613.37             21.71              3.42                     635.95    0.002  280.490   0.0074    0.016



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.657s  93.31%      

|- Newton                                 0.636s  |- 96.80%   

  |- Update                               0.223s    |- 34.97% 

  |- FluxJac                              0.136s    |- 21.43% 

  |- Solver                               0.110s    |- 17.33% 

  |- ScdAcc                               0.048s    |- 7.48%  

  |- Precond                              0.038s    |- 5.99%  

  |- update_dev                           0.025s    |- 3.87%  

  |- PerfJac                              0.014s    |- 2.19%  

  |- SanitizeJac                          0.010s    |- 1.54%  

  |- HeatLoss                             0.009s    |- 1.39%  

  |- Residual                             0.007s    |- 1.09%  

  |- alignvar                             0.006s    |- 1.02%  

|- Output                                 0.014s  |- 2.19%    

|- Logging                                0.002s  |- 0.35%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.047s  6.69%       

|- execution                              0.045s  |- 95.10%   

------------------------------------------------------------

TOTAL                                     0.705s

============================================================



Time steps : 61/61, step size: 59.8361, 78.8186

```

![png]({{ "/assets/images/benchmark_image_44.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_45.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_46.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_47.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_48.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_49.png" | relative_url }})

## stflu007.dat

PEBI_GRID


```
Running simulation [simuapp]: 2D diagonal flow: pebi grid

Elapsed: 2.04s

    59 272.1883  6   3650.000   619.02             12.22              1.94                     635.95    0.005  1.2e+03   0.0553    0.049



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.798s  96.97%      

|- Newton                                 1.765s  |- 98.19%   

  |- Solver                               0.783s    |- 44.37% 

  |- FluxJac                              0.382s    |- 21.66% 

  |- Update                               0.317s    |- 17.96% 

  |- ScdAcc                               0.090s    |- 5.11%  

  |- Precond                              0.061s    |- 3.45%  

  |- update_dev                           0.045s    |- 2.53%  

  |- HeatLoss                             0.018s    |- 1.02%  

  |- PerfJac                              0.014s    |- 0.81%  

  |- Residual                             0.014s    |- 0.79%  

  |- SanitizeJac                          0.012s    |- 0.69%  

  |- alignvar                             0.009s    |- 0.52%  

|- Output                                 0.024s  |- 1.36%    

|- Logging                                0.003s  |- 0.18%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.056s  3.03%       

|- execution                              0.048s  |- 84.67%   

------------------------------------------------------------

TOTAL                                     1.854s

============================================================



Time steps : 59/59, step size: 61.8644, 117.981

```

![png]({{ "/assets/images/benchmark_image_50.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_51.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_52.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_53.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_54.png" | relative_url }})

# SPE4C

* Steam flood on three component live oil

* 'Water', 'LiteOil', 'Medm oil', 'Heavy oil'


## Run & Load

```
Running simulation [simuapp]: SPE4-C benchmark on live oil

Elapsed: 2.86s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.630s  97.96%      

|- Newton                                 2.587s  |- 98.38%   

  |- Solver                               0.809s    |- 31.26% 

  |- FluxJac                              0.577s    |- 22.32% 

  |- Update                               0.470s    |- 18.19% 

  |- ScdAcc                               0.202s    |- 7.80%  

  |- Precond                              0.202s    |- 7.79%  

  |- update_dev                           0.113s    |- 4.38%  

  |- PerfJac                              0.077s    |- 2.96%  

  |- SanitizeJac                          0.042s    |- 1.63%  

  |- alignvar                             0.026s    |- 1.00%  

  |- Residual                             0.014s    |- 0.53%  

  |- HeatLoss                             0.014s    |- 0.53%  

|- Output                                 0.028s  |- 1.06%    

|- Logging                                0.018s  |- 0.70%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.055s  2.04%       

|- execution                              0.052s  |- 95.09%   

------------------------------------------------------------

TOTAL                                     2.684s

============================================================



Time steps : 94/113, step size: 33.7201, 49.5189

```

#### Load CMG

### Load ECL

### Wells

![png]({{ "/assets/images/benchmark_image_55.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_56.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_57.png" | relative_url }})

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

### Block

#### Block Pressure


```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_64.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_65.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_66.png" | relative_url }})

#### Block Temperature

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_67.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_68.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_69.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_70.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_71.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_72.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_73.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_74.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_75.png" | relative_url }})

#### v.s. ECL

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_76.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_77.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_78.png" | relative_url }})

# Cyclic steam stimulation

## CSS SPE4

stspe001.dat: Cyclic steam stimulation on radial grid

```
Running simulation [simuapp]: Cyclic steam stimulation in Radial grid

Elapsed: 0.86s

   101  68.6845  6   1095.000     1.24              0.76             37.92                               0.020   24.100   0.1646    4.453



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.605s  90.62%      

|- Newton                                 0.569s  |- 94.07%   

  |- Update                               0.166s    |- 29.11% 

  |- FluxJac                              0.094s    |- 16.58% 

  |- Precond                              0.072s    |- 12.60% 

  |- PerfJac                              0.065s    |- 11.39% 

  |- ScdAcc                               0.053s    |- 9.32%  

  |- Solver                               0.032s    |- 5.67%  

  |- update_dev                           0.029s    |- 5.18%  

  |- SanitizeJac                          0.024s    |- 4.25%  

  |- alignvar                             0.013s    |- 2.26%  

  |- Residual                             0.004s    |- 0.79%  

  |- HeatLoss                             0.003s    |- 0.57%  

|- Output                                 0.022s  |- 3.69%    

|- Logging                                0.005s  |- 0.81%    

|- Input                                  0.001s  |- 0.14%    

Initialization                            0.063s  9.38%       

|- execution                              0.060s  |- 96.28%   

------------------------------------------------------------

TOTAL                                     0.668s

============================================================



Time steps : 101/102, step size: 10.8416, 21.8903

```

![png]({{ "/assets/images/benchmark_image_79.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_80.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_81.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_82.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_83.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_84.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_85.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_86.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_87.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_88.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_89.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_90.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_91.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_92.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_93.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_94.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_95.png" | relative_url }})



## stflu008.dat

Cyclic steam stimulation on cartesian grid


```
Running simulation [simuapp]: Cyclic steam stimulation in Cartesian

Elapsed: 10.59s

   150  36.8637  6   1095.000     1.59              1.13             41.52                               0.071   21.341   0.0648    2.486



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 10.358s  99.52%      

|- Newton                                10.239s  |- 98.85%   

  |- FluxJac                              3.600s    |- 35.16% 

  |- Update                               2.718s    |- 26.55% 

  |- Solver                               1.616s    |- 15.78% 

  |- ScdAcc                               0.835s    |- 8.15%  

  |- update_dev                           0.461s    |- 4.50%  

  |- Precond                              0.441s    |- 4.31%  

  |- PerfJac                              0.107s    |- 1.04%  

  |- Residual                             0.099s    |- 0.97%  

  |- HeatLoss                             0.091s    |- 0.89%  

  |- SanitizeJac                          0.067s    |- 0.65%  

  |- alignvar                             0.067s    |- 0.65%  

|- Output                                 0.078s  |- 0.76%    

|- Logging                                0.024s  |- 0.23%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.050s  0.48%       

|- execution                              0.047s  |- 95.34%   

------------------------------------------------------------

TOTAL                                    10.408s

============================================================



Time steps : 150/161, step size: 7.3, 16.8364

```

```
Found 151 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu008_00150.vtu

```

![png]({{ "/assets/images/benchmark_image_96.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_97.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_98.png" | relative_url }})

## stflu009.dat - grid-resolution comparison (not PEBI-vs-Cartesian parity)



`stflu009.dat` runs the same cyclic steam stimulation as `stflu008.dat`, but on a PEBI grid.

Everything that *can* be matched between the two decks has been - layer-centre depths, initial

pressure, per-layer permeability, and the hand-set well indices that reproduce the Cartesian

Peaceman value - so the only real difference left is the well cell's planar footprint:



| | stflu008 (Cartesian) | stflu009 (PEBI) |

|---|---|---|

| well-cell footprint | DI=DJ=3 ft -> 9.0 ft^2 | regular hexagon -> 155.9 ft^2 (~12.5 x 12.5 ft) |



`stflu009_grd.vtk` is a *uniform* ~7.7 ft honeycomb (29x33x4, 3764 cells - refined from the earlier

15x17x4/988-cell, ~15.5 ft version) with no near-well refinement, so the well cell's pore volume is

still ~17.3x the Cartesian one (down from ~69x). Heating rate scales as `1/PV`, and the injector's

injectivity is governed by how fast the well cell heats enough to boil off steam and unlock relative

permeability (`krw(Sw=0.45)=0`, oil is 487 cp at 125 F). At this resolution the well cell now warms

from 125 F to ~233 F in the first 10-day cycle (vs only ~10 C on the coarser grid), and water

injection ramps from ~1.1 to ~14.6 m^3/d while still pinned on `*MAX BHP`; oil production shows a

real per-cycle peak (~7-12 m^3/d) rather than near zero - but `Sg` at the well cell still stays 0

through day 10, so full steam breakthrough still lags the Cartesian run's by day 3.



So the plot below is a **grid-resolution** comparison - it shows the uniform PEBI grid is simply

too coarse near the well, not a PEBI-vs-Cartesian *physics* discrepancy. A meaningful parity plot

needs near-well PEBI refinement (inner cells down to the ~3 ft Cartesian scale), which is the

whole point of using PEBI in the first place.

```
Running simulation [simuapp]: Cyclic steam stimulation in Pebi-grid

Elapsed: 30.54s

   122  34.5009  6   1095.000     0.85              0.44             34.12                               0.005   73.368   0.2557    1.917



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 30.231s  99.67%      

|- Newton                                30.022s  |- 99.31%   

  |- FluxJac                             11.080s    |- 36.91% 

  |- Update                               7.345s    |- 24.47% 

  |- Solver                               6.877s    |- 22.91% 

  |- ScdAcc                               1.789s    |- 5.96%  

  |- Precond                              0.991s    |- 3.30%  

  |- update_dev                           0.975s    |- 3.25%  

  |- Residual                             0.271s    |- 0.90%  

  |- HeatLoss                             0.133s    |- 0.44%  

  |- alignvar                             0.103s    |- 0.34%  

  |- PerfJac                              0.071s    |- 0.24%  

  |- SanitizeJac                          0.069s    |- 0.23%  

|- Output                                 0.177s  |- 0.59%    

|- Logging                                0.022s  |- 0.07%    

|- Input                                  0.001s  |- 0.00%    

Initialization                            0.101s  0.33%       

|- execution                              0.070s  |- 68.64%   

------------------------------------------------------------

TOTAL                                    30.332s

============================================================



Time steps : 122/123, step size: 8.97541, 20.3546

```

```
Found 123 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu009_00122.vtu

```

![png]({{ "/assets/images/benchmark_image_99.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_100.png" | relative_url }})

### stflu025.dat - near-well-refined PEBI (the real PEBI-vs-Cartesian parity case)



`stflu025.dat` is the PEBI companion the note above asks for: a *graded* honeycomb whose

inner cells are refined down toward the ~3 ft Cartesian near-well scale, instead of the uniform

~7.7 ft cells of `stflu009.dat`. With a small enough well-cell pore volume the injector regains

injectivity (the cell heats, steam boils off, `krw` unlocks), so the cyclic-steam response

tracks the near-well-refined Cartesian run (`stflu008.dat`) more closely than the uniform PEBI

grid does, whose well cell (now ~17.3x the Cartesian pore volume, down from ~69x) still stays

pinned on `*MAX BHP` and lags the Cartesian steam breakthrough even though it heats much faster

than before (see note above).



The three curves below are therefore the intended comparison:



| run | grid | near-well cell |

|---|---|---|

| `stflu008.dat` | Cartesian | DI=DJ=3 ft (~9 ft^2) |

| `stflu009.dat` | uniform PEBI | ~12.5 ft hexagon (155.9 ft^2) |

| `stflu025.dat` | graded PEBI | refined toward ~3 ft near the well |


```
Running simulation [simuapp]: Cyclic steam stimulation in graded Pebi-grid

Elapsed: 15.51s

   216  32.0337  6   1095.000     1.71              1.17             40.59                               0.302   19.089   0.0744    1.982



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 15.216s  99.39%      

|- Newton                                15.030s  |- 98.78%   

  |- FluxJac                              5.312s    |- 35.34% 

  |- Update                               3.564s    |- 23.71% 

  |- Solver                               3.207s    |- 21.34% 

  |- ScdAcc                               1.010s    |- 6.72%  

  |- update_dev                           0.626s    |- 4.16%  

  |- Precond                              0.590s    |- 3.93%  

  |- PerfJac                              0.172s    |- 1.15%  

  |- SanitizeJac                          0.137s    |- 0.91%  

  |- Residual                             0.125s    |- 0.83%  

  |- alignvar                             0.074s    |- 0.49%  

  |- HeatLoss                             0.060s    |- 0.40%  

|- Output                                 0.148s  |- 0.98%    

|- Logging                                0.017s  |- 0.11%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.093s  0.61%       

|- execution                              0.077s  |- 82.86%   

------------------------------------------------------------

TOTAL                                    15.309s

============================================================



Time steps : 216/220, step size: 5.06944, 13.8063

```

```
Found 217 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu025_00216.vtu

```

![png]({{ "/assets/images/benchmark_image_101.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_102.png" | relative_url }})

### stflu010.dat 

incomp gas

```
Running simulation [simuapp]: Incomp GAS

Elapsed: 3.38s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  3.126s  97.74%      

|- Newton                                 3.072s  |- 98.28%   

  |- Solver                               0.927s    |- 30.17% 

  |- Update                               0.674s    |- 21.94% 

  |- FluxJac                              0.535s    |- 17.42% 

  |- Precond                              0.321s    |- 10.45% 

  |- ScdAcc                               0.266s    |- 8.67%  

  |- update_dev                           0.138s    |- 4.50%  

  |- SanitizeJac                          0.077s    |- 2.51%  

  |- alignvar                             0.045s    |- 1.46%  

  |- Residual                             0.016s    |- 0.51%  

  |- PerfJac                              0.012s    |- 0.39%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.039s  |- 1.24%    

|- Logging                                0.028s  |- 0.91%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.072s  2.26%       

|- execution                              0.069s  |- 95.01%   

------------------------------------------------------------

TOTAL                                     3.198s

============================================================



Time steps : 126/151, step size: 5.47619e-05, 3.0321e-05

```

![png]({{ "/assets/images/benchmark_image_103.png" | relative_url }})

### SAGD

#### 2D cross the well

```
Running simulation [simuapp]: SAGD

Elapsed: 4.37s

   217   4.3042  6   2526.000     6.02             57.86             90.57                      54.10    0.002    0.834   0.0794    1.773



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  4.135s  98.60%      

|- Newton                                 4.050s  |- 97.93%   

  |- Solver                               1.113s    |- 27.49% 

  |- Update                               0.997s    |- 24.61% 

  |- FluxJac                              0.895s    |- 22.10% 

  |- ScdAcc                               0.328s    |- 8.09%  

  |- Precond                              0.268s    |- 6.62%  

  |- update_dev                           0.183s    |- 4.52%  

  |- SanitizeJac                          0.073s    |- 1.80%  

  |- alignvar                             0.049s    |- 1.22%  

  |- PerfJac                              0.042s    |- 1.04%  

  |- Residual                             0.034s    |- 0.84%  

  |- HeatLoss                             0.007s    |- 0.17%  

|- Output                                 0.059s  |- 1.42%    

|- Logging                                0.021s  |- 0.51%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.059s  1.40%       

|- execution                              0.056s  |- 95.93%   

------------------------------------------------------------

TOTAL                                     4.194s

============================================================



Time steps : 217/221, step size: 11.6406, 12.8434

```

![png]({{ "/assets/images/benchmark_image_104.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_105.png" | relative_url }})

#### 2D along well

```
Running simulation [simuapp]: SAGD

Elapsed: 5.11s

   148  17.2912  6   2526.000    12.47            119.30             90.54                     118.66    7.005    6.555   0.1058    1.726



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  4.874s  98.89%      

|- Newton                                 4.783s  |- 98.12%   

  |- Solver                               1.749s    |- 36.56% 

  |- Update                               0.927s    |- 19.38% 

  |- FluxJac                              0.743s    |- 15.53% 

  |- PerfJac                              0.446s    |- 9.33%  

  |- ScdAcc                               0.281s    |- 5.88%  

  |- Precond                              0.240s    |- 5.02%  

  |- update_dev                           0.175s    |- 3.66%  

  |- SanitizeJac                          0.075s    |- 1.56%  

  |- alignvar                             0.044s    |- 0.91%  

  |- Residual                             0.031s    |- 0.64%  

  |- HeatLoss                             0.007s    |- 0.14%  

|- Output                                 0.042s  |- 0.85%    

|- Logging                                0.031s  |- 0.63%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.055s  1.11%       

|- execution                              0.052s  |- 95.63%   

------------------------------------------------------------

TOTAL                                     4.929s

============================================================



Time steps : 148/158, step size: 17.0676, 33.3375

```

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_106.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_107.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_108.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_109.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_110.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_111.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_112.png" | relative_url }})

#### 3D

```
Running simulation [simuapp]: SAGD 3D

Elapsed: 32.81s

   152   4.8609  6    680.000    15.68            104.34             86.93                      95.24    1.103    2.751   0.1112    6.221



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 32.558s  99.84%      

|- Newton                                32.392s  |- 99.49%   

  |- Solver                              12.341s    |- 38.10% 

  |- FluxJac                              9.005s    |- 27.80% 

  |- Update                               6.235s    |- 19.25% 

  |- ScdAcc                               1.816s    |- 5.61%  

  |- update_dev                           1.062s    |- 3.28%  

  |- Precond                              0.804s    |- 2.48%  

  |- PerfJac                              0.382s    |- 1.18%  

  |- Residual                             0.206s    |- 0.64%  

  |- alignvar                             0.114s    |- 0.35%  

  |- SanitizeJac                          0.096s    |- 0.30%  

  |- HeatLoss                             0.085s    |- 0.26%  

|- Output                                 0.117s  |- 0.36%    

|- Logging                                0.019s  |- 0.06%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.053s  0.16%       

|- execution                              0.051s  |- 95.24%   

------------------------------------------------------------

TOTAL                                    32.611s

============================================================



Time steps : 152/156, step size: 4.47368, 3.96866

```

# Speed



`-DCMAKE_BUILD_TYPE=Release`

### Dome corner grid

```
Running simulation [simuapp]: Dome Corner point

Elapsed: 3.08s

    48  76.3132  1    365.000                                                                            0.032    0.033   0.0011   16.069



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.809s  97.37%      

|- Newton                                 2.792s  |- 99.39%   

  |- Solver                               1.113s    |- 39.86% 

  |- Update                               0.646s    |- 23.12% 

  |- FluxJac                              0.636s    |- 22.78% 

  |- ScdAcc                               0.150s    |- 5.38%  

  |- update_dev                           0.083s    |- 2.98%  

  |- Precond                              0.069s    |- 2.49%  

  |- Residual                             0.024s    |- 0.88%  

  |- HeatLoss                             0.016s    |- 0.58%  

  |- alignvar                             0.010s    |- 0.37%  

  |- SanitizeJac                          0.010s    |- 0.35%  

  |- PerfJac                              0.001s    |- 0.05%  

|- Logging                                0.007s  |- 0.26%    

|- Output                                 0.005s  |- 0.19%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.076s  2.63%       

|- execution                              0.067s  |- 88.49%   

------------------------------------------------------------

TOTAL                                     2.885s

============================================================



Time steps : 48/51, step size: 7.60417, 20.5374

```

```
Found 4 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu018_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_113.png" | relative_url }})

## Heterogeneous

### SPE10 benchmark 2D 

```
Running simulation [simuapp]: SPE10 benchmark 2D water flooding 375 days ~7s single thread (OMP_NUM_THREADS=8)

Elapsed: 10.28s

    90   0.7245  6    375.000    19.31             4e-04              0.00                      19.43    0.006    0.191   0.0151  5.6e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 10.012s  99.23%      

|- Newton                                 9.900s  |- 98.88%   

  |- FluxJac                              2.883s    |- 29.12% 

  |- Update                               2.737s    |- 27.65% 

  |- Solver                               2.076s    |- 20.97% 

  |- ScdAcc                               0.779s    |- 7.87%  

  |- update_dev                           0.463s    |- 4.67%  

  |- Precond                              0.335s    |- 3.38%  

  |- PerfJac                              0.260s    |- 2.62%  

  |- Residual                             0.124s    |- 1.26%  

  |- alignvar                             0.052s    |- 0.52%  

  |- SanitizeJac                          0.047s    |- 0.47%  

  |- HeatLoss                             0.021s    |- 0.21%  

|- Output                                 0.076s  |- 0.76%    

|- Logging                                0.008s  |- 0.08%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.078s  0.77%       

|- execution                              0.071s  |- 90.72%   

------------------------------------------------------------

TOTAL                                    10.090s

============================================================



Time steps : 90/90, step size: 4.16667, 2.86513

```

![png]({{ "/assets/images/benchmark_image_114.png" | relative_url }})

### Medium size



* 202,005 grid block (201x201x5) with heterogeneous permeability

* 61 wells water flooding pattern 

* 1500 days

```
Running simulation [simuapp]: Heterogeneous + 61wells - performance test medium size ~3m.50s (Single) (OMP_NUM_THREADS=8)

Elapsed: 340.76s

    32  22.4795  5    365.000   257.24              8.05              3.03                     720.00    0.002  111.711   0.0064    1.455



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                               5m 39.63s  99.79%      

|- Newton                              5m 38.09s  |- 99.54%   

  |- FluxJac                           1m 46.15s    |- 31.40% 

  |- Solver                            1m 32.14s    |- 27.25% 

  |- Update                            1m 17.84s    |- 23.02% 

  |- ScdAcc                              22.820s    |- 6.75%  

  |- update_dev                          12.934s    |- 3.83%  

  |- Precond                             10.941s    |- 3.24%  

  |- Residual                             4.028s    |- 1.19%  

  |- HeatLoss                             2.884s    |- 0.85%  

  |- PerfJac                              2.179s    |- 0.64%  

  |- alignvar                             1.001s    |- 0.30%  

  |- SanitizeJac                          0.614s    |- 0.18%  

|- Output                                 1.034s  |- 0.30%    

|- Logging                                0.018s  |- 0.01%    

|- Input                                  0.003s  |- 0.00%    

Initialization                            0.714s  0.21%       

|- execution                              0.571s  |- 79.99%   

------------------------------------------------------------

TOTAL                                  5m 40.35s

============================================================



Time steps : 32/32, step size: 11.4062, 13.2812

```

### Johnansen water flooding

```
Running simulation [simuapp]: Johnansen water flooding takes ~5m on M2 (OMP_NUM_THREADS=8)

Elapsed: 29.85s

    17 365.0000  1   3650.000   353.53              0.07              0.02                     188.86    0.000    3.269   0.0067  3.1e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 28.379s  96.61%      

|- Newton                                28.212s  |- 99.41%   

  |- Solver                               8.754s    |- 31.03% 

  |- FluxJac                              7.880s    |- 27.93% 

  |- Update                               7.411s    |- 26.27% 

  |- ScdAcc                               1.642s    |- 5.82%  

  |- update_dev                           0.841s    |- 2.98%  

  |- Precond                              0.809s    |- 2.87%  

  |- Residual                             0.367s    |- 1.30%  

  |- alignvar                             0.079s    |- 0.28%  

  |- SanitizeJac                          0.036s    |- 0.13%  

  |- PerfJac                              0.003s    |- 0.01%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.123s  |- 0.43%    

|- Logging                                0.002s  |- 0.01%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.995s  3.39%       

|- execution                              0.659s  |- 66.24%   

------------------------------------------------------------

TOTAL                                    29.374s

============================================================



Time steps : 17/17, step size: 214.706, 163.784

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data//stflu016_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_115.png" | relative_url }})

# MPI



`simumpi` runs the same deck domain-decomposed across MPI ranks (METIS partitioning, one rank per

subdomain) and rank 0 writes the whole reservoir's `<stem>.smy` - the same filename and the same

columns `simuapp` writes, with per-well and per-cell values reduced across ranks. That is what lets

every plot above read either engine's output, and what the two checks below compare.



Built only when `BUILD_MPI_SIMU=ON` (and never by the MSVC preset), so this section skips itself

when `simumpi` or `mpirun` is missing.


```
parity deck:  /Users/mark/Documents/workspace/hatch/app/build-release/test/data/spe04b.dat  ranks [1, 2, 4]

scaling deck: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/speed002.dat (exists: True)

scaling ranks: [1, 2, 4, 8]  (8 physical cores, 4 fast, 1 thread/rank, best of 2)

  heterogeneous CPU: np>4 spills onto the slower cores and is paced by them - see the scaling notes

simumpi available: True

```

```
Running simulation [simuapp]: MPI comparison baseline (OMP_NUM_THREADS=1)

Elapsed: 1.29s

    46  85.0883  5   3650.000     0.06              4.42             98.56                       4.57   10.346    5.911   0.0086    1.523



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.026s  93.44%      

|- Newton                                 1.007s  |- 98.19%   

  |- FluxJac                              0.419s    |- 41.55% 

  |- Update                               0.217s    |- 21.52% 

  |- Solver                               0.125s    |- 12.42% 

  |- ScdAcc                               0.105s    |- 10.47% 

  |- update_dev                           0.078s    |- 7.73%  

  |- PerfJac                              0.025s    |- 2.50%  

  |- Precond                              0.015s    |- 1.48%  

  |- alignvar                             0.005s    |- 0.50%  

  |- Residual                             0.004s    |- 0.43%  

  |- HeatLoss                             0.003s    |- 0.32%  

  |- SanitizeJac                          0.001s    |- 0.09%  

|- Output                                 0.012s  |- 1.21%    

|- Logging                                0.003s  |- 0.25%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.072s  6.56%       

|- execution                              0.069s  |- 95.47%   

------------------------------------------------------------

TOTAL                                     1.098s

============================================================



Time steps : 46/46, step size: 79.3478, 84.4867

Running simulation [simumpi]: MPI comparison np=1 (OMP_NUM_THREADS=1, np=1)

Elapsed: 1.41s

    27  42.9065  6   1065.356     2.17              6.06             73.66                       5.96    0.910   26.277   0.1832   51.430

    28  29.6443 11   1095.000     2.39              6.35             72.69                       5.96    0.913   41.870   0.1773   58.480

    29  31.6963  6   1126.696     2.05              5.71             73.56                       5.96    0.912   42.875   0.2260   20.753

    30  29.5042  6   1156.201     2.06              5.75             73.63                       5.96    0.911   32.692   0.1726   17.564



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    31  32.0094  6   1188.210     2.12              5.72             72.98                       5.96    0.909   17.230   0.1034   24.247

    32  44.2127  6   1232.423     2.17              5.62             72.15                       5.96    0.904   27.685   0.1552   31.974

    33  50.7098 11   1283.132     3.02              7.16             70.34                       5.98    0.957  193.205   0.2000   66.463

    34  50.7052  6   1333.838     3.01              6.89             69.60                       6.01    0.862   50.880   0.2011   60.837

    35  50.5426  6   1384.380     1.33              4.69             77.87                       5.96    0.861  198.034   0.1425   18.785

    36  60.4784  6   1444.859     0.88              4.42             83.39                       5.96    0.845  125.866   0.1618   25.629

    37  67.8886  6   1512.747     0.56              4.51             88.88                       5.96    0.829  112.264   0.1582   28.156

    38  77.0869  5   1589.834     0.44              4.53             91.12                       5.96    0.811  130.608   0.1590   28.037

    39  87.3149  6   1677.149     0.32              4.62             93.44                       5.96    0.793  169.194   0.1345   18.844

    40 107.4119  6   1784.561     0.21              4.72             95.70                       5.96    0.774  234.694   0.1201   19.749

    41 139.2014  5   1923.762     0.24              4.92             95.36                       5.96    0.754  314.821   0.1506   13.798

    42 162.0996  6   2085.862     0.15              4.74             96.85                       5.96    0.728  380.332   0.1037   20.660

    43 223.5990  5   2309.461     0.09              4.67             98.16                       5.96    0.693  591.456   0.0944   27.053

    44 296.0144  6   2605.475     0.06              4.49             98.69                       5.96    0.646  912.534   0.1686   27.551

    45 317.3500  7   2922.825     0.04              4.24             99.12                       5.96    0.614  1.1e+03   0.1585   45.034

    46 304.5413  6   3227.367     0.02              3.49             99.52                       5.96    0.617  1.4e+03   0.2315   43.877

    47 253.3296  6   3480.696     0.09              3.53             97.47                       4.99    0.590  523.034   0.1305    9.990

    48 169.3037  4   3650.000     0.09              4.16             97.84                       4.53    0.585   17.333   0.0264    3.691

Time steps : 48/48, step size: 76.0417, 78.3457

Running simulation [simumpi]: MPI comparison np=2 (OMP_NUM_THREADS=1, np=2)

Elapsed: 1.08s

=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    31  47.1917  9   1265.525     2.87              6.99             70.91                       5.96    1.857  186.106   0.1855   63.995

    32  49.2309  6   1314.756     3.06              6.87             69.22                       5.96    1.679   78.720   0.2480   62.360

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.0589377) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.0589377) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.127623) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.127623) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.00424974) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.00424974) - this cycle cannot be accepted as converged

    33  43.2948 14   1358.051     1.62              5.01             75.53                       5.96    1.664  174.717   0.2018   21.726

    34  37.1098  5   1395.161     1.08              4.47             80.51                       5.96    1.645   93.840   0.1213   13.312

    35  47.8786  6   1443.039     0.86              4.52             83.99                       5.96    1.622   80.700   0.1104   20.815

    36  64.3459  6   1507.385     0.55              4.41             88.86                       5.96    1.590  107.141   0.1517   26.182

    37  74.6368  5   1582.022     0.45              4.61             91.19                       5.96    1.559  126.726   0.1543   26.285

    38  85.8544  5   1667.877     0.33              4.65             93.33                       5.96    1.526  163.773   0.1259   20.356

    39 108.8990  5   1776.776     0.22              4.73             95.62                       5.96    1.489  236.671   0.1277   21.231

    40 137.2696  5   1914.045     0.24              4.93             95.35                       5.96    1.450  310.548   0.1534   13.114

    41 158.3343  6   2072.379     0.16              4.75             96.75                       5.96    1.402  369.664   0.1041   19.998

    42 218.0518  5   2290.431     0.09              4.67             98.12                       5.96    1.337  570.347   0.0822   28.027

    43 293.1978  6   2583.629     0.06              4.53             98.67                       5.96    1.250  898.762   0.1651   25.466

    44 316.9160  6   2900.545     0.04              4.24             99.09                       5.96    1.157  1.1e+03   0.1477   45.089

    45 306.7570  6   3207.302     0.02              3.55             99.49                       5.96    1.132  1.4e+03   0.2421   44.975

    46 257.0457  6   3464.348     0.09              3.45             97.53                       5.07    1.074  610.654   0.1415   10.741

    47 185.6522  4   3650.000     0.09              4.14             97.83                       4.51    1.065   21.403   0.0302    4.078

Time steps : 47/47, step size: 77.6596, 78.8507

Running simulation [simumpi]: MPI comparison np=4 (OMP_NUM_THREADS=1, np=4)

Elapsed: 1.29s

    33  44.4501  6   1217.869     2.54              6.19             70.88                       5.96    0.304   54.986   0.1899   29.395

    34  45.7671  6   1263.636     3.05              6.79             69.03                       5.96    0.331  157.269   0.1750   56.054

    35  49.2948  6   1312.931     2.37              5.79             70.99                       5.96    0.367   96.087   0.2241   51.209

    36  46.1215  6   1359.052     1.67              5.14             75.52                       5.96    0.367   99.940   0.1803   21.820

    37  48.8742  5   1407.926     1.22              4.76             79.61                       5.96    0.367   86.989   0.1304   20.082

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.122865) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.122865) - this cycle cannot be accepted as converged

[rank 3] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.122865) - this cycle cannot be accepted as converged

[rank 2] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.122865) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 1.48889e-05) - this cycle cannot be accepted as converged

[rank 3] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 1.48889e-05) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 1.48889e-05) - this cycle cannot be accepted as converged

[rank 2] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 1.48889e-05) - this cycle cannot be accepted as converged

    38  61.0060  7   1468.932     0.76              4.52             85.53                       5.96    0.367  128.212   0.1473   24.184

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.256138) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.256138) - this cycle cannot be accepted as converged

[rank 2] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.256138) - this cycle cannot be accepted as converged

[rank 3] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.256138) - this cycle cannot be accepted as converged

    39  71.8203  8   1540.753     0.48              4.44             90.31                       5.96    0.367  116.914   0.0904   25.970

    40 104.5480  5   1645.301     0.34              4.60             93.07                       5.96    0.367  193.696   0.1449   27.195

    41 124.0969  6   1769.397     0.20              4.66             95.98                       5.96    0.367  262.871   0.1268    9.965

    42 156.8925  6   1926.290     0.23              4.92             95.52                       5.96    0.367  342.441   0.1106   18.906

    43 210.7353  6   2137.025     0.12              4.72             97.58                       5.96    0.367  508.486   0.1159   27.041

    44 277.3702  6   2414.395     0.07              4.63             98.55                       5.96    0.367  800.351   0.1613   20.472

    45 311.8066  6   2726.202     0.04              4.39             99.00                       5.96    0.367  992.597   0.1203   43.678

    46 319.1451  6   3045.347     0.02              3.94             99.40                       5.96    0.368  1.3e+03   0.2108   47.640

    47 282.8357  6   3328.183     0.01              3.10             99.71                       5.83    0.368  1.3e+03   0.1899   15.973

    48 241.0539  6   3569.237     0.09              4.03             97.74                       4.55    0.368   48.486   0.0682    5.911

    49  80.7634  6   3650.000     0.09              4.36             98.06                       4.59    0.368    4.406   0.0112    1.609

Time steps : 49/50, step size: 74.4898, 81.0822

simuapp          rc=0   1.10s   46/ 46 steps  to  3650.00 days

simumpi np=1     rc=0   1.02s   48/ 48 steps,  0 cuts  to  3650.00 days

simumpi np=2     rc=0   0.80s   47/ 47 steps,  0 cuts  to  3650.00 days

simumpi np=4     rc=0   0.92s   49/ 50 steps,  1 cuts  to  3650.00 days

```

### Well curves against the CMG benchmark



The three wells of `spe04b.dat` are `INJECTOR`, `CRNR PRDCR` and `EDGE PRDCR` in deck order, and

that order is the trailing index on the `.smy`'s well columns - so `vratesc_aquatic0` is the

injector's water rate and `bhpres2` the edge producer's bottom-hole pressure. Each rank count is

drawn as its own marker series over CMG's history, so a rank that drifts shows up as markers

leaving the red curve.



Beyond one rank the two engines are not the same numerical method: the MPI linear solve is

preconditioned block by block (one ILU factor per rank, no cross-rank fill-in) where a single rank

is a global serial ILU. That shows up immediately as roundoff - np=2 leaves np=1 in the ninth

significant digit by the third step - and the adaptive timestep controller then amplifies it into

a different `dt` sequence. So the marker series do not share x positions, and each rank count

reaches the same 3650 days over its own step sequence (49 steps at np=1, 50 at np=2, 48 at

np=4). Every rank count does reach it; the endpoint column in the table above is the check

that they did.



Read the well kinds differently. Rates respond to a constraint switch: a well that switches at a

slightly different time shows a step offset while the rest of the curve still tracks CMG. BHP is

the smoother signal and the better place to see a trajectory genuinely diverging. All three wells'

BHP moving off CMG together points at the trajectory; one well's rate alone points at that well's

constraint timing.


![png]({{ "/assets/images/benchmark_image_116.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_117.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_118.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_119.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_120.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_121.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_122.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_123.png" | relative_url }})

### Cyclic steam stimulation across rank counts



`stflu008.dat` is the second parity deck, in a different numerical regime: thermal cyclic steam

stimulation on a 15x15x4 = 900 cell grid, against `spe04b.dat`'s black oil. It is worth sweeping

because a steam front carries a sharp viscosity contrast - 487 cp at 125 F to 2.5 cp at 450 F -

and the `isfinite` guards that recover degenerate cell states after a steam cycle act on each

rank's own subdomain, so a partition boundary cutting across the front is where a rank would drift.



The two series are the ones the serial comparison cell above plots: the injector's water rate and

the producer's oil rate, both at standard conditions, with CMG's history as the benchmark line and

each rank count as its own markers.


```
Running simulation [simuapp]: CSS parity baseline (OMP_NUM_THREADS=1)

Elapsed: 24.77s

   150  36.8637  6   1095.000     1.59              1.13             41.52                               0.071   21.341   0.0648    2.486



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 24.428s  99.70%      

|- Newton                                24.319s  |- 99.56%   

  |- FluxJac                             11.993s    |- 49.32% 

  |- Update                               5.503s    |- 22.63% 

  |- ScdAcc                               2.461s    |- 10.12% 

  |- Solver                               1.738s    |- 7.15%  

  |- update_dev                           1.615s    |- 6.64%  

  |- Precond                              0.438s    |- 1.80%  

  |- alignvar                             0.124s    |- 0.51%  

  |- PerfJac                              0.114s    |- 0.47%  

  |- Residual                             0.099s    |- 0.41%  

  |- HeatLoss                             0.086s    |- 0.35%  

  |- SanitizeJac                          0.025s    |- 0.10%  

|- Output                                 0.088s  |- 0.36%    

|- Logging                                0.011s  |- 0.04%    

|- Input                                  0.001s  |- 0.00%    

Initialization                            0.073s  0.30%       

|- execution                              0.070s  |- 96.19%   

------------------------------------------------------------

TOTAL                                    24.501s

============================================================



Time steps : 150/161, step size: 7.3, 16.8364

Running simulation [simumpi]: CSS parity np=1 (OMP_NUM_THREADS=1, np=1)

Elapsed: 20.28s

   114   1.5784  6    740.000                                                                  158.99    0.466  234.639   0.1281   33.157

   115   7.0000  6    747.000                                                                            0.466  1.2e+03   0.1535   29.604

   116   0.3333  5 1  747.333                     113.87            100.00                               0.466  761.287   0.0313   30.020

   117   0.4480  7    747.781     0.88            112.12             99.22                               0.467  375.772   0.1607   22.283

   118   0.5047  6    748.286     2.41             85.60             97.26                               0.467  161.153   0.1272    6.740

   119   0.6372  6    748.923     4.28             65.79             93.89                               0.468  139.346   0.1524    5.615

   120   0.7376  6    749.661     5.92             51.62             89.71                               0.468  116.904   0.1800    4.734



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   121   0.7822  6    750.443     9.83             40.10             80.31                               0.464   96.273   0.1209    3.724

   122   1.0105  6    751.454     9.48             35.10             78.74                               0.463   97.693   0.0381    3.853

   123   1.8803  6    753.334     9.39             28.71             75.35                               0.463  136.749   0.4728    5.564

   124   1.0567  6    754.391     8.69             26.87             75.56                               0.464   66.167   0.0185    2.703

   125   2.1135  6    756.504     8.07             23.10             74.12                               0.464  101.322   0.0231    4.530

   126   4.2269  6    760.731     6.99             18.06             72.11                               0.465  142.817   0.0443    6.705

   127   7.6127  5    768.344     5.55             12.92             69.96                               0.466  167.842   0.1130    9.054

   128  10.1312  8    778.475     4.39              9.64             68.71                               0.467  131.490   0.1324    8.671

   129  12.5586  6    791.033     3.64              7.40             67.03                               0.468  100.320   0.0407    8.312

   130  23.0485  6    814.082     2.82              5.06             64.22                               0.469  105.971   0.0924   10.771

   131  33.2811  6    847.363     2.38              3.64             60.48                               0.471   81.614   0.0838   10.301

   132  49.8297  6    897.193     2.04              2.64             56.47                               0.472   67.827   0.1322    9.129

   133  61.7968  6    958.990     1.95              1.98             50.37                               0.473   54.040   0.0911    7.042

   134  89.6974  6   1048.687     1.70              1.37             44.59                               0.475   58.034   0.1153    7.196

   135  46.3129  6   1095.000     1.62              1.13             41.13                               0.475   26.689   0.0666    3.135

Time steps : 135/141, step size: 8.11111, 17.5876

Running simulation [simumpi]: CSS parity np=2 (OMP_NUM_THREADS=1, np=2)

Elapsed: 13.12s

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 12.5646) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 12.5646) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.36371) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.36371) - this cycle cannot be accepted as converged

   111   7.0000  7    747.000                                                                            0.838  1.2e+03   0.1534   29.636

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.226291) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.226291) - this cycle cannot be accepted as converged

   112   1.0000  6    748.000     3.25             93.76             96.65                               0.833  1.1e+03   0.0708   45.313

   113   1.1501  6    749.150     5.52             66.01             92.28                               0.834  239.931   0.1751   12.392

   114   1.2381  6    750.388     7.86             47.60             85.83                               0.835  162.609   0.0642    6.730

   115   2.0233  6    752.411     9.11             34.74             79.22                               0.837  172.027   0.1923    7.001

   116   2.0686  6    754.480     8.85             28.05             76.02                               0.838  132.542   0.0221    5.632

   117   4.1373  6    758.617     7.78             21.02             72.99                               0.839  172.305   0.0402    7.928

   118   7.6116  6    766.229     6.11             14.55             70.43                               0.842  196.159   0.1094    9.937

   119  10.2683  5    776.497     4.61             10.27             69.03                               0.844  156.266   0.1552    9.754

   120  11.7760  6    788.273     3.81              8.06             67.89                               0.845  107.621   0.0485    8.388



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   121  20.7686  6    809.042     3.05              5.57             64.60                               0.848  108.558   0.0747   10.586

   122  32.3486  6    841.390     2.44              3.88             61.40                               0.850   90.050   0.0857   10.954

   123  48.0423  6    889.433     2.10              2.79             57.05                               0.853   72.070   0.1369    9.684

   124  58.6067  6    948.039     2.02              2.09             50.93                               0.855   54.012   0.1017    7.047

   125  81.4978  6   1029.537     1.77              1.47             45.34                               0.858   56.576   0.1214    7.030

   126  65.4629  6   1095.000     1.67              1.15             40.79                               0.859   38.286   0.0745    4.451

Time steps : 126/129, step size: 8.69048, 18.3764

Running simulation [simumpi]: CSS parity np=4 (OMP_NUM_THREADS=1, np=4)

Elapsed: 12.03s

   122   1.4731  6    739.304                                                                  158.99    0.220  226.632   0.1176   28.866

   123   0.6962  6    740.000                                                                  158.99    0.219  116.843   0.0842   15.023

[rank 3] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 21.9023) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 21.9023) - this cycle cannot be accepted as converged

[rank 2] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 21.9023) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 21.9023) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.46058) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.46058) - this cycle cannot be accepted as converged

[rank 2] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.46058) - this cycle cannot be accepted as converged

[rank 3] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.46058) - this cycle cannot be accepted as converged

   124   7.0000  6    747.000                                                                            0.219  1.2e+03   0.1566   29.648

[rank 3] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.124789) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.124789) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.124789) - this cycle cannot be accepted as converged

[rank 2] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.124789) - this cycle cannot be accepted as converged

   125   1.0000  6    748.000     5.88             90.23             93.88                               0.207  1.1e+03   0.1855   45.092

   126   1.0431  6    749.043     4.96             68.42             93.23                               0.207  225.146   0.0727   12.369

   127   1.6393  6    750.682     7.78             45.72             85.45                               0.208  202.192   0.0524    8.271

   128   2.8352  6    753.518     8.73             31.58             78.33                               0.208  208.299   0.1595    8.661

   129   3.2063  6    756.724     8.13             24.21             74.87                               0.209  163.754   0.0261    7.180

   130   6.3736  6    763.097     6.78             17.11             71.62                               0.209  192.636   0.0697    9.383

   131  10.1514  6    773.249     5.09             11.58             69.48                               0.210  183.881   0.1638   10.812

   132  11.3233  6    784.572     4.06              8.78             68.37                               0.210  119.862   0.0355    8.676

   133  21.3626  6    805.935     3.22              5.99             65.03                               0.211  122.352   0.0601   11.513

   134  35.5823  7    841.517     2.50              3.95             61.23                               0.211  103.220   0.1103   12.249

   135  47.8420  8    889.359     2.14              2.86             57.28                               0.212   73.626   0.1449    9.810

   136  56.7862  6    946.145     2.05              2.17             51.40                               0.213   53.950   0.1068    6.927

   137  77.4004  6   1023.546     1.82              1.51             45.30                               0.213   55.566   0.1136    6.867

   138  71.4543  6   1095.000     1.68              1.18             41.13                               0.214   42.574   0.0720    4.892

Time steps : 138/148, step size: 7.93478, 17.5006

simuapp          rc=0  24.50s  150/161 steps  to  1095.00 days

simumpi np=1     rc=0  19.95s  135/141 steps,  6 cuts  to  1095.00 days

simumpi np=2     rc=0  12.82s  126/129 steps,  3 cuts  to  1095.00 days

simumpi np=4     rc=0  11.67s  138/148 steps, 10 cuts  to  1095.00 days

```

![png]({{ "/assets/images/benchmark_image_124.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_125.png" | relative_url }})

### Wall-clock scaling



Measured on `speed002.dat` (201x201x5 = 202,005 cells), not on the parity deck above: the two

questions need different decks, and asking this one of 180 cells can only ever answer "no". The

timings come from each engine's own closing report rather than from wall clock, so mpirun's

fork/exec and PETSc's initialization are not charged to the curve, and every rank count is timed

over the same number of marched steps (`SCALING_MAXSTEPS`) rather than over its own `dt` sequence.



The sweep runs `SCALING_RANK_SWEEP` - powers of two up to the machine's **physical** core count,

not `MPI_RANK_SWEEP`'s 1/2/4. Parity is answered by a few rank counts; scaling is not, because

what changes past np=4 is not the arithmetic per rank but the cost of coordinating ranks, and a

sweep that stops at 4 cannot see it. Both panels below are plotted against the same sweep:



- **left, seconds** - the quantity actually measured. The `simuapp` line is the serial engine on

  the same deck and the same step budget, which is the only honest reference for "is this worth

  running at all".

- **right, speedup and efficiency** - derived. Speedup is against `simumpi` at np=1, not against

  `simuapp`: same binary, same code path, so the ratio isolates decomposition rather than mixing

  in the serial/distributed differences (global ILU vs. block Jacobi, among others). Efficiency

  is that speedup over the ideal, and is the number that says when adding ranks has stopped

  paying.



Four things decide whether these numbers mean anything, and all four have bitten:



- **Deck size.** At np=4 the parity deck gives each rank ~45 cells - a few milliseconds of

  arithmetic per step against MPI collectives that cost the same regardless. The speedup there is

  below 1 and says nothing about the decomposition. The `cells/rank` and `ghosts` columns below

  come from the real partition rather than from the deck's grid dimensions, and are printed for

  exactly this reason: once a rank holds only a few hundred cells, read the row as noise.

- **Threads per rank.** `USE_OPENMP=ON` plus an unset `OMP_NUM_THREADS` means every rank opens a

  whole machine's worth of OpenMP threads; np=4 then oversubscribes the box fourfold. On an

  8-core machine that alone took np=4 from 3.3x down to 1.6x. `MPI_OMP_THREADS` pins it, and the

  sweep's physical-core ceiling keeps `ranks x threads` inside the machine.

- **Measurement noise.** On a desktop this deck has come back anywhere from 32s to 72s for the

  identical run. Each configuration is timed `SCALING_REPEATS` times and the minimum kept - noise

  only adds time, so the fastest sample is the least contaminated. Treat a few percent between

  adjacent rank counts as nothing.

- **Cores that are not all the same speed.** Apple Silicon packages performance and efficiency

  cores together - an M2 is 4 P + 4 E, and an E core is roughly a third of a P core. MPI is

  bulk-synchronous, so every collective waits on the slowest rank and the whole run is paced by

  whichever cores the sweep spilled onto. Measured on this deck on an M2 over two sweeps: np=4

  lands at 3.3-3.5x and ~85% efficiency, np=8 only at 4.0-4.4x and ~50% - but np=4 -> np=8

  gaining 1.2x for twice the ranks is almost exactly what 4 P + 4 E predicts (4 + 4/3 effective

  cores is 1.33x, less the halo growing from 4,235 to 8,325 ghosts). The spread between those

  two sweeps is also the honest width of any single number here. The shaded region and the `*`

  in the table below mark those rows; the clean part of the curve ends at the fast-core count.



The sweep stops at the physical core count. Going further needs `mpirun --oversubscribe`, which

puts two ranks on one core - that measures contention, not decomposition, and cannot support a

scaling claim. On this M2 that makes np=8 the ceiling and np=4 the last fully meaningful point.



The linear solve is a real distributed `KSPSolve` over a `MATMPIAIJ` (`SolverPetscMPI`) - each rank

assembles and owns its own rows, with nothing gathered to rank 0 - and on this deck it is only

~9% of Newton's time anyway. The flux Jacobian and the property update are the ~70% that

decomposition actually has to carry. Ghost exchange is no longer on the list of things that grow

with rank count: `DistributedGhostCellSync` is neighbor-to-neighbor over a halo map resolved once

at startup, so nothing in the per-Newton-iteration refresh scales with the global cell count.


```
Running simulation [simuapp]: scaling baseline (attempt 1/2) (OMP_NUM_THREADS=1)

Elapsed: 38.13s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 36.808s  97.55%      

|- Newton                                36.648s  |- 99.57%   

  |- FluxJac                             15.574s    |- 42.50% 

  |- Update                              10.888s    |- 29.71% 

  |- ScdAcc                               3.441s    |- 9.39%  

  |- Solver                               3.050s    |- 8.32%  

  |- update_dev                           2.174s    |- 5.93%  

  |- Precond                              0.611s    |- 1.67%  

  |- Residual                             0.218s    |- 0.60%  

  |- alignvar                             0.178s    |- 0.49%  

  |- HeatLoss                             0.102s    |- 0.28%  

  |- PerfJac                              0.082s    |- 0.22%  

  |- SanitizeJac                          0.052s    |- 0.14%  

|- Output                                 0.093s  |- 0.25%    

|- Logging                                0.001s  |- 0.00%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.926s  2.45%       

|- execution                              0.770s  |- 83.13%   

------------------------------------------------------------

TOTAL                                    37.734s

============================================================



Time steps : 4/4, step size: 0.12948, 0.0270322

Running simulation [simuapp]: scaling baseline (attempt 2/2) (OMP_NUM_THREADS=1)

Elapsed: 38.55s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 37.450s  97.86%      

|- Newton                                37.308s  |- 99.62%   

  |- FluxJac                             15.930s    |- 42.70% 

  |- Update                              10.975s    |- 29.42% 

  |- ScdAcc                               3.513s    |- 9.41%  

  |- Solver                               3.114s    |- 8.35%  

  |- update_dev                           2.228s    |- 5.97%  

  |- Precond                              0.644s    |- 1.73%  

  |- Residual                             0.220s    |- 0.59%  

  |- alignvar                             0.183s    |- 0.49%  

  |- HeatLoss                             0.111s    |- 0.30%  

  |- PerfJac                              0.086s    |- 0.23%  

  |- SanitizeJac                          0.059s    |- 0.16%  

|- Output                                 0.080s  |- 0.21%    

|- Logging                                0.001s  |- 0.00%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.819s  2.14%       

|- execution                              0.690s  |- 84.25%   

------------------------------------------------------------

TOTAL                                    38.269s

============================================================



Time steps : 4/4, step size: 0.12948, 0.0270322

Running simulation [simumpi]: scaling np=1 (attempt 1/2) (OMP_NUM_THREADS=1, np=1)

Elapsed: 43.41s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-28







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.260   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     720.00    0.000  358.615   0.0032    0.123

     3   0.1391  2      0.356   426.16             27.46              6.05                     720.00    0.000  375.796   0.0037    0.139

     4   0.1621  3      0.518   376.48             25.97              6.45                     720.00    0.000  339.799   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129461, 0.0270304

Running simulation [simumpi]: scaling np=1 (attempt 2/2) (OMP_NUM_THREADS=1, np=1)

Elapsed: 43.74s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-28







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.260   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     720.00    0.000  358.615   0.0032    0.123

     3   0.1391  2      0.356   426.16             27.46              6.05                     720.00    0.000  375.796   0.0037    0.139

     4   0.1621  3      0.518   376.48             25.97              6.45                     720.00    0.000  339.799   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129461, 0.0270304

Running simulation [simumpi]: scaling np=2 (attempt 1/2) (OMP_NUM_THREADS=1, np=2)

Elapsed: 25.21s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-28







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.308   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     720.00    0.000  358.575   0.0032    0.123

     3   0.1391  2      0.356   426.16             27.46              6.05                     720.00    0.000  375.794   0.0037    0.139

     4   0.1621  3      0.518   376.49             25.97              6.45                     720.00    0.000  339.800   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129459, 0.0270309

Running simulation [simumpi]: scaling np=2 (attempt 2/2) (OMP_NUM_THREADS=1, np=2)

Elapsed: 25.06s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-28







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.308   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     720.00    0.000  358.575   0.0032    0.123

     3   0.1391  2      0.356   426.16             27.46              6.05                     720.00    0.000  375.794   0.0037    0.139

     4   0.1621  3      0.518   376.49             25.97              6.45                     720.00    0.000  339.800   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129459, 0.0270309

Running simulation [simumpi]: scaling np=4 (attempt 1/2) (OMP_NUM_THREADS=1, np=4)

Elapsed: 17.97s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-28







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.259   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     720.00    0.000  358.613   0.0032    0.123

     3   0.1391  2      0.356   426.16             27.46              6.05                     720.00    0.000  375.796   0.0037    0.139

     4   0.1621  3      0.518   376.48             25.97              6.45                     720.00    0.000  339.799   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129461, 0.0270305

Running simulation [simumpi]: scaling np=4 (attempt 2/2) (OMP_NUM_THREADS=1, np=4)

Elapsed: 17.97s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-28







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.259   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     720.00    0.000  358.613   0.0032    0.123

     3   0.1391  2      0.356   426.16             27.46              6.05                     720.00    0.000  375.796   0.0037    0.139

     4   0.1621  3      0.518   376.48             25.97              6.45                     720.00    0.000  339.799   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129461, 0.0270305

Running simulation [simumpi]: scaling np=8 (attempt 1/2) (OMP_NUM_THREADS=1, np=8)

Elapsed: 15.20s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-28







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.274   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     719.99    0.000  358.634   0.0032    0.123

     3   0.1391  2      0.356   426.17             27.46              6.05                     720.00    0.000  375.776   0.0037    0.139

     4   0.1621  3      0.518   376.49             25.97              6.45                     720.00    0.000  339.792   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129458, 0.0270287

Running simulation [simumpi]: scaling np=8 (attempt 2/2) (OMP_NUM_THREADS=1, np=8)

Elapsed: 18.67s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-28







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.274   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     719.99    0.000  358.634   0.0032    0.123

     3   0.1391  2      0.356   426.17             27.46              6.05                     720.00    0.000  375.776   0.0037    0.139

     4   0.1621  3      0.518   376.49             25.97              6.45                     720.00    0.000  339.792   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129458, 0.0270287

```

![png]({{ "/assets/images/benchmark_image_126.png" | relative_url }})

```
   config  steps   seconds   speedup   effic.  cells/rank   ghosts

  simuapp      4     37.73         -        -           -        -

     np=1      4     41.57     1.00x     100%      202005        0

     np=2      4     23.31     1.78x      89%      101080     2110

     np=4      4     16.18     2.57x      64%       50520     4235

     np=8      4     12.98     3.20x      40%       25610     8325 *

  * more ranks than the 4 fast cores on this CPU - paced by the slow ones, so read the efficiency as the machine's, not the partition's

```

```
Script completed at: 2026-10-28 11:33:39

```
