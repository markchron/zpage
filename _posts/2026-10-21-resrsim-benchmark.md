---
layout: default
title: "Benchmark results of resrsim"
date: 2026-10-21
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

Elapsed: 0.65s

    24  55.0000  1   3650.000    47.19              1.86              3.80                      30.06    0.000   39.479 4.29e-04    0.029



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.266s  69.81%      

|- Newton                                 0.238s  |- 89.70%   

  |- Update                               0.094s    |- 39.48% 

  |- FluxJac                              0.054s    |- 22.52% 

  |- ScdAcc                               0.027s    |- 11.26% 

  |- Solver                               0.024s    |- 9.90%  

  |- update_dev                           0.012s    |- 4.85%  

  |- Precond                              0.011s    |- 4.70%  

  |- Residual                             0.006s    |- 2.44%  

  |- SanitizeJac                          0.002s    |- 0.79%  

  |- alignvar                             0.001s    |- 0.62%  

  |- PerfJac                              0.001s    |- 0.61%  

  |- HeatLoss                             0.001s    |- 0.31%  

|- Output                                 0.016s  |- 6.04%    

|- Logging                                0.001s  |- 0.38%    

|- Input                                  0.000s  |- 0.04%    

Initialization                            0.115s  30.19%      

|- execution                              0.100s  |- 87.25%   

------------------------------------------------------------

TOTAL                                     0.380s

============================================================



Time steps : 24/24, step size: 152.083, 111.804

```

```
Found 25 VTU files

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

Elapsed: 0.89s

    83 141.8617  1   3650.000     0.01              4.11             99.74                       4.63    0.786   30.085   0.0340    2.929



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.659s  91.54%      

|- Newton                                 0.622s  |- 94.44%   

  |- Update                               0.162s    |- 26.00% 

  |- FluxJac                              0.158s    |- 25.36% 

  |- Solver                               0.100s    |- 16.15% 

  |- ScdAcc                               0.058s    |- 9.25%  

  |- Precond                              0.045s    |- 7.19%  

  |- update_dev                           0.038s    |- 6.04%  

  |- PerfJac                              0.022s    |- 3.61%  

  |- SanitizeJac                          0.013s    |- 2.04%  

  |- alignvar                             0.007s    |- 1.20%  

  |- Residual                             0.005s    |- 0.75%  

  |- HeatLoss                             0.003s    |- 0.49%  

|- Output                                 0.024s  |- 3.64%    

|- Logging                                0.005s  |- 0.70%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.061s  8.46%       

|- execution                              0.058s  |- 95.08%   

------------------------------------------------------------

TOTAL                                     0.720s

============================================================



Time steps : 83/84, step size: 43.9759, 51.037

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

Elapsed: 0.81s

    85 121.7872  1   3650.000     0.07              3.90             98.21                       5.96    1.148  220.631   0.0484    4.238



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.573s  90.33%      

|- Newton                                 0.538s  |- 93.97%   

  |- Update                               0.159s    |- 29.58% 

  |- FluxJac                              0.125s    |- 23.15% 

  |- Solver                               0.082s    |- 15.18% 

  |- ScdAcc                               0.051s    |- 9.43%  

  |- Precond                              0.036s    |- 6.62%  

  |- update_dev                           0.034s    |- 6.24%  

  |- PerfJac                              0.020s    |- 3.66%  

  |- SanitizeJac                          0.010s    |- 1.80%  

  |- alignvar                             0.007s    |- 1.24%  

  |- Residual                             0.004s    |- 0.81%  

  |- HeatLoss                             0.003s    |- 0.53%  

|- Output                                 0.022s  |- 3.79%    

|- Logging                                0.003s  |- 0.59%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.061s  9.67%       

|- execution                              0.059s  |- 95.61%   

------------------------------------------------------------

TOTAL                                     0.634s

============================================================



Time steps : 85/87, step size: 42.9412, 58.7001

```

![png]({{ "/assets/images/benchmark_image_36.png" | relative_url }})

# Buckley- Leverett



Two phase, isothermal problem

variable order: [Sw, P, T, So, X0, X1, Sg]



Acc w.r.t. [Sw, So, Sg, X0, X1, P, T]

```
Running simulation [simuapp]: Buckley-Leverett

Elapsed: 0.63s

    78   5.6285  4     10.000                       0.16            100.00                       0.16   21.543    0.009 1.34e-05  6.5e-06



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.383s  87.67%      

|- Newton                                 0.360s  |- 94.17%   

  |- Update                               0.120s    |- 33.22% 

  |- FluxJac                              0.056s    |- 15.57% 

  |- ScdAcc                               0.043s    |- 12.04% 

  |- Solver                               0.041s    |- 11.42% 

  |- Precond                              0.029s    |- 8.02%  

  |- update_dev                           0.024s    |- 6.73%  

  |- PerfJac                              0.017s    |- 4.69%  

  |- SanitizeJac                          0.008s    |- 2.26%  

  |- alignvar                             0.006s    |- 1.67%  

  |- HeatLoss                             0.005s    |- 1.33%  

  |- Residual                             0.004s    |- 1.12%  

|- Output                                 0.015s  |- 3.97%    

|- Logging                                0.002s  |- 0.62%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.054s  12.33%      

|- execution                              0.051s  |- 95.52%   

------------------------------------------------------------

TOTAL                                     0.436s

============================================================



Time steps : 78/80, step size: 0.128205, 0.6966

```

### Load Benchmark

### Buckley Plot

![png]({{ "/assets/images/benchmark_image_37.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_38.png" | relative_url }})

# MISC

## spe04b_cw.dat

```
Running simulation [simuapp]: SPE4-b water flooding

Elapsed: 0.45s

    30 137.9736  1   3650.000     0.78             10.17             92.91                      10.73    1.070   10.692   0.0100    0.002



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.217s  78.35%      

|- Newton                                 0.203s  |- 93.55%   

  |- Update                               0.070s    |- 34.68% 

  |- FluxJac                              0.059s    |- 28.99% 

  |- Solver                               0.026s    |- 12.65% 

  |- ScdAcc                               0.017s    |- 8.35%  

  |- Precond                              0.010s    |- 4.91%  

  |- update_dev                           0.009s    |- 4.51%  

  |- PerfJac                              0.003s    |- 1.30%  

  |- Residual                             0.002s    |- 1.23%  

  |- SanitizeJac                          0.002s    |- 1.07%  

  |- alignvar                             0.002s    |- 0.79%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.010s  |- 4.54%    

|- Logging                                0.001s  |- 0.35%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.060s  21.65%      

|- execution                              0.057s  |- 95.58%   

------------------------------------------------------------

TOTAL                                     0.277s

============================================================



Time steps : 30/30, step size: 121.667, 136.9

```



## watfld_cw.dat

```
Running simulation [simuapp]: SPE4-b Water flooding without vmod

Elapsed: 0.57s

    37 117.4106  1   3650.000     1.04             78.98             98.70                      80.00    3.284    6.279   0.0108    0.001



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.333s  83.42%      

|- Newton                                 0.315s  |- 94.58%   

  |- Update                               0.101s    |- 31.96% 

  |- FluxJac                              0.088s    |- 27.97% 

  |- Solver                               0.044s    |- 13.86% 

  |- ScdAcc                               0.026s    |- 8.14%  

  |- Precond                              0.015s    |- 4.75%  

  |- PerfJac                              0.014s    |- 4.58%  

  |- update_dev                           0.013s    |- 4.25%  

  |- Residual                             0.004s    |- 1.13%  

  |- SanitizeJac                          0.003s    |- 1.06%  

  |- alignvar                             0.003s    |- 0.80%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.011s  |- 3.32%    

|- Logging                                0.001s  |- 0.37%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.066s  16.58%      

|- execution                              0.064s  |- 96.37%   

------------------------------------------------------------

TOTAL                                     0.399s

============================================================



Time steps : 37/37, step size: 98.6486, 133.593

```

## stflu001.dat

Inverted 9 spot water flooding with area/block modifier, 5 point transmissibility


```
Running simulation [simuapp]: Inverted 9 spot water flooding

Elapsed: 1.34s

   186   7.9802  1   3650.000     0.52            139.26             99.63                     139.63   36.893   33.161   0.1333   22.500



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.108s  94.55%      

|- Newton                                 1.048s  |- 94.63%   

  |- Update                               0.304s    |- 29.04% 

  |- FluxJac                              0.300s    |- 28.60% 

  |- ScdAcc                               0.118s    |- 11.25% 

  |- Precond                              0.103s    |- 9.85%  

  |- update_dev                           0.078s    |- 7.43%  

  |- Solver                               0.067s    |- 6.41%  

  |- SanitizeJac                          0.020s    |- 1.91%  

  |- alignvar                             0.014s    |- 1.36%  

  |- PerfJac                              0.013s    |- 1.23%  

  |- Residual                             0.009s    |- 0.82%  

  |- HeatLoss                             0.006s    |- 0.54%  

|- Output                                 0.041s  |- 3.74%    

|- Logging                                0.010s  |- 0.87%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.064s  5.45%       

|- execution                              0.061s  |- 95.95%   

------------------------------------------------------------

TOTAL                                     1.172s

============================================================



Time steps : 186/194, step size: 19.6237, 59.6502

```

## stflu002.dat

5000x5000x50, 2D diagonal water flooding in uniformed cartesian

```
Running simulation [simuapp]: Uniformed cartesian water flooding

Elapsed: 0.63s

    90 113.4862  2   3650.000   626.19              8.89              1.40                     635.79    0.456  372.182   0.0171    0.009



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.416s  89.67%      

|- Newton                                 0.389s  |- 93.52%   

  |- Update                               0.115s    |- 29.57% 

  |- FluxJac                              0.088s    |- 22.66% 

  |- Solver                               0.062s    |- 15.99% 

  |- ScdAcc                               0.035s    |- 8.97%  

  |- Precond                              0.027s    |- 7.01%  

  |- update_dev                           0.019s    |- 4.90%  

  |- PerfJac                              0.015s    |- 3.74%  

  |- SanitizeJac                          0.008s    |- 1.99%  

  |- alignvar                             0.005s    |- 1.33%  

  |- HeatLoss                             0.004s    |- 1.04%  

  |- Residual                             0.004s    |- 0.97%  

|- Output                                 0.018s  |- 4.21%    

|- Logging                                0.003s  |- 0.64%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.048s  10.33%      

|- execution                              0.046s  |- 95.03%   

------------------------------------------------------------

TOTAL                                     0.464s

============================================================



Time steps : 90/90, step size: 40.5556, 66.7849

```



## stflu003.dat

5000x5000x50, 2D diagonal water flooding in uniformed corner point

```
Running simulation [simuapp]: uniformed corner grid

Elapsed: 0.53s

    62  80.2045  2   3650.000   624.88             10.10              1.59                     635.81    0.436  237.218   0.0120    0.006



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.287s  78.93%      

|- Newton                                 0.269s  |- 93.75%   

  |- Update                               0.082s    |- 30.27% 

  |- FluxJac                              0.057s    |- 20.97% 

  |- Solver                               0.045s    |- 16.71% 

  |- ScdAcc                               0.025s    |- 9.30%  

  |- Precond                              0.017s    |- 6.29%  

  |- update_dev                           0.017s    |- 6.17%  

  |- PerfJac                              0.010s    |- 3.65%  

  |- SanitizeJac                          0.005s    |- 1.70%  

  |- alignvar                             0.004s    |- 1.33%  

  |- HeatLoss                             0.003s    |- 1.00%  

  |- Residual                             0.002s    |- 0.92%  

|- Output                                 0.012s  |- 4.08%    

|- Logging                                0.002s  |- 0.57%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.077s  21.07%      

|- execution                              0.074s  |- 96.09%   

------------------------------------------------------------

TOTAL                                     0.364s

============================================================



Time steps : 62/62, step size: 58.871, 90.1875

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

Elapsed: 0.60s

    62 147.0960  1   3650.000   634.83              0.94              0.15                     635.95   57.689  375.000   0.0380    0.020



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.372s  87.36%      

|- Newton                                 0.350s  |- 94.02%   

  |- Update                               0.142s    |- 40.75% 

  |- FluxJac                              0.068s    |- 19.39% 

  |- Solver                               0.050s    |- 14.23% 

  |- ScdAcc                               0.029s    |- 8.41%  

  |- Precond                              0.016s    |- 4.68%  

  |- update_dev                           0.015s    |- 4.35%  

  |- PerfJac                              0.006s    |- 1.83%  

  |- SanitizeJac                          0.004s    |- 1.18%  

  |- Residual                             0.004s    |- 1.16%  

  |- HeatLoss                             0.004s    |- 1.14%  

  |- alignvar                             0.004s    |- 1.03%  

|- Output                                 0.016s  |- 4.18%    

|- Logging                                0.002s  |- 0.41%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.054s  12.64%      

|- execution                              0.051s  |- 94.14%   

------------------------------------------------------------

TOTAL                                     0.426s

============================================================



Time steps : 62/62, step size: 58.871, 106.169

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

Elapsed: 2.87s

   119 107.7825  3   3650.000   625.95              8.49              1.34                     635.95    0.460  426.485   0.0229    0.018



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.626s  97.30%      

|- Newton                                 2.572s  |- 97.96%   

  |- Solver                               0.869s    |- 33.76% 

  |- FluxJac                              0.719s    |- 27.96% 

  |- Update                               0.541s    |- 21.04% 

  |- ScdAcc                               0.147s    |- 5.70%  

  |- Precond                              0.087s    |- 3.40%  

  |- update_dev                           0.079s    |- 3.06%  

  |- HeatLoss                             0.025s    |- 0.98%  

  |- Residual                             0.021s    |- 0.82%  

  |- PerfJac                              0.020s    |- 0.77%  

  |- SanitizeJac                          0.020s    |- 0.76%  

  |- alignvar                             0.015s    |- 0.60%  

|- Output                                 0.036s  |- 1.37%    

|- Logging                                0.008s  |- 0.29%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.073s  2.70%       

|- execution                              0.059s  |- 80.58%   

------------------------------------------------------------

TOTAL                                     2.699s

============================================================



Time steps : 119/119, step size: 30.6723, 55.3696

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

Elapsed: 2.27s

   121   7.0479  6   3650.000     0.00              4.15             99.95                       4.36    2.041    5.093   0.0025    0.162



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.034s  97.13%      

|- Newton                                 1.981s  |- 97.39%   

  |- Solver                               0.615s    |- 31.07% 

  |- FluxJac                              0.424s    |- 21.43% 

  |- Update                               0.405s    |- 20.46% 

  |- ScdAcc                               0.170s    |- 8.60%  

  |- Precond                              0.140s    |- 7.05%  

  |- update_dev                           0.092s    |- 4.62%  

  |- PerfJac                              0.041s    |- 2.05%  

  |- SanitizeJac                          0.031s    |- 1.58%  

  |- alignvar                             0.020s    |- 0.99%  

  |- Residual                             0.010s    |- 0.49%  

  |- HeatLoss                             0.009s    |- 0.45%  

|- Output                                 0.034s  |- 1.69%    

|- Logging                                0.009s  |- 0.44%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.060s  2.87%       

|- execution                              0.057s  |- 95.66%   

------------------------------------------------------------

TOTAL                                     2.094s

============================================================



Time steps : 121/131, step size: 30.1653, 41.8375

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

Elapsed: 0.79s

   147  52.2476  1   1095.000     0.80              0.19             19.40                               1.168    5.244   0.0888    1.583



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.549s  89.43%      

|- Newton                                 0.493s  |- 89.87%   

  |- Update                               0.154s    |- 31.21% 

  |- FluxJac                              0.089s    |- 18.08% 

  |- Precond                              0.056s    |- 11.43% 

  |- ScdAcc                               0.045s    |- 9.22%  

  |- PerfJac                              0.042s    |- 8.43%  

  |- Solver                               0.030s    |- 5.99%  

  |- update_dev                           0.029s    |- 5.88%  

  |- SanitizeJac                          0.018s    |- 3.69%  

  |- alignvar                             0.010s    |- 1.96%  

  |- Residual                             0.003s    |- 0.71%  

  |- HeatLoss                             0.002s    |- 0.42%  

|- Output                                 0.036s  |- 6.60%    

|- Logging                                0.008s  |- 1.48%    

|- Input                                  0.001s  |- 0.17%    

Initialization                            0.065s  10.57%      

|- execution                              0.062s  |- 96.37%   

------------------------------------------------------------

TOTAL                                     0.614s

============================================================



Time steps : 147/151, step size: 7.44898, 16.9265

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

Elapsed: 5.96s

   212  53.2157  1   1095.000     2.55              1.86             42.21                               7.744   14.055   0.1228    2.304



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  5.726s  99.01%      

|- Newton                                 5.578s  |- 97.41%   

  |- FluxJac                              1.684s    |- 30.19% 

  |- Update                               1.539s    |- 27.60% 

  |- Solver                               1.209s    |- 21.67% 

  |- ScdAcc                               0.417s    |- 7.48%  

  |- update_dev                           0.226s    |- 4.05%  

  |- Precond                              0.199s    |- 3.57%  

  |- PerfJac                              0.057s    |- 1.03%  

  |- Residual                             0.057s    |- 1.02%  

  |- HeatLoss                             0.041s    |- 0.73%  

  |- SanitizeJac                          0.038s    |- 0.67%  

  |- alignvar                             0.033s    |- 0.59%  

|- Output                                 0.108s  |- 1.88%    

|- Logging                                0.021s  |- 0.37%    

|- Input                                  0.001s  |- 0.02%    

Initialization                            0.057s  0.99%       

|- execution                              0.055s  |- 95.41%   

------------------------------------------------------------

TOTAL                                     5.783s

============================================================



Time steps : 212/213, step size: 5.16509, 14.034

```

```
Found 213 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu008_00212.vtu

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

Elapsed: 6.19s

    77  27.5021  1   1095.000     0.70              0.04              4.92                               0.758    3.473 5.72e-04    0.623



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  5.917s  98.34%      

|- Newton                                 5.788s  |- 97.82%   

  |- FluxJac                              1.976s    |- 34.14% 

  |- Update                               1.627s    |- 28.12% 

  |- Solver                               1.292s    |- 22.33% 

  |- ScdAcc                               0.358s    |- 6.18%  

  |- update_dev                           0.184s    |- 3.18%  

  |- Precond                              0.158s    |- 2.73%  

  |- Residual                             0.062s    |- 1.08%  

  |- alignvar                             0.020s    |- 0.35%  

  |- HeatLoss                             0.020s    |- 0.35%  

  |- SanitizeJac                          0.019s    |- 0.33%  

  |- PerfJac                              0.002s    |- 0.04%  

|- Output                                 0.106s  |- 1.79%    

|- Logging                                0.005s  |- 0.08%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.100s  1.66%       

|- execution                              0.069s  |- 68.94%   

------------------------------------------------------------

TOTAL                                     6.017s

============================================================



Time steps : 77/77, step size: 14.2208, 25.9287

```

```
Found 78 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu009_00077.vtu

```

![png]({{ "/assets/images/benchmark_image_99.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_100.png" | relative_url }})

### stflu009_graded.dat - near-well-refined PEBI (the real PEBI-vs-Cartesian parity case)



`stflu009_graded.dat` is the PEBI companion the note above asks for: a *graded* honeycomb whose

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

| `stflu009_graded.dat` | graded PEBI | refined toward ~3 ft near the well |


```
Running simulation [simuapp]: Cyclic steam stimulation in graded Pebi-grid

Elapsed: 10.45s

   329  77.9588  6   1095.000     2.41              1.78             42.45                               6.593   35.984   0.1621    6.791



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 10.161s  99.01%      

|- Newton                                 9.882s  |- 97.25%   

  |- FluxJac                              3.059s    |- 30.95% 

  |- Solver                               2.623s    |- 26.54% 

  |- Update                               2.494s    |- 25.24% 

  |- ScdAcc                               0.594s    |- 6.01%  

  |- Precond                              0.345s    |- 3.49%  

  |- update_dev                           0.324s    |- 3.28%  

  |- Residual                             0.089s    |- 0.91%  

  |- PerfJac                              0.087s    |- 0.88%  

  |- SanitizeJac                          0.065s    |- 0.65%  

  |- alignvar                             0.055s    |- 0.56%  

  |- HeatLoss                             0.035s    |- 0.35%  

|- Output                                 0.218s  |- 2.14%    

|- Logging                                0.021s  |- 0.21%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.102s  0.99%       

|- execution                              0.086s  |- 84.26%   

------------------------------------------------------------

TOTAL                                    10.263s

============================================================



Time steps : 329/336, step size: 3.32827, 10.4836

```

```
Found 330 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu009_graded_00329.vtu

```

![png]({{ "/assets/images/benchmark_image_101.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_102.png" | relative_url }})

### stflu010.dat 

incomp gas

```
Running simulation [simuapp]: Incomp GAS

Elapsed: 3.19s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.938s  97.83%      

|- Newton                                 2.890s  |- 98.36%   

  |- Solver                               0.789s    |- 27.29% 

  |- Update                               0.670s    |- 23.19% 

  |- FluxJac                              0.532s    |- 18.40% 

  |- Precond                              0.302s    |- 10.45% 

  |- ScdAcc                               0.277s    |- 9.57%  

  |- update_dev                           0.133s    |- 4.62%  

  |- SanitizeJac                          0.074s    |- 2.56%  

  |- alignvar                             0.044s    |- 1.52%  

  |- Residual                             0.014s    |- 0.50%  

  |- PerfJac                              0.008s    |- 0.27%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.033s  |- 1.14%    

|- Logging                                0.019s  |- 0.63%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.065s  2.17%       

|- execution                              0.061s  |- 93.47%   

------------------------------------------------------------

TOTAL                                     3.004s

============================================================



Time steps : 130/171, step size: 4.56091e-05, 2.87034e-05

```

![png]({{ "/assets/images/benchmark_image_103.png" | relative_url }})

### SAGD

#### 2D cross the well

```
Running simulation [simuapp]: SAGD

Elapsed: 2.83s

   216   6.3788  1   2526.000     5.48             54.38             90.84                      53.66    0.357    3.439   0.1358    5.309



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.605s  97.94%      

|- Newton                                 2.496s  |- 95.85%   

  |- Update                               0.658s    |- 26.34% 

  |- Solver                               0.582s    |- 23.33% 

  |- FluxJac                              0.574s    |- 22.97% 

  |- ScdAcc                               0.217s    |- 8.69%  

  |- update_dev                           0.159s    |- 6.38%  

  |- Precond                              0.137s    |- 5.50%  

  |- SanitizeJac                          0.039s    |- 1.58%  

  |- alignvar                             0.028s    |- 1.14%  

  |- Residual                             0.027s    |- 1.08%  

  |- PerfJac                              0.026s    |- 1.02%  

  |- HeatLoss                             0.004s    |- 0.14%  

|- Output                                 0.080s  |- 3.08%    

|- Logging                                0.016s  |- 0.60%    

|- Input                                  0.001s  |- 0.02%    

Initialization                            0.055s  2.06%       

|- execution                              0.052s  |- 94.55%   

------------------------------------------------------------

TOTAL                                     2.659s

============================================================



Time steps : 216/221, step size: 11.6944, 13.0005

```

![png]({{ "/assets/images/benchmark_image_104.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_105.png" | relative_url }})

#### 2D along well

```
Running simulation [simuapp]: SAGD

Elapsed: 2.89s

   134  11.8536  1   2526.000    14.85            120.86             89.06                     128.23    1.746    1.705   0.0873    2.060



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.638s  98.00%      

|- Newton                                 2.573s  |- 97.54%   

  |- Solver                               0.958s    |- 37.25% 

  |- Update                               0.519s    |- 20.18% 

  |- FluxJac                              0.407s    |- 15.83% 

  |- PerfJac                              0.228s    |- 8.85%  

  |- ScdAcc                               0.153s    |- 5.93%  

  |- Precond                              0.113s    |- 4.40%  

  |- update_dev                           0.090s    |- 3.49%  

  |- SanitizeJac                          0.035s    |- 1.35%  

  |- alignvar                             0.023s    |- 0.88%  

  |- Residual                             0.016s    |- 0.63%  

  |- HeatLoss                             0.003s    |- 0.12%  

|- Output                                 0.038s  |- 1.45%    

|- Logging                                0.008s  |- 0.30%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.054s  2.00%       

|- execution                              0.051s  |- 95.20%   

------------------------------------------------------------

TOTAL                                     2.692s

============================================================



Time steps : 134/143, step size: 18.8507, 30.6056

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

Elapsed: 16.84s

   176   6.1174  1    680.000    11.62             89.75             88.53                      97.95    1.086    4.311   0.0909    9.386



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 16.601s  99.60%      

|- Newton                                16.413s  |- 98.87%   

  |- Solver                               6.088s    |- 37.09% 

  |- FluxJac                              4.457s    |- 27.16% 

  |- Update                               3.369s    |- 20.53% 

  |- ScdAcc                               0.891s    |- 5.43%  

  |- update_dev                           0.501s    |- 3.05%  

  |- Precond                              0.411s    |- 2.51%  

  |- PerfJac                              0.250s    |- 1.52%  

  |- Residual                             0.122s    |- 0.74%  

  |- alignvar                             0.057s    |- 0.35%  

  |- SanitizeJac                          0.051s    |- 0.31%  

  |- HeatLoss                             0.042s    |- 0.25%  

|- Output                                 0.125s  |- 0.75%    

|- Logging                                0.048s  |- 0.29%    

|- Input                                  0.001s  |- 0.00%    

Initialization                            0.066s  0.40%       

|- execution                              0.063s  |- 95.65%   

------------------------------------------------------------

TOTAL                                    16.667s

============================================================



Time steps : 176/182, step size: 3.86364, 3.29238

```

# Speed



`-DCMAKE_BUILD_TYPE=Release`

### Dome corner grid

```
Running simulation [simuapp]: Dome Corner point

Elapsed: 20.40s

    63   9.3301  1    365.000    59.46            294.92             83.22                              10.540  375.000   0.0011    0.025



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 20.116s  99.55%      

|- Newton                                20.096s  |- 99.90%   

  |- Solver                              14.045s    |- 69.89% 

  |- FluxJac                              2.424s    |- 12.06% 

  |- Update                               2.074s    |- 10.32% 

  |- ScdAcc                               0.606s    |- 3.02%  

  |- update_dev                           0.326s    |- 1.62%  

  |- Precond                              0.275s    |- 1.37%  

  |- Residual                             0.077s    |- 0.38%  

  |- HeatLoss                             0.066s    |- 0.33%  

  |- SanitizeJac                          0.060s    |- 0.30%  

  |- alignvar                             0.042s    |- 0.21%  

  |- PerfJac                              0.002s    |- 0.01%  

|- Logging                                0.015s  |- 0.07%    

|- Output                                 0.006s  |- 0.03%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.090s  0.45%       

|- execution                              0.082s  |- 90.64%   

------------------------------------------------------------

TOTAL                                    20.206s

============================================================



Time steps : 63/75, step size: 5.79365, 11.7164

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

Elapsed: 3.29s

    91   8.1262  1    375.000    19.28              0.00              0.02                      19.45    3.641    1.979   0.2000    0.006



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  3.038s  97.58%      

|- Newton                                 2.930s  |- 96.46%   

  |- Update                               0.894s    |- 30.50% 

  |- FluxJac                              0.749s    |- 25.56% 

  |- Solver                               0.666s    |- 22.73% 

  |- ScdAcc                               0.221s    |- 7.56%  

  |- update_dev                           0.115s    |- 3.92%  

  |- Precond                              0.083s    |- 2.82%  

  |- PerfJac                              0.081s    |- 2.76%  

  |- Residual                             0.042s    |- 1.43%  

  |- alignvar                             0.014s    |- 0.47%  

  |- SanitizeJac                          0.012s    |- 0.41%  

  |- HeatLoss                             0.005s    |- 0.19%  

|- Output                                 0.070s  |- 2.32%    

|- Logging                                0.004s  |- 0.15%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.075s  2.42%       

|- execution                              0.067s  |- 89.27%   

------------------------------------------------------------

TOTAL                                     3.113s

============================================================



Time steps : 91/92, step size: 4.12088, 2.73231

```

![png]({{ "/assets/images/benchmark_image_114.png" | relative_url }})

### Medium size



* 202,005 grid block (201x201x5) with heterogeneous permeability

* 61 wells water flooding pattern 

* 1500 days

```
Running simulation [simuapp]: Heterogeneous + 61wells - performance test medium size ~3m.50s (Single) (OMP_NUM_THREADS=8)

Elapsed: 113.90s

    40   5.8771  1    365.000   259.21              0.00              0.00                     719.92    0.009  288.207   0.0737    0.385



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                               1m 52.86s  99.40%      

|- Newton                              1m 51.68s  |- 98.96%   

  |- Update                              32.397s    |- 29.01% 

  |- FluxJac                             31.314s    |- 28.04% 

  |- Solver                              28.903s    |- 25.88% 

  |- ScdAcc                               6.903s    |- 6.18%  

  |- update_dev                           3.950s    |- 3.54%  

  |- Precond                              2.931s    |- 2.62%  

  |- Residual                             1.673s    |- 1.50%  

  |- HeatLoss                             0.704s    |- 0.63%  

  |- PerfJac                              0.546s    |- 0.49%  

  |- alignvar                             0.376s    |- 0.34%  

  |- SanitizeJac                          0.190s    |- 0.17%  

|- Output                                 0.774s  |- 0.69%    

|- Logging                                0.008s  |- 0.01%    

|- Input                                  0.003s  |- 0.00%    

Initialization                            0.682s  0.60%       

|- execution                              0.545s  |- 79.87%   

------------------------------------------------------------

TOTAL                                  1m 53.54s

============================================================



Time steps : 40/40, step size: 9.125, 8.58057

```

### Johnansen water flooding

```
Running simulation [simuapp]: Johnansen water flooding takes ~5m on M2 (OMP_NUM_THREADS=8)

Elapsed: 22.59s

    17 365.0000  1   3650.000   353.53              0.07              0.02                     188.86    0.000    3.269   0.0067  3.1e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 21.153s  95.47%      

|- Newton                                21.022s  |- 99.38%   

  |- Solver                               6.503s    |- 30.94% 

  |- Update                               6.214s    |- 29.56% 

  |- FluxJac                              5.359s    |- 25.49% 

  |- ScdAcc                               1.170s    |- 5.56%  

  |- update_dev                           0.681s    |- 3.24%  

  |- Precond                              0.476s    |- 2.26%  

  |- Residual                             0.257s    |- 1.22%  

  |- alignvar                             0.067s    |- 0.32%  

  |- SanitizeJac                          0.030s    |- 0.14%  

  |- PerfJac                              0.002s    |- 0.01%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.095s  |- 0.45%    

|- Logging                                0.001s  |- 0.01%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            1.004s  4.53%       

|- execution                              0.686s  |- 68.37%   

------------------------------------------------------------

TOTAL                                    22.157s

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

Elapsed: 1.13s

    83 141.8617  1   3650.000     0.01              4.11             99.74                       4.63    0.786   30.085   0.0340    2.929



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.898s  94.45%      

|- Newton                                 0.865s  |- 96.22%   

  |- FluxJac                              0.348s    |- 40.30% 

  |- Update                               0.208s    |- 24.03% 

  |- Solver                               0.099s    |- 11.47% 

  |- ScdAcc                               0.087s    |- 10.03% 

  |- update_dev                           0.064s    |- 7.45%  

  |- PerfJac                              0.022s    |- 2.53%  

  |- Precond                              0.013s    |- 1.46%  

  |- Residual                             0.004s    |- 0.51%  

  |- alignvar                             0.004s    |- 0.47%  

  |- HeatLoss                             0.003s    |- 0.31%  

  |- SanitizeJac                          0.001s    |- 0.10%  

|- Output                                 0.023s  |- 2.54%    

|- Logging                                0.004s  |- 0.48%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.053s  5.55%       

|- execution                              0.050s  |- 95.23%   

------------------------------------------------------------

TOTAL                                     0.951s

============================================================



Time steps : 83/84, step size: 43.9759, 51.037

Running simulation [simumpi]: MPI comparison np=1 (OMP_NUM_THREADS=1, np=1)

Elapsed: 1.43s

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  31.0005  9   1181.958     2.18              6.22             74.03                       5.96    0.356   31.570   0.2059   57.471

    62  20.3514  5   1202.309     2.02              5.87             74.37                       5.96    0.356   29.357   0.1391   15.793

    63  24.6375  5   1226.946     1.84              5.68             75.51                       5.96    0.355   29.151   0.1399   23.249

    64  28.2733  4   1255.220     1.64              5.40             76.68                       5.96    0.354   35.723   0.1015   21.559

    65  33.6901  6   1288.910     1.46              5.15             77.92                       5.96    0.352   36.032   0.1627   30.368

    66  33.4556  5   1322.366     1.35              5.13             79.20                       5.96    0.349   44.998   0.1694   20.002

    67  36.6609  4   1359.026     1.23              4.99             80.28                       5.96    0.346   52.236   0.0965   31.666

    68  35.5333  4   1394.560     1.14              5.15             81.86                       5.96    0.344   54.734   0.1551   21.853

    69  40.7585  3   1435.318     1.00              5.28             84.04                       5.96    0.341   53.365   0.1625   16.569

    70  45.6550  5   1480.973     0.77              5.09             86.78                       5.96    0.333   67.700   0.1310   19.396

    71  56.8734  3   1537.847     0.71              4.99             87.49                       5.96    0.332   84.941   0.1257   17.804

    72  72.2053  2   1610.052     0.59              4.96             89.30                       5.96    0.373  116.304   0.1316   12.350

    73  89.7393  2   1699.791     0.49              4.99             91.06                       5.96    0.366  155.321   0.0861   12.328

    74 133.0489  2   1832.840     0.36              4.92             93.14                       5.96    0.350  252.954   0.1056    9.384

    75 182.1837  5   2015.024     0.25              4.83             95.05                       5.96    0.334  398.211   0.0844   12.332

    76 206.1673  3   2221.191     0.17              4.72             96.54                       5.96    0.314  503.682   0.1073   13.372

    77 205.3035  4   2426.495     0.11              4.54             97.62                       5.96    0.257  562.555   0.0857   11.998

    78 191.6054  2   2618.100     0.07              4.38             98.37                       5.96    0.224  586.523   0.0385   10.684

    79 174.3638  2   2792.464     0.05              4.18             98.84                       5.96    0.201  579.076   0.0324    9.220

    80 159.9120  2   2952.376     0.03              3.99             99.16                       5.96    0.184  568.227   0.0273    8.096

    81 148.3450  3   3100.721     0.02              3.65             99.40                       5.96    0.167  589.309   0.0706    7.601

    82 134.6060  1   3235.327     0.02              3.95             99.54                       5.96    0.037  437.692   0.0253    5.392

    83 144.9261  3   3380.253     0.01              3.01             99.69                       5.96    0.038  739.318   0.0656    8.006

    84 113.8009  5   3494.054     0.01              3.33             99.74                       5.17    0.038  279.576   0.0363    3.930

    85 155.9461  1   3650.000     0.01              4.18             99.74                       4.59    0.044   25.061   0.0275    2.972

Time steps : 85/86, step size: 42.9412, 51.7447

Running simulation [simumpi]: MPI comparison np=2 (OMP_NUM_THREADS=1, np=2)

Elapsed: 0.86s

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  27.9525  3   1122.952     1.92              5.73             74.93                       5.96    0.085   18.169   0.1102   21.178

    62  33.5983  3   1156.551     2.01              6.05             75.08                       5.96    0.085   25.574   0.1237   35.070

    63  30.6392  7   1187.190     2.13              6.29             74.66                       5.96    0.144   22.639   0.2133   53.608

    64  21.1354  6   1208.325     2.02              5.80             74.16                       5.96    0.144   23.413   0.1403   26.234

    65  22.7685  4   1231.094     1.68              5.49             76.59                       5.96    0.144   47.518   0.1485   14.297

    66  26.7005  4   1257.794     1.62              5.35             76.75                       5.96    0.144   33.984   0.1210   20.758

    67  32.4049  6   1290.199     1.47              5.11             77.72                       5.96    0.144   36.306   0.1668   29.070

    68  32.9890  6   1323.188     1.34              5.13             79.24                       5.96    0.144   47.793   0.1704   21.072

    69  36.0363  4   1359.225     1.21              4.96             80.43                       5.96    0.144   57.617   0.1168   28.414

    70  37.1588  4   1396.383     1.13              5.19             82.07                       5.96    0.144   56.678   0.1475   21.526

    71  43.7196  4   1440.103     0.99              5.30             84.26                       5.96    0.144   56.034   0.1639   19.145

    72  48.7495  3   1488.853     0.78              6.10             88.67                       5.96    1.201   77.255   0.1411   22.061

    73  57.4353  3   1546.288     0.70              5.06             87.88                       5.96    1.189   86.147   0.1126   14.132

    74  76.5572  2   1622.845     0.57              4.99             89.81                       5.96    1.043  124.386   0.1264   13.247

    75  96.9417  2   1719.787     0.47              5.00             91.46                       5.96    1.040  170.066   0.1363   11.416

    76 118.4974  2   1838.284     0.36              4.90             93.21                       5.96    0.979  226.083   0.0982    8.250

    77 167.1070  4   2005.391     0.26              4.83             94.98                       5.96    0.949  362.679   0.0833   11.266

    78 198.2146  3   2203.606     0.17              4.73             96.46                       5.96    0.910  482.668   0.1093   13.731

    79 202.2202  4   2405.826     0.11              4.55             97.54                       5.96    0.891  547.863   0.0904   11.876

    80 191.7323  2   2597.558     0.08              4.40             98.32                       5.96    0.870  580.332   0.0386   10.743

    81 175.6099  2   2773.168     0.05              4.20             98.82                       5.96    0.843  577.716   0.0329    9.330

    82 161.2848  2   2934.453     0.03              4.01             99.14                       5.96    0.816  568.848   0.0269    8.204

    83 149.5200  3   3083.973     0.02              3.67             99.39                       5.96    0.784  591.263   0.0740    7.706

    84 135.3979  1   3219.371     0.02              3.97             99.53                       5.96    0.908  435.810   0.0261    5.423

    85 146.1169  3   3365.488     0.01              3.06             99.69                       5.96    0.867  737.172   0.0673    8.051

    86 114.9573  5   3480.445     0.01              3.20             99.74                       5.29    0.842  343.680   0.0334    4.286

    87 139.9617  1   3620.407     0.01              4.11             99.74                       4.64    0.875   28.077   0.0322    2.957

    88  29.5932  1   3650.000     0.01              4.15             99.74                       4.67    0.832    2.749   0.0435    0.463

Time steps : 88/89, step size: 41.4773, 49.9087

Running simulation [simumpi]: MPI comparison np=4 (OMP_NUM_THREADS=1, np=4)

Elapsed: 0.94s

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  23.1126  4   1132.620     1.97              5.85             74.85                       5.96    1.008   23.459   0.1030   17.887

    62  30.0444  3   1162.665     2.05              6.08             74.73                       5.96    1.007   18.792   0.0939   29.265

    63  30.4710  9   1193.136     2.16              6.09             73.84                       5.96    1.052   31.783   0.1896   53.225

    64  21.1256  5   1214.261     1.87              5.65             75.13                       5.96    1.051   27.123   0.1303   19.228

    65  26.3811  4   1240.642     1.60              5.40             77.10                       5.96    1.049   31.866   0.1091   17.777

    66  34.3868  4   1275.029     1.49              5.23             77.86                       5.96    1.043   36.933   0.1341   30.233

    67  34.2347  1   1309.264     1.35              5.22             79.39                       5.96    1.025   26.421   0.1624   23.374

    68  38.3581  5   1347.622     1.18              4.93             80.64                       5.96    1.017   73.936   0.2193   31.685

    69  36.3572  4   1383.979     1.16              5.09             81.44                       5.96    1.011   48.730   0.1128   37.066

    70  32.0444  3   1416.024     1.01              5.24             83.84                       5.96    0.985   49.618   0.1692   10.529

    71  35.1382  2   1451.162     0.86              5.15             85.75                       5.96    0.978   45.806   0.0893   15.531

    72  48.5062  3   1499.668     0.79              5.08             86.47                       5.96    0.970   68.970   0.1167   23.855

    73  54.9366  2   1554.605     0.71              5.03             87.68                       5.96    0.969   82.217   0.1386   14.072

    74  66.6152  2   1621.220     0.58              4.99             89.65                       5.96    1.097  107.220   0.1086   11.759

    75  90.1726  2   1711.392     0.48              4.99             91.24                       5.96    1.068  156.133   0.0733   13.528

    76 131.4008  3   1842.793     0.36              4.90             93.12                       5.96    1.028  254.840   0.1003    9.334

    77 182.5476  3   2025.341     0.25              4.83             95.05                       5.96    0.980  400.487   0.0799   12.309

    78 205.9726  4   2231.313     0.17              4.65             96.53                       5.96    1.220  504.230   0.1155   12.776

    79 204.9816  3   2436.295     0.11              4.52             97.61                       5.96    1.110  562.939   0.0853   11.941

    80 191.2266  2   2627.522     0.07              4.37             98.36                       5.96    1.041  587.936   0.0380   10.646

    81 173.7636  2   2801.285     0.05              4.17             98.84                       5.96    0.981  578.527   0.0326    9.168

    82 159.4535  2   2960.739     0.03              3.98             99.15                       5.96    0.930  567.908   0.0273    8.059

    83 147.9697  3   3108.708     0.02              3.64             99.40                       5.96    0.879  588.788   0.0691    7.569

    84 134.3381  1   3243.047     0.02              3.95             99.53                       5.96    0.674  438.267   0.0252    5.381

    85 144.5354  3   3387.582     0.01              3.00             99.69                       5.96    0.634  740.326   0.0651    7.995

    86 113.3916  4   3500.974     0.01              3.47             99.73                       5.16    0.624  256.984   0.0369    3.793

    87 149.0264  1   3650.000     0.01              4.14             99.73                       4.58    0.586   25.060   0.0468    2.847

Time steps : 87/88, step size: 41.954, 51.0671

simuapp          rc=0   0.95s   83/ 84 steps  to  3650.00 days

simumpi np=1     rc=0   0.95s   85/ 86 steps,  1 cuts  to  3650.00 days

simumpi np=2     rc=0   0.60s   88/ 89 steps,  1 cuts  to  3650.00 days

simumpi np=4     rc=0   0.66s   87/ 88 steps,  1 cuts  to  3650.00 days

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

Elapsed: 10.90s

   212  53.2157  1   1095.000     2.55              1.86             42.21                               7.744   14.055   0.1228    2.304



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 10.673s  99.50%      

|- Newton                                10.518s  |- 98.55%   

  |- FluxJac                              4.492s    |- 42.71% 

  |- Update                               2.804s    |- 26.66% 

  |- Solver                               1.147s    |- 10.91% 

  |- ScdAcc                               0.979s    |- 9.30%  

  |- update_dev                           0.646s    |- 6.14%  

  |- Precond                              0.179s    |- 1.70%  

  |- PerfJac                              0.056s    |- 0.53%  

  |- Residual                             0.053s    |- 0.51%  

  |- alignvar                             0.051s    |- 0.48%  

  |- HeatLoss                             0.035s    |- 0.34%  

  |- SanitizeJac                          0.011s    |- 0.10%  

|- Output                                 0.128s  |- 1.20%    

|- Logging                                0.009s  |- 0.09%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.053s  0.50%       

|- execution                              0.051s  |- 95.89%   

------------------------------------------------------------

TOTAL                                    10.726s

============================================================



Time steps : 212/213, step size: 5.16509, 14.034

Running simulation [simumpi]: CSS parity np=1 (OMP_NUM_THREADS=1, np=1)

Elapsed: 4.17s

    51   0.4823  1      9.969                                                                  158.97    0.376  132.082   0.2910   12.753

    52   0.0310  1     10.000                                                                  158.96    0.377  370.136   0.0842    6.687

[rank 0] linear solve did not converge: DIVERGED_ITS after 150 iterations (residual norm 8.33381) - this cycle cannot be accepted as converged

    53   7.0000  6     17.000                                                                            0.379  1.5e+03   0.1615   49.384

    54   1.0000  5     18.000                                                                            0.593  1.2e+03   0.1247   30.756

    55   0.5437  5     18.544    20.74             80.23             79.46                               0.587  264.331   0.1593   29.726

    56   0.1822  1 1   18.726    13.83            381.87             96.50                               0.437   72.577   0.2000    7.351

    57   0.0607  3 1   18.787    11.25             96.34             89.54                               0.435  217.298   0.0788   14.900

    58   0.0852  1     18.872    16.39            141.75             89.63                               0.416  115.099   0.2000    6.348

    59   0.0852  1     18.957                                                                            0.437  444.339   0.2224   34.326

    60   0.0788  1     19.036     0.11              5.03             97.83                               0.436   67.686   0.2624   10.087



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61   0.0668  1     19.103     1.50             49.65             97.06                               0.430   84.051   0.1418    7.486

    62   0.0267 14 1   19.129                                                                            0.437  174.323   0.2357  1.0e+03

    63 1.36e-03  2     19.131                                                                            0.442   23.681   0.1197  446.207

    64 1.52e-04  1     19.131                                                                            4.715    3.476   0.1340  1.5e+03

    65 5.25e-06  1     19.131                                                                            0.439    0.026   0.0288    0.001

    66 1.03e-05  1     19.131                                                                            6.618   19.174   0.0841  1.5e+03





TimeLoop terminates due to: time step too small





Time steps : 66/69, step size: 0.289863, 0.865151

Running simulation [simumpi]: CSS parity np=2 (OMP_NUM_THREADS=1, np=2)

Elapsed: 7.80s

   231   0.4921  1    750.214     6.38             60.63             90.48                               3.566   54.489   0.1851    2.277

   232   0.5141  1    750.729    17.99             53.45             74.82                               3.594  109.789   0.2667    9.462

   233   0.4317  1    751.160    10.99             46.41             80.85                               3.597   90.070   0.0761    7.353

   234   0.6684  1    751.829     9.24             41.31             81.72                               3.599   62.089   0.0338    4.674

   235   1.2725  1    753.101     9.00             35.16             79.61                               3.604   96.366   0.0168    3.683

   236   2.3622  1    755.463     8.62             28.35             76.68                               3.612  134.428   0.0543    5.018

   237   4.0474  1    759.511     7.97             21.73             73.17                               3.624  148.933   0.2763    5.934

   238   3.3231  1    762.834     7.40             18.41             71.33                               3.630   99.807   0.1413    5.976

   239   3.9927  1    766.826     6.61             15.32             69.86                               3.636   94.769   0.0272    4.756

   240   7.4368  1    774.263     5.57             11.84             68.00                               3.648  121.295   0.0884    6.420



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   241  10.9174  1    785.181     4.48              9.00             66.74                               3.659  113.277   0.0946    7.265

   242  15.6222  1    800.803     3.98              8.09             67.05                               3.846   31.722   0.2820    3.632

   243  12.6563  1    813.459     3.62              6.58             64.50                               3.846   79.818   0.3039   10.402

   244   9.7590  1    823.218     3.55              6.23             63.71                               3.940   18.354   0.1049    2.435

   245  13.4019  1    836.620     3.49              5.94             63.00                               4.080   14.714   0.1048    1.714

   246  18.4119  1    855.032     3.46              5.82             62.72                               4.308    7.926   0.1008    0.969

   247  25.6909  1    880.723     3.07              4.38             58.79                               4.323   78.768   0.1221   13.664

   248  33.0469  2    913.770     2.79              3.31             54.29                               4.332   63.137   0.1123   10.130

   249  44.0971  1    957.867     2.52              3.07             54.98                               4.567   13.234   0.1039    1.678

   250  60.7808  3   1018.648     2.36              2.53             51.72                               4.714   40.524   0.1516    5.513

   251  70.5310  3   1089.179     2.47              2.03             45.03                               4.827   47.777   0.1233    6.972

   252   5.8213  1   1095.000     2.32              1.61             40.93                               4.828   12.869   0.1103    1.658

Time steps : 252/253, step size: 4.34524, 11.3491

Running simulation [simumpi]: CSS parity np=4 (OMP_NUM_THREADS=1, np=4)

Elapsed: 7.36s

[rank 2] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 1.40396) - this cycle cannot be accepted as converged

   178   1.0000  7    748.000     2.38            107.90             97.84                               1.617  1.1e+03   0.0658   47.831

   179   0.5857  1    748.586     3.22             82.84             96.26                               1.622  153.319   0.0274    5.899

   180   0.9700  1    749.556     5.58             61.16             91.64                               1.632  158.638   0.0339    6.193



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   181   1.5904  1    751.146     5.83             59.76             91.11                               1.835   20.289   0.3172    3.185

   182   1.1913  1    752.337     7.63             49.02             86.54                               1.848  134.138   0.1586    5.277

   183   1.3513  1    753.689     8.22             38.58             82.44                               1.853  114.296   0.0273    4.855

   184   2.4164  1    756.105     8.38             30.15             78.26                               1.860  148.467   0.0334    5.722

   185   4.0392  1    760.144     7.97             24.36             75.36                               1.947  110.069   0.2635    4.499

   186   3.4190  1    763.563     7.34             20.06             73.22                               1.952  112.456   0.0644    5.795

   187   5.5814  1    769.145     6.50             15.74             70.78                               1.964  134.572   0.1040   11.503

   188   7.6901  1    776.835     5.34             11.78             68.81                               1.974  126.478   0.0595    6.829

   189  12.8469  1    789.682     4.14              8.59             67.49                               1.982  127.171   0.0938    8.533

   190  18.4427  1    808.124     3.81              7.97             67.68                               2.239   25.563   0.3281    3.273

   191  13.5009  1    821.625     3.41              6.48             65.50                               2.248   79.295   0.1112   10.917

   192  18.0942  1    839.720     3.37              6.31             65.18                               2.487    9.763   0.0819    1.319

   193  27.3092  2    867.029     3.11              4.97             61.51                               2.603   65.062   0.2334    8.648

   194  24.9325  1    891.961     2.68              3.89             59.19                               2.612   62.102   0.0580   10.092

   195  40.1625  5    932.124     2.23              3.68             62.24                               2.799   30.416   0.1095    4.579

   196  54.1686  2    986.292     2.36              2.71             53.50                               2.961   41.067   0.1374    5.828

   197  65.9693  2   1052.262     2.23              2.25             50.21                               3.108   38.430   0.1504    4.805

   198  42.7384  1   1095.000     2.19              1.94             46.91                               3.155   27.576   0.0793    3.095

Time steps : 198/200, step size: 5.5303, 13.6749

simuapp          rc=0  10.73s  212/213 steps  to  1095.00 days

simumpi np=1     rc=0   3.88s   66/ 69 steps,  3 cuts  to    19.13 days

simumpi np=2     rc=0   7.54s  252/253 steps,  1 cuts  to  1095.00 days

simumpi np=4     rc=0   7.03s  198/200 steps,  2 cuts  to  1095.00 days

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

Elapsed: 24.24s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 23.003s  96.00%      

|- Newton                                22.853s  |- 99.35%   

  |- FluxJac                              8.845s    |- 38.70% 

  |- Update                               7.655s    |- 33.50% 

  |- Solver                               2.105s    |- 9.21%  

  |- ScdAcc                               2.003s    |- 8.77%  

  |- update_dev                           1.277s    |- 5.59%  

  |- Precond                              0.358s    |- 1.57%  

  |- Residual                             0.159s    |- 0.69%  

  |- alignvar                             0.106s    |- 0.46%  

  |- HeatLoss                             0.067s    |- 0.29%  

  |- PerfJac                              0.049s    |- 0.21%  

  |- SanitizeJac                          0.048s    |- 0.21%  

|- Output                                 0.091s  |- 0.40%    

|- Logging                                0.001s  |- 0.00%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.958s  4.00%       

|- execution                              0.811s  |- 84.66%   

------------------------------------------------------------

TOTAL                                    23.961s

============================================================



Time steps : 4/4, step size: 0.129526, 0.0271065

Running simulation [simuapp]: scaling baseline (attempt 2/2) (OMP_NUM_THREADS=1)

Elapsed: 23.96s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 22.861s  96.55%      

|- Newton                                22.743s  |- 99.48%   

  |- FluxJac                              8.759s    |- 38.52% 

  |- Update                               7.561s    |- 33.24% 

  |- Solver                               2.163s    |- 9.51%  

  |- ScdAcc                               1.981s    |- 8.71%  

  |- update_dev                           1.252s    |- 5.50%  

  |- Precond                              0.374s    |- 1.64%  

  |- Residual                             0.158s    |- 0.70%  

  |- alignvar                             0.102s    |- 0.45%  

  |- HeatLoss                             0.087s    |- 0.38%  

  |- SanitizeJac                          0.057s    |- 0.25%  

  |- PerfJac                              0.054s    |- 0.24%  

|- Output                                 0.056s  |- 0.25%    

|- Logging                                0.001s  |- 0.00%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.816s  3.45%       

|- execution                              0.686s  |- 84.05%   

------------------------------------------------------------

TOTAL                                    23.677s

============================================================



Time steps : 4/4, step size: 0.129526, 0.0271065

Running simulation [simumpi]: scaling np=1 (attempt 1/2) (OMP_NUM_THREADS=1, np=1)

Elapsed: 26.28s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-20







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.260   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     720.00    0.000  358.615   0.0032    0.123

     3   0.1391  1      0.356   426.18             27.34              6.03                     719.99    0.000  376.205   0.0037    0.139

     4   0.1620  1      0.518   376.58             25.84              6.42                     720.00    0.000  366.852   0.0042    0.158





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129439, 0.0269948

Running simulation [simumpi]: scaling np=1 (attempt 2/2) (OMP_NUM_THREADS=1, np=1)

Elapsed: 27.31s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-20







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.260   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     720.00    0.000  358.615   0.0032    0.123

     3   0.1391  1      0.356   426.18             27.34              6.03                     719.99    0.000  376.205   0.0037    0.139

     4   0.1620  1      0.518   376.58             25.84              6.42                     720.00    0.000  366.852   0.0042    0.158





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129439, 0.0269948

Running simulation [simumpi]: scaling np=2 (attempt 1/2) (OMP_NUM_THREADS=1, np=2)

Elapsed: 14.68s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-20







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.308   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     720.00    0.000  358.575   0.0032    0.123

     3   0.1391  1      0.356   426.19             27.34              6.03                     720.00    0.000  376.177   0.0037    0.139

     4   0.1620  1      0.518   376.59             25.84              6.42                     720.00    0.000  366.843   0.0042    0.158





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129438, 0.0269976

Running simulation [simumpi]: scaling np=2 (attempt 2/2) (OMP_NUM_THREADS=1, np=2)

Elapsed: 14.22s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-20







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.308   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     720.00    0.000  358.575   0.0032    0.123

     3   0.1391  1      0.356   426.19             27.34              6.03                     720.00    0.000  376.177   0.0037    0.139

     4   0.1620  1      0.518   376.59             25.84              6.42                     720.00    0.000  366.843   0.0042    0.158





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129438, 0.0269976

Running simulation [simumpi]: scaling np=4 (attempt 1/2) (OMP_NUM_THREADS=1, np=4)

Elapsed: 8.69s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-20







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.259   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     720.00    0.000  358.613   0.0032    0.123

     3   0.1391  1      0.356   426.18             27.34              6.03                     719.99    0.000  376.203   0.0037    0.139

     4   0.1620  1      0.518   376.58             25.84              6.42                     720.00    0.000  366.832   0.0042    0.158





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129439, 0.0269952

Running simulation [simumpi]: scaling np=4 (attempt 2/2) (OMP_NUM_THREADS=1, np=4)

Elapsed: 8.54s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-20







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.259   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     720.00    0.000  358.613   0.0032    0.123

     3   0.1391  1      0.356   426.18             27.34              6.03                     719.99    0.000  376.203   0.0037    0.139

     4   0.1620  1      0.518   376.58             25.84              6.42                     720.00    0.000  366.832   0.0042    0.158





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129439, 0.0269952

Running simulation [simumpi]: scaling np=8 (attempt 1/2) (OMP_NUM_THREADS=1, np=8)

Elapsed: 8.31s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-20







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.274   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     719.99    0.000  358.634   0.0032    0.123

     3   0.1391  1      0.356   426.19             27.34              6.03                     719.99    0.000  376.238   0.0037    0.139

     4   0.1620  1      0.518   376.59             25.84              6.42                     720.00    0.000  366.790   0.0042    0.158





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129433, 0.0269886

Running simulation [simumpi]: scaling np=8 (attempt 2/2) (OMP_NUM_THREADS=1, np=8)

Elapsed: 9.88s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-20







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.274   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     719.99    0.000  358.634   0.0032    0.123

     3   0.1391  1      0.356   426.19             27.34              6.03                     719.99    0.000  376.238   0.0037    0.139

     4   0.1620  1      0.518   376.59             25.84              6.42                     720.00    0.000  366.790   0.0042    0.158





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129433, 0.0269886

```

![png]({{ "/assets/images/benchmark_image_126.png" | relative_url }})

```
   config  steps   seconds   speedup   effic.  cells/rank   ghosts

  simuapp      4     23.68         -        -           -        -

     np=1      4     24.25     1.00x     100%      202005        0

     np=2      4     12.73     1.91x      95%      101080     2110

     np=4      4      7.33     3.31x      83%       50520     4235

     np=8      4      6.30     3.85x      48%       25610     8325 *

  * more ranks than the 4 fast cores on this CPU - paced by the slow ones, so read the efficiency as the machine's, not the partition's

```

```
Script completed at: 2026-10-21 07:14:37

```
