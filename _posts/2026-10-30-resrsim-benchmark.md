---
layout: default
title: "Benchmark results of resrsim"
date: 2026-10-30
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

Elapsed: 1.05s

    22  55.0000  1   3650.000    47.21              1.86              3.80                      30.05    0.000   39.404 4.29e-04    0.029



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.242s  57.77%      

|- Newton                                 0.217s  |- 89.54%   

  |- Update                               0.083s    |- 38.27% 

  |- FluxJac                              0.051s    |- 23.69% 

  |- ScdAcc                               0.026s    |- 12.08% 

  |- Solver                               0.020s    |- 9.16%  

  |- update_dev                           0.010s    |- 4.77%  

  |- Precond                              0.010s    |- 4.46%  

  |- Residual                             0.006s    |- 2.56%  

  |- SanitizeJac                          0.002s    |- 0.78%  

  |- alignvar                             0.001s    |- 0.63%  

  |- PerfJac                              0.001s    |- 0.60%  

  |- HeatLoss                             0.001s    |- 0.33%  

|- Output                                 0.015s  |- 6.36%    

|- Logging                                0.001s  |- 0.25%    

|- Input                                  0.000s  |- 0.04%    

Initialization                            0.177s  42.23%      

|- execution                              0.161s  |- 90.73%   

------------------------------------------------------------

TOTAL                                     0.420s

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

Elapsed: 1.18s

    80  59.6411  9   3650.000     0.01              4.43             99.73                       4.61    0.022    2.431   0.0029    1.082



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.868s  93.44%      

|- Newton                                 0.832s  |- 95.87%   

  |- Update                               0.214s    |- 25.70% 

  |- FluxJac                              0.201s    |- 24.15% 

  |- Solver                               0.144s    |- 17.31% 

  |- ScdAcc                               0.074s    |- 8.94%  

  |- Precond                              0.063s    |- 7.52%  

  |- update_dev                           0.044s    |- 5.29%  

  |- PerfJac                              0.036s    |- 4.37%  

  |- SanitizeJac                          0.018s    |- 2.22%  

  |- alignvar                             0.011s    |- 1.30%  

  |- Residual                             0.007s    |- 0.81%  

  |- HeatLoss                             0.005s    |- 0.62%  

|- Output                                 0.023s  |- 2.65%    

|- Logging                                0.005s  |- 0.57%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.061s  6.56%       

|- execution                              0.058s  |- 95.59%   

------------------------------------------------------------

TOTAL                                     0.929s

============================================================



Time steps : 80/80, step size: 45.625, 50.7859

```

## Select and Plot Columns

Select specific columns from the loaded DataFrames and plot them using matplotlib. For example, plot `TIME` vs `TEMP 1-1-4` from `stars_spe4b_special.csv`.

### Wells

* One row per well: bottom-hole pressure, water rate, oil rate (producers only). ECL names the producers PNEAR (EDGE PRDCR, block 5,5,4) and PFAR (CRNR PRDCR, block 9,1,1).

![png]({{ "/assets/images/benchmark_image_4.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation, CMG and ECL against OURS.

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

![png]({{ "/assets/images/benchmark_image_5.png" | relative_url }})

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

Timeloop                                  0.774s  93.35%      

|- Newton                                 0.749s  |- 96.78%   

  |- Update                               0.195s    |- 26.02% 

  |- FluxJac                              0.175s    |- 23.32% 

  |- Solver                               0.128s    |- 17.16% 

  |- ScdAcc                               0.066s    |- 8.83%  

  |- Precond                              0.059s    |- 7.92%  

  |- update_dev                           0.037s    |- 4.96%  

  |- PerfJac                              0.032s    |- 4.33%  

  |- SanitizeJac                          0.017s    |- 2.22%  

  |- alignvar                             0.011s    |- 1.42%  

  |- Residual                             0.006s    |- 0.83%  

  |- HeatLoss                             0.005s    |- 0.69%  

|- Output                                 0.016s  |- 2.06%    

|- Logging                                0.008s  |- 0.99%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.055s  6.65%       

|- execution                              0.053s  |- 95.27%   

------------------------------------------------------------

TOTAL                                     0.829s

============================================================



Time steps : 49/55, step size: 74.4898, 98.6205

```

![png]({{ "/assets/images/benchmark_image_6.png" | relative_url }})

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

Timeloop                                  0.581s  92.06%      

|- Newton                                 0.558s  |- 95.98%   

  |- Update                               0.175s    |- 31.32% 

  |- FluxJac                              0.085s    |- 15.25% 

  |- Solver                               0.065s    |- 11.64% 

  |- ScdAcc                               0.064s    |- 11.43% 

  |- Precond                              0.055s    |- 9.78%  

  |- PerfJac                              0.032s    |- 5.74%  

  |- update_dev                           0.030s    |- 5.34%  

  |- SanitizeJac                          0.016s    |- 2.82%  

  |- alignvar                             0.010s    |- 1.84%  

  |- HeatLoss                             0.009s    |- 1.67%  

  |- Residual                             0.006s    |- 1.10%  

|- Output                                 0.016s  |- 2.71%    

|- Logging                                0.003s  |- 0.56%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.050s  7.94%       

|- execution                              0.048s  |- 95.19%   

------------------------------------------------------------

TOTAL                                     0.632s

============================================================



Time steps : 81/85, step size: 0.123457, 0.528462

```

### Load Benchmark

### Buckley Plot

![png]({{ "/assets/images/benchmark_image_7.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_8.png" | relative_url }})

# MISC

## spe04b_cw.dat

```
Running simulation [simuapp]: SPE4-b water flooding

Elapsed: 0.64s

    22 163.8815  2   3650.000     0.78             10.19             92.87                      10.73    0.001   13.764   0.0097    0.002



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.370s  86.65%      

|- Newton                                 0.359s  |- 97.14%   

  |- Update                               0.113s    |- 31.46% 

  |- FluxJac                              0.110s    |- 30.51% 

  |- Solver                               0.044s    |- 12.25% 

  |- ScdAcc                               0.031s    |- 8.73%  

  |- Precond                              0.022s    |- 6.21%  

  |- update_dev                           0.015s    |- 4.21%  

  |- PerfJac                              0.006s    |- 1.74%  

  |- SanitizeJac                          0.005s    |- 1.35%  

  |- Residual                             0.004s    |- 1.14%  

  |- alignvar                             0.004s    |- 0.98%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.007s  |- 2.01%    

|- Logging                                0.001s  |- 0.27%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.057s  13.35%      

|- execution                              0.055s  |- 95.95%   

------------------------------------------------------------

TOTAL                                     0.427s

============================================================



Time steps : 22/22, step size: 165.909, 155.033

```



## watfld_cw.dat

```
Running simulation [simuapp]: SPE4-b Water flooding without vmod

Elapsed: 0.88s

    35  33.3426  2   3650.000     1.04             79.00             98.70                      80.00    0.000    1.919   0.0029  3.2e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.588s  92.03%      

|- Newton                                 0.571s  |- 97.14%   

  |- Update                               0.175s    |- 30.66% 

  |- FluxJac                              0.167s    |- 29.16% 

  |- Solver                               0.073s    |- 12.80% 

  |- ScdAcc                               0.044s    |- 7.66%  

  |- PerfJac                              0.031s    |- 5.44%  

  |- Precond                              0.031s    |- 5.37%  

  |- update_dev                           0.025s    |- 4.32%  

  |- SanitizeJac                          0.008s    |- 1.39%  

  |- Residual                             0.006s    |- 1.07%  

  |- alignvar                             0.005s    |- 0.87%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.010s  |- 1.77%    

|- Logging                                0.001s  |- 0.25%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.051s  7.97%       

|- execution                              0.049s  |- 95.66%   

------------------------------------------------------------

TOTAL                                     0.639s

============================================================



Time steps : 35/35, step size: 104.286, 142.633

```

## stflu001.dat

Inverted 9 spot hot water flooding with area/block modifier, 5 point transmissibility


```
Running simulation [simuapp]: Inverted 9 spot hot water flooding

Elapsed: 1.06s

    95 365.0000  2   3650.000    2e-04            597.41            100.00                     597.41    0.007    0.460 3.94e-04    0.011



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.823s  94.76%      

|- Newton                                 0.793s  |- 96.31%   

  |- Update                               0.245s    |- 30.90% 

  |- FluxJac                              0.214s    |- 27.04% 

  |- ScdAcc                               0.079s    |- 10.02% 

  |- Precond                              0.070s    |- 8.87%  

  |- Solver                               0.065s    |- 8.17%  

  |- update_dev                           0.045s    |- 5.64%  

  |- SanitizeJac                          0.019s    |- 2.46%  

  |- PerfJac                              0.014s    |- 1.83%  

  |- alignvar                             0.012s    |- 1.47%  

  |- Residual                             0.008s    |- 1.00%  

  |- HeatLoss                             0.006s    |- 0.76%  

|- Output                                 0.022s  |- 2.73%    

|- Logging                                0.004s  |- 0.53%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.045s  5.24%       

|- execution                              0.043s  |- 94.91%   

------------------------------------------------------------

TOTAL                                     0.868s

============================================================



Time steps : 95/98, step size: 38.4211, 98.4228

```

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation, CMG against OURS.

![png]({{ "/assets/images/benchmark_image_9.png" | relative_url }})

## stflu002.dat

5000x5000x50, 2D diagonal water flooding in uniformed cartesian

```
Running simulation [simuapp]: Uniformed cartesian water flooding

Elapsed: 0.57s

    49 268.8942  6   3650.000   620.60             11.38              1.80                     635.95    0.007  1.1e+03   0.0405    0.028



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.305s  87.16%      

|- Newton                                 0.290s  |- 95.00%   

  |- Update                               0.080s    |- 27.63% 

  |- FluxJac                              0.059s    |- 20.42% 

  |- Solver                               0.058s    |- 19.83% 

  |- ScdAcc                               0.024s    |- 8.17%  

  |- Precond                              0.023s    |- 7.97%  

  |- PerfJac                              0.012s    |- 4.19%  

  |- update_dev                           0.011s    |- 3.91%  

  |- SanitizeJac                          0.007s    |- 2.38%  

  |- alignvar                             0.004s    |- 1.46%  

  |- HeatLoss                             0.003s    |- 1.18%  

  |- Residual                             0.003s    |- 1.04%  

|- Output                                 0.010s  |- 3.20%    

|- Logging                                0.002s  |- 0.56%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.045s  12.84%      

|- execution                              0.043s  |- 94.96%   

------------------------------------------------------------

TOTAL                                     0.350s

============================================================



Time steps : 49/49, step size: 74.4898, 130.04

```



## stflu003.dat

5000x5000x50, 2D diagonal water flooding in uniformed corner point

```
Running simulation [simuapp]: uniformed corner grid

Elapsed: 0.54s

    44 242.0923  6   3650.000   621.22             11.18              1.77                     635.95    0.005  850.791   0.0365    0.025



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.267s  83.38%      

|- Newton                                 0.253s  |- 95.07%   

  |- Update                               0.072s    |- 28.60% 

  |- FluxJac                              0.052s    |- 20.54% 

  |- Solver                               0.050s    |- 19.65% 

  |- ScdAcc                               0.020s    |- 7.97%  

  |- Precond                              0.019s    |- 7.51%  

  |- PerfJac                              0.011s    |- 4.32%  

  |- update_dev                           0.010s    |- 3.89%  

  |- SanitizeJac                          0.006s    |- 2.22%  

  |- alignvar                             0.003s    |- 1.32%  

  |- HeatLoss                             0.003s    |- 1.22%  

  |- Residual                             0.003s    |- 1.03%  

|- Output                                 0.008s  |- 3.15%    

|- Logging                                0.001s  |- 0.54%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.053s  16.62%      

|- execution                              0.051s  |- 95.17%   

------------------------------------------------------------

TOTAL                                     0.320s

============================================================



Time steps : 44/44, step size: 82.9545, 133.208

```

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_10.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_11.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_12.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_13.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_14.png" | relative_url }})



## stflu004.dat

2D diagonal water flooding for reduction of numerical dispersion and grid orientation effect


```
Running simulation [simuapp]: 2D diagonal flow: grid orientation

Elapsed: 0.92s

    61  22.1594  5   3650.000   613.37             21.71              3.42                     635.95    0.002  280.490   0.0074    0.016



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.645s  92.24%      

|- Newton                                 0.625s  |- 96.93%   

  |- Update                               0.226s    |- 36.15% 

  |- FluxJac                              0.130s    |- 20.76% 

  |- Solver                               0.108s    |- 17.35% 

  |- ScdAcc                               0.049s    |- 7.78%  

  |- Precond                              0.033s    |- 5.32%  

  |- update_dev                           0.024s    |- 3.88%  

  |- PerfJac                              0.014s    |- 2.25%  

  |- HeatLoss                             0.009s    |- 1.43%  

  |- SanitizeJac                          0.008s    |- 1.34%  

  |- Residual                             0.007s    |- 1.10%  

  |- alignvar                             0.006s    |- 0.91%  

|- Output                                 0.013s  |- 2.08%    

|- Logging                                0.002s  |- 0.34%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.054s  7.76%       

|- execution                              0.052s  |- 95.64%   

------------------------------------------------------------

TOTAL                                     0.699s

============================================================



Time steps : 61/61, step size: 59.8361, 78.8186

```

![png]({{ "/assets/images/benchmark_image_15.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_16.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_17.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_18.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_19.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_20.png" | relative_url }})

## stflu007.dat

PEBI_GRID


```
Running simulation [simuapp]: 2D diagonal flow: pebi grid

Elapsed: 2.10s

    59 272.1883  6   3650.000   619.02             12.22              1.94                     635.95    0.005  1.2e+03   0.0553    0.049



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.827s  96.99%      

|- Newton                                 1.798s  |- 98.45%   

  |- Solver                               0.764s    |- 42.46% 

  |- FluxJac                              0.399s    |- 22.18% 

  |- Update                               0.337s    |- 18.74% 

  |- ScdAcc                               0.089s    |- 4.93%  

  |- Precond                              0.060s    |- 3.33%  

  |- update_dev                           0.056s    |- 3.10%  

  |- HeatLoss                             0.018s    |- 1.01%  

  |- PerfJac                              0.015s    |- 0.82%  

  |- SanitizeJac                          0.014s    |- 0.79%  

  |- Residual                             0.014s    |- 0.78%  

  |- alignvar                             0.010s    |- 0.55%  

|- Output                                 0.019s  |- 1.06%    

|- Logging                                0.009s  |- 0.47%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.057s  3.01%       

|- execution                              0.047s  |- 83.76%   

------------------------------------------------------------

TOTAL                                     1.883s

============================================================



Time steps : 59/59, step size: 61.8644, 117.981

```

![png]({{ "/assets/images/benchmark_image_21.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_22.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_23.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_24.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_25.png" | relative_url }})

## stflu026.dat

* Steam flood on two component live oil

```
Running simulation [simuapp]: 3 component steam flooding

Elapsed: 18.10s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 17.780s  99.56%      

|- Newton                                17.455s  |- 98.17%   

  |- Update                               5.037s    |- 28.86% 

  |- FluxJac                              4.343s    |- 24.88% 

  |- Solver                               1.940s    |- 11.11% 

  |- ScdAcc                               1.673s    |- 9.58%  

  |- Precond                              1.582s    |- 9.06%  

  |- update_dev                           0.813s    |- 4.66%  

  |- PerfJac                              0.784s    |- 4.49%  

  |- SanitizeJac                          0.406s    |- 2.32%  

  |- alignvar                             0.260s    |- 1.49%  

  |- Residual                             0.151s    |- 0.87%  

  |- HeatLoss                             0.137s    |- 0.79%  

|- Output                                 0.215s  |- 1.21%    

|- Logging                                0.107s  |- 0.60%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.078s  0.44%       

|- execution                              0.074s  |- 94.82%   

------------------------------------------------------------

TOTAL                                    17.858s

============================================================



Time steps : 756/1000, step size: 0.198605, 1.26366

```

#### Load OURS, CMG and ECL

* STARS wells: CRNR PRDCR, EDGE PRDCR, INJECTOR. STARS block history at (1,1,4), (5,5,4), (9,1,1) and (5,4,1); ECL has the first three only.

* ECL names the two producers PNEAR (EDGE PRDCR, block 5,5,4) and PFAR (CRNR PRDCR, block 9,1,1); PNEAR produces twice PFAR at the start, as EDGE does CRNR.

```
OURS reached day 150.1 of 3650

```

### Wells

* One row per well: bottom-hole pressure, water rate, oil rate (producers only).

![png]({{ "/assets/images/benchmark_image_26.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation. (5,4,1) has no ECL curve.

![png]({{ "/assets/images/benchmark_image_27.png" | relative_url }})

# SPE4C

* Steam flood on three component live oil

* 'Water', 'LiteOil', 'Medm oil', 'Heavy oil'


## Run & Load

```
Running simulation [simuapp]: SPE4-C benchmark on live oil

Elapsed: 2.27s

    91 209.8728 10   3650.000     0.00              4.23             99.91                       4.27    1.054   11.518   0.0097    4.096



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.864s  94.18%      

|- Newton                                 1.821s  |- 97.72%   

  |- Solver                               0.543s    |- 29.82% 

  |- FluxJac                              0.397s    |- 21.77% 

  |- Update                               0.347s    |- 19.03% 

  |- ScdAcc                               0.136s    |- 7.49%  

  |- Precond                              0.135s    |- 7.39%  

  |- update_dev                           0.074s    |- 4.06%  

  |- alignvar                             0.063s    |- 3.46%  

  |- PerfJac                              0.052s    |- 2.86%  

  |- SanitizeJac                          0.030s    |- 1.62%  

  |- Residual                             0.009s    |- 0.51%  

  |- HeatLoss                             0.009s    |- 0.49%  

|- Output                                 0.029s  |- 1.53%    

|- Logging                                0.008s  |- 0.44%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.115s  5.82%       

|- execution                              0.110s  |- 95.28%   

------------------------------------------------------------

TOTAL                                     1.979s

============================================================



Time steps : 91/95, step size: 40.1099, 58.0692

```

#### Load CMG

### Load ECL

### Wells

* One row per well: bottom-hole pressure, water rate, oil rate (producers only). ECL names the producers PNEAR (EDGE PRDCR) and PFAR (CRNR PRDCR).

![png]({{ "/assets/images/benchmark_image_28.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation, CMG and ECL against OURS.

![png]({{ "/assets/images/benchmark_image_29.png" | relative_url }})

# Cyclic steam stimulation

## CSS SPE4

stspe001.dat: Cyclic steam stimulation on radial grid

```
Running simulation [simuapp]: Cyclic steam stimulation in Radial grid

Elapsed: 1.01s

   101  68.6845  6   1095.000     1.24              0.76             37.92                               0.020   24.100   0.1646    4.453



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.675s  91.47%      

|- Newton                                 0.637s  |- 94.36%   

  |- Update                               0.179s    |- 28.07% 

  |- FluxJac                              0.119s    |- 18.68% 

  |- Precond                              0.080s    |- 12.56% 

  |- PerfJac                              0.066s    |- 10.35% 

  |- ScdAcc                               0.061s    |- 9.64%  

  |- Solver                               0.033s    |- 5.20%  

  |- update_dev                           0.032s    |- 5.05%  

  |- SanitizeJac                          0.028s    |- 4.35%  

  |- alignvar                             0.016s    |- 2.44%  

  |- Residual                             0.004s    |- 0.66%  

  |- HeatLoss                             0.003s    |- 0.52%  

|- Output                                 0.023s  |- 3.48%    

|- Logging                                0.007s  |- 0.96%    

|- Input                                  0.001s  |- 0.14%    

Initialization                            0.063s  8.53%       

|- execution                              0.060s  |- 95.36%   

------------------------------------------------------------

TOTAL                                     0.738s

============================================================



Time steps : 101/102, step size: 10.8416, 21.8903

```

![png]({{ "/assets/images/benchmark_image_30.png" | relative_url }})

### Wells

* Injector: bottom-hole pressure (ECL only; the CMG well export has none) and water rate. Producer: bottom-hole pressure (ECL only), water and oil rate.

* Bottom-hole pressure is drawn only while the well flows: ECL reports 0 for a shut-in well and OURS holds its last value.

![png]({{ "/assets/images/benchmark_image_31.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation, CMG and ECL against OURS.

![png]({{ "/assets/images/benchmark_image_32.png" | relative_url }})



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

Timeloop                                 10.234s  99.24%      

|- Newton                                10.106s  |- 98.75%   

  |- FluxJac                              3.402s    |- 33.66% 

  |- Update                               2.705s    |- 26.77% 

  |- Solver                               1.690s    |- 16.72% 

  |- ScdAcc                               0.849s    |- 8.40%  

  |- update_dev                           0.451s    |- 4.46%  

  |- Precond                              0.440s    |- 4.35%  

  |- PerfJac                              0.106s    |- 1.05%  

  |- Residual                             0.095s    |- 0.94%  

  |- HeatLoss                             0.093s    |- 0.92%  

  |- SanitizeJac                          0.086s    |- 0.85%  

  |- alignvar                             0.064s    |- 0.63%  

|- Output                                 0.099s  |- 0.97%    

|- Logging                                0.017s  |- 0.16%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.078s  0.76%       

|- execution                              0.075s  |- 96.10%   

------------------------------------------------------------

TOTAL                                    10.312s

============================================================



Time steps : 150/161, step size: 7.3, 16.8364

```

```
Found 151 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu008_00150.vtu

```

![png]({{ "/assets/images/benchmark_image_33.png" | relative_url }})

### Wells

![png]({{ "/assets/images/benchmark_image_34.png" | relative_url }})

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

Elapsed: 33.27s

   122  34.5009  6   1095.000     0.85              0.44             34.12                               0.005   73.368   0.2557    1.917



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 32.612s  99.33%      

|- Newton                                32.413s  |- 99.39%   

  |- FluxJac                             12.336s    |- 38.06% 

  |- Update                               8.034s    |- 24.79% 

  |- Solver                               6.910s    |- 21.32% 

  |- ScdAcc                               2.066s    |- 6.37%  

  |- update_dev                           1.082s    |- 3.34%  

  |- Precond                              0.994s    |- 3.07%  

  |- Residual                             0.263s    |- 0.81%  

  |- HeatLoss                             0.142s    |- 0.44%  

  |- alignvar                             0.119s    |- 0.37%  

  |- SanitizeJac                          0.083s    |- 0.26%  

  |- PerfJac                              0.070s    |- 0.22%  

|- Output                                 0.164s  |- 0.50%    

|- Logging                                0.026s  |- 0.08%    

|- Input                                  0.002s  |- 0.01%    

Initialization                            0.220s  0.67%       

|- execution                              0.179s  |- 81.41%   

------------------------------------------------------------

TOTAL                                    32.832s

============================================================



Time steps : 122/123, step size: 8.97541, 20.3546

```

```
Found 123 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu009_00122.vtu

```

![png]({{ "/assets/images/benchmark_image_35.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_36.png" | relative_url }})

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

Elapsed: 15.10s

   216  32.0337  6   1095.000     1.71              1.17             40.59                               0.302   19.089   0.0744    1.982



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 14.652s  99.07%      

|- Newton                                14.468s  |- 98.74%   

  |- FluxJac                              4.984s    |- 34.45% 

  |- Update                               3.421s    |- 23.64% 

  |- Solver                               3.226s    |- 22.30% 

  |- ScdAcc                               0.985s    |- 6.81%  

  |- Precond                              0.588s    |- 4.07%  

  |- update_dev                           0.544s    |- 3.76%  

  |- PerfJac                              0.176s    |- 1.22%  

  |- Residual                             0.122s    |- 0.84%  

  |- SanitizeJac                          0.113s    |- 0.78%  

  |- alignvar                             0.075s    |- 0.52%  

  |- HeatLoss                             0.060s    |- 0.41%  

|- Output                                 0.144s  |- 0.98%    

|- Logging                                0.032s  |- 0.22%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.138s  0.93%       

|- execution                              0.112s  |- 81.36%   

------------------------------------------------------------

TOTAL                                    14.790s

============================================================



Time steps : 216/220, step size: 5.06944, 13.8063

```

```
Found 217 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu025_00216.vtu

```

![png]({{ "/assets/images/benchmark_image_37.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_38.png" | relative_url }})

### stflu010.dat 

incomp gas

```
Running simulation [simuapp]: Incomp GAS

Elapsed: 3.39s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  3.091s  98.21%      

|- Newton                                 3.039s  |- 98.32%   

  |- Solver                               0.917s    |- 30.17% 

  |- Update                               0.660s    |- 21.70% 

  |- FluxJac                              0.538s    |- 17.71% 

  |- Precond                              0.337s    |- 11.09% 

  |- ScdAcc                               0.267s    |- 8.79%  

  |- update_dev                           0.133s    |- 4.38%  

  |- SanitizeJac                          0.067s    |- 2.19%  

  |- alignvar                             0.041s    |- 1.33%  

  |- Residual                             0.015s    |- 0.51%  

  |- PerfJac                              0.011s    |- 0.35%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.034s  |- 1.10%    

|- Logging                                0.020s  |- 0.66%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.056s  1.79%       

|- execution                              0.053s  |- 93.30%   

------------------------------------------------------------

TOTAL                                     3.148s

============================================================



Time steps : 126/151, step size: 5.47619e-05, 3.0321e-05

```

### Wells

![png]({{ "/assets/images/benchmark_image_39.png" | relative_url }})

### SAGD

#### 2D cross the well

```
Running simulation [simuapp]: SAGD

Elapsed: 4.40s

   217   4.3042  6   2526.000     6.02             57.86             90.57                      54.10    0.002    0.834   0.0794    1.773



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  4.132s  98.86%      

|- Newton                                 4.051s  |- 98.03%   

  |- Solver                               1.134s    |- 27.98% 

  |- Update                               1.025s    |- 25.30% 

  |- FluxJac                              0.849s    |- 20.95% 

  |- ScdAcc                               0.337s    |- 8.32%  

  |- Precond                              0.256s    |- 6.31%  

  |- update_dev                           0.189s    |- 4.66%  

  |- SanitizeJac                          0.069s    |- 1.71%  

  |- alignvar                             0.051s    |- 1.25%  

  |- PerfJac                              0.043s    |- 1.05%  

  |- Residual                             0.034s    |- 0.84%  

  |- HeatLoss                             0.007s    |- 0.18%  

|- Output                                 0.054s  |- 1.31%    

|- Logging                                0.017s  |- 0.42%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.048s  1.14%       

|- execution                              0.045s  |- 94.90%   

------------------------------------------------------------

TOTAL                                     4.180s

============================================================



Time steps : 217/221, step size: 11.6406, 12.8434

```

### Wells

* The reference here is the in-house Fortran code (stm_stflu020_*.csv), labelled FORTRAN. It reports producer rates negative.

![png]({{ "/assets/images/benchmark_image_40.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, water, oil and gas saturation. (1,5,13) sits near the injector and (1,5,18) near the producer.

![png]({{ "/assets/images/benchmark_image_41.png" | relative_url }})

#### 2D along well

```
Running simulation [simuapp]: SAGD

Elapsed: 5.26s

   148  17.2912  6   2526.000    12.47            119.30             90.54                     118.66    7.005    6.555   0.1058    1.726



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  4.982s  99.05%      

|- Newton                                 4.895s  |- 98.25%   

  |- Solver                               1.734s    |- 35.43% 

  |- Update                               0.951s    |- 19.43% 

  |- FluxJac                              0.795s    |- 16.24% 

  |- PerfJac                              0.456s    |- 9.31%  

  |- ScdAcc                               0.302s    |- 6.18%  

  |- Precond                              0.241s    |- 4.93%  

  |- update_dev                           0.179s    |- 3.66%  

  |- SanitizeJac                          0.080s    |- 1.63%  

  |- alignvar                             0.057s    |- 1.17%  

  |- Residual                             0.031s    |- 0.63%  

  |- HeatLoss                             0.007s    |- 0.14%  

|- Output                                 0.053s  |- 1.06%    

|- Logging                                0.023s  |- 0.46%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.048s  0.95%       

|- execution                              0.045s  |- 94.36%   

------------------------------------------------------------

TOTAL                                     5.030s

============================================================



Time steps : 148/158, step size: 17.0676, 33.3375

```

### Wells

![png]({{ "/assets/images/benchmark_image_42.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation. The blocks follow the producer-injector pair down the 10x1x20 grid.

![png]({{ "/assets/images/benchmark_image_43.png" | relative_url }})

#### 3D

```
Running simulation [simuapp]: SAGD 3D

Elapsed: 31.71s

   152   4.8609  6    680.000    15.68            104.34             86.93                      95.24    1.103    2.751   0.1112    6.221



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 31.373s  99.80%      

|- Newton                                31.208s  |- 99.48%   

  |- Solver                              11.924s    |- 38.21% 

  |- FluxJac                              8.405s    |- 26.93% 

  |- Update                               6.039s    |- 19.35% 

  |- ScdAcc                               1.822s    |- 5.84%  

  |- update_dev                           1.100s    |- 3.52%  

  |- Precond                              0.786s    |- 2.52%  

  |- PerfJac                              0.377s    |- 1.21%  

  |- Residual                             0.199s    |- 0.64%  

  |- alignvar                             0.128s    |- 0.41%  

  |- SanitizeJac                          0.103s    |- 0.33%  

  |- HeatLoss                             0.084s    |- 0.27%  

|- Output                                 0.112s  |- 0.36%    

|- Logging                                0.027s  |- 0.08%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.064s  0.20%       

|- execution                              0.061s  |- 95.94%   

------------------------------------------------------------

TOTAL                                    31.436s

============================================================



Time steps : 152/156, step size: 4.47368, 3.96866

```

#### 2D live oil

* 10x1x20 cross-section, two-component live oil (CH4 + HOIL) with water. Injector 'Inj' (2:9,1,13) and producer 'Prod' (2:9,1,18); both are shut in and preheated for 60 days, then opened.

* CMG only (no ECL run for this deck).

```
Running simulation [simuapp]: SAGD live oil

Elapsed: 26.33s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 26.021s  99.74%      

|- Newton                                25.616s  |- 98.44%   

  |- Solver                               8.052s    |- 31.43% 

  |- FluxJac                              5.450s    |- 21.28% 

  |- Update                               4.702s    |- 18.36% 

  |- PerfJac                              2.267s    |- 8.85%  

  |- ScdAcc                               1.942s    |- 7.58%  

  |- Precond                              1.140s    |- 4.45%  

  |- update_dev                           1.084s    |- 4.23%  

  |- SanitizeJac                          0.325s    |- 1.27%  

  |- alignvar                             0.204s    |- 0.80%  

  |- Residual                             0.155s    |- 0.61%  

  |- HeatLoss                             0.033s    |- 0.13%  

|- Output                                 0.226s  |- 0.87%    

|- Logging                                0.061s  |- 0.23%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.068s  0.26%       

|- execution                              0.065s  |- 95.45%   

------------------------------------------------------------

TOTAL                                    26.089s

============================================================



Time steps : 849/1000, step size: 1.70792, 4.71602

```

#### Load OURS and CMG

* STARS wells: Inj, Prod (deck order, so .smy well index 0 and 1). STARS block history at (1,1,19), (2,1,18), (5,1,13) and (5,1,5).

* 10x1x20 grid, so the .smy block index is (i-1) + (k-1)*10.

```
OURS reached day 1450.0 of 2526

```

### Wells

* Top row: injector BHP and water rate, producer BHP. Bottom row: producer oil, water and gas rates. The wells are shut in until day 60.

![png]({{ "/assets/images/benchmark_image_44.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation.

![png]({{ "/assets/images/benchmark_image_45.png" | relative_url }})

# Speed



`-DCMAKE_BUILD_TYPE=Release`

### Dome corner grid

```
Running simulation [simuapp]: Dome Corner point

Elapsed: 3.07s

    48  76.3132  1    365.000                                                                            0.032    0.033   0.0011   16.069



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.714s  97.46%      

|- Newton                                 2.696s  |- 99.36%   

  |- Solver                               1.116s    |- 41.39% 

  |- Update                               0.606s    |- 22.47% 

  |- FluxJac                              0.577s    |- 21.38% 

  |- ScdAcc                               0.148s    |- 5.48%  

  |- update_dev                           0.088s    |- 3.26%  

  |- Precond                              0.069s    |- 2.57%  

  |- Residual                             0.024s    |- 0.91%  

  |- HeatLoss                             0.016s    |- 0.61%  

  |- alignvar                             0.012s    |- 0.44%  

  |- SanitizeJac                          0.011s    |- 0.39%  

  |- PerfJac                              0.001s    |- 0.05%  

|- Output                                 0.005s  |- 0.20%    

|- Logging                                0.003s  |- 0.10%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.071s  2.54%       

|- execution                              0.063s  |- 88.50%   

------------------------------------------------------------

TOTAL                                     2.785s

============================================================



Time steps : 48/51, step size: 7.60417, 20.5374

```

```
Found 4 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu018_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_46.png" | relative_url }})

## Heterogeneous

### SPE10 benchmark 2D 

```
Running simulation [simuapp]: SPE10 benchmark 2D water flooding 375 days ~7s single thread (OMP_NUM_THREADS=8)

Elapsed: 10.32s

    90   0.7245  6    375.000    19.31             4e-04              0.00                      19.43    0.006    0.191   0.0151  5.6e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 10.027s  99.08%      

|- Newton                                 9.904s  |- 98.77%   

  |- FluxJac                              2.834s    |- 28.62% 

  |- Update                               2.817s    |- 28.45% 

  |- Solver                               2.071s    |- 20.91% 

  |- ScdAcc                               0.796s    |- 8.04%  

  |- update_dev                           0.416s    |- 4.20%  

  |- Precond                              0.337s    |- 3.40%  

  |- PerfJac                              0.264s    |- 2.66%  

  |- Residual                             0.125s    |- 1.26%  

  |- alignvar                             0.052s    |- 0.53%  

  |- SanitizeJac                          0.046s    |- 0.47%  

  |- HeatLoss                             0.022s    |- 0.22%  

|- Output                                 0.085s  |- 0.85%    

|- Logging                                0.012s  |- 0.12%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.093s  0.92%       

|- execution                              0.086s  |- 92.12%   

------------------------------------------------------------

TOTAL                                    10.120s

============================================================



Time steps : 90/90, step size: 4.16667, 2.86513

```

![png]({{ "/assets/images/benchmark_image_47.png" | relative_url }})

### Medium size



* 202,005 grid block (201x201x5) with heterogeneous permeability

* 61 wells water flooding pattern 

* 1500 days

```
Running simulation [simuapp]: Heterogeneous + 61wells - performance test medium size ~3m.50s (Single) (OMP_NUM_THREADS=8)

Elapsed: 291.98s

    32  22.4795  5    365.000   257.24              8.05              3.03                     720.00    0.002  111.711   0.0064    1.455



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                               4m 50.78s  99.76%      

|- Newton                              4m 49.42s  |- 99.53%   

  |- FluxJac                           1m 29.59s    |- 30.95% 

  |- Solver                            1m 20.92s    |- 27.96% 

  |- Update                             1m 9.45s    |- 24.00% 

  |- ScdAcc                              18.432s    |- 6.37%  

  |- update_dev                          10.335s    |- 3.57%  

  |- Precond                              8.550s    |- 2.95%  

  |- Residual                             3.310s    |- 1.14%  

  |- HeatLoss                             2.247s    |- 0.78%  

  |- PerfJac                              1.655s    |- 0.57%  

  |- alignvar                             0.765s    |- 0.26%  

  |- SanitizeJac                          0.537s    |- 0.19%  

|- Output                                 0.889s  |- 0.31%    

|- Logging                                0.014s  |- 0.00%    

|- Input                                  0.006s  |- 0.00%    

Initialization                            0.696s  0.24%       

|- execution                              0.555s  |- 79.72%   

------------------------------------------------------------

TOTAL                                  4m 51.47s

============================================================



Time steps : 32/32, step size: 11.4062, 13.2812

```

### Johnansen water flooding

```
Running simulation [simuapp]: Johnansen water flooding takes ~5m on M2 (OMP_NUM_THREADS=8)

Elapsed: 24.45s

    17 365.0000  1   3650.000   353.53              0.07              0.02                     188.86    0.000    3.269   0.0067  3.1e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 23.167s  96.50%      

|- Newton                                22.962s  |- 99.12%   

  |- Solver                               7.764s    |- 33.81% 

  |- Update                               6.035s    |- 26.28% 

  |- FluxJac                              5.898s    |- 25.69% 

  |- ScdAcc                               1.183s    |- 5.15%  

  |- update_dev                           0.667s    |- 2.90%  

  |- Precond                              0.663s    |- 2.89%  

  |- Residual                             0.316s    |- 1.37%  

  |- alignvar                             0.064s    |- 0.28%  

  |- SanitizeJac                          0.031s    |- 0.14%  

  |- PerfJac                              0.002s    |- 0.01%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.160s  |- 0.69%    

|- Logging                                0.002s  |- 0.01%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.840s  3.50%       

|- execution                              0.532s  |- 63.35%   

------------------------------------------------------------

TOTAL                                    24.007s

============================================================



Time steps : 17/17, step size: 214.706, 163.784

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data//stflu016_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_48.png" | relative_url }})

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

Elapsed: 2.09s

    80  59.6411  9   3650.000     0.01              4.43             99.73                       4.61    0.022    2.431   0.0029    1.082



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.670s  92.05%      

|- Newton                                 1.577s  |- 94.45%   

  |- FluxJac                              0.644s    |- 40.82% 

  |- Update                               0.345s    |- 21.88% 

  |- Solver                               0.188s    |- 11.90% 

  |- ScdAcc                               0.163s    |- 10.32% 

  |- update_dev                           0.123s    |- 7.80%  

  |- PerfJac                              0.040s    |- 2.56%  

  |- Precond                              0.023s    |- 1.49%  

  |- alignvar                             0.009s    |- 0.56%  

  |- Residual                             0.007s    |- 0.46%  

  |- HeatLoss                             0.005s    |- 0.33%  

  |- SanitizeJac                          0.002s    |- 0.10%  

|- Output                                 0.080s  |- 4.80%    

|- Logging                                0.013s  |- 0.80%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.144s  7.95%       

|- execution                              0.131s  |- 90.50%   

------------------------------------------------------------

TOTAL                                     1.814s

============================================================



Time steps : 80/80, step size: 45.625, 50.7859

Running simulation [simumpi]: MPI comparison np=1 (OMP_NUM_THREADS=1, np=1)

Elapsed: 1.82s

    57  32.7518  6   1262.277     1.60              5.27             76.75                       5.96    0.124   34.980   0.1288   27.836

    58  34.1599  6   1296.437     1.40              5.03             78.23                       5.96    0.124   39.769   0.1370   20.524

    59  41.6630  6   1338.100     1.26              5.10             80.14                       5.96    0.124   58.331   0.1206   30.315

    60  41.4143  6   1379.514     1.06              4.93             82.33                       5.96    0.124   70.837   0.1491   22.570



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  48.2420  5   1427.756     1.02              5.33             83.98                       5.96    0.124   69.761   0.1697   22.786

    62  52.8076  5   1480.564     0.76              5.12             87.02                       5.96    0.124   78.476   0.1448   26.291

    63  56.8224  6   1537.386     0.70              4.94             87.60                       5.96    0.124   93.171   0.1368    8.858

    64  69.3391  5   1606.725     0.58              4.94             89.43                       5.96    0.124  113.851   0.1035   11.651

    65  95.7370  5   1702.462     0.47              4.99             91.40                       5.96    0.124  171.074   0.1055    8.661

    66 131.1277  5   1833.590     0.35              4.90             93.34                       5.96    0.124  255.459   0.1019    9.282

    67 181.9891  5   2015.579     0.24              4.82             95.24                       5.96    0.124  401.053   0.0819   12.236

    68 205.1928  6   2220.772     0.16              4.70             96.70                       5.96    0.124  510.663   0.1033   12.849

    69 202.7223  6   2423.494     0.10              4.48             97.73                       5.96    0.124  574.822   0.0843   12.067

    70 186.7530  5   2610.247     0.07              4.31             98.44                       5.96    0.124  590.844   0.0385   10.602

    71 169.1876  5   2779.435     0.05              4.11             98.89                       5.96    0.124  582.284   0.0322    9.163

    72 154.6449  6   2934.079     0.03              3.90             99.20                       5.96    0.124  573.962   0.0275    8.087

    73 142.5919  6   3076.671     0.02              3.56             99.43                       5.96    0.124  581.926   0.0699    7.444

    74 130.3841  6   3207.055     0.01              3.24             99.58                       5.96    0.124  596.134   0.0726    6.987

    75 117.4771  6   3324.533     0.01              2.78             99.71                       5.96    0.125  622.914   0.0174    6.732

    76 103.0074  5   3427.540     0.01              3.47             99.73                       5.09    0.125  180.944   0.0405    3.058

    77 162.1234  5   3589.663     0.01              4.15             99.73                       4.58    0.125   21.317   0.0794    3.525

    78  60.3366  9   3650.000     0.01              4.43             99.73                       4.61    0.125    2.407   0.0029    1.093

Time steps : 78/78, step size: 46.7949, 51.4258

Running simulation [simumpi]: MPI comparison np=2 (OMP_NUM_THREADS=1, np=2)

Elapsed: 1.23s

    57  31.7056  5   1260.366     1.61              5.29             76.69                       5.96    0.134   35.484   0.1177   26.405

    58  34.0363  6   1294.402     1.42              5.03             77.99                       5.96    0.133   39.674   0.1513   21.870

    59  39.5318  5   1333.934     1.29              5.11             79.89                       5.96    0.132   55.554   0.1192   31.755

    60  38.2531  5   1372.187     1.09              4.92             81.84                       5.96    0.131   63.347   0.1589   26.346



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  41.1142  4   1413.302     1.05              5.31             83.45                       5.96    0.130   63.171   0.1792   17.068

    62  43.7060  6   1457.008     0.88              5.25             85.58                       5.96    0.129   57.262   0.0832   17.463

    63  57.4170  5   1514.425     0.71              4.97             87.48                       5.96    0.128   85.947   0.1149   19.526

    64  71.7266  5   1586.151     0.61              4.96             89.02                       5.96    0.126  117.378   0.1366   11.772

    65  87.5795  5   1673.731     0.50              4.97             90.90                       5.96    0.124  152.391   0.0830   10.176

    66 131.5487  5   1805.279     0.37              4.92             93.00                       5.96    0.121  251.715   0.0897    9.472

    67 183.6642  6   1988.944     0.25              4.82             95.01                       5.96    0.114  397.504   0.0921   12.493

    68 208.0328  6   2196.976     0.17              4.72             96.55                       5.96    0.109  510.366   0.1095   13.152

    69 205.5972  6   2402.574     0.11              4.50             97.63                       5.96    0.103  575.689   0.0899   12.314

    70 189.2285  5   2591.802     0.07              4.34             98.38                       5.96    0.098  592.944   0.0391   10.799

    71 171.0584  5   2762.860     0.05              4.13             98.85                       5.96    0.094  584.105   0.0326    9.304

    72 156.0581  6   2918.919     0.03              3.92             99.17                       5.96    0.089  574.713   0.0275    8.181

    73 143.7812  6   3062.700     0.02              3.59             99.41                       5.96    0.085  580.460   0.0725    7.493

    74 131.6733  6   3194.373     0.01              3.31             99.57                       5.96    0.081  595.259   0.0384    7.035

    75 118.7457  6   3313.119     0.01              2.81             99.70                       5.96    0.082  618.631   0.0520    6.738

    76 104.5685  6   3417.687     0.01              3.32             99.73                       5.20    0.080  239.761   0.0375    3.398

    77 148.8341  5   3566.521     0.01              4.12             99.73                       4.63    0.079   24.146   0.0691    3.251

    78  83.4788  4   3650.000     0.01              4.41             99.73                       4.59    0.079    1.035   0.0047    1.579

Time steps : 78/78, step size: 46.7949, 51.7233

Running simulation [simumpi]: MPI comparison np=4 (OMP_NUM_THREADS=1, np=4)

Elapsed: 1.32s

    57  31.7100  6   1260.249     1.60              5.29             76.75                       5.96    0.260   35.140   0.1168   26.440

    58  34.0169  6   1294.266     1.42              5.03             78.05                       5.96    0.260   39.640   0.1448   21.839

    59  40.2784  5   1334.544     1.28              5.11             79.94                       5.96    0.260   56.210   0.1205   31.637

    60  39.0604  5   1373.605     1.09              4.92             81.93                       5.96    0.260   64.861   0.1575   25.957



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  42.3194  4   1415.924     1.05              5.31             83.55                       5.96    0.260   64.375   0.1784   17.983

    62  45.0978  6   1461.022     0.87              5.23             85.80                       5.96    0.260   60.057   0.0955   18.748

    63  57.3994  5   1518.421     0.71              4.97             87.51                       5.96    0.260   86.053   0.1094   17.813

    64  74.7522  5   1593.174     0.60              4.96             89.20                       5.96    0.260  121.748   0.1347   12.418

    65  91.9032  5   1685.077     0.49              4.97             91.11                       5.96    0.260  161.584   0.0925    9.807

    66 132.6694  5   1817.746     0.36              4.90             93.14                       5.96    0.260  255.731   0.1111    9.485

    67 177.8737  6   1995.620     0.25              4.83             95.07                       5.96    0.260  386.760   0.0876   12.034

    68 204.3157  6   2199.935     0.17              4.72             96.57                       5.96    0.260  501.991   0.1078   12.883

    69 203.8518  6   2403.787     0.11              4.50             97.64                       5.96    0.260  571.055   0.0893   12.200

    70 188.5412  5   2592.328     0.07              4.34             98.38                       5.96    0.260  590.750   0.0389   10.758

    71 170.8242  5   2763.153     0.05              4.14             98.85                       5.96    0.260  583.220   0.0325    9.292

    72 155.9884  6   2919.141     0.03              3.92             99.17                       5.96    0.260  574.362   0.0275    8.179

    73 143.7700  6   3062.911     0.02              3.59             99.41                       5.96    0.260  580.255   0.0726    7.493

    74 131.6913  6   3194.602     0.01              3.31             99.57                       5.96    0.260  595.154   0.0369    7.036

    75 118.7748  6   3313.377     0.01              2.81             99.70                       5.96    0.260  618.420   0.0536    6.738

    76 104.6163  6   3417.994     0.01              3.32             99.73                       5.20    0.260  242.130   0.0374    3.412

    77 148.3306  5   3566.324     0.01              4.11             99.73                       4.63    0.260   24.260   0.0693    3.243

    78  83.6758  6   3650.000     0.01              4.41             99.73                       4.59    0.260    1.080   0.0047    1.586

Time steps : 78/78, step size: 46.7949, 51.3532

simuapp          rc=0   1.81s   80/ 80 steps  to  3650.00 days

simumpi np=1     rc=0   1.42s   78/ 78 steps,  0 cuts  to  3650.00 days

simumpi np=2     rc=0   0.88s   78/ 78 steps,  0 cuts  to  3650.00 days

simumpi np=4     rc=0   0.82s   78/ 78 steps,  0 cuts  to  3650.00 days

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


![png]({{ "/assets/images/benchmark_image_49.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_50.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_51.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_52.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_53.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_54.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_55.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_56.png" | relative_url }})

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

Elapsed: 22.91s

   150  36.8637  6   1095.000     1.59              1.13             41.52                               0.071   21.341   0.0648    2.486



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 22.557s  99.57%      

|- Newton                                22.446s  |- 99.51%   

  |- FluxJac                             11.080s    |- 49.36% 

  |- Update                               5.069s    |- 22.58% 

  |- ScdAcc                               2.229s    |- 9.93%  

  |- Solver                               1.591s    |- 7.09%  

  |- update_dev                           1.480s    |- 6.59%  

  |- Precond                              0.426s    |- 1.90%  

  |- alignvar                             0.116s    |- 0.52%  

  |- PerfJac                              0.105s    |- 0.47%  

  |- Residual                             0.091s    |- 0.41%  

  |- HeatLoss                             0.080s    |- 0.36%  

  |- SanitizeJac                          0.024s    |- 0.11%  

|- Output                                 0.091s  |- 0.40%    

|- Logging                                0.052s  |- 0.23%    

|- Input                                  0.001s  |- 0.00%    

Initialization                            0.097s  0.43%       

|- execution                              0.094s  |- 97.66%   

------------------------------------------------------------

TOTAL                                    22.654s

============================================================



Time steps : 150/161, step size: 7.3, 16.8364

Running simulation [simumpi]: CSS parity np=1 (OMP_NUM_THREADS=1, np=1)

Elapsed: 19.81s

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

Elapsed: 10.85s

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 12.5646) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 12.5646) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.36371) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.36371) - this cycle cannot be accepted as converged

   111   7.0000  7    747.000                                                                            0.838  1.2e+03   0.1534   29.636

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.226291) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.226291) - this cycle cannot be accepted as converged

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

Elapsed: 8.31s

   122   1.4731  6    739.304                                                                  158.99    0.220  226.632   0.1176   28.866

   123   0.6962  6    740.000                                                                  158.99    0.219  116.843   0.0842   15.023

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 21.9023) - this cycle cannot be accepted as converged

[rank 3] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 21.9023) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 21.9023) - this cycle cannot be accepted as converged

[rank 2] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 21.9023) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.46058) - this cycle cannot be accepted as converged

[rank 3] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.46058) - this cycle cannot be accepted as converged

[rank 2] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.46058) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.46058) - this cycle cannot be accepted as converged

   124   7.0000  6    747.000                                                                            0.219  1.2e+03   0.1566   29.648

[rank 3] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.124789) - this cycle cannot be accepted as converged

[rank 2] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.124789) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.124789) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.124789) - this cycle cannot be accepted as converged

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

simuapp          rc=0  22.65s  150/161 steps  to  1095.00 days

simumpi np=1     rc=0  19.48s  135/141 steps,  6 cuts  to  1095.00 days

simumpi np=2     rc=0  10.54s  126/129 steps,  3 cuts  to  1095.00 days

simumpi np=4     rc=0   7.99s  138/148 steps, 10 cuts  to  1095.00 days

```

![png]({{ "/assets/images/benchmark_image_57.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_58.png" | relative_url }})

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

Elapsed: 37.66s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 36.432s  97.58%      

|- Newton                                36.246s  |- 99.49%   

  |- FluxJac                             15.384s    |- 42.44% 

  |- Update                              10.677s    |- 29.46% 

  |- ScdAcc                               3.397s    |- 9.37%  

  |- Solver                               3.121s    |- 8.61%  

  |- update_dev                           2.156s    |- 5.95%  

  |- Precond                              0.610s    |- 1.68%  

  |- Residual                             0.219s    |- 0.60%  

  |- alignvar                             0.182s    |- 0.50%  

  |- HeatLoss                             0.109s    |- 0.30%  

  |- PerfJac                              0.083s    |- 0.23%  

  |- SanitizeJac                          0.054s    |- 0.15%  

|- Output                                 0.098s  |- 0.27%    

|- Logging                                0.002s  |- 0.00%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.903s  2.42%       

|- execution                              0.762s  |- 84.33%   

------------------------------------------------------------

TOTAL                                    37.335s

============================================================



Time steps : 4/4, step size: 0.12948, 0.0270322

Running simulation [simuapp]: scaling baseline (attempt 2/2) (OMP_NUM_THREADS=1)

Elapsed: 37.87s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 36.767s  97.83%      

|- Newton                                36.640s  |- 99.65%   

  |- FluxJac                             15.453s    |- 42.17% 

  |- Update                              10.839s    |- 29.58% 

  |- ScdAcc                               3.427s    |- 9.35%  

  |- Solver                               3.233s    |- 8.82%  

  |- update_dev                           2.166s    |- 5.91%  

  |- Precond                              0.616s    |- 1.68%  

  |- Residual                             0.220s    |- 0.60%  

  |- alignvar                             0.181s    |- 0.49%  

  |- HeatLoss                             0.111s    |- 0.30%  

  |- PerfJac                              0.083s    |- 0.23%  

  |- SanitizeJac                          0.061s    |- 0.17%  

|- Output                                 0.060s  |- 0.16%    

|- Logging                                0.002s  |- 0.00%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.816s  2.17%       

|- execution                              0.686s  |- 84.05%   

------------------------------------------------------------

TOTAL                                    37.583s

============================================================



Time steps : 4/4, step size: 0.12948, 0.0270322

Running simulation [simumpi]: scaling np=1 (attempt 1/2) (OMP_NUM_THREADS=1, np=1)

Elapsed: 38.91s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-30







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

Elapsed: 39.12s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-30







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

Elapsed: 22.04s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-30







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

Elapsed: 20.45s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-30







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

Elapsed: 12.42s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-30







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

Elapsed: 12.74s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-30







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

Elapsed: 10.62s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-30







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

Elapsed: 10.75s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-30







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

![png]({{ "/assets/images/benchmark_image_59.png" | relative_url }})

```
   config  steps   seconds   speedup   effic.  cells/rank   ghosts

  simuapp      4     37.34         -        -           -        -

     np=1      4     36.98     1.00x     100%      202005        0

     np=2      4     18.90     1.96x      98%      101080     2110

     np=4      4     11.24     3.29x      82%       50520     4235

     np=8      4      8.96     4.13x      52%       25610     8325 *

  * more ranks than the 4 fast cores on this CPU - paced by the slow ones, so read the efficiency as the machine's, not the partition's

```

```
Script completed at: 2026-10-30 12:19:51

```
