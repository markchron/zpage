---
layout: default
title: "Benchmark results of resrsim"
date: 2026-11-21
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

Timeloop                                  0.226s  62.96%      

|- Newton                                 0.204s  |- 90.11%   

  |- Update                               0.077s    |- 37.59% 

  |- FluxJac                              0.049s    |- 24.29% 

  |- ScdAcc                               0.026s    |- 12.59% 

  |- Solver                               0.016s    |- 7.64%  

  |- update_dev                           0.010s    |- 4.97%  

  |- Precond                              0.010s    |- 4.84%  

  |- Residual                             0.005s    |- 2.61%  

  |- SanitizeJac                          0.002s    |- 0.95%  

  |- alignvar                             0.001s    |- 0.69%  

  |- PerfJac                              0.001s    |- 0.65%  

  |- HeatLoss                             0.001s    |- 0.33%  

|- Output                                 0.012s  |- 5.45%    

|- Logging                                0.001s  |- 0.30%    

|- Input                                  0.000s  |- 0.05%    

Initialization                            0.133s  37.04%      

|- execution                              0.123s  |- 92.30%   

------------------------------------------------------------

TOTAL                                     0.359s

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

Elapsed: 1.01s

    79  76.8632  5   3650.000     0.01              4.41             99.73                       4.59    0.044    0.560   0.0041    1.440



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.797s  93.43%      

|- Newton                                 0.779s  |- 97.67%   

  |- Update                               0.232s    |- 29.77% 

  |- FluxJac                              0.203s    |- 26.03% 

  |- ScdAcc                               0.077s    |- 9.85%  

  |- Precond                              0.073s    |- 9.42%  

  |- update_dev                           0.047s    |- 5.99%  

  |- Solver                               0.040s    |- 5.17%  

  |- PerfJac                              0.037s    |- 4.77%  

  |- SanitizeJac                          0.022s    |- 2.78%  

  |- alignvar                             0.014s    |- 1.83%  

  |- Residual                             0.009s    |- 1.16%  

  |- HeatLoss                             0.006s    |- 0.83%  

|- Output                                 0.007s  |- 0.83%    

|- Logging                                0.005s  |- 0.68%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.056s  6.57%       

|- execution                              0.053s  |- 95.20%   

------------------------------------------------------------

TOTAL                                     0.853s

============================================================



Time steps : 79/79, step size: 46.2025, 50.7314

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

Elapsed: 0.69s

    36 193.7837  6   3650.000     0.05              3.00             98.40                       5.84    0.197  483.732   0.0600    7.763



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.461s  88.16%      

|- Newton                                 0.452s  |- 98.00%   

  |- Update                               0.137s    |- 30.23% 

  |- FluxJac                              0.111s    |- 24.62% 

  |- Precond                              0.045s    |- 9.90%  

  |- ScdAcc                               0.043s    |- 9.59%  

  |- Solver                               0.027s    |- 5.97%  

  |- update_dev                           0.025s    |- 5.52%  

  |- PerfJac                              0.021s    |- 4.66%  

  |- SanitizeJac                          0.013s    |- 2.88%  

  |- alignvar                             0.009s    |- 1.92%  

  |- Residual                             0.005s    |- 1.13%  

  |- HeatLoss                             0.004s    |- 0.88%  

|- Logging                                0.004s  |- 0.93%    

|- Output                                 0.003s  |- 0.65%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.062s  11.84%      

|- execution                              0.059s  |- 94.97%   

------------------------------------------------------------

TOTAL                                     0.523s

============================================================



Time steps : 36/38, step size: 101.389, 106.145

```

![png]({{ "/assets/images/benchmark_image_6.png" | relative_url }})

# Buckley- Leverett



Two phase, isothermal problem

variable order: [Sw, P, T, So, X0, X1, Sg]



Acc w.r.t. [Sw, So, Sg, X0, X1, P, T]

```
Running simulation [simuapp]: Buckley-Leverett (-novtu)

Elapsed: 0.78s

    79   4.9496  1     10.000    5e-10              0.16            100.00                       0.16   13.643    0.005 7.13e-06  3.9e-07



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.538s  88.91%      

|- Newton                                 0.528s  |- 98.08%   

  |- Update                               0.185s    |- 35.04% 

  |- FluxJac                              0.079s    |- 14.93% 

  |- ScdAcc                               0.064s    |- 12.12% 

  |- Precond                              0.061s    |- 11.54% 

  |- update_dev                           0.032s    |- 6.13%  

  |- PerfJac                              0.029s    |- 5.45%  

  |- SanitizeJac                          0.019s    |- 3.58%  

  |- Solver                               0.013s    |- 2.51%  

  |- alignvar                             0.013s    |- 2.45%  

  |- HeatLoss                             0.010s    |- 1.95%  

  |- Residual                             0.008s    |- 1.48%  

|- Logging                                0.005s  |- 0.91%    

|- Output                                 0.003s  |- 0.61%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.067s  11.09%      

|- execution                              0.063s  |- 94.22%   

------------------------------------------------------------

TOTAL                                     0.606s

============================================================



Time steps : 79/81, step size: 0.126582, 0.647044

```

### Load Benchmark

### Buckley Plot

![png]({{ "/assets/images/benchmark_image_7.png" | relative_url }})

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

Elapsed: 0.80s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.577s  90.84%      

|- Newton                                 0.561s  |- 97.28%   

  |- Update                               0.235s    |- 41.88% 

  |- FluxJac                              0.111s    |- 19.70% 

  |- ScdAcc                               0.068s    |- 12.13% 

  |- update_dev                           0.038s    |- 6.82%  

  |- Precond                              0.033s    |- 5.88%  

  |- HeatLoss                             0.016s    |- 2.83%  

  |- Solver                               0.014s    |- 2.55%  

  |- Residual                             0.012s    |- 2.07%  

  |- PerfJac                              0.008s    |- 1.47%  

  |- SanitizeJac                          0.006s    |- 1.15%  

  |- alignvar                             0.006s    |- 0.99%  

|- Output                                 0.010s  |- 1.77%    

|- Logging                                0.002s  |- 0.28%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.058s  9.16%       

|- execution                              0.056s  |- 95.93%   

------------------------------------------------------------

TOTAL                                     0.635s

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

![png]({{ "/assets/images/benchmark_image_8.png" | relative_url }})

The relative error is largest, and concentrated right at the advancing front, for the snapshots

taken before the analytic breakthrough time (~13.8 days) - the expected signature of numerical

dispersion smearing Lauwerier's mathematically sharp step. Once every cell is past its own local

breakthrough (t >~ 32 days) the profile is governed by the smoother post-breakthrough erfc tail,

and the relative L2 error over the whole 804-cell row drops accordingly.

![png]({{ "/assets/images/benchmark_image_9.png" | relative_url }})

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

Elapsed: 0.26s

    17   1.4144  2     10.000                                                                 9521.20    0.053  152.652             1.045



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Initialization                            0.056s  56.00%      

|- execution                              0.054s  |- 96.04%   

Timeloop                                  0.044s  44.00%      

|- Newton                                 0.040s  |- 90.47%   

  |- Update                               0.013s    |- 32.30% 

  |- Precond                              0.006s    |- 15.39% 

  |- PerfJac                              0.005s    |- 12.36% 

  |- ScdAcc                               0.004s    |- 9.75%  

  |- FluxJac                              0.004s    |- 9.42%  

  |- update_dev                           0.002s    |- 5.99%  

  |- SanitizeJac                          0.002s    |- 5.73%  

  |- alignvar                             0.001s    |- 3.16%  

  |- Solver                               0.001s    |- 2.64%  

  |- Residual                             0.000s    |- 0.46%  

  |- HeatLoss                             0.000s    |- 0.02%  

|- Output                                 0.003s  |- 6.80%    

|- Logging                                0.001s  |- 1.67%    

|- Input                                  0.000s  |- 0.07%    

------------------------------------------------------------

TOTAL                                     0.100s

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

![png]({{ "/assets/images/benchmark_image_10.png" | relative_url }})

The mismatch is concentrated at the advancing front and shrinks as cells fully equilibrate - the

same numerical-dispersion signature as the Lauwerier comparison above, not a sign the two models

disagree on the front's speed. `avd_mdot` is the deck's design target (100 kg/s); the remaining

gap is plausibly the well's day-0-to-5.5 ramp from bottom-hole-pressure control up to the rate

target (the analytic solution assumes that full rate from t=0), compounded by this deck's coarse

15-block grid - only the first 3-4 blocks sit inside the thermal front by day 10.


![png]({{ "/assets/images/benchmark_image_11.png" | relative_url }})

# MISC

## spe04b_cw.dat

```
Running simulation [simuapp]: SPE4-b water flooding (-novtu)

Elapsed: 0.57s

    22 163.2234  2   3650.000     0.78             10.19             92.87                      10.73    0.000   13.707   0.0098    0.002



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.347s  84.54%      

|- Newton                                 0.343s  |- 98.74%   

  |- Update                               0.111s    |- 32.37% 

  |- FluxJac                              0.103s    |- 30.05% 

  |- Solver                               0.033s    |- 9.69%  

  |- ScdAcc                               0.032s    |- 9.19%  

  |- Precond                              0.023s    |- 6.73%  

  |- update_dev                           0.015s    |- 4.49%  

  |- PerfJac                              0.007s    |- 1.91%  

  |- SanitizeJac                          0.005s    |- 1.52%  

  |- Residual                             0.005s    |- 1.36%  

  |- alignvar                             0.004s    |- 1.15%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.001s  |- 0.37%    

|- Logging                                0.001s  |- 0.29%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.064s  15.46%      

|- execution                              0.061s  |- 96.40%   

------------------------------------------------------------

TOTAL                                     0.411s

============================================================



Time steps : 22/22, step size: 165.909, 155.033

```



## watfld_cw.dat

```
Running simulation [simuapp]: SPE4-b Water flooding without vmod (-novtu)

Elapsed: 0.75s

    35  32.2986  2   3650.000     1.04             79.00             98.70                      80.00    0.000    1.859   0.0028  3.1e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.533s  89.96%      

|- Newton                                 0.525s  |- 98.37%   

  |- Update                               0.168s    |- 32.11% 

  |- FluxJac                              0.151s    |- 28.70% 

  |- Solver                               0.054s    |- 10.25% 

  |- ScdAcc                               0.042s    |- 8.08%  

  |- Precond                              0.032s    |- 6.02%  

  |- PerfJac                              0.030s    |- 5.75%  

  |- update_dev                           0.021s    |- 3.96%  

  |- SanitizeJac                          0.008s    |- 1.45%  

  |- Residual                             0.007s    |- 1.26%  

  |- alignvar                             0.005s    |- 1.03%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.003s  |- 0.55%    

|- Logging                                0.001s  |- 0.27%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.060s  10.04%      

|- execution                              0.057s  |- 96.00%   

------------------------------------------------------------

TOTAL                                     0.593s

============================================================



Time steps : 35/35, step size: 104.286, 142.699

```

## stflu001.dat

Inverted 9 spot hot water flooding with area/block modifier, 5 point transmissibility


```
Running simulation [simuapp]: Inverted 9 spot hot water flooding (-novtu)

Elapsed: 1.07s

    95 281.6618  2   3650.000    5e-05            597.44            100.00                     597.44    0.486    0.077 9.13e-05    0.002



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.850s  93.65%      

|- Newton                                 0.836s  |- 98.41%   

  |- Update                               0.267s    |- 31.95% 

  |- FluxJac                              0.216s    |- 25.80% 

  |- Precond                              0.088s    |- 10.52% 

  |- ScdAcc                               0.084s    |- 9.99%  

  |- update_dev                           0.048s    |- 5.69%  

  |- Solver                               0.042s    |- 4.98%  

  |- SanitizeJac                          0.025s    |- 3.01%  

  |- alignvar                             0.017s    |- 2.05%  

  |- PerfJac                              0.016s    |- 1.89%  

  |- Residual                             0.010s    |- 1.18%  

  |- HeatLoss                             0.007s    |- 0.88%  

|- Output                                 0.007s  |- 0.85%    

|- Logging                                0.005s  |- 0.62%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.058s  6.35%       

|- execution                              0.055s  |- 95.74%   

------------------------------------------------------------

TOTAL                                     0.907s

============================================================



Time steps : 95/98, step size: 38.4211, 93.6796

```

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation, CMG against OURS.

![png]({{ "/assets/images/benchmark_image_12.png" | relative_url }})

## stflu002.dat

5000x5000x50, 2D diagonal water flooding in uniformed cartesian

```
Running simulation [simuapp]: Uniformed cartesian water flooding (-novtu)

Elapsed: 0.40s

    49 330.7333  5   3650.000   624.40             11.54              1.82                     635.95    0.000  1.1e+03   0.0498    0.028



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.182s  74.86%      

|- Newton                                 0.175s  |- 95.99%   

  |- Update                               0.061s    |- 34.73% 

  |- FluxJac                              0.035s    |- 20.06% 

  |- Precond                              0.018s    |- 10.22% 

  |- ScdAcc                               0.018s    |- 10.20% 

  |- update_dev                           0.009s    |- 4.88%  

  |- Solver                               0.008s    |- 4.63%  

  |- PerfJac                              0.008s    |- 4.42%  

  |- SanitizeJac                          0.006s    |- 3.18%  

  |- alignvar                             0.004s    |- 2.04%  

  |- HeatLoss                             0.003s    |- 1.73%  

  |- Residual                             0.003s    |- 1.56%  

|- Output                                 0.002s  |- 1.28%    

|- Logging                                0.002s  |- 0.97%    

|- Input                                  0.000s  |- 0.05%    

Initialization                            0.061s  25.14%      

|- execution                              0.059s  |- 95.82%   

------------------------------------------------------------

TOTAL                                     0.243s

============================================================



Time steps : 49/49, step size: 74.4898, 130.886

```



## stflu003.dat

5000x5000x50, 2D diagonal water flooding in uniformed corner point

```
Running simulation [simuapp]: uniformed corner grid (-novtu)

Elapsed: 0.39s

    46 255.0522  5   3650.000   624.70             11.24              1.77                     635.95    0.000  747.532   0.0384    0.019



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.184s  77.65%      

|- Newton                                 0.178s  |- 96.46%   

  |- Update                               0.059s    |- 33.34% 

  |- FluxJac                              0.039s    |- 22.02% 

  |- Precond                              0.018s    |- 10.28% 

  |- ScdAcc                               0.018s    |- 9.92%  

  |- update_dev                           0.009s    |- 5.04%  

  |- PerfJac                              0.008s    |- 4.40%  

  |- Solver                               0.008s    |- 4.37%  

  |- SanitizeJac                          0.005s    |- 2.95%  

  |- alignvar                             0.004s    |- 2.00%  

  |- HeatLoss                             0.003s    |- 1.63%  

  |- Residual                             0.003s    |- 1.45%  

|- Logging                                0.002s  |- 1.23%    

|- Output                                 0.002s  |- 1.12%    

|- Input                                  0.000s  |- 0.05%    

Initialization                            0.053s  22.35%      

|- execution                              0.050s  |- 94.60%   

------------------------------------------------------------

TOTAL                                     0.238s

============================================================



Time steps : 46/46, step size: 79.3478, 130.807

```

![png]({{ "/assets/images/benchmark_image_13.png" | relative_url }})



## stflu004.dat

2D diagonal water flooding for reduction of numerical dispersion and grid orientation effect


```
Running simulation [simuapp]: 2D diagonal flow: grid orientation

Elapsed: 0.69s

    61  58.6232  5   3650.000   613.68             22.27              3.50                     635.95    0.000  680.511   0.0195    0.039



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.466s  88.39%      

|- Newton                                 0.449s  |- 96.33%   

  |- Update                               0.183s    |- 40.65% 

  |- FluxJac                              0.102s    |- 22.74% 

  |- ScdAcc                               0.038s    |- 8.52%  

  |- Solver                               0.029s    |- 6.49%  

  |- Precond                              0.029s    |- 6.40%  

  |- update_dev                           0.021s    |- 4.64%  

  |- PerfJac                              0.012s    |- 2.71%  

  |- HeatLoss                             0.008s    |- 1.69%  

  |- SanitizeJac                          0.007s    |- 1.50%  

  |- Residual                             0.006s    |- 1.43%  

  |- alignvar                             0.004s    |- 0.99%  

|- Output                                 0.012s  |- 2.67%    

|- Logging                                0.002s  |- 0.50%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.061s  11.61%      

|- execution                              0.059s  |- 96.08%   

------------------------------------------------------------

TOTAL                                     0.528s

============================================================



Time steps : 61/61, step size: 59.8361, 80.6364

```

![png]({{ "/assets/images/benchmark_image_14.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_15.png" | relative_url }})

## stflu007.dat

PEBI_GRID


```
Running simulation [simuapp]: 2D diagonal flow: pebi grid

Elapsed: 0.92s

    59 354.4145  5   3650.000   623.41             12.54              1.97                     635.95    0.000  1.3e+03   0.0716    0.058



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.666s  89.54%      

|- Newton                                 0.646s  |- 96.91%   

  |- Update                               0.208s    |- 32.16% 

  |- FluxJac                              0.205s    |- 31.72% 

  |- Solver                               0.058s    |- 8.93%  

  |- ScdAcc                               0.052s    |- 8.04%  

  |- Precond                              0.038s    |- 5.85%  

  |- update_dev                           0.029s    |- 4.48%  

  |- HeatLoss                             0.012s    |- 1.78%  

  |- Residual                             0.010s    |- 1.54%  

  |- PerfJac                              0.009s    |- 1.42%  

  |- SanitizeJac                          0.009s    |- 1.34%  

  |- alignvar                             0.006s    |- 0.88%  

|- Output                                 0.014s  |- 2.11%    

|- Logging                                0.002s  |- 0.29%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.078s  10.46%      

|- execution                              0.068s  |- 87.40%   

------------------------------------------------------------

TOTAL                                     0.744s

============================================================



Time steps : 59/59, step size: 61.8644, 119.411

```

![png]({{ "/assets/images/benchmark_image_16.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_17.png" | relative_url }})

## stflu026.dat

* Steam flood on two component live oil

```
Running simulation [simuapp]: 3 component steam flooding (-novtu)

Elapsed: 1.39s

    94  36.8774  4   3650.000     0.01              4.36             99.85                       4.50    2.860    9.784   0.0020    0.821



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.152s  94.41%      

|- Newton                                 1.130s  |- 98.10%   

  |- FluxJac                              0.329s    |- 29.08% 

  |- Update                               0.306s    |- 27.08% 

  |- ScdAcc                               0.111s    |- 9.83%  

  |- Precond                              0.102s    |- 9.00%  

  |- Solver                               0.084s    |- 7.40%  

  |- update_dev                           0.061s    |- 5.43%  

  |- PerfJac                              0.048s    |- 4.26%  

  |- SanitizeJac                          0.027s    |- 2.43%  

  |- alignvar                             0.019s    |- 1.64%  

  |- Residual                             0.011s    |- 1.00%  

  |- HeatLoss                             0.009s    |- 0.79%  

|- Output                                 0.008s  |- 0.68%    

|- Logging                                0.006s  |- 0.50%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.068s  5.59%       

|- execution                              0.065s  |- 94.85%   

------------------------------------------------------------

TOTAL                                     1.220s

============================================================



Time steps : 94/95, step size: 38.8298, 73.243

```

#### Load OURS, CMG and ECL

* STARS wells: CRNR PRDCR, EDGE PRDCR, INJECTOR. STARS block history at (1,1,4), (5,5,4), (9,1,1) and (5,4,1); ECL has the first three only.

* ECL names the two producers PNEAR (EDGE PRDCR, block 5,5,4) and PFAR (CRNR PRDCR, block 9,1,1); PNEAR produces twice PFAR at the start, as EDGE does CRNR.

```
OURS reached day 3650.0 of 3650

```

### Wells

* One row per well: bottom-hole pressure, water rate, oil rate (producers only).

![png]({{ "/assets/images/benchmark_image_18.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation. (5,4,1) has no ECL curve.

![png]({{ "/assets/images/benchmark_image_19.png" | relative_url }})

# SPE4C

* Steam flood on three component live oil

* 'Water', 'LiteOil', 'Medm oil', 'Heavy oil'


## Run & Load

```
Running simulation [simuapp]: SPE4-C benchmark on live oil (-novtu)

Elapsed: 1.59s

    95 165.6701  5   3650.000     0.01              4.25             99.86                       4.32    2.067    0.690   0.0040    3.074



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.364s  95.80%      

|- Newton                                 1.342s  |- 98.42%   

  |- FluxJac                              0.359s    |- 26.74% 

  |- Update                               0.336s    |- 25.02% 

  |- Solver                               0.155s    |- 11.58% 

  |- Precond                              0.135s    |- 10.07% 

  |- ScdAcc                               0.131s    |- 9.79%  

  |- update_dev                           0.080s    |- 5.94%  

  |- PerfJac                              0.054s    |- 4.02%  

  |- SanitizeJac                          0.028s    |- 2.11%  

  |- alignvar                             0.019s    |- 1.40%  

  |- Residual                             0.011s    |- 0.85%  

  |- HeatLoss                             0.010s    |- 0.74%  

|- Output                                 0.009s  |- 0.62%    

|- Logging                                0.006s  |- 0.46%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.060s  4.20%       

|- execution                              0.056s  |- 94.28%   

------------------------------------------------------------

TOTAL                                     1.424s

============================================================



Time steps : 95/98, step size: 38.4211, 55.9079

```

#### Load CMG

### Load ECL

### Wells

* One row per well: bottom-hole pressure, water rate, oil rate (producers only). ECL names the producers PNEAR (EDGE PRDCR) and PFAR (CRNR PRDCR).

![png]({{ "/assets/images/benchmark_image_20.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation, CMG and ECL against OURS.

![png]({{ "/assets/images/benchmark_image_21.png" | relative_url }})

# Cyclic steam stimulation

## CSS SPE4

stspe001.dat: Cyclic steam stimulation on radial grid

```
Running simulation [simuapp]: Cyclic steam stimulation in Radial grid

Elapsed: 0.92s

   110  16.2309  6   1095.000     0.79              0.50             38.50                               0.062    4.644   0.1420    1.026



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.693s  92.37%      

|- Newton                                 0.656s  |- 94.68%   

  |- Update                               0.196s    |- 29.96% 

  |- FluxJac                              0.124s    |- 18.83% 

  |- Precond                              0.077s    |- 11.67% 

  |- ScdAcc                               0.068s    |- 10.29% 

  |- PerfJac                              0.065s    |- 9.87%  

  |- update_dev                           0.035s    |- 5.36%  

  |- SanitizeJac                          0.026s    |- 3.97%  

  |- Solver                               0.023s    |- 3.51%  

  |- alignvar                             0.014s    |- 2.19%  

  |- Residual                             0.006s    |- 0.87%  

  |- HeatLoss                             0.004s    |- 0.64%  

|- Output                                 0.023s  |- 3.30%    

|- Logging                                0.006s  |- 0.83%    

|- Input                                  0.001s  |- 0.13%    

Initialization                            0.057s  7.63%       

|- execution                              0.055s  |- 95.92%   

------------------------------------------------------------

TOTAL                                     0.750s

============================================================



Time steps : 110/116, step size: 9.95455, 19.0521

```

![png]({{ "/assets/images/benchmark_image_22.png" | relative_url }})

### Wells

* Injector: bottom-hole pressure (ECL only; the CMG well export has none) and water rate. Producer: bottom-hole pressure (ECL only), water and oil rate.

* Bottom-hole pressure is drawn only while the well flows: ECL reports 0 for a shut-in well and OURS holds its last value.

![png]({{ "/assets/images/benchmark_image_23.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation, CMG and ECL against OURS.

![png]({{ "/assets/images/benchmark_image_24.png" | relative_url }})



## stflu008.dat

Cyclic steam stimulation on cartesian grid


```
Running simulation [simuapp]: Cyclic steam stimulation in Cartesian

Elapsed: 9.11s

   139  89.7013  6   1095.000     1.43              1.45             50.29                               0.476   49.444   0.1070    5.828



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  8.878s  99.23%      

|- Newton                                 8.780s  |- 98.89%   

  |- FluxJac                              3.142s    |- 35.79% 

  |- Update                               2.647s    |- 30.15% 

  |- Solver                               0.849s    |- 9.67%  

  |- ScdAcc                               0.724s    |- 8.24%  

  |- Precond                              0.421s    |- 4.79%  

  |- update_dev                           0.414s    |- 4.71%  

  |- Residual                             0.096s    |- 1.09%  

  |- PerfJac                              0.090s    |- 1.02%  

  |- HeatLoss                             0.088s    |- 1.01%  

  |- SanitizeJac                          0.087s    |- 1.00%  

  |- alignvar                             0.064s    |- 0.73%  

|- Output                                 0.073s  |- 0.82%    

|- Logging                                0.043s  |- 0.48%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.069s  0.77%       

|- execution                              0.067s  |- 96.49%   

------------------------------------------------------------

TOTAL                                     8.947s

============================================================



Time steps : 139/147, step size: 7.8777, 16.6126

```

```
Found 140 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu008_00139.vtu

```

![png]({{ "/assets/images/benchmark_image_25.png" | relative_url }})

### Wells

![png]({{ "/assets/images/benchmark_image_26.png" | relative_url }})

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

Elapsed: 31.16s

   123  40.1083  6   1095.000     0.76              0.44             36.84                               0.161   75.104   0.1995    2.169



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 30.865s  99.60%      

|- Newton                                30.615s  |- 99.19%   

  |- FluxJac                             12.953s    |- 42.31% 

  |- Update                               8.324s    |- 27.19% 

  |- Solver                               3.874s    |- 12.65% 

  |- ScdAcc                               2.030s    |- 6.63%  

  |- update_dev                           1.253s    |- 4.09%  

  |- Precond                              1.101s    |- 3.60%  

  |- Residual                             0.290s    |- 0.95%  

  |- HeatLoss                             0.138s    |- 0.45%  

  |- alignvar                             0.130s    |- 0.42%  

  |- SanitizeJac                          0.085s    |- 0.28%  

  |- PerfJac                              0.069s    |- 0.22%  

|- Output                                 0.217s  |- 0.70%    

|- Logging                                0.019s  |- 0.06%    

|- Input                                  0.001s  |- 0.00%    

Initialization                            0.125s  0.40%       

|- execution                              0.084s  |- 67.73%   

------------------------------------------------------------

TOTAL                                    30.990s

============================================================



Time steps : 123/125, step size: 8.90244, 19.9592

```

```
Found 124 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu009_00123.vtu

```

![png]({{ "/assets/images/benchmark_image_27.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_28.png" | relative_url }})

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

Elapsed: 16.67s

   213  32.9215  7   1095.000     1.62              1.67             50.81                               1.543   25.689   0.1019    2.570



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 16.344s  99.32%      

|- Newton                                16.159s  |- 98.87%   

  |- FluxJac                              6.429s    |- 39.79% 

  |- Update                               4.329s    |- 26.79% 

  |- Solver                               1.967s    |- 12.17% 

  |- ScdAcc                               1.207s    |- 7.47%  

  |- update_dev                           0.743s    |- 4.60%  

  |- Precond                              0.664s    |- 4.11%  

  |- PerfJac                              0.187s    |- 1.16%  

  |- Residual                             0.137s    |- 0.85%  

  |- SanitizeJac                          0.119s    |- 0.74%  

  |- alignvar                             0.097s    |- 0.60%  

  |- HeatLoss                             0.067s    |- 0.42%  

|- Output                                 0.145s  |- 0.88%    

|- Logging                                0.038s  |- 0.23%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.111s  0.68%       

|- execution                              0.088s  |- 78.71%   

------------------------------------------------------------

TOTAL                                    16.456s

============================================================



Time steps : 213/221, step size: 5.14085, 14.6231

```

```
Found 214 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu025_00213.vtu

```

![png]({{ "/assets/images/benchmark_image_29.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_30.png" | relative_url }})

### stflu013.dat - SPE4 problem 1A, cyclic steam

* 20x20x4 corner-point FIELD grid, water and dead oil with no gas component. One well location is modelled as two wells that are never open together: 'Injector 1' (`*MAX *STW 1000`, BHP limit 10000 psi) and 'Producer 1' (`*MAX *STL 1000`, `*MIN *BHP 17`). Three cycles of 10 days of injection, 7 of soak, then production, ending at days 365, 730 and 1095.

* Reference is the DeepFlow THERM `stars_stflu013.log` time step summary, one row per step. simuapp is run with `-log` to write the same table, so both sides are read the same way. THERM is in bbl/day, ours in m3/day.

* No free gas is produced, so the gas and GOR columns of both logs are blank. `read_step_summary_log()` drops blank fields and would leave the rates NaN, so this section reads the table by column position instead.

```
Running simulation [simuapp]: Cyclic steam stimulation, SPE4 problem 1A (-novtu)

Elapsed: 8.21s

No text to display.

```

```
OURS reached day 1095.0 of 1095

THERM: 77 steps marched, 0 cuts, 96 Newton cycles, material balance error 0.021 % at the last step

 OURS: 99 steps marched, 9 cuts, 375 Newton cycles, material balance error 0.028 % at the last step

```

### Wells

* Field totals from the time step summary, in m3/day at standard conditions. While injecting, 'Injector 1' holds its 1000 bbl/day (158.99 m3/day) `*STW` target; while producing, 'Producer 1' holds 1000 bbl/day of liquid, so the oil and water curves must sum to the same target. The liquid panel checks that sum directly.

![png]({{ "/assets/images/benchmark_image_31.png" | relative_url }})

### Step size

* Steps are compared on simulated time, not step number: the two programs march different counts.

* The first run in `runs` is the reference; the right panel is the interpolated dt ratio to it.

* Fewer steps and Newton cycles at the same end time is cheaper, but only counts when the well curves above still agree.

```
run             THERM  OURS

steps              77    99

newton             96   375

newton/step     1.247 3.788

cuts                0     9

dt min          0.002 0.002

dt geomean      1.671 1.927

dt max          118.9 133.6

end day          1095  1095

steps@1.09d         5     5

steps@11d          10    10

steps@110d         19    20

steps@548d         45    57

steps@1.1e+03d     77    99

```

![png]({{ "/assets/images/benchmark_image_32.png" | relative_url }})

### stflu015.dat - single producer on a corner-point grid

* 14x14x5 corner-point FIELD grid, water and dead oil with no gas component. One producer, 'Producer', perforated in block (1,1,1) on `*OPERATE *MAX *STL 400` with a `*MIN *BHP 17` limit. There is no injector, so this is a depletion run to day 365, from an initial `*REFPRES 1000`.

* Reference is the DeepFlow THERM `stars_stflu015.log` time step summary, read with `read_step_summary_columns()` from the stflu013 section above (gas and GOR are blank in both logs). THERM is in bbl/day, ours in m3/day.

* Our log prints the rates with two decimals, so the water curve is coarse.

```
Running simulation [simuapp]: Corner grid, single producer on STL (-novtu)

Elapsed: 0.44s

No text to display.

```

```
OURS reached day 365.0 of 365

THERM: 14 steps marched, 0 cuts, 14 Newton cycles, material balance error 5e-06 % at the last step

 OURS: 14 steps marched, 0 cuts, 14 Newton cycles, material balance error 0 % at the last step

```

### Wells

* Field totals from the time step summary, in m3/day at standard conditions. 'Producer' holds 400 bbl/day (63.6 m3/day) of liquid on `*STL`, so oil plus water must sit on that target; the liquid panel checks the sum directly.

![png]({{ "/assets/images/benchmark_image_33.png" | relative_url }})

### Step size

* Steps are compared on simulated time, not step number: the two programs march different counts.

* The first run in `runs` is the reference; the right panel is the interpolated dt ratio to it.

* Fewer steps and Newton cycles at the same end time is cheaper, but only counts when the well curves above still agree.

```
run           THERM  OURS

steps            14    14

newton           14    14

newton/step       1     1

cuts              0     0

dt min         0.02  0.02

dt geomean    2.654 2.619

dt max        159.2 172.9

end day         365   365

steps@0.365d      3     3

steps@3.65d       6     6

steps@36.5d      10    10

steps@182d       12    12

steps@365d       14    14

```

![png]({{ "/assets/images/benchmark_image_34.png" | relative_url }})

### VAPEX (2D) Experiment 

* incomp gas

* 'WATER' 'LLOYD_O' 'ASPHALT' 'PROPANE'

* MOD

* 9 hours

```
Running simulation [simuapp]: Incomp GAS (-novtu)

Elapsed: 3.36s

No text to display.

```

### Wells

![png]({{ "/assets/images/benchmark_image_35.png" | relative_url }})

### Step size

* Steps are compared on simulated time, not step number: the two programs march different counts.

* The first run in `runs` is the reference; the right panel is the interpolated dt ratio to it.

* Fewer steps and Newton cycles at the same end time is cheaper, but only counts when the well curves above still agree.

```
run                 THERM     OURS

steps                  61      267

newton                224     1664

newton/step         3.672    6.232

cuts                    1        9

dt min            5.8e-06 4.63e-06

dt geomean      0.0001588 0.001012

dt max             0.0016  0.00175

end day           0.01736    0.375

steps@1.74e-05d         2        3

steps@0.000174d        10        9

steps@0.00174d         21       18

steps@0.00868d         47       45

steps@0.0174d          61       60

```

![png]({{ "/assets/images/benchmark_image_36.png" | relative_url }})

### SAGD

#### 2D cross the well

```
Running simulation [simuapp]: SAGD (-novtu)

Elapsed: 3.55s

   213   9.6907  6   2526.000     5.52             52.63             90.50                      54.07    0.276    2.889   0.0408    6.325



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  3.310s  98.04%      

|- Newton                                 3.273s  |- 98.88%   

  |- Update                               1.061s    |- 32.42% 

  |- FluxJac                              0.865s    |- 26.42% 

  |- ScdAcc                               0.362s    |- 11.06% 

  |- Precond                              0.282s    |- 8.60%  

  |- update_dev                           0.234s    |- 7.15%  

  |- Solver                               0.173s    |- 5.28%  

  |- SanitizeJac                          0.074s    |- 2.26%  

  |- alignvar                             0.054s    |- 1.66%  

  |- PerfJac                              0.052s    |- 1.58%  

  |- Residual                             0.041s    |- 1.25%  

  |- HeatLoss                             0.008s    |- 0.25%  

|- Logging                                0.019s  |- 0.57%    

|- Output                                 0.014s  |- 0.43%    

|- Input                                  0.001s  |- 0.02%    

Initialization                            0.066s  1.96%       

|- execution                              0.063s  |- 95.59%   

------------------------------------------------------------

TOTAL                                     3.376s

============================================================



Time steps : 213/216, step size: 11.8592, 13.1609

```

### Wells

* The reference here is the in-house Fortran code (stm_stflu020_*.csv), labelled FORTRAN. It reports producer rates negative.

![png]({{ "/assets/images/benchmark_image_37.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, water, oil and gas saturation. (1,5,13) sits near the injector and (1,5,18) near the producer.

![png]({{ "/assets/images/benchmark_image_38.png" | relative_url }})

#### 2D along well

```
Running simulation [simuapp]: SAGD (-novtu)

Elapsed: 2.83s

   100 163.6974  6   2526.000     5.79            142.07             96.08                     150.00    1.212  124.377   0.0832   11.957



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.583s  97.62%      

|- Newton                                 2.556s  |- 98.94%   

  |- Update                               0.679s    |- 26.56% 

  |- FluxJac                              0.628s    |- 24.55% 

  |- PerfJac                              0.398s    |- 15.59% 

  |- ScdAcc                               0.249s    |- 9.73%  

  |- Precond                              0.169s    |- 6.61%  

  |- update_dev                           0.138s    |- 5.39%  

  |- Solver                               0.111s    |- 4.33%  

  |- SanitizeJac                          0.066s    |- 2.58%  

  |- alignvar                             0.033s    |- 1.30%  

  |- Residual                             0.026s    |- 1.02%  

  |- HeatLoss                             0.005s    |- 0.20%  

|- Logging                                0.016s  |- 0.63%    

|- Output                                 0.010s  |- 0.38%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.063s  2.38%       

|- execution                              0.060s  |- 95.73%   

------------------------------------------------------------

TOTAL                                     2.646s

============================================================



Time steps : 100/109, step size: 25.26, 52.2428

```

### Wells

![png]({{ "/assets/images/benchmark_image_39.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation. The blocks follow the producer-injector pair down the 10x1x20 grid.

![png]({{ "/assets/images/benchmark_image_40.png" | relative_url }})

#### 3D

```
Running simulation [simuapp]: SAGD 3D (-novtu)

Elapsed: 25.18s

   154   3.6054  6    680.000    14.23             99.74             87.51                      90.66    1.090    1.472   0.0912    5.244



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 24.939s  99.74%      

|- Newton                                24.866s  |- 99.71%   

  |- FluxJac                              9.687s    |- 38.96% 

  |- Update                               7.146s    |- 28.74% 

  |- Solver                               2.694s    |- 10.83% 

  |- ScdAcc                               2.026s    |- 8.15%  

  |- update_dev                           1.155s    |- 4.64%  

  |- Precond                              0.893s    |- 3.59%  

  |- PerfJac                              0.356s    |- 1.43%  

  |- Residual                             0.246s    |- 0.99%  

  |- alignvar                             0.138s    |- 0.56%  

  |- SanitizeJac                          0.112s    |- 0.45%  

  |- HeatLoss                             0.100s    |- 0.40%  

|- Logging                                0.039s  |- 0.16%    

|- Output                                 0.023s  |- 0.09%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.065s  0.26%       

|- execution                              0.062s  |- 95.69%   

------------------------------------------------------------

TOTAL                                    25.004s

============================================================



Time steps : 154/160, step size: 4.41558, 3.45336

```

#### 2D live oil

* 10x1x20 cross-section, two-component live oil (CH4 + HOIL) with water. Injector 'Inj' (2:9,1,13) and producer 'Prod' (2:9,1,18); both are shut in and preheated for 60 days, then opened.

* CMG only (no ECL run for this deck).

```
Running simulation [simuapp]: SAGD live oil (-novtu)

Elapsed: 5.53s

   167   8.7430  6   2526.000     7.54     4.81   146.72     0.64    95.11                     150.00    0.973   10.397   0.0394    1.101



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  5.284s  98.58%      

|- Newton                                 5.236s  |- 99.09%   

  |- FluxJac                              1.436s    |- 27.43% 

  |- Update                               1.286s    |- 24.56% 

  |- PerfJac                              0.715s    |- 13.65% 

  |- ScdAcc                               0.529s    |- 10.10% 

  |- Solver                               0.341s    |- 6.52%  

  |- update_dev                           0.329s    |- 6.28%  

  |- Precond                              0.316s    |- 6.03%  

  |- SanitizeJac                          0.084s    |- 1.60%  

  |- alignvar                             0.057s    |- 1.10%  

  |- Residual                             0.043s    |- 0.82%  

  |- HeatLoss                             0.009s    |- 0.18%  

|- Logging                                0.022s  |- 0.41%    

|- Output                                 0.018s  |- 0.34%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.076s  1.42%       

|- execution                              0.073s  |- 95.93%   

------------------------------------------------------------

TOTAL                                     5.360s

============================================================



Time steps : 167/180, step size: 15.1257, 12.5404

```

#### Load OURS and CMG

* STARS wells: Inj, Prod (deck order, so .smy well index 0 and 1). STARS block history at (1,1,19), (2,1,18), (5,1,13) and (5,1,5).

* 10x1x20 grid, so the .smy block index is (i-1) + (k-1)*10.

```
OURS reached day 2526.0 of 2526

```

### Wells

* Top row: injector BHP and water rate, producer BHP. Bottom row: producer oil, water and gas rates. The wells are shut in until day 60.

![png]({{ "/assets/images/benchmark_image_41.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation.

![png]({{ "/assets/images/benchmark_image_42.png" | relative_url }})

#### 3D live oil

* 20x10x10 SAGD, live oil (CH4 + HOIL) with water. Injector 'Inj' (2:19,1,7) and producer 'Prod' (2:19,1,9); both are shut in and heated by `UHTR`/`TMPSET` for 60 days, then opened. The run ends at the first `*STOP`, day 680.

* Reference is the `stars_stflu024.log` time step summary (one row per step), not a well-history CSV, so both sides are read from the same kind of table: simuapp is run with `-log` to write its own.

* Injection is water only (steam, quality 0.85); the injection oil and gas columns are blank in both logs.

```
Running simulation [simuapp]: SAGD 3D live oil (-novtu)

Elapsed: 34.24s

No text to display.

```

```
OURS reached day 680.0 of 680

  CMG: 124 steps marched, 0 cuts, 289 Newton cycles

 OURS: 147 steps marched, 12 cuts, 858 Newton cycles

```

### Wells

* Rates are m3/day at standard conditions, read from the time step summary. The wells are shut in until day 60, so there is nothing to plot before it.

![png]({{ "/assets/images/benchmark_image_43.png" | relative_url }})

#### *KRTEMTAB verification (stflu028)

* 5x5x1 FIELD grid with five producers and one injector, from the STARS `verify48` verification deck. `*KRTEMTAB` moves the relative permeability endpoints with temperature between 123 F and 500 F. The producers run on `*OPERATE *MAX *STO 30`; the injector is open from day 700 to day 1431. The run ends at day 2435.

* Reference is the CMG `verify48` run: `stars_stflu028.log` (time step summary, field totals in FIELD units) and `stars_stfu028_special.csv` (pressure at blocks (1,2,1) and (2,3,1)). simuapp is run with `-log` so both sides of the rates are the same kind of table.

```
Running simulation [simuapp]: *KRTEMTAB verification (-novtu)

Elapsed: 0.44s

No text to display.

```

```
OURS reached day 2435.0 of 2435

  CMG: 90 steps marched, 0 cuts, 94 Newton cycles

 OURS: 40 steps marched, 0 cuts, 134 Newton cycles

```

### Wells

* Field totals from the time step summary. The CMG log is in bbl/day and ft3/day, ours in m3/day. The injector is open only between days 700 and 1431.

![png]({{ "/assets/images/benchmark_image_44.png" | relative_url }})

### Blocks

* Pressure at the two blocks CMG reports. 5x5x1 grid, so the .smy block index is (i-1) + (j-1)*5: (1,2,1) is 5 and (2,3,1) is 11.

![png]({{ "/assets/images/benchmark_image_45.png" | relative_url }})

#### Temperature dependent relative permeability (stflu029)

* 15x1x15 SI cross-section, injector 'Injector S1' at (1,1,15) and producer 'Producer P1' at (1,1,12). Both are shut in and heated by `UHTR`/`TMPSET` for 150 days, then opened. `*KRTEMTAB *SWR *SORW` moves the connate and critical water and the residual oil between 7 C and 307 C. The run ends at day 820.

* Reference is the DeepFlow THERM `stars_stflu029.log` time step summary (one row per step), not a well-history CSV, so both sides are read from the same kind of table: simuapp is run with `-log` to write its own. Both logs are in m3/day.

* Our log prints the rates with two decimals, so the oil and gas curves are coarse.

```
Running simulation [simuapp]: Temperature dependent relative permeability (-novtu)

Elapsed: 5.77s

No text to display.

```

```
OURS reached day 820.0 of 820

THERM: 506 steps marched, 0 cuts, 659 Newton cycles

 OURS: 246 steps marched, 14 cuts, 1317 Newton cycles

```

### Wells

* Rates are m3/day at standard conditions, read from the time step summary. The wells are shut in until day 150, so there is nothing to plot before it.

![png]({{ "/assets/images/benchmark_image_46.png" | relative_url }})

#### Wet combustion tube (stflu033)

* 20x1x1 SI tube, 1.75 m long, with six components (water, heavy / medium / light oil, inert gas, oxygen) and three oil-burning reactions (`*STOREAC`, `*STOPROD`, `*RORDER`, `*FREQFAC`, `*EACT`, `*RENTH`): the Smith and Perkins forward wet-combustion experiment. Heaters bring the four blocks at the inlet to 267 C, air is injected from day 2e-4, and water is co-injected with it from day 0.02 (`*INCOMP *WATER-GAS`, `*OPERATE *STF`). The producer holds 5620 kPa at the far end (`*PERF *TUBE-END`). The run ends at day 0.6667.

* Reference is DeepFlow THERM: `stars_stflu033.log` (time step summary) for the production rates and the cost of the run, and `stars_stflu033.prn` for the grid profiles at its report times and for the cumulative balance with its reaction totals. Our profiles come from the VTU series (`*OUTSRF *GRID`; the profiles are all that reads it, so this deck keeps its `.vtu` in `FIELD_PLOT_DECKS`), our balance from the `.out` the run writes.

* Two things are judged separately. The reaction totals are what the kinetics burn, wherever the front is; the profiles say where the heat goes - the hot peak at the front, and the wet plateau behind it where the injected water condenses.

```
Running simulation [simuapp]: Wet combustion tube

Elapsed: 0.85s

No text to display.

```

```
OURS reached day 0.6670 of 0.6667

THERM: 116 steps marched, 0 cuts, 361 Newton cycles

 OURS: 126 steps marched, 6 cuts, 580 Newton cycles

```

### Wells

* Producer rates are m3/day at standard conditions. DeepFlow's come from its time step summary; ours from the `.smy`, which keeps the digits the `.log` rounds away (the oil rate falls to 1e-11).

* The injector holds its target (3.06883 m3/day of water and air, 8.83e-3 of it water), so the producer is the curve to read.

![png]({{ "/assets/images/benchmark_image_47.png" | relative_url }})

### Profiles along the tube

* Temperature, water and oil saturation against distance from the injector, at DeepFlow's report times (the deck's `*TIME` cards), DeepFlow dashed and ours solid in the same colour.

* The tube is one-dimensional: block 1 is at the injector end (`*KDIR *DOWN`). The `.prn` marks a few values with a trailing `i` / `p` (the well blocks); the marker is dropped.

```
DeepFlow report times (days): [1e-05, 0.0002, 0.02, 0.083333, 0.16667, 0.25, 0.66667]

```

![png]({{ "/assets/images/benchmark_image_48.png" | relative_url }})

```
 t (days)   peak T DEEPFLOW (C)  at (m)    peak T OURS (C)  at (m)

    1e-05                    99    0.04                 99    0.04

   0.0002                   261    0.04                262    0.04

     0.02                   341    0.04                341    0.04

  0.08333                   348    0.13                348    0.13

   0.1667                   380    0.22                380    0.22

     0.25                   403    0.31                403    0.31

   0.6667                   477    1.10                470    1.10

```

### Reactions

* What the reactions did by each time, from the cumulative balance both programs print (the `Net Reactions` column): oxygen consumed, oil burnt, water produced and heat released.

* DeepFlow prints it for a handful of steps; the step's time comes from its `.log`. Ours is read from the `.out` at every report.

```
At day 0.6667 (ours: report at day 0.6667)

                     DEEPFLOW         OURS  difference

 Oxygen consumed        17.52        17.33       -1.1%  gmol

       Oil burnt       0.5619       0.5552       -1.2%  gmol

  Water produced        11.53         11.4       -1.1%  gmol

   Heat released    7.346e+06    7.268e+06       -1.1%  J

```

![png]({{ "/assets/images/benchmark_image_49.png" | relative_url }})

### Step size

* Steps are compared on simulated time, as for the other decks. The first run is the reference.

```
run                THERM     OURS

steps                116      126

newton               361      580

newton/step        3.112    4.603

cuts                   0        6

dt min           8.8e-06 7.24e-06

dt geomean      0.002991 0.002744

dt max             0.017   0.0203

end day           0.6667    0.667

steps@0.000667d       13       14

steps@0.00667d        17       18

steps@0.0667d         36       39

steps@0.333d          79       82

steps@0.667d         116      125

```

![png]({{ "/assets/images/benchmark_image_50.png" | relative_url }})

#### Foamy oil primary production (sttst66)

* 12x12x7 SI block with one horizontal producer (`*WELL 1 'PRODN' *FRAC 0.25`, `*GEOMETRY *J`, six perforated layers) on a 250 kPa bottom-hole limit and no injection. Four components: water, dead oil, and two gases (`FM_GAS`, `GAS`) that stay in the gas phase through a constant K value. The `*STOREAC` reaction turns dissolved-gas-like `FM_GAS` into free `GAS` (the foamy-oil lamella drainage), and the run lasts two years.

* Reference is DeepFlow THERM: `stars_sttst66.log`. Its step table prints only the oil rate for this deck (no gas or water is produced in the first two years), so that is the comparison; the producer's bottom-hole pressure is held at its limit.

* Two modelling details decide the first step. `*WELL *FRAC` scales the well index only, while a `*GEOMETRY` `ff` also changes the equivalent radius; and a deck without `*PRPOR` takes the reference pressure of the porosity from `*PRSR`, which is what makes the initial oil in place equal DeepFlow's.

```
Running simulation [simuapp]: Foamy oil primary production (-novtu)

Elapsed: 1.73s

No text to display.

```

```
OURS reached day 730.0 of 730.0

oil rate against DeepFlow: mean |error| 0.94%, max 1.44%

   day   DEEPFLOW       OURS    error

     1     42.140     42.144    0.01%

    30     36.550     36.499   -0.14%

    90     31.190     31.001   -0.61%

   180     26.890     26.591   -1.11%

   365     22.400     22.100   -1.34%

   730     18.460     18.194   -1.44%

THERM: 35 steps marched, 0 cuts, 35 Newton cycles

 OURS: 40 steps marched, 0 cuts, 78 Newton cycles

```

![png]({{ "/assets/images/benchmark_image_51.png" | relative_url }})

```
run          THERM  OURS

steps           35    40

newton          35    78

newton/step      1  1.95

cuts             0     0

dt min           1     1

dt geomean   15.73 13.21

dt max          30    30

end day        730   730

steps@0.73d      0     0

steps@7.3d       3     3

steps@73d       10    10

steps@365d      22    26

steps@730d      35    40

```

![png]({{ "/assets/images/benchmark_image_52.png" | relative_url }})

# Speed



`-DCMAKE_BUILD_TYPE=Release`

### Dome corner grid

```
Running simulation [simuapp]: Dome Corner point

Elapsed: 3.14s

    76  77.6820  1    365.000                                                                            0.016   12.402   0.0148    4.869



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.864s  96.88%      

|- Newton                                 2.841s  |- 99.19%   

  |- FluxJac                              1.008s    |- 35.50% 

  |- Update                               0.985s    |- 34.69% 

  |- ScdAcc                               0.250s    |- 8.79%  

  |- Solver                               0.199s    |- 7.01%  

  |- update_dev                           0.128s    |- 4.50%  

  |- Precond                              0.109s    |- 3.84%  

  |- Residual                             0.042s    |- 1.47%  

  |- HeatLoss                             0.026s    |- 0.92%  

  |- alignvar                             0.016s    |- 0.57%  

  |- SanitizeJac                          0.015s    |- 0.53%  

  |- PerfJac                              0.002s    |- 0.07%  

|- Logging                                0.008s  |- 0.28%    

|- Output                                 0.007s  |- 0.25%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.092s  3.12%       

|- execution                              0.082s  |- 88.43%   

------------------------------------------------------------

TOTAL                                     2.956s

============================================================



Time steps : 76/79, step size: 4.80263, 16.5526

```

```
Found 4 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu018_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_53.png" | relative_url }})

## Heterogeneous

### SPE10 benchmark 2D 

```
Running simulation [simuapp]: SPE10 benchmark 2D water flooding 375 days ~7s single thread (OMP_NUM_THREADS=8)

Elapsed: 8.19s

    89   2.1695  6    375.000    19.31             4e-06             2e-05                      19.43    3.367    0.557   0.0471    0.002



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  7.925s  98.98%      

|- Newton                                 7.796s  |- 98.37%   

  |- Update                               2.378s    |- 30.50% 

  |- FluxJac                              2.301s    |- 29.52% 

  |- Solver                               1.274s    |- 16.34% 

  |- ScdAcc                               0.659s    |- 8.45%  

  |- update_dev                           0.329s    |- 4.22%  

  |- Precond                              0.296s    |- 3.80%  

  |- PerfJac                              0.240s    |- 3.08%  

  |- Residual                             0.099s    |- 1.28%  

  |- alignvar                             0.044s    |- 0.57%  

  |- SanitizeJac                          0.040s    |- 0.51%  

  |- HeatLoss                             0.019s    |- 0.25%  

|- Output                                 0.096s  |- 1.21%    

|- Logging                                0.010s  |- 0.13%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.081s  1.02%       

|- execution                              0.073s  |- 89.55%   

------------------------------------------------------------

TOTAL                                     8.006s

============================================================



Time steps : 89/89, step size: 4.21348, 2.75343

```

![png]({{ "/assets/images/benchmark_image_54.png" | relative_url }})

### Medium size



* 202,005 grid block (201x201x5) with heterogeneous permeability

* 61 wells water flooding pattern 

* 1500 days

```
Running simulation [simuapp]: Heterogeneous + 61wells - performance test medium size ~4m.50s (Single) (OMP_NUM_THREADS=8, -novtu)

Elapsed: 246.07s

    32  22.4900  5    365.000   257.30              7.92              2.99                     720.00    0.000  111.773   0.0064    1.457



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                4m 4.31s  99.41%      

|- Newton                               4m 3.84s  |- 99.81%   

  |- FluxJac                           1m 17.64s    |- 31.84% 

  |- Update                            1m 11.46s    |- 29.31% 

  |- Solver                              48.423s    |- 19.86% 

  |- ScdAcc                              17.157s    |- 7.04%  

  |- update_dev                           9.807s    |- 4.02%  

  |- Precond                              7.915s    |- 3.25%  

  |- Residual                             3.071s    |- 1.26%  

  |- HeatLoss                             1.935s    |- 0.79%  

  |- PerfJac                              1.451s    |- 0.59%  

  |- alignvar                             0.832s    |- 0.34%  

  |- SanitizeJac                          0.521s    |- 0.21%  

|- Output                                 0.068s  |- 0.03%    

|- Logging                                0.017s  |- 0.01%    

|- Input                                  0.002s  |- 0.00%    

Initialization                            1.448s  0.59%       

|- execution                              1.310s  |- 90.46%   

------------------------------------------------------------

TOTAL                                   4m 5.75s

============================================================



Time steps : 32/32, step size: 11.4062, 13.2808

```

### Johnansen water flooding

```
Running simulation [simuapp]: Johnansen water flooding takes ~5m on M2 (OMP_NUM_THREADS=8)

Elapsed: 18.76s

    17 365.0000  1   3650.000   353.53              0.07              0.02                     188.86    0.000    3.270   0.0067  3.1e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 17.042s  92.85%      

|- Newton                                16.917s  |- 99.27%   

  |- Update                               5.825s    |- 34.43% 

  |- FluxJac                              5.240s    |- 30.98% 

  |- Solver                               2.881s    |- 17.03% 

  |- ScdAcc                               1.164s    |- 6.88%  

  |- update_dev                           0.668s    |- 3.95%  

  |- Precond                              0.497s    |- 2.94%  

  |- Residual                             0.268s    |- 1.59%  

  |- alignvar                             0.055s    |- 0.33%  

  |- SanitizeJac                          0.031s    |- 0.18%  

  |- PerfJac                              0.002s    |- 0.01%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.086s  |- 0.51%    

|- Logging                                0.002s  |- 0.01%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            1.313s  7.15%       

|- execution                              1.014s  |- 77.25%   

------------------------------------------------------------

TOTAL                                    18.354s

============================================================



Time steps : 17/17, step size: 214.706, 163.784

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data//stflu016_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_55.png" | relative_url }})

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

Elapsed: 1.62s

    79  76.8632  5   3650.000     0.01              4.41             99.73                       4.59    0.044    0.560   0.0041    1.440



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.379s  95.64%      

|- Newton                                 1.358s  |- 98.45%   

  |- FluxJac                              0.602s    |- 44.32% 

  |- Update                               0.322s    |- 23.74% 

  |- ScdAcc                               0.145s    |- 10.65% 

  |- update_dev                           0.108s    |- 7.96%  

  |- Solver                               0.042s    |- 3.07%  

  |- PerfJac                              0.036s    |- 2.67%  

  |- Residual                             0.034s    |- 2.48%  

  |- Precond                              0.021s    |- 1.52%  

  |- alignvar                             0.008s    |- 0.61%  

  |- HeatLoss                             0.005s    |- 0.35%  

  |- SanitizeJac                          0.001s    |- 0.10%  

|- Logging                                0.021s  |- 1.56%    

|- Output                                 0.009s  |- 0.68%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.063s  4.36%       

|- execution                              0.060s  |- 95.56%   

------------------------------------------------------------

TOTAL                                     1.442s

============================================================



Time steps : 79/79, step size: 46.2025, 50.7314

Running simulation [simumpi]: MPI comparison np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 1.63s

    58  34.7768  6   1283.952     1.45              5.06             77.69                       5.96    0.112   41.400   0.1585   30.829

    59  34.2363  6   1318.188     1.37              5.19             79.07                       5.96    0.112   49.445   0.1865   28.352

    60  35.3456  6   1353.533     1.19              4.98             80.75                       5.96    0.112   50.751   0.1295   29.817



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  35.4693  5   1389.003     1.11              5.17             82.31                       5.96    0.112   58.708   0.1482   11.988

    62  41.6349  6   1430.638     0.99              5.28             84.25                       5.96    0.131   52.421   0.0856   20.376

    63  50.9803  6   1481.618     0.73              5.10             87.51                       5.96    0.048   77.847   0.1510   25.489

    64  55.7725  6   1537.390     0.68              4.97             88.02                       5.96    0.047   91.402   0.1354    8.837

    65  68.4025  5   1605.793     0.57              4.93             89.58                       5.96    0.047  111.716   0.1034   11.631

    66  94.4905  5   1700.283     0.47              4.98             91.43                       5.96    0.046  168.523   0.1077    8.200

    67 128.3437  6   1828.627     0.35              4.90             93.32                       5.96    0.045  249.098   0.1046    9.095

    68 176.4333  7   2005.060     0.24              4.82             95.18                       5.96    0.044  385.972   0.0843   11.881

    69 202.8709  9   2207.931     0.16              4.73             96.65                       5.96    0.044  500.142   0.0568   12.735

    70 202.8379  8   2410.769     0.11              4.48             97.69                       5.96    0.044  570.122   0.0874   12.110

    71 187.7887  6   2598.558     0.07              4.33             98.42                       5.96    0.044  590.638   0.0392   10.707

    72 170.1622  6   2768.720     0.05              4.13             98.87                       5.96    0.044  582.895   0.0325    9.252

    73 155.4366  6   2924.156     0.03              3.92             99.18                       5.96    0.044  574.075   0.0273    8.148

    74 143.3048  6   3067.461     0.02              3.58             99.42                       5.96    0.044  580.559   0.0719    7.475

    75 131.2235  6   3198.685     0.01              3.29             99.58                       5.96    0.044  595.371   0.0465    7.020

    76 118.3265  6   3317.011     0.01              2.80             99.70                       5.96    0.044  619.469   0.0435    6.733

    77 104.1116  6   3421.123     0.01              3.36             99.73                       5.17    0.044  224.271   0.0383    3.312

    78 152.0140  6   3573.137     0.01              4.13             99.73                       4.61    0.044   23.341   0.0679    3.321

    79  76.8632  5   3650.000     0.01              4.41             99.73                       4.59    0.044    0.560   0.0041    1.440

Time steps : 79/79, step size: 46.2025, 50.7314

Running simulation [simumpi]: MPI comparison np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 1.03s

    58  34.7666  6   1283.857     1.45              5.06             77.69                       5.96    0.112   41.329   0.1588   30.825

    59  34.2286  6   1318.085     1.37              5.19             79.07                       5.96    0.112   49.360   0.1862   28.293

    60  35.3791  6   1353.464     1.19              4.98             80.74                       5.96    0.112   50.736   0.1291   29.829



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  35.4948  5   1388.959     1.11              5.17             82.30                       5.96    0.112   58.741   0.1479   11.992

    62  41.7046  6   1430.664     0.99              5.28             84.25                       5.96    0.131   52.517   0.0858   20.408

    63  51.0274  6   1481.691     0.73              5.10             87.52                       5.96    0.051   77.922   0.1512   25.498

    64  55.8133  7   1537.504     0.68              4.97             88.02                       5.96    0.050   91.464   0.1355    8.843

    65  68.4337  6   1605.938     0.57              4.93             89.58                       5.96    0.049  111.784   0.1034   11.636

    66  94.5403  5   1700.478     0.47              4.98             91.44                       5.96    0.049  168.637   0.1078    8.197

    67 128.3744  6   1828.853     0.35              4.90             93.33                       5.96    0.047  249.194   0.1045    9.096

    68 176.5287  7   2005.382     0.24              4.82             95.19                       5.96    0.045  386.272   0.0843   11.887

    69 202.9008  6   2208.282     0.16              4.73             96.65                       5.96    0.043  500.235   0.0568   12.734

    70 202.8463  8   2411.129     0.11              4.48             97.69                       5.96    0.043  570.290   0.0873   12.110

    71 187.7631  6   2598.892     0.07              4.33             98.42                       5.96    0.043  590.667   0.0392   10.705

    72 170.1338  6   2769.026     0.05              4.13             98.88                       5.96    0.043  582.888   0.0325    9.250

    73 155.4118  6   2924.437     0.03              3.92             99.18                       5.96    0.043  574.069   0.0273    8.147

    74 143.2828  6   3067.720     0.02              3.58             99.42                       5.96    0.043  580.583   0.0719    7.474

    75 131.2000  6   3198.920     0.01              3.29             99.58                       5.96    0.043  595.391   0.0472    7.019

    76 118.3029  6   3317.223     0.01              2.80             99.70                       5.96    0.043  619.543   0.0428    6.733

    77 104.0829  6   3421.306     0.01              3.36             99.73                       5.17    0.043  223.184   0.0383    3.306

    78 152.2483  6   3573.554     0.01              4.13             99.73                       4.61    0.043   23.302   0.0678    3.326

    79  76.4457  5   3650.000     0.01              4.41             99.73                       4.59    0.043    0.619   0.0040    1.431

Time steps : 79/79, step size: 46.2025, 50.7362

Running simulation [simumpi]: MPI comparison np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 1.09s

    60  35.3089  6   1353.624     1.19              4.98             80.75                       5.96    0.114   50.777   0.1298   29.813



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  35.4354  5   1389.060     1.11              5.17             82.31                       5.96    0.114   58.660   0.1485   11.980

    62  41.5491  6   1430.609     0.99              5.28             84.25                       5.96    0.132   52.308   0.0854   20.333

    63  50.9266  6   1481.535     0.73              5.10             87.51                       5.96    0.050   77.763   0.1509   25.477

    64  55.7275  6   1537.263     0.68              4.97             88.02                       5.96    0.050   91.317   0.1353    8.830

    65  68.3758  5   1605.639     0.57              4.93             89.58                       5.96    0.049  111.662   0.1034   11.628

    66  94.4337  5   1700.072     0.47              4.98             91.43                       5.96    0.048  168.394   0.1076    8.209

    67 128.3250  6   1828.397     0.35              4.90             93.32                       5.96    0.047  249.027   0.1047    9.094

    68 176.3573  7   2004.755     0.24              4.82             95.18                       5.96    0.046  385.731   0.0844   11.877

    69  67.6161  5 1 2072.371     0.21              4.81             95.74                       5.96    0.046  153.035   0.0228    4.161

    70 112.0458  6   2184.417     0.17              4.72             96.55                       5.96    0.046  270.406   0.0859    6.772

    71 151.9044  6   2336.321     0.12              4.56             97.39                       5.96    0.046  403.137   0.0931    8.992

    72 170.8135  5   2507.135     0.08              4.44             98.15                       5.96    0.046  507.714   0.0353    9.907

    73 169.3209  6   2676.455     0.06              4.25             98.68                       5.96    0.046  551.529   0.0336    9.433

    74 159.9040  6   2836.359     0.04              4.05             99.04                       5.96    0.046  563.684   0.0303    8.567

    75 149.0555  6   2985.415     0.03              3.84             99.31                       5.96    0.046  565.716   0.0281    7.751

    76 138.6429  6   3124.058     0.02              3.47             99.50                       5.96    0.046  584.267   0.0636    7.295

    77 126.4638  6   3250.522     0.01              3.11             99.64                       5.96    0.046  601.268   0.0799    6.892

    78 113.3458  6   3363.867     0.01              2.68             99.75                       5.92    0.046  606.732   0.0186    6.431

    79 101.0231  5   3464.890     0.01              3.72             99.74                       4.84    0.046   45.363   0.0958    3.037

    80 143.8453  5   3608.736     0.01              4.30             99.74                       4.58    0.046   10.491   0.0143    3.091

    81  41.2643  6   3650.000     0.01              4.49             99.74                       4.63    0.046    3.093   0.0020    0.747

Time steps : 81/82, step size: 45.0617, 45.9696

simuapp          rc=0   1.44s   79/ 79 steps  to  3650.00 days

simumpi np=1     rc=0   1.31s   79/ 79 steps,  0 cuts  to  3650.00 days

simumpi np=2     rc=0   0.77s   79/ 79 steps,  0 cuts  to  3650.00 days

simumpi np=4     rc=0   0.74s   81/ 82 steps,  1 cuts  to  3650.00 days

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
Running simulation [simuapp]: CSS parity baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 21.75s

   139  89.7013  6   1095.000     1.43              1.45             50.29                               0.476   49.444   0.1070    5.828



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 21.492s  99.69%      

|- Newton                                21.464s  |- 99.87%   

  |- FluxJac                             10.854s    |- 50.57% 

  |- Update                               5.110s    |- 23.81% 

  |- ScdAcc                               2.169s    |- 10.11% 

  |- update_dev                           1.479s    |- 6.89%  

  |- Solver                               0.887s    |- 4.13%  

  |- Precond                              0.392s    |- 1.83%  

  |- alignvar                             0.122s    |- 0.57%  

  |- PerfJac                              0.095s    |- 0.44%  

  |- Residual                             0.095s    |- 0.44%  

  |- HeatLoss                             0.080s    |- 0.37%  

  |- SanitizeJac                          0.024s    |- 0.11%  

|- Logging                                0.021s  |- 0.10%    

|- Output                                 0.010s  |- 0.05%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.066s  0.31%       

|- execution                              0.064s  |- 96.31%   

------------------------------------------------------------

TOTAL                                    21.558s

============================================================



Time steps : 139/147, step size: 7.8777, 16.6126

Running simulation [simumpi]: CSS parity np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 21.10s

   118   7.0000  6    747.000                                                                            0.204  1.2e+03   0.1595   29.740

   119   0.1111  6 2  747.111     0.06            158.93             99.96                               0.204  813.179   0.0496   33.440

   120   0.1451  6    747.256     0.08            148.31             99.94                               0.204  187.541   0.0183   10.360



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   121   0.2867  6    747.543     0.22            119.28             99.82                               0.204  160.591   0.0708    7.291

   122   0.4545  6    747.997     1.46             91.63             98.43                               0.204  169.106   0.1185    6.623

   123   0.5925  6    748.590     3.26             70.30             95.57                               0.204  149.672   0.1190    5.848

   124   0.7709  6    749.361     5.31             53.52             90.97                               0.204  132.811   0.1865    5.393

   125   0.8018  6    750.163     7.03             43.96             86.22                               0.205  104.959   0.1169    4.102

   126   1.0516  6    751.214     8.48             36.27             81.06                               0.205  105.284   0.0420    4.113

   127   1.9167  6    753.131     9.21             28.75             75.75                               0.205  140.715   0.4706    5.686

   128   1.0810  6    754.212     8.68             26.67             75.45                               0.205   68.204   0.0188    2.820

   129   2.1620  6    756.374     8.04             22.93             74.03                               0.206  102.642   0.0221    4.581

   130   4.3239  6    760.698     7.01             18.01             71.98                               0.206  144.794   0.0942    6.739

   131   6.1981  6    766.896     5.81             13.54             69.99                               0.206  143.187   0.1129    7.571

   132   8.2531  7    775.149     4.53             10.06             68.94                               0.207  120.149   0.1466    7.514

   133   9.7398  6    784.889     3.77              8.28             68.73                               0.207   92.968   0.0265    7.108

   134  19.3146  6    804.203     3.05              5.78             65.49                               0.208  108.006   0.0432   10.268

   135  34.9913 11    839.195     2.39              3.86             61.79                               0.208   99.795   0.1284   11.989

   136  38.1724  6    877.367     1.97              2.89             59.47                               0.209   62.859   0.0900    8.389

   137  55.6738  6    933.041     1.49              2.44             62.14                               0.299   42.753   0.1197    5.154

   138  72.2579  6   1005.299     1.51              2.06             57.72                               0.420   40.438   0.0919    4.851

   139  89.7013  6   1095.000     1.43              1.45             50.29                               0.476   49.444   0.1070    5.828

Time steps : 139/147, step size: 7.8777, 16.6126

Running simulation [simumpi]: CSS parity np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 12.14s

   119   0.1968  6    747.597     0.22            112.39             99.80                               0.313   94.031   0.0504    4.066

   120   0.3437  6    747.941     1.19             92.95             98.73                               0.313  130.120   0.0942    5.088



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   121   0.4926  6    748.434     2.52             74.04             96.71                               0.314  132.744   0.1024    5.187

   122   0.6830  6    749.117     4.44             57.91             92.88                               0.314  129.622   0.1543    5.327

   123   0.7857  6    749.902     5.83             45.89             88.74                               0.314  111.039   0.1920    4.357

   124   0.8041  6    750.706     7.32             38.68             84.10                               0.315   90.186   0.0530    3.448

   125   1.3862  6    752.093     8.60             31.31             78.46                               0.315  116.537   0.1014    4.694

   126   1.9297  6    754.022     8.65             26.28             75.24                               0.315  124.583   0.3793    5.145

   127   1.2761  6    755.298     8.09             24.51             75.17                               0.316   67.820   0.0677    2.948

   128   2.0512  6    757.350     7.65             21.72             73.95                               0.316   83.718   0.0686    3.893

   129   3.2843  6    760.634     6.95             18.06             72.23                               0.316  108.530   0.0489    4.891

   130   5.7794  6    766.413     5.78             13.66             70.25                               0.317  132.726   0.1135    6.867

   131   7.6756  7    774.089     4.58             10.33             69.28                               0.317  113.640   0.1477    6.940

   132   9.0229  6    783.112     3.84              8.52             68.95                               0.318   89.661   0.0249    6.643

   133  18.0457  6    801.158     3.14              6.06             65.85                               0.319  106.818   0.1127    9.857

   134  24.0439 12    825.201     2.52              4.38             63.50                               0.320   83.706   0.0884    9.487

   135  24.0439  9    849.245     2.25              3.51             60.90                               0.320   52.915   0.0715    7.035

   136  32.0586  6    881.304     1.97              2.86             59.27                               0.321   46.788   0.0831    6.495

   137  48.1360  6    929.440     1.85              2.24             54.78                               0.322   46.421   0.0882    5.922

   138  70.7401  7   1000.180     1.71              1.66             49.24                               0.336   51.275   0.1614    6.386

   139  79.5147  6   1079.695     1.36              1.23             47.54                               0.405   47.551   0.1359    5.563

   140  15.3053  6   1095.000     0.99              1.30             56.91                               0.415    8.965   0.0721    1.044

Time steps : 140/145, step size: 7.82143, 16.9958

Running simulation [simumpi]: CSS parity np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 7.05s

   115   0.1111  6    747.222     0.08            152.04             99.95                               0.699  170.284   0.0130    9.402

   116   0.2222  6    747.444     0.01            126.95             99.99                               0.699  138.341   0.0506    6.338

   117   0.3878  6    747.832     0.97             99.84             99.04                               0.699  158.939   0.1046    6.334

   118   0.5332  6    748.365     2.52             77.72             96.86                               0.699  154.941   0.1213    6.138

   119   0.6878  6    749.053     4.45             59.48             93.04                               0.699  135.403   0.1755    5.481

   120   0.7396  6    749.793     6.03             47.93             88.82                               0.699  108.911   0.1495    4.315



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   121   0.8642  6    750.657     7.58             39.78             83.99                               0.699   98.800   0.0628    3.770

   122   1.4217  6    752.079     8.84             31.97             78.33                               0.699  119.764   0.1616    4.847

   123   1.5969  6    753.676     8.90             27.32             75.42                               0.699  108.598   0.3168    4.446

   124   1.1974  6    754.873     8.33             25.37             75.29                               0.699   68.381   0.0171    2.906

   125   2.3947  6    757.268     7.73             21.78             73.82                               0.699   99.999   0.0795    4.651

   126   3.6527  6    760.920     6.94             17.86             72.02                               0.699  119.855   0.0705    5.445

   127   5.7985  6    766.719     5.80             13.58             70.07                               0.699  132.665   0.1101    6.907

   128   7.8033  7    774.522     4.58             10.24             69.10                               0.701  114.597   0.1440    7.036

   129   9.2901  6    783.812     3.84              8.47             68.84                               0.701   90.736   0.0252    6.789

   130  18.5589  6    802.371     3.13              5.97             65.63                               0.701  107.640   0.0359   10.008

   131  34.9402 13    837.311     2.40              3.95             62.26                               0.701  103.253   0.1397   12.144

   132  32.2525  7    869.564     2.09              3.10             59.75                               0.702   57.466   0.1064    7.713

   133  44.0292  7    913.593     2.03              2.48             54.97                               0.711   49.407   0.1267    6.665

   134  55.6866  7    969.280     1.84              1.87             50.32                               0.711   46.445   0.1098    5.966

   135  75.0135  6   1044.293     1.68              1.37             44.90                               0.715   48.411   0.1039    5.975

   136  50.7068  6   1095.000     1.15              1.14             49.68                               0.762   29.536   0.0665    3.371

Time steps : 136/140, step size: 8.05147, 17.7087

simuapp          rc=0  21.56s  139/147 steps  to  1095.00 days

simumpi np=1     rc=0  20.80s  139/147 steps,  8 cuts  to  1095.00 days

simumpi np=2     rc=0  11.87s  140/145 steps,  5 cuts  to  1095.00 days

simumpi np=4     rc=0   6.75s  136/140 steps,  4 cuts  to  1095.00 days

```

![png]({{ "/assets/images/benchmark_image_57.png" | relative_url }})

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

Elapsed: 38.29s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 36.381s  95.73%      

|- Newton                                36.297s  |- 99.77%   

  |- FluxJac                             15.649s    |- 43.11% 

  |- Update                              10.964s    |- 30.21% 

  |- ScdAcc                               3.543s    |- 9.76%  

  |- Solver                               2.373s    |- 6.54%  

  |- update_dev                           2.198s    |- 6.05%  

  |- Precond                              0.623s    |- 1.72%  

  |- Residual                             0.227s    |- 0.63%  

  |- alignvar                             0.189s    |- 0.52%  

  |- HeatLoss                             0.106s    |- 0.29%  

  |- PerfJac                              0.083s    |- 0.23%  

  |- SanitizeJac                          0.054s    |- 0.15%  

|- Output                                 0.008s  |- 0.02%    

|- Logging                                0.001s  |- 0.00%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            1.622s  4.27%       

|- execution                              1.479s  |- 91.21%   

------------------------------------------------------------

TOTAL                                    38.003s

============================================================



Time steps : 4/4, step size: 0.129481, 0.0270325

Running simulation [simuapp]: scaling baseline (attempt 2/2) (OMP_NUM_THREADS=1, -novtu)

Elapsed: 38.19s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 36.427s  96.04%      

|- Newton                                36.350s  |- 99.79%   

  |- FluxJac                             15.876s    |- 43.67% 

  |- Update                              10.989s    |- 30.23% 

  |- ScdAcc                               3.487s    |- 9.59%  

  |- update_dev                           2.220s    |- 6.11%  

  |- Solver                               2.192s    |- 6.03%  

  |- Precond                              0.629s    |- 1.73%  

  |- Residual                             0.226s    |- 0.62%  

  |- alignvar                             0.193s    |- 0.53%  

  |- HeatLoss                             0.125s    |- 0.34%  

  |- PerfJac                              0.084s    |- 0.23%  

  |- SanitizeJac                          0.059s    |- 0.16%  

|- Output                                 0.008s  |- 0.02%    

|- Logging                                0.001s  |- 0.00%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            1.502s  3.96%       

|- execution                              1.369s  |- 91.17%   

------------------------------------------------------------

TOTAL                                    37.929s

============================================================



Time steps : 4/4, step size: 0.129481, 0.0270325

Running simulation [simumpi]: scaling np=1 (attempt 1/2) (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 39.86s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-20





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.61             20.31              3.30                     720.00    0.000  375.000   0.0027    0.111

     2   0.1167  1      0.217   497.90             26.53              5.06                     720.00    0.000  358.745   0.0032    0.123

     3   0.1391  2      0.356   426.17             27.46              6.05                     720.00    0.000  375.856   0.0037    0.139

     4   0.1621  3      0.518   376.49             25.96              6.45                     720.00    0.000  339.829   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129481, 0.0270325

Running simulation [simumpi]: scaling np=1 (attempt 2/2) (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 38.64s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-20





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.61             20.31              3.30                     720.00    0.000  375.000   0.0027    0.111

     2   0.1167  1      0.217   497.90             26.53              5.06                     720.00    0.000  358.745   0.0032    0.123

     3   0.1391  2      0.356   426.17             27.46              6.05                     720.00    0.000  375.856   0.0037    0.139

     4   0.1621  3      0.518   376.49             25.96              6.45                     720.00    0.000  339.829   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129481, 0.0270325

Running simulation [simumpi]: scaling np=2 (attempt 1/2) (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 20.16s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-20





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.63             20.31              3.30                     720.00    0.000  375.000   0.0027    0.111

     2   0.1167  1      0.217   497.91             26.52              5.06                     720.00    0.000  358.733   0.0032    0.123

     3   0.1391  2      0.356   426.18             27.46              6.05                     720.00    0.000  375.864   0.0037    0.139

     4   0.1621  3      0.518   376.49             25.96              6.45                     720.00    0.000  339.832   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129481, 0.0270332

Running simulation [simumpi]: scaling np=2 (attempt 2/2) (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 19.90s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-20





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.63             20.31              3.30                     720.00    0.000  375.000   0.0027    0.111

     2   0.1167  1      0.217   497.91             26.52              5.06                     720.00    0.000  358.733   0.0032    0.123

     3   0.1391  2      0.356   426.18             27.46              6.05                     720.00    0.000  375.864   0.0037    0.139

     4   0.1621  3      0.518   376.49             25.96              6.45                     720.00    0.000  339.832   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129481, 0.0270332

Running simulation [simumpi]: scaling np=4 (attempt 1/2) (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 11.55s

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-20





VTU generation is suppressed.

VTU generation is suppressed.

VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.61             20.31              3.30                     720.00    0.000  375.000   0.0027    0.111

     2   0.1167  1      0.217   497.90             26.53              5.06                     720.00    0.000  358.745   0.0032    0.123

     3   0.1391  2      0.356   426.17             27.46              6.05                     720.00    0.000  375.857   0.0037    0.139

     4   0.1621  3      0.518   376.49             25.96              6.45                     720.00    0.000  339.829   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129481, 0.0270325

Running simulation [simumpi]: scaling np=4 (attempt 2/2) (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 11.87s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-20





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.61             20.31              3.30                     720.00    0.000  375.000   0.0027    0.111

     2   0.1167  1      0.217   497.90             26.53              5.06                     720.00    0.000  358.745   0.0032    0.123

     3   0.1391  2      0.356   426.17             27.46              6.05                     720.00    0.000  375.857   0.0037    0.139

     4   0.1621  3      0.518   376.49             25.96              6.45                     720.00    0.000  339.829   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129481, 0.0270325

Running simulation [simumpi]: scaling np=8 (attempt 1/2) (OMP_NUM_THREADS=1, np=8, -novtu)

Elapsed: 9.99s



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-20





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

     1   0.1000  1      0.100   595.62             20.31              3.30                     720.00    0.000  375.000   0.0027    0.111

     2   0.1167  1      0.217   497.91             26.52              5.06                     719.99    0.000  358.759   0.0032    0.123

     3   0.1391  2      0.356   426.18             27.46              6.05                     720.00    0.000  375.848   0.0037    0.139

     4   0.1621  3      0.518   376.49             25.96              6.45                     720.00    0.000  339.825   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.12948, 0.0270316

Running simulation [simumpi]: scaling np=8 (attempt 2/2) (OMP_NUM_THREADS=1, np=8, -novtu)

Elapsed: 10.09s

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-20





VTU generation is suppressed.

VTU generation is suppressed.

VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.62             20.31              3.30                     720.00    0.000  375.000   0.0027    0.111

     2   0.1167  1      0.217   497.91             26.52              5.06                     719.99    0.000  358.759   0.0032    0.123

     3   0.1391  2      0.356   426.18             27.46              6.05                     720.00    0.000  375.848   0.0037    0.139

     4   0.1621  3      0.518   376.49             25.96              6.45                     720.00    0.000  339.825   0.0034    0.151





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.12948, 0.0270316

```

![png]({{ "/assets/images/benchmark_image_58.png" | relative_url }})

```
   config  steps   seconds   speedup   effic.  cells/rank   ghosts

  simuapp      4     37.93         -        -           -        -

     np=1      4     35.84     1.00x     100%      202005        0

     np=2      4     18.04     1.99x      99%      101080     2110

     np=4      4     10.02     3.58x      89%       50520     4235

     np=8      4      8.04     4.46x      56%       25610     8325 *

  * more ranks than the 4 fast cores on this CPU - paced by the slow ones, so read the efficiency as the machine's, not the partition's

```

```
Script completed at: 2026-11-21 05:56:11

```
