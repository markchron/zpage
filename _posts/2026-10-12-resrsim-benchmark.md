---
layout: default
title: "Benchmark results of resrsim"
date: 2026-10-12
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

Elapsed: 0.76s

    25  55.0000  1   3650.000    47.50              1.87              3.78                      29.98    0.000   39.341 4.30e-04    0.029



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.329s  68.19%      

|- Newton                                 0.300s  |- 91.37%   

  |- Update                               0.129s    |- 42.81% 

  |- FluxJac                              0.070s    |- 23.21% 

  |- ScdAcc                               0.031s    |- 10.41% 

  |- Solver                               0.022s    |- 7.22%  

  |- update_dev                           0.015s    |- 4.89%  

  |- Precond                              0.012s    |- 4.15%  

  |- Residual                             0.007s    |- 2.43%  

  |- alignvar                             0.002s    |- 0.71%  

  |- SanitizeJac                          0.002s    |- 0.69%  

  |- PerfJac                              0.002s    |- 0.54%  

  |- HeatLoss                             0.001s    |- 0.38%  

|- Output                                 0.018s  |- 5.58%    

|- Logging                                0.001s  |- 0.34%    

|- Input                                  0.000s  |- 0.04%    

Initialization                            0.153s  31.81%      

|- execution                              0.138s  |- 90.23%   

------------------------------------------------------------

TOTAL                                     0.482s

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

Elapsed: 0.66s

    51 338.8120  3   3650.000     0.01              3.51             99.64                       5.81    9.672  840.053   0.0802    9.586



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.429s  86.91%      

|- Newton                                 0.407s  |- 94.69%   

  |- Update                               0.118s    |- 28.98% 

  |- FluxJac                              0.098s    |- 24.17% 

  |- Solver                               0.062s    |- 15.20% 

  |- ScdAcc                               0.035s    |- 8.62%  

  |- Precond                              0.025s    |- 6.19%  

  |- update_dev                           0.021s    |- 5.27%  

  |- PerfJac                              0.017s    |- 4.13%  

  |- SanitizeJac                          0.007s    |- 1.73%  

  |- alignvar                             0.005s    |- 1.18%  

  |- Residual                             0.004s    |- 0.91%  

  |- HeatLoss                             0.003s    |- 0.77%  

|- Output                                 0.015s  |- 3.58%    

|- Logging                                0.005s  |- 1.26%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.065s  13.09%      

|- execution                              0.060s  |- 92.78%   

------------------------------------------------------------

TOTAL                                     0.494s

============================================================



Time steps : 51/51, step size: 71.5686, 94.1896

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

### Corner grid

```
Running simulation [simuapp]: Corner Grid

Elapsed: 2.13s

   113  37.9918 11   3650.000     0.18              6.43             97.32                       5.96    9.587  119.083   0.2443    6.532



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.882s  96.52%      

|- Newton                                 1.828s  |- 97.11%   

  |- Update                               0.484s    |- 26.47% 

  |- FluxJac                              0.418s    |- 22.85% 

  |- Solver                               0.370s    |- 20.24% 

  |- ScdAcc                               0.153s    |- 8.40%  

  |- Precond                              0.114s    |- 6.24%  

  |- update_dev                           0.094s    |- 5.17%  

  |- PerfJac                              0.071s    |- 3.86%  

  |- SanitizeJac                          0.032s    |- 1.74%  

  |- alignvar                             0.022s    |- 1.19%  

  |- Residual                             0.015s    |- 0.81%  

  |- HeatLoss                             0.014s    |- 0.76%  

|- Output                                 0.037s  |- 1.96%    

|- Logging                                0.018s  |- 0.97%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.068s  3.48%       

|- execution                              0.065s  |- 95.76%   

------------------------------------------------------------

TOTAL                                     1.950s

============================================================



Time steps : 113/137, step size: 32.3009, 34.3542

```

![png]({{ "/assets/images/benchmark_image_36.png" | relative_url }})

# Buckley- Leverett



Two phase, isothermal problem

variable order: [Sw, P, T, So, X0, X1, Sg]



Acc w.r.t. [Sw, So, Sg, X0, X1, P, T]

```
Running simulation [simuapp]: Buckley-Leverett

Elapsed: 0.52s

    78   4.7172  1     10.000                       0.16            100.00                       0.16   33.905    0.002 7.15e-06  1.4e-05



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.294s  83.20%      

|- Newton                                 0.270s  |- 91.91%   

  |- Update                               0.095s    |- 35.12% 

  |- FluxJac                              0.040s    |- 14.95% 

  |- Solver                               0.031s    |- 11.36% 

  |- ScdAcc                               0.026s    |- 9.74%  

  |- Precond                              0.025s    |- 9.15%  

  |- update_dev                           0.013s    |- 4.78%  

  |- PerfJac                              0.012s    |- 4.43%  

  |- SanitizeJac                          0.008s    |- 2.79%  

  |- HeatLoss                             0.006s    |- 2.08%  

  |- alignvar                             0.005s    |- 1.84%  

  |- Residual                             0.004s    |- 1.37%  

|- Output                                 0.016s  |- 5.35%    

|- Logging                                0.003s  |- 0.85%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.059s  16.80%      

|- execution                              0.057s  |- 96.12%   

------------------------------------------------------------

TOTAL                                     0.354s

============================================================



Time steps : 78/79, step size: 0.128205, 0.636868

```

### Load Benchmark

### Buckley Plot

![png]({{ "/assets/images/benchmark_image_37.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_38.png" | relative_url }})

# MISC

## spe04b_cw.dat

```
Running simulation [simuapp]: SPE4-b water flooding

Elapsed: 0.44s

    25 330.8312  1   3650.000     0.78             10.17             92.88                      10.73    0.982   28.161   0.0307    0.004



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.193s  76.21%      

|- Newton                                 0.181s  |- 93.83%   

  |- Update                               0.069s    |- 38.01% 

  |- FluxJac                              0.048s    |- 26.50% 

  |- Solver                               0.022s    |- 12.15% 

  |- ScdAcc                               0.014s    |- 7.65%  

  |- Precond                              0.009s    |- 5.19%  

  |- update_dev                           0.007s    |- 3.97%  

  |- Residual                             0.003s    |- 1.48%  

  |- PerfJac                              0.003s    |- 1.41%  

  |- SanitizeJac                          0.002s    |- 1.07%  

  |- alignvar                             0.002s    |- 0.86%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.008s  |- 4.41%    

|- Logging                                0.001s  |- 0.33%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.060s  23.79%      

|- execution                              0.058s  |- 95.92%   

------------------------------------------------------------

TOTAL                                     0.253s

============================================================



Time steps : 25/25, step size: 146, 149.392

```



## watfld_cw.dat

```
Running simulation [simuapp]: SPE4-b Water flooding without vmod

Elapsed: 0.56s

    38  40.9777  1   3650.000     1.04             78.98             98.70                      80.00    3.287    1.793   0.0038  4.6e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.333s  85.13%      

|- Newton                                 0.311s  |- 93.35%   

  |- Update                               0.110s    |- 35.31% 

  |- FluxJac                              0.084s    |- 27.19% 

  |- Solver                               0.041s    |- 13.06% 

  |- ScdAcc                               0.022s    |- 6.95%  

  |- PerfJac                              0.014s    |- 4.44%  

  |- Precond                              0.014s    |- 4.36%  

  |- update_dev                           0.012s    |- 3.73%  

  |- Residual                             0.004s    |- 1.28%  

  |- SanitizeJac                          0.004s    |- 1.14%  

  |- alignvar                             0.002s    |- 0.71%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.015s  |- 4.51%    

|- Logging                                0.001s  |- 0.43%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.058s  14.87%      

|- execution                              0.055s  |- 95.25%   

------------------------------------------------------------

TOTAL                                     0.391s

============================================================



Time steps : 38/38, step size: 96.0526, 135.309

```

## stflu001.dat

Inverted 9 spot water flooding with area/block modifier, 5 point transmissibility


```
Running simulation [simuapp]: Inverted 9 spot water flooding

Elapsed: 1.03s

   202  79.4173  6   3650.000     0.07            140.76             99.95                     138.21   39.900   88.641   0.1125    2.631



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.816s  93.92%      

|- Newton                                 0.749s  |- 91.69%   

  |- Update                               0.258s    |- 34.51% 

  |- FluxJac                              0.195s    |- 25.99% 

  |- ScdAcc                               0.070s    |- 9.31%  

  |- Precond                              0.062s    |- 8.30%  

  |- Solver                               0.054s    |- 7.17%  

  |- update_dev                           0.041s    |- 5.51%  

  |- SanitizeJac                          0.018s    |- 2.44%  

  |- alignvar                             0.011s    |- 1.48%  

  |- PerfJac                              0.010s    |- 1.38%  

  |- Residual                             0.008s    |- 1.09%  

  |- HeatLoss                             0.006s    |- 0.79%  

|- Output                                 0.049s  |- 6.04%    

|- Logging                                0.008s  |- 0.98%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.053s  6.08%       

|- execution                              0.050s  |- 95.10%   

------------------------------------------------------------

TOTAL                                     0.869s

============================================================



Time steps : 202/204, step size: 18.0693, 61.317

```

## stflu002.dat

5000x5000x50, 2D diagonal water flooding in uniformed cartesian

```
Running simulation [simuapp]: Uniformed cartesian water flooding

Elapsed: 0.44s

    46  56.9256  2   3650.000   715.28              1.74              0.24                     635.95   44.366  750.000   0.0030    0.020



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.214s  78.04%      

|- Newton                                 0.199s  |- 92.80%   

  |- Update                               0.058s    |- 29.04% 

  |- Solver                               0.042s    |- 21.02% 

  |- FluxJac                              0.036s    |- 18.16% 

  |- Precond                              0.016s    |- 8.09%  

  |- ScdAcc                               0.015s    |- 7.42%  

  |- update_dev                           0.007s    |- 3.69%  

  |- PerfJac                              0.007s    |- 3.58%  

  |- SanitizeJac                          0.005s    |- 2.47%  

  |- alignvar                             0.003s    |- 1.63%  

  |- HeatLoss                             0.003s    |- 1.42%  

  |- Residual                             0.002s    |- 1.03%  

|- Output                                 0.010s  |- 4.70%    

|- Logging                                0.002s  |- 0.70%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.060s  21.96%      

|- execution                              0.057s  |- 94.78%   

------------------------------------------------------------

TOTAL                                     0.274s

============================================================



Time steps : 46/46, step size: 79.3478, 130.449

```



## stflu003.dat

5000x5000x50, 2D diagonal water flooding in uniformed corner point

```
Running simulation [simuapp]: uniformed corner grid

Elapsed: 0.38s

    42 125.6950  2   3650.000   631.01              4.94              0.78                     642.05   41.030  750.000   0.0151    0.020



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.165s  76.79%      

|- Newton                                 0.152s  |- 92.01%   

  |- Update                               0.047s    |- 30.74% 

  |- Solver                               0.029s    |- 19.13% 

  |- FluxJac                              0.029s    |- 18.85% 

  |- ScdAcc                               0.011s    |- 7.49%  

  |- Precond                              0.011s    |- 7.36%  

  |- update_dev                           0.006s    |- 3.82%  

  |- PerfJac                              0.006s    |- 3.71%  

  |- SanitizeJac                          0.003s    |- 2.15%  

  |- HeatLoss                             0.002s    |- 1.47%  

  |- alignvar                             0.002s    |- 1.31%  

  |- Residual                             0.002s    |- 1.10%  

|- Output                                 0.009s  |- 5.28%    

|- Logging                                0.001s  |- 0.90%    

|- Input                                  0.000s  |- 0.04%    

Initialization                            0.050s  23.21%      

|- execution                              0.046s  |- 91.70%   

------------------------------------------------------------

TOTAL                                     0.214s

============================================================



Time steps : 42/42, step size: 86.9048, 138.299

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

Elapsed: 0.51s

    53 311.3861  1   3650.000   634.73              0.94              0.15                     635.95   61.649  375.000   0.0373    0.016



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.288s  84.72%      

|- Newton                                 0.271s  |- 94.11%   

  |- Update                               0.112s    |- 41.21% 

  |- FluxJac                              0.051s    |- 18.79% 

  |- Solver                               0.042s    |- 15.32% 

  |- ScdAcc                               0.019s    |- 7.09%  

  |- Precond                              0.014s    |- 5.06%  

  |- update_dev                           0.009s    |- 3.46%  

  |- PerfJac                              0.005s    |- 1.92%  

  |- HeatLoss                             0.004s    |- 1.64%  

  |- Residual                             0.004s    |- 1.35%  

  |- SanitizeJac                          0.003s    |- 1.25%  

  |- alignvar                             0.002s    |- 0.92%  

|- Output                                 0.011s  |- 3.94%    

|- Logging                                0.001s  |- 0.45%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.052s  15.28%      

|- execution                              0.049s  |- 94.87%   

------------------------------------------------------------

TOTAL                                     0.340s

============================================================



Time steps : 53/53, step size: 68.8679, 122.446

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

Elapsed: 1.26s

    48 278.1405  2   3650.000   588.86              2.21              0.37                     635.95   60.296  698.996   0.0561    0.032



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.030s  94.21%      

|- Newton                                 1.004s  |- 97.48%   

  |- Solver                               0.336s    |- 33.43% 

  |- FluxJac                              0.250s    |- 24.94% 

  |- Update                               0.240s    |- 23.91% 

  |- ScdAcc                               0.055s    |- 5.52%  

  |- Precond                              0.032s    |- 3.19%  

  |- update_dev                           0.030s    |- 2.99%  

  |- HeatLoss                             0.013s    |- 1.32%  

  |- Residual                             0.010s    |- 0.95%  

  |- SanitizeJac                          0.009s    |- 0.85%  

  |- PerfJac                              0.007s    |- 0.74%  

  |- alignvar                             0.006s    |- 0.57%  

|- Output                                 0.018s  |- 1.75%    

|- Logging                                0.004s  |- 0.42%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.063s  5.79%       

|- execution                              0.052s  |- 82.13%   

------------------------------------------------------------

TOTAL                                     1.094s

============================================================



Time steps : 48/48, step size: 76.0417, 129.207

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

Elapsed: 2.07s

   131   3.0770  1   3650.000     0.01              4.64             99.88                       4.61   10.517    0.416 1.98e-04    0.064



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.838s  97.10%      

|- Newton                                 1.776s  |- 96.66%   

  |- Solver                               0.575s    |- 32.39% 

  |- FluxJac                              0.360s    |- 20.26% 

  |- Update                               0.357s    |- 20.11% 

  |- ScdAcc                               0.150s    |- 8.46%  

  |- Precond                              0.117s    |- 6.61%  

  |- update_dev                           0.072s    |- 4.03%  

  |- PerfJac                              0.044s    |- 2.49%  

  |- SanitizeJac                          0.032s    |- 1.82%  

  |- alignvar                             0.020s    |- 1.14%  

  |- Residual                             0.010s    |- 0.56%  

  |- HeatLoss                             0.010s    |- 0.56%  

|- Output                                 0.042s  |- 2.30%    

|- Logging                                0.012s  |- 0.65%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.055s  2.90%       

|- execution                              0.052s  |- 95.01%   

------------------------------------------------------------

TOTAL                                     1.893s

============================================================



Time steps : 131/141, step size: 27.8626, 52.2968

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

Elapsed: 0.54s

   111  73.1734  1   1095.000     0.99              0.24             19.32                               0.494   10.811   0.0847    2.650



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.300s  81.59%      

|- Newton                                 0.261s  |- 86.79%   

  |- Update                               0.089s    |- 34.01% 

  |- FluxJac                              0.038s    |- 14.62% 

  |- PerfJac                              0.031s    |- 11.91% 

  |- Precond                              0.028s    |- 10.88% 

  |- ScdAcc                               0.022s    |- 8.60%  

  |- Solver                               0.013s    |- 4.91%  

  |- update_dev                           0.011s    |- 4.34%  

  |- SanitizeJac                          0.010s    |- 3.65%  

  |- alignvar                             0.006s    |- 2.25%  

  |- Residual                             0.002s    |- 0.90%  

  |- HeatLoss                             0.002s    |- 0.60%  

|- Output                                 0.026s  |- 8.74%    

|- Logging                                0.004s  |- 1.27%    

|- Input                                  0.001s  |- 0.21%    

Initialization                            0.068s  18.41%      

|- execution                              0.065s  |- 95.72%   

------------------------------------------------------------

TOTAL                                     0.368s

============================================================



Time steps : 111/111, step size: 9.86486, 21.5585

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

Elapsed: 5.25s

   190   5.1482  1   1095.000     2.04              1.76             46.23                               2.047    5.862   0.1004    0.888



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  5.015s  98.79%      

|- Newton                                 4.867s  |- 97.05%   

  |- Update                               1.542s    |- 31.69% 

  |- FluxJac                              1.441s    |- 29.61% 

  |- Solver                               0.934s    |- 19.19% 

  |- ScdAcc                               0.333s    |- 6.84%  

  |- update_dev                           0.174s    |- 3.57%  

  |- Precond                              0.161s    |- 3.31%  

  |- Residual                             0.057s    |- 1.17%  

  |- PerfJac                              0.050s    |- 1.03%  

  |- HeatLoss                             0.047s    |- 0.98%  

  |- SanitizeJac                          0.032s    |- 0.66%  

  |- alignvar                             0.030s    |- 0.61%  

|- Output                                 0.114s  |- 2.28%    

|- Logging                                0.008s  |- 0.17%    

|- Input                                  0.001s  |- 0.02%    

Initialization                            0.061s  1.21%       

|- execution                              0.059s  |- 96.10%   

------------------------------------------------------------

TOTAL                                     5.076s

============================================================



Time steps : 190/191, step size: 5.76316, 15.511

```

```
Found 191 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu008_00190.vtu

```

![png]({{ "/assets/images/benchmark_image_96.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_97.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_98.png" | relative_url }})



## stflu009.dat

Cyclic steam stimulation on pebi grid


```
Running simulation [simuapp]: Cyclic steam stimulation in Pebi-grid

Elapsed: 3.21s

   113  12.0638  1   1095.000     1.66              0.97             36.84                               0.736   17.488   0.0347    0.962



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.954s  97.20%      

|- Newton                                 2.868s  |- 97.08%   

  |- FluxJac                              0.981s    |- 34.20% 

  |- Update                               0.956s    |- 33.32% 

  |- Solver                               0.408s    |- 14.22% 

  |- ScdAcc                               0.178s    |- 6.21%  

  |- update_dev                           0.108s    |- 3.77%  

  |- Precond                              0.094s    |- 3.28%  

  |- Residual                             0.034s    |- 1.18%  

  |- PerfJac                              0.025s    |- 0.86%  

  |- SanitizeJac                          0.017s    |- 0.58%  

  |- alignvar                             0.016s    |- 0.56%  

  |- HeatLoss                             0.016s    |- 0.54%  

|- Output                                 0.065s  |- 2.22%    

|- Logging                                0.005s  |- 0.16%    

|- Input                                  0.001s  |- 0.03%    

Initialization                            0.085s  2.80%       

|- execution                              0.074s  |- 86.73%   

------------------------------------------------------------

TOTAL                                     3.039s

============================================================



Time steps : 113/113, step size: 9.69027, 21.7405

```

```
Found 114 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu009_00113.vtu

```

![png]({{ "/assets/images/benchmark_image_99.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_100.png" | relative_url }})

### stflu010.dat 

incomp gas

```
Running simulation [simuapp]: Incomp GAS

Elapsed: 1.10s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.867s  93.57%      

|- Newton                                 0.855s  |- 98.65%   

  |- Update                               0.233s    |- 27.30% 

  |- Solver                               0.225s    |- 26.27% 

  |- FluxJac                              0.147s    |- 17.22% 

  |- Precond                              0.091s    |- 10.66% 

  |- ScdAcc                               0.072s    |- 8.42%  

  |- update_dev                           0.033s    |- 3.86%  

  |- SanitizeJac                          0.020s    |- 2.36%  

  |- alignvar                             0.013s    |- 1.46%  

  |- Residual                             0.006s    |- 0.67%  

  |- PerfJac                              0.003s    |- 0.32%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.008s  |- 0.94%    

|- Logging                                0.004s  |- 0.44%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.060s  6.43%       

|- execution                              0.056s  |- 93.61%   

------------------------------------------------------------

TOTAL                                     0.926s

============================================================



Time steps : 33/56, step size: 0.000210583, 0.000151768

```

![png]({{ "/assets/images/benchmark_image_101.png" | relative_url }})

### SAGD

#### 2D cross the well

```
Running simulation [simuapp]: SAGD

Elapsed: 2.64s

   222  16.3533  5   2526.000     6.52             43.95             87.08                      38.76    0.451    5.991   0.5674   20.875



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.395s  97.56%      

|- Newton                                 2.306s  |- 96.30%   

  |- Update                               0.666s    |- 28.88% 

  |- Solver                               0.568s    |- 24.62% 

  |- FluxJac                              0.498s    |- 21.61% 

  |- ScdAcc                               0.183s    |- 7.95%  

  |- Precond                              0.126s    |- 5.47%  

  |- update_dev                           0.111s    |- 4.82%  

  |- SanitizeJac                          0.034s    |- 1.46%  

  |- alignvar                             0.025s    |- 1.10%  

  |- PerfJac                              0.023s    |- 0.99%  

  |- Residual                             0.023s    |- 0.98%  

  |- HeatLoss                             0.005s    |- 0.22%  

|- Output                                 0.057s  |- 2.38%    

|- Logging                                0.023s  |- 0.97%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.060s  2.44%       

|- execution                              0.057s  |- 94.81%   

------------------------------------------------------------

TOTAL                                     2.455s

============================================================



Time steps : 222/228, step size: 11.3784, 12.8828

```

![png]({{ "/assets/images/benchmark_image_102.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_103.png" | relative_url }})

#### 2D along well

```
Running simulation [simuapp]: SAGD

Elapsed: 2.50s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.246s  97.69%      

|- Newton                                 2.199s  |- 97.89%   

  |- Solver                               0.723s    |- 32.90% 

  |- Update                               0.480s    |- 21.81% 

  |- FluxJac                              0.408s    |- 18.55% 

  |- ScdAcc                               0.152s    |- 6.90%  

  |- PerfJac                              0.129s    |- 5.86%  

  |- update_dev                           0.104s    |- 4.75%  

  |- Precond                              0.096s    |- 4.39%  

  |- SanitizeJac                          0.030s    |- 1.35%  

  |- alignvar                             0.020s    |- 0.90%  

  |- Residual                             0.016s    |- 0.72%  

  |- HeatLoss                             0.006s    |- 0.28%  

|- Output                                 0.026s  |- 1.17%    

|- Logging                                0.015s  |- 0.67%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.053s  2.31%       

|- execution                              0.051s  |- 95.30%   

------------------------------------------------------------

TOTAL                                     2.300s

============================================================



Time steps : 89/101, step size: 7.91539, 9.05714

```

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_104.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_105.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_106.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_107.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_108.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_109.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_110.png" | relative_url }})

# Speed



`-DCMAKE_BUILD_TYPE=Release`

### Dome corner grid

```
Running simulation [simuapp]: Dome Corner point

Elapsed: 1.29s

    28  90.1906  1    365.000     4.80              5.27             52.35                               0.507    2.792   0.1500    7.585



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.033s  92.72%      

|- Newton                                 1.021s  |- 98.90%   

  |- Solver                               0.472s    |- 46.24% 

  |- Update                               0.240s    |- 23.50% 

  |- FluxJac                              0.180s    |- 17.60% 

  |- ScdAcc                               0.047s    |- 4.56%  

  |- update_dev                           0.026s    |- 2.56%  

  |- Precond                              0.020s    |- 1.96%  

  |- Residual                             0.011s    |- 1.06%  

  |- HeatLoss                             0.007s    |- 0.64%  

  |- alignvar                             0.004s    |- 0.37%  

  |- SanitizeJac                          0.003s    |- 0.29%  

  |- PerfJac                              0.000s    |- 0.04%  

|- Output                                 0.004s  |- 0.42%    

|- Logging                                0.002s  |- 0.20%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.081s  7.28%       

|- execution                              0.072s  |- 88.62%   

------------------------------------------------------------

TOTAL                                     1.114s

============================================================



Time steps : 28/28, step size: 13.0357, 24.8982

```

```
Found 4 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu018_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_111.png" | relative_url }})

## Heterogeneous

### SPE10 benchmark 2D 

```
Running simulation [simuapp]: SPE10 benchmark 2D water flooding 375 days ~7s single thread (OMP_NUM_THREADS=8)

Elapsed: 3.35s

    79   5.1032  1    375.000    19.23              0.00              0.02                      19.49   13.053    1.813   0.0982    0.004



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  3.064s  97.71%      

|- Newton                                 2.961s  |- 96.65%   

  |- Update                               1.003s    |- 33.89% 

  |- FluxJac                              0.709s    |- 23.95% 

  |- Solver                               0.655s    |- 22.12% 

  |- ScdAcc                               0.214s    |- 7.22%  

  |- update_dev                           0.109s    |- 3.67%  

  |- Precond                              0.079s    |- 2.68%  

  |- PerfJac                              0.067s    |- 2.26%  

  |- Residual                             0.045s    |- 1.52%  

  |- alignvar                             0.016s    |- 0.54%  

  |- SanitizeJac                          0.011s    |- 0.36%  

  |- HeatLoss                             0.007s    |- 0.23%  

|- Output                                 0.071s  |- 2.32%    

|- Logging                                0.004s  |- 0.13%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.072s  2.29%       

|- execution                              0.063s  |- 87.41%   

------------------------------------------------------------

TOTAL                                     3.135s

============================================================



Time steps : 79/79, step size: 4.74684, 2.42242

```

![png]({{ "/assets/images/benchmark_image_112.png" | relative_url }})

### Medium size



* 202,005 grid block (201x201x5) with heterogeneous permeability

* 61 wells water flooding pattern 

* 1500 days

```
Running simulation [simuapp]: Heterogeneous + 61wells - performance test medium size ~3m.50s (Single) (OMP_NUM_THREADS=8)

Elapsed: 127.63s

    36  23.9824  2    365.000   257.96              0.02              0.01                     719.91    0.012  254.602   0.0819    1.572



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                2m 6.56s  99.42%      

|- Newton                               2m 5.28s  |- 98.99%   

  |- Update                              41.694s    |- 33.28% 

  |- FluxJac                             33.211s    |- 26.51% 

  |- Solver                              28.228s    |- 22.53% 

  |- ScdAcc                               8.113s    |- 6.48%  

  |- update_dev                           4.905s    |- 3.92%  

  |- Precond                              3.006s    |- 2.40%  

  |- Residual                             1.896s    |- 1.51%  

  |- HeatLoss                             1.006s    |- 0.80%  

  |- PerfJac                              0.523s    |- 0.42%  

  |- alignvar                             0.497s    |- 0.40%  

  |- SanitizeJac                          0.194s    |- 0.15%  

|- Output                                 0.880s  |- 0.70%    

|- Logging                                0.010s  |- 0.01%    

|- Input                                  0.001s  |- 0.00%    

Initialization                            0.744s  0.58%       

|- execution                              0.573s  |- 76.99%   

------------------------------------------------------------

TOTAL                                   2m 7.30s

============================================================



Time steps : 36/36, step size: 10.1389, 10.6136

```

### Johnansen water flooding

```
Running simulation [simuapp]: Johnansen water flooding takes ~5m on M2 (OMP_NUM_THREADS=8)

Elapsed: 23.90s

    17 365.0000  1   3650.000   353.53              0.07              0.02                     188.86    0.000    3.269   0.0067  3.1e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 22.423s  95.52%      

|- Newton                                22.274s  |- 99.34%   

  |- Update                               7.113s    |- 31.93% 

  |- Solver                               6.334s    |- 28.44% 

  |- FluxJac                              5.599s    |- 25.14% 

  |- ScdAcc                               1.269s    |- 5.70%  

  |- update_dev                           0.722s    |- 3.24%  

  |- Precond                              0.509s    |- 2.29%  

  |- Residual                             0.311s    |- 1.39%  

  |- alignvar                             0.080s    |- 0.36%  

  |- SanitizeJac                          0.029s    |- 0.13%  

  |- PerfJac                              0.002s    |- 0.01%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.113s  |- 0.50%    

|- Logging                                0.002s  |- 0.01%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            1.051s  4.48%       

|- execution                              0.682s  |- 64.89%   

------------------------------------------------------------

TOTAL                                    23.474s

============================================================



Time steps : 17/17, step size: 214.706, 163.784

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data//stflu016_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_113.png" | relative_url }})

# MPI



`simumpi` runs the same deck domain-decomposed across MPI ranks (METIS partitioning, one rank per

subdomain) and rank 0 writes the whole reservoir's `<stem>.smy` - the same filename and the same

columns `simuapp` writes, with per-well and per-cell values reduced across ranks. That is what lets

every plot above read either engine's output, and what the two checks below compare.



Built only when `BUILD_MPI_SIMU=ON` (and never by the MSVC preset), so this section skips itself

when `simumpi` or `mpirun` is missing.


```
parity deck:  /Users/mark/Documents/workspace/hatch/app/build-release/test/data/spe04b.dat

scaling deck: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/speed002.dat (exists: True)

simumpi available: True

```

```
Running simulation [simuapp]: MPI comparison baseline (OMP_NUM_THREADS=1)

Elapsed: 0.92s

    51 338.8120  3   3650.000     0.01              3.51             99.64                       5.81    9.672  840.053   0.0802    9.586



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.675s  91.83%      

|- Newton                                 0.655s  |- 97.09%   

  |- FluxJac                              0.266s    |- 40.66% 

  |- Update                               0.172s    |- 26.20% 

  |- ScdAcc                               0.068s    |- 10.44% 

  |- Solver                               0.059s    |- 8.98%  

  |- update_dev                           0.048s    |- 7.35%  

  |- PerfJac                              0.016s    |- 2.38%  

  |- Precond                              0.009s    |- 1.34%  

  |- alignvar                             0.004s    |- 0.57%  

  |- Residual                             0.003s    |- 0.52%  

  |- HeatLoss                             0.003s    |- 0.41%  

  |- SanitizeJac                          0.001s    |- 0.08%  

|- Output                                 0.014s  |- 2.07%    

|- Logging                                0.002s  |- 0.35%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.060s  8.17%       

|- execution                              0.057s  |- 95.64%   

------------------------------------------------------------

TOTAL                                     0.735s

============================================================



Time steps : 51/51, step size: 71.5686, 94.1896

Running simulation [simumpi]: MPI comparison np=1 (OMP_NUM_THREADS=1, np=1)

Elapsed: 0.95s

    30  42.5990  2    879.343     2.27              5.41             70.49                       6.08            50.208   0.2432   23.194



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    31  37.9161  3    917.259     2.27              5.66             71.40                       6.02            19.521   0.1175   25.619

    32  49.6065  3    966.865     2.10              5.68             72.97                       5.93            23.129   0.2911   32.609

    33  39.3579  2   1006.223     2.07              5.77             73.54                       6.03            17.518   0.1880   27.616

    34  40.7497  3   1046.973     2.19              5.99             73.23                       5.97            20.427   0.1420   39.172

    35  48.0271 10   1095.000     2.06              5.77             73.73                       5.94            40.883   0.2124   51.167

    36  46.3834  4   1141.383     1.50              4.59             75.34                       5.92            45.828   0.1941   31.549

    37  47.1734  5   1188.557     1.53              5.26             77.48                       5.95            96.400   0.1808   38.620

    38  49.9079  3   1238.465     1.37              5.06             78.71                       5.95            63.334   0.1525   41.590

    39  57.7497  4   1296.214     1.07              4.92             82.18                       5.95            89.443   0.2213   30.141

    40  54.4399  3   1350.654     1.00              5.30             84.09                       5.96            81.322   0.1623   22.764

    41  61.0110  2   1411.665     0.88              4.14             82.47                       5.95            82.549   0.1555   33.140

    42  69.8964  4   1481.562     0.63              4.81             88.42                       5.96           124.280   0.2015   11.243

    43  69.5972  2   1551.159     0.54              4.95             90.24                       5.96           113.641   0.1543    6.104

    44  80.0533  2   1631.212     0.45              4.96             91.70                       5.96           141.659   0.0422    5.900

    45 145.7745  2   1776.987     0.32              4.91             93.81                       5.96           281.091   0.1094   10.227

    46 196.7033  4   1973.690     0.22              4.80             95.68                       5.96           439.384   0.0836   13.171

    47 293.0001  5   2266.690     0.12              4.57             97.41                       5.96           779.333   0.1348   18.398

    48 341.0260  3   2607.716     0.06              4.35             98.63                       5.96           1.0e+03   0.0713   19.203

    49 338.1008  2   2945.817     0.04              4.21             99.11                       5.86           750.000   0.0442   11.171

    50 365.0000  3   3310.817     0.02              3.91             99.43                       5.83           821.177   0.0813   10.592

    51 339.1831  3   3650.000     0.01              3.51             99.64                       5.81           840.158   0.0826    9.603

Time steps : 51/51, step size: 71.5686, 94.2394

Running simulation [simumpi]: MPI comparison np=2 (OMP_NUM_THREADS=1, np=2)

Elapsed: 0.72s

    40  25.9887  2   1062.637     2.06              6.04             74.58                       5.96            23.268   0.1120   28.412

    41  32.3627  2   1095.000     2.09              5.91             73.87                       5.96            38.402   0.2392   20.302

    42  29.1043  4   1124.104     2.05              6.21             75.20                       5.96            60.142   0.1134   43.831

    43  38.6752  5   1162.780     1.96              5.72             74.44                       5.96            35.308   0.2620   29.168

    44  32.8578  4   1195.637     1.61              5.37             76.92                       5.96            55.966   0.1854   21.855

    45  34.2869  2   1229.924     1.36              3.76             73.44                       5.96            35.871   0.2389   28.494

    46  30.8595  2   1260.784     1.45              5.31             78.54                       5.96            46.030   0.2811   27.722

    47  25.0516  2   1285.835     1.15              4.97             81.14                       5.96            46.305   0.1745   16.819

    48  27.0231  2   1312.858     1.04              4.80             82.23                       5.96            45.476   0.1237   20.410

    49  34.5590  2   1347.417     1.02              5.05             83.21                       5.96            55.953   0.1897   14.743

    50  35.6068  2   1383.024     0.93              5.17             84.75                       5.96            44.953   0.0844   13.120

    51  53.1575  2   1436.182     0.78              3.15             80.19                       5.96            79.456   0.1432   22.507

    52  63.4557  4   1499.637     0.62              4.74             88.38                       5.96           108.363   0.1466   10.394

    53  74.8831  2   1574.520     0.52              4.96             90.52                       5.96           123.561   0.1868    5.899

    54  77.8131  2   1652.334     0.44              4.98             91.94                       5.96           138.281   0.0425    5.757

    55 141.4610  2   1793.795     0.32              4.92             93.97                       5.96           272.663   0.1027    9.949

    56 195.9003  4   1989.695     0.21              4.81             95.79                       5.96           428.821   0.0878   12.961

    57 288.3540  3   2278.049     0.12              4.70             97.47                       5.96           687.718   0.1177   16.577

    58 356.6299  4   2634.679     0.06              4.37             98.69                       5.96           1.1e+03   0.0710   20.429

    59 346.0109  2   2980.690     0.04              4.23             99.16                       5.86           750.000   0.0464   11.305

    60 365.0000  3   3345.690     0.02              3.94             99.46                       5.83           825.304   0.0831   10.764



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61 304.3103  3   3650.000     0.01              3.50             99.66                       5.84           856.933   0.0837    9.875

Time steps : 61/62, step size: 59.8361, 88.0722

Running simulation [simumpi]: MPI comparison np=4 (OMP_NUM_THREADS=1, np=4)

Elapsed: 0.77s

    44  22.6229  3   1117.623     1.95              5.82             74.87                       5.96            47.806   0.2204   13.413

    45  21.3741  2   1138.997     1.87              5.72             75.36                       5.96            21.345   0.0625   18.582

    46  35.2112  4   1174.208     1.71              5.31             75.61                       5.96            59.140   0.1876   23.098

    47  36.5072  2   1210.715     1.49              4.42             74.80                       5.96            44.153   0.2839   30.189

    48  29.4479  2   1240.163     1.37              4.96             78.36                       5.96            48.436   0.0372   27.718

    49  47.6010  3   1287.764     1.11              5.09             82.07                       5.96            66.086   0.2231   35.798

    50  44.6598  3   1332.424     0.94              4.55             82.87                       5.96            84.648   0.1860   16.897

    51  46.5143  2   1378.938     0.96              5.13             84.20                       5.96            65.618   0.0997   18.354

    52  65.1892  3   1444.128     0.72              5.87             89.13                       5.96           105.464   0.1823   21.798

    53  68.6563  3   1512.784     0.58              4.94             89.42                       5.96           110.745   0.1279    9.901

    54  86.4801  2   1599.264     0.46              4.94             91.43                       5.96           146.591   0.1079    6.498

    55 117.3749  2   1716.639     0.37              4.92             93.04                       5.96           217.498   0.0565    8.469

    56 198.9143  4   1915.553     0.24              4.80             95.18                       5.96           423.352   0.1115   13.690

    57 266.2744  4   2181.828     0.14              4.69             97.01                       5.96           664.877   0.1208   16.958

    58 334.5441  5   2516.372     0.07              4.35             98.39                       5.96           1.0e+03   0.0880   20.196

    59 334.2347  3   2850.606     0.04              4.11             99.15                       5.96           1.1e+03   0.0651   17.283

    60 318.2697  3   3168.876     0.02              3.83             99.46                       5.86           824.363   0.0765   10.485



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61 360.0123  4   3528.888     0.01              3.33             99.72                       5.87           1.2e+03   0.0817   13.277

    62  40.3706  7 1 3569.259     0.01              3.74             99.74                       5.96           132.495   0.0351    2.589

    63  23.0690 10 1 3592.328     0.01              2.81             99.76                       5.96            89.545   0.0546    3.749

    64  27.6828  1   3620.011     0.01              3.79             99.75                       4.57            15.405   0.1463    2.722

    65  29.9893  1   3650.000     0.01              3.84             99.75                       4.66             2.243   0.0530    0.564

Time steps : 65/69, step size: 56.1538, 83.4488

simuapp          rc=0   0.73s   51/ 51 steps  to  3650.00 days

simumpi np=1     rc=0   0.65s   51/ 51 steps,  0 cuts  to  3650.00 days

simumpi np=2     rc=0   0.46s   61/ 62 steps,  1 cuts  to  3650.00 days

simumpi np=4     rc=0   0.49s   65/ 69 steps,  4 cuts  to  3650.00 days

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


![png]({{ "/assets/images/benchmark_image_114.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_115.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_116.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_117.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_118.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_119.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_120.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_121.png" | relative_url }})

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

Elapsed: 11.07s

   190   5.1482  1   1095.000     2.04              1.76             46.23                               2.047    5.862   0.1004    0.888



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 10.568s  98.23%      

|- Newton                                10.406s  |- 98.47%   

  |- FluxJac                              4.468s    |- 42.93% 

  |- Update                               2.958s    |- 28.43% 

  |- ScdAcc                               1.005s    |- 9.66%  

  |- Solver                               0.940s    |- 9.04%  

  |- update_dev                           0.597s    |- 5.74%  

  |- Precond                              0.150s    |- 1.44%  

  |- alignvar                             0.059s    |- 0.56%  

  |- Residual                             0.056s    |- 0.53%  

  |- PerfJac                              0.050s    |- 0.48%  

  |- HeatLoss                             0.043s    |- 0.42%  

  |- SanitizeJac                          0.009s    |- 0.08%  

|- Output                                 0.135s  |- 1.27%    

|- Logging                                0.015s  |- 0.14%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.190s  1.77%       

|- execution                              0.180s  |- 94.88%   

------------------------------------------------------------

TOTAL                                    10.758s

============================================================



Time steps : 190/191, step size: 5.76316, 15.511

Running simulation [simumpi]: CSS parity np=1 (OMP_NUM_THREADS=1, np=1)

Elapsed: 10.16s

   169   0.4838  1    737.735                                                                  159.00            90.860   0.0352   11.762

   170   0.7414  1    738.477                                                                  159.00           123.569   0.0340   17.223

   171   0.9798  2    739.457                                                                  158.04            47.727   0.2776    7.772

   172   0.5435  1    740.000                                                                  159.00           123.839   0.1482   13.669

   173   7.0000  3    747.000                                                                                   1.1e+03   0.2234   26.808

   174   1.0000  3    748.000     2.59            156.39             98.37                                      1.1e+03   0.1430   42.414

   175   0.6121  1    748.612    21.97            102.13             82.29                                      101.169   0.1500    5.715

   176   0.7141  1    749.326    11.92             70.39             85.51                                      165.387   0.0535   10.625

   177   1.1318  1    750.458     9.51             51.39             84.38                                      149.061   0.0320    7.388

   178   1.8897  1    752.348     9.24             36.14             79.63                                      164.334   0.0370    6.728

   179   3.0658  1    755.414     8.52             25.83             75.20                                      174.876   0.0267    7.013

   180   4.8786  1    760.292     7.20             18.94             72.46                                      181.457   0.0216    7.419



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   181   7.6713  1    767.963     6.66             16.19             70.87                                       87.362   0.2625    4.078

   182   6.5095  1    774.473     5.52             12.30             69.03                                      126.987   0.0363    6.355

   183  11.3465  1    785.819     4.21              8.89             67.85                                      136.338   0.0524    7.784

   184  19.4161  1    805.236     3.29              7.26             68.79                                       47.088   0.0719    4.046

   185  30.6287  1    835.864     2.97              5.05             62.98                                      134.435   0.0660   14.143

   186  43.8835  1    879.748     2.45              3.40             58.11                                       99.060   0.1155   10.783

   187  57.8540  4    937.602     2.19              2.57             54.06                                       42.087   0.1194    6.793

   188  75.1536  6   1012.755     2.12              2.52             54.27                                        7.788   0.1912    0.968

   189  77.0965  8   1089.852     2.01              2.04             50.29                                       35.343   0.1192    6.753

   190   5.1482  1   1095.000     2.04              1.76             46.23                                        5.862   0.1004    0.888

Time steps : 190/191, step size: 5.76316, 15.511

Running simulation [simumpi]: CSS parity np=2 (OMP_NUM_THREADS=1, np=2)

Elapsed: 5.83s

   174   0.6089  1    737.355                                                                  158.94           192.483   0.2411   12.875

   175   0.5449  1    737.900                                                                  158.99            97.302   0.0362   13.188

   176   0.8016  1    738.702                                                                  158.97            40.209   0.2371    4.417

   177   0.7248  2    739.427                                                                  158.99           117.597   0.1565   17.447

   178   0.5733  1    740.000                                                                  158.99            85.991   0.0420   12.608

   179   7.0000  3    747.000                                                                                   1.1e+03   0.1866   26.586

   180   1.0000  3    748.000     0.43            158.56             99.73                                      779.268   0.2624   29.851



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   181   0.7581  2    748.758    14.52            106.99             88.05                                      327.042   0.2439   17.225

   182   0.6736  1    749.432    10.98             75.01             87.23                                      142.172   0.0524   10.441

   183   1.0735  1    750.505    10.02             53.24             84.16                                      139.162   0.0360    6.436

   184   1.8269  1    752.332     9.57             36.80             79.36                                      160.863   0.0255    6.536

   185   2.9831  1    755.315     8.63             25.93             75.03                                      173.977   0.0275    6.947

   186   4.7546  1    760.070     7.31             19.15             72.37                                      182.036   0.0274    7.344

   187   7.4686  1    767.538     5.87             13.77             70.12                                      168.829   0.0280    7.697

   188  12.0167  1    779.555     5.43             11.95             68.77                                       73.930   0.2441    3.913

   189  10.6709  1    790.226     4.22              8.86             67.76                                      125.611   0.0486    7.028

   190  18.6513  1    808.877     3.25              7.50             69.78                                       49.328   0.0711    4.175

   191  29.5278  1    838.405     2.98              5.03             62.84                                      128.031   0.0804   13.577

   192  42.9700  1    881.375     2.45              3.38             57.96                                       96.760   0.1008   10.265

   193  59.9731  4    941.348     2.26              2.38             51.37                                       63.866   0.1171   10.523

   194  78.6010  5   1019.949     2.10              1.95             48.18                                       40.586   0.1160    9.197

   195  75.0509  1   1095.000     2.04              1.35             39.81                                       55.426   0.0945   13.507

Time steps : 195/199, step size: 5.61538, 15.0906

Running simulation [simumpi]: CSS parity np=4 (OMP_NUM_THREADS=1, np=4)

Elapsed: 5.24s

   181   0.4592  1    749.923                                                                                    29.544   0.1894    9.612

   182   0.4736  1    750.397     0.20             18.83             98.93                                       31.791   0.1194    1.598

   183   0.6153  1    751.012     0.30             27.27             98.91                                       51.345   0.0664   22.500

   184   0.7178  1    751.730     1.22             25.20             95.38                                       33.400   0.1413   20.568

   185   0.8624  2    752.592     1.15             24.12             95.45                                       28.420   0.2053   16.156

   186   0.8496  1    753.442    12.85             48.93             79.20                                      203.386   0.1500   33.272

   187   0.7997  2    754.242     0.10              1.54             93.63                                      342.054   0.1309   37.396

   188   0.7010  1    754.943     0.54              1.68             75.81                                       52.913   0.2206   11.297

   189   0.6621  1    755.605     1.31             24.79             94.97                                       49.244   0.1420    1.523

   190   0.7937  1    756.398     0.19              8.95             97.91                                       15.051   0.1581    9.270

   191   0.9016  1    757.300     0.60             16.52             96.48                                       37.916   0.2400    9.288

   192   0.8092  1    758.109     1.52             22.55             93.70                                       18.735   0.0314   22.500

   193   0.9440  1    759.053     1.65             19.01             92.01                                       27.992   0.2252    5.370

   194   0.8807  1    759.934    11.17             38.42             77.48                                      171.420   0.1500   25.330

   195   0.9667  1    760.901     8.46             67.73             88.90                                       82.800   0.1400    5.819

   196   1.1666  1    762.067     8.12             36.68             81.87                                       82.014   0.0538    4.184

   197   2.0032  1    764.070     7.74             24.26             75.82                                      111.421   0.0304    4.080

   198   3.6035  1    767.674     7.28             19.50             72.81                                      122.159   0.2847    4.575

   199   2.9013  1    770.575     6.83             17.07             71.41                                       84.874   0.0473    4.595

   200   5.1462  1    775.721     5.79             13.55             70.05                                      115.910   0.0284    5.592

   201   9.1725  1    784.894     4.59             10.35             69.29                                      133.582   0.0472    6.993

   202  15.7811  1    800.675     4.45             10.00             69.20                                       11.324   0.2331    1.220

   203  14.4184  1    815.093     3.65              7.77             68.07                                       88.625   0.0669    6.253

   204  23.2616  1    838.355     3.12              5.58             64.13                                      115.805   0.0851   11.122

   205  34.6236  1    872.979     2.75              4.50             62.08                                       58.777   0.0807    6.052

   206  52.5305  9    925.509     2.31              3.41             59.63                                       59.240   0.1297    8.510

   207  65.7395  9    991.249     2.16              2.81             56.50                                       40.294   0.1268    6.105

   208  83.1132  3   1074.362     2.19              1.85             45.85                                       67.292   0.1122    9.781

   209  20.6382  1   1095.000     2.15              1.74             44.74                                       17.522   0.0781    2.381

Time steps : 209/215, step size: 5.23923, 14.9519

simuapp          rc=0  10.76s  190/191 steps  to  1095.00 days

simumpi np=1     rc=0   9.83s  190/191 steps,  1 cuts  to  1095.00 days

simumpi np=2     rc=0   5.48s  195/199 steps,  4 cuts  to  1095.00 days

simumpi np=4     rc=0   4.89s  209/215 steps,  6 cuts  to  1095.00 days

```

![png]({{ "/assets/images/benchmark_image_122.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_123.png" | relative_url }})

### Wall-clock scaling



Measured on `speed002.dat` (201x201x5 = 202,005 cells), not on the parity deck above: the two

questions need different decks, and asking this one of 180 cells can only ever answer "no". The

timings come from each engine's own closing report rather than from wall clock, so mpirun's

fork/exec and PETSc's initialization are not charged to the curve, and every rank count is timed

over the same number of marched steps (`SCALING_MAXSTEPS`) rather than over its own `dt` sequence.



Two configuration details decide whether the number below means anything, and both bit before:



- **Deck size.** At np=4 the parity deck gives each rank ~45 cells - a few milliseconds of

  arithmetic per step against MPI collectives that cost the same regardless. The speedup there is

  below 1 and says nothing about the decomposition.

- **Threads per rank.** `USE_OPENMP=ON` plus an unset `OMP_NUM_THREADS` means every rank opens a

  whole machine's worth of OpenMP threads; np=4 then oversubscribes the box fourfold. On an

  8-core machine that alone took np=4 from 3.3x down to 1.6x. `MPI_OMP_THREADS` pins it.



The linear solve is a real distributed `KSPSolve` over a `MATMPIAIJ` (`SolverPetscMPI`) - each rank

assembles and owns its own rows, with nothing gathered to rank 0 - and on this deck it is only

~9% of Newton's time anyway. The flux Jacobian and the property update are the ~70% that

decomposition actually has to carry.


```
Running simulation [simuapp]: scaling baseline (OMP_NUM_THREADS=1)

Elapsed: 29.04s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 27.187s  95.13%      

|- Newton                                26.999s  |- 99.31%   

  |- FluxJac                             10.560s    |- 39.11% 

  |- Update                               9.306s    |- 34.47% 

  |- ScdAcc                               2.449s    |- 9.07%  

  |- Solver                               2.114s    |- 7.83%  

  |- update_dev                           1.448s    |- 5.36%  

  |- Precond                              0.377s    |- 1.40%  

  |- Residual                             0.192s    |- 0.71%  

  |- alignvar                             0.153s    |- 0.57%  

  |- HeatLoss                             0.098s    |- 0.36%  

  |- PerfJac                              0.048s    |- 0.18%  

  |- SanitizeJac                          0.038s    |- 0.14%  

|- Output                                 0.113s  |- 0.41%    

|- Logging                                0.002s  |- 0.01%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            1.391s  4.87%       

|- execution                              1.200s  |- 86.26%   

------------------------------------------------------------

TOTAL                                    28.578s

============================================================



Time steps : 4/4, step size: 0.129526, 0.0271065

Running simulation [simumpi]: scaling np=1 (OMP_NUM_THREADS=1, np=1)

Elapsed: 30.70s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-11







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.61             20.31              3.30                     720.00           375.000   0.0027    0.111

     2   0.1167  1      0.217   497.90             26.53              5.06                     720.00           358.750   0.0032    0.123

     3   0.1391  1      0.356   426.44             27.34              6.03                     720.22           375.000   0.0037    0.139

     4   0.1623  1      0.518   376.68             25.84              6.42                     720.00           367.634   0.0042    0.158





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129526, 0.0271065

Running simulation [simumpi]: scaling np=2 (OMP_NUM_THREADS=1, np=2)

Elapsed: 15.82s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-11







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.63             20.31              3.30                     720.00           375.000   0.0027    0.111

     2   0.1167  1      0.217   497.91             26.52              5.06                     720.00           358.735   0.0032    0.123

     3   0.1391  1      0.356   426.45             27.34              6.03                     720.22           375.000   0.0037    0.139

     4   0.1623  1      0.518   376.69             25.84              6.42                     720.00           367.622   0.0042    0.158





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129528, 0.0271081

Running simulation [simumpi]: scaling np=4 (OMP_NUM_THREADS=1, np=4)

Elapsed: 9.17s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-11







=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.61             20.31              3.30                     720.00           375.000   0.0027    0.111

     2   0.1167  1      0.217   497.90             26.53              5.06                     720.00           358.748   0.0032    0.123

     3   0.1391  1      0.356   426.44             27.34              6.03                     720.22           375.000   0.0037    0.139

     4   0.1623  1      0.518   376.68             25.84              6.42                     720.00           367.613   0.0042    0.158





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129527, 0.0271067

```

![png]({{ "/assets/images/benchmark_image_124.png" | relative_url }})

```
np=1:  28.65s  1.00x

np=2:  14.26s  2.01x

np=4:   7.76s  3.69x

simuapp:  28.58s

```

```
Script completed at: 2026-10-12 16:16:51

```
