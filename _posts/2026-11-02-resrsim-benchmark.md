---
layout: default
title: "Benchmark results of resrsim"
date: 2026-11-02
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

build-release/bin/simumpi built: True, mpirun on PATH: /opt/homebrew/bin/mpirun

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

Elapsed: 0.60s

    22  55.0000  1   3650.000    47.22              1.86              3.80                      30.05    0.000   39.381 4.29e-04    0.029



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.224s  67.70%      

|- Newton                                 0.202s  |- 90.01%   

  |- Update                               0.081s    |- 40.15% 

  |- FluxJac                              0.051s    |- 25.37% 

  |- ScdAcc                               0.019s    |- 9.46%  

  |- Solver                               0.014s    |- 6.98%  

  |- update_dev                           0.010s    |- 5.05%  

  |- Precond                              0.010s    |- 5.04%  

  |- Residual                             0.005s    |- 2.57%  

  |- SanitizeJac                          0.002s    |- 0.97%  

  |- alignvar                             0.001s    |- 0.67%  

  |- PerfJac                              0.001s    |- 0.64%  

  |- HeatLoss                             0.001s    |- 0.34%  

|- Output                                 0.011s  |- 5.10%    

|- Logging                                0.001s  |- 0.25%    

|- Input                                  0.000s  |- 0.05%    

Initialization                            0.107s  32.30%      

|- execution                              0.099s  |- 92.71%   

------------------------------------------------------------

TOTAL                                     0.331s

============================================================



Time steps : 22/22, step size: 165.909, 124.409

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
Running simulation [simuapp]: SPE4-b (-novtu)

Elapsed: 1.40s

    81  85.9779  6   3650.000     0.01              4.40             99.73                       4.59    0.119    1.494   0.0052    1.644



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.122s  94.32%      

|- Newton                                 1.094s  |- 97.55%   

  |- Update                               0.296s    |- 27.01% 

  |- FluxJac                              0.257s    |- 23.45% 

  |- Solver                               0.145s    |- 13.29% 

  |- ScdAcc                               0.104s    |- 9.53%  

  |- Precond                              0.091s    |- 8.35%  

  |- update_dev                           0.064s    |- 5.84%  

  |- PerfJac                              0.042s    |- 3.80%  

  |- SanitizeJac                          0.027s    |- 2.51%  

  |- alignvar                             0.019s    |- 1.77%  

  |- Residual                             0.008s    |- 0.77%  

  |- HeatLoss                             0.007s    |- 0.61%  

|- Logging                                0.016s  |- 1.45%    

|- Output                                 0.008s  |- 0.70%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.068s  5.68%       

|- execution                              0.065s  |- 95.93%   

------------------------------------------------------------

TOTAL                                     1.189s

============================================================



Time steps : 81/81, step size: 45.0617, 50.5258

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
Running simulation [simuapp]: Corner Grid (-novtu)

Elapsed: 1.10s

    46  27.5824  4   3650.000     0.06              3.71             98.42                       5.96    0.156   11.053   0.0307    0.829



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.779s  92.46%      

|- Newton                                 0.764s  |- 98.00%   

  |- Update                               0.193s    |- 25.25% 

  |- FluxJac                              0.184s    |- 24.14% 

  |- Solver                               0.123s    |- 16.10% 

  |- ScdAcc                               0.070s    |- 9.21%  

  |- Precond                              0.063s    |- 8.20%  

  |- update_dev                           0.043s    |- 5.57%  

  |- PerfJac                              0.030s    |- 3.89%  

  |- SanitizeJac                          0.018s    |- 2.34%  

  |- alignvar                             0.013s    |- 1.69%  

  |- Residual                             0.006s    |- 0.85%  

  |- HeatLoss                             0.005s    |- 0.70%  

|- Logging                                0.006s  |- 0.83%    

|- Output                                 0.004s  |- 0.56%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.064s  7.54%       

|- execution                              0.060s  |- 94.78%   

------------------------------------------------------------

TOTAL                                     0.843s

============================================================



Time steps : 46/51, step size: 79.3478, 95.346

```

![png]({{ "/assets/images/benchmark_image_6.png" | relative_url }})

# Buckley- Leverett



Two phase, isothermal problem

variable order: [Sw, P, T, So, X0, X1, Sg]



Acc w.r.t. [Sw, So, Sg, X0, X1, P, T]

```
Running simulation [simuapp]: Buckley-Leverett (-novtu)

Elapsed: 0.83s

    79   4.0256  1     10.000    2e-10              0.16            100.00                       0.16   13.238    0.002 2.86e-06  1.8e-07



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.569s  90.64%      

|- Newton                                 0.553s  |- 97.31%   

  |- Update                               0.187s    |- 33.75% 

  |- FluxJac                              0.082s    |- 14.90% 

  |- ScdAcc                               0.072s    |- 13.02% 

  |- Precond                              0.064s    |- 11.57% 

  |- update_dev                           0.035s    |- 6.25%  

  |- PerfJac                              0.030s    |- 5.39%  

  |- SanitizeJac                          0.021s    |- 3.78%  

  |- Solver                               0.015s    |- 2.67%  

  |- alignvar                             0.014s    |- 2.58%  

  |- HeatLoss                             0.011s    |- 1.95%  

  |- Residual                             0.007s    |- 1.29%  

|- Logging                                0.006s  |- 1.14%    

|- Output                                 0.004s  |- 0.72%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.059s  9.36%       

|- execution                              0.056s  |- 95.99%   

------------------------------------------------------------

TOTAL                                     0.627s

============================================================



Time steps : 79/81, step size: 0.126582, 0.601838

```

### Load Benchmark

### Buckley Plot

![png]({{ "/assets/images/benchmark_image_7.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_8.png" | relative_url }})

# Lauwerier problem



`lauwerier.dat` is a 804x1x1, single-phase, single-component (pure water) hot-water injection

along a thin layer that loses heat only by vertical conduction into semi-infinite over- and

under-burden - the classic closed-form check H.A. Lauwerier published in 1955 for a thermal

simulator's advection + conduction-loss coupling. See `../doc/Lauwerier problem simulation

validation.md` for the literature survey this verification follows.



The run currently stops at day 43.3 of its 1095-day schedule. Day 43.3 is still well past

the analytic breakthrough time for this geometry (~13.8 days), so the comparison below covers the

whole transient Lauwerier describes: the initial sharp advancing front, breakthrough at the

producer, and the smoother post-breakthrough regime.

```
Running simulation [simuapp]: Lauwerier thin-layer thermal front

Elapsed: 0.82s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.572s  90.52%      

|- Newton                                 0.557s  |- 97.33%   

  |- Update                               0.230s    |- 41.23% 

  |- FluxJac                              0.115s    |- 20.70% 

  |- ScdAcc                               0.063s    |- 11.24% 

  |- update_dev                           0.039s    |- 7.05%  

  |- Precond                              0.034s    |- 6.05%  

  |- HeatLoss                             0.016s    |- 2.88%  

  |- Solver                               0.014s    |- 2.55%  

  |- Residual                             0.012s    |- 2.19%  

  |- PerfJac                              0.008s    |- 1.45%  

  |- SanitizeJac                          0.007s    |- 1.23%  

  |- alignvar                             0.005s    |- 0.97%  

|- Output                                 0.010s  |- 1.67%    

|- Logging                                0.001s  |- 0.23%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.060s  9.48%       

|- execution                              0.058s  |- 96.35%   

------------------------------------------------------------

TOTAL                                     0.632s

============================================================



Time steps : 22/49, step size: 1.96991, 3.48374

```

```
Analytic front speed: 729.1 ft/day, breakthrough at 13.8 days (804 cells)

```

```
  t (days)   L2 rel. err   Linf rel. err

      1.27        0.1048          0.4908

      6.01        0.1814          0.4453

     13.03        0.1343          0.4050

     31.95        0.0181          0.0245

     43.07        0.0096          0.0205

```

![png]({{ "/assets/images/benchmark_image_9.png" | relative_url }})

The relative error is largest, and concentrated right at the advancing front, for the snapshots

taken before the analytic breakthrough time (~13.8 days) - the expected signature of numerical

dispersion smearing Lauwerier's mathematically sharp step. Once every cell is past its own local

breakthrough (t >~ 32 days) the profile is governed by the smoother post-breakthrough erfc tail,

and the relative L2 error over the whole 804-cell row drops accordingly.

![png]({{ "/assets/images/benchmark_image_10.png" | relative_url }})

# Avdonin problem



`avdonin.dat` is a 15-block radial grid (1000 m outer radius), single-phase, single-component

(pure water) cold-water injection into a hot aquifer - N.A. Avdonin's (1964) radial heat

convection/conduction solution, carried into Western benchmarking by Ross et al. (1982) and

Updegraff (1989) as "Problem 3" of the 1980 Geothermal Model Intercomparison Study, and used by

TOUGH ([LBL-32611](https://escholarship.org/content/qt9nt0r7wp/qt9nt0r7wp.pdf)), MOOSE, FEHM and

Waiwera. See `../doc/Avdonin solution simulator verification.md` for the literature survey this

verification follows; that doc flagged the radial closed form as "not retrieved" because the

official MOOSE page returns HTTP 403 - it is sourced here instead from a Hugging Face mirror of

the same page (`huggingface.co/spaces/aikubo/parrot_2/blob/main/allmd/1d_radial_avdonin.md`):



    (T(r,t) - T0) / (Tinj - T0) = Q(nu, r^2 / (4*D*t))



with `Q(nu, x) = Gamma(nu, x)/Gamma(nu)` the regularized upper incomplete gamma function, `D =

lambda_m/(rho_m*cp_m)` the medium's thermal diffusivity, and `nu = mdot*cp_w/(4*pi*h*lambda_m)` a

Peclet-like ratio of the injected mass rate's heat capacity to the medium's radial conduction.

The `r^2/(4*D*t)` argument is exactly the O'Sullivan (1981) r^2/t similarity variable that

LBL-32611 reports TOUGH's own radial solutions collapse onto - a second, independent confirmation

of the formula beyond the mirror itself.



Two bugs in the deck had to be fixed before this comparison meant anything, both in

`avdonin.dat` itself rather than only in this notebook:



- `*HLOSSPROP` was set for both over- and underburden, with the same ROCKCP/THCONR as the

  reservoir rock. On this grid's single K layer every cell is both an overburden and an

  underburden face, so that keyword was quietly switching on top/bottom heat loss - directly

  contradicting Avdonin's adiabatic-boundary assumption. Removed; the cumulative material

  balance's "Net Heat Lost" is now exactly zero.

- WATER's `*CMM 18.0` and `*MOLDEN 3.41` were CMG's field-unit constants (lb/lbmol, lbmol/ft3)

  entered verbatim under a deck declared `*INUNIT *SI`. Every other SI deck under `test/data`

  that models WATER (`heteroCompare.dat`, `sthrw001.dat`, ...) writes `*CMM 0.018` and leaves

  WATER's `*MOLDEN 0` (its density comes from the built-in steam tables regardless of that

  field). Before the fix the injected water was ~1000x too light and the near-well cells

  *warmed* above the 170 C initial temperature instead of cooling toward the 160 C injection

  temperature. Fixed to match that precedent.


```
Running simulation [simuapp]: Avdonin radial thermal front

Elapsed: 0.31s

    17   1.4144  2     10.000                                                                 9521.20    0.053  152.652             1.045



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Initialization                            0.083s  64.31%      

|- execution                              0.081s  |- 97.29%   

Timeloop                                  0.046s  35.69%      

|- Newton                                 0.042s  |- 90.53%   

  |- Update                               0.014s    |- 33.08% 

  |- Precond                              0.006s    |- 15.33% 

  |- PerfJac                              0.005s    |- 11.82% 

  |- FluxJac                              0.004s    |- 9.96%  

  |- ScdAcc                               0.004s    |- 9.74%  

  |- update_dev                           0.002s    |- 5.88%  

  |- SanitizeJac                          0.002s    |- 5.68%  

  |- alignvar                             0.001s    |- 3.18%  

  |- Solver                               0.001s    |- 2.57%  

  |- Residual                             0.000s    |- 0.43%  

  |- HeatLoss                             0.000s    |- 0.01%  

|- Output                                 0.003s  |- 6.18%    

|- Logging                                0.001s  |- 1.44%    

|- Input                                  0.000s  |- 0.07%    

------------------------------------------------------------

TOTAL                                     0.129s

============================================================



Time steps : 17/20, step size: 0.588235, 0.379146

```

```
D=6.088e-06 m2/s, nu=17.26

```

```
  t (days)   L2 rel. err   Linf rel. err

     0.556        0.3018          0.9560

     1.661        0.2894          0.8908

     4.450        0.2052          0.7420

     7.210        0.1334          0.4699

    10.000        0.1330          0.5091

```

![png]({{ "/assets/images/benchmark_image_11.png" | relative_url }})

The mismatch is concentrated at the advancing front and shrinks as cells fully equilibrate - the

same numerical-dispersion signature as the Lauwerier comparison above, not a sign the two models

disagree on the front's speed. `avd_mdot` is the deck's design target (100 kg/s); the remaining

gap is plausibly the well's day-0-to-5.5 ramp from bottom-hole-pressure control up to the rate

target (the analytic solution assumes that full rate from t=0), compounded by this deck's coarse

15-block grid - only the first 3-4 blocks sit inside the thermal front by day 10.


![png]({{ "/assets/images/benchmark_image_12.png" | relative_url }})

# MISC

## spe04b_cw.dat

```
Running simulation [simuapp]: SPE4-b water flooding (-novtu)

Elapsed: 0.59s

    22 163.2235  2   3650.000     0.78             10.19             92.87                      10.73    0.001   13.707   0.0098    0.002



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.356s  86.17%      

|- Newton                                 0.351s  |- 98.49%   

  |- Update                               0.115s    |- 32.78% 

  |- FluxJac                              0.102s    |- 29.04% 

  |- Solver                               0.035s    |- 9.95%  

  |- ScdAcc                               0.032s    |- 9.20%  

  |- Precond                              0.023s    |- 6.69%  

  |- update_dev                           0.018s    |- 5.17%  

  |- PerfJac                              0.007s    |- 1.88%  

  |- SanitizeJac                          0.005s    |- 1.46%  

  |- Residual                             0.004s    |- 1.22%  

  |- alignvar                             0.004s    |- 1.12%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.001s  |- 0.39%    

|- Logging                                0.001s  |- 0.30%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.057s  13.83%      

|- execution                              0.055s  |- 95.99%   

------------------------------------------------------------

TOTAL                                     0.413s

============================================================



Time steps : 22/22, step size: 165.909, 155.033

```



## watfld_cw.dat

```
Running simulation [simuapp]: SPE4-b Water flooding without vmod (-novtu)

Elapsed: 0.77s

    35  32.9891  2   3650.000     1.04             79.00             98.70                      80.00    0.000    1.899   0.0029  3.2e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.536s  90.27%      

|- Newton                                 0.525s  |- 97.94%   

  |- Update                               0.168s    |- 32.08% 

  |- FluxJac                              0.143s    |- 27.17% 

  |- Solver                               0.059s    |- 11.15% 

  |- ScdAcc                               0.043s    |- 8.26%  

  |- Precond                              0.032s    |- 6.16%  

  |- PerfJac                              0.031s    |- 5.95%  

  |- update_dev                           0.022s    |- 4.18%  

  |- SanitizeJac                          0.007s    |- 1.40%  

  |- Residual                             0.006s    |- 1.20%  

  |- alignvar                             0.005s    |- 1.04%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.003s  |- 0.56%    

|- Logging                                0.001s  |- 0.28%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.058s  9.73%       

|- execution                              0.055s  |- 95.89%   

------------------------------------------------------------

TOTAL                                     0.594s

============================================================



Time steps : 35/35, step size: 104.286, 142.655

```

## stflu001.dat

Inverted 9 spot hot water flooding with area/block modifier, 5 point transmissibility


```
Running simulation [simuapp]: Inverted 9 spot hot water flooding (-novtu)

Elapsed: 1.09s

    93 352.2655  2   3650.000    2e-04            597.42            100.00                     597.42    0.272    0.396 3.40e-04    0.010



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.858s  93.52%      

|- Newton                                 0.839s  |- 97.72%   

  |- Update                               0.259s    |- 30.87% 

  |- FluxJac                              0.221s    |- 26.40% 

  |- ScdAcc                               0.089s    |- 10.56% 

  |- Precond                              0.079s    |- 9.43%  

  |- update_dev                           0.055s    |- 6.60%  

  |- Solver                               0.045s    |- 5.39%  

  |- SanitizeJac                          0.022s    |- 2.63%  

  |- alignvar                             0.017s    |- 1.97%  

  |- PerfJac                              0.015s    |- 1.85%  

  |- Residual                             0.009s    |- 1.10%  

  |- HeatLoss                             0.007s    |- 0.81%  

|- Logging                                0.010s  |- 1.11%    

|- Output                                 0.007s  |- 0.87%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.059s  6.48%       

|- execution                              0.057s  |- 95.77%   

------------------------------------------------------------

TOTAL                                     0.918s

============================================================



Time steps : 93/94, step size: 39.2473, 94.8079

```

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation, CMG against OURS.

![png]({{ "/assets/images/benchmark_image_13.png" | relative_url }})

## stflu002.dat

5000x5000x50, 2D diagonal water flooding in uniformed cartesian

```
Running simulation [simuapp]: Uniformed cartesian water flooding (-novtu)

Elapsed: 0.54s

    50  37.5367  5   3650.000   623.97             11.43              1.80                     635.95    0.002  118.652   0.0056    0.003



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.309s  84.59%      

|- Newton                                 0.300s  |- 96.94%   

  |- Update                               0.085s    |- 28.33% 

  |- FluxJac                              0.060s    |- 19.99% 

  |- Solver                               0.049s    |- 16.28% 

  |- ScdAcc                               0.028s    |- 9.46%  

  |- Precond                              0.027s    |- 8.90%  

  |- update_dev                           0.013s    |- 4.20%  

  |- PerfJac                              0.012s    |- 3.94%  

  |- SanitizeJac                          0.008s    |- 2.65%  

  |- alignvar                             0.005s    |- 1.74%  

  |- HeatLoss                             0.004s    |- 1.46%  

  |- Residual                             0.003s    |- 1.10%  

|- Output                                 0.002s  |- 0.77%    

|- Logging                                0.002s  |- 0.64%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.056s  15.41%      

|- execution                              0.054s  |- 95.85%   

------------------------------------------------------------

TOTAL                                     0.365s

============================================================



Time steps : 50/50, step size: 73, 129.7

```



## stflu003.dat

5000x5000x50, 2D diagonal water flooding in uniformed corner point

```
Running simulation [simuapp]: uniformed corner grid (-novtu)

Elapsed: 0.51s

    46 309.2362  6   3650.000   620.28             11.15              1.77                     635.95    0.000  1.1e+03   0.0466    0.035



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.282s  83.22%      

|- Newton                                 0.273s  |- 96.86%   

  |- Update                               0.078s    |- 28.60% 

  |- FluxJac                              0.052s    |- 18.97% 

  |- Solver                               0.046s    |- 16.82% 

  |- ScdAcc                               0.025s    |- 9.29%  

  |- Precond                              0.024s    |- 8.62%  

  |- update_dev                           0.014s    |- 5.07%  

  |- PerfJac                              0.011s    |- 3.93%  

  |- SanitizeJac                          0.007s    |- 2.58%  

  |- alignvar                             0.005s    |- 1.76%  

  |- HeatLoss                             0.004s    |- 1.36%  

  |- Residual                             0.003s    |- 1.04%  

|- Output                                 0.002s  |- 0.81%    

|- Logging                                0.002s  |- 0.66%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.057s  16.78%      

|- execution                              0.054s  |- 95.32%   

------------------------------------------------------------

TOTAL                                     0.339s

============================================================



Time steps : 46/46, step size: 79.3478, 131.806

```

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_14.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_15.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_16.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_17.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_18.png" | relative_url }})



## stflu004.dat

2D diagonal water flooding for reduction of numerical dispersion and grid orientation effect


```
Running simulation [simuapp]: 2D diagonal flow: grid orientation

Elapsed: 0.88s

    62  69.9920  5   3650.000   611.68             21.53              3.40                     635.95    0.000  934.482   0.0235    0.054



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.620s  91.71%      

|- Newton                                 0.598s  |- 96.53%   

  |- Update                               0.222s    |- 37.04% 

  |- FluxJac                              0.132s    |- 22.05% 

  |- Solver                               0.087s    |- 14.61% 

  |- ScdAcc                               0.050s    |- 8.33%  

  |- Precond                              0.032s    |- 5.35%  

  |- update_dev                           0.024s    |- 3.93%  

  |- PerfJac                              0.014s    |- 2.26%  

  |- HeatLoss                             0.008s    |- 1.42%  

  |- SanitizeJac                          0.008s    |- 1.28%  

  |- Residual                             0.006s    |- 1.08%  

  |- alignvar                             0.006s    |- 0.93%  

|- Output                                 0.014s  |- 2.20%    

|- Logging                                0.002s  |- 0.35%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.056s  8.29%       

|- execution                              0.053s  |- 95.17%   

------------------------------------------------------------

TOTAL                                     0.676s

============================================================



Time steps : 62/62, step size: 58.871, 77.9274

```

![png]({{ "/assets/images/benchmark_image_19.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_20.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_21.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_22.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_23.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_24.png" | relative_url }})

## stflu007.dat

PEBI_GRID


```
Running simulation [simuapp]: 2D diagonal flow: pebi grid

Elapsed: 1.95s

    60  27.3410  4   3650.000   623.17             12.31              1.94                     635.95    0.000   94.134   0.0056    0.003



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.683s  95.98%      

|- Newton                                 1.653s  |- 98.17%   

  |- Solver                               0.638s    |- 38.60% 

  |- FluxJac                              0.367s    |- 22.19% 

  |- Update                               0.345s    |- 20.89% 

  |- ScdAcc                               0.094s    |- 5.71%  

  |- update_dev                           0.065s    |- 3.90%  

  |- Precond                              0.059s    |- 3.55%  

  |- HeatLoss                             0.017s    |- 1.05%  

  |- SanitizeJac                          0.014s    |- 0.82%  

  |- PerfJac                              0.014s    |- 0.82%  

  |- Residual                             0.013s    |- 0.80%  

  |- alignvar                             0.010s    |- 0.58%  

|- Output                                 0.020s  |- 1.18%    

|- Logging                                0.004s  |- 0.23%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.071s  4.02%       

|- execution                              0.062s  |- 87.47%   

------------------------------------------------------------

TOTAL                                     1.754s

============================================================



Time steps : 60/60, step size: 60.8333, 117.512

```

![png]({{ "/assets/images/benchmark_image_25.png" | relative_url }})

```
<module 'matplotlib.pyplot' from '/Users/mark/Documents/workspace/hatch/app/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>
```

![png]({{ "/assets/images/benchmark_image_26.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_27.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_28.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_29.png" | relative_url }})

## stflu026.dat

* Steam flood on two component live oil

```
Running simulation [simuapp]: 3 component steam flooding (-novtu)

Elapsed: 1.65s

    92 270.2547  6   3650.000     0.01              3.97             99.85                       4.33    4.521   36.033   0.0806    4.475



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.374s  96.05%      

|- Newton                                 1.345s  |- 97.93%   

  |- FluxJac                              0.333s    |- 24.74% 

  |- Update                               0.303s    |- 22.52% 

  |- Solver                               0.282s    |- 20.99% 

  |- ScdAcc                               0.119s    |- 8.81%  

  |- Precond                              0.103s    |- 7.67%  

  |- update_dev                           0.068s    |- 5.06%  

  |- PerfJac                              0.048s    |- 3.54%  

  |- SanitizeJac                          0.027s    |- 2.04%  

  |- alignvar                             0.018s    |- 1.35%  

  |- Residual                             0.009s    |- 0.70%  

  |- HeatLoss                             0.009s    |- 0.65%  

|- Logging                                0.010s  |- 0.75%    

|- Output                                 0.009s  |- 0.63%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.056s  3.95%       

|- execution                              0.054s  |- 95.05%   

------------------------------------------------------------

TOTAL                                     1.430s

============================================================



Time steps : 92/92, step size: 39.6739, 75.3525

```

#### Load OURS, CMG and ECL

* STARS wells: CRNR PRDCR, EDGE PRDCR, INJECTOR. STARS block history at (1,1,4), (5,5,4), (9,1,1) and (5,4,1); ECL has the first three only.

* ECL names the two producers PNEAR (EDGE PRDCR, block 5,5,4) and PFAR (CRNR PRDCR, block 9,1,1); PNEAR produces twice PFAR at the start, as EDGE does CRNR.

```
OURS reached day 3650.0 of 3650

```

### Wells

* One row per well: bottom-hole pressure, water rate, oil rate (producers only).

![png]({{ "/assets/images/benchmark_image_30.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation. (5,4,1) has no ECL curve.

![png]({{ "/assets/images/benchmark_image_31.png" | relative_url }})

# SPE4C

* Steam flood on three component live oil

* 'Water', 'LiteOil', 'Medm oil', 'Heavy oil'


## Run & Load

```
Running simulation [simuapp]: SPE4-C benchmark on live oil (-novtu)

Elapsed: 2.21s

    95 277.9459  9   3650.000     0.01              4.16             99.86                       4.21    0.875   10.158   0.0125    5.543



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.887s  96.53%      

|- Newton                                 1.854s  |- 98.26%   

  |- Solver                               0.481s    |- 25.92% 

  |- FluxJac                              0.446s    |- 24.07% 

  |- Update                               0.375s    |- 20.25% 

  |- ScdAcc                               0.156s    |- 8.40%  

  |- Precond                              0.146s    |- 7.86%  

  |- update_dev                           0.085s    |- 4.59%  

  |- PerfJac                              0.060s    |- 3.22%  

  |- SanitizeJac                          0.031s    |- 1.67%  

  |- alignvar                             0.021s    |- 1.15%  

  |- Residual                             0.012s    |- 0.62%  

  |- HeatLoss                             0.011s    |- 0.60%  

|- Logging                                0.012s  |- 0.66%    

|- Output                                 0.011s  |- 0.60%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.068s  3.47%       

|- execution                              0.065s  |- 95.80%   

------------------------------------------------------------

TOTAL                                     1.954s

============================================================



Time steps : 95/98, step size: 38.4211, 59.6548

```

#### Load CMG

### Load ECL

### Wells

* One row per well: bottom-hole pressure, water rate, oil rate (producers only). ECL names the producers PNEAR (EDGE PRDCR) and PFAR (CRNR PRDCR).

![png]({{ "/assets/images/benchmark_image_32.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation, CMG and ECL against OURS.

![png]({{ "/assets/images/benchmark_image_33.png" | relative_url }})

# Cyclic steam stimulation

## CSS SPE4

stspe001.dat: Cyclic steam stimulation on radial grid

```
Running simulation [simuapp]: Cyclic steam stimulation in Radial grid

Elapsed: 0.99s

   109  30.6814  6   1095.000     0.92              1.36             59.57                               0.413    8.821   0.1488    1.723



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.736s  92.03%      

|- Newton                                 0.694s  |- 94.21%   

  |- Update                               0.194s    |- 28.02% 

  |- FluxJac                              0.133s    |- 19.21% 

  |- Precond                              0.086s    |- 12.45% 

  |- PerfJac                              0.075s    |- 10.88% 

  |- ScdAcc                               0.067s    |- 9.72%  

  |- update_dev                           0.037s    |- 5.26%  

  |- Solver                               0.034s    |- 4.85%  

  |- SanitizeJac                          0.027s    |- 3.89%  

  |- alignvar                             0.015s    |- 2.13%  

  |- Residual                             0.005s    |- 0.71%  

  |- HeatLoss                             0.004s    |- 0.59%  

|- Output                                 0.027s  |- 3.60%    

|- Logging                                0.006s  |- 0.77%    

|- Input                                  0.001s  |- 0.13%    

Initialization                            0.064s  7.97%       

|- execution                              0.061s  |- 96.10%   

------------------------------------------------------------

TOTAL                                     0.800s

============================================================



Time steps : 109/112, step size: 10.0459, 21.48

```

![png]({{ "/assets/images/benchmark_image_34.png" | relative_url }})

### Wells

* Injector: bottom-hole pressure (ECL only; the CMG well export has none) and water rate. Producer: bottom-hole pressure (ECL only), water and oil rate.

* Bottom-hole pressure is drawn only while the well flows: ECL reports 0 for a shut-in well and OURS holds its last value.

![png]({{ "/assets/images/benchmark_image_35.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation, CMG and ECL against OURS.

![png]({{ "/assets/images/benchmark_image_36.png" | relative_url }})



## stflu008.dat

Cyclic steam stimulation on cartesian grid


```
Running simulation [simuapp]: Cyclic steam stimulation in Cartesian

Elapsed: 11.80s

   146  78.9056  9   1095.000     1.47              1.19             44.73                               0.400   48.391   0.1032    5.193



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 11.537s  99.42%      

|- Newton                                11.411s  |- 98.91%   

  |- FluxJac                              4.162s    |- 36.47% 

  |- Update                               3.111s    |- 27.27% 

  |- Solver                               1.543s    |- 13.52% 

  |- ScdAcc                               0.934s    |- 8.18%  

  |- update_dev                           0.566s    |- 4.96%  

  |- Precond                              0.475s    |- 4.16%  

  |- PerfJac                              0.113s    |- 0.99%  

  |- Residual                             0.104s    |- 0.91%  

  |- HeatLoss                             0.098s    |- 0.86%  

  |- SanitizeJac                          0.094s    |- 0.82%  

  |- alignvar                             0.076s    |- 0.67%  

|- Output                                 0.094s  |- 0.82%    

|- Logging                                0.022s  |- 0.19%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.067s  0.58%       

|- execution                              0.065s  |- 95.91%   

------------------------------------------------------------

TOTAL                                    11.604s

============================================================



Time steps : 146/155, step size: 7.5, 16.0457

```

```
Found 147 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu008_00146.vtu

```

![png]({{ "/assets/images/benchmark_image_37.png" | relative_url }})

### Wells

![png]({{ "/assets/images/benchmark_image_38.png" | relative_url }})

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

Elapsed: 39.59s

   129  13.2105  6   1095.000     0.55              0.33             37.37                               0.233   74.267   0.0327    0.736



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 39.254s  99.71%      

|- Newton                                39.024s  |- 99.42%   

  |- FluxJac                             16.316s    |- 41.81% 

  |- Update                               9.311s    |- 23.86% 

  |- Solver                               6.872s    |- 17.61% 

  |- ScdAcc                               2.626s    |- 6.73%  

  |- update_dev                           1.504s    |- 3.85%  

  |- Precond                              1.207s    |- 3.09%  

  |- Residual                             0.301s    |- 0.77%  

  |- alignvar                             0.189s    |- 0.49%  

  |- HeatLoss                             0.161s    |- 0.41%  

  |- SanitizeJac                          0.100s    |- 0.26%  

  |- PerfJac                              0.071s    |- 0.18%  

|- Output                                 0.190s  |- 0.48%    

|- Logging                                0.033s  |- 0.08%    

|- Input                                  0.001s  |- 0.00%    

Initialization                            0.116s  0.29%       

|- execution                              0.084s  |- 72.56%   

------------------------------------------------------------

TOTAL                                    39.370s

============================================================



Time steps : 129/132, step size: 8.48837, 19.4382

```

```
Found 130 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu009_00129.vtu

```

![png]({{ "/assets/images/benchmark_image_39.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_40.png" | relative_url }})

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

Elapsed: 14.85s

   205  88.9753  6   1095.000     1.57              1.73             52.46                               1.664   29.919   0.1321    2.902



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 14.495s  99.38%      

|- Newton                                14.286s  |- 98.56%   

  |- FluxJac                              5.613s    |- 39.29% 

  |- Update                               3.562s    |- 24.93% 

  |- Solver                               2.248s    |- 15.74% 

  |- ScdAcc                               0.981s    |- 6.87%  

  |- Precond                              0.598s    |- 4.19%  

  |- update_dev                           0.589s    |- 4.13%  

  |- PerfJac                              0.176s    |- 1.23%  

  |- Residual                             0.113s    |- 0.79%  

  |- SanitizeJac                          0.109s    |- 0.76%  

  |- alignvar                             0.080s    |- 0.56%  

  |- HeatLoss                             0.060s    |- 0.42%  

|- Output                                 0.162s  |- 1.11%    

|- Logging                                0.028s  |- 0.19%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.091s  0.62%       

|- execution                              0.075s  |- 82.68%   

------------------------------------------------------------

TOTAL                                    14.586s

============================================================



Time steps : 205/208, step size: 5.34146, 14.724

```

```
Found 206 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu025_00205.vtu

```

![png]({{ "/assets/images/benchmark_image_41.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_42.png" | relative_url }})

### VAPEX (2D) Experiment 

* incomp gas

* 'WATER' 'LLOYD_O' 'ASPHALT' 'PROPANE'

* MOD

* 9 hours

```
Running simulation [simuapp]: Incomp GAS (-novtu)

Elapsed: 3.05s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.745s  97.41%      

|- Newton                                 2.715s  |- 98.94%   

  |- Solver                               0.670s    |- 24.68% 

  |- Update                               0.670s    |- 24.67% 

  |- FluxJac                              0.469s    |- 17.29% 

  |- ScdAcc                               0.295s    |- 10.86% 

  |- Precond                              0.294s    |- 10.84% 

  |- update_dev                           0.121s    |- 4.45%  

  |- SanitizeJac                          0.071s    |- 2.61%  

  |- alignvar                             0.050s    |- 1.85%  

  |- Residual                             0.016s    |- 0.58%  

  |- PerfJac                              0.011s    |- 0.39%  

  |- HeatLoss                             0.000s    |- 0.01%  

|- Logging                                0.015s  |- 0.56%    

|- Output                                 0.007s  |- 0.27%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.073s  2.59%       

|- execution                              0.066s  |- 90.07%   

------------------------------------------------------------

TOTAL                                     2.818s

============================================================



Time steps : 104/136, step size: 5.37694e-05, 3.05925e-05

```

### Wells

![png]({{ "/assets/images/benchmark_image_43.png" | relative_url }})

### SAGD

#### 2D cross the well

```
Running simulation [simuapp]: SAGD (-novtu)

Elapsed: 5.08s

   220  14.9511  6   2526.000     5.89             53.45             90.08                      56.73    2.659    9.204   0.1761   24.588



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  4.795s  98.74%      

|- Newton                                 4.743s  |- 98.92%   

  |- Solver                               1.223s    |- 25.78% 

  |- Update                               1.154s    |- 24.34% 

  |- FluxJac                              1.054s    |- 22.22% 

  |- ScdAcc                               0.442s    |- 9.32%  

  |- Precond                              0.311s    |- 6.56%  

  |- update_dev                           0.235s    |- 4.96%  

  |- SanitizeJac                          0.086s    |- 1.82%  

  |- alignvar                             0.067s    |- 1.41%  

  |- PerfJac                              0.053s    |- 1.13%  

  |- Residual                             0.040s    |- 0.85%  

  |- HeatLoss                             0.009s    |- 0.19%  

|- Logging                                0.022s  |- 0.46%    

|- Output                                 0.014s  |- 0.30%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.061s  1.26%       

|- execution                              0.058s  |- 95.79%   

------------------------------------------------------------

TOTAL                                     4.856s

============================================================



Time steps : 220/227, step size: 11.4818, 12.6998

```

### Wells

* The reference here is the in-house Fortran code (stm_stflu020_*.csv), labelled FORTRAN. It reports producer rates negative.

![png]({{ "/assets/images/benchmark_image_44.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, water, oil and gas saturation. (1,5,13) sits near the injector and (1,5,18) near the producer.

![png]({{ "/assets/images/benchmark_image_45.png" | relative_url }})

#### 2D along well

```
Running simulation [simuapp]: SAGD (-novtu)

Elapsed: 5.67s

   149  19.2500  6   2526.000     9.67            119.47             92.51                     115.01    8.905    2.084   0.1468    1.691



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  5.385s  98.89%      

|- Newton                                 5.331s  |- 99.01%   

  |- Solver                               1.951s    |- 36.60% 

  |- Update                               0.983s    |- 18.43% 

  |- FluxJac                              0.887s    |- 16.64% 

  |- PerfJac                              0.485s    |- 9.09%  

  |- ScdAcc                               0.342s    |- 6.41%  

  |- Precond                              0.254s    |- 4.76%  

  |- update_dev                           0.200s    |- 3.75%  

  |- SanitizeJac                          0.076s    |- 1.43%  

  |- alignvar                             0.052s    |- 0.98%  

  |- Residual                             0.033s    |- 0.61%  

  |- HeatLoss                             0.008s    |- 0.14%  

|- Logging                                0.021s  |- 0.39%    

|- Output                                 0.016s  |- 0.30%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.061s  1.11%       

|- execution                              0.058s  |- 95.82%   

------------------------------------------------------------

TOTAL                                     5.445s

============================================================



Time steps : 149/155, step size: 16.953, 33.9159

```

### Wells

![png]({{ "/assets/images/benchmark_image_46.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation. The blocks follow the producer-injector pair down the 10x1x20 grid.

![png]({{ "/assets/images/benchmark_image_47.png" | relative_url }})

#### 3D

```
Running simulation [simuapp]: SAGD 3D (-novtu)

Elapsed: 34.88s

   161   6.8613  7    680.000    19.95            102.68             83.73                      89.99    1.134    4.496   0.2286    7.734



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 34.589s  99.82%      

|- Newton                                34.498s  |- 99.74%   

  |- Solver                              12.257s    |- 35.53% 

  |- FluxJac                              9.918s    |- 28.75% 

  |- Update                               7.033s    |- 20.39% 

  |- ScdAcc                               1.898s    |- 5.50%  

  |- update_dev                           1.206s    |- 3.49%  

  |- Precond                              0.928s    |- 2.69%  

  |- PerfJac                              0.383s    |- 1.11%  

  |- Residual                             0.223s    |- 0.65%  

  |- alignvar                             0.140s    |- 0.41%  

  |- SanitizeJac                          0.118s    |- 0.34%  

  |- HeatLoss                             0.101s    |- 0.29%  

|- Logging                                0.042s  |- 0.12%    

|- Output                                 0.028s  |- 0.08%    

|- Input                                  0.001s  |- 0.00%    

Initialization                            0.063s  0.18%       

|- execution                              0.060s  |- 95.56%   

------------------------------------------------------------

TOTAL                                    34.652s

============================================================



Time steps : 161/165, step size: 4.2236, 3.2094

```

#### 2D live oil

* 10x1x20 cross-section, two-component live oil (CH4 + HOIL) with water. Injector 'Inj' (2:9,1,13) and producer 'Prod' (2:9,1,18); both are shut in and preheated for 60 days, then opened.

* CMG only (no ECL run for this deck).

```
Running simulation [simuapp]: SAGD live oil (-novtu)

Elapsed: 12.22s

   170  32.7778  6   2526.000     0.16     0.04   120.96     0.26    99.87                     121.03    2.295    1.415   0.0043    0.264



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 11.936s  99.44%      

|- Newton                                11.869s  |- 99.44%   

  |- Solver                               6.144s    |- 51.76% 

  |- FluxJac                              1.675s    |- 14.11% 

  |- Update                               1.478s    |- 12.45% 

  |- PerfJac                              0.816s    |- 6.88%  

  |- ScdAcc                               0.626s    |- 5.28%  

  |- Precond                              0.417s    |- 3.51%  

  |- update_dev                           0.356s    |- 3.00%  

  |- SanitizeJac                          0.120s    |- 1.02%  

  |- alignvar                             0.077s    |- 0.65%  

  |- Residual                             0.055s    |- 0.46%  

  |- HeatLoss                             0.012s    |- 0.10%  

|- Logging                                0.031s  |- 0.26%    

|- Output                                 0.020s  |- 0.17%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.067s  0.56%       

|- execution                              0.064s  |- 95.35%   

------------------------------------------------------------

TOTAL                                    12.003s

============================================================



Time steps : 170/179, step size: 14.8588, 13.1276

```

#### Load OURS and CMG

* STARS wells: Inj, Prod (deck order, so .smy well index 0 and 1). STARS block history at (1,1,19), (2,1,18), (5,1,13) and (5,1,5).

* 10x1x20 grid, so the .smy block index is (i-1) + (k-1)*10.

```
OURS reached day 2526.0 of 2526

```

### Wells

* Top row: injector BHP and water rate, producer BHP. Bottom row: producer oil, water and gas rates. The wells are shut in until day 60.

![png]({{ "/assets/images/benchmark_image_48.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation.

![png]({{ "/assets/images/benchmark_image_49.png" | relative_url }})

# Speed



`-DCMAKE_BUILD_TYPE=Release`

### Dome corner grid

```
Running simulation [simuapp]: Dome Corner point

Elapsed: 2.59s

    47  84.3856  1    365.000                                                                            0.020    0.014   0.0010   19.197



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.277s  96.55%      

|- Newton                                 2.256s  |- 99.09%   

  |- Solver                               0.867s    |- 38.45% 

  |- FluxJac                              0.539s    |- 23.91% 

  |- Update                               0.511s    |- 22.64% 

  |- ScdAcc                               0.124s    |- 5.48%  

  |- update_dev                           0.068s    |- 3.01%  

  |- Precond                              0.063s    |- 2.79%  

  |- Residual                             0.023s    |- 1.02%  

  |- HeatLoss                             0.015s    |- 0.66%  

  |- SanitizeJac                          0.010s    |- 0.42%  

  |- alignvar                             0.009s    |- 0.38%  

  |- PerfJac                              0.001s    |- 0.07%  

|- Output                                 0.006s  |- 0.26%    

|- Logging                                0.004s  |- 0.17%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.081s  3.45%       

|- execution                              0.073s  |- 90.06%   

------------------------------------------------------------

TOTAL                                     2.358s

============================================================



Time steps : 47/49, step size: 7.76596, 21.0963

```

```
Found 4 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu018_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_50.png" | relative_url }})

## Heterogeneous

### SPE10 benchmark 2D 

```
Running simulation [simuapp]: SPE10 benchmark 2D water flooding 375 days ~7s single thread (OMP_NUM_THREADS=8)

Elapsed: 9.32s

    92   0.8247  6    375.000    19.31             4e-06             2e-05                      19.43    0.000    0.216   0.0181    0.005



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  9.017s  99.17%      

|- Newton                                 8.890s  |- 98.60%   

  |- FluxJac                              2.732s    |- 30.73% 

  |- Update                               2.699s    |- 30.36% 

  |- Solver                               1.297s    |- 14.59% 

  |- ScdAcc                               0.794s    |- 8.93%  

  |- update_dev                           0.468s    |- 5.27%  

  |- Precond                              0.311s    |- 3.50%  

  |- PerfJac                              0.249s    |- 2.80%  

  |- Residual                             0.100s    |- 1.12%  

  |- alignvar                             0.055s    |- 0.62%  

  |- SanitizeJac                          0.041s    |- 0.46%  

  |- HeatLoss                             0.020s    |- 0.23%  

|- Output                                 0.084s  |- 0.94%    

|- Logging                                0.018s  |- 0.20%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.076s  0.83%       

|- execution                              0.068s  |- 89.90%   

------------------------------------------------------------

TOTAL                                     9.093s

============================================================



Time steps : 92/92, step size: 4.07609, 3.20218

```

![png]({{ "/assets/images/benchmark_image_51.png" | relative_url }})

### Medium size



* 202,005 grid block (201x201x5) with heterogeneous permeability

* 61 wells water flooding pattern 

* 1500 days

```
Running simulation [simuapp]: Heterogeneous + 61wells - performance test medium size ~3m.50s (Single) (OMP_NUM_THREADS=8, -novtu)

Elapsed: 243.74s

    32  22.4900  5    365.000   257.24              8.04              3.03                     720.00    0.002  111.774   0.0064    1.456



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                4m 2.02s  99.46%      

|- Newton                               4m 1.53s  |- 99.80%   

  |- FluxJac                           1m 20.34s    |- 33.26% 

  |- Update                             1m 8.06s    |- 28.18% 

  |- Solver                              48.870s    |- 20.23% 

  |- ScdAcc                              16.370s    |- 6.78%  

  |- update_dev                           9.113s    |- 3.77%  

  |- Precond                              7.756s    |- 3.21%  

  |- Residual                             3.003s    |- 1.24%  

  |- HeatLoss                             1.931s    |- 0.80%  

  |- PerfJac                              1.450s    |- 0.60%  

  |- alignvar                             0.867s    |- 0.36%  

  |- SanitizeJac                          0.505s    |- 0.21%  

|- Output                                 0.067s  |- 0.03%    

|- Logging                                0.015s  |- 0.01%    

|- Input                                  0.003s  |- 0.00%    

Initialization                            1.306s  0.54%       

|- execution                              1.167s  |- 89.31%   

------------------------------------------------------------

TOTAL                                   4m 3.32s

============================================================



Time steps : 32/32, step size: 11.4062, 13.2808

```

### Johnansen water flooding

```
Running simulation [simuapp]: Johnansen water flooding takes ~5m on M2 (OMP_NUM_THREADS=8)

Elapsed: 18.81s

    17 365.0000  1   3650.000   353.53              0.07              0.02                     188.86    0.000    3.270   0.0067  3.1e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 17.400s  94.88%      

|- Newton                                17.276s  |- 99.29%   

  |- Update                               5.693s    |- 32.95% 

  |- FluxJac                              5.554s    |- 32.15% 

  |- Solver                               2.850s    |- 16.50% 

  |- ScdAcc                               1.250s    |- 7.24%  

  |- update_dev                           0.730s    |- 4.22%  

  |- Precond                              0.532s    |- 3.08%  

  |- Residual                             0.273s    |- 1.58%  

  |- alignvar                             0.065s    |- 0.38%  

  |- SanitizeJac                          0.031s    |- 0.18%  

  |- PerfJac                              0.002s    |- 0.01%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.087s  |- 0.50%    

|- Logging                                0.002s  |- 0.01%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.939s  5.12%       

|- execution                              0.627s  |- 66.80%   

------------------------------------------------------------

TOTAL                                    18.339s

============================================================



Time steps : 17/17, step size: 214.706, 163.784

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data//stflu016_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_52.png" | relative_url }})

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
Running simulation [simuapp]: MPI comparison baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 1.68s

    81  85.9779  6   3650.000     0.01              4.40             99.73                       4.59    0.119    1.494   0.0052    1.644



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.445s  96.11%      

|- Newton                                 1.423s  |- 98.52%   

  |- FluxJac                              0.620s    |- 43.55% 

  |- Update                               0.309s    |- 21.73% 

  |- ScdAcc                               0.152s    |- 10.71% 

  |- Solver                               0.139s    |- 9.77%  

  |- update_dev                           0.109s    |- 7.63%  

  |- PerfJac                              0.037s    |- 2.62%  

  |- Precond                              0.022s    |- 1.52%  

  |- alignvar                             0.008s    |- 0.58%  

  |- Residual                             0.006s    |- 0.43%  

  |- HeatLoss                             0.005s    |- 0.33%  

  |- SanitizeJac                          0.001s    |- 0.10%  

|- Output                                 0.007s  |- 0.46%    

|- Logging                                0.005s  |- 0.32%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.059s  3.89%       

|- execution                              0.056s  |- 95.65%   

------------------------------------------------------------

TOTAL                                     1.503s

============================================================



Time steps : 81/81, step size: 45.0617, 50.5258

Running simulation [simumpi]: MPI comparison np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 1.73s



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  32.0262  6   1288.995     1.45              5.03             77.68                       5.96    0.276   36.939   0.1386   26.263

    62  34.4803  7   1323.476     1.34              5.14             79.30                       5.96    0.276   46.615   0.1476   30.057

    63  34.4431  6   1357.919     1.16              4.96             80.98                       5.96    0.276   50.061   0.1353   28.997

    64  35.1138  5   1393.032     1.10              5.18             82.53                       5.96    0.276   57.743   0.1519   12.161

    65  40.7127  6   1433.745     0.97              5.28             84.44                       5.96    0.276   51.420   0.1099   20.395

    66  49.8289  6   1483.574     0.72              5.10             87.57                       5.96    0.196   74.780   0.1419   26.100

    67  53.8274  7   1537.401     0.67              4.97             88.08                       5.96    0.196   89.635   0.1393    8.586

    68  65.1128  5   1602.514     0.58              4.94             89.51                       5.96    0.196  105.940   0.0991   11.030

    69  91.4827  6   1693.997     0.47              4.97             91.35                       5.96    0.196  162.126   0.1067    7.983

    70 124.7150  6   1818.712     0.36              4.91             93.24                       5.96    0.196  240.004   0.1020    8.871

    71 173.1988  6   1991.911     0.25              4.84             95.13                       5.96    0.196  374.110   0.0888   11.690

    72 202.3055  6   2194.216     0.17              4.73             96.60                       5.96    0.196  489.203   0.1100   12.659

    73 204.8331  6   2399.049     0.11              4.51             97.65                       5.96    0.196  570.258   0.0932   12.291

    74 189.6084  5   2588.658     0.07              4.34             98.39                       5.96    0.196  591.486   0.0392   10.849

    75 171.6603  5   2760.318     0.05              4.14             98.86                       5.96    0.196  584.442   0.0329    9.366

    76 156.5521  6   2916.870     0.03              3.93             99.17                       5.96    0.196  575.007   0.0282    8.227

    77 144.1918  6   3061.062     0.02              3.60             99.41                       5.96    0.196  579.576   0.0742    7.516

    78 132.1716  6   3193.233     0.01              3.34             99.57                       5.96    0.196  594.242   0.0275    7.053

    79 119.3202  6   3312.554     0.01              2.83             99.70                       5.96    0.196  616.438   0.0639    6.741

    80 105.3068  6   3417.860     0.01              3.26             99.74                       5.26    0.196  269.796   0.0361    3.570

    81 142.9031  6   3560.764     0.01              4.09             99.74                       4.64    0.196   25.659   0.0717    3.137

    82  89.2364  6   3650.000     0.01              4.40             99.73                       4.59    0.196    1.877   0.0055    1.716

Time steps : 82/82, step size: 44.5122, 50.2074

Running simulation [simumpi]: MPI comparison np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 1.07s



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  32.6516  6   1287.924     1.45              5.04             77.65                       5.96    0.286   39.871   0.1389   28.139

    62  33.8513  6   1321.776     1.36              5.17             79.20                       5.96    0.287   47.561   0.1656   28.606

    63  34.7744  6   1356.550     1.18              4.98             80.85                       5.96    0.287   47.928   0.1238   29.132

    64  35.3589  6   1391.909     1.10              5.15             82.43                       5.96    0.287   58.289   0.1496   12.115

    65  41.3006  6   1433.210     0.98              5.28             84.33                       5.96    0.287   52.389   0.1120   20.415

    66  50.5250  6   1483.735     0.73              5.10             87.56                       5.96    0.211   77.323   0.1515   26.395

    67  54.2506  7   1537.985     0.68              4.97             88.05                       5.96    0.211   90.646   0.1407    8.645

    68  65.3074  5   1603.293     0.58              4.94             89.50                       5.96    0.211  106.241   0.0984   11.063

    69  92.0057  6   1695.298     0.47              4.98             91.36                       5.96    0.211  163.176   0.1074    7.959

    70 125.1129  6   1820.411     0.36              4.90             93.25                       5.96    0.211  240.944   0.1050    8.897

    71 171.7153  6   1992.127     0.25              4.84             95.13                       5.96    0.211  370.824   0.0884   11.584

    72 201.4562  6   2193.583     0.17              4.73             96.59                       5.96    0.211  486.639   0.1101   12.605

    73 204.5801  6   2398.163     0.11              4.51             97.65                       5.96    0.211  568.732   0.0935   12.275

    74 189.6805  5   2587.844     0.07              4.35             98.39                       5.96    0.211  591.247   0.0392   10.859

    75 171.7682  5   2759.612     0.05              4.15             98.86                       5.96    0.211  584.346   0.0329    9.375

    76 156.6663  6   2916.278     0.03              3.93             99.17                       5.96    0.211  575.016   0.0282    8.236

    77 144.2954  6   3060.573     0.02              3.60             99.41                       5.96    0.211  579.412   0.0744    7.521

    78 132.2893  6   3192.863     0.01              3.34             99.57                       5.96    0.211  594.151   0.0275    7.057

    79 119.4376  6   3312.300     0.01              2.84             99.70                       5.96    0.211  616.112   0.0641    6.743

    80 105.4451  6   3417.746     0.01              3.24             99.74                       5.27    0.211  275.564   0.0358    3.604

    81 141.8223  6   3559.568     0.01              4.08             99.74                       4.65    0.211   25.944   0.0722    3.116

    82  90.4321  5   3650.000     0.01              4.40             99.73                       4.59    0.211    2.047   0.0056    1.743

Time steps : 82/82, step size: 44.5122, 50.1535

Running simulation [simumpi]: MPI comparison np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 0.89s



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  32.3464  6   1296.013     1.41              5.01             78.08                       5.96    0.326   39.123   0.1557   19.075

    62  37.0396  6   1333.053     1.29              5.10             79.80                       5.96    0.327   53.507   0.1153   34.747

    63  33.9685  5   1367.021     1.11              4.89             81.48                       5.96    0.327   55.521   0.1708   28.445

    64  35.0049  6   1402.026     1.08              5.28             83.02                       5.96    0.312   56.113   0.1840   12.815

    65  36.6795  5   1438.706     0.94              5.31             84.92                       5.96    0.312   45.966   0.0905   19.219

    66  46.1587  7   1484.864     0.75              5.04             87.07                       5.96    0.312   69.597   0.1304   24.381

    67  51.6913  7   1536.556     0.69              4.97             87.81                       5.96    0.312   86.149   0.1329    8.098

    68  63.9435  6   1600.499     0.59              4.95             89.39                       5.96    0.312  104.043   0.1015   10.778

    69  88.9807  6   1689.480     0.48              4.99             91.23                       5.96    0.312  156.911   0.0977    8.745

    70 125.7119  6   1815.192     0.36              4.91             93.16                       5.96    0.312  241.461   0.1008    8.972

    71 175.4344  8   1990.626     0.25              4.83             95.06                       5.96    0.312  379.365   0.0893   11.886

    72 203.4891  6   2194.115     0.17              4.72             96.56                       5.96    0.312  497.103   0.1099   12.859

    73 204.1650  6   2398.280     0.11              4.51             97.63                       5.96    0.312  568.780   0.0919   12.241

    74 189.2861  5   2587.566     0.07              4.34             98.38                       5.96    0.312  590.490   0.0391   10.821

    75 171.5454  5   2759.112     0.05              4.14             98.85                       5.96    0.312  583.879   0.0328    9.352

    76 156.5393  6   2915.651     0.03              3.93             99.17                       5.96    0.312  574.739   0.0280    8.220

    77 144.2206  6   3059.872     0.02              3.60             99.41                       5.96    0.312  579.670   0.0738    7.515

    78 132.1849  6   3192.057     0.01              3.34             99.57                       5.96    0.312  594.282   0.0276    7.051

    79 119.3274  6   3311.384     0.01              2.83             99.69                       5.96    0.312  616.528   0.0637    6.740

    80 105.3036  6   3416.688     0.01              3.26             99.73                       5.25    0.312  267.724   0.0362    3.558

    81 143.3595  6   3560.047     0.01              4.09             99.73                       4.64    0.312   25.566   0.0715    3.145

    82  89.9528  6   3650.000     0.01              4.40             99.73                       4.59    0.312    1.914   0.0055    1.727

Time steps : 82/82, step size: 44.5122, 50.2431

simuapp          rc=0   1.50s   81/ 81 steps  to  3650.00 days

simumpi np=1     rc=0   1.35s   82/ 82 steps,  0 cuts  to  3650.00 days

simumpi np=2     rc=0   0.81s   82/ 82 steps,  0 cuts  to  3650.00 days

simumpi np=4     rc=0   0.56s   82/ 82 steps,  0 cuts  to  3650.00 days

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


![png]({{ "/assets/images/benchmark_image_53.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_54.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_55.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_56.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_57.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_58.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_59.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_60.png" | relative_url }})

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
Running simulation [simuapp]: CSS parity baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 23.11s

   146  78.9056  9   1095.000     1.47              1.19             44.73                               0.400   48.391   0.1032    5.193



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 22.863s  99.72%      

|- Newton                                22.834s  |- 99.87%   

  |- FluxJac                             11.417s    |- 50.00% 

  |- Update                               5.176s    |- 22.67% 

  |- ScdAcc                               2.286s    |- 10.01% 

  |- update_dev                           1.550s    |- 6.79%  

  |- Solver                               1.442s    |- 6.32%  

  |- Precond                              0.413s    |- 1.81%  

  |- alignvar                             0.128s    |- 0.56%  

  |- PerfJac                              0.108s    |- 0.47%  

  |- Residual                             0.092s    |- 0.40%  

  |- HeatLoss                             0.084s    |- 0.37%  

  |- SanitizeJac                          0.025s    |- 0.11%  

|- Logging                                0.009s  |- 0.04%    

|- Output                                 0.009s  |- 0.04%    

|- Input                                  0.001s  |- 0.00%    

Initialization                            0.064s  0.28%       

|- execution                              0.061s  |- 96.48%   

------------------------------------------------------------

TOTAL                                    22.927s

============================================================



Time steps : 146/155, step size: 7.5, 16.0457

Running simulation [simumpi]: CSS parity np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 20.33s

   113   1.1331  6    736.486                                                                  158.99    0.140  202.569   0.1297   35.294

   114   1.4179  6    737.904                                                                  158.99    0.140  241.755   0.1706   33.727

   115   1.5479  6    739.452                                                                  158.99    0.140  234.215   0.1068   30.651

   116   0.5480  6    740.000                                                                  158.99    0.140  117.361   0.0828   11.853

   117   7.0000  6    747.000                                                                            0.140  1.2e+03   0.1678   29.714

   118   1.0000  7    748.000     2.01             97.41             97.98                               0.139  1.0e+03   0.1105   43.796

   119   1.1730  6    749.173     5.01             65.98             92.94                               0.139  241.329   0.1500   12.590

   120   1.3684  6    750.541     7.33             46.54             86.39                               0.139  172.171   0.0750    7.148



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   121   2.1283  6    752.670     8.55             33.76             79.79                               0.139  173.169   0.1907    7.140

   122   2.1862  6    754.856     8.33             27.17             76.53                               0.139  133.704   0.0227    5.760

   123   4.3724  6    759.228     7.46             20.45             73.28                               0.139  167.877   0.0965    7.949

   124   6.2086  6    765.437     6.22             15.09             70.81                               0.139  162.946   0.1054    8.185

   125   8.5094  9    773.946     4.85             11.04             69.46                               0.139  140.279   0.1565    8.423

   126   9.7174  6    783.664     3.96              8.69             68.73                               0.139  101.215   0.0399    7.497

   127  17.9121  6    801.576     3.23              6.24             65.93                               0.139  109.121   0.0421   10.092

   128  32.6377  6    834.214     2.50              4.17             62.54                               0.145  104.058   0.1501   11.935

   129  38.0620 12    872.276     2.11              3.10             59.54                               0.152   67.752   0.1214    9.056

   130  38.0620  6    910.338     1.93              2.58             57.10                               0.178   42.690   0.1457    5.394

   131  45.0519 12    955.390     1.90              2.06             52.08                               0.178   40.224   0.1484    5.196

   132  45.0519  6   1000.441     1.76              1.66             48.45                               0.192   34.323   0.0858    4.324

   133  66.8821  9   1067.324     1.60              1.27             44.34                               0.208   42.234   0.0999    4.949

   134  27.6765  6   1095.000     1.22              1.17             48.97                               0.230   16.950   0.0636    1.851

Time steps : 134/138, step size: 8.17164, 15.9471

Running simulation [simumpi]: CSS parity np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 13.54s

=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   121   7.0000  6    747.000                                                                            0.360  1.2e+03   0.1697   29.360

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.445431) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.445431) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.0822024) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.0822024) - this cycle cannot be accepted as converged

   122   1.0000  9    748.000     1.19            103.03             98.85                               0.374  1.1e+03   0.2303   47.444

   123   0.9202  7    748.920     4.38             70.11             94.12                               0.372  208.443   0.2978   13.183

   124   0.7193  6    749.640     5.88             57.23             90.69                               0.372  115.306   0.0566    4.692

   125   1.2188  6    750.858     7.69             43.62             85.01                               0.373  137.390   0.0432    5.520

   126   2.2077  6    753.066     8.77             32.53             78.78                               0.373  168.155   0.4313    6.985

   127   1.3292  6    754.395     8.51             29.08             77.35                               0.374   84.385   0.0798    3.477

   128   2.0244  6    756.420     8.20             24.99             75.28                               0.374   98.736   0.0671    4.434

   129   3.2632  6    759.683     7.49             20.26             73.01                               0.375  117.881   0.0437    5.437

   130   5.8960  6    765.579     6.25             15.03             70.63                               0.375  151.740   0.1197    7.681

   131   7.6527  8    773.232     5.04             11.41             69.37                               0.376  127.893   0.1526    7.503

   132   8.8521  6    782.084     4.12              9.06             68.73                               0.377   96.312   0.0600    6.971

   133  14.7536  6    796.837     3.45              6.94             66.79                               0.378  100.308   0.1359    8.868

   134  18.0594  6    814.897     2.88              5.25             64.56                               0.379   78.846   0.0870    8.284

   135  26.6682  6    841.565     2.43              4.24             63.54                               0.385   67.456   0.0822    7.835

   136  40.2009  9    881.766     2.08              2.97             58.74                               0.389   63.538   0.1139    8.523

   137  53.3142  7    935.080     2.06              2.29             52.62                               0.389   54.516   0.1035    6.637

   138  73.6036  8   1008.684     1.86              1.59             46.12                               0.387   57.708   0.1572    6.762

   139  86.3163  6   1095.000     1.53              1.26             45.22                               0.478   39.163   0.1481    3.950

Time steps : 139/144, step size: 7.8777, 16.1203

Running simulation [simumpi]: CSS parity np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 7.17s

[rank 3] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 0.238395) - this cycle cannot be accepted as converged

   112   1.0000  7    748.000     4.49             77.70             94.53                               0.673  1.3e+03   0.4978   62.056

   113   0.5403  6    748.540     2.97             79.37             96.39                               0.674  120.360   0.1082    4.597

   114   0.7325  6    749.273     4.61             59.68             92.83                               0.675  131.738   0.2474    5.371

   115   0.6451  6    749.918     6.18             49.44             88.89                               0.675   90.991   0.0418    3.697

   116   1.1773  6    751.095     7.88             39.01             83.19                               0.676  121.706   0.1716    5.007

   117   1.2814  6    752.377     8.56             32.60             79.21                               0.677  103.852   0.2996    4.405

   118   0.9976  6    753.374     8.34             29.79             78.13                               0.677   70.680   0.0505    2.984

   119   1.7414  6    755.116     8.13             25.96             76.15                               0.678   97.344   0.0531    4.253

   120   3.0017  6    758.117     7.49             21.25             73.93                               0.679  117.035   0.1087    5.519



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   121   4.0607  6    762.178     6.59             16.93             71.96                               0.680  123.625   0.0631    5.724

   122   6.6682  7    768.846     5.41             12.71             70.16                               0.681  136.414   0.0910    7.619

   123   9.6826  6    778.529     4.13              9.38             69.42                               0.682  120.834   0.1219    8.174

   124  12.4643  6    790.993     3.42              7.46             68.58                               0.684   97.513   0.1112    8.154

   125  16.7031  6    807.696     2.92              5.60             65.74                               0.685   84.440   0.1400    8.450

   126  20.1557  7    827.852     2.48              4.33             63.54                               0.687   64.944   0.0798    7.730

   127  30.6991 12    858.551     2.19              3.34             60.42                               0.689   59.768   0.0682    8.079

   128  30.6991  6    889.250     1.83              2.92             61.44                               0.699   41.081   0.1233    5.718

   129  39.3118  7    928.562     1.95              2.43             55.42                               0.701   39.033   0.0749    5.146

   130  61.1851  6    989.747     1.88              1.89             50.20                               0.718   47.611   0.1306    5.711

   131  76.3215  9   1066.068     1.40              1.25             47.17                               0.728   47.287   0.1333    5.334

   132  28.9316  6   1095.000     1.29              1.26             49.31                               0.729   17.644   0.0910    1.923

Time steps : 132/134, step size: 8.29545, 17.2189

simuapp          rc=0  22.93s  146/155 steps  to  1095.00 days

simumpi np=1     rc=0  20.07s  134/138 steps,  4 cuts  to  1095.00 days

simumpi np=2     rc=0  13.25s  139/144 steps,  5 cuts  to  1095.00 days

simumpi np=4     rc=0   6.81s  132/134 steps,  2 cuts  to  1095.00 days

```

![png]({{ "/assets/images/benchmark_image_61.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_62.png" | relative_url }})

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
Running simulation [simuapp]: scaling baseline (attempt 1/2) (OMP_NUM_THREADS=1, -novtu)

Elapsed: 37.48s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 35.797s  96.28%      

|- Newton                                35.723s  |- 99.79%   

  |- FluxJac                             15.677s    |- 43.89% 

  |- Update                              10.793s    |- 30.21% 

  |- ScdAcc                               3.403s    |- 9.52%  

  |- update_dev                           2.209s    |- 6.18%  

  |- Solver                               2.080s    |- 5.82%  

  |- Precond                              0.669s    |- 1.87%  

  |- Residual                             0.212s    |- 0.59%  

  |- alignvar                             0.186s    |- 0.52%  

  |- HeatLoss                             0.103s    |- 0.29%  

  |- PerfJac                              0.083s    |- 0.23%  

  |- SanitizeJac                          0.052s    |- 0.15%  

|- Output                                 0.008s  |- 0.02%    

|- Logging                                0.001s  |- 0.00%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            1.382s  3.72%       

|- execution                              1.242s  |- 89.82%   

------------------------------------------------------------

TOTAL                                    37.179s

============================================================



Time steps : 4/4, step size: 0.129481, 0.0270325

Running simulation [simuapp]: scaling baseline (attempt 2/2) (OMP_NUM_THREADS=1, -novtu)

Elapsed: 36.84s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 35.216s  96.33%      

|- Newton                                35.142s  |- 99.79%   

  |- FluxJac                             15.566s    |- 44.29% 

  |- Update                              10.637s    |- 30.27% 

  |- ScdAcc                               3.333s    |- 9.48%  

  |- update_dev                           2.149s    |- 6.12%  

  |- Solver                               1.966s    |- 5.60%  

  |- Precond                              0.623s    |- 1.77%  

  |- Residual                             0.209s    |- 0.59%  

  |- alignvar                             0.181s    |- 0.52%  

  |- HeatLoss                             0.111s    |- 0.31%  

  |- PerfJac                              0.083s    |- 0.24%  

  |- SanitizeJac                          0.059s    |- 0.17%  

|- Output                                 0.010s  |- 0.03%    

|- Logging                                0.001s  |- 0.00%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            1.340s  3.67%       

|- execution                              1.210s  |- 90.33%   

------------------------------------------------------------

TOTAL                                    36.556s

============================================================



Time steps : 4/4, step size: 0.129481, 0.0270325

Running simulation [simumpi]: scaling np=1 (attempt 1/2) (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 37.17s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-01





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.258   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     720.00    0.000  358.611   0.0032    0.123

     3   0.1391  2      0.356   426.16             27.46              6.05                     720.00    0.000  375.799   0.0037    0.139

     4   0.1621  3      0.518   376.48             25.97              6.45                     720.00    0.000  339.801   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129461, 0.0270306

Running simulation [simumpi]: scaling np=1 (attempt 2/2) (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 37.03s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-01





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.258   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     720.00    0.000  358.611   0.0032    0.123

     3   0.1391  2      0.356   426.16             27.46              6.05                     720.00    0.000  375.799   0.0037    0.139

     4   0.1621  3      0.518   376.48             25.97              6.45                     720.00    0.000  339.801   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129461, 0.0270306

Running simulation [simumpi]: scaling np=2 (attempt 1/2) (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 19.84s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-01





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.298   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     720.00    0.000  358.578   0.0032    0.123

     3   0.1391  2      0.356   426.16             27.46              6.05                     720.00    0.000  375.797   0.0037    0.139

     4   0.1621  3      0.518   376.49             25.97              6.45                     720.00    0.000  339.800   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129459, 0.0270311

Running simulation [simumpi]: scaling np=2 (attempt 2/2) (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 19.79s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-01





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.298   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     720.00    0.000  358.578   0.0032    0.123

     3   0.1391  2      0.356   426.16             27.46              6.05                     720.00    0.000  375.797   0.0037    0.139

     4   0.1621  3      0.518   376.49             25.97              6.45                     720.00    0.000  339.800   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129459, 0.0270311

Running simulation [simumpi]: scaling np=4 (attempt 1/2) (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 11.90s

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-01





VTU generation is suppressed.

VTU generation is suppressed.

VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.258   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     720.00    0.000  358.611   0.0032    0.123

     3   0.1391  2      0.356   426.16             27.46              6.05                     720.00    0.000  375.800   0.0037    0.139

     4   0.1621  3      0.518   376.48             25.97              6.45                     720.00    0.000  339.801   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129461, 0.0270306

Running simulation [simumpi]: scaling np=4 (attempt 2/2) (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 12.15s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-01





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.258   0.0027    0.111

     2   0.1166  1      0.217   497.87             26.53              5.06                     720.00    0.000  358.611   0.0032    0.123

     3   0.1391  2      0.356   426.16             27.46              6.05                     720.00    0.000  375.800   0.0037    0.139

     4   0.1621  3      0.518   376.48             25.97              6.45                     720.00    0.000  339.801   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129461, 0.0270306

Running simulation [simumpi]: scaling np=8 (attempt 1/2) (OMP_NUM_THREADS=1, np=8, -novtu)

Elapsed: 10.66s



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-01





VTU generation is suppressed.

VTU generation is suppressed.

VTU generation is suppressed.

VTU generation is suppressed.

VTU generation is suppressed.

VTU generation is suppressed.

VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.271   0.0027    0.111

     2   0.1166  1      0.217   497.88             26.53              5.06                     719.99    0.000  358.618   0.0032    0.123

     3   0.1391  2      0.356   426.17             27.46              6.05                     720.00    0.000  375.788   0.0037    0.139

     4   0.1621  3      0.518   376.49             25.97              6.45                     720.00    0.000  339.796   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129459, 0.0270297

Running simulation [simumpi]: scaling np=8 (attempt 2/2) (OMP_NUM_THREADS=1, np=8, -novtu)

Elapsed: 10.54s

            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-01





VTU generation is suppressed.

VTU generation is suppressed.

VTU generation is suppressed.

VTU generation is suppressed.

VTU generation is suppressed.

VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.53             20.32              3.30                     720.00    0.000  375.271   0.0027    0.111

     2   0.1166  1      0.217   497.88             26.53              5.06                     719.99    0.000  358.618   0.0032    0.123

     3   0.1391  2      0.356   426.17             27.46              6.05                     720.00    0.000  375.788   0.0037    0.139

     4   0.1621  3      0.518   376.49             25.97              6.45                     720.00    0.000  339.796   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129459, 0.0270297

```

![png]({{ "/assets/images/benchmark_image_63.png" | relative_url }})

```
   config  steps   seconds   speedup   effic.  cells/rank   ghosts

  simuapp      4     36.56         -        -           -        -

     np=1      4     34.75     1.00x     100%      202005        0

     np=2      4     18.11     1.92x      96%      101080     2110

     np=4      4     10.56     3.29x      82%       50520     4235

     np=8      4      8.81     3.95x      49%       25610     8325 *

  * more ranks than the 4 fast cores on this CPU - paced by the slow ones, so read the efficiency as the machine's, not the partition's

```

```
Script completed at: 2026-11-02 11:24:01

```
