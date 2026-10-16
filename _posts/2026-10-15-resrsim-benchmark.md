---
layout: default
title: "Benchmark results of resrsim"
date: 2026-10-15
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

Elapsed: 0.61s

    25  55.0000  1   3650.000    47.50              1.87              3.78                      29.98    0.000   39.341 4.30e-04    0.029



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.285s  77.26%      

|- Newton                                 0.259s  |- 90.83%   

  |- Update                               0.101s    |- 39.09% 

  |- FluxJac                              0.063s    |- 24.26% 

  |- ScdAcc                               0.028s    |- 10.87% 

  |- Solver                               0.023s    |- 8.80%  

  |- update_dev                           0.013s    |- 4.91%  

  |- Precond                              0.011s    |- 4.44%  

  |- Residual                             0.006s    |- 2.44%  

  |- SanitizeJac                          0.002s    |- 0.80%  

  |- alignvar                             0.002s    |- 0.69%  

  |- PerfJac                              0.002s    |- 0.60%  

  |- HeatLoss                             0.001s    |- 0.38%  

|- Output                                 0.014s  |- 5.04%    

|- Logging                                0.001s  |- 0.30%    

|- Input                                  0.000s  |- 0.04%    

Initialization                            0.084s  22.74%      

|- execution                              0.075s  |- 89.40%   

------------------------------------------------------------

TOTAL                                     0.368s

============================================================



Time steps : 25/25, step size: 146, 129.93

```

```
Found 26 VTU files

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

Elapsed: 0.77s

    49  33.9643  1   3650.000     0.06              4.15             98.68                       4.70    0.226    8.451   0.0491    3.702



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.546s  90.95%      

|- Newton                                 0.525s  |- 96.13%   

  |- Update                               0.169s    |- 32.21% 

  |- FluxJac                              0.109s    |- 20.77% 

  |- Solver                               0.096s    |- 18.19% 

  |- Precond                              0.039s    |- 7.40%  

  |- ScdAcc                               0.037s    |- 7.01%  

  |- update_dev                           0.023s    |- 4.37%  

  |- PerfJac                              0.020s    |- 3.76%  

  |- SanitizeJac                          0.011s    |- 2.10%  

  |- alignvar                             0.006s    |- 1.20%  

  |- Residual                             0.004s    |- 0.73%  

  |- HeatLoss                             0.003s    |- 0.66%  

|- Output                                 0.013s  |- 2.34%    

|- Logging                                0.003s  |- 0.54%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.054s  9.05%       

|- execution                              0.048s  |- 89.21%   

------------------------------------------------------------

TOTAL                                     0.600s

============================================================



Time steps : 49/50, step size: 74.4898, 69.7484

```

## Select and Plot Columns

Select specific columns from the loaded DataFrames and plot them using matplotlib. For example, plot `TIME` vs `TEMP 1-1-4` from `stars_spe4b_special.csv`.

### Cell property

#### Block Pressure


### Why (1,1,4) no longer flattens below the CMG curve



That cell is wet steam from about day 157 on, so `P = Psat(T)` holds there to within 33-45 kPa for

the rest of the run: its pressure can only rise as its temperature does, and the two are one

degree of freedom, not two.



It used to stall at ~3865 kPa anyway, well under the STARS curve. That was not physics. Steps

whose well constraint never converged were being accepted (`newtonraphson.cpp`, the

`rconv && (wconv || mconv)` verdict forgave the well equation once its `welcyc` budget ran out),

and because the instantaneous material balance error is exactly `dt * sum(cell residual)`, those

steps are where mass goes missing - 19% of the cumulative water balance, which is what capped the

pressurisation.



With the well constraint no longer forgiven the deck closes to +0.61% water and -1.63% energy, and

P(1,1,4) climbs monotonically to 6717 kPa (556 K) while the injector's BHP reaches 6895 kPa -

exactly its `*OPERATE *MAX *BHP 1000` psi limit, which is the expected endgame once both producers

are choked by `*MAX STEAM`. 112 steps marched of 146 attempted.



`*DTMAX` is a second, independent way to reach the same place - the cap is a workaround for the

same artefact - so this deck no longer sets one. Re-adding `*DTMAX 5` trades the other way: 1 cut

instead of 34 and a slightly closer STARS match (RMSE lower on 9 of 10 series), but the water

balance goes back to ~5%.

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

Elapsed: 1.02s

    60 190.3648  2   3650.000     0.05              2.91             98.45                       5.96    2.444  513.085   0.0612    8.116



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.808s  93.83%      

|- Newton                                 0.783s  |- 96.90%   

  |- Update                               0.208s    |- 26.52% 

  |- FluxJac                              0.191s    |- 24.38% 

  |- Solver                               0.122s    |- 15.60% 

  |- Precond                              0.068s    |- 8.62%  

  |- ScdAcc                               0.066s    |- 8.46%  

  |- update_dev                           0.038s    |- 4.80%  

  |- PerfJac                              0.032s    |- 4.04%  

  |- SanitizeJac                          0.020s    |- 2.56%  

  |- alignvar                             0.012s    |- 1.52%  

  |- Residual                             0.006s    |- 0.81%  

  |- HeatLoss                             0.006s    |- 0.77%  

|- Output                                 0.015s  |- 1.90%    

|- Logging                                0.004s  |- 0.53%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.053s  6.17%       

|- execution                              0.051s  |- 95.15%   

------------------------------------------------------------

TOTAL                                     0.861s

============================================================



Time steps : 60/69, step size: 60.8333, 92.2523

```

![png]({{ "/assets/images/benchmark_image_36.png" | relative_url }})

# Buckley- Leverett



Two phase, isothermal problem

variable order: [Sw, P, T, So, X0, X1, Sg]



Acc w.r.t. [Sw, So, Sg, X0, X1, P, T]

```
Running simulation [simuapp]: Buckley-Leverett

Elapsed: 0.49s

    83   4.4625  1     10.000    2e-09              0.16            100.00                       0.16   25.038  8.3e-04 2.16e-04  3.7e-05



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.283s  85.52%      

|- Newton                                 0.262s  |- 92.55%   

  |- Update                               0.088s    |- 33.73% 

  |- FluxJac                              0.037s    |- 13.96% 

  |- Solver                               0.033s    |- 12.63% 

  |- ScdAcc                               0.027s    |- 10.26% 

  |- Precond                              0.026s    |- 9.91%  

  |- PerfJac                              0.013s    |- 4.93%  

  |- update_dev                           0.012s    |- 4.60%  

  |- SanitizeJac                          0.007s    |- 2.84%  

  |- HeatLoss                             0.005s    |- 1.86%  

  |- alignvar                             0.004s    |- 1.72%  

  |- Residual                             0.003s    |- 1.27%  

|- Output                                 0.014s  |- 4.89%    

|- Logging                                0.002s  |- 0.73%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.048s  14.48%      

|- execution                              0.045s  |- 94.87%   

------------------------------------------------------------

TOTAL                                     0.331s

============================================================



Time steps : 83/84, step size: 0.120482, 0.605262

```

### Load Benchmark

### Buckley Plot

![png]({{ "/assets/images/benchmark_image_37.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_38.png" | relative_url }})

# MISC

## spe04b_cw.dat

```
Running simulation [simuapp]: SPE4-b water flooding

Elapsed: 0.40s

    25 330.8312  1   3650.000     0.78             10.17             92.88                      10.73    0.982   28.161   0.0307    0.004



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.179s  76.34%      

|- Newton                                 0.168s  |- 93.76%   

  |- Update                               0.057s    |- 34.18% 

  |- FluxJac                              0.050s    |- 29.51% 

  |- Solver                               0.022s    |- 13.12% 

  |- ScdAcc                               0.013s    |- 7.73%  

  |- Precond                              0.009s    |- 5.15%  

  |- update_dev                           0.007s    |- 3.95%  

  |- PerfJac                              0.003s    |- 1.50%  

  |- Residual                             0.002s    |- 1.32%  

  |- SanitizeJac                          0.002s    |- 1.10%  

  |- alignvar                             0.001s    |- 0.85%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.008s  |- 4.38%    

|- Logging                                0.001s  |- 0.37%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.056s  23.66%      

|- execution                              0.053s  |- 96.04%   

------------------------------------------------------------

TOTAL                                     0.235s

============================================================



Time steps : 25/25, step size: 146, 149.392

```



## watfld_cw.dat

```
Running simulation [simuapp]: SPE4-b Water flooding without vmod

Elapsed: 0.51s

    37 276.1825  1   3650.000     1.05             78.94             98.69                      80.00    2.559   16.038   0.0266    0.003



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.299s  86.47%      

|- Newton                                 0.283s  |- 94.58%   

  |- Update                               0.092s    |- 32.47% 

  |- FluxJac                              0.073s    |- 25.79% 

  |- Solver                               0.049s    |- 17.42% 

  |- ScdAcc                               0.019s    |- 6.70%  

  |- PerfJac                              0.014s    |- 4.91%  

  |- Precond                              0.013s    |- 4.74%  

  |- update_dev                           0.010s    |- 3.39%  

  |- Residual                             0.003s    |- 1.19%  

  |- SanitizeJac                          0.003s    |- 1.10%  

  |- alignvar                             0.002s    |- 0.77%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.010s  |- 3.29%    

|- Logging                                0.001s  |- 0.31%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.047s  13.53%      

|- execution                              0.045s  |- 95.36%   

------------------------------------------------------------

TOTAL                                     0.346s

============================================================



Time steps : 37/37, step size: 98.6486, 134.987

```

## stflu001.dat

Inverted 9 spot water flooding with area/block modifier, 5 point transmissibility


```
Running simulation [simuapp]: Inverted 9 spot water flooding

Elapsed: 0.95s

   202  79.4174  6   3650.000     0.07            140.76             99.95                     138.21   39.900   88.641   0.1125    2.631



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.720s  92.84%      

|- Newton                                 0.665s  |- 92.35%   

  |- Update                               0.214s    |- 32.11% 

  |- FluxJac                              0.182s    |- 27.34% 

  |- ScdAcc                               0.062s    |- 9.28%  

  |- Precond                              0.057s    |- 8.55%  

  |- Solver                               0.053s    |- 7.93%  

  |- update_dev                           0.040s    |- 6.04%  

  |- SanitizeJac                          0.015s    |- 2.32%  

  |- PerfJac                              0.010s    |- 1.47%  

  |- alignvar                             0.008s    |- 1.26%  

  |- Residual                             0.007s    |- 1.10%  

  |- HeatLoss                             0.005s    |- 0.80%  

|- Output                                 0.040s  |- 5.51%    

|- Logging                                0.005s  |- 0.67%    

|- Input                                  0.000s  |- 0.04%    

Initialization                            0.056s  7.16%       

|- execution                              0.053s  |- 95.83%   

------------------------------------------------------------

TOTAL                                     0.776s

============================================================



Time steps : 202/204, step size: 18.0693, 61.317

```

## stflu002.dat

5000x5000x50, 2D diagonal water flooding in uniformed cartesian

```
Running simulation [simuapp]: Uniformed cartesian water flooding

Elapsed: 0.53s

    49 344.6649  5   3650.000   619.21             12.19              1.93                     635.76    0.463  1.4e+03   0.0518    0.036



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.319s  86.96%      

|- Newton                                 0.305s  |- 95.59%   

  |- Update                               0.083s    |- 27.13% 

  |- Solver                               0.064s    |- 21.01% 

  |- FluxJac                              0.059s    |- 19.33% 

  |- Precond                              0.025s    |- 8.24%  

  |- ScdAcc                               0.025s    |- 8.04%  

  |- PerfJac                              0.013s    |- 4.17%  

  |- update_dev                           0.012s    |- 3.91%  

  |- SanitizeJac                          0.007s    |- 2.32%  

  |- HeatLoss                             0.005s    |- 1.51%  

  |- alignvar                             0.004s    |- 1.21%  

  |- Residual                             0.003s    |- 0.94%  

|- Output                                 0.009s  |- 2.80%    

|- Logging                                0.002s  |- 0.55%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.048s  13.04%      

|- execution                              0.046s  |- 95.36%   

------------------------------------------------------------

TOTAL                                     0.367s

============================================================



Time steps : 49/49, step size: 74.4898, 129.892

```



## stflu003.dat

5000x5000x50, 2D diagonal water flooding in uniformed corner point

```
Running simulation [simuapp]: uniformed corner grid

Elapsed: 0.44s

    44 266.7836  4   3650.000   619.57             12.36              1.96                     635.79    0.415  954.260   0.0402    0.028



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.234s  83.78%      

|- Newton                                 0.220s  |- 94.08%   

  |- Update                               0.063s    |- 28.53% 

  |- Solver                               0.044s    |- 20.04% 

  |- FluxJac                              0.041s    |- 18.60% 

  |- Precond                              0.018s    |- 8.38%  

  |- ScdAcc                               0.017s    |- 7.57%  

  |- PerfJac                              0.009s    |- 4.08%  

  |- update_dev                           0.008s    |- 3.82%  

  |- SanitizeJac                          0.006s    |- 2.56%  

  |- alignvar                             0.004s    |- 1.79%  

  |- HeatLoss                             0.003s    |- 1.45%  

  |- Residual                             0.002s    |- 0.95%  

|- Output                                 0.009s  |- 3.79%    

|- Logging                                0.002s  |- 0.73%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.045s  16.22%      

|- execution                              0.043s  |- 94.55%   

------------------------------------------------------------

TOTAL                                     0.279s

============================================================



Time steps : 44/44, step size: 82.9545, 133.495

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

Elapsed: 0.49s

    53 192.8623  1   3650.000   634.78              0.94              0.15                     635.95   61.041  375.000   0.0400    0.018



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.286s  86.11%      

|- Newton                                 0.269s  |- 94.12%   

  |- Update                               0.108s    |- 40.19% 

  |- FluxJac                              0.051s    |- 19.04% 

  |- Solver                               0.043s    |- 15.93% 

  |- ScdAcc                               0.018s    |- 6.64%  

  |- Precond                              0.015s    |- 5.49%  

  |- update_dev                           0.010s    |- 3.79%  

  |- PerfJac                              0.005s    |- 2.01%  

  |- HeatLoss                             0.004s    |- 1.54%  

  |- SanitizeJac                          0.004s    |- 1.33%  

  |- Residual                             0.003s    |- 1.25%  

  |- alignvar                             0.003s    |- 0.95%  

|- Output                                 0.011s  |- 3.89%    

|- Logging                                0.001s  |- 0.44%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.046s  13.89%      

|- execution                              0.044s  |- 94.92%   

------------------------------------------------------------

TOTAL                                     0.332s

============================================================



Time steps : 53/53, step size: 68.8679, 120.912

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

Elapsed: 2.56s

    60  66.0791  2   3650.000   622.08             13.19              2.08                     636.26    0.465  220.739   0.0135    0.008



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.327s  97.23%      

|- Newton                                 2.301s  |- 98.88%   

  |- Solver                               0.940s    |- 40.86% 

  |- FluxJac                              0.556s    |- 24.16% 

  |- Update                               0.429s    |- 18.65% 

  |- ScdAcc                               0.114s    |- 4.98%  

  |- Precond                              0.077s    |- 3.33%  

  |- update_dev                           0.064s    |- 2.78%  

  |- HeatLoss                             0.029s    |- 1.27%  

  |- SanitizeJac                          0.021s    |- 0.89%  

  |- PerfJac                              0.018s    |- 0.76%  

  |- Residual                             0.017s    |- 0.72%  

  |- alignvar                             0.014s    |- 0.59%  

|- Output                                 0.018s  |- 0.77%    

|- Logging                                0.003s  |- 0.14%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.066s  2.77%       

|- execution                              0.057s  |- 85.61%   

------------------------------------------------------------

TOTAL                                     2.393s

============================================================



Time steps : 60/60, step size: 60.8333, 115.231

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

Elapsed: 1.16s

   110 105.8452  1   3650.000     0.01              4.32             99.85                       4.40    4.072    4.485   0.0030    1.580



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.956s  95.48%      

|- Newton                                 0.915s  |- 95.76%   

  |- Solver                               0.298s    |- 32.54% 

  |- FluxJac                              0.195s    |- 21.27% 

  |- Update                               0.185s    |- 20.18% 

  |- Precond                              0.066s    |- 7.22%  

  |- ScdAcc                               0.065s    |- 7.06%  

  |- update_dev                           0.038s    |- 4.10%  

  |- PerfJac                              0.028s    |- 3.04%  

  |- SanitizeJac                          0.013s    |- 1.37%  

  |- alignvar                             0.007s    |- 0.75%  

  |- Residual                             0.006s    |- 0.64%  

  |- HeatLoss                             0.005s    |- 0.59%  

|- Output                                 0.026s  |- 2.74%    

|- Logging                                0.004s  |- 0.38%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.045s  4.52%       

|- execution                              0.043s  |- 94.34%   

------------------------------------------------------------

TOTAL                                     1.001s

============================================================



Time steps : 110/112, step size: 33.1818, 58.7893

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

Elapsed: 0.62s

   107  16.7546  1   1095.000     1.82              0.48             20.95                               0.274   21.243   0.0888    2.259



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.404s  89.75%      

|- Newton                                 0.367s  |- 90.90%   

  |- Update                               0.112s    |- 30.62% 

  |- FluxJac                              0.061s    |- 16.72% 

  |- Precond                              0.044s    |- 11.96% 

  |- PerfJac                              0.034s    |- 9.18%  

  |- ScdAcc                               0.030s    |- 8.09%  

  |- Solver                               0.029s    |- 7.78%  

  |- update_dev                           0.019s    |- 5.23%  

  |- SanitizeJac                          0.014s    |- 3.92%  

  |- alignvar                             0.007s    |- 1.82%  

  |- Residual                             0.003s    |- 0.82%  

  |- HeatLoss                             0.002s    |- 0.66%  

|- Output                                 0.023s  |- 5.77%    

|- Logging                                0.004s  |- 0.91%    

|- Input                                  0.001s  |- 0.21%    

Initialization                            0.046s  10.25%      

|- execution                              0.044s  |- 94.90%   

------------------------------------------------------------

TOTAL                                     0.450s

============================================================



Time steps : 107/112, step size: 10.2336, 21.6198

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

Elapsed: 6.68s

   203  49.8497  1   1095.000     2.21              1.35             38.04                               3.147   37.959   0.1857    8.413



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  6.458s  99.12%      

|- Newton                                 6.331s  |- 98.04%   

  |- FluxJac                              1.746s    |- 27.59% 

  |- Solver                               1.702s    |- 26.88% 

  |- Update                               1.649s    |- 26.04% 

  |- ScdAcc                               0.431s    |- 6.81%  

  |- Precond                              0.226s    |- 3.57%  

  |- update_dev                           0.221s    |- 3.49%  

  |- Residual                             0.070s    |- 1.10%  

  |- PerfJac                              0.061s    |- 0.96%  

  |- HeatLoss                             0.060s    |- 0.95%  

  |- SanitizeJac                          0.047s    |- 0.74%  

  |- alignvar                             0.035s    |- 0.55%  

|- Output                                 0.092s  |- 1.42%    

|- Logging                                0.009s  |- 0.13%    

|- Input                                  0.001s  |- 0.02%    

Initialization                            0.057s  0.88%       

|- execution                              0.055s  |- 95.96%   

------------------------------------------------------------

TOTAL                                     6.515s

============================================================



Time steps : 203/209, step size: 5.39409, 15.2107

```

```
Found 204 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu008_00203.vtu

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

| well-cell footprint | DI=DJ=3 ft -> 9.0 ft^2 | regular hexagon -> 623.7 ft^2 (~25 x 25 ft) |



`stflu009_grd.vtk` is a *uniform* ~13.4 ft honeycomb with no near-well refinement, so the well

cell's pore volume is ~69x the Cartesian one. Heating rate scales as `1/PV`, and the injector has

zero injectivity until the well cell heats enough to boil off steam and unlock relative

permeability (`krw(Sw=0.45)=0`, oil is 487 cp at 125 F). On the coarse PEBI cell that never

happens: the well cell warms only ~10 C in 10 days, `Sg` stays 0, and all three cycles sit on the

`*MAX BHP` limit at 1-6 m^3/d, against the Cartesian run's steam breakthrough by day 3.



So the plot below is a **grid-resolution** comparison - it shows the uniform PEBI grid is simply

too coarse near the well, not a PEBI-vs-Cartesian *physics* discrepancy. A meaningful parity plot

needs near-well PEBI refinement (inner cells down to the ~3 ft Cartesian scale), which is the

whole point of using PEBI in the first place.

```
Running simulation [simuapp]: Cyclic steam stimulation in Pebi-grid

Elapsed: 1.20s

    64  55.2171  1   1095.000     0.77              0.04              5.18                               0.008    7.394   0.0013    1.478



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.964s  93.95%      

|- Newton                                 0.920s  |- 95.39%   

  |- FluxJac                              0.333s    |- 36.18% 

  |- Update                               0.309s    |- 33.62% 

  |- Solver                               0.111s    |- 12.03% 

  |- ScdAcc                               0.057s    |- 6.25%  

  |- Precond                              0.033s    |- 3.58%  

  |- update_dev                           0.032s    |- 3.47%  

  |- Residual                             0.013s    |- 1.42%  

  |- SanitizeJac                          0.006s    |- 0.66%  

  |- HeatLoss                             0.005s    |- 0.56%  

  |- alignvar                             0.005s    |- 0.51%  

  |- PerfJac                              0.002s    |- 0.18%  

|- Output                                 0.030s  |- 3.09%    

|- Logging                                0.002s  |- 0.20%    

|- Input                                  0.001s  |- 0.08%    

Initialization                            0.062s  6.05%       

|- execution                              0.051s  |- 81.97%   

------------------------------------------------------------

TOTAL                                     1.026s

============================================================



Time steps : 64/64, step size: 17.1094, 29.2456

```

```
Found 65 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu009_00064.vtu

```

![png]({{ "/assets/images/benchmark_image_99.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_100.png" | relative_url }})

### stflu009_graded.dat - near-well-refined PEBI (the real PEBI-vs-Cartesian parity case)



`stflu009_graded.dat` is the PEBI companion the note above asks for: a *graded* honeycomb whose

inner cells are refined down toward the ~3 ft Cartesian near-well scale, instead of the uniform

~13.4 ft cells of `stflu009.dat`. With a small enough well-cell pore volume the injector regains

injectivity (the cell heats, steam boils off, `krw` unlocks), so the cyclic-steam response

tracks the near-well-refined Cartesian run (`stflu008.dat`) rather than flat-lining on the

`*MAX BHP` limit the way the uniform PEBI grid does.



The three curves below are therefore the intended comparison:



| run | grid | near-well cell |

|---|---|---|

| `stflu008.dat` | Cartesian | DI=DJ=3 ft (~9 ft^2) |

| `stflu009.dat` | uniform PEBI | ~25 ft hexagon (623.7 ft^2) |

| `stflu009_graded.dat` | graded PEBI | refined toward ~3 ft near the well |


```
Running simulation [simuapp]: Cyclic steam stimulation in graded Pebi-grid

Elapsed: 10.30s

   301  21.4559  1   1095.000     2.26              1.56             40.94                               3.514   12.741   0.0909    1.988



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 10.059s  99.23%      

|- Newton                                 9.858s  |- 98.00%   

  |- FluxJac                              3.021s    |- 30.65% 

  |- Solver                               2.813s    |- 28.54% 

  |- Update                               2.318s    |- 23.51% 

  |- ScdAcc                               0.560s    |- 5.68%  

  |- update_dev                           0.381s    |- 3.86%  

  |- Precond                              0.331s    |- 3.36%  

  |- PerfJac                              0.087s    |- 0.88%  

  |- Residual                             0.087s    |- 0.88%  

  |- SanitizeJac                          0.064s    |- 0.65%  

  |- alignvar                             0.051s    |- 0.52%  

  |- HeatLoss                             0.042s    |- 0.43%  

|- Output                                 0.147s  |- 1.46%    

|- Logging                                0.013s  |- 0.13%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.078s  0.77%       

|- execution                              0.063s  |- 80.72%   

------------------------------------------------------------

TOTAL                                    10.137s

============================================================



Time steps : 301/311, step size: 3.63787, 12.3656

```

```
Found 302 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu009_graded_00301.vtu

```

![png]({{ "/assets/images/benchmark_image_101.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_102.png" | relative_url }})

### stflu010.dat 

incomp gas

```
Running simulation [simuapp]: Incomp GAS

Elapsed: 0.27s



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-15





[MarkAir.local:16011] shmem: mmap: an error occurred while determining whether or not /var/folders/zj/_m6vvrd158z_rx15qsbyk6c40000gn/T//ompi.MarkAir.501/jf.0/3150315520/sm_segment.MarkAir.501.bbc60000.0 could be created.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1 6.94e-06  4    6.9e-06     0.02                                                 9e-04             0.000  436.861 1.85e-07    0.074

     2 4.14e-06  1    1.1e-05     0.02                                                  0.00             0.373  197.007 8.35e-08    0.033

     3 4.18e-06  1    1.5e-05                                                           0.00             3.251  196.977 8.35e-08    0.033

     4 4.21e-06  1    1.9e-05     0.01                                                  0.00             2.284   75.283 3.19e-08    0.013

     5 6.55e-06  1    2.6e-05    9e-04                                                  0.00             1.546   22.974 9.74e-09    0.004

     6 1.32e-05  1    3.9e-05    2e-04                                                  0.00             0.927    8.798 3.81e-09    0.001

     7 2.92e-05  1    6.8e-05    7e-05                                                  0.00             0.500    2.196 1.12e-09  6.0e-04

     8 6.71e-05  1    1.4e-04    2e-05                                                  0.00             0.246    0.528 6.61e-10    0.002

     9 1.56e-04  1    2.9e-04    1e-05                                                  0.00             0.075    0.167 1.07e-09    0.005

    10 3.64e-04  1    6.6e-04    9e-06                                                  0.00             0.080    0.039 2.28e-09    0.012

    11 8.48e-04  1      0.002    9e-06                                                  0.00             0.314    0.001 4.92e-09    0.025

    12 1.74e-03  1      0.003    9e-06                                                  0.00             0.716    0.015 8.97e-09    0.046

    13 1.74e-03  1      0.005    1e-05                                                  0.00             0.876    0.032 8.72e-09    0.044

    14 1.74e-03  1      0.007    1e-05                                                  0.00             0.987    0.037 8.80e-09    0.045

    15 2.33e-04  1      0.007    1e-05                                                  0.00             0.953    0.046 1.40e-09    0.007

invalid bhp after event update

```

![png]({{ "/assets/images/benchmark_image_103.png" | relative_url }})

### SAGD

#### 2D cross the well

```
Running simulation [simuapp]: SAGD

Elapsed: 2.28s

   210   4.4311  1   2526.000     6.50             44.29             87.20                      38.27    0.955    2.969   0.0576    1.720



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.029s  97.15%      

|- Newton                                 1.962s  |- 96.70%   

  |- Solver                               0.570s    |- 29.04% 

  |- Update                               0.502s    |- 25.57% 

  |- FluxJac                              0.395s    |- 20.13% 

  |- ScdAcc                               0.149s    |- 7.59%  

  |- Precond                              0.138s    |- 7.05%  

  |- update_dev                           0.084s    |- 4.26%  

  |- SanitizeJac                          0.032s    |- 1.64%  

  |- PerfJac                              0.022s    |- 1.11%  

  |- alignvar                             0.021s    |- 1.09%  

  |- Residual                             0.018s    |- 0.92%  

  |- HeatLoss                             0.004s    |- 0.20%  

|- Output                                 0.043s  |- 2.13%    

|- Logging                                0.008s  |- 0.41%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.059s  2.85%       

|- execution                              0.057s  |- 95.55%   

------------------------------------------------------------

TOTAL                                     2.088s

============================================================



Time steps : 210/213, step size: 12.0286, 13.0987

```

![png]({{ "/assets/images/benchmark_image_104.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_105.png" | relative_url }})

#### 2D along well

```
Running simulation [simuapp]: SAGD

Elapsed: 20.16s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 19.942s  99.77%      

|- Newton                                19.512s  |- 97.85%   

  |- Solver                               9.470s    |- 48.53% 

  |- FluxJac                              3.047s    |- 15.61% 

  |- Update                               2.985s    |- 15.30% 

  |- ScdAcc                               1.297s    |- 6.65%  

  |- Precond                              0.911s    |- 4.67%  

  |- update_dev                           0.806s    |- 4.13%  

  |- SanitizeJac                          0.249s    |- 1.27%  

  |- PerfJac                              0.246s    |- 1.26%  

  |- alignvar                             0.174s    |- 0.89%  

  |- Residual                             0.110s    |- 0.57%  

  |- HeatLoss                             0.049s    |- 0.25%  

|- Output                                 0.123s  |- 0.62%    

|- Logging                                0.047s  |- 0.24%    

|- Input                                  0.001s  |- 0.00%    

Initialization                            0.046s  0.23%       

|- execution                              0.044s  |- 94.81%   

------------------------------------------------------------

TOTAL                                    19.988s

============================================================



Time steps : 344/460, step size: 5.75104, 7.12177

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

# Speed



`-DCMAKE_BUILD_TYPE=Release`

### Dome corner grid

```
Running simulation [simuapp]: Dome Corner point

Elapsed: 16.11s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 15.868s  99.59%      

|- Newton                                15.857s  |- 99.93%   

  |- Solver                              11.367s    |- 71.69% 

  |- FluxJac                              1.682s    |- 10.61% 

  |- Update                               1.613s    |- 10.17% 

  |- ScdAcc                               0.447s    |- 2.82%  

  |- update_dev                           0.255s    |- 1.61%  

  |- Precond                              0.221s    |- 1.39%  

  |- HeatLoss                             0.065s    |- 0.41%  

  |- Residual                             0.055s    |- 0.35%  

  |- alignvar                             0.036s    |- 0.23%  

  |- SanitizeJac                          0.035s    |- 0.22%  

  |- PerfJac                              0.006s    |- 0.04%  

|- Logging                                0.008s  |- 0.05%    

|- Output                                 0.004s  |- 0.02%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.065s  0.41%       

|- execution                              0.057s  |- 86.43%   

------------------------------------------------------------

TOTAL                                    15.934s

============================================================



Time steps : 25/41, step size: 0.681722, 1.43466

```

```
Found 3 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu018_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_113.png" | relative_url }})

## Heterogeneous

### SPE10 benchmark 2D 

```
Running simulation [simuapp]: SPE10 benchmark 2D water flooding 375 days ~7s single thread (OMP_NUM_THREADS=8)

Elapsed: 3.01s

    79   5.8793  1    375.000    19.22              0.00              0.02                      19.50   13.382    2.367   0.1488    0.005



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.765s  97.48%      

|- Newton                                 2.677s  |- 96.82%   

  |- Update                               0.831s    |- 31.05% 

  |- FluxJac                              0.666s    |- 24.88% 

  |- Solver                               0.641s    |- 23.95% 

  |- ScdAcc                               0.183s    |- 6.84%  

  |- update_dev                           0.099s    |- 3.71%  

  |- Precond                              0.075s    |- 2.79%  

  |- PerfJac                              0.074s    |- 2.77%  

  |- Residual                             0.037s    |- 1.39%  

  |- alignvar                             0.014s    |- 0.51%  

  |- SanitizeJac                          0.011s    |- 0.41%  

  |- HeatLoss                             0.006s    |- 0.23%  

|- Output                                 0.057s  |- 2.05%    

|- Logging                                0.003s  |- 0.12%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.071s  2.52%       

|- execution                              0.064s  |- 89.75%   

------------------------------------------------------------

TOTAL                                     2.836s

============================================================



Time steps : 79/79, step size: 4.74684, 2.39153

```

![png]({{ "/assets/images/benchmark_image_114.png" | relative_url }})

### Medium size



* 202,005 grid block (201x201x5) with heterogeneous permeability

* 61 wells water flooding pattern 

* 1500 days

```
Running simulation [simuapp]: Heterogeneous + 61wells - performance test medium size ~3m.50s (Single) (OMP_NUM_THREADS=8)

Elapsed: 110.53s

    36  23.9824  2    365.000   257.96              0.02              0.01                     719.91    0.012  254.602   0.0819    1.572



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                               1m 49.54s  99.38%      

|- Newton                              1m 48.52s  |- 99.07%   

  |- Update                              32.164s    |- 29.64% 

  |- FluxJac                             30.332s    |- 27.95% 

  |- Solver                              27.087s    |- 24.96% 

  |- ScdAcc                               7.010s    |- 6.46%  

  |- update_dev                           3.766s    |- 3.47%  

  |- Precond                              2.901s    |- 2.67%  

  |- Residual                             1.598s    |- 1.47%  

  |- HeatLoss                             0.904s    |- 0.83%  

  |- PerfJac                              0.545s    |- 0.50%  

  |- alignvar                             0.368s    |- 0.34%  

  |- SanitizeJac                          0.181s    |- 0.17%  

|- Output                                 0.660s  |- 0.60%    

|- Logging                                0.005s  |- 0.00%    

|- Input                                  0.002s  |- 0.00%    

Initialization                            0.681s  0.62%       

|- execution                              0.545s  |- 80.02%   

------------------------------------------------------------

TOTAL                                  1m 50.22s

============================================================



Time steps : 36/36, step size: 10.1389, 10.6136

```

### Johnansen water flooding

```
Running simulation [simuapp]: Johnansen water flooding takes ~5m on M2 (OMP_NUM_THREADS=8)

Elapsed: 23.86s

    17 365.0000  1   3650.000   353.53              0.07              0.02                     188.86    0.000    3.269   0.0067  3.1e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 22.643s  96.44%      

|- Newton                                22.511s  |- 99.42%   

  |- Solver                               6.999s    |- 31.09% 

  |- Update                               6.257s    |- 27.80% 

  |- FluxJac                              6.072s    |- 26.97% 

  |- ScdAcc                               1.188s    |- 5.28%  

  |- update_dev                           0.703s    |- 3.12%  

  |- Precond                              0.577s    |- 2.56%  

  |- Residual                             0.310s    |- 1.38%  

  |- alignvar                             0.080s    |- 0.36%  

  |- SanitizeJac                          0.031s    |- 0.14%  

  |- PerfJac                              0.002s    |- 0.01%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.093s  |- 0.41%    

|- Logging                                0.002s  |- 0.01%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.836s  3.56%       

|- execution                              0.522s  |- 62.51%   

------------------------------------------------------------

TOTAL                                    23.478s

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

Elapsed: 1.03s

    49  33.9643  1   3650.000     0.06              4.15             98.68                       4.70    0.226    8.451   0.0491    3.702



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.763s  89.50%      

|- Newton                                 0.742s  |- 97.25%   

  |- FluxJac                              0.303s    |- 40.80% 

  |- Update                               0.172s    |- 23.13% 

  |- Solver                               0.092s    |- 12.45% 

  |- ScdAcc                               0.074s    |- 9.93%  

  |- update_dev                           0.053s    |- 7.16%  

  |- PerfJac                              0.019s    |- 2.51%  

  |- Precond                              0.011s    |- 1.43%  

  |- alignvar                             0.004s    |- 0.53%  

  |- Residual                             0.003s    |- 0.46%  

  |- HeatLoss                             0.003s    |- 0.40%  

  |- SanitizeJac                          0.001s    |- 0.09%  

|- Output                                 0.014s  |- 1.87%    

|- Logging                                0.002s  |- 0.32%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.089s  10.50%      

|- execution                              0.086s  |- 96.39%   

------------------------------------------------------------

TOTAL                                     0.852s

============================================================



Time steps : 49/50, step size: 74.4898, 69.7484

Running simulation [simumpi]: MPI comparison np=1 (OMP_NUM_THREADS=1, np=1)

Elapsed: 1.11s

    28  49.2597  5   1051.785     1.74              5.79             76.85                       5.96    1.330   23.086   0.2367   49.290

    29  43.2152  5   1095.000     1.91              6.06             76.02                       5.97    1.328   26.291   0.2156   62.303

    30  41.3727 13   1136.373     1.85              5.81             75.84                       5.96    1.327   31.366   0.2215   57.360



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    31  38.1902  4   1174.563     1.38              5.22             79.10                       5.96    1.313   47.232   0.1303   23.251

    32  47.6893  6   1222.252     1.22              4.66             79.22                       5.96    1.297   71.383   0.1616   29.275

    33  53.5578  4   1275.810     1.26              4.76             79.08                       5.96    1.277   62.226   0.1370   40.644

    34  65.3182 12   1341.128     2.34              7.33             75.78                       5.96    1.338  263.542   0.2313   87.983

    35  59.9507  6   1401.079     1.97              6.34             76.34                       5.96    1.261   98.685   0.2109   40.710

    36  58.1433  3   1459.222     0.85              4.44             83.90                       5.96    1.227  291.826   0.0783   26.828

    37  89.1510  5   1548.373     0.60              4.54             88.30                       5.96    1.199  174.934   0.1782   20.521

    38  95.0713  3   1643.444     0.46              4.69             91.05                       5.96    1.167  171.233   0.1004   28.081

    39 132.8770  5   1776.321     0.37              4.88             93.02                       5.96    1.134  249.288   0.1704   34.476

    40 145.1705  4   1921.492     0.27              4.87             94.70                       5.96    1.100  313.735   0.1858   40.240

    41 151.3069  4   2072.799     0.22              4.84             95.74                       5.96    1.060  342.773   0.1826   37.032

    42 159.2004  5   2231.999     0.17              4.77             96.50                       5.96    1.025  416.557   0.1679   40.741

    43 175.2506  3   2407.250     0.14              4.70             97.03                       5.96    0.977  464.703   0.1759   23.515

    44 188.1825  3   2595.432     0.12              4.55             97.33                       5.96    0.905  529.533   0.1700   21.109

    45 205.8341  3   2801.266     0.11              4.33             97.56                       5.96    0.918  634.234   0.1310   28.239

    46 256.3410  3   3057.607     0.09              4.25             98.01                       5.96    0.824  837.262   0.1538   32.560

    47 287.6424  5   3345.250     0.05              3.88             98.61                       5.96    0.724  1.1e+03   0.2130   54.655

    48 270.7860  5   3616.036     0.05              3.94             98.71                       4.92    0.643  442.922   0.1723   28.656

    49  33.9643  1   3650.000     0.06              4.15             98.68                       4.70    0.640    8.451   0.0491    3.702

Time steps : 49/50, step size: 74.4898, 69.7484

Running simulation [simumpi]: MPI comparison np=2 (OMP_NUM_THREADS=1, np=2)

Elapsed: 0.82s

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    31  42.9800  5   1095.000     2.29              5.85             71.82                       5.96    0.764   30.956   0.2143   28.943

    32  41.2908  5   1136.291     2.39              6.20             72.20                       5.96    0.764   32.174   0.1656   32.353

    33  45.7874  6   1182.078     2.53              6.32             71.42                       5.96    0.764   49.514   0.1704   55.576

    34  50.0230  6   1232.101     2.40              6.07             71.68                       5.96    0.763   47.438   0.2377   36.719

[rank 0] linear solve failed: DIVERGED_ITS after 500 iterations (residual norm 0.00844097) - the timestep will be cut

[rank 1] linear solve failed: DIVERGED_ITS after 500 iterations (residual norm 0.00844097) - the timestep will be cut

    35  15.0542  3 1 1247.155     2.34              5.93             71.67                       5.96    0.763   23.779   0.0758   11.605

    36  23.3322  4   1270.488     2.37              5.93             71.41                       5.96    0.763   23.609   0.1059   19.789

    37  31.9119  6   1302.399     2.13              5.47             72.02                       5.96    0.762   56.253   0.1702   24.145

    38  34.8854  5   1337.285     1.75              5.15             74.66                       5.96    0.762   62.475   0.1334   29.318

    39  43.0782  4   1380.363     1.39              4.92             77.92                       5.96    0.763   59.737   0.1800   35.855

    40  45.6922  4   1426.055     1.14              5.03             81.60                       5.96    0.763   68.132   0.1526   17.637

    41  52.8504  4   1478.906     0.97              4.98             83.69                       5.96    0.764   79.891   0.1447   19.054

    42  62.7646  5   1541.670     0.79              4.99             86.34                       5.96    0.763  105.013   0.1702   26.553

    43  68.6131  3   1610.283     0.68              5.56             89.16                       5.96    1.465  117.871   0.1552    8.900

    44  78.6818  2   1688.965     0.54              5.06             90.30                       5.96    1.455  133.613   0.0972    6.134

    45 111.4060  2   1800.371     0.43              4.95             91.97                       5.96    1.421  200.743   0.0576    8.164

    46 187.8347  3   1988.206     0.28              4.84             94.57                       5.96    1.306  382.509   0.1279   12.942

    47 236.5662  3   2224.772     0.17              4.78             96.47                       5.96    1.265  564.294   0.0708   15.305

    48 319.5296  5   2544.302     0.09              4.48             98.00                       5.96    1.222  909.438   0.1066   19.177

    49 343.1897  4   2887.491     0.04              4.11             98.97                       5.96    1.137  1.2e+03   0.0690   19.474

    50 313.3052  5   3200.796     0.02              3.50             99.50                       5.96    1.032  1.3e+03   0.0924   17.046

    51 269.3976  6   3470.194     0.01              3.12             99.71                       5.48    0.991  1.0e+03   0.0734   10.995

    52 179.8060  3   3650.000     0.01              4.01             99.71                       4.55    0.968   35.580   0.0819    3.529

Time steps : 52/54, step size: 70.1923, 82.6175

Running simulation [simumpi]: MPI comparison np=4 (OMP_NUM_THREADS=1, np=4)

Elapsed: 0.83s

[rank 3] linear solve failed: DIVERGED_ITS after 500 iterations (residual norm 0.00282522) - the timestep will be cut

[rank 2] linear solve failed: DIVERGED_ITS after 500 iterations (residual norm 0.00282522) - the timestep will be cut

[rank 1] linear solve failed: DIVERGED_ITS after 500 iterations (residual norm 0.00282522) - the timestep will be cut

    36  14.4681  5 1 1175.422     2.49              6.33             71.74                       5.96    0.052   19.022   0.1424   23.936

    37  17.3172  6   1192.739     2.42              6.16             71.75                       5.96    0.052   25.891   0.1412   25.583

    38  20.8163  3   1213.555     2.22              5.80             72.31                       5.96    0.052   16.866   0.1026   13.796

    39  28.8409  4   1242.396     2.20              5.73             72.30                       5.96    0.047   24.355   0.1103   22.289

    40  38.7735  6   1281.169     2.09              5.79             73.46                       5.96    0.177   29.128   0.1550   34.522

[rank 0] linear solve failed: DIVERGED_ITS after 500 iterations (residual norm 0.226523) - the timestep will be cut

[rank 1] linear solve failed: DIVERGED_ITS after 500 iterations (residual norm 0.226523) - the timestep will be cut

[rank 2] linear solve failed: DIVERGED_ITS after 500 iterations (residual norm 0.226523) - the timestep will be cut

[rank 3] linear solve failed: DIVERGED_ITS after 500 iterations (residual norm 0.226523) - the timestep will be cut

    41  14.8330  5 1 1296.003     2.01              5.45             73.03                       5.96    0.177   43.395   0.1145   10.787

    42  19.6263  3   1315.629     1.75              5.22             74.88                       5.96    0.176   35.876   0.0913   16.200

    43  28.4730  3   1344.102     1.48              5.82             79.69                       5.96    0.711   46.583   0.0706   25.959

    44  45.1693  5   1389.271     1.24              5.09             80.41                       5.96    0.704   55.476   0.2136   34.684

    45  43.4837  4   1432.755     1.08              5.03             82.32                       5.96    0.699   64.351   0.1802   17.168

    46  46.0929  4   1478.848     0.93              5.02             84.35                       5.96    0.692   70.752   0.1006   16.395

    47  64.3702  3   1543.218     0.86              5.35             86.15                       5.96    0.785  100.819   0.1168   24.019

    48  84.4431  5   1627.661     0.60              4.88             89.11                       5.96    0.700  140.595   0.1501    7.973

    49  98.4881  3   1726.149     0.47              4.94             91.23                       5.96    0.768  172.551   0.0957    7.541

    50 140.3089  3   1866.458     0.35              4.93             93.45                       5.96    0.752  269.079   0.0625   10.104

    51 231.0475  4   2097.506     0.21              4.79             95.73                       5.96    0.722  513.928   0.0996   15.637

    52 323.9538  5   2421.459     0.11              4.54             97.56                       5.96    0.598  877.496   0.1412   20.311

    53 354.6643  4   2776.124     0.05              4.22             98.76                       5.96    0.573  1.2e+03   0.0738   20.614

    54 327.3413  5   3103.465     0.02              3.67             99.40                       5.96    0.530  1.3e+03   0.1055   17.908

    55 282.5465  6   3386.012     0.01              2.77             99.73                       1.62   15.096  1.5e+03   0.0898   16.260

    56 227.1391  3   3613.151     0.01              4.18             99.71                       4.42   15.012   99.192   0.0950    5.815

    57  36.8493  1   3650.000     0.01              4.50             99.71                       4.59   15.007    9.329   0.0021    0.515

Time steps : 57/61, step size: 64.0351, 83.3919

simuapp          rc=0   0.85s   49/ 50 steps  to  3650.00 days

simumpi np=1     rc=0   0.74s   49/ 50 steps,  1 cuts  to  3650.00 days

simumpi np=2     rc=0   0.53s   52/ 54 steps,  2 cuts  to  3650.00 days

simumpi np=4     rc=0   0.53s   57/ 61 steps,  4 cuts  to  3650.00 days

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

a different `dt` sequence. So the marker series do not share x positions, and np>1 marches more,

smaller steps to reach the same 3650 days (51 steps at np=1, 67 at np=2 and np=4). Every rank

count does reach it; the endpoint column in the table above is the check that they did.



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

Elapsed: 13.35s

   203  49.8497  1   1095.000     2.21              1.35             38.04                               3.147   37.959   0.1857    8.413



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 13.096s  99.55%      

|- Newton                                12.949s  |- 98.88%   

  |- FluxJac                              5.644s    |- 43.58% 

  |- Update                               3.178s    |- 24.54% 

  |- Solver                               1.674s    |- 12.92% 

  |- ScdAcc                               1.165s    |- 9.00%  

  |- update_dev                           0.752s    |- 5.81%  

  |- Precond                              0.208s    |- 1.61%  

  |- alignvar                             0.067s    |- 0.52%  

  |- PerfJac                              0.061s    |- 0.47%  

  |- Residual                             0.060s    |- 0.46%  

  |- HeatLoss                             0.053s    |- 0.41%  

  |- SanitizeJac                          0.012s    |- 0.10%  

|- Output                                 0.121s  |- 0.92%    

|- Logging                                0.008s  |- 0.06%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.059s  0.45%       

|- execution                              0.057s  |- 96.11%   

------------------------------------------------------------

TOTAL                                    13.155s

============================================================



Time steps : 203/209, step size: 5.39409, 15.2107

Running simulation [simumpi]: CSS parity np=1 (OMP_NUM_THREADS=1, np=1)

Elapsed: 11.59s

=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   181   1.0000  6    748.000     2.60             88.40             97.14                               1.520  1.0e+03   0.2637   45.341

   182   0.6146  1    748.615     2.33             96.02             97.63                               1.520  126.575   0.1500    6.962

   183   0.7170  1    749.332    13.55             67.75             83.34                               1.534  106.112   0.1928    4.913

   184   0.7322  1    750.064    12.01             64.31             84.26                               1.549   24.283   0.2237    1.898

   185   0.6858  1    750.750     7.78             51.53             86.88                               1.552  102.712   0.1022    7.187

   186   0.9515  1    751.701     8.26             40.70             83.13                               1.554  103.252   0.0649    5.983

   187   1.5496  1    753.251    12.54             31.94             71.80                               1.566  123.052   0.2011    4.449

   188   1.5449  1    754.796    11.52             30.27             72.44                               1.589   39.033   0.1500    1.708

   189   1.8023  1    756.598    11.34             29.75             72.41                               1.625   12.891   0.1500    0.554

   190   2.1027  1    758.701    11.20             29.26             72.32                               1.678   11.972   0.1500    0.484

   191   2.4532  1    761.154     7.85             32.46             80.53                               1.845   11.400   0.1500    0.455

   192   2.8621  1    764.016     8.13             47.45             85.37                               1.999  141.811   0.1484    5.542

   193   3.3575  1    767.373     7.50             25.62             77.36                               2.040  118.834   0.0995    4.868

   194   4.7099  1    772.083     6.79             17.46             71.99                               2.055  128.389   0.0340    5.313

   195   8.1868  1    780.270     5.58             12.43             69.04                               2.067  146.871   0.0328    7.086

   196  13.7264  1    793.997     4.61              9.96             68.36                               2.215   86.369   0.0776    6.990

   197  21.1074  2    815.104     3.97              7.65             65.80                               2.350   99.152   0.1574   11.651

   198  24.0309  3    839.135     3.19              5.46             63.11                               2.356  112.332   0.0888   12.909

   199  35.2231  1    874.358     2.74              3.97             59.11                               2.374   89.189   0.0775   10.419

   200  54.1834  4    928.541     2.57              3.40             56.95                               2.651   31.426   0.1459    4.549

   201  64.0992  8    992.640     2.31              2.33             50.27                               2.661   72.489   0.1612   10.301

   202  72.0890  5   1064.730     2.21              1.71             43.56                               2.683   57.908   0.1324   10.960

   203  30.2705  1   1095.000     1.93              1.50             43.61                               2.700   16.787   0.0756    5.348

Time steps : 203/208, step size: 5.39409, 15.0286

Running simulation [simumpi]: CSS parity np=2 (OMP_NUM_THREADS=1, np=2)

Elapsed: 6.80s

   177   0.2258  1    747.887     2.32            119.91             98.11                               0.973  196.035   0.1463   21.759

   178   0.2667  1    748.153     2.09            107.95             98.10                               1.017   69.723   0.0976    2.517

   179   0.3770  1    748.530     2.02             85.83             97.70                               1.019  118.233   0.0481    8.406

   180   0.6404  1    749.171     8.53             67.37             88.76                               1.041  114.033   0.1705    7.209



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   181   0.6993  1    749.870     6.19             53.61             89.65                               1.043  114.565   0.0424    8.528

   182   1.1833  1    751.053     7.63             41.90             84.59                               1.050  139.062   0.1049    5.631

   183   1.6250  1    752.678     8.11             39.61             83.00                               1.167   29.917   0.2600    2.591

   184   1.3871  1    754.066     8.51             36.90             81.26                               1.248   39.555   0.2522    1.663

   185   1.2070  1    755.273     6.81             40.54             85.62                               1.339   21.070   0.1420    0.925

   186   1.4467  1    756.719    12.86             38.23             74.83                               1.404   68.018   0.2246    6.592

   187   1.3519  1    758.071     9.65             29.90             75.60                               1.408   89.315   0.0486    7.192

   188   2.3822  1    760.453     8.54             24.71             74.32                               1.412  116.824   0.0274    4.386

   189   4.2381  1    764.691     7.38             19.21             72.25                               1.417  139.621   0.0425    5.766

   190   7.2059  1    771.897     6.15             14.39             70.06                               1.428  162.841   0.0580    6.690

   191  11.7232  1    783.621     4.74             10.14             68.14                               1.440  153.182   0.1182    8.403

   192  15.2983  1    798.919     4.53              9.90             68.62                               1.760   10.831   0.0546    1.591

   193  26.1734  3    825.092     3.55              6.32             64.00                               1.790  153.832   0.0574   15.014

   194  36.6287  1    861.721     2.79              4.34             60.86                               1.808  110.095   0.1874   11.590

   195  38.0014  1    899.722     2.66              4.18             61.10                               2.133   11.882   0.0894    1.607

   196  55.5476  2    955.270     2.37              3.26             57.90                               2.305   55.988   0.0993    6.980

   197  77.9984  3   1033.268     2.11              2.50             54.28                               2.494   49.119   0.1557    7.360

   198  61.7316  3   1095.000     1.99              2.25             53.14                               2.714   17.057   0.0914    3.294

Time steps : 198/203, step size: 5.5303, 16.019

Running simulation [simumpi]: CSS parity np=4 (OMP_NUM_THREADS=1, np=4)

Elapsed: 4.99s

[rank 0] linear solve failed: DIVERGED_ITS after 500 iterations (residual norm 0.536958) - the timestep will be cut

[rank 3] linear solve failed: DIVERGED_ITS after 500 iterations (residual norm 0.536958) - the timestep will be cut

[rank 2] linear solve failed: DIVERGED_ITS after 500 iterations (residual norm 0.536958) - the timestep will be cut

   172   0.3333  6 1  747.333     0.67            141.05             99.53                               1.376  937.963   0.1236   37.829

   173   0.2221  9    747.555     1.17            104.06             98.89                               1.376  266.822   0.0451   16.606

   174   0.2962  1    747.852     7.02            151.52             95.57                               1.378  175.861   0.1483   13.764

   175   0.3475  1    748.199     5.59            108.43             95.10                               1.378  103.375   0.0643    4.746

   176   0.5675  1    748.767     6.76             77.78             92.00                               1.378  125.739   0.0282    5.013

   177   0.9917  1    749.758     8.54             52.11             85.93                               1.378  145.752   0.0446    5.781

   178   1.6663  1    751.425     9.35             42.65             82.02                               1.377  162.996   0.0541    6.184

   179   2.7101  1    754.135     8.77             28.16             76.26                               1.375  176.397   0.0270    6.677

   180   4.3006  1    758.435     7.64             20.74             73.07                               1.374  184.860   0.0227    7.133



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   181   6.7214  1    765.157     6.24             14.91             70.51                               1.374  168.058   0.0275    7.558

   182  10.8298  1    775.987     4.82             10.36             68.24                               1.375  172.552   0.0387    8.707

   183  17.3063  1    793.293     3.77              7.68             67.07                               1.394  121.539   0.2291    8.459

   184  15.9788  1    809.272     3.24              5.94             64.71                               1.393   88.119   0.0424    7.522

   185  27.9423  1    837.214     2.69              4.22             61.02                               1.388   89.097   0.0775    9.099

   186  42.9902  2    880.204     2.33              3.77             61.78                               1.492   32.193   0.1456    4.903

   187  50.9099  3    931.114     2.21              2.98             57.35                               1.574   41.333   0.1540    6.272

   188  58.6180  4    989.732     2.16              2.64             54.91                               1.730   22.884   0.1278    4.206

   189  73.8442  3   1063.576     2.07              2.24             51.91                               1.891   27.631   0.0971    5.217

   190  31.4236  1   1095.000     2.20              2.05             48.20                               1.958   13.856   0.1127    2.742

Time steps : 190/196, step size: 5.76316, 14.5829

simuapp          rc=0  13.15s  203/209 steps  to  1095.00 days

simumpi np=1     rc=0  11.30s  203/208 steps,  5 cuts  to  1095.00 days

simumpi np=2     rc=0   6.53s  198/203 steps,  5 cuts  to  1095.00 days

simumpi np=4     rc=0   4.68s  190/196 steps,  6 cuts  to  1095.00 days

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

Elapsed: 24.74s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 23.436s  96.04%      

|- Newton                                23.279s  |- 99.33%   

  |- FluxJac                              9.122s    |- 39.19% 

  |- Update                               7.634s    |- 32.79% 

  |- Solver                               2.225s    |- 9.56%  

  |- ScdAcc                               2.052s    |- 8.81%  

  |- update_dev                           1.262s    |- 5.42%  

  |- Precond                              0.351s    |- 1.51%  

  |- Residual                             0.164s    |- 0.71%  

  |- alignvar                             0.118s    |- 0.51%  

  |- HeatLoss                             0.081s    |- 0.35%  

  |- PerfJac                              0.048s    |- 0.21%  

  |- SanitizeJac                          0.035s    |- 0.15%  

|- Output                                 0.083s  |- 0.36%    

|- Logging                                0.001s  |- 0.00%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.966s  3.96%       

|- execution                              0.828s  |- 85.67%   

------------------------------------------------------------

TOTAL                                    24.403s

============================================================



Time steps : 4/4, step size: 0.129526, 0.0271065

Running simulation [simuapp]: scaling baseline (attempt 2/2) (OMP_NUM_THREADS=1)

Elapsed: 24.67s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 23.506s  96.49%      

|- Newton                                23.372s  |- 99.43%   

  |- FluxJac                              9.170s    |- 39.23% 

  |- Update                               7.726s    |- 33.06% 

  |- Solver                               2.173s    |- 9.30%  

  |- ScdAcc                               2.040s    |- 8.73%  

  |- update_dev                           1.254s    |- 5.37%  

  |- Precond                              0.359s    |- 1.53%  

  |- Residual                             0.162s    |- 0.69%  

  |- alignvar                             0.117s    |- 0.50%  

  |- HeatLoss                             0.087s    |- 0.37%  

  |- PerfJac                              0.049s    |- 0.21%  

  |- SanitizeJac                          0.036s    |- 0.15%  

|- Output                                 0.061s  |- 0.26%    

|- Logging                                0.001s  |- 0.00%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.855s  3.51%       

|- execution                              0.715s  |- 83.62%   

------------------------------------------------------------

TOTAL                                    24.361s

============================================================



Time steps : 4/4, step size: 0.129526, 0.0271065

Running simulation [simumpi]: scaling np=1 (attempt 1/2) (OMP_NUM_THREADS=1, np=1)

Elapsed: 24.99s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-15







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.61             20.31              3.30                     720.00    0.000  375.000   0.0027    0.111

     2   0.1167  1      0.217   497.90             26.53              5.06                     720.00    0.000  358.750   0.0032    0.123

     3   0.1391  1      0.356   426.44             27.34              6.03                     720.22    0.000  375.000   0.0037    0.139

     4   0.1623  1      0.518   376.68             25.84              6.42                     720.00    0.000  367.634   0.0042    0.158





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129526, 0.0271065

Running simulation [simumpi]: scaling np=1 (attempt 2/2) (OMP_NUM_THREADS=1, np=1)

Elapsed: 24.58s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-15







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.61             20.31              3.30                     720.00    0.000  375.000   0.0027    0.111

     2   0.1167  1      0.217   497.90             26.53              5.06                     720.00    0.000  358.750   0.0032    0.123

     3   0.1391  1      0.356   426.44             27.34              6.03                     720.22    0.000  375.000   0.0037    0.139

     4   0.1623  1      0.518   376.68             25.84              6.42                     720.00    0.000  367.634   0.0042    0.158





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129526, 0.0271065

Running simulation [simumpi]: scaling np=2 (attempt 1/2) (OMP_NUM_THREADS=1, np=2)

Elapsed: 13.44s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-15







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.63             20.31              3.30                     720.00    0.000  375.000   0.0027    0.111

     2   0.1167  1      0.217   497.91             26.52              5.06                     720.00    0.000  358.735   0.0032    0.123

     3   0.1391  1      0.356   426.45             27.34              6.03                     720.22    0.000  375.000   0.0037    0.139

     4   0.1623  1      0.518   376.69             25.84              6.42                     720.00    0.000  367.622   0.0042    0.158





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129528, 0.0271081

Running simulation [simumpi]: scaling np=2 (attempt 2/2) (OMP_NUM_THREADS=1, np=2)

Elapsed: 13.31s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-15







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.63             20.31              3.30                     720.00    0.000  375.000   0.0027    0.111

     2   0.1167  1      0.217   497.91             26.52              5.06                     720.00    0.000  358.735   0.0032    0.123

     3   0.1391  1      0.356   426.45             27.34              6.03                     720.22    0.000  375.000   0.0037    0.139

     4   0.1623  1      0.518   376.69             25.84              6.42                     720.00    0.000  367.622   0.0042    0.158





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129528, 0.0271081

Running simulation [simumpi]: scaling np=4 (attempt 1/2) (OMP_NUM_THREADS=1, np=4)

Elapsed: 8.12s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-15







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.61             20.31              3.30                     720.00    0.000  375.000   0.0027    0.111

     2   0.1167  1      0.217   497.90             26.53              5.06                     720.00    0.000  358.748   0.0032    0.123

     3   0.1391  1      0.356   426.44             27.34              6.03                     720.22    0.000  375.000   0.0037    0.139

     4   0.1623  1      0.518   376.68             25.84              6.42                     720.00    0.000  367.613   0.0042    0.158





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129527, 0.0271067

Running simulation [simumpi]: scaling np=4 (attempt 2/2) (OMP_NUM_THREADS=1, np=4)

Elapsed: 8.37s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-15







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.61             20.31              3.30                     720.00    0.000  375.000   0.0027    0.111

     2   0.1167  1      0.217   497.90             26.53              5.06                     720.00    0.000  358.748   0.0032    0.123

     3   0.1391  1      0.356   426.44             27.34              6.03                     720.22    0.000  375.000   0.0037    0.139

     4   0.1623  1      0.518   376.68             25.84              6.42                     720.00    0.000  367.613   0.0042    0.158





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129527, 0.0271067

Running simulation [simumpi]: scaling np=8 (attempt 1/2) (OMP_NUM_THREADS=1, np=8)

Elapsed: 7.25s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-15







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.62             20.31              3.30                     720.00    0.000  375.000   0.0027    0.111

     2   0.1167  1      0.217   497.91             26.52              5.06                     719.99    0.000  358.777   0.0032    0.123

     3   0.1391  1      0.356   426.46             27.34              6.02                     720.22    0.000  375.000   0.0037    0.139

     4   0.1623  1      0.518   376.69             25.84              6.42                     720.00    0.000  367.595   0.0042    0.158





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129524, 0.0271035

Running simulation [simumpi]: scaling np=8 (attempt 2/2) (OMP_NUM_THREADS=1, np=8)

Elapsed: 7.34s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-15







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.62             20.31              3.30                     720.00    0.000  375.000   0.0027    0.111

     2   0.1167  1      0.217   497.91             26.52              5.06                     719.99    0.000  358.777   0.0032    0.123

     3   0.1391  1      0.356   426.46             27.34              6.02                     720.22    0.000  375.000   0.0037    0.139

     4   0.1623  1      0.518   376.69             25.84              6.42                     720.00    0.000  367.595   0.0042    0.158





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129524, 0.0271035

```

![png]({{ "/assets/images/benchmark_image_126.png" | relative_url }})

```
   config  steps   seconds   speedup   effic.  cells/rank   ghosts

  simuapp      4     24.36         -        -           -        -

     np=1      4     22.82     1.00x     100%      202005        0

     np=2      4     11.98     1.91x      95%      101080     2110

     np=4      4      6.95     3.28x      82%       50520     4235

     np=8      4      5.65     4.04x      50%       25610     8325 *

  * more ranks than the 4 fast cores on this CPU - paced by the slow ones, so read the efficiency as the machine's, not the partition's

```

```
Script completed at: 2026-10-15 20:11:54

```
