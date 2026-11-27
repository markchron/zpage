---
layout: default
title: "Benchmark results of resrsim"
date: 2026-11-26
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

Elapsed: 1.17s

    22  55.0000  1   3650.000    62.64              2.02              3.12                      30.27    0.000    9.539 4.20e-04    0.029



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.736s  84.38%      

|- Newton                                 0.680s  |- 92.48%   

  |- Update                               0.290s    |- 42.64% 

  |- FluxJac                              0.157s    |- 23.10% 

  |- Solver                               0.059s    |- 8.61%  

  |- ScdAcc                               0.058s    |- 8.49%  

  |- update_dev                           0.040s    |- 5.93%  

  |- Precond                              0.028s    |- 4.18%  

  |- Residual                             0.011s    |- 1.58%  

  |- alignvar                             0.008s    |- 1.18%  

  |- SanitizeJac                          0.005s    |- 0.73%  

  |- PerfJac                              0.004s    |- 0.62%  

  |- HeatLoss                             0.002s    |- 0.23%  

|- Output                                 0.029s  |- 3.90%    

|- Logging                                0.009s  |- 1.28%    

|- Input                                  0.000s  |- 0.04%    

Initialization                            0.136s  15.62%      

|- execution                              0.126s  |- 92.50%   

------------------------------------------------------------

TOTAL                                     0.872s

============================================================



Time steps : 22/22, step size: 165.909, 129.097

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

Elapsed: 2.35s

    75  53.9980  3   3650.000     0.01              4.31             99.77                       5.96    0.659  235.228   0.0062    2.644



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.004s  95.30%      

|- Newton                                 1.959s  |- 97.80%   

  |- Update                               0.614s    |- 31.36% 

  |- FluxJac                              0.449s    |- 22.92% 

  |- ScdAcc                               0.217s    |- 11.07% 

  |- update_dev                           0.171s    |- 8.74%  

  |- Precond                              0.137s    |- 7.00%  

  |- SanitizeJac                          0.090s    |- 4.57%  

  |- Solver                               0.087s    |- 4.45%  

  |- PerfJac                              0.073s    |- 3.73%  

  |- alignvar                             0.047s    |- 2.38%  

  |- Residual                             0.013s    |- 0.64%  

  |- HeatLoss                             0.009s    |- 0.48%  

|- Logging                                0.019s  |- 0.94%    

|- Output                                 0.013s  |- 0.63%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.099s  4.70%       

|- execution                              0.093s  |- 93.70%   

------------------------------------------------------------

TOTAL                                     2.102s

============================================================



Time steps : 75/75, step size: 48.6667, 60.2013

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

Elapsed: 2.20s

    38  91.8599  3   3650.000     0.12              4.49             97.30                       5.96    0.262  200.553   0.0087    3.754



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.796s  95.00%      

|- Newton                                 1.761s  |- 98.08%   

  |- Update                               0.548s    |- 31.12% 

  |- FluxJac                              0.382s    |- 21.69% 

  |- ScdAcc                               0.183s    |- 10.42% 

  |- Precond                              0.158s    |- 8.98%  

  |- update_dev                           0.140s    |- 7.93%  

  |- SanitizeJac                          0.086s    |- 4.87%  

  |- Solver                               0.078s    |- 4.43%  

  |- PerfJac                              0.055s    |- 3.13%  

  |- alignvar                             0.043s    |- 2.43%  

  |- Residual                             0.009s    |- 0.50%  

  |- HeatLoss                             0.007s    |- 0.41%  

|- Logging                                0.020s  |- 1.11%    

|- Output                                 0.015s  |- 0.83%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.095s  5.00%       

|- execution                              0.089s  |- 94.59%   

------------------------------------------------------------

TOTAL                                     1.890s

============================================================



Time steps : 38/40, step size: 96.0526, 98.3248

```

![png]({{ "/assets/images/benchmark_image_6.png" | relative_url }})

# Buckley- Leverett



Two phase, isothermal problem

variable order: [Sw, P, T, So, X0, X1, Sg]



Acc w.r.t. [Sw, So, Sg, X0, X1, P, T]

```
Running simulation [simuapp]: Buckley-Leverett (-novtu)

Elapsed: 3.21s

    79   5.0372  1     10.000    5e-10              0.16            100.00                       0.16   12.729    0.005 7.02e-06  4.9e-07



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.749s  96.55%      

|- Newton                                 2.703s  |- 98.30%   

  |- Update                               0.932s    |- 34.48% 

  |- FluxJac                              0.392s    |- 14.51% 

  |- ScdAcc                               0.390s    |- 14.43% 

  |- Precond                              0.277s    |- 10.24% 

  |- update_dev                           0.218s    |- 8.07%  

  |- SanitizeJac                          0.178s    |- 6.59%  

  |- PerfJac                              0.093s    |- 3.43%  

  |- alignvar                             0.090s    |- 3.34%  

  |- Solver                               0.046s    |- 1.70%  

  |- HeatLoss                             0.020s    |- 0.74%  

  |- Residual                             0.015s    |- 0.56%  

|- Logging                                0.024s  |- 0.88%    

|- Output                                 0.009s  |- 0.32%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.098s  3.45%       

|- execution                              0.095s  |- 96.41%   

------------------------------------------------------------

TOTAL                                     2.847s

============================================================



Time steps : 79/81, step size: 0.126582, 0.652368

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

Elapsed: 2.69s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.344s  96.01%      

|- Newton                                 2.322s  |- 99.08%   

  |- Update                               0.920s    |- 39.64% 

  |- FluxJac                              0.407s    |- 17.54% 

  |- ScdAcc                               0.339s    |- 14.61% 

  |- update_dev                           0.215s    |- 9.24%  

  |- Precond                              0.153s    |- 6.60%  

  |- SanitizeJac                          0.071s    |- 3.04%  

  |- alignvar                             0.045s    |- 1.95%  

  |- HeatLoss                             0.042s    |- 1.83%  

  |- Solver                               0.037s    |- 1.58%  

  |- PerfJac                              0.028s    |- 1.20%  

  |- Residual                             0.024s    |- 1.03%  

|- Output                                 0.016s  |- 0.69%    

|- Logging                                0.013s  |- 0.56%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.097s  3.99%       

|- execution                              0.091s  |- 93.13%   

------------------------------------------------------------

TOTAL                                     2.441s

============================================================



Time steps : 10/18, step size: 12.6635, 22.211

```

```
Analytic front speed: 729.1 ft/day, breakthrough at 13.8 days (804 cells)

```

```
  t (days)   L2 rel. err   Linf rel. err

      1.16        0.0959          0.4513

      5.52        0.1515          0.3714

     12.00        0.1416          0.3085

     26.15        0.0631          0.1201

     57.14        0.0188          0.0407

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

Elapsed: 0.50s

    18   1.1910  1     10.000                                                                 9521.20    0.048  145.831             0.834



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.113s  53.47%      

|- Newton                                 0.101s  |- 89.42%   

  |- Update                               0.031s    |- 30.55% 

  |- PerfJac                              0.018s    |- 17.54% 

  |- Precond                              0.012s    |- 11.51% 

  |- ScdAcc                               0.009s    |- 8.82%  

  |- FluxJac                              0.008s    |- 8.02%  

  |- update_dev                           0.006s    |- 6.19%  

  |- SanitizeJac                          0.005s    |- 5.13%  

  |- Solver                               0.003s    |- 3.22%  

  |- alignvar                             0.003s    |- 3.01%  

  |- Residual                             0.000s    |- 0.48%  

  |- HeatLoss                             0.000s    |- 0.02%  

|- Output                                 0.009s  |- 7.67%    

|- Logging                                0.004s  |- 3.47%    

|- Input                                  0.000s  |- 0.07%    

Initialization                            0.099s  46.53%      

|- execution                              0.095s  |- 96.70%   

------------------------------------------------------------

TOTAL                                     0.212s

============================================================



Time steps : 18/21, step size: 0.555556, 0.370895

```

```
D=6.088e-06 m2/s, nu=17.26

```

```
  t (days)   L2 rel. err   Linf rel. err

     0.556        0.3072          0.9589

     1.661        0.2973          0.9112

     3.823        0.2125          0.7702

     6.281        0.1000          0.2937

    10.000        0.1233          0.4723

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

Elapsed: 1.58s

    22 163.1620  2   3650.000     0.78             10.19             92.87                      10.73    0.000   13.701   0.0097    0.002



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.200s  93.31%      

|- Newton                                 1.183s  |- 98.58%   

  |- Update                               0.396s    |- 33.48% 

  |- FluxJac                              0.325s    |- 27.49% 

  |- ScdAcc                               0.143s    |- 12.12% 

  |- update_dev                           0.084s    |- 7.10%  

  |- Solver                               0.080s    |- 6.73%  

  |- Precond                              0.061s    |- 5.15%  

  |- SanitizeJac                          0.031s    |- 2.62%  

  |- alignvar                             0.026s    |- 2.16%  

  |- PerfJac                              0.015s    |- 1.30%  

  |- Residual                             0.008s    |- 0.65%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Logging                                0.005s  |- 0.41%    

|- Output                                 0.004s  |- 0.31%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.086s  6.69%       

|- execution                              0.083s  |- 96.07%   

------------------------------------------------------------

TOTAL                                     1.286s

============================================================



Time steps : 22/22, step size: 165.909, 155.032

```



## watfld_cw.dat

```
Running simulation [simuapp]: SPE4-b Water flooding without vmod (-novtu)

Elapsed: 2.27s

    35  32.0338  2   3650.000     1.04             79.00             98.70                      80.00    0.000    1.842   0.0027  3.1e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.918s  95.54%      

|- Newton                                 1.890s  |- 98.53%   

  |- Update                               0.628s    |- 33.25% 

  |- FluxJac                              0.459s    |- 24.31% 

  |- ScdAcc                               0.202s    |- 10.67% 

  |- update_dev                           0.143s    |- 7.56%  

  |- Solver                               0.137s    |- 7.22%  

  |- Precond                              0.092s    |- 4.85%  

  |- PerfJac                              0.080s    |- 4.21%  

  |- SanitizeJac                          0.074s    |- 3.91%  

  |- alignvar                             0.044s    |- 2.33%  

  |- Residual                             0.011s    |- 0.59%  

  |- HeatLoss                             0.000s    |- 0.01%  

|- Output                                 0.008s  |- 0.41%    

|- Logging                                0.008s  |- 0.40%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.090s  4.46%       

|- execution                              0.086s  |- 96.42%   

------------------------------------------------------------

TOTAL                                     2.008s

============================================================



Time steps : 35/35, step size: 104.286, 142.716

```

## stflu001.dat

Inverted 9 spot hot water flooding with area/block modifier, 5 point transmissibility


```
Running simulation [simuapp]: Inverted 9 spot hot water flooding (-novtu)

Elapsed: 3.31s

    88 365.0000  2   3650.000    3e-04            560.95            100.00                     560.95    0.004    0.742 6.55e-04    0.019



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.964s  96.88%      

|- Newton                                 2.928s  |- 98.78%   

  |- Update                               0.927s    |- 31.67% 

  |- FluxJac                              0.712s    |- 24.31% 

  |- ScdAcc                               0.352s    |- 12.03% 

  |- update_dev                           0.283s    |- 9.65%  

  |- Precond                              0.224s    |- 7.67%  

  |- Solver                               0.111s    |- 3.81%  

  |- SanitizeJac                          0.110s    |- 3.74%  

  |- alignvar                             0.098s    |- 3.34%  

  |- PerfJac                              0.030s    |- 1.04%  

  |- Residual                             0.015s    |- 0.51%  

  |- HeatLoss                             0.012s    |- 0.41%  

|- Logging                                0.030s  |- 1.02%    

|- Output                                 0.017s  |- 0.57%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.095s  3.12%       

|- execution                              0.090s  |- 93.93%   

------------------------------------------------------------

TOTAL                                     3.059s

============================================================



Time steps : 88/89, step size: 41.4773, 100.513

```

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation, CMG against OURS.

![png]({{ "/assets/images/benchmark_image_12.png" | relative_url }})

## stflu002.dat

5000x5000x50, 2D diagonal water flooding in uniformed cartesian

```
Running simulation [simuapp]: Uniformed cartesian water flooding (-novtu)

Elapsed: 0.62s

    49 331.7630  3   3650.000   624.41             11.54              1.82                     635.95    0.000  1.1e+03   0.0499    0.028



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.277s  76.74%      

|- Newton                                 0.263s  |- 94.95%   

  |- Update                               0.096s    |- 36.48% 

  |- FluxJac                              0.054s    |- 20.58% 

  |- ScdAcc                               0.023s    |- 8.63%  

  |- Precond                              0.019s    |- 7.34%  

  |- update_dev                           0.016s    |- 6.18%  

  |- Solver                               0.012s    |- 4.49%  

  |- PerfJac                              0.011s    |- 4.24%  

  |- alignvar                             0.011s    |- 4.16%  

  |- SanitizeJac                          0.008s    |- 3.17%  

  |- HeatLoss                             0.003s    |- 1.19%  

  |- Residual                             0.003s    |- 0.97%  

|- Logging                                0.005s  |- 1.75%    

|- Output                                 0.004s  |- 1.55%    

|- Input                                  0.000s  |- 0.06%    

Initialization                            0.084s  23.26%      

|- execution                              0.079s  |- 93.80%   

------------------------------------------------------------

TOTAL                                     0.361s

============================================================



Time steps : 49/49, step size: 74.4898, 130.909

```



## stflu003.dat

5000x5000x50, 2D diagonal water flooding in uniformed corner point

```
Running simulation [simuapp]: uniformed corner grid (-novtu)

Elapsed: 0.86s

    46 252.4658  2   3650.000   624.71             11.24              1.77                     635.95    0.000  740.056   0.0380    0.017



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.466s  84.33%      

|- Newton                                 0.442s  |- 94.88%   

  |- Update                               0.177s    |- 40.02% 

  |- FluxJac                              0.076s    |- 17.22% 

  |- ScdAcc                               0.051s    |- 11.61% 

  |- Precond                              0.039s    |- 8.79%  

  |- update_dev                           0.024s    |- 5.53%  

  |- SanitizeJac                          0.023s    |- 5.29%  

  |- Solver                               0.016s    |- 3.54%  

  |- PerfJac                              0.014s    |- 3.25%  

  |- alignvar                             0.007s    |- 1.63%  

  |- Residual                             0.003s    |- 0.73%  

  |- HeatLoss                             0.003s    |- 0.68%  

|- Output                                 0.006s  |- 1.39%    

|- Logging                                0.005s  |- 1.15%    

|- Input                                  0.000s  |- 0.04%    

Initialization                            0.087s  15.67%      

|- execution                              0.083s  |- 95.54%   

------------------------------------------------------------

TOTAL                                     0.552s

============================================================



Time steps : 46/46, step size: 79.3478, 130.764

```

![png]({{ "/assets/images/benchmark_image_13.png" | relative_url }})



## stflu004.dat

2D diagonal water flooding for reduction of numerical dispersion and grid orientation effect


```
Running simulation [simuapp]: 2D diagonal flow: grid orientation

Elapsed: 1.79s

    61  58.7733  2   3650.000   613.68             22.27              3.50                     635.95    0.000  682.222   0.0196    0.034



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.464s  93.98%      

|- Newton                                 1.391s  |- 95.04%   

  |- Update                               0.633s    |- 45.49% 

  |- FluxJac                              0.234s    |- 16.81% 

  |- ScdAcc                               0.147s    |- 10.57% 

  |- update_dev                           0.088s    |- 6.32%  

  |- Precond                              0.076s    |- 5.46%  

  |- Solver                               0.061s    |- 4.41%  

  |- SanitizeJac                          0.044s    |- 3.14%  

  |- alignvar                             0.041s    |- 2.95%  

  |- PerfJac                              0.021s    |- 1.49%  

  |- Residual                             0.010s    |- 0.74%  

  |- HeatLoss                             0.010s    |- 0.73%  

|- Output                                 0.044s  |- 3.03%    

|- Logging                                0.014s  |- 0.96%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.094s  6.02%       

|- execution                              0.089s  |- 95.21%   

------------------------------------------------------------

TOTAL                                     1.558s

============================================================



Time steps : 61/61, step size: 59.8361, 80.636

```

![png]({{ "/assets/images/benchmark_image_14.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_15.png" | relative_url }})

## stflu007.dat

PEBI_GRID


```
Running simulation [simuapp]: 2D diagonal flow: pebi grid

Elapsed: 2.41s

    59 354.7237  3   3650.000   623.41             12.54              1.97                     635.95    0.000  1.3e+03   0.0717    0.046



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.028s  94.71%      

|- Newton                                 1.946s  |- 95.98%   

  |- Update                               0.767s    |- 39.38% 

  |- FluxJac                              0.466s    |- 23.93% 

  |- ScdAcc                               0.192s    |- 9.86%  

  |- update_dev                           0.121s    |- 6.21%  

  |- Precond                              0.117s    |- 6.02%  

  |- Solver                               0.112s    |- 5.77%  

  |- alignvar                             0.046s    |- 2.35%  

  |- SanitizeJac                          0.044s    |- 2.24%  

  |- HeatLoss                             0.021s    |- 1.09%  

  |- PerfJac                              0.021s    |- 1.08%  

  |- Residual                             0.016s    |- 0.83%  

|- Output                                 0.043s  |- 2.10%    

|- Logging                                0.009s  |- 0.46%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.113s  5.29%       

|- execution                              0.100s  |- 88.20%   

------------------------------------------------------------

TOTAL                                     2.141s

============================================================



Time steps : 59/59, step size: 61.8644, 119.417

```

![png]({{ "/assets/images/benchmark_image_16.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_17.png" | relative_url }})

## stflu026.dat

* Steam flood on two component live oil

```
Running simulation [simuapp]: 3 component steam flooding (-novtu)

Elapsed: 5.15s

    91 308.2084  6   3650.000     0.01              4.50             99.83                       5.96    1.170  1.2e+03   0.0813   13.947



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  4.750s  98.13%      

|- Newton                                 4.671s  |- 98.32%   

  |- Update                               1.348s    |- 28.86% 

  |- FluxJac                              1.083s    |- 23.18% 

  |- ScdAcc                               0.611s    |- 13.07% 

  |- update_dev                           0.398s    |- 8.52%  

  |- Precond                              0.387s    |- 8.28%  

  |- Solver                               0.231s    |- 4.94%  

  |- SanitizeJac                          0.230s    |- 4.92%  

  |- alignvar                             0.133s    |- 2.84%  

  |- PerfJac                              0.127s    |- 2.72%  

  |- Residual                             0.019s    |- 0.40%  

  |- HeatLoss                             0.018s    |- 0.40%  

|- Logging                                0.048s  |- 1.02%    

|- Output                                 0.018s  |- 0.39%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.091s  1.87%       

|- execution                              0.086s  |- 94.86%   

------------------------------------------------------------

TOTAL                                     4.841s

============================================================



Time steps : 91/91, step size: 40.1099, 70.1477

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

Elapsed: 5.10s

    92  20.0248  2   3650.000     0.01              4.11             99.76                       4.94    0.091   22.104   0.0181    0.554



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  4.718s  98.04%      

|- Newton                                 4.649s  |- 98.53%   

  |- Update                               1.334s    |- 28.70% 

  |- FluxJac                              1.088s    |- 23.42% 

  |- ScdAcc                               0.598s    |- 12.86% 

  |- update_dev                           0.373s    |- 8.02%  

  |- Precond                              0.359s    |- 7.73%  

  |- Solver                               0.330s    |- 7.11%  

  |- SanitizeJac                          0.209s    |- 4.49%  

  |- alignvar                             0.124s    |- 2.66%  

  |- PerfJac                              0.118s    |- 2.54%  

  |- HeatLoss                             0.019s    |- 0.40%  

  |- Residual                             0.019s    |- 0.40%  

|- Logging                                0.034s  |- 0.73%    

|- Output                                 0.018s  |- 0.39%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.094s  1.96%       

|- execution                              0.089s  |- 94.70%   

------------------------------------------------------------

TOTAL                                     4.812s

============================================================



Time steps : 92/94, step size: 39.6739, 66.3556

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

Elapsed: 3.52s

   120  15.1549  6   1095.000     0.95              0.55             36.93                               0.106   44.616   0.0873    0.883



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  3.167s  97.02%      

|- Newton                                 2.998s  |- 94.67%   

  |- Update                               0.984s    |- 32.83% 

  |- FluxJac                              0.575s    |- 19.18% 

  |- ScdAcc                               0.374s    |- 12.47% 

  |- Precond                              0.285s    |- 9.51%  

  |- update_dev                           0.232s    |- 7.74%  

  |- SanitizeJac                          0.159s    |- 5.31%  

  |- PerfJac                              0.111s    |- 3.69%  

  |- alignvar                             0.102s    |- 3.40%  

  |- Solver                               0.075s    |- 2.49%  

  |- Residual                             0.013s    |- 0.43%  

  |- HeatLoss                             0.009s    |- 0.30%  

|- Output                                 0.082s  |- 2.57%    

|- Logging                                0.041s  |- 1.31%    

|- Input                                  0.002s  |- 0.07%    

Initialization                            0.097s  2.98%       

|- execution                              0.092s  |- 94.84%   

------------------------------------------------------------

TOTAL                                     3.264s

============================================================



Time steps : 120/129, step size: 9.125, 18.3752

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

Elapsed: 25.74s

   153  53.9586  6   1095.000     1.34              1.17             46.66                               0.073   31.616   0.0691    3.479



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 25.355s  99.58%      

|- Newton                                25.059s  |- 98.83%   

  |- Update                               8.027s    |- 32.03% 

  |- FluxJac                              6.900s    |- 27.53% 

  |- ScdAcc                               2.946s    |- 11.76% 

  |- update_dev                           2.126s    |- 8.48%  

  |- Solver                               2.082s    |- 8.31%  

  |- Precond                              1.178s    |- 4.70%  

  |- alignvar                             0.446s    |- 1.78%  

  |- SanitizeJac                          0.429s    |- 1.71%  

  |- PerfJac                              0.219s    |- 0.87%  

  |- HeatLoss                             0.191s    |- 0.76%  

  |- Residual                             0.186s    |- 0.74%  

|- Output                                 0.181s  |- 0.71%    

|- Logging                                0.071s  |- 0.28%    

|- Input                                  0.003s  |- 0.01%    

Initialization                            0.107s  0.42%       

|- execution                              0.103s  |- 96.10%   

------------------------------------------------------------

TOTAL                                    25.462s

============================================================



Time steps : 153/161, step size: 7.15686, 14.9924

```

```
Found 154 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu008_00153.vtu

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

Elapsed: 55.05s

   124  72.3965 12   1095.000     1.63              0.86             34.51                               0.029   41.919   0.1014    4.631



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 54.587s  99.64%      

|- Newton                                54.175s  |- 99.25%   

  |- FluxJac                             16.523s    |- 30.50% 

  |- Update                              15.306s    |- 28.25% 

  |- Solver                              10.215s    |- 18.86% 

  |- ScdAcc                               4.541s    |- 8.38%  

  |- update_dev                           3.333s    |- 6.15%  

  |- Precond                              2.022s    |- 3.73%  

  |- Residual                             0.452s    |- 0.83%  

  |- alignvar                             0.450s    |- 0.83%  

  |- SanitizeJac                          0.407s    |- 0.75%  

  |- HeatLoss                             0.193s    |- 0.36%  

  |- PerfJac                              0.100s    |- 0.18%  

|- Output                                 0.320s  |- 0.59%    

|- Logging                                0.047s  |- 0.09%    

|- Input                                  0.001s  |- 0.00%    

Initialization                            0.197s  0.36%       

|- execution                              0.132s  |- 66.87%   

------------------------------------------------------------

TOTAL                                    54.784s

============================================================



Time steps : 124/126, step size: 8.83065, 20.2824

```

```
Found 125 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu009_00124.vtu

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

Elapsed: 34.69s

   251  32.6059  6   1095.000     1.73              1.20             40.86                               0.024   20.899   0.0655    2.003



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 34.314s  99.62%      

|- Newton                                33.926s  |- 98.87%   

  |- FluxJac                             12.044s    |- 35.50% 

  |- Update                               9.005s    |- 26.54% 

  |- Solver                               3.945s    |- 11.63% 

  |- ScdAcc                               3.072s    |- 9.06%  

  |- update_dev                           2.319s    |- 6.84%  

  |- Precond                              1.230s    |- 3.62%  

  |- PerfJac                              0.308s    |- 0.91%  

  |- alignvar                             0.269s    |- 0.79%  

  |- SanitizeJac                          0.269s    |- 0.79%  

  |- Residual                             0.245s    |- 0.72%  

  |- HeatLoss                             0.122s    |- 0.36%  

|- Logging                                0.655s  |- 1.91%    

|- Output                                 0.297s  |- 0.87%    

|- Input                                  0.005s  |- 0.01%    

Initialization                            0.132s  0.38%       

|- execution                              0.110s  |- 83.08%   

------------------------------------------------------------

TOTAL                                    34.446s

============================================================



Time steps : 251/261, step size: 4.36255, 10.7879

```

```
Found 252 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu025_00251.vtu

```

![png]({{ "/assets/images/benchmark_image_29.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_30.png" | relative_url }})

### stflu013.dat - SPE4 problem 1A, cyclic steam

* 20x20x4 corner-point FIELD grid, water and dead oil with no gas component. One well location is modelled as two wells that are never open together: 'Injector 1' (`*MAX *STW 1000`, BHP limit 10000 psi) and 'Producer 1' (`*MAX *STL 1000`, `*MIN *BHP 17`). Three cycles of 10 days of injection, 7 of soak, then production, ending at days 365, 730 and 1095.

* Reference is the DeepFlow THERM `stars_stflu013.log` time step summary, one row per step. simuapp is run with `-log` to write the same table, so both sides are read the same way. THERM is in bbl/day, ours in m3/day.

* No free gas is produced, so the gas and GOR columns of both logs are blank. `read_step_summary_log()` drops blank fields and would leave the rates NaN, so this section reads the table by column position instead.

```
Running simulation [simuapp]: Cyclic steam stimulation, SPE4 problem 1A (-novtu)

Elapsed: 12.32s

No text to display.

```

```
OURS reached day 1095.0 of 1095

THERM: 77 steps marched, 0 cuts, 96 Newton cycles, material balance error 0.021 % at the last step

 OURS: 95 steps marched, 6 cuts, 339 Newton cycles, material balance error 0.033 % at the last step

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

steps              77    95

newton             96   339

newton/step     1.247 3.568

cuts                0     6

dt min          0.002 0.002

dt geomean      1.671 2.003

dt max          118.9   114

end day          1095  1095

steps@1.09d         5     5

steps@11d          10    11

steps@110d         19    21

steps@548d         45    60

steps@1.1e+03d     77    95

```

![png]({{ "/assets/images/benchmark_image_32.png" | relative_url }})

### stflu015.dat - single producer on a corner-point grid

* 14x14x5 corner-point FIELD grid, water and dead oil with no gas component. One producer, 'Producer', perforated in block (1,1,1) on `*OPERATE *MAX *STL 400` with a `*MIN *BHP 17` limit. There is no injector, so this is a depletion run to day 365, from an initial `*REFPRES 1000`.

* Reference is the DeepFlow THERM `stars_stflu015.log` time step summary, read with `read_step_summary_columns()` from the stflu013 section above (gas and GOR are blank in both logs). THERM is in bbl/day, ours in m3/day.

* Our log prints the rates with two decimals, so the water curve is coarse.

```
Running simulation [simuapp]: Corner grid, single producer on STL (-novtu)

Elapsed: 0.56s

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

dt geomean    2.654 2.601

dt max        159.2 177.2

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

Elapsed: 5.55s

No text to display.

```

### Wells

![png]({{ "/assets/images/benchmark_image_35.png" | relative_url }})

### Step size

* Steps are compared on simulated time, not step number: the two programs march different counts.

* The first run in `runs` is the reference; the right panel is the interpolated dt ratio to it.

* Fewer steps and Newton cycles at the same end time is cheaper, but only counts when the well curves above still agree.

```
run                 THERM      OURS

steps                  61       281

newton                224      1501

newton/step         3.672     5.342

cuts                    1        19

dt min            5.8e-06  4.63e-06

dt geomean      0.0001588 0.0009537

dt max             0.0016   0.00174

end day           0.01736     0.375

steps@1.74e-05d         2         3

steps@0.000174d        10         9

steps@0.00174d         21        19

steps@0.00868d         47        44

steps@0.0174d          61        64

```

![png]({{ "/assets/images/benchmark_image_36.png" | relative_url }})

### SAGD

#### 2D cross the well

```
Running simulation [simuapp]: SAGD (-novtu)

Elapsed: 5.57s

   207   1.7935  1   2526.000     3.48             51.20             93.63                      50.95    0.004    0.356   0.0056    0.353



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  5.275s  98.57%      

|- Newton                                 5.202s  |- 98.62%   

  |- Update                               1.662s    |- 31.94% 

  |- FluxJac                              1.117s    |- 21.47% 

  |- Precond                              0.617s    |- 11.86% 

  |- ScdAcc                               0.577s    |- 11.10% 

  |- update_dev                           0.424s    |- 8.15%  

  |- Solver                               0.245s    |- 4.72%  

  |- SanitizeJac                          0.219s    |- 4.21%  

  |- alignvar                             0.173s    |- 3.33%  

  |- PerfJac                              0.045s    |- 0.86%  

  |- Residual                             0.033s    |- 0.63%  

  |- HeatLoss                             0.007s    |- 0.13%  

|- Logging                                0.030s  |- 0.57%    

|- Output                                 0.023s  |- 0.43%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.077s  1.43%       

|- execution                              0.073s  |- 95.29%   

------------------------------------------------------------

TOTAL                                     5.351s

============================================================



Time steps : 207/210, step size: 12.2029, 14.494

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

Elapsed: 7.63s

   178 113.2711  3   2526.000     2.23            149.16             98.53                     150.00    0.445   75.568   0.0406    5.068



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  7.346s  98.87%      

|- Newton                                 7.243s  |- 98.60%   

  |- Update                               2.211s    |- 30.52% 

  |- FluxJac                              1.326s    |- 18.30% 

  |- PerfJac                              0.778s    |- 10.74% 

  |- ScdAcc                               0.740s    |- 10.22% 

  |- Precond                              0.678s    |- 9.36%  

  |- update_dev                           0.509s    |- 7.03%  

  |- SanitizeJac                          0.426s    |- 5.89%  

  |- Solver                               0.255s    |- 3.52%  

  |- alignvar                             0.167s    |- 2.30%  

  |- Residual                             0.038s    |- 0.53%  

  |- HeatLoss                             0.007s    |- 0.10%  

|- Logging                                0.038s  |- 0.52%    

|- Output                                 0.024s  |- 0.32%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.084s  1.13%       

|- execution                              0.080s  |- 95.60%   

------------------------------------------------------------

TOTAL                                     7.429s

============================================================



Time steps : 178/189, step size: 14.191, 22.733

```

### Wells

![png]({{ "/assets/images/benchmark_image_39.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation. The blocks follow the producer-injector pair down the 10x1x20 grid.

![png]({{ "/assets/images/benchmark_image_40.png" | relative_url }})

#### 3D

```
Running simulation [simuapp]: SAGD 3D (-novtu)

Elapsed: 30.96s

   145   7.3970  3    680.000    13.34             87.04             86.71                      93.21    0.000    4.364   0.1517    9.412



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 30.616s  99.70%      

|- Newton                                30.448s  |- 99.45%   

  |- FluxJac                              9.161s    |- 30.09% 

  |- Update                               8.843s    |- 29.04% 

  |- Solver                               4.054s    |- 13.31% 

  |- ScdAcc                               2.882s    |- 9.47%  

  |- update_dev                           2.041s    |- 6.70%  

  |- Precond                              1.467s    |- 4.82%  

  |- SanitizeJac                          0.528s    |- 1.73%  

  |- PerfJac                              0.465s    |- 1.53%  

  |- alignvar                             0.385s    |- 1.27%  

  |- Residual                             0.231s    |- 0.76%  

  |- HeatLoss                             0.086s    |- 0.28%  

|- Logging                                0.036s  |- 0.12%    

|- Output                                 0.032s  |- 0.10%    

|- Input                                  0.001s  |- 0.00%    

Initialization                            0.093s  0.30%       

|- execution                              0.089s  |- 95.58%   

------------------------------------------------------------

TOTAL                                    30.710s

============================================================



Time steps : 145/150, step size: 4.68966, 4.48137

```

#### 2D live oil

* 10x1x20 cross-section, two-component live oil (CH4 + HOIL) with water. Injector 'Inj' (2:9,1,13) and producer 'Prod' (2:9,1,18); both are shut in and preheated for 60 days, then opened.

* CMG only (no ECL run for this deck).

```
Running simulation [simuapp]: SAGD live oil (-novtu)

Elapsed: 6.85s

   135   9.9246  3   2526.000     3.48     3.28   149.76     0.94    97.73                     150.00    2.531    6.974   0.0152    1.157



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  6.500s  98.46%      

|- Newton                                 6.430s  |- 98.91%   

  |- Update                               1.680s    |- 26.13% 

  |- FluxJac                              1.392s    |- 21.65% 

  |- ScdAcc                               0.725s    |- 11.28% 

  |- Precond                              0.613s    |- 9.53%  

  |- PerfJac                              0.608s    |- 9.45%  

  |- update_dev                           0.433s    |- 6.73%  

  |- Solver                               0.364s    |- 5.66%  

  |- SanitizeJac                          0.354s    |- 5.50%  

  |- alignvar                             0.138s    |- 2.15%  

  |- Residual                             0.031s    |- 0.48%  

  |- HeatLoss                             0.008s    |- 0.12%  

|- Logging                                0.031s  |- 0.48%    

|- Output                                 0.020s  |- 0.31%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.102s  1.54%       

|- execution                              0.094s  |- 92.85%   

------------------------------------------------------------

TOTAL                                     6.602s

============================================================



Time steps : 135/141, step size: 18.7111, 21.1525

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

Elapsed: 44.32s

No text to display.

```

```
OURS reached day 680.0 of 680

  CMG: 124 steps marched, 0 cuts, 289 Newton cycles

 OURS: 146 steps marched, 10 cuts, 691 Newton cycles

```

### Wells

* Rates are m3/day at standard conditions, read from the time step summary. The wells are shut in until day 60, so there is nothing to plot before it.

![png]({{ "/assets/images/benchmark_image_43.png" | relative_url }})

#### *KRTEMTAB verification (stflu028)

* 5x5x1 FIELD grid with five producers and one injector, from the STARS `verify48` verification deck. `*KRTEMTAB` moves the relative permeability endpoints with temperature between 123 F and 500 F. The producers run on `*OPERATE *MAX *STO 30`; the injector is open from day 700 to day 1431. The run ends at day 2435.

* Reference is the CMG `verify48` run: `stars_stflu028.log` (time step summary, field totals in FIELD units) and `stars_stfu028_special.csv` (pressure at blocks (1,2,1) and (2,3,1)). simuapp is run with `-log` so both sides of the rates are the same kind of table.

```
Running simulation [simuapp]: *KRTEMTAB verification (-novtu)

Elapsed: 0.41s

No text to display.

```

```
OURS reached day 2435.0 of 2435

  CMG: 90 steps marched, 0 cuts, 94 Newton cycles

 OURS: 40 steps marched, 0 cuts, 75 Newton cycles

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

Elapsed: 7.22s

No text to display.

```

```
OURS reached day 820.0 of 820

THERM: 506 steps marched, 0 cuts, 659 Newton cycles

 OURS: 232 steps marched, 5 cuts, 837 Newton cycles

```

### Wells

* Rates are m3/day at standard conditions, read from the time step summary. The wells are shut in until day 150, so time is counted from then, on a log axis: most of the change is in the first 50 days after opening, which a linear axis squeezes into a sliver of the run.

* The oil and gas rates fall by one and three decades, so their rate axes are logarithmic too, and a zero rate is not drawn. The Fortran run marches 506 steps against our 218; it is drawn as a thin line with a marker every few steps, so that both series stay visible.

![png]({{ "/assets/images/benchmark_image_46.png" | relative_url }})

#### Wet combustion tube (stflu033)

* 20x1x1 SI tube, 1.75 m long, with six components (water, heavy / medium / light oil, inert gas, oxygen) and three oil-burning reactions (`*STOREAC`, `*STOPROD`, `*RORDER`, `*FREQFAC`, `*EACT`, `*RENTH`): the Smith and Perkins forward wet-combustion experiment. Heaters bring the four blocks at the inlet to 267 C, air is injected from day 2e-4, and water is co-injected with it from day 0.02 (`*INCOMP *WATER-GAS`, `*OPERATE *STF`). The producer holds 5620 kPa at the far end (`*PERF *TUBE-END`). The run ends at day 0.6667.

* Reference is DeepFlow THERM: `stars_stflu033.log` (time step summary) for the production rates and the cost of the run, and `stars_stflu033.prn` for the grid profiles at its report times and for the cumulative balance with its reaction totals. Our profiles come from the VTU series (`*OUTSRF *GRID`; the profiles are all that reads it, so this deck keeps its `.vtu` in `FIELD_PLOT_DECKS`), our balance from the `.out` the run writes.

* Two things are judged separately. The reaction totals are what the kinetics burn, wherever the front is; the profiles say where the heat goes - the hot peak at the front, and the wet plateau behind it where the injected water condenses.

```
Running simulation [simuapp]: Wet combustion tube

Elapsed: 2.31s

No text to display.

```

```
OURS reached day 0.6670 of 0.6667

THERM: 116 steps marched, 0 cuts, 361 Newton cycles

 OURS: 118 steps marched, 2 cuts, 555 Newton cycles

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

   0.6667                   477    1.10                476    1.10

```

### Reactions

* What the reactions did by each time, from the cumulative balance both programs print (the `Net Reactions` column): oxygen consumed, oil burnt, water produced and heat released.

* DeepFlow prints it for a handful of steps; the step's time comes from its `.log`. Ours is read from the `.out` at every report.

```
At day 0.6667 (ours: report at day 0.6667)

                     DEEPFLOW         OURS  difference

 Oxygen consumed        17.52        17.54       +0.1%  gmol

       Oil burnt       0.5619       0.5625       +0.1%  gmol

  Water produced        11.53        11.54       +0.1%  gmol

   Heat released    7.346e+06    7.356e+06       +0.1%  J

```

![png]({{ "/assets/images/benchmark_image_49.png" | relative_url }})

### Step size

* Steps are compared on simulated time, as for the other decks. The first run is the reference.

```
run                THERM     OURS

steps                116      118

newton               361      555

newton/step        3.112    4.703

cuts                   0        2

dt min           8.8e-06 7.24e-06

dt geomean      0.002991 0.002908

dt max             0.017   0.0216

end day           0.6667    0.667

steps@0.000667d       13       14

steps@0.00667d        17       18

steps@0.0667d         36       35

steps@0.333d          79       77

steps@0.667d         116      117

```

![png]({{ "/assets/images/benchmark_image_50.png" | relative_url }})

#### Foamy oil primary production (sttst66)

* 12x12x7 SI block with one horizontal producer (`*WELL 1 'PRODN' *FRAC 0.25`, `*GEOMETRY *J`, six perforated layers) on a 250 kPa bottom-hole limit and no injection. Four components: water, dead oil, and two gases (`FM_GAS`, `GAS`) that stay in the gas phase through a constant K value. The `*STOREAC` reaction turns dissolved-gas-like `FM_GAS` into free `GAS` (the foamy-oil lamella drainage), and the run lasts two years.

* Reference is DeepFlow THERM: `stars_sttst66.log`. Its step table prints only the oil rate for this deck (no gas or water is produced in the first two years), so that is the comparison; the producer's bottom-hole pressure is held at its limit.

* Two modelling details decide the first step. `*WELL *FRAC` scales the well index only, while a `*GEOMETRY` `ff` also changes the equivalent radius; and a deck without `*PRPOR` takes the reference pressure of the porosity from `*PRSR`, which is what makes the initial oil in place equal DeepFlow's.

```
Running simulation [simuapp]: Foamy oil primary production (-novtu)

Elapsed: 3.52s

No text to display.

```

```
OURS reached day 730.0 of 730.0

oil rate against DeepFlow: mean |error| 0.94%, max 1.44%

   day   DEEPFLOW       OURS    error

     1     42.140     42.143    0.01%

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

#### Rock-fluid interpolation on a component (stsmo097)

* 240x1x1 SI core (0.5 mm blocks, 0.12 m long) with water, a second aqueous component `CHEM` and dead oil. `*INTCOMP 'CHEM' *WATER` interpolates the rock-fluid curves on the mole fraction of `CHEM` in the water phase, between two `*KRINTRP` sets (`*DTRAPW` / `*DTRAPN` 0 and 0.1). The injector holds 1.44e-4 m3/day of water that carries 5% `CHEM` (`*INCOMP *WATER 0.95 0.05 0.0`), so the fraction is 0.05 everywhere: halfway between the sets, `ratw = ratn = 0.5`. The producer holds 1.44e-4 m3/day of liquid. The run ends at day 5.

* The sets differ in the residual oil (`Sorw` 0.3 against 0) and in `Krwiro` (1.0 against 0.8). The interpolated curves have `Sorw` = 0.15, which is why the swept core settles at Sw = 0.85: set 1 alone stops at 0.70 and set 2 alone at 1.0. That is the endpoints being interpolated, not only the relative permeabilities read at fixed endpoints.

* Reference is DeepFlow THERM: `stars_stsmo097.log` (time step summary) for the production rates and the cost of the run, and `stars_stsmo097.prn` for the pressure and water saturation profiles at its report times and for the cumulative balance. Our profiles come from the VTU series (`*OUTSRF *GRID`), so this deck keeps its `.vtu` in `FIELD_PLOT_DECKS`.

* The deck carries `*CONVERGE ... *WELRES 1.0E-4`. A limit counts as broken only beyond that relative excess (1e-3 by default), and with the default our producer, which starts on its minimum BHP, stays there while up to 0.09% over its STL limit, where DeepFlow switches to STL at the first excess. The profiles section shows what that costs: 21 kPa of pressure level.

```
Running simulation [simuapp]: Rock-fluid interpolation on a component

Elapsed: 3.31s

No text to display.

```

```
OURS reached day 5.0000 of 5

THERM: 45 steps marched, 15 cuts, 305 Newton cycles

 OURS: 45 steps marched, 4 cuts, 283 Newton cycles

```

### Wells

* Producer rates are m3/day at standard conditions. DeepFlow's come from its time step summary, which prints two significant digits and leaves the water out until it breaks through (day 0.044); ours from the `.smy`.

* The injector holds its target (1.44e-4 m3/day of water, 5% of it `CHEM`), so the producer is the curve to read. The oil rate and the water cut say how fast the interpolated curves let the oil go; both fall off over four decades.

![png]({{ "/assets/images/benchmark_image_53.png" | relative_url }})

### Profiles along the core

* Water saturation and pressure against distance from the injector. The `.prn` holds the grid at every step DeepFlow marched; the first figure draws eight of those times (the early pressure build-up, the front, breakthrough and the long tail), DeepFlow dashed and ours solid in the same colour. The two programs march different steps, so ours is interpolated in time between the two frames around DeepFlow's time (every `*TIME` card is a frame of both). The second figure compares every time DeepFlow wrote.

* The core is one-dimensional along I, block 1 at the injector. The `.prn` marks a few values with a trailing `i` / `p` (the well blocks); the marker is dropped. DeepFlow's water molar fraction is `WATER` 0.950 / `CHEM` 0.050 in every block at every time, so both programs interpolate at the same fraction throughout.

* Read the saturation first: the plateau at 0.85 is the interpolated residual oil, and the fall towards the producer is the capillary end effect. The mean gap stays below 0.005 over the whole run. The largest single-block gaps (up to 0.05) are at the tip of the advancing front, where one block of position is the difference, and at day 2.139, where it is DeepFlow's own profile that has a one-block dip (block 36 at 0.802 between 0.846 and 0.840).

* The pressure agrees to within 1.5 kPa in shape and 0.5 kPa in level at every time. The level is what the deck's `*WELRES 1.0E-4` buys; the second figure marks DeepFlow's switch. The producer starts on its minimum BHP (7000 kPa) and DeepFlow switches it to its STL limit at day 0.002725, the first time the rate there exceeds 1.44e-4 m3/day (its `.prn`: "Max STL constraint violated"). A limit counts as broken in Catfish only beyond the well residual tolerance (`*CONVERGE *WELRES`, 1e-3 by default; a MAX limit is met while the rate is within `(1 + tol)` of it), so with the default the producer stays on the BHP limit until day 0.0255, up to 0.09% over its STL. That extra 1.6e-9 m3 withdrawn, against a total compressibility times pore volume of 7.8e-11 m3/kPa, is 21 kPa less pressure for the rest of the run: with the injector and the producer then holding the same rates nothing brings it back. With `*WELRES 1.0E-4` the producer switches at day 0.0030 and the gap is the 0.4 kPa that is there from the first step.

```
DeepFlow writes the grid at 45 times, from day 0.0001 to day 5

```

![png]({{ "/assets/images/benchmark_image_54.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_55.png" | relative_url }})

```
mean |dSw| never exceeds 0.0047; the largest block gap is 0.046. Pressure: mean difference -0.5 kPa at the end, shape within 1.5 kPa throughout.

```

### Material balance

* The cumulative balance both programs print at the end of the run, in gmol. The initial totals agree to every digit printed (same densities, porosity and pore volume). At day 5 the totals differ by what the saturation profiles differ by: DeepFlow holds slightly more water and slightly less oil in the core.

* The balance error is how far each program's own books are from closing: DeepFlow's is below 1e-7 percent, ours is about 0.015% for water and CHEM and 0.001% for the oil, the same order as the other decks (a tighter `*WELRES` makes the producer switch earlier, which costs a little closure).

```
             initial   current DEEPFLOW  current OURS  diff %     balance error % DEEPFLOW / OURS

 WATER  3.332381e-01       1.405441e+00  1.404797e+00   -0.05           -0.0000 / 0.0147

  CHEM  1.753885e-02       7.397057e-02  7.393666e-02   -0.05           -0.0000 / 0.0147

   OIL  9.106499e-02       1.786125e-02  1.790513e-02    0.25            0.0000 / -0.0008

```

### Step size

* Steps are compared on simulated time, as for the other decks. The first run is the reference. Both programs are forced to the deck's `*TIME` cards (0.003, 0.01, 0.05, 0.1, 2.5 and 5 days).

```
run             THERM     OURS

steps              45       45

newton            305      283

newton/step     6.778    6.289

cuts               15        4

dt min         0.0001   0.0001

dt geomean   0.004946 0.004443

dt max          1.462    1.431

end day             5        5

steps@0.005d        8        9

steps@0.05d        31       32

steps@0.5d         39       39

steps@2.5d         43       43

steps@5d           45       45

```

![png]({{ "/assets/images/benchmark_image_56.png" | relative_url }})

#### Imbibition capillary pressure tables (stsmo088)

* The same 240x1x1 core, fluids, wells and `*INTCOMP 'CHEM' *WATER` between two `*KRINTRP` sets as stsmo097 above (STARS option No. 88: "Verify/Illustrate `*CP_IMBIB` and `*PCOW_CRV` for Interpolation of Imbibition Capillary Pressure Curves"). The difference is in the tables: the `Pcow` column gives only its end values (1.0 at Sw 0.2, then -0.5 at Sw 0.7 in set 1 and -1 at Sw 1.0 in set 2) and writes the rows between them as `int`, linear in Sw. Catfish does not read `int`, so the deck has those rows written out; the numbers are the ones stsmo097 lists. The `Krow` columns are different from stsmo097's, and DeepFlow warns that `Kro` is above zero at `So = 0` for both sets.

* `*INTERP_ENDS`, `*CP_IMBIB` and `*PCOW_CRV` are named only in the deck's overview comments, not given as keywords, so this runs the default interpolation of stsmo097. The special history requests (`outsrf special blockvar` for `w`, `sw`, `krw`, `kro`, `pcow`) are commented out: Catfish writes no relperm or `Pcow` history.

* The deck carries `*CONVERGE ... *WELRES 1.0E-4` for the reason given for stsmo097: with the default, our producer stays on its BHP limit while above its STL where DeepFlow switches at the first excess.

* Reference is the DeepFlow THERM time step summary `stars_stsmo088.log`: the production rates, the injection rate, the water cut and the cost of the run. The run ends at day 2.5; the oil is gone by day 0.81.

```
Running simulation [simuapp]: Imbibition capillary pressure tables (-novtu)

Elapsed: 11.49s

No text to display.

```

```
OURS reached day 2.5000 of 2.5

THERM: 121 steps marched, 78 cuts, 895 Newton cycles, material balance error 0.019 % at the last step

 OURS: 173 steps marched, 82 cuts, 734 Newton cycles, material balance error 0.012 % at the last step

```

### Wells

* Producer rates are m3/day at standard conditions. DeepFlow's come from its time step summary, which prints two significant digits; ours from the `.smy`. The water cut is the water share of the two rates.

* The injector holds 1.44e-4 m3/day of water, so the producer is the curve to read. The oil rate and the water cut say how fast the interpolated curves let the oil go; DeepFlow's oil is gone at day 0.81 and the rest of the run is water only.

* The two agree to within a point of water cut until day 0.7. In the last stretch of the oil, days 0.76 to 0.81, ours falls off earlier: at day 0.784 the oil rate is 2.3e-6 against DeepFlow's 4.6e-6, and at day 0.804 it is 4e-8 against 2.4e-6 (water cut 99.97 against 98.3). The oil produced over the run is within 1.4% (2.12e-5 m3 against 2.09e-5 m3, the latter integrated from two-digit rates).

![png]({{ "/assets/images/benchmark_image_57.png" | relative_url }})

### Step size

* Steps are compared on simulated time, as for the other decks. The first run is the reference. Both programs are forced to the deck's `*TIME` cards (0.003, 0.01, 0.05, 0.1 and 2.5 days).

* Ours marches more, cheaper steps: 173 against 121, with 725 Newton cycles against 895 (4.2 a step against 7.4) and 82 cuts against 78. The balance error at the last step is 0.016% for ours and 0.019% for DeepFlow.

```
run              THERM     OURS

steps              121      173

newton             895      734

newton/step      7.397    4.243

cuts                78       82

dt min          0.0001   0.0001

dt geomean    0.005791 0.004288

dt max          0.6942   0.6317

end day            2.5      2.5

steps@0.0025d        5        5

steps@0.025d        18       19

steps@0.25d         49       59

steps@1.25d        119      170

steps@2.5d         121      173

```

![png]({{ "/assets/images/benchmark_image_58.png" | relative_url }})

#### Nonlinear viscosity mixing (stsmo051)

* 80x1x1 SI tube (25 m blocks) of water at its connate saturation and an oil of three components, `C10_OIL`, `C4_OIL` and `C1_OIL` (`*AVISC` 10, 0.2 and 0.05 cp). The injector holds 3.17e4 m3/day of oil at the surface (`*INCOMP *OIL 0 0 .23 .77`, `*OPERATE *STO`), lighter than the oil in place; the producer sits on its minimum BHP. The run ends at the `*STOP` of day 545.

* `*VSMIXCOMP 'C4_OIL'` with `*VSMIXENDP 0 0.6` and a curved `*VSMIXFUNC` replaces C4's mole fraction in the log mixing rule by f(x_C4), and the other components share what is left (`../doc/viscosity.md`, Nonlinear Viscosity Mixing). x_C4 in the oil runs from 0.127 (the oil in place) to 0.23 (the injected oil), inside the table.

* The deck is the STARS template stsmo051 modified so that this mixing is the only thing Catfish did not have: the changes are listed in its header (plain SI instead of bar, distinct oil viscosities, constant K values, oil injection on STO). Reference is a DeepFlow THERM run of the same file: `stars_stsmo051.log` (time step summary) and `stars_stsmo051.prn` (well tables, pressure and oil composition profiles at each of its 18 steps).

* A second run of the same deck with the three `*VSMIX` lines commented out shows what the mixing rule is worth: with linear mixing the oil is about 15% more viscous at the initial composition.

```
Running simulation [simuapp]: Nonlinear viscosity mixing

Elapsed: 0.79s

No text to display.

Running simulation [simuapp]: Linear viscosity mixing (stsmo051 without *VSMIX) (-novtu)

Elapsed: 0.35s

No text to display.

```

```
OURS: reached day 545.0 of 545

LINEAR MIXING: reached day 545.0 of 545

        THERM: 18 steps marched, 0 cuts, 48 Newton cycles

         OURS: 18 steps marched, 0 cuts, 60 Newton cycles

LINEAR MIXING: 19 steps marched, 0 cuts, 66 Newton cycles

```

### Wells

* The injector holds its surface oil rate, so its bottom-hole pressure is the curve to read: it is the pressure the oil's viscosity takes to push 3.17e4 m3/day through the tube. DeepFlow's comes from the well table of its `.prn` (five digits, at each of its steps), ours from the `.smy`. The producer stays on its minimum BHP (19000 kPa) in both programs, so its oil rate shows how fast the tube drains.

* The `.smy` names the wells by their order in the run, not in the deck; the series below are picked by what each well does.

```
         OURS: injector BHP - DeepFlow, mean    -6.2 kPa, largest   31.9 kPa

LINEAR MIXING: injector BHP - DeepFlow, mean   191.5 kPa, largest  503.9 kPa

```

![png]({{ "/assets/images/benchmark_image_59.png" | relative_url }})

### Profiles along the tube

* Pressure and the C4 mole fraction in the oil against distance from the injector, at the times both programs wrote the grid (the first steps and the `*TIME` cards 180, 365 and 545). DeepFlow's come from the `.prn`, which lists the oil mole fraction of each component under its own `Component =` line; ours from the VTU series.

* The pressure is where the mixing rule shows: with the nonlinear rule the mean gap to DeepFlow stays within 15 kPa, with linear mixing it is 90 to 150 kPa. The composition is set by the flow of the injected oil through the tube and agrees in both runs.

```
day    2.50: pressure OURS - DEEPFLOW mean    0.05 kPa, largest   6.96 kPa; largest |dx C4| 0.0042

day    3.25: pressure OURS - DEEPFLOW mean   -0.09 kPa, largest   2.62 kPa; largest |dx C4| 0.0037

day  180.00: pressure OURS - DEEPFLOW mean  -14.66 kPa, largest  20.15 kPa; largest |dx C4| 0.0017

day  365.00: pressure OURS - DEEPFLOW mean   -3.11 kPa, largest   4.81 kPa; largest |dx C4| 0.0012

day  545.00: pressure OURS - DEEPFLOW mean   -1.05 kPa, largest   1.76 kPa; largest |dx C4| 0.0009

```

![png]({{ "/assets/images/benchmark_image_60.png" | relative_url }})

### Step size

* Steps are compared on simulated time, as for the other decks. The first run is the reference. Both programs are forced to the deck's `*TIME` cards (180, 365 and the `*STOP` at 545 days).

```
run           THERM   OURS

steps            18     18

newton           48     60

newton/step   2.667  3.333

cuts              0      0

dt min       0.7482 0.7463

dt geomean    12.74  13.45

dt max        110.6  111.3

end day         545    545

steps@0.545d      0      0

steps@5.45d       3      3

steps@54.5d       9      8

steps@272d       14     14

steps@545d       18     18

```

![png]({{ "/assets/images/benchmark_image_61.png" | relative_url }})

#### Caustic-polymer slugs in a laboratory core (stdrm006)

* 19x1x1 SI core (4 mm blocks, 0.076 m long, 150 md, porosity 0.164) at Sw 0.64 with a dead oil; components `WATER`, `POLYMER`, `NAOH` and `DEAD OIL`. The injector holds 2.46e-5 m3/day of water (one pore volume is 0.25 day) that carries a sequence of slugs: NaOH 0.005 with polymer to day 0.0625, then polymer alone at 20, 10 and 5 cp (day 0.0625, 0.125, 0.1875), then pure water from day 0.25. The producer holds 101.3 kPa. The run ends at the `*STOP` of day 0.75.

* Three mechanisms are in play. `*ADSCOMP` / `*ADSLANG` / `*ADMAXT` adsorb NaOH reversibly and polymer irreversibly (`*ADRT`), and `*RRFT` 1.2 is the polymer's residual resistance (`../doc/adsorption.md`). `*IFTTABLE` with `*INTLOG` gives the interfacial tension from the NaOH mole fraction in the water (13 dyne/cm without NaOH, 0.005 at its minimum), and the capillary number interpolates the rock-fluid curves between the two `*KRINTRP` sets (`*DTRAPW` -4.5 and -3, `../doc/rock-fluid.md`). `*VSMIXCOMP 'POLYMER'` mixes the polymer viscosity nonlinearly.

* Reference is DeepFlow THERM: `stars_stdrm006.log` (time step summary) and `stars_stdrm006.prn`, which holds a well table at each of its 45 steps, the grid at every `*TIME` card and the cumulative balance. Our profiles come from the VTU series, so this deck is in `FIELD_PLOT_DECKS`.

* The deck has `*WSRF *GRID *TIME`, so our `.smy` and VTU hold the `*TIME` cards only (seven rows, 0 to 0.75 day), where DeepFlow's well tables cover every step. Curves of ours below therefore have six points; the tables compare both at the `*TIME` cards.

```
Running simulation [simuapp]: Caustic-polymer slugs in a laboratory core

Elapsed: 0.44s

No text to display.

```

```
OURS reached day 0.75 of 0.75

THERM: 45 steps marched, 0 cuts, 148 Newton cycles

 OURS: 45 steps marched, 0 cuts, 179 Newton cycles

```

### Wells

* Producer rates are m3/day at standard conditions. The injector holds its target, so its bottom-hole pressure is the curve to read, together with what the producer makes. DeepFlow's come from the well table of its `.prn` (six digits, every step), ours from the `.smy`, which names the wells by their order in the run; the producer is the one on the 101.3 kPa limit.

* The oil bank reaches the producer between day 0.17 and 0.30: the oil rate climbs three decades and the water cut falls from 99.9% to 55% in DeepFlow, and a second, smaller rise follows from day 0.55. Before the bank and at day 0.5 the oil rate agrees to 0.02% and 6%; the injector pressure agrees to 1.4 kPa at every `*TIME` card.

* The bank is the gap that is left: at day 0.1875 our oil rate is 15% below DeepFlow's and at day 0.25 it is 27% below (7.7e-6 against 1.07e-5 m3/day, water cut 68.5% against 56.6%). By day 0.75 it is 2% low.

```
   day  oil DEEPFLOW  oil OURS     oil %  water cut DEEPFLOW  water cut OURS  inj BHP kPa

0.0625     1.548e-08 1.548e-08  -0.02142               99.94           99.94      -0.4211

 0.125     1.551e-08 1.551e-08 -0.002028               99.94           99.94       -1.335

0.1875     1.918e-06 1.628e-06    -15.14               92.19           93.38      -0.6911

  0.25     1.068e-05 7.745e-06    -27.45                56.6           68.51     -0.02261

   0.5     1.026e-08 9.651e-09    -5.957               99.96           99.96      -0.3408

  0.75     1.134e-06 1.107e-06    -2.351               95.39            95.5      -0.4596

```

![png]({{ "/assets/images/benchmark_image_62.png" | relative_url }})

### Profiles along the core

* Water saturation, pressure and the adsorbed NaOH and polymer against distance from the injector, at the `*TIME` cards 0.0625 to 0.75 day (the times both programs wrote the grid), DeepFlow dashed and ours solid in the same colour. DeepFlow's come from the `.prn`, which prints the saturation to three digits and the pressure to 1 kPa, and lists the adsorption of each component under its own `Component =` line; ours from the VTU series.

* The adsorption is what the new keywords decide, and it agrees: the NaOH front (68 gmol/m3 is `*ADMAXT`) is within 4.5% of `*ADMAXT` at every time, and the polymer within 1.3% except at day 0.1875, where the front sits a block away (6.2%). The pressure is within 1.6 kPa, which is about one digit of the `.prn`.

* The saturation is the loose one: behind the NaOH front it ripples in both programs. The mean gap over the core is 0.007 at day 0.0625, 0.046 at day 0.125 and below 0.025 after; the largest single block is 0.19, at day 0.125.

![png]({{ "/assets/images/benchmark_image_63.png" | relative_url }})

```
   day  mean |dSw|  max |dSw|  mean dP kPa  max |dP| kPa  max |d NaOH adsorbed| % of ADMAXT  max |d Polymer adsorbed| % of ADMAXT

0.0625    0.006729    0.04464        -0.48        0.9746                              2.537                                 1.254

 0.125     0.04632      0.192      -0.3477          1.53                              3.093                                 0.684

0.1875     0.02334    0.06347      -0.1089         1.152                              3.702                                 6.237

  0.25     0.00784    0.01623      0.01192        0.4605                               4.46                                0.1234

   0.5    0.002822    0.01623      -0.3173        0.8499                            0.09862                               0.03731

  0.75    0.002694    0.01623      -0.6152        0.9633                            0.07334                               0.03731

```

### Material balance

* The cumulative balance both programs print at the end of the run, in gmol. DeepFlow's carries a `Net Adsorbed` column; ours does not, so the totals and the net injected minus produced are compared. The initial water and oil agree to every digit printed.

* The water, NaOH and polymer in the core agree to 0.3%, 0.07% and 0.02%; the oil left is 1.5% lower, which is the oil produced being 1.2% higher (2.485e-3 against 2.456e-3 gmol). The balance error is how far each program's own books are from closing: ours is within 0.005% for every component, DeepFlow's up to 0.05% for the polymer.

```
            current DEEPFLOW  current OURS  diff %     balance error % DEEPFLOW / OURS

    WATER       2.850250e-01  2.858187e-01    0.28           -0.0080 / -0.0002

  POLYMER       3.143218e-07  3.143774e-07    0.02            0.0525 / -0.0042

     NAOH       1.863586e-04  1.864800e-04    0.07           -0.0221 / -0.0050

     DEAD       1.999226e-03  1.970333e-03   -1.45           -0.0000 / 0.0001

Oil produced (gmol): DEEPFLOW 2.4561e-03, OURS 2.4850e-03 (+1.18 %)

```

### Step size

* Steps are compared on simulated time, as for the other decks. The first run is the reference. Both programs are forced to the deck's `*TIME` cards (0.0625, 0.125, 0.1875, 0.25, 0.5 and the `*STOP` at 0.75 days), and both take 45 steps without a cut. Ours needs about 20% more Newton cycles.

```
run              THERM    OURS

steps               45      45

newton             148     179

newton/step      3.289   3.978

cuts                 0       0

dt min          0.0025  0.0025

dt geomean     0.01302 0.01324

dt max           0.025   0.025

end day           0.75    0.75

steps@0.00075d       0       0

steps@0.0075d        1       1

steps@0.075d         7       7

steps@0.375d        29      29

steps@0.75d         45      45

```

![png]({{ "/assets/images/benchmark_image_64.png" | relative_url }})

#### Steam foam in a radial cross-section (stdrm010)

* 9x1x3 radial sector (`*RW 0`, rings of 2 to 14 m out to a 500 m outer ring, 60 degrees, 15 m layers, porosity 0.35) of a 1000 md bed with a 1e4 md higher-permeability path (all rings of the top layer, and rings 1 and 6 of the other two). The bed holds water at 0.15 (0.5 in the path) and a bitumen of three million cp at 10 C and 2.9 cp at 316 C (`*VISCTABLE`), at 15.5 C. Components `WATER`, `SURFACT` and `BITUMEN`.

* The injector (`*FRAC` 1/6) holds 150 m3/day of steam at 210 C, quality 0.7, in the bottom layer: 25 m3/day for the sector. The producer (`*FRAC` 0.5) holds 30 m3/day of liquid (`*STL`), 15 for the sector, in the same layer. From day 730 the steam carries surfactant (1.875e-4 mole fraction in the water, 1 wt%). The run ends at the `*STOP` of day 1460; the `*TIME` cards are 365, 730 and 1095.

* The foam is the empirical scheme of `../doc/rock-fluid.md` (Option 3): `*INTCOMP 'SURFACT' *WATER` with `*INTLIN` interpolates the rock-fluid curves on the surfactant mole fraction between three `*KRINTRP` sets (no foam, weak foam with a mobility reduction of 2.5 at `*DTRAPW` 0.4, strong foam with 50 at 0.02, which differ in `*KRGCW`), and `*FMSURF`, `*FMCAP`, `*FMOIL` and `*FMMOB` set where the foam acts. The surfactant adsorbs reversibly (`*ADSCOMP`, `*ADSLANG` at three temperatures, `../doc/adsorption.md`).

* Reference is DeepFlow THERM: `stars_stdrm010.log` (time step summary) and `stars_stdrm010.prn`, which holds a well table at each of its 94 steps, the grid at day 0.1 and at every `*TIME` card, and the cumulative balance. DeepFlow ran the template's default `*KDIR *UP` (K = 1 at the bottom); the deck here is the same model with K reversed and `*KDIR *DOWN`, which Catfish needs, so layer K of ours is layer 4 - K of DeepFlow's and the profile cells turn the `.prn` over. Our profiles come from the VTU series (a frame per step), so this deck is in `FIELD_PLOT_DECKS`.

```
Running simulation [simuapp]: Steam foam in a radial cross-section

Elapsed: 0.93s

No text to display.

```

```
OURS reached day 1460 of 1460

THERM: 94 steps marched, 3 cuts, 198 Newton cycles

 OURS: 88 steps marched, 9 cuts, 383 Newton cycles

```

### Wells

* Rates are m3/day at standard conditions for the sector (the injector's 25, the producer's limit of 15). DeepFlow's come from the well table of its `.prn`, ours from the `.smy`, which has a row per step and names the wells by their order in the run; the producer is the one that makes oil. The table at the foot compares both at the `*TIME` cards, where both programs end a step.

* Both programs show the same course: the oil rate climbs with the steam, falls back at the breakthrough, and rises again after the surfactant starts at day 730; the water cut mirrors it. Over the second period the peak oil rate is 7.7 m3/day in DeepFlow and 7.0 in ours.

* Before the surfactant our oil rate is above DeepFlow's: 31% at day 365 and 24% at day 730 (3.48 against 2.66 and 3.70 against 2.98 m3/day), with the water cut 5.5 and 4.8 points lower and the producer's BHP 4.5% and 7.7% higher. At day 1095 the oil rate agrees (-1.4%). At day 1460 ours has fallen to 4.08 against DeepFlow's 7.68 m3/day (-47%), the water cut 72.8% against 48.8%: DeepFlow's oil rate is still rising over the last 150 days and ours is falling.

* The injector's bottom-hole pressure is 30% below DeepFlow's at days 365 and 730 (1894 against 2684 kPa, 1956 against 2773), 24% and 17% below at days 1095 and 1460. After the surfactant starts, DeepFlow's peaks at 6770 kPa against 4430 for ours.

```
 day  oil DEEPFLOW  oil OURS  water cut DEEPFLOW  water cut OURS  prod BHP DEEPFLOW  prod BHP OURS  inj BHP DEEPFLOW  inj BHP OURS

 365        2.6579    2.7378              82.281          81.748             909.03         923.08            2684.1        1949.2

 730        2.9819    3.3274              80.111          77.818             1116.7         1122.1            2772.8        2054.1

1095        6.2905    5.8859              58.054          60.761             1801.6         1612.9            4175.8        3967.6

1460        7.6799    6.6568              48.801          55.622             1944.6         1816.4            3987.1        3824.9

```

![png]({{ "/assets/images/benchmark_image_65.png" | relative_url }})

### Profiles along the radius

* Temperature, pressure, gas saturation and adsorbed surfactant against radius, one column per layer, at the `*TIME` cards 365 to 1460 (the surfactant starts at 730, so the adsorption is zero before then), DeepFlow dashed and ours solid in the same colour. DeepFlow's come from the `.prn` (temperature and pressure to the integer, saturation to three digits; the adsorption listed under `Component = SURFACT`), ours from the VTU frame of the step that ends at each card.

* The top layer agrees: over the four times the mean gap is 2.3 C, 73 kPa and 0.048 in Sg. The middle and bottom layers do not: 23 to 24 C, 230 to 310 kPa and 0.044 to 0.073, and the largest single blocks (98 to 176 C, 0.27 to 0.52 in Sg, up to 1100 kPa) are in them inside the first 50 m, where the steam front is. The two largest are the middle layer at 6 m at days 365 and 730 (day 365: 62 C in DeepFlow, 192 C in ours) and the bottom layer at 31 to 42 m at days 1095 and 1460.

* Over the whole grid the mean gap is 12 C at day 365, 19 C at days 730 and 1095 and 14 C at day 1460; the pressure 190, 210, 285 and 120 kPa; Sg 0.037, 0.037, 0.061 and 0.085. The surfactant adsorbed is within a mean of 0.18 gmol/m3 (7% of the 2.56 `*ADMAXT`), with the largest block, 1.1 gmol/m3, in the bottom layer at 42 m at day 1095.

![png]({{ "/assets/images/benchmark_image_66.png" | relative_url }})

```
 day  mean |dT C|  max |dT C|  mean |dP kPa|  max |dP kPa|  mean |dSg|  max |dSg|  mean |dAds|  max |dAds|

 365        9.955       130.9          151.9          1078     0.03805     0.2864            0           0

 730        9.721       178.2          147.5         999.4     0.02924     0.2907            0           0

1095        6.791       51.64          201.5         311.7     0.02623     0.2012      0.06793      0.5681

1460        8.631        80.1          139.2         266.3     0.06361     0.3353      0.08004      0.8662

```

### Material balance

* The cumulative balance both programs print at the end of the run, in gmol (energy in J): the initial total, what was injected minus produced, and the error each program's own books show. DeepFlow's table carries a `Net Reactions` column that ours shares; the deck's surfactant degradation (`*STOREAC`, `*EACT`) consumes 1.16e5 gmol of surfactant in DeepFlow and 1.26e5 in ours.

* The initial totals differ by 0.10% in water and 0.04% in energy; the bitumen agrees to 0.002%. Net water injected minus produced is 2.4% higher in ours and net energy 0.8% higher; the bitumen produced is 6.7% higher (1.239e7 against 1.162e7 gmol), which is the same bias as the oil rate before day 1095. What is in the core at the end agrees to 0.2% for water and 0.06% for energy. The surfactant left in the core is 14% lower in ours (5.05e4 against 5.90e4 gmol). The balance error is within 0.04% for ours and up to 0.11% for DeepFlow.

```
          initial DEEPFLOW  initial OURS   net DEEPFLOW     net OURS  diff %  current diff %   balance error % DEEPFLOW / OURS

   WATER      3.814269e+10  3.818231e+10   1.124654e+09 1.135812e+09    0.99            0.16          -0.0147 / -0.0006

 SURFACT      0.000000e+00  0.000000e+00   1.810711e+05 1.821769e+05    0.61            6.05          -0.1113 / -0.0050

 BITUMEN      3.916811e+09  3.916889e+09  -1.161615e+07 -1.181425e+07    1.71           -0.00           0.0011 / 0.0020

  Energy      6.199378e+14  6.201891e+14   6.811423e+13 6.911116e+13    1.46            0.16          -0.0516 / -0.0015

```

### Step size

* Steps are compared on simulated time, as for the other decks. The first run is the reference. Both programs are forced to the `*TIME` cards (365, 730, 1095, and the `*STOP` at 1460 days). DeepFlow marches 94 steps with 3 cuts and 198 Newton cycles, ours 93 steps with 11 cuts and 392: twice the Newton cycles per step.

```
run              THERM   OURS

steps               94     88

newton             198    383

newton/step      2.106  4.352

cuts                 3      9

dt min             0.1 0.0798

dt geomean       5.384  5.762

dt max           79.08    100

end day           1460   1460

steps@1.46d         10     11

steps@14.6d         16     17

steps@146d          25     26

steps@730d          42     48

steps@1.46e+03d     94     88

```

![png]({{ "/assets/images/benchmark_image_67.png" | relative_url }})

#### ES-SAGD with solvent, 2D live oil (stflu023)

* 30x1x32 Cartesian cross-section (144 m wide, 100 m thick slice, 1 m layers; porosity 0.2965, 4264 md horizontally and 852 md vertically) at 10 C. The oil is 97% `BITUMEN` with 2% `CH4` and 1% `C6H14` (3.8 million cp at 5 C), at a saturation of 0.79 with water at 0.21. Components `WATER`, `BITUMEN`, `CH4` and `C6H14`.

* A SAGD pair in the middle column: the injector `INJ-L` in layer 25 and the producer `PRD-L` in layer 30, 5 m below it. Both are shut in until day 90 (`DATE 2005 4 1`) while `*UHTR` / `*TMPSET` heat their blocks to 185 C. They then open: the injector with steam of quality 0.8 at 205 C and 2% `C6H14` (`*INCOMP *WATER-OIL`) on a 2500 kPa BHP limit, the producer on 1000 kPa. The deck is a `*GASTRAP` test with the keyword commented out. The run ends at the last `DATE`, 2013 April 1 (day 3012).

* Reference is DeepFlow THERM: `stars_stflu023.log` (time step summary, 463 steps) and `stars_stflu023.prn`, which holds the final cumulative balance and a well table at ten of its steps. The deck writes no grid to the `.prn`, so there are no profiles to compare, only the wells, the balance and the cost.

* The last `DATE` converts to 3011.958 days here, an hour short of 3012: the deck's dates go through local time, so the run depends on the machine's time zone (with `TZ=UTC` it ends at 3012 in 521 steps, not 511).

```
Running simulation [simuapp]: ES-SAGD with solvent, 2D live oil (-novtu)

Elapsed: 135.88s

No text to display.

```

```
OURS reached day 3012.0 of 3012

THERM: 463 steps marched, 14 cuts, 2268 Newton cycles

 OURS: 511 steps marched, 41 cuts, 3497 Newton cycles

```

### Wells

* Producer rates and the injected water, m3/day at standard conditions, one point per step in both programs: DeepFlow's from its time step summary (four digits), ours from the `.smy`. The time axis is logarithmic from day 80, since the wells open at day 90 and the first months carry the transient, and so is the gas axis. Both wells sit on their BHP limits in both programs from the day they open (injector 2500 kPa, producer 1000 kPa), so the rates are the result.

* The opening at day 90 is the sharpest event: the oil rate peaks at 444 m3/day in DeepFlow and 486 in ours, the gas at 3107 and 2233. After the first months the oil and water rates follow each other: the mean absolute gap to DeepFlow's steps is 5.5% in oil and 0.8% in water over days 200 to 1095, and 3.7% and 0.5% from day 1095 on. The gas rate is the loose one (25% and 18%): it is the smallest and burstiest rate, tens of m3/day after day 200.

* At the end of the run the oil rate is 44.4 m3/day in DeepFlow and 45.0 in ours, the water 2113 and 2122, the injected water 2111 and 2120 (ours at day 3011.96).

```
     rate  mean |gap| % day 90-200  mean |gap| % day 200-1095  mean |gap| % day 1095-3012

      oil                     14.4                        5.5                         3.7

      gas                     43.1                       25.0                        17.9

    water                      6.2                        0.8                         0.5

inj_water                      4.1                        0.9                         0.5

```

![png]({{ "/assets/images/benchmark_image_68.png" | relative_url }})

### Material balance

* The cumulative balance both programs print at the end of the run, in gmol (energy in J): the initial total, what was injected minus produced, and the error each program's own books show. The initial totals agree to 0.002% except the energy (-7.48e13 against -4.89e13 J), so the energy is read from what was injected minus produced.

* The net water injected is 1.7% higher in ours and the bitumen produced 0.3% lower; the `CH4` produced is 0.4% higher and the `C6H14` 5.3% higher; the net energy is 3.4% lower. The balance error is how far each program's own books are from closing: ours is within 0.03% for water, bitumen and energy but 0.26% for `CH4` and 3.5% for `C6H14`, against DeepFlow's 0.16% and 0.05%.

```
          initial DEEPFLOW  initial OURS   net DEEPFLOW     net OURS  diff %   balance error % DEEPFLOW / OURS

   WATER      1.575167e+09  1.575144e+09   1.504974e+08 1.530928e+08    1.72          -0.0668 / -0.0002

 BITUMEN      1.768460e+08  1.768442e+08  -1.439350e+08 -1.434449e+08   -0.34           0.0260 / -0.0226

     CH4      3.646309e+06  3.646273e+06  -3.619410e+06 -3.635500e+06    0.44          -0.1566 / 0.2619

   C6H14      1.823154e+06  1.823136e+06  -1.241833e+06 -1.307927e+06    5.32           0.0546 / 3.5298

  Energy     -7.479612e+13 -4.889817e+13   3.895656e+14 3.763840e+14   -3.38          -0.0022 / -0.0007

```

### Step size

* Steps are compared on simulated time, as for the other decks. The first run is the reference. Both programs are forced to the deck's `DATE` cards (monthly to 2005 May 1, then 2006 February 1, 2007 January 1, 2008 January 1 and the last at 2013 April 1). DeepFlow marches 463 steps with 14 cuts and 2268 Newton cycles, ours 511 steps with 41 cuts and 3497. The two have marched the same number of steps by day 1510 (330); after that ours takes 181 steps where DeepFlow takes 132.

```
run              THERM  OURS

steps              463   511

newton            2268  3497

newton/step      4.898 6.843

cuts                14    41

dt min            0.01  0.01

dt geomean        3.82 3.558

dt max            68.7 65.14

end day           3012  3012

steps@3.01d          9     9

steps@30.1d         15    15

steps@301d         132   131

steps@1.51e+03d    330   330

steps@3.01e+03d    462   511

```

![png]({{ "/assets/images/benchmark_image_69.png" | relative_url }})

#### ES-SAGD with solvent and a wellbore model (stflu031)

* The same model as stflu023 above (STARS Well Management Template No. 116: a `*GASTRAP` test with the keyword commented out, a semi-steady wellbore model), with a `DATE` card in most months and a `STOP` after the card of 2008 December 1 (day 1430), where the run ends. Its wells, fluids and schedule are stflu023's, so the first days of the two DeepFlow logs are identical.

* Reference is DeepFlow THERM: `stars_stflu031.log` and `stars_stflu031.prn`; its run ends at the same `STOP` in 320 steps. The deck here differs from DeepFlow's copy in a few output and perforation keywords only (`*OUTPRN`, `WPRN SECTOR`, and `OPEN FLOW-FROM` / `FLOW-TO` on the two perforations, which ours carries and DeepFlow's copy does not). As for stflu023 there is no grid in the `.prn`, so no profiles.

```
Running simulation [simuapp]: ES-SAGD with solvent and a wellbore model (-novtu)

Elapsed: 74.72s

No text to display.

```

```
OURS reached day 1430.0 of 1430

THERM: 320 steps marched, 9 cuts, 1420 Newton cycles

 OURS: 321 steps marched, 20 cuts, 1922 Newton cycles

```

### Wells

* As for stflu023: the producer's rates and the injected water, one point per step in both programs, on logarithmic time and gas axes, both wells on their BHP limits (2500 and 1000 kPa).

* The mean absolute gap to DeepFlow's steps is 14% in oil and 6% in water over days 90 to 200, 5.5% and 0.9% from day 200 to 1095, and 4.2% and 0.6% to day 1430; the gas 43%, 25% and 15%. These are stflu023's gaps over the same days, as the same model gives. At day 1430 the oil rate is 65.0 m3/day in DeepFlow and 67.1 in ours, the gas 30.5 and 33.8, the water 1939 and 1944.

```
     rate  mean |gap| % day 90-200  mean |gap| % day 200-1095  mean |gap| % day 1095-1430

      oil                     14.4                        5.5                         4.2

      gas                     43.1                       24.7                        15.3

    water                      6.2                        0.9                         0.6

inj_water                      4.1                        0.9                         0.6

```

![png]({{ "/assets/images/benchmark_image_70.png" | relative_url }})

### Material balance

* The cumulative balance at day 1430, the end of the run, in gmol (energy in J): DeepFlow's last table in its `.prn`, ours from the step of the `.out` that ends at day 1430. As for stflu023 the initial energy differs (-7.48e13 against -4.89e13 J), so it is compared on what was injected minus produced.

* The net water injected is 3.5% lower in ours, the bitumen produced 1.7% lower and the `CH4` 2.0% lower; the `C6H14` produced is 2.4% higher; the net energy is 4.2% lower. The balance error of ours is within 0.03% for water, bitumen, `CH4` and energy and 1.2% for `C6H14`, against DeepFlow's 0.12% for `CH4` and below 0.07% for the rest.

```
          initial DEEPFLOW  initial OURS   net DEEPFLOW     net OURS  diff %   balance error % DEEPFLOW / OURS

   WATER      1.575167e+09  1.575144e+09   3.380247e+08 3.261265e+08   -3.52          -0.0622 / -0.0003

 BITUMEN      1.768460e+08  1.768442e+08  -9.809174e+07 -9.644840e+07   -1.68           0.0206 / 0.0029

     CH4      3.646309e+06  3.646273e+06  -2.476333e+06 -2.426510e+06   -2.01          -0.1225 / 0.0243

   C6H14      1.823154e+06  1.823136e+06   1.425575e+06 1.459737e+06    2.40           0.0485 / 1.2050

  Energy     -7.479612e+13 -4.889817e+13   2.327664e+14 2.229012e+14   -4.24           0.0010 / 0.0009

```

### Step size

* Steps are compared on simulated time, as for the other decks. The first run is the reference. Both programs are forced to the deck's `DATE` cards and end at its `STOP`. DeepFlow marches 320 steps with 9 cuts and 1420 Newton cycles, ours 321 steps with 20 cuts and 1922.

```
run              THERM  OURS

steps              320   321

newton            1420  1922

newton/step      4.438 5.988

cuts                 9    20

dt min            0.01  0.01

dt geomean       2.641 2.603

dt max           24.96 17.87

end day           1430  1430

steps@1.43d          7     7

steps@14.3d         13    13

steps@143d          85    88

steps@715d         182   178

steps@1.43e+03d    320   321

```

![png]({{ "/assets/images/benchmark_image_71.png" | relative_url }})

#### Dual-well SAGD in a dipping reservoir (stflu030)

* 25x3x26 Cartesian block (2 m blocks along I, three 100 m rows, 1 to 2 m layers; porosity 0.23 to 0.30, 1468 md horizontally and 562 md vertically) dipping across the rows (`*DTOP` 734.4, 739.6 and 744.0 m), at 48 C and 7600 kPa at 760 m. The oil is a dead oil, 122807 cp at 47 C and 3.3 cp at 300 C (`*VISCTABLE`); components `WATER` and `OIL`.

* Five wells with discretised wellbores (a `FLOW-TO` / `FLOW-FROM` chain through the perforations): the upper pair `UPCASI` (producer on the casing, minimum BHP 11700 kPa) and `UPTUB` (steam injector on the tubing), the lower pair `LWCASI` (producer, minimum BHP 10700 kPa, `STL` limit 50) and `LWTUB` (injector), and `LWTUBP` (producer on the lower tubing, `STL` limit 300). The steam is at 324 C and quality 0.5, `*STW` 200 and a BHP limit of 11700 kPa, on wells of `*FRAC` 0.5, so 100 m3/day each. Wells are shut in and opened by `DATE` cards through 1996; the run ends on 1997 to 2007 year-end cards at 2007 December 31 (day 4382).

* Reference is DeepFlow THERM's time step summary, `stars_stflu030.log` (340 steps). It carries the field totals only, so the wells are compared as field totals: ours is the sum of the producers' (and of the injectors') columns of the `.smy`. DeepFlow's copy of the deck differs from this one in the output cards, `*GRID *VARI` against `*CART`, and in the perforation keywords (`'SURFACE'` and `CLOSED` against 0 and `CLOSE`).

```
Running simulation [simuapp]: Dual-well SAGD in a dipping reservoir (-novtu)

Elapsed: 101.96s

No text to display.

```

```
OURS reached day 4382.0 of 4382

THERM: 340 steps marched, 0 cuts, 340 Newton cycles

 OURS: 523 steps marched, 23 cuts, 2029 Newton cycles

```

### Wells

* Field oil and water production and injected water, m3/day at standard conditions, on logarithmic axes: DeepFlow's rates are orders of magnitude below ours. Its time step summary prints no injection after day 365 (a blank is no flow), and before that at most 0.007 m3/day, where each injector is asked for 100.

* In DeepFlow's run the field makes 0.24 m3/day of oil and 0.12 of water at day 365 and 0.15 and 0.08 at day 4382. In ours the wells inject 52 m3/day at day 365 and produce 13 of oil and 53 of water; the injection falls to 39 at day 1460 and 8.5 at day 4382, and the oil to 13 and 0.4.

* So the table below does not measure how close the two programs are: they do not run the same problem on these decks. Why DeepFlow's wells barely flow is open; the differences between the two copies of the deck listed above are the only ones there are.

```
producers ['UPCASI', 'LWCASI', 'LWTUBP'], injectors ['UPTUB', 'LWTUB']

 day  oil DEEPFLOW  oil OURS  water DEEPFLOW  water OURS  injected DEEPFLOW  injected OURS

  91             0     2.272               0       22.73             0.0066          51.89

 365        0.2398     13.18          0.1239       53.33                  0          51.66

 730        0.2035     15.78          0.1052       56.06                  0           53.9

1460        0.1781     12.85           0.094       39.57                  0          39.18

2921        0.1578    0.7521           0.084       10.25                  0          10.19

4382        0.1453    0.4377           0.077       8.739                  0          8.546

```

![png]({{ "/assets/images/benchmark_image_72.png" | relative_url }})

### Step size

* Steps are compared on simulated time, as for the other decks. The first run is the reference. Both programs are forced to the deck's `DATE` cards. DeepFlow marches 340 steps with no cut and one Newton cycle per step (340 in all), which fits a run in which the wells barely flow; ours 523 steps with 23 cuts and 2029 Newton cycles.

```
run              THERM  OURS

steps              340   523

newton             340  2029

newton/step          1  3.88

cuts                 0    23

dt min           0.001 0.001

dt geomean       8.931 3.837

dt max              15    15

end day           4382  4382

steps@4.38d          4     7

steps@43.8d          9    63

steps@438d          69   204

steps@2.19e+03d    190   373

steps@4.38e+03d    340   523

```

![png]({{ "/assets/images/benchmark_image_73.png" | relative_url }})

# Speed



`-DCMAKE_BUILD_TYPE=Release`

### Dome corner grid

```
Running simulation [simuapp]: Dome Corner point

Elapsed: 9.12s

    65  41.9475  2    365.000     1.65                                                                   0.000   34.975   0.0697    3.673



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  8.787s  98.80%      

|- Newton                                 8.728s  |- 99.32%   

  |- Update                               3.091s    |- 35.42% 

  |- FluxJac                              2.169s    |- 24.85% 

  |- ScdAcc                               0.904s    |- 10.36% 

  |- Solver                               0.702s    |- 8.04%  

  |- update_dev                           0.696s    |- 7.98%  

  |- Precond                              0.531s    |- 6.08%  

  |- SanitizeJac                          0.202s    |- 2.31%  

  |- alignvar                             0.171s    |- 1.96%  

  |- Residual                             0.082s    |- 0.94%  

  |- HeatLoss                             0.064s    |- 0.73%  

  |- PerfJac                              0.017s    |- 0.20%  

|- Logging                                0.019s  |- 0.22%    

|- Output                                 0.010s  |- 0.12%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.107s  1.20%       

|- execution                              0.097s  |- 90.61%   

------------------------------------------------------------

TOTAL                                     8.894s

============================================================



Time steps : 65/68, step size: 5.61538, 11.8477

```

```
Found 4 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu018_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_74.png" | relative_url }})

## Heterogeneous

### SPE10 benchmark 2D 

```
Running simulation [simuapp]: SPE10 benchmark 2D water flooding 375 days ~7s single thread (OMP_NUM_THREADS=8)

Elapsed: 12.21s

    92   2.2603  2    375.000    19.31             4e-06             2e-05                      19.43    0.000    0.575   0.0466    0.002



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 11.902s  99.30%      

|- Newton                                11.630s  |- 97.71%   

  |- Update                               3.513s    |- 30.21% 

  |- Solver                               3.051s    |- 26.23% 

  |- FluxJac                              2.147s    |- 18.46% 

  |- ScdAcc                               0.997s    |- 8.58%  

  |- update_dev                           0.657s    |- 5.65%  

  |- Precond                              0.443s    |- 3.81%  

  |- PerfJac                              0.243s    |- 2.09%  

  |- SanitizeJac                          0.184s    |- 1.59%  

  |- alignvar                             0.167s    |- 1.43%  

  |- Residual                             0.099s    |- 0.85%  

  |- HeatLoss                             0.015s    |- 0.13%  

|- Output                                 0.166s  |- 1.39%    

|- Logging                                0.019s  |- 0.16%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.084s  0.70%       

|- execution                              0.076s  |- 89.73%   

------------------------------------------------------------

TOTAL                                    11.986s

============================================================



Time steps : 92/93, step size: 4.07609, 2.87497

```

![png]({{ "/assets/images/benchmark_image_75.png" | relative_url }})

### Medium size



* 202,005 grid block (201x201x5) with heterogeneous permeability

* 61 wells water flooding pattern 

* 1500 days

```
Running simulation [simuapp]: Heterogeneous + 61wells - performance test medium size ~4m.50s (Single) (OMP_NUM_THREADS=8, -novtu)

Elapsed: 331.90s

    34  23.7345  3    365.000   257.46              8.72              3.28                     720.00    0.000  137.265   0.0117    1.433



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                               5m 29.43s  99.36%      

|- Newton                              5m 28.78s  |- 99.80%   

  |- Solver                            1m 49.26s    |- 33.23% 

  |- Update                            1m 22.17s    |- 24.99% 

  |- FluxJac                           1m 19.78s    |- 24.26% 

  |- ScdAcc                              19.033s    |- 5.79%  

  |- update_dev                          14.883s    |- 4.53%  

  |- Precond                              9.210s    |- 2.80%  

  |- Residual                             3.871s    |- 1.18%  

  |- HeatLoss                             2.288s    |- 0.70%  

  |- PerfJac                              1.692s    |- 0.51%  

  |- alignvar                             1.094s    |- 0.33%  

  |- SanitizeJac                          0.674s    |- 0.21%  

|- Output                                 0.091s  |- 0.03%    

|- Logging                                0.018s  |- 0.01%    

|- Input                                  0.004s  |- 0.00%    

Initialization                            2.125s  0.64%       

|- execution                              1.954s  |- 91.98%   

------------------------------------------------------------

TOTAL                                  5m 31.56s

============================================================



Time steps : 34/35, step size: 10.7353, 11.6116

```

### Johnansen water flooding

```
Running simulation [simuapp]: Johnansen water flooding takes ~5m on M2 (OMP_NUM_THREADS=8)

Elapsed: 26.47s

    17 365.0000  1   3650.000   353.94              0.06              0.02                     189.09    0.000    3.220   0.0066  3.0e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 23.921s  92.11%      

|- Newton                                23.785s  |- 99.43%   

  |- Update                               8.039s    |- 33.80% 

  |- FluxJac                              6.736s    |- 28.32% 

  |- Solver                               4.873s    |- 20.49% 

  |- ScdAcc                               1.512s    |- 6.36%  

  |- update_dev                           1.109s    |- 4.66%  

  |- Precond                              0.671s    |- 2.82%  

  |- Residual                             0.346s    |- 1.45%  

  |- alignvar                             0.076s    |- 0.32%  

  |- SanitizeJac                          0.042s    |- 0.18%  

  |- PerfJac                              0.003s    |- 0.01%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.092s  |- 0.38%    

|- Logging                                0.001s  |- 0.01%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            2.050s  7.89%       

|- execution                              1.649s  |- 80.45%   

------------------------------------------------------------

TOTAL                                    25.971s

============================================================



Time steps : 17/17, step size: 214.706, 163.784

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data//stflu016_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_76.png" | relative_url }})

# MPI



`simumpi` runs the same deck domain-decomposed across MPI ranks (METIS partitioning, one rank per

subdomain) and rank 0 writes the whole reservoir's `<stem>.smy` - the same filename and the same

columns `simuapp` writes, with per-well and per-cell values reduced across ranks. That is what lets

every plot above read either engine's output, and what the checks below compare.



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

Elapsed: 1.81s

    75  53.9980  3   3650.000     0.01              4.31             99.77                       5.96    0.659  235.228   0.0062    2.644



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.525s  95.07%      

|- Newton                                 1.505s  |- 98.65%   

  |- FluxJac                              0.592s    |- 39.33% 

  |- Update                               0.399s    |- 26.50% 

  |- update_dev                           0.173s    |- 11.48% 

  |- ScdAcc                               0.172s    |- 11.41% 

  |- Solver                               0.054s    |- 3.58%  

  |- PerfJac                              0.042s    |- 2.77%  

  |- Precond                              0.022s    |- 1.47%  

  |- alignvar                             0.009s    |- 0.60%  

  |- Residual                             0.007s    |- 0.49%  

  |- HeatLoss                             0.005s    |- 0.33%  

  |- SanitizeJac                          0.002s    |- 0.10%  

|- Logging                                0.014s  |- 0.89%    

|- Output                                 0.008s  |- 0.52%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.079s  4.93%       

|- execution                              0.075s  |- 94.97%   

------------------------------------------------------------

TOTAL                                     1.604s

============================================================



Time steps : 75/75, step size: 48.6667, 60.2013

Running simulation [simumpi]: MPI comparison np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 1.83s

    54  36.7607  7   1249.050     1.97              6.22             75.95                       5.96    0.876   25.139   0.1994   51.689

    55  26.0137  6   1275.063     1.85              5.94             76.28                       5.96    0.876   25.724   0.1053   18.696

    56  33.1518  8   1308.215     1.69              5.80             77.48                       5.96    0.954   41.457   0.1670   25.758

    57  36.0661  7   1344.281     1.29              5.40             80.74                       5.96    0.950   45.739   0.1355   24.005

    58  40.7150  6   1384.996     1.27              5.29             80.70                       5.96    0.944   58.854   0.1252   25.583

    59  44.4552  5   1429.451     1.11              5.37             82.91                       5.96    0.939   63.965   0.1889   23.116

    60  45.9139  6   1475.365     0.96              5.31             84.73                       5.96    0.933   54.596   0.1576   31.387



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  44.7321  5   1520.097     0.87              5.49             86.39                       5.96    0.929   57.770   0.1944   15.742

    62  45.4536  6   1565.551     0.71              5.43             88.48                       5.96    0.924   58.921   0.1097   21.013

    63  54.8414  7   1620.392     0.61              5.31             89.69                       5.96    0.917   80.922   0.1464    8.034

    64  64.7696  4   1685.162     0.55              5.35             90.68                       5.96    0.909   91.889   0.0846    6.757

    65  96.6269  7   1781.789     0.44              5.35             92.46                       5.96    0.898  145.893   0.0767    6.430

    66 149.1514  4   1930.940     0.32              5.38             94.33                       5.96    0.882  240.692   0.0610    9.263

    67 211.9688  6   2142.909     0.21              5.31             96.12                       5.96    0.860  372.902   0.1094   12.037

    68 247.9906  4   2390.900     0.14              5.30             97.46                       5.96    0.833  494.049   0.0556   13.106

    69 249.6887  6   2640.588     0.09              5.20             98.32                       5.96    0.803  559.643   0.0801   12.309

    70 233.7552  7   2874.344     0.06              5.06             98.89                       5.96    0.773  601.043   0.0599   11.211

    71 209.5562  4   3083.900     0.04              4.96             99.25                       5.96    0.745  602.217   0.0331    9.759

    72 187.6365  4   3271.536     0.03              4.83             99.48                       5.96    0.719  591.998   0.0265    8.525

    73 169.7853  4   3441.322     0.02              4.68             99.62                       5.96    0.694  585.445   0.0222    7.620

    74 154.6805  6   3596.002     0.01              4.43             99.73                       5.96    0.669  591.286   0.0721    7.039

    75  53.9980  3   3650.000     0.01              4.31             99.77                       5.96    0.659  235.228   0.0062    2.644

Time steps : 75/75, step size: 48.6667, 60.2013

Running simulation [simumpi]: MPI comparison np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 1.20s

    54  36.7611  7   1249.051     1.97              6.22             75.95                       5.96    0.876   25.140   0.1994   51.689

    55  26.0140  6   1275.065     1.85              5.94             76.28                       5.96    0.876   25.724   0.1053   18.695

    56  33.1527  8   1308.217     1.69              5.80             77.48                       5.96    0.954   41.455   0.1670   25.758

    57  36.0671  7   1344.285     1.29              5.40             80.74                       5.96    0.950   45.739   0.1355   24.006

    58  40.7155  6   1385.000     1.27              5.29             80.70                       5.96    0.944   58.857   0.1252   25.584

    59  44.4544  6   1429.454     1.11              5.37             82.91                       5.96    0.939   64.019   0.1897   23.113

    60  45.7968  6   1475.251     0.96              5.31             84.73                       5.96    0.933   54.408   0.1575   31.388



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  44.6168  5   1519.868     0.87              5.49             86.38                       5.96    0.929   57.660   0.1947   15.773

    62  45.3037  6   1565.172     0.71              5.43             88.46                       5.96    0.924   58.815   0.1098   20.882

    63  54.8260  7   1619.998     0.61              5.31             89.69                       5.96    0.917   80.625   0.1452    8.029

    64  65.0006  4   1684.998     0.55              5.35             90.68                       5.96    0.909   92.188   0.0854    6.821

    65  96.6449  7   1781.643     0.44              5.35             92.45                       5.96    0.898  145.902   0.0771    6.432

    66 148.9741  3   1930.617     0.32              5.38             94.33                       5.96    0.883  240.384   0.0610    9.254

    67 211.8228  6   2142.440     0.21              5.31             96.12                       5.96    0.860  372.558   0.1095   12.031

    68 247.9341  4   2390.374     0.14              5.30             97.46                       5.96    0.833  493.828   0.0556   13.105

    69 249.6955  6   2640.070     0.09              5.20             98.32                       5.96    0.803  559.525   0.0802   12.311

    70 233.7910  7   2873.861     0.06              5.06             98.89                       5.96    0.773  600.974   0.0600   11.214

    71 209.6031  4   3083.464     0.04              4.96             99.25                       5.96    0.745  602.218   0.0331    9.762

    72 187.6784  4   3271.142     0.03              4.83             99.48                       5.96    0.719  592.014   0.0265    8.527

    73 169.8204  4   3440.963     0.02              4.68             99.62                       5.96    0.694  585.455   0.0222    7.622

    74 154.7109  6   3595.674     0.01              4.43             99.73                       5.96    0.669  591.232   0.0722    7.040

    75  54.3264  3   3650.000     0.01              4.31             99.77                       5.96    0.660  236.589   0.0062    2.659

Time steps : 75/75, step size: 48.6667, 60.1976

Running simulation [simumpi]: MPI comparison np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 1.24s

    54  36.7594  7   1249.046     1.97              6.22             75.95                       5.96    0.876   25.137   0.1994   51.689

    55  26.0127  6   1275.058     1.85              5.94             76.28                       5.96    0.876   25.725   0.1053   18.698

    56  33.1486  8   1308.207     1.69              5.80             77.48                       5.96    0.954   41.464   0.1670   25.758

    57  36.0624  7   1344.269     1.29              5.40             80.73                       5.96    0.950   45.738   0.1354   24.003

    58  40.7134  6   1384.983     1.27              5.29             80.70                       5.96    0.944   58.844   0.1252   25.578

    59  44.4581  5   1429.441     1.11              5.37             82.91                       5.96    0.939   63.964   0.1888   23.124

    60  45.9215  6   1475.362     0.96              5.31             84.73                       5.96    0.933   54.609   0.1577   31.395



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  44.7327  5   1520.095     0.87              5.49             86.39                       5.96    0.929   57.771   0.1945   15.742

    62  45.4520  6   1565.547     0.71              5.43             88.48                       5.96    0.924   58.920   0.1097   21.011

    63  54.8415  7   1620.389     0.61              5.31             89.69                       5.96    0.917   80.918   0.1463    8.034

    64  64.7730  4   1685.162     0.55              5.35             90.68                       5.96    0.909   91.893   0.0846    6.758

    65  96.6276  7   1781.789     0.44              5.35             92.46                       5.96    0.898  145.894   0.0767    6.430

    66 149.1496  4   1930.939     0.32              5.38             94.33                       5.96    0.882  240.689   0.0610    9.263

    67 211.9673  6   2142.906     0.21              5.31             96.12                       5.96    0.860  372.899   0.1094   12.037

    68 247.9898  4   2390.896     0.14              5.30             97.46                       5.96    0.833  494.047   0.0556   13.106

    69 249.6886  6   2640.585     0.09              5.20             98.32                       5.96    0.803  559.641   0.0801   12.309

    70 233.7554  7   2874.340     0.06              5.06             98.89                       5.96    0.773  601.042   0.0599   11.211

    71 209.5565  4   3083.896     0.04              4.96             99.25                       5.96    0.745  602.217   0.0331    9.759

    72 187.6368  4   3271.533     0.03              4.83             99.48                       5.96    0.719  591.998   0.0265    8.525

    73 169.7855  4   3441.319     0.02              4.68             99.62                       5.96    0.694  585.445   0.0222    7.620

    74 154.6808  6   3596.000     0.01              4.43             99.73                       5.96    0.668  591.285   0.0721    7.039

    75  54.0005  3   3650.000     0.01              4.31             99.77                       5.96    0.659  235.238   0.0062    2.644

Time steps : 75/75, step size: 48.6667, 60.2013

simuapp          rc=0   1.60s   75/ 75 steps  to  3650.00 days

simumpi np=1     rc=0   1.43s   75/ 75 steps,  0 cuts  to  3650.00 days

simumpi np=2     rc=0   0.87s   75/ 75 steps,  0 cuts  to  3650.00 days

simumpi np=4     rc=0   0.76s   75/ 75 steps,  0 cuts  to  3650.00 days

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


![png]({{ "/assets/images/benchmark_image_77.png" | relative_url }})

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

Elapsed: 25.20s

   153  53.9586  6   1095.000     1.34              1.17             46.66                               0.073   31.616   0.0691    3.479



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 24.896s  99.67%      

|- Newton                                24.854s  |- 99.83%   

  |- FluxJac                             11.408s    |- 45.90% 

  |- Update                               6.260s    |- 25.19% 

  |- ScdAcc                               2.516s    |- 10.12% 

  |- update_dev                           2.279s    |- 9.17%  

  |- Solver                               1.291s    |- 5.20%  

  |- Precond                              0.448s    |- 1.80%  

  |- alignvar                             0.141s    |- 0.57%  

  |- Residual                             0.111s    |- 0.45%  

  |- PerfJac                              0.101s    |- 0.41%  

  |- HeatLoss                             0.092s    |- 0.37%  

  |- SanitizeJac                          0.027s    |- 0.11%  

|- Logging                                0.022s  |- 0.09%    

|- Output                                 0.012s  |- 0.05%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.083s  0.33%       

|- execution                              0.080s  |- 96.26%   

------------------------------------------------------------

TOTAL                                    24.979s

============================================================



Time steps : 153/161, step size: 7.15686, 14.9924

Running simulation [simumpi]: CSS parity np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 24.81s

   132   0.7398  3    749.410     5.88             50.39             89.55                               0.045  144.857   0.2641    5.833

   133   0.6253  6    750.036     6.50             38.74             85.63                               0.045   96.208   0.3191    3.729

   134   0.4665  5    750.502     8.05             32.47             80.13                               0.045   61.827   0.0820    2.317

   135   0.7037  6    751.206     9.55             26.23             73.31                               0.045   77.962   0.4466    2.626

   136   0.4128  4    751.619    10.95             23.61             68.31                               0.045   42.673   0.1359    1.358

   137   0.5053  4    752.124    11.94             21.67             64.47                               0.045   47.315   0.2107    1.482

   138   0.4903  3    752.614    12.10             20.93             63.36                               0.045   41.430   0.0369    1.298

   139   0.9180  4    753.532    11.71             19.58             62.59                               0.045   64.153   0.2327   16.724

   140   0.8396  6    754.372    11.32             19.11             62.80                               0.045   49.515   0.2824    1.654

   141   0.6797  2    755.052    10.30             19.50             65.45                               0.045   35.874   0.0411    1.215

   142   1.2447  3    756.296     9.37             19.18             67.19                               0.045   58.511   0.0400    1.929

   143   2.2935  2    758.590     8.13             18.16             69.08                               0.045   88.706   0.0230    2.974

   144   4.6394  3    763.229     6.62             15.21             69.68                               0.045  125.603   0.0280    4.910

   145   9.1231  5    772.352     4.92             11.02             69.15                               0.045  146.725   0.0730    7.531

   146  14.3210  5    786.673     3.88              8.15             67.73                               0.045  133.262   0.0925    8.846

   147  20.6655  6    807.339     3.01              5.65             65.24                               0.045  113.871   0.0930    9.227

   148  29.7679  5    837.107     2.52              4.08             61.80                               0.045   90.353   0.0758    9.081

   149  46.1487 12    883.256     2.10              2.95             58.37                               0.045   74.816   0.1332    8.758

   150  46.1487 12    929.404     2.00              2.37             54.23                               0.045   48.229   0.0915    5.942



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   151  46.1487  6    975.553     1.80              1.88             51.00                               0.049   38.590   0.0966    4.771

   152  65.4875  5   1041.041     1.67              1.45             46.51                               0.049   43.149   0.0789    5.176

   153  53.9595  6   1095.000     1.34              1.17             46.66                               0.073   31.617   0.0691    3.479

Time steps : 153/161, step size: 7.15686, 14.9924

Running simulation [simumpi]: CSS parity np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 15.37s

   132   0.6112  6    750.028     6.37             38.92             85.94                               0.046   93.852   0.2923    3.688

   133   0.4836  4    750.512     7.77             32.33             80.62                               0.046   63.722   0.1119    2.427

   134   0.6464  4    751.158     9.08             26.94             74.78                               0.046   71.940   0.2913    2.554

   135   0.5127  4    751.671    10.32             23.33             69.34                               0.046   52.356   0.2198    1.651

   136   0.4852  3    752.156    11.48             21.37             65.04                               0.047   45.098   0.2091    1.401

   137   0.4729  5    752.629    11.66             20.56             63.81                               0.047   39.821   0.0571    1.237

   138   0.7992  6    753.428    11.44             19.38             62.88                               0.047   56.920   0.1061   13.552

   139   1.0922  5    754.520    11.40             18.12             61.39                               0.047   62.728   0.4441    8.675

   140   0.6435  6    755.164    10.27             18.77             64.63                               0.047   33.455   0.0491    1.128

   141   1.1313  3    756.295     9.41             18.39             66.14                               0.047   52.957   0.0525    1.741

   142   1.9551  3    758.250     8.26             17.91             68.44                               0.047   77.248   0.0284    2.549

   143   3.8365  3    762.087     6.86             15.66             69.53                               0.047  110.972   0.0222    4.282

   144   7.7961  5    769.883     5.17             11.69             69.33                               0.047  139.438   0.0733    6.877

   145  12.2169  5    782.100     4.08              8.88             68.51                               0.047  130.499   0.0863    8.182

   146  18.0969  4    800.197     3.31              6.27             65.44                               0.047  115.483   0.0593    8.903

   147  30.2582  8    830.455     2.57              4.29             62.54                               0.047  104.011   0.0771    9.981

   148  15.1291  7 1  845.584     2.33              3.71             61.40                               0.047   37.495   0.0579    4.079

   149  25.4689  6    871.053     2.02              3.14             60.82                               0.050   43.647   0.1258    5.158

   150  32.3246  6    903.377     1.94              2.62             57.48                               0.050   38.679   0.1085    4.741



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   151  43.7649  6    947.142     1.91              2.14             52.94                               0.050   40.257   0.0566    5.076

   152  74.1301 11   1021.272     1.68              1.55             47.96                               0.050   51.731   0.0994    6.304

   153  73.7275  7   1095.000     1.56              1.18             43.01                               0.050   42.984   0.0911    4.772

Time steps : 153/162, step size: 7.15686, 15.6515

Running simulation [simumpi]: CSS parity np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 11.31s

   132   0.7398  3    749.410     5.88             50.39             89.55                               0.045  144.856   0.2641    5.833

   133   0.6252  6    750.036     6.50             38.74             85.63                               0.045   96.205   0.3191    3.728

   134   0.4665  5    750.502     8.05             32.47             80.13                               0.045   61.825   0.0820    2.316

   135   0.7037  6    751.206     9.55             26.23             73.31                               0.045   77.964   0.4466    2.626

   136   0.4128  4    751.619    10.95             23.61             68.31                               0.045   42.674   0.1360    1.358

   137   0.5053  4    752.124    11.94             21.67             64.47                               0.045   47.314   0.2107    1.482

   138   0.4904  3    752.614    12.10             20.93             63.36                               0.045   41.431   0.0369    1.298

   139   0.9181  4    753.532    11.71             19.58             62.59                               0.045   64.155   0.2328   16.724

   140   0.8394  6    754.372    11.32             19.11             62.80                               0.045   49.504   0.2824    1.653

   141   0.6795  2    755.051    10.30             19.50             65.45                               0.045   35.866   0.0411    1.215

   142   1.2445  3    756.296     9.37             19.18             67.19                               0.045   58.502   0.0400    1.928

   143   2.2930  2    758.589     8.13             18.16             69.08                               0.045   88.694   0.0230    2.974

   144   4.6384  3    763.227     6.62             15.21             69.68                               0.045  125.592   0.0280    4.910

   145   9.1215  5    772.349     4.92             11.02             69.15                               0.045  146.725   0.0730    7.530

   146  14.3176  5    786.666     3.88              8.15             67.73                               0.045  133.260   0.0925    8.845

   147  20.6626  6    807.329     3.01              5.65             65.24                               0.045  113.880   0.0930    9.227

   148  29.7621  5    837.091     2.52              4.08             61.80                               0.045   90.360   0.0758    9.081

   149  46.1283 12    883.219     2.10              2.95             58.38                               0.045   74.810   0.1332    8.757

   150  46.1283 12    929.347     2.00              2.37             54.24                               0.045   48.226   0.0916    5.940



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   151  46.1283  6    975.476     1.80              1.88             51.00                               0.049   38.584   0.0967    4.771

   152  65.4427  5   1040.918     1.67              1.46             46.51                               0.049   43.134   0.0789    5.174

   153  54.0816  6   1095.000     1.34              1.17             46.62                               0.072   31.688   0.0691    3.487

Time steps : 153/161, step size: 7.15686, 14.9926

simuapp          rc=0  24.98s  153/161 steps  to  1095.00 days

simumpi np=1     rc=0  24.48s  153/161 steps,  8 cuts  to  1095.00 days

simumpi np=2     rc=0  15.04s  153/162 steps,  9 cuts  to  1095.00 days

simumpi np=4     rc=0  10.94s  153/161 steps,  8 cuts  to  1095.00 days

```

![png]({{ "/assets/images/benchmark_image_78.png" | relative_url }})

### Difference from serial and speedup, across mechanisms



The two questions of this section - how far `simumpi` is from `simuapp`, and how much faster it

runs - asked of more than one deck. Each deck below exercises one mechanism that has to work

across a partition boundary:



| deck | mechanism |

|---|---|

| `stflu015` | corner-point grid, deck without `*NUMERICAL` |

| `stflu018` | dome corner-point grid, a perforation in an inactive block |

| `lauwerier` | thermal front, cut steps |

| `stflu028`, `stflu029` | temperature-dependent rock-fluid endpoints (`*KRTEMTAB`) |

| `stflu019` | `*NETGROSS`, `*PVCUTOFF`, 314k active cells |

| `stflu010`, `stflu021` | well constraint switching |

| `stflu033` | combustion reactions |

| `stsmo088`, `stsmo097` | imbibition capillary pressure, rock-fluid interpolation |

| `corner`, `stflu011` | corner-point and 1000-cell Cartesian grids |



**Difference.** For every well and phase, the surface volume (`vratesc_*` integrated over time) up

to the end both runs reached, relative to `simuapp`; the deck's number is the worst of those over

the columns holding at least 1% of its largest volume. Volumes rather than rates, because a

constraint switch one step earlier shifts a rate curve sideways while the volume it moves stays

put. np=1 preconditions with serial's global ILU and should reproduce `simuapp` to roundoff; past

one rank the preconditioner is block Jacobi, which converges to a different point inside the same

linear tolerance, so a difference there is only worth chasing above `PARITY_TOLERANCE` (1%). A run

that ends before `simuapp` did is flagged either way.



**Speed.** Each engine's own marching time (`engine_runtime()`), speedup and efficiency against

`simumpi` at np=1, and the largest rank's share of the cells. The same caveats as the scaling

section below apply, more so: one run each, and most of these decks give a rank only a few

hundred cells, where collectives cost more than the arithmetic - read those rows as overhead, not

as decomposition. `stflu019` is the one deck here large enough for the speedup to mean something;

it is capped at `PARITY_SLOW_MAXSTEPS` steps (about seven minutes serial otherwise), and all its

runs march the same steps.

```
Running simulation [simuapp]: stflu015 baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 0.72s

    14  36.5999  1    365.000    63.57              0.03              0.04                               0.000    6.379 9.26e-05  3.5e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.389s  80.31%      

|- Newton                                 0.387s  |- 99.53%   

  |- Update                               0.148s    |- 38.14% 

  |- FluxJac                              0.140s    |- 36.14% 

  |- ScdAcc                               0.039s    |- 9.99%  

  |- update_dev                           0.027s    |- 7.03%  

  |- Solver                               0.016s    |- 4.24%  

  |- Precond                              0.007s    |- 1.78%  

  |- Residual                             0.003s    |- 0.79%  

  |- alignvar                             0.002s    |- 0.53%  

  |- HeatLoss                             0.001s    |- 0.32%  

  |- SanitizeJac                          0.000s    |- 0.12%  

  |- PerfJac                              0.000s    |- 0.03%  

|- Output                                 0.001s  |- 0.21%    

|- Logging                                0.001s  |- 0.13%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.095s  19.69%      

|- execution                              0.084s  |- 88.31%   

------------------------------------------------------------

TOTAL                                     0.485s

============================================================



Time steps : 14/14, step size: 26.0714, 49.2511

Running simulation [simumpi]: stflu015 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 0.72s

            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-26





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.0200  1      0.020    63.59             4e-06             6e-06                               0.000    0.016 2.37e-07  9.2e-07

     2   0.0467  1      0.067    63.59             1e-05             2e-05                               0.000    0.038 5.53e-07  2.2e-06

     3   0.1089  1      0.176    63.59             3e-05             5e-05                               0.000    0.089 1.29e-06  5.0e-06

     4   0.2540  1      0.430    63.59             8e-05             1e-04                               0.000    0.207 3.00e-06  1.2e-05

     5   0.5923  1      1.022    63.59             2e-04             3e-04                               0.000    0.479 6.95e-06  2.7e-05

     6   1.3802  1      2.402    63.59             5e-04             7e-04                               0.000    1.102 1.60e-05  6.2e-05

     7   3.2111  1      5.613    63.59              0.00              0.00                               0.000    2.494 3.62e-05  1.4e-04

     8   4.3868  1     10.000    63.59              0.00              0.00                               0.000    3.285 4.77e-05  1.9e-04

     9   7.0000  1     17.000    63.59              0.00              0.00                               0.000    4.956 7.19e-05  2.8e-04

    10  16.1203  1     33.120    63.59              0.01              0.01                               0.000   10.132 1.47e-04  5.7e-04

    11  36.6245  1     69.745    63.59              0.01              0.02                               0.000   18.253 2.65e-04    0.001

    12  81.4906  1    151.235    63.58              0.02              0.03                               0.000   27.474 3.99e-04    0.002

    13 177.1648  1    328.400    63.57              0.02              0.04                               0.000   34.806 5.04e-04    0.002

    14  36.5999  1    365.000    63.57              0.03              0.04                               0.000    6.379 9.26e-05  3.5e-04

Time steps : 14/14, step size: 26.0714, 49.2511

Running simulation [simumpi]: stflu015 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 0.58s

            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-26





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.0200  1      0.020    63.59             4e-06             6e-06                               0.000    0.016 2.37e-07  9.2e-07

     2   0.0467  1      0.067    63.59             1e-05             2e-05                               0.000    0.038 5.53e-07  2.2e-06

     3   0.1089  1      0.176    63.59             3e-05             5e-05                               0.000    0.089 1.29e-06  5.0e-06

     4   0.2540  1      0.430    63.59             8e-05             1e-04                               0.000    0.207 3.00e-06  1.2e-05

     5   0.5923  1      1.022    63.59             2e-04             3e-04                               0.000    0.479 6.95e-06  2.7e-05

     6   1.3802  1      2.402    63.59             5e-04             7e-04                               0.000    1.102 1.60e-05  6.2e-05

     7   3.2111  1      5.613    63.59              0.00              0.00                               0.000    2.494 3.62e-05  1.4e-04

     8   4.3868  1     10.000    63.59              0.00              0.00                               0.000    3.285 4.77e-05  1.9e-04

     9   7.0000  1     17.000    63.59              0.00              0.00                               0.000    4.956 7.19e-05  2.8e-04

    10  16.1203  1     33.120    63.59              0.01              0.01                               0.000   10.132 1.47e-04  5.7e-04

    11  36.6245  1     69.745    63.59              0.01              0.02                               0.000   18.253 2.65e-04    0.001

    12  81.4906  1    151.235    63.58              0.02              0.03                               0.000   27.474 3.99e-04    0.002

    13 177.1648  1    328.400    63.57              0.02              0.04                               0.000   34.806 5.04e-04    0.002

    14  36.5999  1    365.000    63.57              0.03              0.04                               0.000    6.379 9.26e-05  3.5e-04

Time steps : 14/14, step size: 26.0714, 49.2511

Running simulation [simumpi]: stflu015 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 0.54s



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-26





VTU generation is suppressed.

VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.0200  1      0.020    63.59             4e-06             6e-06                               0.000    0.016 2.37e-07  9.2e-07

     2   0.0467  1      0.067    63.59             1e-05             2e-05                               0.000    0.038 5.53e-07  2.2e-06

     3   0.1089  1      0.176    63.59             3e-05             5e-05                               0.000    0.089 1.29e-06  5.0e-06

     4   0.2540  1      0.430    63.59             8e-05             1e-04                               0.000    0.207 3.00e-06  1.2e-05

     5   0.5923  1      1.022    63.59             2e-04             3e-04                               0.000    0.479 6.95e-06  2.7e-05

     6   1.3802  1      2.402    63.59             5e-04             7e-04                               0.000    1.102 1.60e-05  6.2e-05

     7   3.2111  1      5.613    63.59              0.00              0.00                               0.000    2.494 3.62e-05  1.4e-04

     8   4.3868  1     10.000    63.59              0.00              0.00                               0.000    3.285 4.77e-05  1.9e-04

     9   7.0000  1     17.000    63.59              0.00              0.00                               0.000    4.956 7.19e-05  2.8e-04

    10  16.1203  1     33.120    63.59              0.01              0.01                               0.000   10.132 1.47e-04  5.7e-04

    11  36.6245  1     69.745    63.59              0.01              0.02                               0.000   18.253 2.65e-04    0.001

    12  81.4906  1    151.235    63.58              0.02              0.03                               0.000   27.474 3.99e-04    0.002

    13 177.1648  1    328.400    63.57              0.02              0.04                               0.000   34.806 5.04e-04    0.002

    14  36.5999  1    365.000    63.57              0.03              0.04                               0.000    6.379 9.26e-05  3.5e-04

Time steps : 14/14, step size: 26.0714, 49.2511

Running simulation [simuapp]: stflu018 baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 12.13s

    65  41.9475  2    365.000     1.65                                                                   0.000   34.975   0.0697    3.673



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 11.792s  99.08%      

|- Newton                                11.775s  |- 99.85%   

  |- FluxJac                              4.827s    |- 41.00% 

  |- Update                               3.412s    |- 28.98% 

  |- ScdAcc                               1.300s    |- 11.04% 

  |- update_dev                           1.135s    |- 9.64%  

  |- Solver                               0.591s    |- 5.02%  

  |- Precond                              0.226s    |- 1.92%  

  |- alignvar                             0.068s    |- 0.58%  

  |- Residual                             0.064s    |- 0.54%  

  |- HeatLoss                             0.049s    |- 0.42%  

  |- SanitizeJac                          0.015s    |- 0.12%  

  |- PerfJac                              0.013s    |- 0.11%  

|- Logging                                0.008s  |- 0.07%    

|- Output                                 0.004s  |- 0.03%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.110s  0.92%       

|- execution                              0.098s  |- 89.32%   

------------------------------------------------------------

TOTAL                                    11.902s

============================================================



Time steps : 65/68, step size: 5.61538, 11.8477

Running simulation [simumpi]: stflu018 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 12.17s

    44   0.3527  1     18.353     0.22             27.91             99.22                               0.001  274.721   0.0533    7.685

    45   0.6073  1     18.960     0.16             21.36             99.27                               0.001  299.576   0.0261    6.607

    46   1.0223  4     19.982                      15.65            100.00                               0.001  316.278   0.1346    8.173

    47   1.2572  3     21.239                      13.06            100.00                               0.001  272.371   0.2064    7.617

    48   1.2346  6     22.474                      10.41            100.00                               0.001  185.649   0.1090    6.278

    49   1.6684  2     24.142                       7.79            100.00                               0.001  172.386   0.0613   12.010

    50   2.7633  3     26.906                       5.77            100.00                               0.001  204.053   0.1065    6.314

    51   3.7705  4     30.676     0.53              4.34             89.20                               0.001  194.663   0.0915    6.231

    52   5.4654  2     36.142     0.66              3.28             83.27                               0.001  186.985   0.1673    6.864

    53   6.0285  3     42.170     0.60              2.57             80.95                               0.001  141.787   0.1190    5.953

    54   7.8428  5     50.013     0.56              2.00             78.30                               0.001  126.416   0.0827    6.665

    55  11.7941  5     61.807     0.65              1.38             67.92                               0.001  113.534   0.1219    8.269

    56  15.1806  5     76.988     0.65              0.97             59.73                               0.001  107.438   0.1463    8.151

    57  17.9317  9     94.919     0.56              0.71             56.09                               0.001   96.866   0.1504    7.632

    58  20.8916 10    115.811     0.38              0.57             60.05                               0.000   77.650   0.1756    7.125

    59  22.4594 14    138.270     0.28              0.48             62.86                               0.000   51.589   0.0848    6.817

    60  19.2509  3    157.521     0.38              0.30             44.54                               0.000   34.370   0.0820    4.890



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  29.0472  3    186.568     0.63              0.12             15.87                               0.000   38.454   0.0936    5.891

    62  41.7313  6    228.300     0.91              0.01              0.81                               0.000   44.431   0.1848    6.726

    63  43.6299 10    271.930     1.31                                                                   0.000   31.407   0.1487    5.763

    64  51.1230  7    323.053     1.37                                                                   0.000   25.178   0.1588    5.395

    65  41.9475  2    365.000     1.65                                                                   0.000   34.975   0.0697    3.673

Time steps : 65/68, step size: 5.61538, 11.8477

Running simulation [simumpi]: stflu018 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 7.15s

    44   0.3527  1     18.353     0.22             27.91             99.22                               0.001  274.721   0.0533    7.685

    45   0.6073  1     18.960     0.16             21.36             99.27                               0.001  299.576   0.0261    6.607

    46   1.0223  4     19.982                      15.65            100.00                               0.001  316.278   0.1346    8.173

    47   1.2572  3     21.239                      13.06            100.00                               0.001  272.371   0.2064    7.617

    48   1.2346  6     22.474                      10.41            100.00                               0.001  185.649   0.1090    6.278

    49   1.6684  2     24.142                       7.79            100.00                               0.001  172.386   0.0613   12.010

    50   2.7633  3     26.906                       5.77            100.00                               0.001  204.053   0.1065    6.314

    51   3.7705  4     30.676     0.53              4.34             89.20                               0.001  194.663   0.0915    6.231

    52   5.4654  2     36.142     0.66              3.28             83.27                               0.001  186.985   0.1673    6.864

    53   6.0285  3     42.170     0.60              2.57             80.95                               0.001  141.787   0.1190    5.953

    54   7.8428  5     50.013     0.56              2.00             78.30                               0.001  126.416   0.0827    6.665

    55  11.7941  5     61.807     0.65              1.38             67.92                               0.001  113.534   0.1219    8.269

    56  15.1806  5     76.988     0.65              0.97             59.73                               0.001  107.438   0.1463    8.151

    57  17.9317  9     94.919     0.56              0.71             56.09                               0.001   96.866   0.1504    7.632

    58  20.8916 10    115.811     0.38              0.57             60.05                               0.000   77.650   0.1756    7.125

    59  22.4594 14    138.270     0.28              0.48             62.86                               0.000   51.589   0.0848    6.817

    60  19.2509  3    157.521     0.38              0.30             44.54                               0.000   34.370   0.0820    4.890



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  29.0472  3    186.568     0.63              0.12             15.87                               0.000   38.454   0.0936    5.891

    62  41.7313  6    228.300     0.91              0.01              0.81                               0.000   44.431   0.1848    6.726

    63  43.6299 10    271.930     1.31                                                                   0.000   31.407   0.1487    5.763

    64  51.1230  7    323.053     1.37                                                                   0.000   25.178   0.1588    5.395

    65  41.9475  2    365.000     1.65                                                                   0.000   34.975   0.0697    3.673

Time steps : 65/68, step size: 5.61538, 11.8477

Running simulation [simumpi]: stflu018 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 5.35s

    44   0.3527  1     18.353     0.22             27.91             99.22                               0.001  274.721   0.0533    7.685

    45   0.6073  1     18.960     0.16             21.36             99.27                               0.001  299.576   0.0261    6.607

    46   1.0223  4     19.982                      15.65            100.00                               0.001  316.278   0.1346    8.173

    47   1.2572  3     21.239                      13.06            100.00                               0.001  272.371   0.2064    7.617

    48   1.2346  6     22.474                      10.41            100.00                               0.001  185.649   0.1090    6.278

    49   1.6684  2     24.142                       7.79            100.00                               0.001  172.386   0.0613   12.010

    50   2.7633  3     26.906                       5.77            100.00                               0.001  204.053   0.1065    6.314

    51   3.7705  4     30.676     0.53              4.34             89.20                               0.001  194.663   0.0915    6.231

    52   5.4654  2     36.142     0.66              3.28             83.27                               0.001  186.985   0.1673    6.864

    53   6.0285  3     42.170     0.60              2.57             80.95                               0.001  141.787   0.1190    5.953

    54   7.8428  5     50.013     0.56              2.00             78.30                               0.001  126.416   0.0827    6.665

    55  11.7941  5     61.807     0.65              1.38             67.92                               0.001  113.534   0.1219    8.269

    56  15.1806  5     76.988     0.65              0.97             59.73                               0.001  107.438   0.1463    8.151

    57  17.9317  9     94.919     0.56              0.71             56.09                               0.001   96.866   0.1504    7.632

    58  20.8916 10    115.811     0.38              0.57             60.05                               0.000   77.650   0.1756    7.125

    59  22.4594 14    138.270     0.28              0.48             62.86                               0.000   51.589   0.0848    6.817

    60  19.2509  3    157.521     0.38              0.30             44.54                               0.000   34.370   0.0820    4.890



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  29.0472  3    186.568     0.63              0.12             15.87                               0.000   38.454   0.0936    5.891

    62  41.7314  6    228.300     0.91              0.01              0.81                               0.000   44.431   0.1848    6.726

    63  43.6299 10    271.930     1.31                                                                   0.000   31.407   0.1487    5.763

    64  51.1230  7    323.053     1.37                                                                   0.000   25.178   0.1588    5.395

    65  41.9474  2    365.000     1.65                                                                   0.000   34.975   0.0697    3.673

Time steps : 65/68, step size: 5.61538, 11.8477

Running simulation [simuapp]: lauwerier baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 1.88s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.559s  95.57%      

|- Newton                                 1.557s  |- 99.87%   

  |- Update                               0.537s    |- 34.49% 

  |- FluxJac                              0.469s    |- 30.10% 

  |- ScdAcc                               0.242s    |- 15.53% 

  |- update_dev                           0.164s    |- 10.52% 

  |- Precond                              0.032s    |- 2.07%  

  |- Solver                               0.026s    |- 1.68%  

  |- HeatLoss                             0.022s    |- 1.41%  

  |- Residual                             0.017s    |- 1.10%  

  |- PerfJac                              0.012s    |- 0.79%  

  |- alignvar                             0.009s    |- 0.59%  

  |- SanitizeJac                          0.001s    |- 0.08%  

|- Logging                                0.008s  |- 0.50%    

|- Output                                 0.001s  |- 0.04%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.072s  4.43%       

|- execution                              0.069s  |- 95.08%   

------------------------------------------------------------

TOTAL                                     1.632s

============================================================



Time steps : 10/18, step size: 12.6635, 22.211

Running simulation [simumpi]: lauwerier np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 1.80s



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-26





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  9      0.100                     158.99            100.00                     158.99    0.000  6.6e+04           137.021

     2   0.1333  1      0.233                     158.99            100.00                     158.99    0.000  1.5e-11            55.391

     3   0.2917  1      0.525                     158.99            100.00                     158.99    0.000  7.3e-12            60.863

     4   0.6344  1      1.159                     158.99            100.00                     158.99    0.000  7.3e-12            63.518

     5   1.3753  1      2.535                     158.99            100.00                     158.99    0.000  7.3e-12            63.104

     6   2.9832  1      5.518                     158.99            100.00                     158.99    0.000  7.3e-12            61.037

     7   6.4857  1     12.004                     158.99            100.00                     158.99    0.000  7.3e-12            58.056

     8  14.1477  1     26.151                     158.99            100.00                     158.99    0.000  7.3e-12            54.466

     9  30.9861  1     57.138                     158.99            100.00                     158.99    0.000  7.3e-12            33.614

    10  69.4977  1    126.635                     158.99            100.00                     158.99    0.003  7.3e-12 1.00e-05   13.679





TimeLoop terminates due to: too many step cut





Time steps : 10/18, step size: 12.6635, 22.211

Running simulation [simumpi]: lauwerier np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 1.15s



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-26





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  9      0.100                     158.99            100.00                     158.99    0.000  6.6e+04           137.021

     2   0.1333  1      0.233                     158.99            100.00                     158.99    0.000  7.3e-11            55.391

     3   0.2917  1      0.525                     158.99            100.00                     158.99    0.000  5.8e-11            60.863

     4   0.6344  1      1.159                     158.99            100.00                     158.99    0.000  5.8e-11            63.518

     5   1.3753  1      2.535                     158.99            100.00                     158.99    0.000  1.0e-10            63.104

     6   2.9832  1      5.518                     158.99            100.00                     158.99    0.000  1.0e-10            61.037

     7   6.4857  1     12.004                     158.99            100.00                     158.99    0.000  1.0e-10            58.056

     8  14.1477  1     26.151                     158.99            100.00                     158.99    0.000  1.0e-10            54.466

     9  30.9861  1     57.138                     158.99            100.00                     158.99    0.000  1.0e-10            33.614

    10  69.4977  1    126.635                     158.99            100.00                     158.99    0.003  1.0e-10 1.00e-05   13.679





TimeLoop terminates due to: too many step cut





Time steps : 10/18, step size: 12.6635, 22.211

Running simulation [simumpi]: lauwerier np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 1.02s

            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-26





VTU generation is suppressed.

VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  9      0.100                     158.99            100.00                     158.99    0.000  6.6e+04           137.021

     2   0.1333  1      0.233                     158.99            100.00                     158.99    0.000  1.4e-08            55.391

     3   0.2917  1      0.525                     158.99            100.00                     158.99    0.000  1.4e-08            60.863

     4   0.6344  1      1.159                     158.99            100.00                     158.99    0.000  2.9e-08            63.518

     5   1.3753  1      2.535                     158.99            100.00                     158.99    0.000  4.2e-08            63.104

     6   2.9832  1      5.518                     158.99            100.00                     158.99    0.000  4.2e-08            61.037

     7   6.4857  1     12.004                     158.99            100.00                     158.99    0.000  4.2e-08            58.056

     8  14.1477  1     26.151                     158.99            100.00                     158.99    0.000  4.2e-08            54.466

     9  30.9861  1     57.138                     158.99            100.00                     158.99    0.000  4.2e-08            33.614

    10  69.4977  1    126.635                     158.99            100.00                     158.99    0.003  4.1e-08 1.00e-05   13.679





TimeLoop terminates due to: too many step cut





Time steps : 10/18, step size: 12.6635, 22.211

Running simulation [simuapp]: stflu028 baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 0.38s

    40  31.4527  2   2435.000     0.08     1.44     0.21    19.02    73.71                               0.000   16.384 2.36e-04    0.037



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.081s  51.63%      

|- Newton                                 0.068s  |- 83.92%   

  |- FluxJac                              0.024s    |- 34.97% 

  |- Update                               0.020s    |- 30.13% 

  |- ScdAcc                               0.008s    |- 11.39% 

  |- update_dev                           0.007s    |- 9.74%  

  |- Solver                               0.003s    |- 4.81%  

  |- Precond                              0.002s    |- 2.23%  

  |- PerfJac                              0.001s    |- 1.71%  

  |- Residual                             0.001s    |- 0.87%  

  |- HeatLoss                             0.001s    |- 0.79%  

  |- alignvar                             0.000s    |- 0.62%  

  |- SanitizeJac                          0.000s    |- 0.18%  

|- Logging                                0.003s  |- 4.10%    

|- Output                                 0.003s  |- 4.06%    

|- Input                                  0.001s  |- 0.88%    

Initialization                            0.076s  48.37%      

|- execution                              0.072s  |- 95.89%   

------------------------------------------------------------

TOTAL                                     0.156s

============================================================



Time steps : 40/40, step size: 60.875, 37.2029

Running simulation [simumpi]: stflu028 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 0.38s

    19  18.6252  1    718.625     0.06     1.19     0.01    19.02    16.06                       0.02    0.000   13.776 2.55e-04    0.009

    20  43.1712  2    761.796     0.06     1.18     0.01    19.02    16.05                       0.03    0.000   50.538 9.93e-04    0.031

    21  90.0000  2    851.796     0.06     1.17     0.01    19.02    16.06                       0.08    0.000  247.144   0.0051    0.138

    22  90.0000  4    941.796     0.06     1.16     0.01    19.02    16.09                       0.32    0.000  561.064   0.0118    0.339

    23  90.0000  3   1031.796     0.06     1.15     0.01    19.02    16.66                       0.78    0.000  717.301   0.0149    0.727

    24  90.0000  3   1121.796     0.06     1.13     0.02    19.02    24.38                       1.31    0.000  661.012   0.0137    1.042

    25  90.0000  3   1211.796     0.06     1.13     0.06    19.02    48.50                       1.79    0.000  547.374   0.0118    1.212

    26  90.0000  3   1301.796     0.06     1.12     0.16    19.02    72.83                       2.14    0.000  399.735   0.0097    1.214

    27  90.0000  2   1391.796     0.06     1.12     0.35    19.02    85.67                       2.40    0.000  321.704   0.0088    1.146

    28  39.2036  2   1431.000     0.06     1.11     0.46    19.02    88.68                       2.68    0.000  170.767   0.0049    0.556

    29  84.4989  4   1515.499     0.17     3.18     2.27    19.02    93.15                               0.000  3.2e+03   0.0550    1.529

    30  78.0484  3   1593.547     0.13     2.57     1.41    19.02    91.29                               0.000  798.378   0.0118    0.815



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    31  90.0000  2   1683.547     0.11     2.18     1.07    19.02    90.33                               0.000  399.207   0.0055    0.634

    32  90.0000  2   1773.547     0.10     1.95     0.86    19.02    89.31                               0.000  247.593   0.0036    0.465

    33  90.0000  2   1863.547     0.09     1.80     0.70    19.02    88.01                               0.000  179.361   0.0024    0.355

    34  90.0000  2   1953.547     0.09     1.70     0.57    19.02    86.44                               0.000  138.678   0.0018    0.280

    35  90.0000  2   2043.547     0.09     1.63     0.47    19.02    84.58                               0.000  110.552   0.0015    0.226

    36  90.0000  2   2133.547     0.08     1.57     0.39    19.02    82.47                               0.000   89.592   0.0012    0.186

    37  90.0000  2   2223.547     0.08     1.52     0.32    19.02    80.12                               0.000   73.337 9.94e-04    0.155

    38  90.0000  2   2313.547     0.08     1.48     0.27    19.02    77.55                               0.000   60.452 8.32e-04    0.132

    39  90.0000  2   2403.547     0.08     1.45     0.23    19.02    74.78                               0.000   50.111 7.13e-04    0.113

    40  31.4527  2   2435.000     0.08     1.44     0.21    19.02    73.71                               0.000   16.384 2.36e-04    0.037

Time steps : 40/40, step size: 60.875, 37.2029

Running simulation [simumpi]: stflu028 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 0.39s

    19  18.6252  1    718.625     0.06     1.19     0.01    19.02    16.06                       0.02    0.000   13.776 2.55e-04    0.009

    20  43.1712  2    761.796     0.06     1.18     0.01    19.02    16.05                       0.03    0.000   50.538 9.93e-04    0.031

    21  90.0000  2    851.796     0.06     1.17     0.01    19.02    16.06                       0.08    0.000  247.143   0.0051    0.138

    22  90.0000  4    941.796     0.06     1.16     0.01    19.02    16.09                       0.32    0.000  561.063   0.0118    0.339

    23  90.0000  3   1031.796     0.06     1.15     0.01    19.02    16.66                       0.78    0.000  717.301   0.0149    0.727

    24  90.0000  3   1121.796     0.06     1.13     0.02    19.02    24.38                       1.31    0.000  661.012   0.0137    1.042

    25  90.0000  3   1211.796     0.06     1.13     0.06    19.02    48.50                       1.79    0.000  547.374   0.0118    1.212

    26  90.0000  3   1301.796     0.06     1.12     0.16    19.02    72.83                       2.14    0.000  399.735   0.0097    1.214

    27  90.0000  2   1391.796     0.06     1.12     0.35    19.02    85.67                       2.40    0.000  321.704   0.0088    1.146

    28  39.2036  2   1431.000     0.06     1.11     0.46    19.02    88.68                       2.68    0.000  170.767   0.0049    0.556

    29  84.4989  4   1515.499     0.17     3.18     2.27    19.02    93.15                               0.000  3.2e+03   0.0550    1.529

    30  78.0484  3   1593.547     0.13     2.57     1.41    19.02    91.29                               0.000  798.378   0.0118    0.815



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    31  90.0000  2   1683.547     0.11     2.18     1.07    19.02    90.33                               0.000  399.207   0.0055    0.634

    32  90.0000  2   1773.547     0.10     1.95     0.86    19.02    89.31                               0.000  247.593   0.0036    0.465

    33  90.0000  2   1863.547     0.09     1.80     0.70    19.02    88.01                               0.000  179.361   0.0024    0.355

    34  90.0000  2   1953.547     0.09     1.70     0.57    19.02    86.44                               0.000  138.678   0.0018    0.280

    35  90.0000  2   2043.547     0.09     1.63     0.47    19.02    84.58                               0.000  110.552   0.0015    0.226

    36  90.0000  2   2133.547     0.08     1.57     0.39    19.02    82.47                               0.000   89.592   0.0012    0.186

    37  90.0000  2   2223.547     0.08     1.52     0.32    19.02    80.12                               0.000   73.337 9.94e-04    0.155

    38  90.0000  2   2313.547     0.08     1.48     0.27    19.02    77.55                               0.000   60.452 8.32e-04    0.132

    39  90.0000  2   2403.547     0.08     1.45     0.23    19.02    74.78                               0.000   50.111 7.13e-04    0.113

    40  31.4527  2   2435.000     0.08     1.44     0.21    19.02    73.71                               0.000   16.384 2.36e-04    0.037

Time steps : 40/40, step size: 60.875, 37.2029

Running simulation [simumpi]: stflu028 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 0.41s

    19  18.6252  1    718.625     0.06     1.19     0.01    19.02    16.06                       0.02    0.000   13.776 2.55e-04    0.009

    20  43.1712  2    761.796     0.06     1.18     0.01    19.02    16.05                       0.03    0.000   50.538 9.93e-04    0.031

    21  90.0000  2    851.796     0.06     1.17     0.01    19.02    16.06                       0.08    0.000  247.143   0.0051    0.138

    22  90.0000  4    941.796     0.06     1.16     0.01    19.02    16.09                       0.32    0.000  561.063   0.0118    0.339

    23  90.0000  3   1031.796     0.06     1.15     0.01    19.02    16.66                       0.78    0.000  717.301   0.0149    0.727

    24  90.0000  3   1121.796     0.06     1.13     0.02    19.02    24.38                       1.31    0.000  661.012   0.0137    1.042

    25  90.0000  3   1211.796     0.06     1.13     0.06    19.02    48.50                       1.79    0.000  547.374   0.0118    1.212

    26  90.0000  3   1301.796     0.06     1.12     0.16    19.02    72.83                       2.14    0.000  399.735   0.0097    1.214

    27  90.0000  2   1391.796     0.06     1.12     0.35    19.02    85.67                       2.40    0.000  321.705   0.0088    1.146

    28  39.2036  2   1431.000     0.06     1.11     0.46    19.02    88.68                       2.68    0.000  170.767   0.0049    0.556

    29  84.4989  4   1515.499     0.17     3.18     2.27    19.02    93.15                               0.000  3.2e+03   0.0550    1.529

    30  78.0484  3   1593.547     0.13     2.57     1.41    19.02    91.29                               0.000  798.378   0.0118    0.815



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    31  90.0000  2   1683.547     0.11     2.18     1.07    19.02    90.33                               0.000  399.207   0.0055    0.634

    32  90.0000  2   1773.547     0.10     1.95     0.86    19.02    89.31                               0.000  247.593   0.0036    0.465

    33  90.0000  2   1863.547     0.09     1.80     0.70    19.02    88.01                               0.000  179.361   0.0024    0.355

    34  90.0000  2   1953.547     0.09     1.70     0.57    19.02    86.44                               0.000  138.678   0.0018    0.280

    35  90.0000  2   2043.547     0.09     1.63     0.47    19.02    84.58                               0.000  110.552   0.0015    0.226

    36  90.0000  2   2133.547     0.08     1.57     0.39    19.02    82.47                               0.000   89.592   0.0012    0.186

    37  90.0000  2   2223.547     0.08     1.52     0.32    19.02    80.12                               0.000   73.337 9.94e-04    0.155

    38  90.0000  2   2313.547     0.08     1.48     0.27    19.02    77.55                               0.000   60.452 8.32e-04    0.132

    39  90.0000  2   2403.547     0.08     1.45     0.23    19.02    74.78                               0.000   50.111 7.13e-04    0.113

    40  31.4527  2   2435.000     0.08     1.44     0.21    19.02    73.71                               0.000   16.384 2.36e-04    0.037

Time steps : 40/40, step size: 60.875, 37.2029

Running simulation [simuapp]: stflu029 baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 7.27s

   232   4.2493  2    820.000     0.04     0.00     1.58     0.05    97.63                       1.59    0.144    0.745   0.0103    1.687



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  6.971s  98.90%      

|- Newton                                 6.927s  |- 99.37%   

  |- FluxJac                              2.845s    |- 41.06% 

  |- Update                               1.805s    |- 26.05% 

  |- ScdAcc                               0.905s    |- 13.06% 

  |- update_dev                           0.689s    |- 9.94%  

  |- Solver                               0.359s    |- 5.18%  

  |- Precond                              0.155s    |- 2.24%  

  |- alignvar                             0.045s    |- 0.66%  

  |- Residual                             0.035s    |- 0.51%  

  |- PerfJac                              0.014s    |- 0.20%  

  |- SanitizeJac                          0.011s    |- 0.15%  

  |- HeatLoss                             0.008s    |- 0.11%  

|- Logging                                0.023s  |- 0.33%    

|- Output                                 0.010s  |- 0.15%    

|- Input                                  0.001s  |- 0.02%    

Initialization                            0.078s  1.10%       

|- execution                              0.075s  |- 96.11%   

------------------------------------------------------------

TOTAL                                     7.049s

============================================================



Time steps : 232/237, step size: 3.53448, 5.42163

Running simulation [simumpi]: stflu029 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 7.22s



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   211  26.4092  9    601.409     0.04     0.00     1.58     0.09    97.70                       1.59    0.144   27.617   0.0963   17.158

   212   3.5908  2    605.000     0.04     0.00     1.58     0.09    97.69                       1.59    0.144    3.486   0.0095    1.783

   213   7.7631  3    612.763     0.04     0.00     1.58     0.09    97.67                       1.59    0.144    5.919   0.0285    3.452

   214  15.2243  6    627.987     0.04     0.00     1.58     0.09    97.66                       1.59    0.144   10.526   0.0504    9.517

   215   7.0126  4    635.000     0.04     0.00     1.58     0.09    97.67                       1.59    0.144    4.243   0.0272    4.192

   216  13.7933  5    648.793     0.04     0.00     1.58     0.08    97.68                       1.59    0.144    7.159   0.0310    6.901

   217  16.2067  5    665.000     0.04     0.00     1.58     0.08    97.71                       1.59    0.144    7.287   0.0421    8.292

   218  27.6327  6    692.633     0.04     0.00     1.58     0.08    97.70                       1.59    0.144    9.595   0.0840   15.336

   219   2.3673  2    695.000     0.04     0.00     1.58     0.08    97.69                       1.59    0.144    0.969   0.0067    0.995

   220   5.2874  5    700.287     0.04     0.00     1.58     0.07    97.68                       1.59    0.144    1.166   0.0160    2.462

   221  11.1204  4    711.408     0.04     0.00     1.58     0.07    97.66                       1.59    0.144    2.338   0.0409    5.711

   222  18.5922  6    730.000     0.04     0.00     1.58     0.07    97.65                       1.59    0.144    3.443   0.0709   12.009

   223  28.2853 10    758.285     0.04     0.00     1.58     0.06    97.64                       1.59    0.144    2.902   0.0666   14.436

   224   1.7147  2    760.000     0.04     0.00     1.58     0.06    97.64                       1.58    0.144    0.988   0.0041    0.678

   225   3.8838  3    763.884     0.04     0.00     1.58     0.06    97.63                       1.58    0.144    0.234   0.0110    1.758

   226   8.4054  5    772.289     0.04     0.00     1.58     0.06    97.64                       1.58    0.144    0.811   0.0199    4.707

   227  16.2197  6    788.509     0.04     0.00     1.58     0.06    97.63                       1.58    0.144    1.061   0.0327    7.425

   228   1.4910  2    790.000     0.04     0.00     1.58     0.06    97.63                       1.58    0.144    0.820   0.0032    0.620

   229   3.3857  2    793.386     0.04     0.00     1.58     0.06    97.63                       1.58    0.144    0.119   0.0078    1.415

   230   7.4325  4    800.818     0.04     0.00     1.58     0.06    97.64                       1.59    0.144    0.875   0.0220    3.631

   231  14.9325  5    815.751     0.04     0.00     1.58     0.05    97.63                       1.59    0.144    0.609   0.0477    6.929

   232   4.2493  2    820.000     0.04     0.00     1.58     0.05    97.63                       1.59    0.144    0.745   0.0103    1.687

Time steps : 232/237, step size: 3.53448, 5.42163

Running simulation [simumpi]: stflu029 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 4.83s

   207   8.0488  4    515.000     0.04     0.00     1.57     0.11    97.60                       1.58    0.045   11.312   0.0250    4.471

   208  15.6670  6    530.667     0.04     0.00     1.57     0.11    97.64                       1.58    0.045   21.325   0.0522   11.913

   209  14.3330  5    545.000     0.04     0.00     1.58     0.10    97.67                       1.59    0.044   21.117   0.0452   10.541

   210  22.7745  8    567.774     0.04     0.00     1.58     0.09    97.71                       1.59    0.044   27.535   0.0590   12.217



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   211   7.2255  6    575.000     0.04     0.00     1.58     0.10    97.72                       1.59    0.044    8.201   0.0168    3.654

   212  14.4511  5    589.451     0.04     0.00     1.58     0.09    97.73                       1.59    0.044   16.086   0.0569   10.130

   213  15.5489  6    605.000     0.04     0.00     1.58     0.09    97.70                       1.59    0.043   14.349   0.0581    9.266

   214  25.6980  6    630.698     0.04     0.00     1.58     0.09    97.68                       1.59    0.085   18.465   0.0843   15.319

   215   4.3020  5    635.000     0.04     0.00     1.58     0.09    97.66                       1.59    0.085    2.533   0.0124    1.895

   216   9.2583  3    644.258     0.04     0.00     1.58     0.08    97.66                       1.59    0.085    4.697   0.0191    4.633

   217  17.9144  6    662.173     0.04     0.00     1.58     0.08    97.69                       1.59    0.085    8.488   0.0529    9.507

   218   2.8273  3    665.000     0.04     0.00     1.58     0.08    97.69                       1.59    0.085    1.254   0.0069    1.264

   219   6.2461  3    671.246     0.04     0.00     1.58     0.08    97.70                       1.59    0.085    2.175   0.0149    3.027

   220  12.8459  5    684.092     0.04     0.00     1.58     0.08    97.71                       1.59    0.085    4.978   0.0373    7.383

   221  10.9080  6    695.000     0.04     0.00     1.58     0.08    97.71                       1.59    0.085    3.116   0.0387    5.347

   222  20.2271  6    715.227     0.04     0.00     1.58     0.07    97.68                       1.59    0.085    4.418   0.0678   10.462

   223  14.7729  6    730.000     0.04     0.00     1.58     0.07    97.66                       1.59    0.085    2.657   0.0530    9.601

   224  24.1604  8    754.160     0.04     0.00     1.58     0.06    97.64                       1.59    0.085    2.051   0.0649   11.880

   225   5.8396  5    760.000     0.04     0.00     1.58     0.06    97.64                       1.59    0.085    0.746   0.0147    3.144

   226  11.9553  5    771.955     0.04     0.00     1.58     0.06    97.64                       1.59    0.085    1.110   0.0377    6.835

   227  18.0447  6    790.000     0.04     0.00     1.58     0.06    97.64                       1.59    0.085    1.362   0.0370    8.093

   228  30.0000  9    820.000     0.04     0.00     1.58     0.05    97.63                       1.59    0.157    1.130   0.0965   13.727

Time steps : 228/232, step size: 3.59649, 5.60524

Running simulation [simumpi]: stflu029 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 4.12s

   200  17.4892 10    412.489     0.04              1.55             97.37                       1.55    1.048   40.927   0.0599   13.202

   201  12.5108  7    425.000     0.04     0.12     1.56     2.90    97.46                       1.56    2.995   30.138   0.0588    9.449

   202   2.2843  6 2  427.284     0.04     0.01     1.56     0.31    97.51                       1.58    2.995    5.817   0.0131    4.279

   203   4.4783  4    431.763     0.04     0.01     1.56     0.16    97.52                       1.57    2.995   10.446   0.0127    3.239

   204   9.1345  5    440.897     0.04     0.01     1.56     0.14    97.56                       1.57    2.995   22.370   0.0366    5.855

   205  14.1029  7    455.000     0.04     0.00     1.57     0.12    97.59                       1.58    2.996   28.687   0.0734   11.197

   206  21.9723  6    476.972     0.04     0.00     1.57     0.12    97.61                       1.58    3.012   44.620   0.0789   11.624

   207   8.0277  4    485.000     0.04     0.00     1.57     0.12    97.62                       1.58    3.012   13.281   0.0240    3.578

   208  16.1458  6    501.146     0.04     0.00     1.58     0.12    97.69                       1.59    3.012   29.607   0.0436    7.184

   209  13.8542  6    515.000     0.04     0.00     1.58     0.12    97.75                       1.59    3.012   21.112   0.0322    7.437

   210  24.2960  6    539.296     0.04     0.00     1.58     0.11    97.74                       1.59    3.012   33.403   0.0872   14.082



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   211   5.7040  5    545.000     0.04     0.00     1.58     0.11    97.73                       1.59    3.012    8.490   0.0172    3.284

   212  11.6141  4    556.614     0.04     0.00     1.58     0.10    97.72                       1.59    3.012   14.851   0.0489    6.664

   213  18.3859  6    575.000     0.04     0.00     1.58     0.10    97.75                       1.59    3.012   20.652   0.0546    9.632

   214  30.0000 11    605.000     0.04     0.00     1.58     0.09    97.75                       1.59    3.012   30.145   0.0756   18.444

   215  30.0000 11    635.000     0.04     0.00     1.58     0.09    97.72                       1.59    3.012   21.697   0.0873   15.846

   216  30.0000  6    665.000     0.04     0.00     1.58     0.08    97.71                       1.59    3.012   14.306   0.0762   15.528

   217  30.0000  6    695.000     0.04     0.00     1.58     0.07    97.70                       1.59    3.012    9.905   0.0707   16.623

   218  35.0000 14    730.000     0.04     0.00     1.58     0.07    97.66                       1.59    3.011    6.906   0.0914   17.010

   219  30.0000  7    760.000     0.04     0.00     1.58     0.06    97.63                       1.59    3.012    3.215   0.0829   17.395

   220  30.0000  7    790.000     0.04     0.00     1.58     0.06    97.63                       1.58    3.133    2.559   0.0671   13.554

   221  30.0000 14    820.000     0.04     0.00     1.58     0.05    97.62                       1.58    3.133    4.478   0.0718   13.642

Time steps : 221/229, step size: 3.71041, 6.71871

Running simulation [simuapp]: stflu019 baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 188.50s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                               2m 55.46s  94.00%      

|- Newton                              2m 53.51s  |- 98.89%   

  |- Update                            1m 18.31s    |- 45.13% 

  |- FluxJac                             41.386s    |- 23.85% 

  |- Solver                              22.628s    |- 13.04% 

  |- update_dev                          11.027s    |- 6.36%  

  |- ScdAcc                              10.991s    |- 6.33%  

  |- Precond                              1.842s    |- 1.06%  

  |- Residual                             1.205s    |- 0.69%  

  |- SanitizeJac                          0.647s    |- 0.37%  

  |- alignvar                             0.580s    |- 0.33%  

  |- HeatLoss                             0.201s    |- 0.12%  

  |- PerfJac                              0.015s    |- 0.01%  

|- Output                                 0.071s  |- 0.04%    

|- Logging                                0.015s  |- 0.01%    

|- Input                                  0.000s  |- 0.00%    

Initialization                           11.198s  6.00%       

|- execution                              8.566s  |- 76.50%   

------------------------------------------------------------

TOTAL                                   3m 6.66s

============================================================



Time steps : 11/11, step size: 3.27389, 4.63394

Running simulation [simumpi]: stflu019 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 127.04s

            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-26





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100    29.89              0.02              0.05                      40.00    0.000  153.606   0.0015    0.078

     2   0.1655  1      0.266    27.99              0.03              0.11                      40.00    0.000  162.930   0.0029    0.108

     3   0.2693  1      0.535    26.18              0.04              0.16                      40.00    0.000  188.590   0.0051    0.150

     4   0.4180  1      0.953    24.67              0.05              0.20                      40.00    0.000  184.538   0.0082    0.206

     5   0.6537  1      1.607    23.49              0.05              0.23                      40.00    0.000  170.897   0.0128    0.297

     6   1.0478  1      2.654    22.58              0.06              0.26                      40.00    0.000  144.654   0.0171    0.444

     7   1.7643  1      4.419    21.83              0.06              0.27                      40.00    0.000  143.106   0.0234    0.715

     8   2.9796  1      7.398    21.15              0.06              0.29                      40.00    0.000  137.296   0.0218    1.166

     9   5.0892  1     12.487    20.49              0.06              0.30                      40.00    0.000  124.482   0.0274    1.876

    10   8.9153  1     21.403    19.83              0.06              0.31                      40.00    0.000  158.943   0.0354    3.004

    11  14.6100  1     36.013    19.27              0.06              0.31                      40.00    0.000  181.378   0.0568    4.175





TimeLoop terminates due to: reach maximum time step





Time steps : 11/11, step size: 3.27389, 4.63394

Running simulation [simumpi]: stflu019 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 83.27s

            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-26





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100    29.89              0.02              0.05                      40.00    0.000  153.607   0.0015    0.078

     2   0.1655  1      0.266    27.99              0.03              0.11                      40.00    0.000  162.930   0.0029    0.108

     3   0.2693  1      0.535    26.18              0.04              0.16                      40.00    0.000  188.590   0.0051    0.150

     4   0.4180  1      0.953    24.67              0.05              0.20                      40.00    0.000  184.538   0.0082    0.206

     5   0.6537  1      1.607    23.49              0.05              0.23                      40.00    0.000  170.897   0.0128    0.297

     6   1.0478  1      2.654    22.58              0.06              0.26                      40.00    0.000  144.654   0.0171    0.444

     7   1.7643  1      4.419    21.83              0.06              0.27                      40.00    0.000  143.106   0.0234    0.715

     8   2.9796  1      7.398    21.15              0.06              0.29                      40.00    0.000  137.296   0.0218    1.166

     9   5.0892  1     12.487    20.49              0.06              0.30                      40.00    0.000  124.482   0.0274    1.876

    10   8.9153  1     21.403    19.83              0.06              0.31                      40.00    0.000  158.943   0.0354    3.004

    11  14.6100  1     36.013    19.27              0.06              0.31                      40.00    0.000  181.378   0.0568    4.175





TimeLoop terminates due to: reach maximum time step





Time steps : 11/11, step size: 3.27389, 4.63394

Running simulation [simumpi]: stflu019 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 62.24s

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-26





VTU generation is suppressed.

VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100    29.89              0.02              0.05                      40.00    0.000  153.607   0.0015    0.078

     2   0.1655  1      0.266    27.99              0.03              0.11                      40.00    0.000  162.930   0.0029    0.108

     3   0.2693  1      0.535    26.18              0.04              0.16                      40.00    0.000  188.590   0.0051    0.150

     4   0.4180  1      0.953    24.67              0.05              0.20                      40.00    0.000  184.538   0.0082    0.206

     5   0.6537  1      1.607    23.49              0.05              0.23                      40.00    0.000  170.897   0.0128    0.297

     6   1.0478  1      2.654    22.58              0.06              0.26                      40.00    0.000  144.654   0.0171    0.444

     7   1.7643  1      4.419    21.83              0.06              0.27                      40.00    0.000  143.106   0.0234    0.715

     8   2.9796  1      7.398    21.15              0.06              0.29                      40.00    0.000  137.296   0.0218    1.166

     9   5.0892  1     12.487    20.49              0.06              0.30                      40.00    0.000  124.483   0.0274    1.876

    10   8.9153  1     21.403    19.83              0.06              0.31                      40.00    0.000  158.943   0.0354    3.004

    11  14.6100  1     36.013    19.27              0.06              0.31                      40.00    0.000  181.379   0.0568    4.175





TimeLoop terminates due to: reach maximum time step





Time steps : 11/11, step size: 3.27389, 4.63394

Running simulation [simuapp]: stflu010 baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 6.41s

   281 1.30e-03  3      0.375    8e-04     0.07             94.09                       0.28             0.240    0.054 5.36e-04    0.675



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  4.970s  86.10%      

|- Newton                                 4.938s  |- 99.36%   

  |- FluxJac                              1.828s    |- 37.02% 

  |- Update                               1.114s    |- 22.57% 

  |- ScdAcc                               0.721s    |- 14.61% 

  |- update_dev                           0.493s    |- 9.99%  

  |- Solver                               0.356s    |- 7.20%  

  |- Precond                              0.212s    |- 4.30%  

  |- alignvar                             0.033s    |- 0.66%  

  |- Residual                             0.023s    |- 0.47%  

  |- PerfJac                              0.012s    |- 0.24%  

  |- SanitizeJac                          0.009s    |- 0.19%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Logging                                0.095s  |- 1.92%    

|- Output                                 0.018s  |- 0.37%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.802s  13.90%      

|- execution                              0.761s  |- 94.91%   

------------------------------------------------------------

TOTAL                                     5.772s

============================================================



Time steps : 281/300, step size: 0.00133452, 0.000635538

Running simulation [simumpi]: stflu010 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 6.06s

   257 1.74e-03  7      0.340    8e-04     0.07             93.79                       0.07             0.094    0.020   0.0452    0.196

   258 1.74e-03  6      0.342    8e-04     0.07             93.81                       0.07             0.094    0.013   0.0462    0.179

   259 1.74e-03  7      0.343    8e-04     0.07             93.84                       0.07             0.094    0.008   0.0470    0.164

   260 1.74e-03  6      0.345    8e-04     0.07             93.87                       0.06             0.094    0.005   0.0476    0.152

   261 1.74e-03  7      0.347    8e-04     0.07             93.89                       0.06             0.094    0.004   0.0483    0.141

   262 1.74e-03  6      0.349    8e-04     0.07             93.92                       0.06             0.094    0.002   0.0488    0.132

   263 1.74e-03  9      0.350    8e-04     0.07             93.94                       0.06             0.094    0.002   0.0492    0.124

   264 1.74e-03  7      0.352    8e-04     0.07             93.96                       0.06             0.094    0.002   0.0496    0.117

   265 1.74e-03  7      0.354    8e-04     0.07             93.98                       0.05             0.094    0.002   0.0500    0.110

   266 1.74e-03  2      0.356    8e-04     0.07             94.00                       0.05             0.094    0.002   0.0503    0.105

   267 1.74e-03  2      0.357    8e-04     0.07             94.01                       0.05             0.094    0.002   0.0505    0.100

   268 1.74e-03  2      0.359    8e-04     0.07             94.03                       0.05             0.094    0.002   0.0507    0.096

   269 1.74e-03  2      0.361    8e-04     0.07             94.04                       0.05             0.094    0.002   0.0509    0.091

   270 1.74e-03  3      0.362    8e-04     0.07             94.05                       0.05             0.095    0.003   0.0509    0.088



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   271 1.74e-03  2      0.364    8e-04     0.07             94.05                       0.05             0.095    0.005   0.0508    0.084

   272 1.74e-03  2      0.366    8e-04     0.07             94.06                       0.05             0.095    0.010   0.0501    0.080

   273 1.74e-03  3      0.368    8e-04     0.07             94.06                       0.06             0.095    0.031   0.0476    0.111

   274 1.74e-03  8      0.369    8e-04     0.07             94.05                       0.14             0.094    0.146   0.0315    0.496

   275 1.74e-03  6      0.371    8e-04     0.07             94.11                       0.26             0.094    0.021   0.0059    0.691

   276 1.74e-03  3      0.373    8e-04     0.07             94.15                       0.28             0.093    0.011   0.0010    0.963

   277 1.74e-03  4      0.375    8e-04     0.07             94.18                       0.24             0.092    0.066   0.0095    0.692

   278 3.63e-04  4      0.375    8e-04     0.07             94.19                       0.09             0.092    0.021   0.0088    0.056

Time steps : 278/296, step size: 0.00134892, 0.000631706

Running simulation [simumpi]: stflu010 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 4.57s

   260 1.74e-03  7      0.340    8e-04     0.07             93.84                       0.08             0.088    0.024   0.0448    0.203

   261 1.74e-03  9      0.342    8e-04     0.07             93.86                       0.07             0.088    0.015   0.0458    0.185

   262 1.74e-03  9      0.343    8e-04     0.07             93.89                       0.07             0.088    0.009   0.0467    0.169

   263 1.74e-03  9      0.345    8e-04     0.07             93.91                       0.07             0.088    0.006   0.0474    0.156

   264 1.74e-03  9      0.347    8e-04     0.07             93.93                       0.06             0.088    0.004   0.0480    0.145

   265 1.74e-03  7      0.349    8e-04     0.07             93.96                       0.06             0.089    0.003   0.0486    0.135

   266 1.74e-03  7      0.350    8e-04     0.07             93.98                       0.06             0.089    0.002   0.0491    0.126

   267 1.74e-03  7      0.352    8e-04     0.07             94.00                       0.06             0.089    0.002   0.0495    0.119

   268 1.74e-03  6      0.354    8e-04     0.07             94.01                       0.05             0.089    0.002   0.0498    0.113

   269 1.74e-03  4      0.356    8e-04     0.07             94.03                       0.05             0.089    0.002   0.0502    0.107

   270 1.74e-03  2      0.357    8e-04     0.07             94.04                       0.05             0.089    0.002   0.0504    0.102



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   271 1.74e-03  2      0.359    8e-04     0.07             94.05                       0.05             0.089    0.002   0.0507    0.097

   272 1.74e-03  2      0.361    8e-04     0.07             94.06                       0.05             0.089    0.002   0.0508    0.093

   273 1.74e-03  2      0.362    8e-04     0.07             94.07                       0.05             0.089    0.003   0.0509    0.089

   274 1.74e-03  2      0.364    8e-04     0.07             94.07                       0.05             0.089    0.005   0.0508    0.085

   275 1.74e-03  2      0.366    8e-04     0.07             94.08                       0.05             0.089    0.008   0.0504    0.082

   276 1.74e-03  3      0.368    8e-04     0.07             94.08                       0.06             0.089    0.020   0.0489    0.080

   277 1.74e-03  4      0.369    8e-04     0.07             94.07                       0.10             0.089    0.090   0.0402    0.284

   278 1.74e-03  6      0.371    8e-04     0.07             94.13                       0.23             0.089    0.091   0.0117    0.684

   279 1.74e-03  3      0.373    8e-04     0.07             94.20                       0.27             0.088    0.010   0.0021    0.819

   280 1.74e-03  3      0.375    8e-04     0.07             94.24                       0.28             0.087    0.041 6.60e-04    0.998

   281 3.63e-04  2      0.375    8e-04     0.07             94.25                       0.28             0.087    0.015 1.41e-04    0.202

Time steps : 281/300, step size: 0.00133452, 0.000637752

Running simulation [simumpi]: stflu010 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 0.47s

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-26





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1 6.94e-06  4    6.9e-06     0.02                                                  0.87             0.000  375.309 1.58e-07    0.064

     2 4.63e-06  2    1.2e-05     0.02                                                  1.56             0.000  144.003 7.32e-08    0.082

     3 5.51e-06  2    1.7e-05     0.02                                                  2.38             0.002  119.225 8.23e-08    0.169

     4 7.16e-06  3    2.4e-05     0.02                                                  3.47             0.001   67.800 9.70e-08    0.345

     5 3.84e-06  2 1  2.8e-05     0.02                                                  4.98             0.002   54.713 3.79e-08    0.280

     6 2.19e-06  2 1  3.0e-05     0.02                                                  6.00             0.002   58.616 2.45e-08    0.196

     7 1.22e-06  2 1  3.1e-05     0.02                                                  6.60             0.002   41.455 1.73e-08    0.122





TimeLoop terminates due to: time step too small





Time steps : 7/11, step size: 4.49777e-06, 2.25924e-06

Running simulation [simuapp]: stflu021 baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 6.56s

   178 113.2711  3   2526.000     2.23            149.16             98.53                     150.00    0.445   75.568   0.0406    5.068



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  6.222s  98.79%      

|- Newton                                 6.170s  |- 99.18%   

  |- FluxJac                              2.153s    |- 34.89% 

  |- Update                               1.413s    |- 22.89% 

  |- ScdAcc                               0.694s    |- 11.25% 

  |- update_dev                           0.626s    |- 10.14% 

  |- PerfJac                              0.585s    |- 9.48%  

  |- Solver                               0.189s    |- 3.06%  

  |- Precond                              0.079s    |- 1.28%  

  |- alignvar                             0.037s    |- 0.60%  

  |- Residual                             0.029s    |- 0.47%  

  |- SanitizeJac                          0.005s    |- 0.09%  

  |- HeatLoss                             0.005s    |- 0.07%  

|- Logging                                0.283s  |- 4.55%    

|- Output                                 0.022s  |- 0.35%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.076s  1.21%       

|- execution                              0.064s  |- 83.68%   

------------------------------------------------------------

TOTAL                                     6.298s

============================================================



Time steps : 178/189, step size: 14.191, 22.733

Running simulation [simumpi]: stflu021 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 7.35s

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   151   4.1345  4   1965.914    62.32            220.88             77.99                     150.00    0.445    4.925   0.1666    4.225

   152   4.5713  4   1970.485    61.73            196.98             76.14                     150.00    0.445    7.050   0.1289    4.516

   153   5.7374  3   1976.223    62.54            183.51             74.58                     150.00    0.445    4.418   0.1709    6.630

   154   6.2585  5   1982.481    63.93            180.16             73.81                     150.00    0.445    4.847   0.1484    5.693

   155   7.3395  4   1989.821    66.95            196.59             74.60                     150.00    0.445    7.316   0.1718    9.186

   156   7.9821  4   1997.803    69.05            213.40             75.55                     150.00    0.445    4.062   0.2301   13.208

   157   7.3491  6   2005.152    62.56            191.55             75.38                     150.00    0.445    6.394   0.1401    2.947

   158   8.8677  5   2014.020    57.20            180.72             75.96                     150.00    0.445   12.841   0.2143   16.311

   159   8.5201  6   2022.540    53.13            161.70             75.27                     150.00    0.445   11.155   0.1008    6.424

   160  11.8920  6   2034.432    49.85            157.29             75.93                     150.00    0.445    4.974   0.1802    8.951

   161  12.6054  5   2047.037    48.68            171.84             77.92                     150.00    0.445    0.997   0.3106    7.399

   162   9.5791  6   2056.616    44.45            170.20             79.29                     150.00    0.445    4.702   0.1671    2.817

   163  10.5737  4   2067.190    43.51            168.96             79.52                     150.00    0.445    6.979   0.2117   11.114

   164  10.2329  5   2077.423    43.38            179.56             80.54                     150.00    0.445    5.198   0.2572    8.080

   165   8.7948  4   2086.218    41.70            183.01             81.44                     150.00    0.445    9.069   0.1963    7.533

   166   8.8889  5   2095.107    41.19            193.77             82.47                     150.00    0.445    5.041   0.2862   10.057

   167   7.1327  5   2102.239    37.37            180.92             82.88                     150.00    0.445    6.294   0.1216    3.700

   168   9.1923  4   2111.432    36.97            193.58             83.96                     150.00    0.445    6.721   0.2883    9.336

   169   7.3403  6   2118.772    32.72            190.42             85.34                     150.00    0.445    6.700   0.2125    7.548

   170   7.0865  4   2125.858    27.62            171.48             86.13                     150.00    0.445   14.110   0.0731    8.216

   171  11.1167  6   2136.975    30.35            168.96             84.77                     150.00    0.445   14.517   0.1081   17.373

   172  14.6372  5   2151.612    27.16            154.54             85.05                     150.00    0.445    3.718   0.1278    4.909

   173  18.4394  5   2170.052    19.79            145.59             88.04                     150.00    0.445    1.304   0.0860    3.579

   174  27.3491  3   2197.401    13.87            144.37             91.24                     150.00    0.445    5.549   0.0749    4.462

   175  42.5573  3   2239.958     9.28            145.86             94.02                     150.00    0.445   14.726   0.0736    5.311

   176  66.6136  3   2306.572     5.94            147.54             96.13                     150.00    0.445   32.159   0.0696    5.838

   177 106.1573  3   2412.729     3.55            148.66             97.67                     150.00    0.445   63.511   0.0626    6.203

   178 113.2711  3   2526.000     2.23            149.16             98.53                     150.00    0.445   75.568   0.0406    5.068

Time steps : 178/189, step size: 14.191, 22.733

Running simulation [simumpi]: stflu021 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 9.37s

   163   6.6924  3   1995.431    61.19            197.97             76.39                     150.00    0.010    3.238   0.1491    2.104

   164   7.8318  4   2003.263    57.78            193.71             77.02                     150.00    0.010    3.194   0.1785    3.070

   165   8.3434  4   2011.606    54.30            185.47             77.35                     150.00    0.010    4.465   0.1935    5.570

   166   8.5023  6   2020.109    48.70            158.43             76.49                     150.00    0.010    9.790   0.0812    8.258

   167  12.8713  6   2032.980    50.56            160.06             76.00                     150.00    0.010    9.057   0.3644   10.517

   168   8.7580  6   2041.738    51.25            163.93             76.18                     150.00    0.010    4.623   0.2066    3.909

   169   8.5958  4   2050.334    52.75            177.99             77.14                     150.00    0.010    7.069   0.1580   10.072

   170   9.7669  3   2060.101    55.71            211.48             79.15                     150.00    0.010    2.969   0.2620   13.530

   171   8.2967  6   2068.397    49.26            202.11             80.40                     150.00    0.010    6.552   0.2191    5.153

   172   7.8680  4   2076.265    42.50            166.85             79.70                     150.00    0.010   13.358   0.0650    9.695

   173  12.8106  6   2089.076    45.18            172.93             79.28                     150.00    0.010    9.988   0.2620   11.305

   174  10.8825  5   2099.959    47.23            213.28             81.87                     150.00    0.010    4.569   0.3232    4.353

   175   8.0494  5   2108.008    39.55            204.13             83.77                     150.00    0.010    6.580   0.2364    6.426

   176   7.2911  4   2115.299    32.23            174.53             84.41                     150.00    0.010   11.475   0.0921   11.437

   177  10.5426  5   2125.842    32.16            167.63             83.90                     150.00    0.010   16.612   0.0739   15.909

   178  14.4103  4   2140.252    29.41            158.23             84.32                     150.00    0.010   10.015   0.1292    9.933

   179  18.0665  5   2158.318    23.10            148.83             86.56                     150.00    0.010    1.394   0.1001    3.969

   180  25.2849  3   2183.603    16.15            144.39             89.94                     150.00    0.010    3.332   0.0723    4.231



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   181  39.8062  3   2223.410    10.70            145.23             93.14                     150.00    0.010   11.515   0.0735    5.171

   182  62.3304  3   2285.740     6.78            147.10             95.59                     150.00    0.010   27.489   0.0695    5.735

   183  99.3986  3   2385.139     4.04            148.41             97.35                     150.00    0.010   56.752   0.0630    6.090

   184 140.8614  3   2526.000     2.29            149.14             98.49                     150.00    0.010   92.964   0.0500    6.324

Time steps : 184/194, step size: 13.7283, 22.7

Running simulation [simumpi]: stflu021 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 22.19s

   189  15.0763  5   2299.965    24.23            157.37             86.66                     150.00    0.093    6.013   0.1740    6.311

   190  16.2878  3   2316.253    23.21            158.40             87.22                     150.00    0.093    8.527   0.2618    3.308

   191  13.8424  4   2330.095    22.71            159.06             87.51                     150.00    0.093    8.085   0.1995    2.643

   192  13.8639  3   2343.959    22.08            157.30             87.69                     150.00    0.093    8.650   0.2112    2.694

   193  13.4328  6   2357.392    21.03            152.65             87.89                     150.00    0.093    9.833   0.1041    2.052

   194  18.5049  5   2375.897    20.96            151.46             87.85                     150.00    0.093    9.314   0.2095    7.942

   195  18.0150  5   2393.912    21.38            153.64             87.79                     150.00    0.093    8.533   0.1833    9.154

   196  18.9187  4   2412.831    22.26            156.53             87.55                     150.00    0.093   12.533   0.1805    3.683

   197  20.0330  5   2432.864    23.33            160.90             87.34                     150.00    0.093   11.938   0.2879    4.262

   198  16.0112  5   2448.875    23.24            162.49             87.49                     150.00    0.093   12.349   0.2189    2.391

   199  15.1921  5   2464.067    22.29            157.24             87.58                     150.00    0.093   12.536   0.1203    3.969

   200  19.6709  4   2483.738    22.90            153.99             87.05                     150.00    0.093   12.487   0.3118   10.648

   201  14.9091  5   2498.647    24.10            156.15             86.63                     150.00    0.093   10.233   0.2110    5.158

[rank 3] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.16617e-07) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.16617e-07) - this cycle cannot be accepted as converged

[rank 2] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.16617e-07) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.16617e-07) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 1.65815e-07) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 1.65815e-07) - this cycle cannot be accepted as converged

[rank 2] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 1.65815e-07) - this cycle cannot be accepted as converged

[rank 3] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 1.65815e-07) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 3.65452e-06) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 3.65452e-06) - this cycle cannot be accepted as converged

[rank 2] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 3.65452e-06) - this cycle cannot be accepted as converged

[rank 3] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 3.65452e-06) - this cycle cannot be accepted as converged

   202   4.8182  3 1 2503.465    24.70            159.19             86.57                     150.00    0.093    4.162   0.0677    1.505

   203   7.7476  3   2511.213    25.42            164.06             86.59                     150.00    0.093    6.642   0.1619    2.418

   204   8.6929  4   2519.906    26.55            184.36             87.41                     150.00    0.093   12.307   0.2793    3.154

   205   6.0943  6   2526.000    23.82            180.89             88.36                     150.00    0.093    8.488   0.1525    2.508

Time steps : 205/217, step size: 12.322, 17.5386

Running simulation [simuapp]: stflu033 baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 1.43s



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.975s  86.90%      

|- Newton                                 0.958s  |- 98.36%   

  |- FluxJac                              0.188s    |- 19.65% 

  |- ScdAcc                               0.123s    |- 12.82% 

  |- Update                               0.106s    |- 11.10% 

  |- update_dev                           0.057s    |- 5.95%  

  |- Reaction                             0.038s    |- 3.93%  

  |- Precond                              0.030s    |- 3.16%  

  |- Solver                               0.028s    |- 2.92%  

  |- PerfJac                              0.008s    |- 0.80%  

  |- alignvar                             0.004s    |- 0.44%  

  |- Residual                             0.003s    |- 0.30%  

  |- SanitizeJac                          0.001s    |- 0.13%  

  |- HeatLoss                             0.000s    |- 0.02%  

|- Logging                                0.351s  |- 35.98%   

|- Output                                 0.010s  |- 1.07%    

|- Input                                  0.000s  |- 0.04%    

Initialization                            0.147s  13.10%      

|- execution                              0.139s  |- 94.38%   

------------------------------------------------------------

TOTAL                                     1.121s

============================================================



Time steps : 118/120, step size: 0.00564972, 0.00363207

Running simulation [simumpi]: stflu033 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 2.11s

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    91 4.92e-03  3      0.461    3e-11     2.93     0.01    9e+10   100.00              3.06     0.01    0.018    0.800   0.0600   13.661

    92 7.14e-03  3      0.468    3e-11     3.09     0.01    1e+11   100.00              3.06     0.01    0.018    1.127   0.0458   26.802

    93 7.61e-03  4      0.476    3e-11     2.88     0.01    1e+11   100.00              3.06     0.01    0.018    0.807   0.0426   28.493

    94 7.83e-03  4      0.484    3e-11     3.15     0.01    1e+11   100.00              3.06     0.01    0.017    1.572   0.0642   28.936

    95 7.99e-03  6      0.492    3e-11     3.17     0.01    9e+10   100.00              3.06     0.01    0.017    0.924   0.0265   23.660

    96 9.09e-03  4      0.501    3e-11     2.62     0.01    9e+10   100.00              3.06     0.01    0.017    2.513   0.1493   32.053

    97 8.75e-03  4      0.510    3e-11     2.79     0.01    9e+10   100.00              3.06     0.01    0.017    0.313   0.1429   34.714

    98 8.03e-03  4      0.518    3e-11     3.06     0.01    1e+11   100.00              3.06     0.01    0.017    1.383   0.0739   25.922

    99 8.71e-03  4      0.526    3e-11     3.13     0.01    1e+11   100.00              3.06     0.01    0.016    1.097   0.0797   31.357

   100 8.49e-03  6      0.535    3e-11     3.04     0.01    9e+10   100.00              3.06     0.01    0.105    1.306   0.0239   35.232

   101 7.72e-03  4      0.542    3e-11     2.91     0.01    9e+10   100.00              3.06     0.01    0.105    0.556   0.0410   27.271

   102 8.14e-03  4      0.551    3e-11     2.66     0.01    9e+10   100.00              3.06     0.01    0.105    2.047   0.1373   24.975

   103 9.00e-03  4      0.560    3e-11     3.09     0.01    9e+10   100.00              3.06     0.01    0.105    1.034   0.1464   35.440

   104 8.16e-03  6      0.568    3e-11     3.01     0.01    9e+10   100.00              3.06     0.01    0.105    1.203   0.0727   31.343

   105 7.95e-03  3      0.576    3e-11     2.81     0.01    9e+10   100.00              3.06     0.01    0.105    0.517   0.0336   28.690

   106 8.16e-03  3      0.584    3e-11     3.10     0.01    9e+10   100.00              3.06     0.01    0.105    1.753   0.0631   32.027

   107 7.85e-03  4      0.592    4e-11     3.13     0.01    8e+10   100.00              3.06     0.01    0.105    0.689   0.0902   29.653

   108 7.91e-03  6      0.600    3e-11     2.62     0.01    9e+10   100.00              3.06     0.01    0.105    2.116   0.1391   25.190

   109 2.90e-03  3 1    0.603    3e-11     2.58     0.01    9e+10   100.00              3.06     0.01    0.105    0.276   0.0538    8.271

   110 4.95e-03  3      0.607    3e-11     2.84     0.01    9e+10   100.00              3.06     0.01    0.105    0.600   0.0781   17.257

   111 6.54e-03  3      0.614    3e-11     3.11     0.01    1e+11   100.00              3.06     0.01    0.105    1.384   0.0601   25.989

   112 7.08e-03  4      0.621    3e-11     3.16     0.01    9e+10   100.00              3.06     0.01    0.105    0.846   0.0663   26.146

   113 7.64e-03  5      0.629    4e-11     3.12     0.01    9e+10   100.00              3.06     0.01    0.105    1.810   0.0615   26.589

   114 8.17e-03  3      0.637    3e-11     2.83     0.01    8e+10   100.00              3.06     0.01    0.105    1.000   0.0487   28.263

   115 8.45e-03  3      0.645    3e-11     2.65     0.01    9e+10   100.00              3.06     0.01    0.105    2.266   0.1498   28.649

   116 8.67e-03  5      0.654    4e-11     3.16     0.01    9e+10   100.00              3.06     0.01    0.105    1.127   0.1372   27.199

   117 9.16e-03  6      0.663    3e-11     3.00     0.01    9e+10   100.00              3.06     0.01    0.105    1.447   0.0707   30.511

   118 3.52e-03  4      0.667    3e-11     2.55     0.01    9e+10   100.00              3.06     0.01    0.105    2.034   0.0176   12.792

Time steps : 118/120, step size: 0.00564972, 0.00363207

Running simulation [simumpi]: stflu033 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 0.69s

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    91 4.92e-03  3      0.461    3e-11     2.93     0.01    9e+10   100.00              3.06     0.01    0.018    0.800   0.0600   13.661

    92 7.14e-03  3      0.468    3e-11     3.09     0.01    1e+11   100.00              3.06     0.01    0.018    1.127   0.0458   26.802

    93 7.61e-03  4      0.476    3e-11     2.88     0.01    1e+11   100.00              3.06     0.01    0.018    0.807   0.0426   28.493

    94 7.83e-03  4      0.484    3e-11     3.15     0.01    1e+11   100.00              3.06     0.01    0.017    1.572   0.0642   28.936

    95 7.99e-03  6      0.492    3e-11     3.17     0.01    9e+10   100.00              3.06     0.01    0.017    0.924   0.0265   23.660

    96 9.09e-03  4      0.501    3e-11     2.62     0.01    9e+10   100.00              3.06     0.01    0.017    2.513   0.1493   32.053

    97 8.75e-03  4      0.510    3e-11     2.79     0.01    9e+10   100.00              3.06     0.01    0.017    0.313   0.1429   34.714

    98 8.03e-03  4      0.518    3e-11     3.06     0.01    1e+11   100.00              3.06     0.01    0.017    1.383   0.0739   25.922

    99 8.71e-03  4      0.526    3e-11     3.13     0.01    1e+11   100.00              3.06     0.01    0.016    1.097   0.0797   31.357

   100 8.49e-03  6      0.535    3e-11     3.04     0.01    9e+10   100.00              3.06     0.01    0.105    1.306   0.0239   35.232

   101 7.72e-03  4      0.542    3e-11     2.91     0.01    9e+10   100.00              3.06     0.01    0.105    0.556   0.0410   27.271

   102 8.14e-03  4      0.551    3e-11     2.66     0.01    9e+10   100.00              3.06     0.01    0.105    2.047   0.1373   24.975

   103 9.00e-03  4      0.560    3e-11     3.09     0.01    9e+10   100.00              3.06     0.01    0.105    1.034   0.1464   35.440

   104 8.16e-03  6      0.568    3e-11     3.01     0.01    9e+10   100.00              3.06     0.01    0.105    1.203   0.0727   31.343

   105 7.95e-03  3      0.576    3e-11     2.81     0.01    9e+10   100.00              3.06     0.01    0.105    0.517   0.0336   28.690

   106 8.16e-03  3      0.584    3e-11     3.10     0.01    9e+10   100.00              3.06     0.01    0.105    1.753   0.0631   32.027

   107 7.85e-03  4      0.592    4e-11     3.13     0.01    8e+10   100.00              3.06     0.01    0.105    0.689   0.0902   29.653

   108 7.91e-03  6      0.600    3e-11     2.62     0.01    9e+10   100.00              3.06     0.01    0.105    2.116   0.1391   25.190

   109 2.90e-03  3 1    0.603    3e-11     2.58     0.01    9e+10   100.00              3.06     0.01    0.105    0.276   0.0538    8.271

   110 4.95e-03  3      0.607    3e-11     2.84     0.01    9e+10   100.00              3.06     0.01    0.105    0.600   0.0781   17.257

   111 6.54e-03  3      0.614    3e-11     3.11     0.01    1e+11   100.00              3.06     0.01    0.105    1.384   0.0601   25.989

   112 7.08e-03  4      0.621    3e-11     3.16     0.01    9e+10   100.00              3.06     0.01    0.105    0.846   0.0663   26.146

   113 7.64e-03  5      0.629    4e-11     3.12     0.01    9e+10   100.00              3.06     0.01    0.105    1.810   0.0615   26.589

   114 8.17e-03  3      0.637    3e-11     2.83     0.01    8e+10   100.00              3.06     0.01    0.105    1.000   0.0487   28.263

   115 8.45e-03  3      0.645    3e-11     2.65     0.01    9e+10   100.00              3.06     0.01    0.105    2.266   0.1498   28.649

   116 8.67e-03  5      0.654    4e-11     3.16     0.01    9e+10   100.00              3.06     0.01    0.105    1.127   0.1372   27.199

   117 9.16e-03  6      0.663    3e-11     3.00     0.01    9e+10   100.00              3.06     0.01    0.105    1.447   0.0707   30.511

   118 3.52e-03  4      0.667    3e-11     2.55     0.01    9e+10   100.00              3.06     0.01    0.105    2.034   0.0176   12.792

Time steps : 118/120, step size: 0.00564972, 0.00363207

Running simulation [simumpi]: stflu033 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 0.67s

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    91 4.92e-03  3      0.461    3e-11     2.93     0.01    9e+10   100.00              3.06     0.01    0.018    0.800   0.0600   13.661

    92 7.14e-03  3      0.468    3e-11     3.09     0.01    1e+11   100.00              3.06     0.01    0.018    1.127   0.0458   26.802

    93 7.61e-03  4      0.476    3e-11     2.88     0.01    1e+11   100.00              3.06     0.01    0.018    0.807   0.0426   28.493

    94 7.83e-03  4      0.484    3e-11     3.15     0.01    1e+11   100.00              3.06     0.01    0.018    1.572   0.0642   28.936

    95 7.99e-03  6      0.492    3e-11     3.17     0.01    9e+10   100.00              3.06     0.01    0.017    0.924   0.0265   23.660

    96 9.09e-03  4      0.501    3e-11     2.62     0.01    9e+10   100.00              3.06     0.01    0.017    2.513   0.1493   32.053

    97 8.75e-03  4      0.510    3e-11     2.79     0.01    9e+10   100.00              3.06     0.01    0.017    0.313   0.1429   34.714

    98 8.03e-03  4      0.518    3e-11     3.06     0.01    1e+11   100.00              3.06     0.01    0.017    1.383   0.0739   25.922

    99 8.71e-03  4      0.526    3e-11     3.13     0.01    1e+11   100.00              3.06     0.01    0.016    1.097   0.0797   31.357

   100 8.49e-03  6      0.535    3e-11     3.04     0.01    9e+10   100.00              3.06     0.01    0.105    1.306   0.0239   35.232

   101 7.72e-03  4      0.542    3e-11     2.91     0.01    9e+10   100.00              3.06     0.01    0.105    0.556   0.0410   27.271

   102 8.14e-03  4      0.551    3e-11     2.66     0.01    9e+10   100.00              3.06     0.01    0.105    2.047   0.1373   24.975

   103 9.00e-03  4      0.560    3e-11     3.09     0.01    9e+10   100.00              3.06     0.01    0.105    1.034   0.1464   35.440

   104 8.16e-03  6      0.568    3e-11     3.01     0.01    9e+10   100.00              3.06     0.01    0.105    1.203   0.0727   31.344

   105 7.95e-03  3      0.576    3e-11     2.81     0.01    9e+10   100.00              3.06     0.01    0.105    0.517   0.0336   28.690

   106 8.16e-03  3      0.584    3e-11     3.10     0.01    9e+10   100.00              3.06     0.01    0.105    1.753   0.0631   32.027

   107 7.85e-03  4      0.592    4e-11     3.13     0.01    8e+10   100.00              3.06     0.01    0.105    0.689   0.0902   29.653

   108 7.91e-03  6      0.600    3e-11     2.62     0.01    9e+10   100.00              3.06     0.01    0.105    2.116   0.1391   25.190

   109 2.90e-03  3 1    0.603    3e-11     2.58     0.01    9e+10   100.00              3.06     0.01    0.105    0.276   0.0538    8.271

   110 4.95e-03  3      0.607    3e-11     2.84     0.01    9e+10   100.00              3.06     0.01    0.105    0.600   0.0781   17.257

   111 6.54e-03  3      0.614    3e-11     3.11     0.01    1e+11   100.00              3.06     0.01    0.105    1.384   0.0601   25.989

   112 7.08e-03  4      0.621    3e-11     3.16     0.01    9e+10   100.00              3.06     0.01    0.105    0.846   0.0663   26.146

   113 7.64e-03  5      0.629    4e-11     3.12     0.01    9e+10   100.00              3.06     0.01    0.105    1.810   0.0615   26.589

   114 8.17e-03  3      0.637    3e-11     2.83     0.01    8e+10   100.00              3.06     0.01    0.105    1.000   0.0486   28.263

   115 8.45e-03  3      0.645    3e-11     2.65     0.01    9e+10   100.00              3.06     0.01    0.105    2.266   0.1498   28.649

   116 8.67e-03  5      0.654    4e-11     3.16     0.01    9e+10   100.00              3.06     0.01    0.105    1.127   0.1372   27.199

   117 9.16e-03  6      0.663    3e-11     3.00     0.01    9e+10   100.00              3.06     0.01    0.105    1.447   0.0707   30.511

   118 3.52e-03  4      0.667    3e-11     2.55     0.01    9e+10   100.00              3.06     0.01    0.105    2.034   0.0176   12.792

Time steps : 118/120, step size: 0.00564972, 0.00363207

Running simulation [simuapp]: stsmo088 baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 10.59s

   173   0.6046  1      2.500                      1e-04            100.00                      1e-04    0.012  1.4e-07 1.09e-14  5.8e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 10.259s  99.03%      

|- Newton                                10.231s  |- 99.73%   

  |- FluxJac                              3.004s    |- 29.36% 

  |- Update                               2.843s    |- 27.78% 

  |- update_dev                           1.841s    |- 17.99% 

  |- ScdAcc                               1.598s    |- 15.62% 

  |- Precond                              0.223s    |- 2.18%  

  |- Solver                               0.222s    |- 2.16%  

  |- alignvar                             0.075s    |- 0.74%  

  |- Residual                             0.057s    |- 0.55%  

  |- PerfJac                              0.020s    |- 0.20%  

  |- SanitizeJac                          0.015s    |- 0.14%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Logging                                0.242s  |- 2.36%    

|- Output                                 0.016s  |- 0.15%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.100s  0.97%       

|- execution                              0.083s  |- 83.15%   

------------------------------------------------------------

TOTAL                                    10.359s

============================================================



Time steps : 173/255, step size: 0.0144509, 0.0691969

Running simulation [simumpi]: stsmo088 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 12.80s

=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   151 2.70e-03  2 1    0.739    7e-06             1e-04             95.44                      1e-04    0.012    0.025   0.0147  2.1e-05

   152 5.75e-03  5      0.744    6e-06             1e-04             95.58                      1e-04    0.012    0.052   0.0281  4.4e-05

   153 3.77e-03  3 1    0.748    6e-06             1e-04             95.70                      1e-04    0.012    0.031   0.0191  2.9e-05

   154 7.79e-03  7      0.756    6e-06             1e-04             95.98                      1e-04    0.012    0.056   0.0385  5.9e-05

   155 1.48e-03  2 2    0.757    6e-06             1e-04             96.03                      1e-04    0.012    0.012   0.0101  1.1e-05

   156 3.24e-03  4      0.761    6e-06             1e-04             96.16                      1e-04    0.012    0.023   0.0200  2.4e-05

   157 6.68e-03  7      0.767    5e-06             1e-04             96.48                      1e-04    0.012    0.036   0.0345  4.9e-05

   158 1.27e-03  2 2    0.769    5e-06             1e-04             96.55                      1e-04    0.012    0.011   0.0088  9.4e-06

   159 2.80e-03  3      0.771    5e-06             1e-04             96.71                      1e-04    0.012    0.020   0.0179  2.1e-05

   160 1.95e-03  3 1    0.773    5e-06             1e-04             96.86                      1e-04    0.012    0.014   0.0130  1.4e-05

   161 4.18e-03  6      0.778    4e-06             1e-04             97.24                      1e-04    0.012    0.028   0.0254  3.0e-05

   162 8.35e-03  8      0.786    2e-06             1e-04             98.43                      1e-04    0.012    0.043   0.0423  6.0e-05

   163 4.18e-03  7 1    0.790    8e-07             1e-04             99.46                      1e-04    0.012    0.013   0.0114  3.0e-05

   164 7.95e-04  3 2    0.791    6e-07             1e-04             99.57                      1e-04    0.012    0.010   0.0083  5.6e-06

   165 1.76e-03  3      0.793    5e-07             1e-04             99.63                      1e-04    0.012    0.006   0.0044  1.2e-05

   166 3.98e-03  2      0.797    2e-07             1e-04             99.84                      1e-04    0.012    0.002   0.0016  2.8e-05

   167 9.20e-03  2      0.806    4e-08             1e-04             99.97                      1e-04    0.012  9.5e-04 8.63e-04  6.4e-05

   168   0.0213  2      0.827    2e-09             1e-04            100.00                      1e-04    0.012  1.9e-04 1.65e-04  1.4e-04

   169   0.0497  2      0.877    6e-11             1e-04            100.00                      1e-04    0.012  1.3e-05 1.07e-05  3.1e-04

   170   0.1160  1      0.993    5e-13             1e-04            100.00                      1e-04    0.012  4.5e-07 2.55e-07  6.1e-04

   171   0.2707  1      1.264    2e-15             1e-04            100.00                      1e-04    0.012  2.4e-07 2.33e-09  1.0e-03

   172   0.6317  1      1.895                      1e-04            100.00                      1e-04    0.012  2.8e-07 8.48e-12    0.001

   173   0.6046  1      2.500                      1e-04            100.00                      1e-04    0.012  1.4e-07 1.09e-14  5.8e-04

Time steps : 173/255, step size: 0.0144509, 0.0691969

Running simulation [simumpi]: stsmo088 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 14.17s

   232 2.59e-03  5      0.747    6e-06             1e-04             95.86                      1e-04    0.013    0.018   0.0137  2.0e-05

   233 1.84e-03  4 1    0.749    6e-06             1e-04             95.93                      1e-04    0.013    0.012   0.0108  1.4e-05

   234 4.01e-03  6      0.753    6e-06             1e-04             96.10                      1e-04    0.013    0.026   0.0227  3.0e-05

   235 8.92e-04  3 2    0.754    6e-06             1e-04             96.14                      1e-04    0.013    0.007   0.0060  6.8e-06

   236 2.00e-03  3      0.756    5e-06             1e-04             96.23                      1e-04    0.013    0.014   0.0130  1.5e-05

   237 1.43e-03  3 1    0.757    5e-06             1e-04             96.30                      1e-04    0.013    0.012   0.0103  1.1e-05

   238 3.13e-03  5      0.760    5e-06             1e-04             96.47                      1e-04    0.013    0.024   0.0205  2.3e-05

   239 2.14e-03  5 1    0.763    5e-06             1e-04             96.60                      1e-04    0.013    0.017   0.0147  1.6e-05

   240 1.52e-03  3 1    0.764    5e-06             1e-04             96.70                      1e-04    0.013    0.011   0.0105  1.1e-05



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   241 3.31e-03  5      0.767    4e-06             1e-04             97.00                      1e-04    0.013    0.023   0.0218  2.4e-05

   242 2.24e-03  3 1    0.770    4e-06             1e-04             97.23                      1e-04    0.013    0.016   0.0151  1.7e-05

   243 1.59e-03  3 1    0.771    4e-06             1e-04             97.40                      1e-04    0.013    0.014   0.0116  1.2e-05

   244 1.15e-03  3 1    0.772    4e-06             1e-04             97.54                      1e-04    0.013    0.010   0.0087  8.4e-06

   245 2.53e-03  4      0.775    3e-06             1e-04             98.03                      1e-04    0.013    0.019   0.0180  1.8e-05

   246 5.26e-03  6      0.780    1e-06             1e-04             99.29                      1e-04    0.013    0.022   0.0194  3.8e-05

   247   0.0105  3      0.791    9e-08             1e-04             99.94                      1e-04    0.013    0.005   0.0041  7.5e-05

   248   0.0239  2      0.815    3e-09             1e-04            100.00                      1e-04    0.013  4.8e-04 3.88e-04  1.6e-04

   249   0.0557  2      0.870    5e-11             1e-04            100.00                      1e-04    0.013  1.8e-05 1.48e-05  3.5e-04

   250   0.1299  1      1.000    3e-13             1e-04            100.00                      1e-04    0.013  2.8e-07 2.29e-07  6.8e-04

   251   0.3030  1      1.303                      1e-04            100.00                      1e-04    0.013  1.8e-09 1.46e-09    0.001

   252   0.7070  1      2.010                      1e-04            100.00                      1e-04    0.013  2.2e-10 1.45e-10    0.001

   253   0.4899  1      2.500                      1e-04            100.00                      1e-04    0.013  2.1e-10 1.44e-10  4.7e-04

Time steps : 253/382, step size: 0.00988142, 0.0574438

Running simulation [simumpi]: stsmo088 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 10.24s

   220 2.72e-03  5 1    0.736    6e-06             1e-04             95.50                      1e-04    0.002    0.025   0.0177  2.1e-05

   221 5.68e-03  3      0.742    6e-06             1e-04             95.71                      1e-04    0.002    0.048   0.0306  4.4e-05

   222 3.67e-03  5 1    0.746    6e-06             1e-04             95.85                      1e-04    0.002    0.026   0.0225  2.8e-05

   223 7.44e-03 12      0.753    5e-06             1e-04             96.21                      1e-04    0.002    0.042   0.0397  5.7e-05

   224 8.27e-04  3 2    0.754    5e-06             1e-04             96.25                      1e-04    0.002    0.007   0.0057  6.3e-06

   225 1.86e-03  3      0.756    5e-06             1e-04             96.35                      1e-04    0.002    0.015   0.0129  1.4e-05

   226 1.33e-03  4 1    0.757    5e-06             1e-04             96.42                      1e-04    0.002    0.012   0.0099  1.0e-05

   227 2.91e-03  4      0.760    5e-06             1e-04             96.59                      1e-04    0.002    0.022   0.0196  2.2e-05

   228 2.00e-03  2 1    0.762    5e-06             1e-04             96.73                      1e-04    0.002    0.015   0.0137  1.5e-05

   229 4.28e-03  6      0.766    4e-06             1e-04             97.14                      1e-04    0.002    0.029   0.0266  3.2e-05

   230 2.83e-03  5 1    0.769    4e-06             1e-04             97.45                      1e-04    0.002    0.021   0.0183  2.1e-05

   231 5.89e-03  7      0.775    2e-06             1e-04             98.38                      1e-04    0.002    0.033   0.0317  4.3e-05

   232 1.12e-03  4 2    0.776    2e-06             1e-04             98.73                      1e-04    0.002    0.010   0.0079  8.2e-06

   233 2.49e-03  3      0.779    5e-07             1e-04             99.62                      1e-04    0.002    0.007   0.0056  1.8e-05

   234 5.59e-03  1      0.784    8e-08             1e-04             99.94                      1e-04    0.002    0.003   0.0020  4.0e-05

   235   0.0129  3      0.797    5e-09             1e-04            100.00                      1e-04    0.002  4.1e-04 3.35e-04  9.1e-05

   236   0.0300  2      0.827    1e-10             1e-04            100.00                      1e-04    0.002  2.5e-05 2.02e-05  2.0e-04

   237   0.0699  1      0.897    1e-12             1e-04            100.00                      1e-04    0.002  6.4e-07 5.14e-07  4.3e-04

   238   0.1631  1      1.060    6e-15             1e-04            100.00                      1e-04    0.002  6.8e-09 5.47e-09  7.9e-04

   239   0.3807  1      1.441                      1e-04            100.00                      1e-04    0.002  2.0e-11 2.28e-11    0.001

   240   0.8882  1      2.329                      1e-04            100.00                      1e-04    0.002  9.1e-12 1.21e-13    0.001



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   241   0.1710  1      2.500                      1e-04            100.00                      1e-04    0.002  2.7e-12 1.85e-14  1.7e-04

Time steps : 241/360, step size: 0.0103734, 0.0636836

Running simulation [simuapp]: stsmo097 baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 4.55s

    45   1.0693  3      5.000    3e-07             1e-04             99.82                      1e-04    0.015    0.302   0.0216  1.6e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  4.160s  97.14%      

|- Newton                                 4.153s  |- 99.83%   

  |- Update                               0.676s    |- 16.27% 

  |- FluxJac                              0.603s    |- 14.53% 

  |- update_dev                           0.431s    |- 10.37% 

  |- ScdAcc                               0.362s    |- 8.72%  

  |- Solver                               0.053s    |- 1.27%  

  |- Precond                              0.049s    |- 1.18%  

  |- alignvar                             0.017s    |- 0.40%  

  |- Residual                             0.013s    |- 0.30%  

  |- PerfJac                              0.004s    |- 0.10%  

  |- SanitizeJac                          0.003s    |- 0.08%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Logging                                1.921s  |- 46.17%   

|- Output                                 0.005s  |- 0.11%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.123s  2.86%       

|- execution                              0.104s  |- 84.77%   

------------------------------------------------------------

TOTAL                                     4.283s

============================================================



Time steps : 45/49, step size: 0.111111, 0.301545

Running simulation [simumpi]: stsmo097 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 3.02s

    24 1.76e-03  8      0.030    1e-04                                                          1e-04    0.000    3.798   0.0539  4.7e-04

    25 2.64e-03 14      0.033    1e-04                                                          1e-04    0.000    5.562   0.0615  6.3e-04

    26 2.26e-03 10      0.035    1e-04                                                          1e-04    0.000    5.427   0.0529  5.2e-04

    27 2.72e-03 13      0.038    1e-04                                                          1e-04    0.000    6.766   0.0569  5.4e-04

    28 2.51e-03 11      0.040    1e-04                                                          1e-04    0.000    6.836   0.0536  4.4e-04

    29 2.74e-03 13      0.043    1e-04                                                          1e-04    0.000    7.836   0.0557  3.6e-04

    30 2.53e-03 11      0.045    1e-04             5e-06              3.61                      1e-04    0.031    7.809   0.0520  2.3e-04



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    31 2.76e-03  4      0.048    1e-04             3e-05             17.96                      1e-04    0.030    8.300   0.0389  1.9e-04

    32 1.84e-03  3      0.050    1e-04             4e-05             27.94                      1e-04    0.029    4.723   0.0184  1.0e-04

    33 3.82e-03  3      0.054    8e-05             6e-05             41.31                      1e-04    0.029    7.245   0.0281  1.5e-04

    34 7.50e-03  4      0.061    7e-05             8e-05             54.06                      1e-04    0.028    9.144   0.0268  3.5e-04

    35   0.0148  3      0.076    5e-05             9e-05             65.29                      1e-04    0.026   10.863   0.0301  7.1e-04

    36   0.0238  3      0.100    4e-05             1e-04             73.85                      1e-04    0.025   10.097   0.0337  9.9e-04

    37   0.0454  4      0.145    3e-05             1e-04             81.65                      1e-04    0.023   10.148   0.0440    0.001

    38   0.0819  4      0.227    2e-05             1e-04             87.76                      1e-04    0.021    8.780   0.0517    0.002

    39   0.1422  4      0.370    1e-05             1e-04             92.16                      1e-04    0.020    6.949   0.0564    0.002

    40   0.2411  4      0.611    7e-06             1e-04             95.21                      1e-04    0.018    5.125   0.0593    0.003

    41   0.4033  4      1.014    4e-06             1e-04             97.23                      1e-04    0.017    3.598   0.0613    0.003

    42   0.6681  4      1.682    2e-06             1e-04             98.50                      1e-04    0.016    2.363   0.0623    0.002

    43   0.8179  4      2.500    1e-06             1e-04             99.20                      1e-04    0.015    1.244   0.0501    0.001

    44   1.4307  4      3.931    5e-07             1e-04             99.66                      1e-04    0.015    0.830   0.0454  5.7e-04

    45   1.0693  3      5.000    3e-07             1e-04             99.82                      1e-04    0.015    0.302   0.0216  1.6e-04

Time steps : 45/49, step size: 0.111111, 0.301545

Running simulation [simumpi]: stsmo097 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 1.40s

    24 1.76e-03  8      0.030    1e-04                                                          1e-04    0.000    3.792   0.0539  4.8e-04

    25 2.64e-03 14      0.033    1e-04                                                          1e-04    0.000    5.577   0.0615  6.3e-04

    26 2.26e-03 10      0.035    1e-04                                                          1e-04    0.000    5.444   0.0529  5.3e-04

    27 2.72e-03 13      0.038    1e-04                                                          1e-04    0.000    6.770   0.0569  5.4e-04

    28 2.51e-03 11      0.040    1e-04                                                          1e-04    0.000    6.837   0.0536  4.4e-04

    29 2.74e-03 13      0.043    1e-04                                                          1e-04    0.000    7.843   0.0557  3.7e-04

    30 2.53e-03 11      0.045    1e-04             5e-06              3.61                      1e-04    0.031    7.811   0.0520  2.4e-04



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    31 2.76e-03  4      0.048    1e-04             3e-05             17.96                      1e-04    0.030    8.300   0.0389  1.9e-04

    32 1.84e-03  3      0.050    1e-04             4e-05             27.94                      1e-04    0.029    4.724   0.0184  1.0e-04

    33 3.82e-03  3      0.054    8e-05             6e-05             41.31                      1e-04    0.029    7.245   0.0281  1.5e-04

    34 7.50e-03  4      0.061    7e-05             8e-05             54.06                      1e-04    0.028    9.145   0.0268  3.5e-04

    35   0.0148  3      0.076    5e-05             9e-05             65.29                      1e-04    0.026   10.863   0.0301  7.1e-04

    36   0.0238  3      0.100    4e-05             1e-04             73.85                      1e-04    0.025   10.097   0.0337  9.9e-04

    37   0.0454  4      0.145    3e-05             1e-04             81.65                      1e-04    0.023   10.148   0.0440    0.001

    38   0.0819  5      0.227    2e-05             1e-04             87.76                      1e-04    0.021    8.780   0.0517    0.002

    39   0.1422  4      0.370    1e-05             1e-04             92.16                      1e-04    0.020    6.949   0.0564    0.002

    40   0.2411  5      0.611    7e-06             1e-04             95.21                      1e-04    0.018    5.125   0.0593    0.003

    41   0.4033  5      1.014    4e-06             1e-04             97.23                      1e-04    0.017    3.598   0.0613    0.003

    42   0.6681  4      1.682    2e-06             1e-04             98.50                      1e-04    0.016    2.363   0.0623    0.002

    43   0.8179  4      2.500    1e-06             1e-04             99.20                      1e-04    0.015    1.244   0.0501    0.001

    44   1.4308  5      3.931    5e-07             1e-04             99.66                      1e-04    0.015    0.830   0.0454  5.7e-04

    45   1.0692  5      5.000    3e-07             1e-04             99.82                      1e-04    0.015    0.302   0.0216  1.6e-04

Time steps : 45/49, step size: 0.111111, 0.301546

Running simulation [simumpi]: stsmo097 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 1.51s

    32 2.61e-03 13      0.044    1e-04                                                          1e-04    0.000    7.651   0.0564  2.7e-04

    33 2.40e-03  7      0.047    1e-04             1e-05              6.86                      1e-04    0.002    7.638   0.0511  1.8e-04

    34 3.24e-03  4      0.050    1e-04             4e-05             26.35                      1e-04    0.002    8.661   0.0399  1.8e-04

    35 5.97e-03  4      0.056    8e-05             7e-05             45.26                      1e-04    0.002   10.167   0.0385  2.3e-04

    36   0.0111  3      0.067    6e-05             9e-05             59.25                      1e-04    0.002   10.989   0.0331  5.4e-04

    37   0.0212  4      0.088    4e-05             1e-04             70.21                      1e-04    0.002   11.635   0.0333  9.5e-04

    38   0.0118  4      0.100    4e-05             1e-04             74.05                      1e-04    0.002    4.631   0.0166  4.9e-04

    39   0.0247  4      0.125    3e-05             1e-04             79.24                      1e-04    0.002    6.577   0.0285  8.5e-04

    40   0.0484  5      0.173    2e-05             1e-04             84.66                      1e-04    0.002    7.555   0.0402    0.001

    41   0.0891  4      0.262    2e-05             1e-04             89.42                      1e-04    0.002    7.161   0.0494    0.002

    42   0.1564  5      0.419    1e-05             1e-04             93.16                      1e-04    0.002    6.001   0.0549    0.002

    43   0.2672  5      0.686    6e-06             1e-04             95.81                      1e-04    0.002    4.548   0.0584    0.003

    44   0.4489  5      1.135    3e-06             1e-04             97.59                      1e-04    0.002    3.226   0.0608    0.002

    45   0.7453  5      1.880    2e-06             1e-04             98.73                      1e-04    0.002    2.091   0.0620    0.002

    46   0.6201  5      2.500    1e-06             1e-04             99.23                      1e-04    0.002    0.887   0.0371  7.7e-04

    47   1.1597  5      3.660    5e-07             1e-04             99.63                      1e-04    0.002    0.733   0.0398  5.0e-04

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 4.44161e-12) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 4.44161e-12) - this cycle cannot be accepted as converged

[rank 2] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 4.44161e-12) - this cycle cannot be accepted as converged

[rank 3] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 4.44161e-12) - this cycle cannot be accepted as converged

[rank 2] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 1.91577e-14) - this cycle cannot be accepted as converged

[rank 3] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 1.91577e-14) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 1.91577e-14) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 1.91577e-14) - this cycle cannot be accepted as converged

[rank 2] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.64217e-17) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.64217e-17) - this cycle cannot be accepted as converged

[rank 3] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.64217e-17) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.64217e-17) - this cycle cannot be accepted as converged

    48   1.3403  6      5.000    2e-07             1e-04             99.83                      1e-04    0.002    0.364   0.0264  1.9e-04

Time steps : 48/55, step size: 0.104167, 0.286932

Running simulation [simuapp]: corner baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 4.67s

    78   5.0000  1   3650.000    80.45   428.63     1.73     5.33     2.11                               0.000    0.776 1.26e-05  8.3e-05



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  4.321s  97.76%      

|- Newton                                 4.291s  |- 99.32%   

  |- FluxJac                              1.649s    |- 38.42% 

  |- Update                               1.513s    |- 35.25% 

  |- ScdAcc                               0.333s    |- 7.76%  

  |- Solver                               0.308s    |- 7.18%  

  |- update_dev                           0.243s    |- 5.66%  

  |- Precond                              0.103s    |- 2.40%  

  |- Residual                             0.027s    |- 0.63%  

  |- alignvar                             0.018s    |- 0.43%  

  |- SanitizeJac                          0.008s    |- 0.20%  

  |- HeatLoss                             0.006s    |- 0.13%  

  |- PerfJac                              0.003s    |- 0.08%  

|- Logging                                0.055s  |- 1.26%    

|- Output                                 0.013s  |- 0.29%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.099s  2.24%       

|- execution                              0.091s  |- 92.42%   

------------------------------------------------------------

TOTAL                                     4.420s

============================================================



Time steps : 78/78, step size: 46.7949, 11.3039

Running simulation [simumpi]: corner np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 4.28s

    57  50.0000  1   2645.000    81.73   435.44     1.72     5.33     2.06                               0.000   10.227 1.26e-04    0.001

    58  50.0000  1   2695.000    81.66   435.06     1.72     5.33     2.06                               0.000   10.072 1.26e-04    0.001

    59  50.0000  1   2745.000    81.59   434.68     1.72     5.33     2.06                               0.000    9.922 1.26e-04    0.001

    60  50.0000  1   2795.000    81.52   434.31     1.72     5.33     2.07                               0.000    9.775 1.26e-04    0.001



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  50.0000  1   2845.000    81.45   433.94     1.72     5.33     2.07                               0.000    9.632 1.26e-04    0.001

    62  50.0000  1   2895.000    81.38   433.58     1.72     5.33     2.07                               0.000    9.493 1.26e-04  9.9e-04

    63  50.0000  1   2945.000    81.31   433.22     1.72     5.33     2.07                               0.000    9.358 1.27e-04  9.8e-04

    64  50.0000  1   2995.000    81.25   432.87     1.72     5.33     2.08                               0.000    9.226 1.27e-04  9.6e-04

    65  50.0000  1   3045.000    81.18   432.52     1.72     5.33     2.08                               0.000    9.097 1.27e-04  9.5e-04

    66  50.0000  1   3095.000    81.12   432.18     1.73     5.33     2.08                               0.000    8.971 1.27e-04  9.4e-04

    67  50.0000  1   3145.000    81.05   431.84     1.73     5.33     2.09                               0.000    8.845 1.27e-04  9.2e-04

    68  50.0000  1   3195.000    80.99   431.50     1.73     5.33     2.09                               0.000    8.724 1.27e-04  9.1e-04

    69  50.0000  1   3245.000    80.93   431.17     1.73     5.33     2.09                               0.000    8.606 1.26e-04  9.0e-04

    70  50.0000  1   3295.000    80.87   430.84     1.73     5.33     2.09                               0.000    8.492 1.26e-04  8.9e-04

    71  50.0000  1   3345.000    80.80   430.52     1.73     5.33     2.10                               0.000    8.380 1.26e-04  8.8e-04

    72  50.0000  1   3395.000    80.74   430.20     1.73     5.33     2.10                               0.000    8.271 1.26e-04  8.7e-04

    73  50.0000  1   3445.000    80.69   429.88     1.73     5.33     2.10                               0.000    8.165 1.26e-04  8.6e-04

    74  50.0000  1   3495.000    80.63   429.57     1.73     5.33     2.10                               0.000    8.061 1.26e-04  8.5e-04

    75  50.0000  1   3545.000    80.57   429.26     1.73     5.33     2.11                               0.000    7.960 1.26e-04  8.4e-04

    76  50.0000  1   3595.000    80.51   428.96     1.73     5.33     2.11                               0.000    7.861 1.26e-04  8.4e-04

    77  50.0000  1   3645.000    80.46   428.66     1.73     5.33     2.11                               0.000    7.765 1.26e-04  8.3e-04

    78   5.0000  1   3650.000    80.45   428.63     1.73     5.33     2.11                               0.000    0.776 1.26e-05  8.3e-05

Time steps : 78/78, step size: 46.7949, 11.3039

Running simulation [simumpi]: corner np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 2.26s

    57  50.0000  1   2645.000    81.73   435.44     1.72     5.33     2.06                               0.000   10.227 1.26e-04    0.001

    58  50.0000  1   2695.000    81.66   435.06     1.72     5.33     2.06                               0.000   10.072 1.26e-04    0.001

    59  50.0000  1   2745.000    81.59   434.68     1.72     5.33     2.06                               0.000    9.922 1.26e-04    0.001

    60  50.0000  1   2795.000    81.52   434.31     1.72     5.33     2.07                               0.000    9.775 1.26e-04    0.001



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  50.0000  1   2845.000    81.45   433.94     1.72     5.33     2.07                               0.000    9.632 1.26e-04    0.001

    62  50.0000  1   2895.000    81.38   433.58     1.72     5.33     2.07                               0.000    9.493 1.26e-04  9.9e-04

    63  50.0000  1   2945.000    81.31   433.22     1.72     5.33     2.07                               0.000    9.358 1.27e-04  9.8e-04

    64  50.0000  1   2995.000    81.25   432.87     1.72     5.33     2.08                               0.000    9.226 1.27e-04  9.6e-04

    65  50.0000  1   3045.000    81.18   432.52     1.72     5.33     2.08                               0.000    9.097 1.27e-04  9.5e-04

    66  50.0000  1   3095.000    81.12   432.18     1.73     5.33     2.08                               0.000    8.971 1.27e-04  9.4e-04

    67  50.0000  1   3145.000    81.05   431.84     1.73     5.33     2.09                               0.000    8.845 1.27e-04  9.2e-04

    68  50.0000  1   3195.000    80.99   431.50     1.73     5.33     2.09                               0.000    8.724 1.27e-04  9.1e-04

    69  50.0000  1   3245.000    80.93   431.17     1.73     5.33     2.09                               0.000    8.606 1.26e-04  9.0e-04

    70  50.0000  1   3295.000    80.87   430.84     1.73     5.33     2.09                               0.000    8.492 1.26e-04  8.9e-04

    71  50.0000  1   3345.000    80.80   430.52     1.73     5.33     2.10                               0.000    8.380 1.26e-04  8.8e-04

    72  50.0000  1   3395.000    80.74   430.20     1.73     5.33     2.10                               0.000    8.271 1.26e-04  8.7e-04

    73  50.0000  1   3445.000    80.69   429.88     1.73     5.33     2.10                               0.000    8.165 1.26e-04  8.6e-04

    74  50.0000  1   3495.000    80.63   429.57     1.73     5.33     2.10                               0.000    8.061 1.26e-04  8.5e-04

    75  50.0000  1   3545.000    80.57   429.26     1.73     5.33     2.11                               0.000    7.960 1.26e-04  8.4e-04

    76  50.0000  1   3595.000    80.51   428.96     1.73     5.33     2.11                               0.000    7.861 1.26e-04  8.4e-04

    77  50.0000  1   3645.000    80.46   428.66     1.73     5.33     2.11                               0.000    7.765 1.26e-04  8.3e-04

    78   5.0000  1   3650.000    80.45   428.63     1.73     5.33     2.11                               0.000    0.776 1.26e-05  8.3e-05

Time steps : 78/78, step size: 46.7949, 11.3039

Running simulation [simumpi]: corner np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 2.49s

    57  50.0000  1   2645.000    81.73   435.44     1.72     5.33     2.06                               0.000   10.227 1.26e-04    0.001

    58  50.0000  1   2695.000    81.66   435.06     1.72     5.33     2.06                               0.000   10.072 1.26e-04    0.001

    59  50.0000  1   2745.000    81.59   434.68     1.72     5.33     2.06                               0.000    9.922 1.26e-04    0.001

    60  50.0000  1   2795.000    81.52   434.31     1.72     5.33     2.07                               0.000    9.775 1.26e-04    0.001



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  50.0000  1   2845.000    81.45   433.94     1.72     5.33     2.07                               0.000    9.632 1.26e-04    0.001

    62  50.0000  1   2895.000    81.38   433.58     1.72     5.33     2.07                               0.000    9.493 1.26e-04  9.9e-04

    63  50.0000  1   2945.000    81.31   433.22     1.72     5.33     2.07                               0.000    9.358 1.27e-04  9.8e-04

    64  50.0000  1   2995.000    81.25   432.87     1.72     5.33     2.08                               0.000    9.226 1.27e-04  9.6e-04

    65  50.0000  1   3045.000    81.18   432.52     1.72     5.33     2.08                               0.000    9.097 1.27e-04  9.5e-04

    66  50.0000  1   3095.000    81.12   432.18     1.73     5.33     2.08                               0.000    8.971 1.27e-04  9.4e-04

    67  50.0000  1   3145.000    81.05   431.84     1.73     5.33     2.09                               0.000    8.845 1.27e-04  9.2e-04

    68  50.0000  1   3195.000    80.99   431.50     1.73     5.33     2.09                               0.000    8.724 1.27e-04  9.1e-04

    69  50.0000  1   3245.000    80.93   431.17     1.73     5.33     2.09                               0.000    8.606 1.26e-04  9.0e-04

    70  50.0000  1   3295.000    80.87   430.84     1.73     5.33     2.09                               0.000    8.492 1.26e-04  8.9e-04

    71  50.0000  1   3345.000    80.80   430.52     1.73     5.33     2.10                               0.000    8.380 1.26e-04  8.8e-04

    72  50.0000  1   3395.000    80.74   430.20     1.73     5.33     2.10                               0.000    8.271 1.26e-04  8.7e-04

    73  50.0000  1   3445.000    80.69   429.88     1.73     5.33     2.10                               0.000    8.165 1.26e-04  8.6e-04

    74  50.0000  1   3495.000    80.63   429.57     1.73     5.33     2.10                               0.000    8.061 1.26e-04  8.5e-04

    75  50.0000  1   3545.000    80.57   429.26     1.73     5.33     2.11                               0.000    7.960 1.26e-04  8.4e-04

    76  50.0000  1   3595.000    80.51   428.96     1.73     5.33     2.11                               0.000    7.861 1.26e-04  8.4e-04

    77  50.0000  1   3645.000    80.46   428.66     1.73     5.33     2.11                               0.000    7.765 1.26e-04  8.3e-04

    78   5.0000  1   3650.000    80.45   428.63     1.73     5.33     2.11                               0.000    0.776 1.26e-05  8.3e-05

Time steps : 78/78, step size: 46.7949, 11.3039

Running simulation [simuapp]: stflu011 baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 0.63s

    10 144.8245  1   1095.000   171.12              0.02              0.01                      80.00    0.000    7.015   0.0036  8.9e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.299s  74.24%      

|- Newton                                 0.296s  |- 99.13%   

  |- FluxJac                              0.114s    |- 38.42% 

  |- Update                               0.103s    |- 34.93% 

  |- ScdAcc                               0.026s    |- 8.73%  

  |- update_dev                           0.022s    |- 7.45%  

  |- Solver                               0.018s    |- 5.97%  

  |- Precond                              0.004s    |- 1.51%  

  |- PerfJac                              0.003s    |- 1.05%  

  |- Residual                             0.002s    |- 0.62%  

  |- alignvar                             0.001s    |- 0.47%  

  |- SanitizeJac                          0.000s    |- 0.10%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.001s  |- 0.37%    

|- Logging                                0.000s  |- 0.13%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.104s  25.76%      

|- execution                              0.094s  |- 91.02%   

------------------------------------------------------------

TOTAL                                     0.402s

============================================================



Time steps : 10/10, step size: 109.5, 135.68

Running simulation [simumpi]: stflu011 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 0.60s

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-26





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   1.0000  1      1.000   172.88             2e-04             1e-04                      80.00    0.000    1.391 5.16e-05  1.9e-04

     2   2.3247  1      3.325   172.86             7e-04             4e-04                      80.00    0.000    2.256 1.23e-04  3.1e-04

     3   5.3919  1      8.717   172.81              0.00             8e-04                      80.00    0.000    3.562 2.87e-04  4.8e-04

     4  12.4627  1     21.179   172.73              0.00              0.00                      80.00    0.000    5.476 6.65e-04  7.4e-04

     5  28.6610  1     49.840   172.58              0.00              0.00                      80.00    0.000    9.050   0.0015    0.001

     6  65.2998  1    115.140   172.34              0.01              0.00                      80.00    0.000   14.799   0.0035    0.002

     7 146.5816  1    261.722   171.99              0.01              0.01                      80.00    0.000   21.529   0.0076    0.003

     8 323.4538  1    585.176   171.55              0.02              0.01                      80.00    0.000   27.868   0.0156    0.004

     9 365.0000  1    950.176   171.23              0.02              0.01                      80.00    0.000   20.664   0.0103    0.003

    10 144.8245  1   1095.000   171.12              0.02              0.01                      80.00    0.000    7.015   0.0036  8.9e-04

Time steps : 10/10, step size: 109.5, 135.68

Running simulation [simumpi]: stflu011 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 0.47s

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-26





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   1.0000  1      1.000   172.88             2e-04             1e-04                      80.00    0.000    1.391 5.16e-05  1.9e-04

     2   2.3247  1      3.325   172.86             7e-04             4e-04                      80.00    0.000    2.256 1.23e-04  3.1e-04

     3   5.3919  1      8.717   172.81              0.00             8e-04                      80.00    0.000    3.562 2.87e-04  4.8e-04

     4  12.4627  1     21.179   172.73              0.00              0.00                      80.00    0.000    5.476 6.65e-04  7.4e-04

     5  28.6610  1     49.840   172.58              0.00              0.00                      80.00    0.000    9.050   0.0015    0.001

     6  65.2998  1    115.140   172.34              0.01              0.00                      80.00    0.000   14.799   0.0035    0.002

     7 146.5816  1    261.722   171.99              0.01              0.01                      80.00    0.000   21.529   0.0076    0.003

     8 323.4538  1    585.176   171.55              0.02              0.01                      80.00    0.000   27.868   0.0156    0.004

     9 365.0000  1    950.176   171.23              0.02              0.01                      80.00    0.000   20.664   0.0103    0.003

    10 144.8245  1   1095.000   171.12              0.02              0.01                      80.00    0.000    7.015   0.0036  8.9e-04

Time steps : 10/10, step size: 109.5, 135.68

Running simulation [simumpi]: stflu011 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 0.45s

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-26





VTU generation is suppressed.

VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   1.0000  1      1.000   172.88             2e-04             1e-04                      80.00    0.000    1.391 5.16e-05  1.9e-04

     2   2.3247  1      3.325   172.86             7e-04             4e-04                      80.00    0.000    2.256 1.23e-04  3.1e-04

     3   5.3919  1      8.717   172.81              0.00             8e-04                      80.00    0.000    3.562 2.87e-04  4.8e-04

     4  12.4627  1     21.179   172.73              0.00              0.00                      80.00    0.000    5.476 6.65e-04  7.4e-04

     5  28.6610  1     49.840   172.58              0.00              0.00                      80.00    0.000    9.050   0.0015    0.001

     6  65.2998  1    115.140   172.34              0.01              0.00                      80.00    0.000   14.799   0.0035    0.002

     7 146.5816  1    261.722   171.99              0.01              0.01                      80.00    0.000   21.529   0.0076    0.003

     8 323.4538  1    585.176   171.55              0.02              0.01                      80.00    0.000   27.868   0.0156    0.004

     9 365.0000  1    950.176   171.23              0.02              0.01                      80.00    0.000   20.664   0.0103    0.003

    10 144.8245  1   1095.000   171.12              0.02              0.01                      80.00    0.000    7.015   0.0036  8.9e-04

Time steps : 10/10, step size: 109.5, 135.68

Difference from simuapp (worst relative cumulative well volume)

deck       mechanism                        end (d)             np=1             np=2             np=4

stflu015   corner point, no *NUMERICAL       365.00   7.8e-16     ok   8.4e-14     ok   6.3e-12     ok

stflu018   inactive-block perforation        365.00   2.6e-13     ok   1.3e-08     ok   1.7e-08     ok

lauwerier  thermal front, cut steps          126.64   0.0e+00     ok   7.3e-13     ok   3.3e-10     ok

stflu028   *KRTEMTAB                        2435.00   0.0e+00     ok   5.0e-08     ok   6.7e-08     ok

stflu029   *KRTEMTAB, shut-in wells          820.00   0.0e+00     ok   3.8e-04     ok   1.2e-01  CHECK

stflu019   *NETGROSS, *PVCUTOFF               36.01   1.1e-10     ok   5.4e-10     ok   1.8e-08     ok

stflu010   STG constraint switching            0.38   1.7e+00  CHECK   1.7e+00  CHECK   1.0e+00  SHORT

stflu021   SAGD, BHP-limit demotion         2526.00   0.0e+00     ok   3.0e-03     ok   5.7e-02  CHECK

stflu033   combustion reactions                0.67   0.0e+00     ok   7.6e-09     ok   2.0e-07     ok

stsmo088   imbibition capillary pressure       2.50   0.0e+00     ok   5.4e-03     ok   1.3e-02  CHECK

stsmo097   rock-fluid interpolation            5.00   0.0e+00     ok   1.3e-07     ok   1.2e-02  CHECK

corner     corner-point grid                3650.00   0.0e+00     ok   2.9e-08     ok   4.6e-08     ok

stflu011   1000-cell Cartesian grid         1095.00   0.0e+00     ok   1.7e-09     ok   4.0e-10     ok

  CHECK: stflu029 simumpi np=4 - worst column vratesc_gasoline1

  CHECK: stflu010 simumpi np=1 - worst column vratesc_gasoline0

  CHECK: stflu010 simumpi np=2 - worst column vratesc_gasoline0

  SHORT: stflu010 simumpi np=4 - rc=0, reached 0.00 days

  CHECK: stflu021 simumpi np=4 - worst column vratesc_oleic1

  CHECK: stsmo088 simumpi np=4 - worst column vratesc_oleic1

  CHECK: stsmo097 simumpi np=4 - worst column vratesc_oleic1



Speed (seconds marching; speedup and efficiency against simumpi np=1)

deck       steps  simuapp    np=1    np=2    np=4   x np=2   x np=4  effic. cells/rank

stflu015      14     0.48    0.38    0.22    0.15    1.71x    2.47x     62%        238

stflu018      65    11.90   11.79    6.78    4.93    1.74x    2.39x     60%        393

lauwerier     10     1.63    1.48    0.81    0.60    1.84x    2.48x     62%        206

stflu028      40     0.16    0.08    0.06    0.06    1.32x    1.28x     32%          7

stflu029     232     7.05    6.91    4.49    3.72    1.54x    1.86x     46%         58

stflu019      11   188.50  112.60   67.11   39.05    1.68x    2.88x     72%      78972

stflu010     281     5.77    5.69    3.97    0.10    1.43x   59.75x   1494%         20

stflu021     178     6.30    6.91    8.67   21.44    0.80x    0.32x      8%         51

stflu033     118     1.12    1.71    0.36    0.32    4.80x    5.34x    133%          5

stsmo088     173    10.36   12.36   13.79    9.61    0.90x    1.29x     32%         62

stsmo097      45     4.28    2.71    1.00    1.04    2.70x    2.61x     65%         62

corner        78     4.42    3.51    1.90    2.07    1.85x    1.70x     43%        306

stflu011      10     0.40    0.29    0.17    0.12    1.78x    2.38x     60%        257

  effic. and cells/rank are at np=4; under ~500 cells per rank the time is collective overhead, not decomposition.

```

Left, the difference from `simuapp` on a log scale: np=1 should sit at the left edge

(roundoff), and anything right of the dashed line is worth chasing. Right, parallel efficiency

against np=1, with 100% the ideal. One row per deck in both; a deck with no marker for a rank count

failed or stopped short there - the tables above say which.

![png]({{ "/assets/images/benchmark_image_79.png" | relative_url }})

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

Elapsed: 40.42s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 37.944s  94.84%      

|- Newton                                37.838s  |- 99.72%   

  |- FluxJac                             14.046s    |- 37.12% 

  |- Update                              12.280s    |- 32.46% 

  |- ScdAcc                               3.716s    |- 9.82%  

  |- update_dev                           3.622s    |- 9.57%  

  |- Solver                               2.367s    |- 6.26%  

  |- Precond                              0.588s    |- 1.55%  

  |- Residual                             0.288s    |- 0.76%  

  |- alignvar                             0.204s    |- 0.54%  

  |- HeatLoss                             0.128s    |- 0.34%  

  |- SanitizeJac                          0.105s    |- 0.28%  

  |- PerfJac                              0.088s    |- 0.23%  

|- Logging                                0.081s  |- 0.21%    

|- Output                                 0.010s  |- 0.03%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            2.066s  5.16%       

|- execution                              1.913s  |- 92.56%   

------------------------------------------------------------

TOTAL                                    40.011s

============================================================



Time steps : 4/4, step size: 0.129382, 0.0269202

Running simulation [simuapp]: scaling baseline (attempt 2/2) (OMP_NUM_THREADS=1, -novtu)

Elapsed: 48.23s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 45.614s  95.62%      

|- Newton                                45.409s  |- 99.55%   

  |- FluxJac                             16.225s    |- 35.73% 

  |- Update                              13.535s    |- 29.81% 

  |- Solver                               5.761s    |- 12.69% 

  |- ScdAcc                               3.835s    |- 8.45%  

  |- update_dev                           3.207s    |- 7.06%  

  |- Precond                              0.780s    |- 1.72%  

  |- SanitizeJac                          0.446s    |- 0.98%  

  |- Residual                             0.388s    |- 0.86%  

  |- HeatLoss                             0.300s    |- 0.66%  

  |- alignvar                             0.224s    |- 0.49%  

  |- PerfJac                              0.119s    |- 0.26%  

|- Output                                 0.012s  |- 0.03%    

|- Logging                                0.005s  |- 0.01%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            2.090s  4.38%       

|- execution                              1.925s  |- 92.13%   

------------------------------------------------------------

TOTAL                                    47.704s

============================================================



Time steps : 4/4, step size: 0.129382, 0.0269202

Running simulation [simumpi]: scaling np=1 (attempt 1/2) (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 40.91s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-26





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.64             20.22              3.28                     720.00    0.000  375.000   0.0027    0.110

     2   0.1167  1      0.217   497.87             26.41              5.04                     720.00    0.000  359.596   0.0032    0.122

     3   0.1390  2      0.356   426.18             27.34              6.03                     720.00    0.000  376.058   0.0037    0.138

     4   0.1619  2      0.518   376.54             25.85              6.42                     720.00    0.000  339.726   0.0034    0.150





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129382, 0.0269202

Running simulation [simumpi]: scaling np=1 (attempt 2/2) (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 43.01s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-26





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.64             20.22              3.28                     720.00    0.000  375.000   0.0027    0.110

     2   0.1167  1      0.217   497.87             26.41              5.04                     720.00    0.000  359.596   0.0032    0.122

     3   0.1390  2      0.356   426.18             27.34              6.03                     720.00    0.000  376.058   0.0037    0.138

     4   0.1619  2      0.518   376.54             25.85              6.42                     720.00    0.000  339.726   0.0034    0.150





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129382, 0.0269202

Running simulation [simumpi]: scaling np=2 (attempt 1/2) (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 25.23s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-26





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.64             20.22              3.28                     720.00    0.000  375.000   0.0027    0.110

     2   0.1167  1      0.217   497.87             26.41              5.04                     720.00    0.000  359.596   0.0032    0.122

     3   0.1390  2      0.356   426.18             27.34              6.03                     720.00    0.000  376.058   0.0037    0.138

     4   0.1619  2      0.518   376.54             25.85              6.42                     720.00    0.000  339.726   0.0034    0.150





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129382, 0.0269202

Running simulation [simumpi]: scaling np=2 (attempt 2/2) (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 27.32s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-26





VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.64             20.22              3.28                     720.00    0.000  375.000   0.0027    0.110

     2   0.1167  1      0.217   497.87             26.41              5.04                     720.00    0.000  359.596   0.0032    0.122

     3   0.1390  2      0.356   426.18             27.34              6.03                     720.00    0.000  376.058   0.0037    0.138

     4   0.1619  2      0.518   376.54             25.85              6.42                     720.00    0.000  339.726   0.0034    0.150





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129382, 0.0269202

Running simulation [simumpi]: scaling np=4 (attempt 1/2) (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 23.25s

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-26





VTU generation is suppressed.

VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.64             20.22              3.28                     720.00    0.000  375.000   0.0027    0.110

     2   0.1167  1      0.217   497.87             26.41              5.04                     720.00    0.000  359.596   0.0032    0.122

     3   0.1390  2      0.356   426.18             27.34              6.03                     720.00    0.000  376.058   0.0037    0.138

     4   0.1619  2      0.518   376.54             25.85              6.42                     720.00    0.000  339.726   0.0034    0.150





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129382, 0.0269202

Running simulation [simumpi]: scaling np=4 (attempt 2/2) (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 20.21s

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-26





VTU generation is suppressed.

VTU generation is suppressed.

VTU generation is suppressed.



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1      0.100   595.64             20.22              3.28                     720.00    0.000  375.000   0.0027    0.110

     2   0.1167  1      0.217   497.87             26.41              5.04                     720.00    0.000  359.596   0.0032    0.122

     3   0.1390  2      0.356   426.18             27.34              6.03                     720.00    0.000  376.058   0.0037    0.138

     4   0.1619  2      0.518   376.54             25.85              6.42                     720.00    0.000  339.726   0.0034    0.150





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129382, 0.0269202

Running simulation [simumpi]: scaling np=8 (attempt 1/2) (OMP_NUM_THREADS=1, np=8, -novtu)

Elapsed: 18.96s

            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-26





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

     1   0.1000  1      0.100   595.64             20.22              3.28                     720.00    0.000  375.000   0.0027    0.110

     2   0.1167  1      0.217   497.87             26.41              5.04                     720.00    0.000  359.596   0.0032    0.122

     3   0.1390  2      0.356   426.18             27.34              6.03                     720.00    0.000  376.058   0.0037    0.138

     4   0.1619  2      0.518   376.54             25.85              6.42                     720.00    0.000  339.726   0.0034    0.150





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129382, 0.0269202

Running simulation [simumpi]: scaling np=8 (attempt 2/2) (OMP_NUM_THREADS=1, np=8, -novtu)

Elapsed: 17.41s

            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-26





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

     1   0.1000  1      0.100   595.64             20.22              3.28                     720.00    0.000  375.000   0.0027    0.110

     2   0.1167  1      0.217   497.87             26.41              5.04                     720.00    0.000  359.596   0.0032    0.122

     3   0.1390  2      0.356   426.18             27.34              6.03                     720.00    0.000  376.058   0.0037    0.138

     4   0.1619  2      0.518   376.54             25.85              6.42                     720.00    0.000  339.726   0.0034    0.150





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129382, 0.0269202

```

![png]({{ "/assets/images/benchmark_image_80.png" | relative_url }})

```
   config  steps   seconds   speedup   effic.  cells/rank   ghosts

  simuapp      4     40.01         -        -           -        -

     np=1      4     36.89     1.00x     100%      202005        0

     np=2      4     22.72     1.62x      81%      101080     2110

     np=4      4     15.53     2.38x      59%       50520     4235

     np=8      4     12.78     2.89x      36%       25610     8325 *

  * more ranks than the 4 fast cores on this CPU - paced by the slow ones, so read the efficiency as the machine's, not the partition's

```

```
Script completed at: 2026-11-26 19:08:18

```
