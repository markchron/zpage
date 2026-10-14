---
layout: default
title: "Benchmark results of resrsim"
date: 2026-10-13
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

Timeloop                                  0.362s  73.24%      

|- Newton                                 0.329s  |- 91.14%   

  |- Update                               0.138s    |- 41.79% 

  |- FluxJac                              0.076s    |- 23.19% 

  |- ScdAcc                               0.035s    |- 10.48% 

  |- Solver                               0.025s    |- 7.57%  

  |- update_dev                           0.016s    |- 4.93%  

  |- Precond                              0.014s    |- 4.11%  

  |- Residual                             0.007s    |- 2.26%  

  |- SanitizeJac                          0.002s    |- 0.73%  

  |- alignvar                             0.002s    |- 0.70%  

  |- PerfJac                              0.002s    |- 0.51%  

  |- HeatLoss                             0.001s    |- 0.36%  

|- Output                                 0.018s  |- 4.94%    

|- Logging                                0.004s  |- 1.24%    

|- Input                                  0.000s  |- 0.05%    

Initialization                            0.132s  26.76%      

|- execution                              0.117s  |- 88.29%   

------------------------------------------------------------

TOTAL                                     0.494s

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

Elapsed: 3.32s

   114  10.6607  2   3650.000     0.09              3.96             97.89                       5.97   18.659    3.789   0.0186    0.919



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  3.077s  97.76%      

|- Newton                                 3.016s  |- 98.01%   

  |- Update                               0.777s    |- 25.75% 

  |- FluxJac                              0.676s    |- 22.43% 

  |- Solver                               0.586s    |- 19.42% 

  |- ScdAcc                               0.263s    |- 8.74%  

  |- Precond                              0.226s    |- 7.48%  

  |- update_dev                           0.175s    |- 5.79%  

  |- PerfJac                              0.102s    |- 3.39%  

  |- SanitizeJac                          0.074s    |- 2.45%  

  |- alignvar                             0.043s    |- 1.43%  

  |- Residual                             0.021s    |- 0.69%  

  |- HeatLoss                             0.020s    |- 0.67%  

|- Output                                 0.039s  |- 1.27%    

|- Logging                                0.022s  |- 0.70%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.071s  2.24%       

|- execution                              0.068s  |- 95.88%   

------------------------------------------------------------

TOTAL                                     3.147s

============================================================



Time steps : 114/157, step size: 32.0175, 28.5766

```

## Select and Plot Columns

Select specific columns from the loaded DataFrames and plot them using matplotlib. For example, plot `TIME` vs `TEMP 1-1-4` from `stars_spe4b_special.csv`.

### Cell property

#### Block Pressure


### Timestep caveat for the (1,1,4) pressure comparison



`spe04b.dat` sets no `*DTMAX`, so the adaptive controller grows the step to ~148 days and takes

~43 cuts late in the run. Those late steps are accepted with the well-constraint budget exhausted

(`newtonraphson.cpp`: `rconv && (wconv || mconv)`), which leaks ~9% of the cumulative water

balance; the lost mass is why P(1,1,4) appears to flatten at ~3865 kPa below the CMG curve. That

cell is wet steam there (`P = Psat(T)`), so its pressure can only rise as its temperature does.



Re-running the *same* deck with a single added `*DTMAX 5` line removes the cuts (732/732 steps,

0 cuts), cuts the water-balance error to ~1%, and the pressure then climbs monotonically to

~6160 kPa with the injector BHP converging on the `*MAX BHP` 6895 kPa limit - which matches CMG's

higher pressure. So the gap below the red CMG curve is a timestep / mass-balance artifact of the

default run, **not** a physical discrepancy. Add `*DTMAX 5` to the deck (or a copy of it) to

compare physics rather than the timestep error.

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

Elapsed: 1.97s

    87  86.8561  3   3650.000     0.51              5.62             91.73                       5.96   11.937  188.740   0.2212    4.318



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.734s  96.67%      

|- Newton                                 1.692s  |- 97.58%   

  |- Update                               0.448s    |- 26.47% 

  |- FluxJac                              0.376s    |- 22.22% 

  |- Solver                               0.323s    |- 19.08% 

  |- ScdAcc                               0.141s    |- 8.35%  

  |- Precond                              0.127s    |- 7.51%  

  |- update_dev                           0.090s    |- 5.32%  

  |- PerfJac                              0.064s    |- 3.81%  

  |- SanitizeJac                          0.040s    |- 2.34%  

  |- alignvar                             0.024s    |- 1.43%  

  |- Residual                             0.013s    |- 0.76%  

  |- HeatLoss                             0.012s    |- 0.73%  

|- Output                                 0.027s  |- 1.53%    

|- Logging                                0.015s  |- 0.86%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.060s  3.33%       

|- execution                              0.056s  |- 94.48%   

------------------------------------------------------------

TOTAL                                     1.794s

============================================================



Time steps : 87/104, step size: 41.954, 36.3545

```

![png]({{ "/assets/images/benchmark_image_36.png" | relative_url }})

# Buckley- Leverett



Two phase, isothermal problem

variable order: [Sw, P, T, So, X0, X1, Sg]



Acc w.r.t. [Sw, So, Sg, X0, X1, P, T]

```
Running simulation [simuapp]: Buckley-Leverett

Elapsed: 0.51s

    78   4.7172  1     10.000                       0.16            100.00                       0.16   33.905    0.002 7.15e-06  1.4e-05



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.288s  82.90%      

|- Newton                                 0.263s  |- 91.34%   

  |- Update                               0.090s    |- 34.39% 

  |- FluxJac                              0.039s    |- 14.95% 

  |- Solver                               0.032s    |- 11.98% 

  |- ScdAcc                               0.028s    |- 10.47% 

  |- Precond                              0.021s    |- 7.88%  

  |- update_dev                           0.013s    |- 4.78%  

  |- PerfJac                              0.012s    |- 4.65%  

  |- SanitizeJac                          0.006s    |- 2.30%  

  |- HeatLoss                             0.005s    |- 1.93%  

  |- alignvar                             0.004s    |- 1.69%  

  |- Residual                             0.004s    |- 1.49%  

|- Output                                 0.017s  |- 5.89%    

|- Logging                                0.005s  |- 1.87%    

|- Input                                  0.000s  |- 0.04%    

Initialization                            0.059s  17.10%      

|- execution                              0.057s  |- 95.38%   

------------------------------------------------------------

TOTAL                                     0.347s

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

Timeloop                                  0.201s  76.30%      

|- Newton                                 0.188s  |- 93.76%   

  |- Update                               0.070s    |- 37.26% 

  |- FluxJac                              0.053s    |- 28.14% 

  |- Solver                               0.022s    |- 11.86% 

  |- ScdAcc                               0.014s    |- 7.47%  

  |- Precond                              0.009s    |- 4.85%  

  |- update_dev                           0.008s    |- 4.17%  

  |- PerfJac                              0.003s    |- 1.39%  

  |- Residual                             0.003s    |- 1.36%  

  |- SanitizeJac                          0.002s    |- 1.02%  

  |- alignvar                             0.002s    |- 0.81%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.009s  |- 4.49%    

|- Logging                                0.001s  |- 0.36%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.062s  23.70%      

|- execution                              0.060s  |- 96.32%   

------------------------------------------------------------

TOTAL                                     0.263s

============================================================



Time steps : 25/25, step size: 146, 149.392

```



## watfld_cw.dat

```
Running simulation [simuapp]: SPE4-b Water flooding without vmod

Elapsed: 0.52s

    38  40.9777  1   3650.000     1.04             78.98             98.70                      80.00    3.287    1.793   0.0038  4.6e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.305s  85.66%      

|- Newton                                 0.287s  |- 93.85%   

  |- Update                               0.098s    |- 34.31% 

  |- FluxJac                              0.078s    |- 27.09% 

  |- Solver                               0.040s    |- 13.96% 

  |- ScdAcc                               0.020s    |- 6.94%  

  |- PerfJac                              0.014s    |- 4.78%  

  |- Precond                              0.013s    |- 4.49%  

  |- update_dev                           0.010s    |- 3.56%  

  |- Residual                             0.004s    |- 1.31%  

  |- SanitizeJac                          0.003s    |- 1.12%  

  |- alignvar                             0.002s    |- 0.76%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.012s  |- 3.87%    

|- Logging                                0.001s  |- 0.35%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.051s  14.34%      

|- execution                              0.049s  |- 95.39%   

------------------------------------------------------------

TOTAL                                     0.357s

============================================================



Time steps : 38/38, step size: 96.0526, 135.309

```

## stflu001.dat

Inverted 9 spot water flooding with area/block modifier, 5 point transmissibility


```
Running simulation [simuapp]: Inverted 9 spot water flooding

Elapsed: 1.07s

   202  79.4173  6   3650.000     0.07            140.76             99.95                     138.21   39.900   88.641   0.1125    2.631



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.831s  93.52%      

|- Newton                                 0.761s  |- 91.62%   

  |- Update                               0.255s    |- 33.52% 

  |- FluxJac                              0.201s    |- 26.44% 

  |- ScdAcc                               0.084s    |- 10.98% 

  |- Solver                               0.057s    |- 7.43%  

  |- Precond                              0.053s    |- 6.95%  

  |- update_dev                           0.043s    |- 5.61%  

  |- SanitizeJac                          0.019s    |- 2.46%  

  |- PerfJac                              0.011s    |- 1.43%  

  |- alignvar                             0.010s    |- 1.31%  

  |- Residual                             0.008s    |- 1.10%  

  |- HeatLoss                             0.006s    |- 0.81%  

|- Output                                 0.051s  |- 6.19%    

|- Logging                                0.007s  |- 0.82%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.058s  6.48%       

|- execution                              0.055s  |- 94.85%   

------------------------------------------------------------

TOTAL                                     0.889s

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

Timeloop                                  0.206s  75.73%      

|- Newton                                 0.192s  |- 93.03%   

  |- Update                               0.055s    |- 28.96% 

  |- Solver                               0.042s    |- 22.03% 

  |- FluxJac                              0.035s    |- 18.29% 

  |- ScdAcc                               0.015s    |- 8.09%  

  |- Precond                              0.013s    |- 6.66%  

  |- PerfJac                              0.007s    |- 3.77%  

  |- update_dev                           0.007s    |- 3.72%  

  |- SanitizeJac                          0.004s    |- 1.90%  

  |- HeatLoss                             0.003s    |- 1.55%  

  |- alignvar                             0.002s    |- 1.25%  

  |- Residual                             0.002s    |- 1.12%  

|- Output                                 0.009s  |- 4.49%    

|- Logging                                0.002s  |- 0.81%    

|- Input                                  0.000s  |- 0.04%    

Initialization                            0.066s  24.27%      

|- execution                              0.063s  |- 95.50%   

------------------------------------------------------------

TOTAL                                     0.272s

============================================================



Time steps : 46/46, step size: 79.3478, 130.449

```



## stflu003.dat

5000x5000x50, 2D diagonal water flooding in uniformed corner point

```
Running simulation [simuapp]: uniformed corner grid

Elapsed: 0.43s

    42 125.6950  2   3650.000   631.01              4.94              0.78                     642.05   41.030  750.000   0.0151    0.020



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.173s  69.13%      

|- Newton                                 0.159s  |- 92.02%   

  |- Update                               0.049s    |- 30.99% 

  |- FluxJac                              0.032s    |- 20.31% 

  |- Solver                               0.030s    |- 19.05% 

  |- ScdAcc                               0.013s    |- 7.89%  

  |- Precond                              0.010s    |- 6.32%  

  |- update_dev                           0.006s    |- 3.90%  

  |- PerfJac                              0.006s    |- 3.62%  

  |- SanitizeJac                          0.003s    |- 1.66%  

  |- HeatLoss                             0.002s    |- 1.48%  

  |- alignvar                             0.002s    |- 1.18%  

  |- Residual                             0.002s    |- 1.14%  

|- Output                                 0.009s  |- 5.13%    

|- Logging                                0.001s  |- 0.75%    

|- Input                                  0.000s  |- 0.05%    

Initialization                            0.077s  30.87%      

|- execution                              0.068s  |- 87.77%   

------------------------------------------------------------

TOTAL                                     0.250s

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

Elapsed: 0.52s

    53 311.3861  1   3650.000   634.73              0.94              0.15                     635.95   61.649  375.000   0.0373    0.016



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.307s  85.10%      

|- Newton                                 0.289s  |- 94.03%   

  |- Update                               0.123s    |- 42.51% 

  |- FluxJac                              0.056s    |- 19.38% 

  |- Solver                               0.042s    |- 14.52% 

  |- ScdAcc                               0.020s    |- 7.07%  

  |- Precond                              0.011s    |- 3.97%  

  |- update_dev                           0.011s    |- 3.87%  

  |- PerfJac                              0.005s    |- 1.85%  

  |- HeatLoss                             0.005s    |- 1.66%  

  |- Residual                             0.004s    |- 1.37%  

  |- SanitizeJac                          0.003s    |- 0.96%  

  |- alignvar                             0.002s    |- 0.78%  

|- Output                                 0.013s  |- 4.10%    

|- Logging                                0.001s  |- 0.46%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.054s  14.90%      

|- execution                              0.051s  |- 95.04%   

------------------------------------------------------------

TOTAL                                     0.361s

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

Elapsed: 1.34s

    48 278.1405  2   3650.000   588.86              2.21              0.37                     635.95   60.296  698.996   0.0561    0.032



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.065s  93.65%      

|- Newton                                 1.034s  |- 97.16%   

  |- Solver                               0.345s    |- 33.36% 

  |- FluxJac                              0.261s    |- 25.23% 

  |- Update                               0.250s    |- 24.18% 

  |- ScdAcc                               0.055s    |- 5.36%  

  |- Precond                              0.032s    |- 3.10%  

  |- update_dev                           0.030s    |- 2.89%  

  |- HeatLoss                             0.014s    |- 1.34%  

  |- Residual                             0.009s    |- 0.91%  

  |- PerfJac                              0.008s    |- 0.74%  

  |- SanitizeJac                          0.007s    |- 0.71%  

  |- alignvar                             0.006s    |- 0.56%  

|- Output                                 0.022s  |- 2.06%    

|- Logging                                0.006s  |- 0.53%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.072s  6.35%       

|- execution                              0.060s  |- 82.99%   

------------------------------------------------------------

TOTAL                                     1.137s

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

Elapsed: 1.40s

   114 127.8229  2   3650.000     0.19              4.18             95.55                       4.54   13.873    4.428   0.0057    1.465



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.158s  95.34%      

|- Newton                                 1.100s  |- 95.00%   

  |- Solver                               0.331s    |- 30.06% 

  |- Update                               0.242s    |- 21.99% 

  |- FluxJac                              0.236s    |- 21.48% 

  |- ScdAcc                               0.090s    |- 8.19%  

  |- Precond                              0.075s    |- 6.80%  

  |- update_dev                           0.042s    |- 3.84%  

  |- PerfJac                              0.029s    |- 2.67%  

  |- SanitizeJac                          0.017s    |- 1.50%  

  |- alignvar                             0.010s    |- 0.90%  

  |- Residual                             0.007s    |- 0.62%  

  |- HeatLoss                             0.006s    |- 0.58%  

|- Output                                 0.038s  |- 3.26%    

|- Logging                                0.006s  |- 0.48%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.057s  4.66%       

|- execution                              0.054s  |- 95.24%   

------------------------------------------------------------

TOTAL                                     1.215s

============================================================



Time steps : 114/117, step size: 32.0175, 59.8918

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

Elapsed: 0.49s

   104  27.8956  1   1095.000     1.24              3.92             75.95                               0.587   25.324   0.1212    2.924



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.262s  83.46%      

|- Newton                                 0.224s  |- 85.39%   

  |- Update                               0.078s    |- 34.82% 

  |- FluxJac                              0.035s    |- 15.65% 

  |- Precond                              0.024s    |- 10.61% 

  |- PerfJac                              0.024s    |- 10.52% 

  |- ScdAcc                               0.018s    |- 8.16%  

  |- Solver                               0.011s    |- 4.95%  

  |- update_dev                           0.010s    |- 4.36%  

  |- SanitizeJac                          0.008s    |- 3.72%  

  |- alignvar                             0.005s    |- 2.13%  

  |- Residual                             0.002s    |- 1.00%  

  |- HeatLoss                             0.001s    |- 0.65%  

|- Output                                 0.023s  |- 8.84%    

|- Logging                                0.003s  |- 1.12%    

|- Input                                  0.001s  |- 0.41%    

Initialization                            0.052s  16.54%      

|- execution                              0.050s  |- 95.46%   

------------------------------------------------------------

TOTAL                                     0.314s

============================================================



Time steps : 104/104, step size: 10.5288, 22.2361

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

Elapsed: 4.99s

   194  64.9779  1   1095.000     2.12              1.43             40.39                               3.332   48.628   0.1082    5.703



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  4.733s  98.81%      

|- Newton                                 4.579s  |- 96.74%   

  |- Update                               1.415s    |- 30.91% 

  |- FluxJac                              1.414s    |- 30.87% 

  |- Solver                               0.789s    |- 17.24% 

  |- ScdAcc                               0.331s    |- 7.24%  

  |- update_dev                           0.183s    |- 3.99%  

  |- Precond                              0.166s    |- 3.62%  

  |- Residual                             0.058s    |- 1.27%  

  |- PerfJac                              0.049s    |- 1.07%  

  |- HeatLoss                             0.045s    |- 0.98%  

  |- alignvar                             0.028s    |- 0.60%  

  |- SanitizeJac                          0.027s    |- 0.59%  

|- Output                                 0.117s  |- 2.48%    

|- Logging                                0.012s  |- 0.26%    

|- Input                                  0.001s  |- 0.03%    

Initialization                            0.057s  1.19%       

|- execution                              0.054s  |- 94.94%   

------------------------------------------------------------

TOTAL                                     4.790s

============================================================



Time steps : 194/195, step size: 5.64433, 14.9923

```

```
Found 195 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu008_00194.vtu

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

Elapsed: 1.52s

    64  55.2171  1   1095.000     0.77              0.04              5.18                               0.008    7.394   0.0013    1.478



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.268s  94.65%      

|- Newton                                 1.202s  |- 94.83%   

  |- Update                               0.423s    |- 35.17% 

  |- FluxJac                              0.418s    |- 34.77% 

  |- Solver                               0.152s    |- 12.64% 

  |- ScdAcc                               0.072s    |- 5.98%  

  |- update_dev                           0.041s    |- 3.44%  

  |- Precond                              0.038s    |- 3.18%  

  |- Residual                             0.016s    |- 1.34%  

  |- HeatLoss                             0.006s    |- 0.53%  

  |- SanitizeJac                          0.006s    |- 0.52%  

  |- alignvar                             0.006s    |- 0.49%  

  |- PerfJac                              0.002s    |- 0.16%  

|- Output                                 0.048s  |- 3.78%    

|- Logging                                0.004s  |- 0.34%    

|- Input                                  0.001s  |- 0.06%    

Initialization                            0.072s  5.35%       

|- execution                              0.059s  |- 82.96%   

------------------------------------------------------------

TOTAL                                     1.339s

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

| `stflu009.dat` | uniform PEBI | ~13.4 ft hexagon (~155 ft^2) |

| `stflu009_graded.dat` | graded PEBI | refined toward ~3 ft near the well |


```
Running simulation [simuapp]: Cyclic steam stimulation in graded Pebi-grid

Elapsed: 7.93s

   272  66.7800  3   1095.000     2.35              2.25             48.87                               3.462   18.631   0.0933    3.117



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  7.675s  98.94%      

|- Newton                                 7.429s  |- 96.79%   

  |- FluxJac                              2.486s    |- 33.46% 

  |- Update                               2.090s    |- 28.14% 

  |- Solver                               1.512s    |- 20.36% 

  |- ScdAcc                               0.461s    |- 6.20%  

  |- update_dev                           0.261s    |- 3.51%  

  |- Precond                              0.246s    |- 3.31%  

  |- Residual                             0.079s    |- 1.07%  

  |- PerfJac                              0.075s    |- 1.01%  

  |- SanitizeJac                          0.042s    |- 0.56%  

  |- alignvar                             0.035s    |- 0.48%  

  |- HeatLoss                             0.033s    |- 0.45%  

|- Output                                 0.194s  |- 2.53%    

|- Logging                                0.018s  |- 0.23%    

|- Input                                  0.002s  |- 0.02%    

Initialization                            0.082s  1.06%       

|- execution                              0.064s  |- 77.78%   

------------------------------------------------------------

TOTAL                                     7.757s

============================================================



Time steps : 272/273, step size: 4.02574, 12.8678

```

```
Found 273 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu009_graded_00272.vtu

```

![png]({{ "/assets/images/benchmark_image_101.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_102.png" | relative_url }})

### stflu010.dat 

incomp gas

```
Running simulation [simuapp]: Incomp GAS

Elapsed: 1.40s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.029s  88.23%      

|- Newton                                 1.013s  |- 98.43%   

  |- Update                               0.256s    |- 25.32% 

  |- Solver                               0.251s    |- 24.80% 

  |- FluxJac                              0.168s    |- 16.54% 

  |- ScdAcc                               0.108s    |- 10.64% 

  |- Precond                              0.095s    |- 9.39%  

  |- update_dev                           0.070s    |- 6.95%  

  |- SanitizeJac                          0.021s    |- 2.09%  

  |- alignvar                             0.014s    |- 1.37%  

  |- Residual                             0.006s    |- 0.57%  

  |- PerfJac                              0.003s    |- 0.33%  

  |- HeatLoss                             0.000s    |- 0.01%  

|- Output                                 0.012s  |- 1.13%    

|- Logging                                0.010s  |- 0.98%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.137s  11.77%      

|- execution                              0.119s  |- 86.73%   

------------------------------------------------------------

TOTAL                                     1.166s

============================================================



Time steps : 33/56, step size: 0.000210583, 0.000151768

```

![png]({{ "/assets/images/benchmark_image_103.png" | relative_url }})

### SAGD

#### 2D cross the well

```
Running simulation [simuapp]: SAGD

Elapsed: 2.29s

   205   5.8667  1   2526.000     5.82             40.83             87.53                      40.42    1.358    1.961   0.0854    3.228



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.063s  97.28%      

|- Newton                                 1.974s  |- 95.69%   

  |- Update                               0.537s    |- 27.23% 

  |- Solver                               0.500s    |- 25.34% 

  |- FluxJac                              0.441s    |- 22.35% 

  |- ScdAcc                               0.174s    |- 8.80%  

  |- Precond                              0.104s    |- 5.29%  

  |- update_dev                           0.093s    |- 4.69%  

  |- SanitizeJac                          0.028s    |- 1.41%  

  |- alignvar                             0.021s    |- 1.04%  

  |- Residual                             0.019s    |- 0.98%  

  |- PerfJac                              0.017s    |- 0.85%  

  |- HeatLoss                             0.004s    |- 0.22%  

|- Output                                 0.062s  |- 3.03%    

|- Logging                                0.015s  |- 0.71%    

|- Input                                  0.001s  |- 0.03%    

Initialization                            0.058s  2.72%       

|- execution                              0.054s  |- 93.52%   

------------------------------------------------------------

TOTAL                                     2.120s

============================================================



Time steps : 205/205, step size: 12.322, 13.2842

```

![png]({{ "/assets/images/benchmark_image_104.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_105.png" | relative_url }})

#### 2D along well

```
Running simulation [simuapp]: SAGD

Elapsed: 34.63s

   564   4.6567  8   2526.000    11.14             13.47             54.73                              91.585  178.039   0.4103    5.613



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 34.391s  99.83%      

|- Newton                                33.846s  |- 98.42%   

  |- Solver                              16.261s    |- 48.04% 

  |- Update                               5.787s    |- 17.10% 

  |- FluxJac                              5.140s    |- 15.19% 

  |- ScdAcc                               2.260s    |- 6.68%  

  |- update_dev                           1.470s    |- 4.34%  

  |- Precond                              1.362s    |- 4.02%  

  |- SanitizeJac                          0.371s    |- 1.10%  

  |- PerfJac                              0.283s    |- 0.84%  

  |- alignvar                             0.283s    |- 0.84%  

  |- Residual                             0.205s    |- 0.61%  

  |- HeatLoss                             0.091s    |- 0.27%  

|- Output                                 0.241s  |- 0.70%    

|- Logging                                0.104s  |- 0.30%    

|- Input                                  0.001s  |- 0.00%    

Initialization                            0.059s  0.17%       

|- execution                              0.056s  |- 95.26%   

------------------------------------------------------------

TOTAL                                    34.450s

============================================================



Time steps : 564/815, step size: 4.47872, 15.5288

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

Elapsed: 1.50s

    26  66.3722  1    365.000     0.05              0.01             10.81                               0.431    7.102   0.0227    5.711



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.230s  93.49%      

|- Newton                                 1.219s  |- 99.14%   

  |- Solver                               0.675s    |- 55.36% 

  |- Update                               0.227s    |- 18.63% 

  |- FluxJac                              0.186s    |- 15.29% 

  |- ScdAcc                               0.047s    |- 3.87%  

  |- update_dev                           0.026s    |- 2.16%  

  |- Precond                              0.020s    |- 1.65%  

  |- Residual                             0.011s    |- 0.87%  

  |- HeatLoss                             0.007s    |- 0.57%  

  |- alignvar                             0.004s    |- 0.30%  

  |- SanitizeJac                          0.003s    |- 0.24%  

  |- PerfJac                              0.001s    |- 0.07%  

|- Output                                 0.005s  |- 0.38%    

|- Logging                                0.001s  |- 0.12%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.086s  6.51%       

|- execution                              0.076s  |- 88.77%   

------------------------------------------------------------

TOTAL                                     1.315s

============================================================



Time steps : 26/26, step size: 14.0385, 25.1055

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

Elapsed: 3.58s

    79   5.1032  1    375.000    19.23              0.00              0.02                      19.49   13.053    1.813   0.0982    0.004



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  3.323s  97.82%      

|- Newton                                 3.200s  |- 96.28%   

  |- Update                               1.047s    |- 32.72% 

  |- FluxJac                              0.813s    |- 25.42% 

  |- Solver                               0.699s    |- 21.85% 

  |- ScdAcc                               0.216s    |- 6.77%  

  |- update_dev                           0.120s    |- 3.75%  

  |- PerfJac                              0.087s    |- 2.72%  

  |- Precond                              0.083s    |- 2.59%  

  |- Residual                             0.045s    |- 1.40%  

  |- alignvar                             0.017s    |- 0.52%  

  |- SanitizeJac                          0.013s    |- 0.39%  

  |- HeatLoss                             0.007s    |- 0.23%  

|- Output                                 0.090s  |- 2.69%    

|- Logging                                0.009s  |- 0.27%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.074s  2.18%       

|- execution                              0.064s  |- 86.39%   

------------------------------------------------------------

TOTAL                                     3.397s

============================================================



Time steps : 79/79, step size: 4.74684, 2.42242

```

![png]({{ "/assets/images/benchmark_image_114.png" | relative_url }})

### Medium size



* 202,005 grid block (201x201x5) with heterogeneous permeability

* 61 wells water flooding pattern 

* 1500 days

```
Running simulation [simuapp]: Heterogeneous + 61wells - performance test medium size ~3m.50s (Single) (OMP_NUM_THREADS=8)

Elapsed: 132.00s

    36  23.9824  2    365.000   257.96              0.02              0.01                     719.91    0.012  254.602   0.0819    1.572



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                               2m 10.94s  99.43%      

|- Newton                               2m 9.67s  |- 99.03%   

  |- Update                              42.531s    |- 32.80% 

  |- FluxJac                             36.104s    |- 27.84% 

  |- Solver                              29.351s    |- 22.63% 

  |- ScdAcc                               7.851s    |- 6.05%  

  |- update_dev                           4.549s    |- 3.51%  

  |- Precond                              3.067s    |- 2.37%  

  |- Residual                             1.914s    |- 1.48%  

  |- HeatLoss                             1.075s    |- 0.83%  

  |- PerfJac                              0.533s    |- 0.41%  

  |- alignvar                             0.480s    |- 0.37%  

  |- SanitizeJac                          0.204s    |- 0.16%  

|- Output                                 0.855s  |- 0.65%    

|- Logging                                0.005s  |- 0.00%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.751s  0.57%       

|- execution                              0.571s  |- 76.01%   

------------------------------------------------------------

TOTAL                                  2m 11.69s

============================================================



Time steps : 36/36, step size: 10.1389, 10.6136

```

### Johnansen water flooding

```
Running simulation [simuapp]: Johnansen water flooding takes ~5m on M2 (OMP_NUM_THREADS=8)

Elapsed: 24.80s

    17 365.0000  1   3650.000   353.53              0.07              0.02                     188.86    0.000    3.269   0.0067  3.1e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 23.414s  95.89%      

|- Newton                                23.280s  |- 99.43%   

  |- Update                               7.377s    |- 31.69% 

  |- Solver                               6.612s    |- 28.40% 

  |- FluxJac                              5.820s    |- 25.00% 

  |- ScdAcc                               1.425s    |- 6.12%  

  |- update_dev                           0.761s    |- 3.27%  

  |- Precond                              0.529s    |- 2.27%  

  |- Residual                             0.321s    |- 1.38%  

  |- alignvar                             0.081s    |- 0.35%  

  |- SanitizeJac                          0.030s    |- 0.13%  

  |- PerfJac                              0.002s    |- 0.01%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.098s  |- 0.42%    

|- Logging                                0.002s  |- 0.01%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            1.004s  4.11%       

|- execution                              0.635s  |- 63.28%   

------------------------------------------------------------

TOTAL                                    24.419s

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

Elapsed: 4.24s

   114  10.6607  2   3650.000     0.09              3.96             97.89                       5.97   18.659    3.789   0.0186    0.919



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  4.004s  98.69%      

|- Newton                                 3.947s  |- 98.58%   

  |- FluxJac                              1.468s    |- 37.19% 

  |- Update                               0.918s    |- 23.26% 

  |- Solver                               0.557s    |- 14.12% 

  |- ScdAcc                               0.435s    |- 11.02% 

  |- update_dev                           0.319s    |- 8.08%  

  |- PerfJac                              0.091s    |- 2.31%  

  |- Precond                              0.052s    |- 1.33%  

  |- alignvar                             0.022s    |- 0.55%  

  |- Residual                             0.017s    |- 0.43%  

  |- HeatLoss                             0.015s    |- 0.39%  

  |- SanitizeJac                          0.003s    |- 0.08%  

|- Output                                 0.042s  |- 1.04%    

|- Logging                                0.021s  |- 0.53%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.053s  1.31%       

|- execution                              0.051s  |- 95.57%   

------------------------------------------------------------

TOTAL                                     4.057s

============================================================



Time steps : 114/157, step size: 32.0175, 28.5766

Running simulation [simumpi]: MPI comparison np=1 (OMP_NUM_THREADS=1, np=1)

Elapsed: 4.32s

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    91  11.8227  2 1 3391.697     0.10              4.92             97.96                       5.99   10.082    2.429   0.0083    0.454

    92   8.7108  2 1 3400.408     0.10              4.87             97.96                       6.01   10.323    4.404   0.0249    0.823

    93  17.4294  2   3417.837     0.10              4.86             97.97                       5.96   10.678    1.913   0.0075    0.527

    94  12.9146  2 1 3430.752     0.10              4.83             97.97                       5.99   10.987    2.735   0.0327    0.786

    95   8.2465  2 1 3438.998     0.10              4.82             97.97                       5.96   11.186    2.227   0.0060    0.451

    96  18.4999  6   3457.498     0.10              4.76             97.97                       6.06   11.749    5.275   0.0527    2.000

    97  10.6461  2 1 3468.144     0.10              4.74             97.97                       5.96   12.006    1.898   0.0066    0.506

    98   7.9320  2 1 3476.076     0.10              4.69             97.97                       6.00   12.247    3.777   0.0359    0.868

    99  14.9329  3   3491.009     0.10              4.72             97.97                       5.96   12.540    3.521   0.0032   22.638

   100   8.5262  2 1 3499.536     0.10              4.65             97.97                       5.96   12.818    4.674   0.0189    0.910

   101  17.6653 11   3517.201     0.09              4.52             97.96                       5.96   13.615   14.663   0.0575   22.336

   102   6.4238  2 1 3523.625     0.09              4.47             97.96                       5.97   13.858    3.968   0.0176    0.889

   103  13.4127  5   3537.037     0.09              4.50             97.96                       5.96   14.206    3.722   0.0080   22.658

   104   7.6564  2 1 3544.694     0.09              4.45             97.96                       5.96   14.494    5.061   0.0190    0.961

   105  15.8595  7   3560.553     0.09              4.38             97.94                       5.96   15.165   11.741   0.0396   22.406

   106   9.0626  2 1 3569.616     0.09              4.36             97.94                       6.01   15.450    1.652   0.0062    0.914

   107   6.7668  2 1 3576.383     0.09              4.31             97.94                       5.96   15.721    4.223   0.0179    0.980

   108  14.1037  6   3590.486     0.09              4.30             97.93                       5.96   16.226    4.644   0.0192    1.538

   109   9.4025  2 1 3599.889     0.09              4.26             97.93                       6.00   16.571    3.157   0.0174    0.915

   110   6.5526  2 1 3606.442     0.09              4.25             97.92                       5.96   16.794    1.664   0.0057    0.479

   111  14.7338 10   3621.175     0.09              4.11             97.91                       5.96   17.516    7.383   0.0432    2.653

   112   5.8935  2 1 3627.069     0.09              4.05             97.91                       6.00   17.796    4.888   0.0181    1.070

   113  12.2704  5   3639.339     0.09              4.01             97.90                       5.96   18.225    4.358   0.0075   22.654

   114  10.6607  2   3650.000     0.09              3.96             97.89                       5.97   18.659    3.789   0.0186    0.919

Time steps : 114/157, step size: 32.0175, 28.5766

Running simulation [simumpi]: MPI comparison np=2 (OMP_NUM_THREADS=1, np=2)

Elapsed: 0.85s

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    31  22.0757  1    932.967     1.90              5.19             73.16                       5.96    1.711   11.112   0.0927   16.723

    32  31.8404  3    964.807     2.02              5.56             73.40                       5.96    1.705   38.326   0.2256   26.922

    33  29.6692  2    994.476     2.11              5.73             73.06                       5.96    1.701   26.072   0.1954   19.450

    34  30.0634  2   1024.540     2.21              5.77             72.28                       5.96    1.688   12.672   0.0823   26.193

    35  45.2979  4   1069.837     2.40              5.98             71.35                       5.96    1.682   32.349   0.1506   37.836

    36  25.1625  2   1095.000     2.48              6.11             71.12                       5.96    1.684   21.033   0.1577   15.364

    37  28.6174  2   1123.617     2.67              6.06             69.44                       5.96    1.672   31.812   0.2119   20.563

    38  27.6730  3   1151.290     2.43              6.14             71.68                       5.96    1.689   20.157   0.1582   23.240

    39  31.4312  1   1182.722     2.61              6.84             72.37                       5.96    1.383   31.038   0.1244   22.500

    40  40.0854  6   1222.807     2.54              6.36             71.46                       5.96    1.372   23.789   0.2364   56.121

    41  36.3138  4   1259.121     2.35              5.93             71.59                       5.96    1.465   34.829   0.1161   28.308

    42  47.7547  3   1306.875     2.31              5.95             72.04                       5.96    1.429   65.138   0.1417   41.396

    43  57.3064  6   1364.182     1.78              5.16             74.32                       5.96    1.665   92.697   0.2425   47.999

    44  51.1033  3   1415.285     1.32              5.57             80.90                       5.96    1.098   66.600   0.2326   38.974

    45  46.7524  3   1462.038     1.05              4.89             82.31                       5.96    1.096   82.703   0.2049   16.679

    46  46.1029  2   1508.140     0.92              4.88             84.11                       5.96    1.084   74.038   0.1451   19.888

    47  54.6828  3   1562.823     0.77              4.85             86.36                       5.96    1.191   94.908   0.1680   21.971

    48  60.1773  2   1623.001     0.65              5.12             88.81                       5.96    1.322  102.608   0.1434    7.406

    49  71.7899  2   1694.790     0.58              4.84             89.34                       5.96    1.289  121.042   0.0777    5.634

    50 110.3326  2   1805.123     0.43              4.92             91.94                       5.96    1.226  198.992   0.0656    8.213

    51 179.0876  3   1984.211     0.28              4.88             94.49                       5.96    1.187  363.589   0.1098   12.558

    52 241.2268  3   2225.437     0.17              4.75             96.47                       5.96    1.107  570.668   0.0720   15.761

    53 324.2820  5   2549.719     0.09              4.49             98.01                       5.96    0.962  916.297   0.1130   19.532

    54 346.8819  3   2896.601     0.04              4.23             98.96                       5.96    0.818  1.1e+03   0.0689   18.626

    55 330.3129  2   3226.914     0.03              4.07             99.34                       5.85    2.905  750.000   0.0405   10.183

    56 365.0000  5   3591.914     0.01              3.45             99.67                       5.90    4.135  1.3e+03   0.0927   14.911

    57  58.0858  2   3650.000     0.01              2.63             99.73                       5.96    4.040  360.478   0.0119    3.685

Time steps : 57/60, step size: 64.0351, 85.8945

Running simulation [simumpi]: MPI comparison np=4 (OMP_NUM_THREADS=1, np=4)

Elapsed: 0.63s

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    31  50.7446  4   1145.745     2.29              6.27             73.25                       5.96    2.859   42.481   0.1935   53.922

[rank 0] linear solve failed: DIVERGED_ITS after 500 iterations (residual norm 1.16748) - the timestep will be cut

[rank 2] linear solve failed: DIVERGED_ITS after 500 iterations (residual norm 1.16748) - the timestep will be cut

[rank 1] linear solve failed: DIVERGED_ITS after 500 iterations (residual norm 1.16748) - the timestep will be cut

[rank 3] linear solve failed: DIVERGED_ITS after 500 iterations (residual norm 1.16748) - the timestep will be cut

    32  17.2335  2 1 1162.978     2.78              6.65             70.54                       5.96    2.868   46.973   0.2357   11.689

    33  15.6387  2   1178.617     2.63              6.51             71.25                       5.96    2.831   51.846   0.0519   45.000

    34  21.2153  3   1199.832     2.36              6.02             71.88                       5.96    2.832   39.787   0.2237   15.292

    35  19.8697  2   1219.702     2.36              6.07             71.97                       5.96    2.839   36.785   0.2200    9.598

    36  18.7972  2   1238.499     2.40              6.00             71.46                       5.96    2.840   24.326   0.0834   11.900

    37  28.1923  2   1266.691     2.39              5.93             71.25                       5.96    2.844   34.644   0.1439   23.341

    38  33.5780  2   1300.269     2.46              6.20             71.59                       5.96    2.813   65.597   0.1756   33.081

    39  36.0924  3   1336.362     2.09              5.72             73.25                       5.96    2.772   36.919   0.2445   37.681

    40  32.0226  3   1368.384     1.53              5.05             76.75                       5.96    2.800  138.501   0.2224   31.056

    41  30.0934  2   1398.478     1.18              6.24             84.11                       5.96    1.922   47.002   0.0887   25.830

    42  44.1228  4   1442.600     1.08              4.99             82.23                       5.96    1.904   76.823   0.2335   19.895

    43  40.2686  2   1482.869     0.95              4.77             83.35                       5.96    2.003   60.374   0.1234   14.639

    44  51.5579  2   1534.427     0.83              4.93             85.60                       5.96    1.996   72.194   0.1419   26.049

    45  61.8162  2   1596.243     0.78              4.97             86.46                       5.96    2.451  103.617   0.1641   10.132

    46  68.8888  4   1665.132     0.62              4.60             88.20                       5.96    2.563  123.336   0.0910    5.663

    47 100.0538  2   1765.186     0.42              4.95             92.24                       5.96    2.681  173.611   0.0939    7.515

    48 143.6003  2   1908.786     0.31              4.91             94.05                       5.96    2.568  274.152   0.0631   10.198

    49 235.8207  4   2144.607     0.19              4.76             96.12                       5.96    2.428  530.432   0.1032   15.903

    50 325.9398  5   2470.546     0.10              4.53             97.80                       5.96    2.240  892.777   0.1418   20.365

    51 353.5702  3   2824.117     0.05              4.30             98.86                       5.96    2.023  1.1e+03   0.0742   19.447

    52 339.2504  2   3163.367     0.03              4.14             99.27                       5.85    4.024  750.000   0.0434   10.644

    53 365.0000  4   3528.367     0.01              3.66             99.62                       5.89    5.047  1.2e+03   0.0660   14.540

    54 121.6328  3   3650.000     0.01              2.61             99.75                       5.96    4.797  711.862   0.0546    7.516

Time steps : 54/56, step size: 67.5926, 87.6498

simuapp          rc=0   4.06s  114/157 steps  to  3650.00 days

simumpi np=1     rc=0   3.99s  114/157 steps, 43 cuts  to  3650.00 days

simumpi np=2     rc=0   0.55s   57/ 60 steps,  3 cuts  to  3650.00 days

simumpi np=4     rc=0   0.35s   54/ 56 steps,  2 cuts  to  3650.00 days

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

Elapsed: 9.66s

   194  64.9779  1   1095.000     2.12              1.43             40.39                               3.332   48.628   0.1082    5.703



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  9.422s  99.37%      

|- Newton                                 9.234s  |- 98.00%   

  |- FluxJac                              4.013s    |- 43.46% 

  |- Update                               2.661s    |- 28.82% 

  |- ScdAcc                               0.866s    |- 9.38%  

  |- Solver                               0.747s    |- 8.10%  

  |- update_dev                           0.533s    |- 5.77%  

  |- Precond                              0.139s    |- 1.50%  

  |- alignvar                             0.053s    |- 0.57%  

  |- Residual                             0.052s    |- 0.56%  

  |- PerfJac                              0.049s    |- 0.53%  

  |- HeatLoss                             0.046s    |- 0.49%  

  |- SanitizeJac                          0.008s    |- 0.09%  

|- Output                                 0.158s  |- 1.68%    

|- Logging                                0.012s  |- 0.12%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.060s  0.63%       

|- execution                              0.058s  |- 96.31%   

------------------------------------------------------------

TOTAL                                     9.482s

============================================================



Time steps : 194/195, step size: 5.64433, 14.9923

Running simulation [simumpi]: CSS parity np=1 (OMP_NUM_THREADS=1, np=1)

Elapsed: 9.53s

   170   0.5162  1    738.211                                                                  158.99    1.194  137.519   0.1532   15.423

   171   0.5959  1    738.807                                                                  158.96    1.194  188.138   0.2335   10.251

   172   0.5439  1    739.351                                                                  158.99    1.194   97.685   0.0482   12.854

   173   0.6491  2    740.000                                                                  159.11    1.194   47.937   0.2281    3.420

   174   7.0000  3    747.000                                                                            1.194  1.1e+03   0.1497   27.812

   175   1.0000  3    748.000     5.28            153.70             96.68                               1.204  967.216   0.2367   40.373

   176   0.6519  1    748.652    34.30            109.36             76.13                               1.246  110.559   0.1500    5.902

   177   0.7606  1    749.412    15.58             70.87             81.98                               1.257  200.818   0.0469   11.625

   178   1.1557  1    750.568     9.98             51.43             83.75                               1.260  155.339   0.0329    8.321

   179   1.9068  1    752.475     8.94             36.22             80.20                               1.260  170.089   0.0300    7.320

   180   3.0609  1    755.536     8.08             25.63             76.03                               1.259  173.784   0.0247    7.590



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   181   4.8804  1    760.416     7.69             22.31             74.36                               1.298   85.695   0.2564    3.929

   182   4.2027  1    764.619     6.73             16.30             70.76                               1.298  139.215   0.0388    6.216

   183   7.1514  1    771.770     5.56             11.68             67.74                               1.298  140.802   0.0549    7.167

   184  12.1315  1    783.902     4.26              8.11             65.53                               1.298  144.617   0.0798    7.933

   185  18.4757  1    802.378     3.28              5.89             64.24                               1.295  125.088   0.0840    8.149

   186  27.6379  1    830.015     2.64              4.11             60.84                               1.292   97.063   0.0868   10.160

   187  40.8450  2    870.860     2.24              3.42             60.44                               1.359   39.352   0.1300    6.250

   188  51.0646  4    921.925     2.09              2.97             58.67                               1.482   26.884   0.1469    4.759

   189  60.2036  2    982.129     2.09              2.61             55.44                               1.634   25.101   0.1223    4.171

   190  77.3777  7   1059.506     2.08              1.84             46.85                               1.691   54.899   0.1398   10.431

   191  35.4937  1   1095.000     1.97              1.76             47.12                               1.827    2.104   0.0806    0.273

Time steps : 191/192, step size: 5.73298, 15.3821

Running simulation [simumpi]: CSS parity np=2 (OMP_NUM_THREADS=1, np=2)

Elapsed: 6.60s

   174   0.8183  1    739.310                                                                  158.98    1.267  135.580   0.0357   19.058

   175   0.6899  1    740.000                                                                  158.99    1.267   36.680   0.2205    8.798

   176   7.0000  5    747.000                                                                            1.267  1.1e+03   0.2072   29.255

   177   1.0000  4    748.000    48.53            110.45             69.47                               1.361  775.617   0.1587   29.865

   178   0.7605  2    748.760     3.37             41.50             92.48                               1.356  623.025   0.1082   33.427

   179   0.6667  1    749.427     9.94             56.72             85.09                               1.359  131.700   0.0768    5.275

   180   1.0290  1    750.456     8.93             50.20             84.90                               1.359  129.560   0.0446    5.438



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   181   1.7844  1    752.241     8.75             36.15             80.52                               1.358  153.833   0.0248    6.404

   182   2.9525  1    755.193     9.13             32.97             78.32                               1.389   53.959   0.2744    2.387

   183   2.4347  1    757.628     8.95             25.20             73.78                               1.388  131.278   0.1922    5.370

   184   2.4904  1    760.118     8.53             20.12             70.23                               1.387  107.758   0.1802    4.519

   185   2.6401  1    762.758     7.72             16.27             67.82                               1.387   88.032   0.1324    3.894

   186   3.2724  1    766.031     6.65             13.29             66.67                               1.388   81.789   0.0448    3.960

   187   5.8786  1    771.909     5.33             10.25             65.81                               1.388  107.533   0.0448    5.355

   188  10.5626  1    782.472     3.97              7.73             66.04                               1.389  129.330   0.0744    6.937

   189  16.4740  1    798.946     3.80              7.36             65.97                               1.498   14.565   0.0686    1.643

   190  26.3803  5    825.326     2.92              5.09             63.57                               1.497  147.126   0.1039   13.889

   191  36.3723  1    861.698     2.34              3.81             61.92                               1.517   82.881   0.1061    7.649

   192  49.7106  4    911.409     2.06              3.36             62.06                               1.635   27.241   0.0794    4.307

   193  75.8561 12    987.265     1.89              2.50             56.97                               1.725   56.370   0.1540   10.051

   194  75.8561  4   1063.121     1.88              2.01             51.55                               1.852   33.582   0.1145    5.400

   195  31.8788  1   1095.000     2.12              1.65             43.77                               1.866   24.592   0.0914    3.903

Time steps : 195/198, step size: 5.61538, 15.7905

Running simulation [simumpi]: CSS parity np=4 (OMP_NUM_THREADS=1, np=4)

Elapsed: 4.54s

   173   0.6901  1    737.588                                                                  158.99    1.074  124.140   0.0511   18.765

   174   0.8779  2    738.466                                                                  158.99    1.073  230.003   0.1937   23.447

   175   0.8939  2    739.360                                                                  158.89    1.073  120.549   0.3507   17.097

   176   0.6405  2    740.000                                                                  158.13    1.073   43.050   0.2311   14.992

   177   7.0000  3    747.000                                                                            1.074  1.1e+03   0.1379   27.202

   178   1.0000  5    748.000    15.14            143.85             90.48                               1.101  895.853   0.2679   35.928

   179   0.6885  2    748.689     2.26             19.18             89.48                               1.089  571.500   0.1709   34.767

   180   0.6312  1    749.320     8.35             32.12             79.37                               1.094  111.320   0.0520    7.289



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   181   1.0938  1    750.414     9.75             87.41             89.97                               1.098  111.382   0.1500    7.643

   182   1.2761  1    751.690    11.26             53.85             82.71                               1.097  141.991   0.0653    5.807

   183   2.0743  1    753.764    10.17             36.14             78.04                               1.097  153.899   0.0303    6.424

   184   3.4316  1    757.196     8.65             23.90             73.42                               1.096  169.830   0.0296    6.998

   185   5.5112  1    762.707     7.09             17.07             70.66                               1.096  178.444   0.0294    7.393

   186   8.7133  1    771.420     5.56             12.03             68.37                               1.097  160.672   0.0386    7.795

   187  14.2329  1    785.653     4.09              8.21             66.77                               1.097  163.274   0.0596    9.039

   188  23.1364  2    808.789     3.39              5.90             63.52                               1.095  127.905   0.2074   12.520

   189  22.6567  1    831.446     3.26              5.76             63.84                               1.228   13.114   0.0811    1.450

   190  34.3197  1    865.766     2.74              4.18             60.35                               1.248   82.493   0.0834    9.996

   191  51.4661  5    917.232     2.30              3.51             60.38                               1.366   37.341   0.0945    5.153

   192  73.6746  6    990.907     2.45              2.04             45.43                               1.373   84.395   0.1369   12.909

   193  89.8797  4   1080.786     2.20              1.61             42.20                               1.473   49.968   0.1185   10.175

   194  14.2137  1   1095.000     2.15              1.44             40.07                               1.483    9.045   0.0813    1.921

Time steps : 194/197, step size: 5.64433, 14.2745

simuapp          rc=0   9.48s  194/195 steps  to  1095.00 days

simumpi np=1     rc=0   9.21s  191/192 steps,  1 cuts  to  1095.00 days

simumpi np=2     rc=0   6.32s  195/198 steps,  3 cuts  to  1095.00 days

simumpi np=4     rc=0   4.22s  194/197 steps,  3 cuts  to  1095.00 days

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

Elapsed: 29.57s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 28.161s  96.30%      

|- Newton                                28.014s  |- 99.48%   

  |- FluxJac                             10.591s    |- 37.81% 

  |- Update                               9.809s    |- 35.01% 

  |- ScdAcc                               2.501s    |- 8.93%  

  |- Solver                               2.431s    |- 8.68%  

  |- update_dev                           1.524s    |- 5.44%  

  |- Precond                              0.379s    |- 1.35%  

  |- Residual                             0.213s    |- 0.76%  

  |- alignvar                             0.163s    |- 0.58%  

  |- HeatLoss                             0.089s    |- 0.32%  

  |- PerfJac                              0.048s    |- 0.17%  

  |- SanitizeJac                          0.029s    |- 0.10%  

|- Output                                 0.071s  |- 0.25%    

|- Logging                                0.001s  |- 0.00%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            1.081s  3.70%       

|- execution                              0.902s  |- 83.38%   

------------------------------------------------------------

TOTAL                                    29.242s

============================================================



Time steps : 4/4, step size: 0.129526, 0.0271065

Running simulation [simuapp]: scaling baseline (attempt 2/2) (OMP_NUM_THREADS=1)

Elapsed: 29.36s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 27.997s  96.51%      

|- Newton                                27.812s  |- 99.34%   

  |- FluxJac                             10.753s    |- 38.67% 

  |- Update                               9.714s    |- 34.93% 

  |- ScdAcc                               2.474s    |- 8.90%  

  |- Solver                               2.258s    |- 8.12%  

  |- update_dev                           1.489s    |- 5.35%  

  |- Precond                              0.381s    |- 1.37%  

  |- Residual                             0.195s    |- 0.70%  

  |- alignvar                             0.152s    |- 0.55%  

  |- HeatLoss                             0.092s    |- 0.33%  

  |- PerfJac                              0.048s    |- 0.17%  

  |- SanitizeJac                          0.033s    |- 0.12%  

|- Output                                 0.101s  |- 0.36%    

|- Logging                                0.001s  |- 0.00%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            1.012s  3.49%       

|- execution                              0.834s  |- 82.44%   

------------------------------------------------------------

TOTAL                                    29.010s

============================================================



Time steps : 4/4, step size: 0.129526, 0.0271065

Running simulation [simumpi]: scaling np=1 (attempt 1/2) (OMP_NUM_THREADS=1, np=1)

Elapsed: 30.22s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-13







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

Elapsed: 29.43s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-13







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

Elapsed: 16.55s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-13







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

Elapsed: 16.33s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-13







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

Elapsed: 9.48s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-13







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

Elapsed: 9.99s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-13







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

Elapsed: 9.17s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-13







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

Elapsed: 8.82s

          |   | /  ____||  \  |  ||   ||          ||  .____|

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-10-13







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

  simuapp      4     29.01         -        -           -        -

     np=1      4     27.23     1.00x     100%      202005        0

     np=2      4     14.67     1.86x      93%      101080     2110

     np=4      4      8.22     3.31x      83%       50520     4235

     np=8      4      6.97     3.91x      49%       25610     8325 *

  * more ranks than the 4 fast cores on this CPU - paced by the slow ones, so read the efficiency as the machine's, not the partition's

```

```
Script completed at: 2026-10-13 22:52:43

```
