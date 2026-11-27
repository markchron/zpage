---
layout: default
title: "Benchmark results of resrsim"
date: 2026-11-27
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


## stflu005.dat

steam injection in corner-point grid

```
Running simulation [simuapp]: Steam injection Corner point

Elapsed: 1.05s

    22  55.0000  1     5   3650.000    62.64              2.02              3.12                      30.27    0.000    9.539 4.20e-04    0.029



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.407s  64.50%      

|- Newton                                 0.378s  |- 92.76%   

  |- Update                               0.141s    |- 37.26% 

  |- FluxJac                              0.105s    |- 27.83% 

  |- Solver                               0.039s    |- 10.36% 

  |- ScdAcc                               0.037s    |- 9.75%  

  |- update_dev                           0.022s    |- 5.83%  

  |- Precond                              0.014s    |- 3.61%  

  |- Residual                             0.006s    |- 1.64%  

  |- SanitizeJac                          0.003s    |- 0.77%  

  |- alignvar                             0.002s    |- 0.48%  

  |- PerfJac                              0.002s    |- 0.44%  

  |- HeatLoss                             0.001s    |- 0.21%  

|- Output                                 0.017s  |- 4.18%    

|- Logging                                0.002s  |- 0.37%    

|- Input                                  0.000s  |- 0.05%    

Initialization                            0.224s  35.50%      

|- execution                              0.206s  |- 91.84%   

------------------------------------------------------------

TOTAL                                     0.631s

============================================================



Time steps : 22/22, step size: 165.909, 129.097, Newton cycles: 22, linear iterations: 159

```

Three grids in one view, top to bottom: the PEBI grid (cell volume), the cylindrical grid (K permeability) and the

`stflu005` corner-point grid (pressure at its first output).

```
Loading: /Users/mark/Documents/workspace/hatch/app/test/data/pebi_resr_grid.vtk

Loading: /Users/mark/Documents/workspace/hatch/app/test/python/radial_grid.vtk

Found 23 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu005_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_1.png" | relative_url }})

# SPE4-b

* Steam flooding with water and dead oil

* VMod on 9x5x4 cartesian grid


### Load STARS

### Load ECL

### Load SMY File

Load the SMY file (`spe04b.smy`) into a pandas DataFrame, ensuring proper parsing of the data.

```
Running simulation [simuapp]: SPE4-b (-novtu)

Elapsed: 1.30s

    75  53.9980  3    34   3650.000     0.01              4.31             99.77                       5.96    0.659  235.228   0.0062    2.644



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.003s  94.21%      

|- Newton                                 0.976s  |- 97.28%   

  |- Update                               0.304s    |- 31.16% 

  |- FluxJac                              0.237s    |- 24.25% 

  |- ScdAcc                               0.104s    |- 10.63% 

  |- update_dev                           0.077s    |- 7.87%  

  |- Precond                              0.077s    |- 7.85%  

  |- Solver                               0.051s    |- 5.18%  

  |- PerfJac                              0.037s    |- 3.82%  

  |- alignvar                             0.027s    |- 2.74%  

  |- SanitizeJac                          0.026s    |- 2.68%  

  |- Residual                             0.007s    |- 0.71%  

  |- HeatLoss                             0.005s    |- 0.51%  

|- Logging                                0.011s  |- 1.12%    

|- Output                                 0.011s  |- 1.08%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.062s  5.79%       

|- execution                              0.059s  |- 95.56%   

------------------------------------------------------------

TOTAL                                     1.065s

============================================================



Time steps : 75/75, step size: 48.6667, 60.2013, Newton cycles: 386, linear iterations: 3118

```

## Select and Plot Columns

Select specific columns from the loaded DataFrames and plot them using matplotlib. For example, plot `TIME` vs `TEMP 1-1-4` from `stars_spe4b_special.csv`.

### Wells

* One row per well: bottom-hole pressure, water rate, oil rate (producers only). ECL names the producers PNEAR (EDGE PRDCR, block 5,5,4) and PFAR (CRNR PRDCR, block 9,1,1).

![png]({{ "/assets/images/benchmark_image_2.png" | relative_url }})

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

![png]({{ "/assets/images/benchmark_image_3.png" | relative_url }})

### Corner grid

```
Running simulation [simuapp]: Corner Grid (-novtu)

Elapsed: 0.82s

    38  91.8599  3    41   3650.000     0.12              4.49             97.30                       5.96    0.262  200.553   0.0087    3.754



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.514s  86.67%      

|- Newton                                 0.502s  |- 97.58%   

  |- Update                               0.153s    |- 30.55% 

  |- FluxJac                              0.117s    |- 23.38% 

  |- ScdAcc                               0.051s    |- 10.23% 

  |- Precond                              0.046s    |- 9.18%  

  |- update_dev                           0.035s    |- 7.07%  

  |- Solver                               0.031s    |- 6.19%  

  |- PerfJac                              0.020s    |- 4.07%  

  |- SanitizeJac                          0.013s    |- 2.64%  

  |- alignvar                             0.008s    |- 1.63%  

  |- Residual                             0.005s    |- 0.90%  

  |- HeatLoss                             0.003s    |- 0.68%  

|- Logging                                0.009s  |- 1.71%    

|- Output                                 0.004s  |- 0.86%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.079s  13.33%      

|- execution                              0.076s  |- 95.94%   

------------------------------------------------------------

TOTAL                                     0.593s

============================================================



Time steps : 38/40, step size: 96.0526, 98.3248, Newton cycles: 258, linear iterations: 2663

```

![png]({{ "/assets/images/benchmark_image_4.png" | relative_url }})

# Buckley- Leverett



Two phase, isothermal problem

variable order: [Sw, P, T, So, X0, X1, Sg]



Acc w.r.t. [Sw, So, Sg, X0, X1, P, T]

```
Running simulation [simuapp]: Buckley-Leverett (-novtu)

Elapsed: 0.89s

    79   5.0372  1     1     10.000    5e-10              0.16            100.00                       0.16   12.729    0.005 7.02e-06  4.9e-07



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.622s  88.13%      

|- Newton                                 0.611s  |- 98.28%   

  |- Update                               0.214s    |- 34.93% 

  |- FluxJac                              0.083s    |- 13.62% 

  |- ScdAcc                               0.074s    |- 12.16% 

  |- Precond                              0.072s    |- 11.74% 

  |- update_dev                           0.038s    |- 6.26%  

  |- PerfJac                              0.033s    |- 5.33%  

  |- SanitizeJac                          0.022s    |- 3.67%  

  |- Solver                               0.016s    |- 2.63%  

  |- alignvar                             0.015s    |- 2.50%  

  |- HeatLoss                             0.012s    |- 1.98%  

  |- Residual                             0.009s    |- 1.53%  

|- Logging                                0.010s  |- 1.66%    

|- Output                                 0.003s  |- 0.55%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.084s  11.87%      

|- execution                              0.081s  |- 96.60%   

------------------------------------------------------------

TOTAL                                     0.706s

============================================================



Time steps : 79/81, step size: 0.126582, 0.652368, Newton cycles: 489, linear iterations: 489

```

### Load Benchmark

### Buckley Plot

![png]({{ "/assets/images/benchmark_image_5.png" | relative_url }})

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

Elapsed: 0.87s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.606s  89.60%      

|- Newton                                 0.599s  |- 98.85%   

  |- Update                               0.256s    |- 42.66% 

  |- FluxJac                              0.107s    |- 17.86% 

  |- ScdAcc                               0.072s    |- 12.09% 

  |- update_dev                           0.041s    |- 6.86%  

  |- Precond                              0.038s    |- 6.32%  

  |- HeatLoss                             0.019s    |- 3.10%  

  |- Solver                               0.016s    |- 2.61%  

  |- Residual                             0.013s    |- 2.15%  

  |- PerfJac                              0.009s    |- 1.52%  

  |- SanitizeJac                          0.007s    |- 1.24%  

  |- alignvar                             0.006s    |- 1.03%  

|- Output                                 0.005s  |- 0.86%    

|- Logging                                0.001s  |- 0.25%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.070s  10.40%      

|- execution                              0.067s  |- 94.78%   

------------------------------------------------------------

TOTAL                                     0.676s

============================================================



Time steps : 10/18, step size: 12.6635, 22.211, Newton cycles: 138, linear iterations: 138

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

![png]({{ "/assets/images/benchmark_image_6.png" | relative_url }})

The relative error is largest, and concentrated right at the advancing front, for the snapshots

taken before the analytic breakthrough time (~13.8 days) - the expected signature of numerical

dispersion smearing Lauwerier's mathematically sharp step. Once every cell is past its own local

breakthrough (t >~ 32 days) the profile is governed by the smoother post-breakthrough erfc tail,

and the relative L2 error over the whole 804-cell row drops accordingly.

![png]({{ "/assets/images/benchmark_image_7.png" | relative_url }})

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

    18   1.1910  1     1     10.000                                                                 9521.20    0.048  145.831             0.834



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Initialization                            0.061s  56.44%      

|- execution                              0.059s  |- 96.38%   

Timeloop                                  0.047s  43.56%      

|- Newton                                 0.043s  |- 90.68%   

  |- Update                               0.014s    |- 33.99% 

  |- Precond                              0.006s    |- 14.91% 

  |- PerfJac                              0.005s    |- 12.04% 

  |- ScdAcc                               0.004s    |- 9.36%  

  |- FluxJac                              0.004s    |- 8.90%  

  |- update_dev                           0.003s    |- 6.43%  

  |- SanitizeJac                          0.002s    |- 5.74%  

  |- alignvar                             0.001s    |- 3.13%  

  |- Solver                               0.001s    |- 2.57%  

  |- Residual                             0.000s    |- 0.44%  

  |- HeatLoss                             0.000s    |- 0.01%  

|- Output                                 0.003s  |- 6.69%    

|- Logging                                0.001s  |- 1.44%    

|- Input                                  0.000s  |- 0.07%    

------------------------------------------------------------

TOTAL                                     0.108s

============================================================



Time steps : 18/21, step size: 0.555556, 0.370895, Newton cycles: 75, linear iterations: 75

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

![png]({{ "/assets/images/benchmark_image_8.png" | relative_url }})

The mismatch is concentrated at the advancing front and shrinks as cells fully equilibrate - the

same numerical-dispersion signature as the Lauwerier comparison above, not a sign the two models

disagree on the front's speed. `avd_mdot` is the deck's design target (100 kg/s); the remaining

gap is plausibly the well's day-0-to-5.5 ramp from bottom-hole-pressure control up to the rate

target (the analytic solution assumes that full rate from t=0), compounded by this deck's coarse

15-block grid - only the first 3-4 blocks sit inside the thermal front by day 10.


![png]({{ "/assets/images/benchmark_image_9.png" | relative_url }})

# MISC

## spe04b_cw.dat

```
Running simulation [simuapp]: SPE4-b water flooding (-novtu)

Elapsed: 0.61s

    22 163.1620  2    26   3650.000     0.78             10.19             92.87                      10.73    0.000   13.701   0.0097    0.002



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.348s  84.08%      

|- Newton                                 0.343s  |- 98.70%   

  |- Update                               0.112s    |- 32.71% 

  |- FluxJac                              0.095s    |- 27.62% 

  |- Solver                               0.038s    |- 11.10% 

  |- ScdAcc                               0.033s    |- 9.51%  

  |- update_dev                           0.021s    |- 6.23%  

  |- Precond                              0.021s    |- 6.04%  

  |- PerfJac                              0.006s    |- 1.75%  

  |- SanitizeJac                          0.005s    |- 1.32%  

  |- Residual                             0.004s    |- 1.21%  

  |- alignvar                             0.003s    |- 1.01%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.001s  |- 0.42%    

|- Logging                                0.001s  |- 0.35%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.066s  15.92%      

|- execution                              0.064s  |- 96.45%   

------------------------------------------------------------

TOTAL                                     0.414s

============================================================



Time steps : 22/22, step size: 165.909, 155.032, Newton cycles: 74, linear iterations: 793

```



## watfld_cw.dat

```
Running simulation [simuapp]: SPE4-b Water flooding without vmod (-novtu)

Elapsed: 0.77s

    35  32.0338  2    33   3650.000     1.04             79.00             98.70                      80.00    0.000    1.842   0.0027  3.1e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.519s  88.51%      

|- Newton                                 0.510s  |- 98.25%   

  |- Update                               0.161s    |- 31.55% 

  |- FluxJac                              0.133s    |- 26.11% 

  |- Solver                               0.061s    |- 12.04% 

  |- ScdAcc                               0.044s    |- 8.63%  

  |- update_dev                           0.031s    |- 6.08%  

  |- Precond                              0.029s    |- 5.70%  

  |- PerfJac                              0.027s    |- 5.24%  

  |- SanitizeJac                          0.006s    |- 1.22%  

  |- Residual                             0.006s    |- 1.14%  

  |- alignvar                             0.005s    |- 0.90%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.003s  |- 0.58%    

|- Logging                                0.002s  |- 0.33%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.067s  11.49%      

|- execution                              0.065s  |- 96.50%   

------------------------------------------------------------

TOTAL                                     0.586s

============================================================



Time steps : 35/35, step size: 104.286, 142.716, Newton cycles: 98, linear iterations: 1555

```

## stflu001.dat

Inverted 9 spot hot water flooding with area/block modifier, 5 point transmissibility


```
Running simulation [simuapp]: Inverted 9 spot hot water flooding (-novtu)

Elapsed: 1.00s

    88 365.0000  2    18   3650.000    3e-04            560.95            100.00                     560.95    0.004    0.742 6.55e-04    0.019



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.748s  92.74%      

|- Newton                                 0.734s  |- 98.21%   

  |- Update                               0.239s    |- 32.56% 

  |- FluxJac                              0.177s    |- 24.14% 

  |- ScdAcc                               0.075s    |- 10.24% 

  |- Precond                              0.070s    |- 9.55%  

  |- update_dev                           0.050s    |- 6.84%  

  |- Solver                               0.044s    |- 5.99%  

  |- SanitizeJac                          0.020s    |- 2.78%  

  |- alignvar                             0.015s    |- 1.98%  

  |- PerfJac                              0.013s    |- 1.71%  

  |- Residual                             0.008s    |- 1.15%  

  |- HeatLoss                             0.006s    |- 0.83%  

|- Output                                 0.007s  |- 0.96%    

|- Logging                                0.006s  |- 0.74%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.059s  7.26%       

|- execution                              0.056s  |- 95.70%   

------------------------------------------------------------

TOTAL                                     0.806s

============================================================



Time steps : 88/89, step size: 41.4773, 100.513, Newton cycles: 449, linear iterations: 3162

```

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation, CMG against OURS.

![png]({{ "/assets/images/benchmark_image_10.png" | relative_url }})

## stflu002.dat

5000x5000x50, 2D diagonal water flooding in uniformed cartesian

```
Running simulation [simuapp]: Uniformed cartesian water flooding (-novtu)

Elapsed: 0.38s

    49 331.7630  3    38   3650.000   624.41             11.54              1.82                     635.95    0.000  1.1e+03   0.0499    0.028



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.134s  67.66%      

|- Newton                                 0.126s  |- 94.25%   

  |- Update                               0.047s    |- 37.44% 

  |- FluxJac                              0.022s    |- 17.66% 

  |- Precond                              0.012s    |- 9.82%  

  |- ScdAcc                               0.012s    |- 9.80%  

  |- update_dev                           0.007s    |- 5.50%  

  |- Solver                               0.006s    |- 5.12%  

  |- PerfJac                              0.005s    |- 4.29%  

  |- SanitizeJac                          0.004s    |- 2.86%  

  |- alignvar                             0.002s    |- 1.90%  

  |- HeatLoss                             0.002s    |- 1.64%  

  |- Residual                             0.002s    |- 1.60%  

|- Output                                 0.002s  |- 1.76%    

|- Logging                                0.002s  |- 1.28%    

|- Input                                  0.000s  |- 0.08%    

Initialization                            0.064s  32.34%      

|- execution                              0.061s  |- 95.82%   

------------------------------------------------------------

TOTAL                                     0.197s

============================================================



Time steps : 49/49, step size: 74.4898, 130.909, Newton cycles: 77, linear iterations: 577

```



## stflu003.dat

5000x5000x50, 2D diagonal water flooding in uniformed corner point

```
Running simulation [simuapp]: uniformed corner grid (-novtu)

Elapsed: 0.37s

    46 252.4658  2    25   3650.000   624.71             11.24              1.77                     635.95    0.000  740.056   0.0380    0.017



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.123s  65.35%      

|- Newton                                 0.117s  |- 94.72%   

  |- Update                               0.042s    |- 36.42% 

  |- FluxJac                              0.021s    |- 18.38% 

  |- Precond                              0.012s    |- 10.17% 

  |- ScdAcc                               0.011s    |- 9.62%  

  |- update_dev                           0.006s    |- 5.53%  

  |- Solver                               0.006s    |- 5.36%  

  |- PerfJac                              0.005s    |- 4.30%  

  |- SanitizeJac                          0.003s    |- 2.88%  

  |- alignvar                             0.002s    |- 1.97%  

  |- HeatLoss                             0.002s    |- 1.55%  

  |- Residual                             0.002s    |- 1.52%  

|- Output                                 0.002s  |- 1.68%    

|- Logging                                0.001s  |- 1.01%    

|- Input                                  0.000s  |- 0.07%    

Initialization                            0.065s  34.65%      

|- execution                              0.062s  |- 95.70%   

------------------------------------------------------------

TOTAL                                     0.188s

============================================================



Time steps : 46/46, step size: 79.3478, 130.764, Newton cycles: 72, linear iterations: 603

```

![png]({{ "/assets/images/benchmark_image_11.png" | relative_url }})



## stflu004.dat

2D diagonal water flooding for reduction of numerical dispersion and grid orientation effect


```
Running simulation [simuapp]: 2D diagonal flow: grid orientation

Elapsed: 0.83s

    61  58.7733  2    35   3650.000   613.68             22.27              3.50                     635.95    0.000  682.222   0.0196    0.034



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.485s  82.78%      

|- Newton                                 0.455s  |- 93.76%   

  |- Update                               0.197s    |- 43.37% 

  |- FluxJac                              0.087s    |- 19.14% 

  |- ScdAcc                               0.044s    |- 9.62%  

  |- Solver                               0.032s    |- 7.07%  

  |- Precond                              0.026s    |- 5.73%  

  |- update_dev                           0.024s    |- 5.36%  

  |- PerfJac                              0.009s    |- 1.95%  

  |- alignvar                             0.007s    |- 1.43%  

  |- SanitizeJac                          0.006s    |- 1.35%  

  |- HeatLoss                             0.006s    |- 1.24%  

  |- Residual                             0.005s    |- 1.18%  

|- Output                                 0.024s  |- 4.98%    

|- Logging                                0.004s  |- 0.91%    

|- Input                                  0.000s  |- 0.03%    

Initialization                            0.101s  17.22%      

|- execution                              0.098s  |- 97.13%   

------------------------------------------------------------

TOTAL                                     0.586s

============================================================



Time steps : 61/61, step size: 59.8361, 80.636, Newton cycles: 109, linear iterations: 1598

```

![png]({{ "/assets/images/benchmark_image_12.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_13.png" | relative_url }})

## stflu007.dat

PEBI_GRID


```
Running simulation [simuapp]: 2D diagonal flow: pebi grid

Elapsed: 0.89s

    59 354.7237  3    58   3650.000   623.41             12.54              1.97                     635.95    0.000  1.3e+03   0.0717    0.046



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.572s  84.99%      

|- Newton                                 0.540s  |- 94.44%   

  |- Update                               0.182s    |- 33.63% 

  |- FluxJac                              0.160s    |- 29.61% 

  |- Solver                               0.051s    |- 9.48%  

  |- ScdAcc                               0.046s    |- 8.56%  

  |- Precond                              0.029s    |- 5.33%  

  |- update_dev                           0.029s    |- 5.28%  

  |- HeatLoss                             0.008s    |- 1.54%  

  |- Residual                             0.008s    |- 1.50%  

  |- PerfJac                              0.007s    |- 1.24%  

  |- SanitizeJac                          0.006s    |- 1.09%  

  |- alignvar                             0.004s    |- 0.73%  

|- Output                                 0.025s  |- 4.33%    

|- Logging                                0.002s  |- 0.43%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.101s  15.01%      

|- execution                              0.088s  |- 86.73%   

------------------------------------------------------------

TOTAL                                     0.673s

============================================================



Time steps : 59/59, step size: 61.8644, 119.417, Newton cycles: 92, linear iterations: 1054

```

![png]({{ "/assets/images/benchmark_image_14.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_15.png" | relative_url }})

## stflu026.dat

* Steam flood on two component live oil

```
Running simulation [simuapp]: 3 component steam flooding (-novtu)

Elapsed: 1.48s

    89 261.3693  8   103   3650.000     0.01              4.44             99.84                       5.96    0.400  1.0e+03   0.0804   12.068



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.219s  94.94%      

|- Newton                                 1.197s  |- 98.17%   

  |- Update                               0.332s    |- 27.73% 

  |- FluxJac                              0.297s    |- 24.81% 

  |- ScdAcc                               0.114s    |- 9.53%  

  |- Precond                              0.096s    |- 8.00%  

  |- Solver                               0.094s    |- 7.87%  

  |- update_dev                           0.086s    |- 7.23%  

  |- PerfJac                              0.046s    |- 3.88%  

  |- SanitizeJac                          0.025s    |- 2.10%  

  |- alignvar                             0.021s    |- 1.78%  

  |- Residual                             0.010s    |- 0.86%  

  |- HeatLoss                             0.008s    |- 0.69%  

|- Logging                                0.020s  |- 1.61%    

|- Output                                 0.008s  |- 0.65%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.065s  5.06%       

|- execution                              0.062s  |- 95.07%   

------------------------------------------------------------

TOTAL                                     1.284s

============================================================



Time steps : 89/89, step size: 41.0112, 73.9959, Newton cycles: 519, linear iterations: 4176

```

#### Load OURS, CMG and ECL

* STARS wells: CRNR PRDCR, EDGE PRDCR, INJECTOR. STARS block history at (1,1,4), (5,5,4), (9,1,1) and (5,4,1); ECL has the first three only.

* ECL names the two producers PNEAR (EDGE PRDCR, block 5,5,4) and PFAR (CRNR PRDCR, block 9,1,1); PNEAR produces twice PFAR at the start, as EDGE does CRNR.

```
OURS reached day 3650.0 of 3650

```

### Wells

* One row per well: bottom-hole pressure, water rate, oil rate (producers only).

![png]({{ "/assets/images/benchmark_image_16.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation. (5,4,1) has no ECL curve.

![png]({{ "/assets/images/benchmark_image_17.png" | relative_url }})

# SPE4C

* Steam flood on three component live oil

* 'Water', 'LiteOil', 'Medm oil', 'Heavy oil'


## Run & Load

```
Running simulation [simuapp]: SPE4-C benchmark on live oil (-novtu)

Elapsed: 1.69s

    93 152.7778  6    68   3650.000     0.01              4.30             99.79                       5.11    0.006  287.567   0.0321    4.784



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.394s  95.31%      

|- Newton                                 1.371s  |- 98.38%   

  |- Update                               0.368s    |- 26.88% 

  |- FluxJac                              0.320s    |- 23.34% 

  |- Solver                               0.172s    |- 12.51% 

  |- Precond                              0.138s    |- 10.10% 

  |- ScdAcc                               0.131s    |- 9.58%  

  |- update_dev                           0.099s    |- 7.25%  

  |- PerfJac                              0.052s    |- 3.78%  

  |- SanitizeJac                          0.027s    |- 1.93%  

  |- alignvar                             0.017s    |- 1.24%  

  |- Residual                             0.011s    |- 0.78%  

  |- HeatLoss                             0.009s    |- 0.66%  

|- Logging                                0.010s  |- 0.73%    

|- Output                                 0.009s  |- 0.65%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.069s  4.69%       

|- execution                              0.066s  |- 95.93%   

------------------------------------------------------------

TOTAL                                     1.462s

============================================================



Time steps : 93/97, step size: 39.2473, 57.1343, Newton cycles: 544, linear iterations: 4556

```

#### Load CMG

### Load ECL

### Wells

* One row per well: bottom-hole pressure, water rate, oil rate (producers only). ECL names the producers PNEAR (EDGE PRDCR) and PFAR (CRNR PRDCR).

![png]({{ "/assets/images/benchmark_image_18.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation, CMG and ECL against OURS.

![png]({{ "/assets/images/benchmark_image_19.png" | relative_url }})

# Cyclic steam stimulation

## CSS SPE4

stspe001.dat: Cyclic steam stimulation on radial grid

```
Running simulation [simuapp]: Cyclic steam stimulation in Radial grid

Elapsed: 1.02s

   120  15.1549  6    24   1095.000     0.95              0.55             36.93                               0.106   44.616   0.0873    0.883



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.743s  91.77%      

|- Newton                                 0.692s  |- 93.15%   

  |- Update                               0.211s    |- 30.46% 

  |- FluxJac                              0.116s    |- 16.78% 

  |- Precond                              0.089s    |- 12.82% 

  |- ScdAcc                               0.066s    |- 9.59%  

  |- PerfJac                              0.044s    |- 6.40%  

  |- update_dev                           0.043s    |- 6.19%  

  |- SanitizeJac                          0.030s    |- 4.30%  

  |- Solver                               0.025s    |- 3.64%  

  |- alignvar                             0.015s    |- 2.20%  

  |- Residual                             0.005s    |- 0.78%  

  |- HeatLoss                             0.004s    |- 0.57%  

|- Output                                 0.035s  |- 4.75%    

|- Logging                                0.023s  |- 3.13%    

|- Input                                  0.001s  |- 0.14%    

Initialization                            0.067s  8.23%       

|- execution                              0.064s  |- 95.65%   

------------------------------------------------------------

TOTAL                                     0.810s

============================================================



Time steps : 120/129, step size: 9.125, 18.3752, Newton cycles: 672, linear iterations: 2965

```

### Wells

* Injector: bottom-hole pressure (ECL only; the CMG well export has none) and water rate. Producer: bottom-hole pressure (ECL only), water and oil rate.

* Bottom-hole pressure is drawn only while the well flows: ECL reports 0 for a shut-in well and OURS holds its last value.

![png]({{ "/assets/images/benchmark_image_20.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation, CMG and ECL against OURS.

![png]({{ "/assets/images/benchmark_image_21.png" | relative_url }})



## stflu008.dat

Cyclic steam stimulation on cartesian grid


```
Running simulation [simuapp]: Cyclic steam stimulation in Cartesian

Elapsed: 9.15s

   153  53.9655  6    77   1095.000     1.34              1.17             46.66                               0.073   31.620   0.0691    3.479



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  8.882s  99.08%      

|- Newton                                 8.759s  |- 98.61%   

  |- FluxJac                              2.880s    |- 32.88% 

  |- Update                               2.638s    |- 30.12% 

  |- Solver                               0.973s    |- 11.11% 

  |- ScdAcc                               0.728s    |- 8.31%  

  |- update_dev                           0.575s    |- 6.57%  

  |- Precond                              0.419s    |- 4.78%  

  |- Residual                             0.094s    |- 1.07%  

  |- HeatLoss                             0.082s    |- 0.94%  

  |- SanitizeJac                          0.077s    |- 0.88%  

  |- PerfJac                              0.076s    |- 0.86%  

  |- alignvar                             0.058s    |- 0.67%  

|- Output                                 0.095s  |- 1.07%    

|- Logging                                0.037s  |- 0.41%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.083s  0.92%       

|- execution                              0.080s  |- 96.50%   

------------------------------------------------------------

TOTAL                                     8.965s

============================================================



Time steps : 153/161, step size: 7.15686, 14.9924, Newton cycles: 883, linear iterations: 8182

```

### Wells

![png]({{ "/assets/images/benchmark_image_22.png" | relative_url }})

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

Elapsed: 25.42s

   124  72.3966 12   185   1095.000     1.63              0.86             34.51                               0.029   41.919   0.1014    4.631



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 25.049s  99.42%      

|- Newton                                24.808s  |- 99.04%   

  |- FluxJac                              8.601s    |- 34.67% 

  |- Update                               6.961s    |- 28.06% 

  |- Solver                               4.681s    |- 18.87% 

  |- ScdAcc                               1.621s    |- 6.54%  

  |- update_dev                           1.308s    |- 5.27%  

  |- Precond                              0.788s    |- 3.18%  

  |- Residual                             0.224s    |- 0.90%  

  |- HeatLoss                             0.103s    |- 0.42%  

  |- alignvar                             0.099s    |- 0.40%  

  |- SanitizeJac                          0.063s    |- 0.25%  

  |- PerfJac                              0.043s    |- 0.17%  

|- Output                                 0.207s  |- 0.83%    

|- Logging                                0.016s  |- 0.06%    

|- Input                                  0.001s  |- 0.00%    

Initialization                            0.146s  0.58%       

|- execution                              0.103s  |- 70.98%   

------------------------------------------------------------

TOTAL                                    25.194s

============================================================



Time steps : 124/126, step size: 8.83065, 20.2824, Newton cycles: 514, linear iterations: 4474

```

![png]({{ "/assets/images/benchmark_image_23.png" | relative_url }})

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

Elapsed: 15.28s

   251  32.6059  6    71   1095.000     1.73              1.20             40.86                               0.024   20.899   0.0655    2.003



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 14.931s  99.12%      

|- Newton                                14.718s  |- 98.57%   

  |- FluxJac                              5.012s    |- 34.06% 

  |- Update                               4.085s    |- 27.76% 

  |- Solver                               2.242s    |- 15.23% 

  |- ScdAcc                               1.109s    |- 7.54%  

  |- update_dev                           0.825s    |- 5.61%  

  |- Precond                              0.649s    |- 4.41%  

  |- PerfJac                              0.159s    |- 1.08%  

  |- Residual                             0.142s    |- 0.96%  

  |- SanitizeJac                          0.122s    |- 0.83%  

  |- alignvar                             0.093s    |- 0.63%  

  |- HeatLoss                             0.066s    |- 0.45%  

|- Output                                 0.169s  |- 1.13%    

|- Logging                                0.042s  |- 0.28%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.132s  0.88%       

|- execution                              0.112s  |- 84.69%   

------------------------------------------------------------

TOTAL                                    15.063s

============================================================



Time steps : 251/261, step size: 4.36255, 10.7879, Newton cycles: 1261, linear iterations: 12373

```

#### Temperature fields of the cyclic steam runs

The last output of each run, 2 by 2: the radial grid of `stspe001` and the Cartesian `stflu008` on top, the uniform PEBI

`stflu009` and the graded PEBI `stflu025` below.

```
Found 121 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stspe001_00120.vtu

Found 154 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu008_00153.vtu

Found 125 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu009_00124.vtu

Found 252 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu025_00251.vtu

```

![png]({{ "/assets/images/benchmark_image_24.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_25.png" | relative_url }})

### stflu013.dat - SPE4 problem 1A, cyclic steam

* 20x20x4 corner-point FIELD grid, water and dead oil with no gas component. One well location is modelled as two wells that are never open together: 'Injector 1' (`*MAX *STW 1000`, BHP limit 10000 psi) and 'Producer 1' (`*MAX *STL 1000`, `*MIN *BHP 17`). Three cycles of 10 days of injection, 7 of soak, then production, ending at days 365, 730 and 1095.

* Reference is the DeepFlow THERM `stars_stflu013.log` time step summary, one row per step. simuapp is run with `-log` to write the same table, so both sides are read the same way. THERM is in bbl/day, ours in m3/day.

* No free gas is produced, so the gas and GOR columns of both logs are blank. `read_step_summary_log()` drops blank fields and would leave the rates NaN, so this section reads the table by column position instead.

```
Running simulation [simuapp]: Cyclic steam stimulation, SPE4 problem 1A (-novtu)

Elapsed: 7.20s

No text to display.

```

```
OURS reached day 1095.0 of 1095

THERM: 77 steps marched, 0 cuts, 96 Newton cycles, material balance error 0.021 % at the last step

 OURS: 95 steps marched, 6 cuts, 339 Newton cycles, 2139 linear iterations, material balance error 0.033 % at the last step

```

### Wells

* Field totals from the time step summary, in m3/day at standard conditions. While injecting, 'Injector 1' holds its 1000 bbl/day (158.99 m3/day) `*STW` target; while producing, 'Producer 1' holds 1000 bbl/day of liquid, so the oil and water curves must sum to the same target. The liquid panel checks that sum directly.

![png]({{ "/assets/images/benchmark_image_26.png" | relative_url }})

### Step size

* Steps are compared on simulated time, not step number: the two programs march different counts.

* The first run in `runs` is the reference; the right panel is the interpolated dt ratio to it.

* Fewer steps and Newton cycles at the same end time is cheaper, but only counts when the well curves above still agree.

```
run             THERM  OURS

steps              77    95

newton             96   339

newton/step     1.247 3.568

linear            NaN  2139

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

![png]({{ "/assets/images/benchmark_image_27.png" | relative_url }})

### stflu015.dat - single producer on a corner-point grid

* 14x14x5 corner-point FIELD grid, water and dead oil with no gas component. One producer, 'Producer', perforated in block (1,1,1) on `*OPERATE *MAX *STL 400` with a `*MIN *BHP 17` limit. There is no injector, so this is a depletion run to day 365, from an initial `*REFPRES 1000`.

* Reference is the DeepFlow THERM `stars_stflu015.log` time step summary, read with `read_step_summary_columns()` from the stflu013 section above (gas and GOR are blank in both logs). THERM is in bbl/day, ours in m3/day.

* Our log prints the rates with two decimals, so the water curve is coarse.

```
Running simulation [simuapp]: Corner grid, single producer on STL (-novtu)

Elapsed: 0.46s

No text to display.

```

```
OURS reached day 365.0 of 365

THERM: 14 steps marched, 0 cuts, 14 Newton cycles, material balance error 5e-06 % at the last step

 OURS: 14 steps marched, 0 cuts, 14 Newton cycles, 28 linear iterations, material balance error 0 % at the last step

```

### Wells

* Field totals from the time step summary, in m3/day at standard conditions. 'Producer' holds 400 bbl/day (63.6 m3/day) of liquid on `*STL`, so oil plus water must sit on that target; the liquid panel checks the sum directly.

![png]({{ "/assets/images/benchmark_image_28.png" | relative_url }})

### Step size

* Steps are compared on simulated time, not step number: the two programs march different counts.

* The first run in `runs` is the reference; the right panel is the interpolated dt ratio to it.

* Fewer steps and Newton cycles at the same end time is cheaper, but only counts when the well curves above still agree.

```
run           THERM  OURS

steps            14    14

newton           14    14

newton/step       1     1

linear          NaN    28

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

![png]({{ "/assets/images/benchmark_image_29.png" | relative_url }})

### stflu006.dat - solution-gas oil on a corner-point grid

* 5x14x17 corner-point FIELD grid (`*COORD` / `*ZCORN`, dipping from 7400 to 10800 ft), components `WATER`, `OIL` and `Soln_Gas`, at 125 F and `*REFPRES 1000` in block (1,1,1), Sw 0.47, no free gas, 0.1228 mole fraction of dissolved gas in the oil. One producer, 'PRODUCER', on `*OPERATE *MAX *STL 1000` with a `*MIN *BHP 170` limit; the steam injector is commented out in the deck (the title still names steam). A depletion run to day 3650.

* Reference is the DeepFlow THERM `stars_stflu006.log` time step summary, read with `read_step_summary_columns()` from the stflu013 section above (injection columns are blank in both logs). THERM is in bbl/day and ft3/day, ours in m3/day.

* Our log prints the rates with two decimals, so the water curve is stepped.

```
Running simulation [simuapp]: Solution-gas oil on a corner-point grid (-novtu)

Elapsed: 0.71s

No text to display.

```

```
OURS reached day 3650.0 of 3650

THERM: 28 steps marched, 0 cuts, 28 Newton cycles

 OURS: 28 steps marched, 0 cuts, 28 Newton cycles, 226 linear iterations

```

### Wells

* Field totals from the time step summary, in m3/day at standard conditions: the one producer, on its BHP limit (ours holds 1172.1 kPa, 170 psi, throughout).

* Ours starts 2.7% below THERM in oil (108.3 against 111.3 m3/day) and ends 4.2% above (93.9 against 90.1): the curves cross near day 800, because ours declines 13% over the run and THERM 19%. Gas and water start 2.5% and 2.6% low, and the mean absolute gap over THERM's steps is 2.4% in oil, 2.6% in gas and 2.2% in water. The water cut starts equal (1.85%) and ends at 2.07 against 2.19%. The decline gap is not explained yet.

```
 day  oil THERM  gas THERM  water THERM  oil OURS  gas OURS  water OURS

   1      111.3      591.8        2.094     108.3     576.9        2.04

 595        102      540.9        2.092     101.6     541.2        2.04

1095      98.48      523.9         2.08     99.32     529.1        2.03

2095      94.15      501.2        2.054     96.57     514.5        2.01

3650       90.1      478.6        2.018     93.88     500.2        1.99

mean |gap| to THERM over its steps, %: oil 2.4, gas 2.6, water 2.2

```

![png]({{ "/assets/images/benchmark_image_30.png" | relative_url }})

### Step size

* Both programs march the same 28 steps with no cut and one Newton cycle per step; the steps are set by `dtmax` 200 and the `*TIME` cards, so the step-size panels coincide.

```
run              THERM  OURS

steps               28    28

newton              28    28

newton/step          1     1

linear             NaN   226

cuts                 0     0

dt min               1     1

dt geomean       80.11 80.36

dt max             200   200

end day           3650  3650

steps@3.65d          2     2

steps@36.5d          4     4

steps@365d           7     7

steps@1.82e+03d     16    16

steps@3.65e+03d     28    28

```

![png]({{ "/assets/images/benchmark_image_31.png" | relative_url }})

### VAPEX (2D) Experiment 

* incomp gas

* 'WATER' 'LLOYD_O' 'ASPHALT' 'PROPANE'

* MOD

* 9 hours

```
Running simulation [simuapp]: Incomp GAS (-novtu)

Elapsed: 3.07s

No text to display.

```

### Wells

![png]({{ "/assets/images/benchmark_image_32.png" | relative_url }})

### Step size

* Steps are compared on simulated time, not step number: the two programs march different counts.

* The first run in `runs` is the reference; the right panel is the interpolated dt ratio to it.

* Fewer steps and Newton cycles at the same end time is cheaper, but only counts when the well curves above still agree.

```
run                 THERM      OURS

steps                  61       278

newton                224      1501

newton/step         3.672     5.399

linear                NaN 1.139e+04

cuts                    1        15

dt min            5.8e-06  4.63e-06

dt geomean      0.0001588  0.001014

dt max             0.0016   0.00175

end day           0.01736     0.375

steps@1.74e-05d         2         3

steps@0.000174d        10         9

steps@0.00174d         21        16

steps@0.00868d         47        35

steps@0.0174d          61        57

```

![png]({{ "/assets/images/benchmark_image_33.png" | relative_url }})

### SAGD

#### 2D cross the well

```
Running simulation [simuapp]: SAGD (-novtu)

Elapsed: 2.79s

   207   1.7935  1    14   2526.000     3.48             51.20             93.63                      50.95    0.004    0.356   0.0056    0.353



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.430s  96.65%      

|- Newton                                 2.394s  |- 98.54%   

  |- Update                               0.758s    |- 31.67% 

  |- FluxJac                              0.597s    |- 24.94% 

  |- ScdAcc                               0.269s    |- 11.23% 

  |- Precond                              0.193s    |- 8.08%  

  |- update_dev                           0.181s    |- 7.55%  

  |- Solver                               0.179s    |- 7.47%  

  |- SanitizeJac                          0.059s    |- 2.45%  

  |- alignvar                             0.040s    |- 1.68%  

  |- PerfJac                              0.034s    |- 1.43%  

  |- Residual                             0.029s    |- 1.23%  

  |- HeatLoss                             0.005s    |- 0.22%  

|- Logging                                0.018s  |- 0.73%    

|- Output                                 0.012s  |- 0.49%    

|- Input                                  0.001s  |- 0.02%    

Initialization                            0.084s  3.35%       

|- execution                              0.081s  |- 96.53%   

------------------------------------------------------------

TOTAL                                     2.514s

============================================================



Time steps : 207/210, step size: 12.2029, 14.494, Newton cycles: 1006, linear iterations: 12338

```

### Wells

* The reference here is the in-house Fortran code (stm_stflu020_*.csv), labelled FORTRAN. It reports producer rates negative.

![png]({{ "/assets/images/benchmark_image_34.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, water, oil and gas saturation. (1,5,13) sits near the injector and (1,5,18) near the producer.

![png]({{ "/assets/images/benchmark_image_35.png" | relative_url }})

#### 2D along well

```
Running simulation [simuapp]: SAGD (-novtu)

Elapsed: 3.60s

   178 113.2794  3    32   2526.000     2.23            149.16             98.53                     150.00    0.445   75.573   0.0406    5.069



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  3.320s  97.63%      

|- Newton                                 3.272s  |- 98.58%   

  |- Update                               0.944s    |- 28.85% 

  |- FluxJac                              0.691s    |- 21.11% 

  |- PerfJac                              0.546s    |- 16.68% 

  |- ScdAcc                               0.302s    |- 9.22%  

  |- update_dev                           0.207s    |- 6.33%  

  |- Precond                              0.194s    |- 5.91%  

  |- Solver                               0.168s    |- 5.14%  

  |- SanitizeJac                          0.052s    |- 1.60%  

  |- alignvar                             0.039s    |- 1.18%  

  |- Residual                             0.034s    |- 1.03%  

  |- HeatLoss                             0.006s    |- 0.18%  

|- Logging                                0.027s  |- 0.81%    

|- Output                                 0.017s  |- 0.51%    

|- Input                                  0.001s  |- 0.02%    

Initialization                            0.081s  2.37%       

|- execution                              0.077s  |- 95.02%   

------------------------------------------------------------

TOTAL                                     3.400s

============================================================



Time steps : 178/189, step size: 14.191, 22.7331, Newton cycles: 1010, linear iterations: 9186

```

### Wells

![png]({{ "/assets/images/benchmark_image_36.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation. The blocks follow the producer-injector pair down the 10x1x20 grid.

![png]({{ "/assets/images/benchmark_image_37.png" | relative_url }})

#### 3D

```
Running simulation [simuapp]: SAGD 3D (-novtu)

Elapsed: 16.19s

   145   7.3972  3    70    680.000    13.34             87.04             86.71                      93.21    0.000    4.364   0.1517    9.412



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 15.865s  99.36%      

|- Newton                                15.798s  |- 99.58%   

  |- FluxJac                              4.977s    |- 31.51% 

  |- Update                               4.597s    |- 29.10% 

  |- Solver                               2.781s    |- 17.60% 

  |- ScdAcc                               1.146s    |- 7.26%  

  |- update_dev                           0.927s    |- 5.87%  

  |- Precond                              0.526s    |- 3.33%  

  |- PerfJac                              0.288s    |- 1.82%  

  |- Residual                             0.152s    |- 0.96%  

  |- alignvar                             0.087s    |- 0.55%  

  |- SanitizeJac                          0.066s    |- 0.42%  

  |- HeatLoss                             0.056s    |- 0.35%  

|- Output                                 0.021s  |- 0.13%    

|- Logging                                0.018s  |- 0.11%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.102s  0.64%       

|- execution                              0.096s  |- 94.54%   

------------------------------------------------------------

TOTAL                                    15.967s

============================================================



Time steps : 145/150, step size: 4.68966, 4.48137, Newton cycles: 663, linear iterations: 11735

```

#### 2D live oil

* 10x1x20 cross-section, two-component live oil (CH4 + HOIL) with water. Injector 'Inj' (2:9,1,13) and producer 'Prod' (2:9,1,18); both are shut in and preheated for 60 days, then opened.

* CMG only (no ECL run for this deck).

```
Running simulation [simuapp]: SAGD live oil (-novtu)

Elapsed: 3.87s

   151 181.8788  6    73   2526.000     2.40     0.01   149.46     0.00    98.42                     150.00    0.026  135.358   0.0774   11.678



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  3.622s  98.10%      

|- Newton                                 3.582s  |- 98.88%   

  |- Update                               0.879s    |- 24.53% 

  |- FluxJac                              0.870s    |- 24.29% 

  |- PerfJac                              0.513s    |- 14.31% 

  |- ScdAcc                               0.356s    |- 9.93%  

  |- Solver                               0.275s    |- 7.67%  

  |- Precond                              0.251s    |- 7.02%  

  |- update_dev                           0.244s    |- 6.81%  

  |- SanitizeJac                          0.059s    |- 1.64%  

  |- alignvar                             0.039s    |- 1.08%  

  |- Residual                             0.030s    |- 0.85%  

  |- HeatLoss                             0.006s    |- 0.17%  

|- Logging                                0.023s  |- 0.63%    

|- Output                                 0.015s  |- 0.42%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.070s  1.90%       

|- execution                              0.067s  |- 95.12%   

------------------------------------------------------------

TOTAL                                     3.693s

============================================================



Time steps : 151/157, step size: 16.7285, 19.7238, Newton cycles: 932, linear iterations: 9582

```

#### Load OURS and CMG

* STARS wells: Inj, Prod (deck order, so .smy well index 0 and 1). STARS block history at (1,1,19), (2,1,18), (5,1,13) and (5,1,5).

* 10x1x20 grid, so the .smy block index is (i-1) + (k-1)*10.

```
OURS reached day 2526.0 of 2526

```

### Wells

* Top row: injector BHP and water rate, producer BHP. Bottom row: producer oil, water and gas rates. The wells are shut in until day 60.

![png]({{ "/assets/images/benchmark_image_38.png" | relative_url }})

### Blocks

* One row per block: pressure, temperature, oil saturation, gas saturation.

![png]({{ "/assets/images/benchmark_image_39.png" | relative_url }})

#### 3D live oil

* 20x10x10 SAGD, live oil (CH4 + HOIL) with water. Injector 'Inj' (2:19,1,7) and producer 'Prod' (2:19,1,9); both are shut in and heated by `UHTR`/`TMPSET` for 60 days, then opened. The run ends at the first `*STOP`, day 680.

* Reference is the `stars_stflu024.log` time step summary (one row per step), not a well-history CSV, so both sides are read from the same kind of table: simuapp is run with `-log` to write its own.

* Injection is water only (steam, quality 0.85); the injection oil and gas columns are blank in both logs.

```
Running simulation [simuapp]: SAGD 3D live oil (-novtu)

```

```
OURS reached day 680.0 of 680

  CMG: 124 steps marched, 0 cuts, 289 Newton cycles

 OURS: 125 steps marched, 4 cuts, 513 Newton cycles

```

### Wells

* Rates are m3/day at standard conditions, read from the time step summary. The wells are shut in until day 60, so there is nothing to plot before it.

![png]({{ "/assets/images/benchmark_image_40.png" | relative_url }})

#### *KRTEMTAB verification (stflu028)

* 5x5x1 FIELD grid with five producers and one injector, from the STARS `verify48` verification deck. `*KRTEMTAB` moves the relative permeability endpoints with temperature between 123 F and 500 F. The producers run on `*OPERATE *MAX *STO 30`; the injector is open from day 700 to day 1431. The run ends at day 2435.

* Reference is the CMG `verify48` run: `stars_stflu028.log` (time step summary, field totals in FIELD units) and `stars_stfu028_special.csv` (pressure at blocks (1,2,1) and (2,3,1)). simuapp is run with `-log` so both sides of the rates are the same kind of table.

```
Running simulation [simuapp]: *KRTEMTAB verification (-novtu)

Elapsed: 0.34s

No text to display.

```

```
OURS reached day 2435.0 of 2435

  CMG: 90 steps marched, 0 cuts, 94 Newton cycles

 OURS: 40 steps marched, 0 cuts, 75 Newton cycles

```

### Wells

* Field totals from the time step summary. The CMG log is in bbl/day and ft3/day, ours in m3/day. The injector is open only between days 700 and 1431.

![png]({{ "/assets/images/benchmark_image_41.png" | relative_url }})

### Blocks

* Pressure at the two blocks CMG reports. 5x5x1 grid, so the .smy block index is (i-1) + (j-1)*5: (1,2,1) is 5 and (2,3,1) is 11.

![png]({{ "/assets/images/benchmark_image_42.png" | relative_url }})

#### Temperature dependent relative permeability (stflu029)

* 15x1x15 SI cross-section, injector 'Injector S1' at (1,1,15) and producer 'Producer P1' at (1,1,12). Both are shut in and heated by `UHTR`/`TMPSET` for 150 days, then opened. `*KRTEMTAB *SWR *SORW` moves the connate and critical water and the residual oil between 7 C and 307 C. The run ends at day 820.

* Reference is the DeepFlow THERM `stars_stflu029.log` time step summary (one row per step), not a well-history CSV, so both sides are read from the same kind of table: simuapp is run with `-log` to write its own. Both logs are in m3/day.

* Our log prints the rates with two decimals, so the oil and gas curves are coarse.

```
Running simulation [simuapp]: Temperature dependent relative permeability (-novtu)

Elapsed: 3.10s

No text to display.

```

```
OURS reached day 820.0 of 820

THERM: 506 steps marched, 0 cuts, 659 Newton cycles

 OURS: 224 steps marched, 6 cuts, 799 Newton cycles

```

### Wells

* Rates are m3/day at standard conditions, read from the time step summary. The wells are shut in until day 150, so time is counted from then, on a log axis: most of the change is in the first 50 days after opening, which a linear axis squeezes into a sliver of the run.

* The oil and gas rates fall by one and three decades, so their rate axes are logarithmic too, and a zero rate is not drawn. The Fortran run marches 506 steps against our 218; it is drawn as a thin line with a marker every few steps, so that both series stay visible.

![png]({{ "/assets/images/benchmark_image_43.png" | relative_url }})

#### Wet combustion tube (stflu033)

* 20x1x1 SI tube, 1.75 m long, with six components (water, heavy / medium / light oil, inert gas, oxygen) and three oil-burning reactions (`*STOREAC`, `*STOPROD`, `*RORDER`, `*FREQFAC`, `*EACT`, `*RENTH`): the Smith and Perkins forward wet-combustion experiment. Heaters bring the four blocks at the inlet to 267 C, air is injected from day 2e-4, and water is co-injected with it from day 0.02 (`*INCOMP *WATER-GAS`, `*OPERATE *STF`). The producer holds 5620 kPa at the far end (`*PERF *TUBE-END`). The run ends at day 0.6667.

* Reference is DeepFlow THERM: `stars_stflu033.log` (time step summary) for the production rates and the cost of the run, and `stars_stflu033.prn` for the grid profiles at its report times and for the cumulative balance with its reaction totals. Our profiles come from the VTU series (`*OUTSRF *GRID`; the profiles are all that reads it, so this deck keeps its `.vtu` in `FIELD_PLOT_DECKS`), our balance from the `.out` the run writes.

* Two things are judged separately. The reaction totals are what the kinetics burn, wherever the front is; the profiles say where the heat goes - the hot peak at the front, and the wet plateau behind it where the injected water condenses.

```
Running simulation [simuapp]: Wet combustion tube

Elapsed: 0.78s

No text to display.

```

```
OURS reached day 0.6670 of 0.6667

THERM: 116 steps marched, 0 cuts, 361 Newton cycles

 OURS: 120 steps marched, 2 cuts, 572 Newton cycles

```

### Wells

* Producer rates are m3/day at standard conditions. DeepFlow's come from its time step summary; ours from the `.smy`, which keeps the digits the `.log` rounds away (the oil rate falls to 1e-11).

* The injector holds its target (3.06883 m3/day of water and air, 8.83e-3 of it water), so the producer is the curve to read.

![png]({{ "/assets/images/benchmark_image_44.png" | relative_url }})

### Profiles along the tube

* Temperature, water and oil saturation against distance from the injector, at DeepFlow's report times (the deck's `*TIME` cards), DeepFlow dashed and ours solid in the same colour.

* The tube is one-dimensional: block 1 is at the injector end (`*KDIR *DOWN`). The `.prn` marks a few values with a trailing `i` / `p` (the well blocks); the marker is dropped.

```
DeepFlow report times (days): [1e-05, 0.0002, 0.02, 0.083333, 0.16667, 0.25, 0.66667]

```

![png]({{ "/assets/images/benchmark_image_45.png" | relative_url }})

```
 t (days)   peak T DEEPFLOW (C)  at (m)    peak T OURS (C)  at (m)

    1e-05                    99    0.04                 99    0.04

   0.0002                   261    0.04                262    0.04

     0.02                   341    0.04                341    0.04

  0.08333                   348    0.13                348    0.13

   0.1667                   380    0.22                380    0.22

     0.25                   403    0.31                403    0.31

   0.6667                   477    1.10                472    1.10

```

### Reactions

* What the reactions did by each time, from the cumulative balance both programs print (the `Net Reactions` column): oxygen consumed, oil burnt, water produced and heat released.

* DeepFlow prints it for a handful of steps; the step's time comes from its `.log`. Ours is read from the `.out` at every report.

```
At day 0.6667 (ours: report at day 0.6667)

                     DEEPFLOW         OURS  difference

 Oxygen consumed        17.52        17.51       -0.0%  gmol

       Oil burnt       0.5619       0.5615       -0.1%  gmol

  Water produced        11.53        11.52       -0.0%  gmol

   Heat released    7.346e+06    7.343e+06       -0.0%  J

```

![png]({{ "/assets/images/benchmark_image_46.png" | relative_url }})

### Step size

* Steps are compared on simulated time, as for the other decks. The first run is the reference.

```
run                THERM     OURS

steps                116      120

newton               361      572

newton/step        3.112    4.767

cuts                   0        2

dt min           8.8e-06 7.24e-06

dt geomean      0.002991 0.002858

dt max             0.017   0.0164

end day           0.6667    0.667

steps@0.000667d       13       14

steps@0.00667d        17       18

steps@0.0667d         36       37

steps@0.333d          79       81

steps@0.667d         116      119

```

![png]({{ "/assets/images/benchmark_image_47.png" | relative_url }})

#### Foamy oil primary production (sttst66)

* 12x12x7 SI block with one horizontal producer (`*WELL 1 'PRODN' *FRAC 0.25`, `*GEOMETRY *J`, six perforated layers) on a 250 kPa bottom-hole limit and no injection. Four components: water, dead oil, and two gases (`FM_GAS`, `GAS`) that stay in the gas phase through a constant K value. The `*STOREAC` reaction turns dissolved-gas-like `FM_GAS` into free `GAS` (the foamy-oil lamella drainage), and the run lasts two years.

* Reference is DeepFlow THERM: `stars_sttst66.log`. Its step table prints only the oil rate for this deck (no gas or water is produced in the first two years), so that is the comparison; the producer's bottom-hole pressure is held at its limit.

* Two modelling details decide the first step. `*WELL *FRAC` scales the well index only, while a `*GEOMETRY` `ff` also changes the equivalent radius; and a deck without `*PRPOR` takes the reference pressure of the porosity from `*PRSR`, which is what makes the initial oil in place equal DeepFlow's.

```
Running simulation [simuapp]: Foamy oil primary production (-novtu)

Elapsed: 1.47s

No text to display.

```

```
OURS reached day 730.0 of 730.0

oil rate against DeepFlow: mean |error| 0.93%, max 1.42%

   day   DEEPFLOW       OURS    error

     1     42.140     42.143    0.01%

    30     36.550     36.498   -0.14%

    90     31.190     31.001   -0.61%

   180     26.890     26.590   -1.12%

   365     22.400     22.103   -1.33%

   730     18.460     18.197   -1.42%

THERM: 35 steps marched, 0 cuts, 35 Newton cycles

 OURS: 38 steps marched, 0 cuts, 74 Newton cycles

```

![png]({{ "/assets/images/benchmark_image_48.png" | relative_url }})

```
run          THERM  OURS

steps           35    38

newton          35    74

newton/step      1 1.947

cuts             0     0

dt min           1     1

dt geomean   15.73  13.9

dt max          30 30.24

end day        730   730

steps@0.73d      0     0

steps@7.3d       3     3

steps@73d       10    10

steps@365d      22    25

steps@730d      35    38

```

![png]({{ "/assets/images/benchmark_image_49.png" | relative_url }})

#### Rock-fluid interpolation on a component (stsmo097)

* 240x1x1 SI core (0.5 mm blocks, 0.12 m long) with water, a second aqueous component `CHEM` and dead oil. `*INTCOMP 'CHEM' *WATER` interpolates the rock-fluid curves on the mole fraction of `CHEM` in the water phase, between two `*KRINTRP` sets (`*DTRAPW` / `*DTRAPN` 0 and 0.1). The injector holds 1.44e-4 m3/day of water that carries 5% `CHEM` (`*INCOMP *WATER 0.95 0.05 0.0`), so the fraction is 0.05 everywhere: halfway between the sets, `ratw = ratn = 0.5`. The producer holds 1.44e-4 m3/day of liquid. The run ends at day 5.

* The sets differ in the residual oil (`Sorw` 0.3 against 0) and in `Krwiro` (1.0 against 0.8). The interpolated curves have `Sorw` = 0.15, which is why the swept core settles at Sw = 0.85: set 1 alone stops at 0.70 and set 2 alone at 1.0. That is the endpoints being interpolated, not only the relative permeabilities read at fixed endpoints.

* Reference is DeepFlow THERM: `stars_stsmo097.log` (time step summary) for the production rates and the cost of the run, and `stars_stsmo097.prn` for the pressure and water saturation profiles at its report times and for the cumulative balance. Our profiles come from the VTU series (`*OUTSRF *GRID`), so this deck keeps its `.vtu` in `FIELD_PLOT_DECKS`.

* The deck carries `*CONVERGE ... *WELRES 1.0E-4`. A limit counts as broken only beyond that relative excess (1e-3 by default), and with the default our producer, which starts on its minimum BHP, stays there while up to 0.09% over its STL limit, where DeepFlow switches to STL at the first excess. The profiles section shows what that costs: 21 kPa of pressure level.

```
Running simulation [simuapp]: Rock-fluid interpolation on a component

Elapsed: 1.12s

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

![png]({{ "/assets/images/benchmark_image_50.png" | relative_url }})

### Profiles along the core

* Water saturation and pressure against distance from the injector. The `.prn` holds the grid at every step DeepFlow marched; the first figure draws eight of those times (the early pressure build-up, the front, breakthrough and the long tail), DeepFlow dashed and ours solid in the same colour. The two programs march different steps, so ours is interpolated in time between the two frames around DeepFlow's time (every `*TIME` card is a frame of both). The second figure compares every time DeepFlow wrote.

* The core is one-dimensional along I, block 1 at the injector. The `.prn` marks a few values with a trailing `i` / `p` (the well blocks); the marker is dropped. DeepFlow's water molar fraction is `WATER` 0.950 / `CHEM` 0.050 in every block at every time, so both programs interpolate at the same fraction throughout.

* Read the saturation first: the plateau at 0.85 is the interpolated residual oil, and the fall towards the producer is the capillary end effect. The mean gap stays below 0.005 over the whole run. The largest single-block gaps (up to 0.05) are at the tip of the advancing front, where one block of position is the difference, and at day 2.139, where it is DeepFlow's own profile that has a one-block dip (block 36 at 0.802 between 0.846 and 0.840).

* The pressure agrees to within 1.5 kPa in shape and 0.5 kPa in level at every time. The level is what the deck's `*WELRES 1.0E-4` buys; the second figure marks DeepFlow's switch. The producer starts on its minimum BHP (7000 kPa) and DeepFlow switches it to its STL limit at day 0.002725, the first time the rate there exceeds 1.44e-4 m3/day (its `.prn`: "Max STL constraint violated"). A limit counts as broken in Catfish only beyond the well residual tolerance (`*CONVERGE *WELRES`, 1e-3 by default; a MAX limit is met while the rate is within `(1 + tol)` of it), so with the default the producer stays on the BHP limit until day 0.0255, up to 0.09% over its STL. That extra 1.6e-9 m3 withdrawn, against a total compressibility times pore volume of 7.8e-11 m3/kPa, is 21 kPa less pressure for the rest of the run: with the injector and the producer then holding the same rates nothing brings it back. With `*WELRES 1.0E-4` the producer switches at day 0.0030 and the gap is the 0.4 kPa that is there from the first step.

```
DeepFlow writes the grid at 45 times, from day 0.0001 to day 5

```

![png]({{ "/assets/images/benchmark_image_51.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_52.png" | relative_url }})

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

![png]({{ "/assets/images/benchmark_image_53.png" | relative_url }})

#### Imbibition capillary pressure tables (stsmo088)

* The same 240x1x1 core, fluids, wells and `*INTCOMP 'CHEM' *WATER` between two `*KRINTRP` sets as stsmo097 above (STARS option No. 88: "Verify/Illustrate `*CP_IMBIB` and `*PCOW_CRV` for Interpolation of Imbibition Capillary Pressure Curves"). The difference is in the tables: the `Pcow` column gives only its end values (1.0 at Sw 0.2, then -0.5 at Sw 0.7 in set 1 and -1 at Sw 1.0 in set 2) and writes the rows between them as `int`, linear in Sw. Catfish does not read `int`, so the deck has those rows written out; the numbers are the ones stsmo097 lists. The `Krow` columns are different from stsmo097's, and DeepFlow warns that `Kro` is above zero at `So = 0` for both sets.

* `*INTERP_ENDS`, `*CP_IMBIB` and `*PCOW_CRV` are named only in the deck's overview comments, not given as keywords, so this runs the default interpolation of stsmo097. The special history requests (`outsrf special blockvar` for `w`, `sw`, `krw`, `kro`, `pcow`) are commented out: Catfish writes no relperm or `Pcow` history.

* The deck carries `*CONVERGE ... *WELRES 1.0E-4` for the reason given for stsmo097: with the default, our producer stays on its BHP limit while above its STL where DeepFlow switches at the first excess.

* Reference is the DeepFlow THERM time step summary `stars_stsmo088.log`: the production rates, the injection rate, the water cut and the cost of the run. The run ends at day 2.5; the oil is gone by day 0.81.

```
Running simulation [simuapp]: Imbibition capillary pressure tables (-novtu)

Elapsed: 5.08s

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

![png]({{ "/assets/images/benchmark_image_54.png" | relative_url }})

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

![png]({{ "/assets/images/benchmark_image_55.png" | relative_url }})

#### Nonlinear viscosity mixing (stsmo051)

* 80x1x1 SI tube (25 m blocks) of water at its connate saturation and an oil of three components, `C10_OIL`, `C4_OIL` and `C1_OIL` (`*AVISC` 10, 0.2 and 0.05 cp). The injector holds 3.17e4 m3/day of oil at the surface (`*INCOMP *OIL 0 0 .23 .77`, `*OPERATE *STO`), lighter than the oil in place; the producer sits on its minimum BHP. The run ends at the `*STOP` of day 545.

* `*VSMIXCOMP 'C4_OIL'` with `*VSMIXENDP 0 0.6` and a curved `*VSMIXFUNC` replaces C4's mole fraction in the log mixing rule by f(x_C4), and the other components share what is left (`../doc/viscosity.md`, Nonlinear Viscosity Mixing). x_C4 in the oil runs from 0.127 (the oil in place) to 0.23 (the injected oil), inside the table.

* The deck is the STARS template stsmo051 modified so that this mixing is the only thing Catfish did not have: the changes are listed in its header (plain SI instead of bar, distinct oil viscosities, constant K values, oil injection on STO). Reference is a DeepFlow THERM run of the same file: `stars_stsmo051.log` (time step summary) and `stars_stsmo051.prn` (well tables, pressure and oil composition profiles at each of its 18 steps).

* A second run of the same deck with the three `*VSMIX` lines commented out shows what the mixing rule is worth: with linear mixing the oil is about 15% more viscous at the initial composition.

```
Running simulation [simuapp]: Nonlinear viscosity mixing

Elapsed: 0.34s

No text to display.

Running simulation [simuapp]: Linear viscosity mixing (stsmo051 without *VSMIX) (-novtu)

Elapsed: 0.31s

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

![png]({{ "/assets/images/benchmark_image_56.png" | relative_url }})

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

![png]({{ "/assets/images/benchmark_image_57.png" | relative_url }})

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

![png]({{ "/assets/images/benchmark_image_58.png" | relative_url }})

#### Caustic-polymer slugs in a laboratory core (stdrm006)

* 19x1x1 SI core (4 mm blocks, 0.076 m long, 150 md, porosity 0.164) at Sw 0.64 with a dead oil; components `WATER`, `POLYMER`, `NAOH` and `DEAD OIL`. The injector holds 2.46e-5 m3/day of water (one pore volume is 0.25 day) that carries a sequence of slugs: NaOH 0.005 with polymer to day 0.0625, then polymer alone at 20, 10 and 5 cp (day 0.0625, 0.125, 0.1875), then pure water from day 0.25. The producer holds 101.3 kPa. The run ends at the `*STOP` of day 0.75.

* Three mechanisms are in play. `*ADSCOMP` / `*ADSLANG` / `*ADMAXT` adsorb NaOH reversibly and polymer irreversibly (`*ADRT`), and `*RRFT` 1.2 is the polymer's residual resistance (`../doc/adsorption.md`). `*IFTTABLE` with `*INTLOG` gives the interfacial tension from the NaOH mole fraction in the water (13 dyne/cm without NaOH, 0.005 at its minimum), and the capillary number interpolates the rock-fluid curves between the two `*KRINTRP` sets (`*DTRAPW` -4.5 and -3, `../doc/rock-fluid.md`). `*VSMIXCOMP 'POLYMER'` mixes the polymer viscosity nonlinearly.

* Reference is DeepFlow THERM: `stars_stdrm006.log` (time step summary) and `stars_stdrm006.prn`, which holds a well table at each of its 45 steps, the grid at every `*TIME` card and the cumulative balance. Our profiles come from the VTU series, so this deck is in `FIELD_PLOT_DECKS`.

* The deck has `*WSRF *GRID *TIME`, so our `.smy` and VTU hold the `*TIME` cards only (seven rows, 0 to 0.75 day), where DeepFlow's well tables cover every step. Curves of ours below therefore have six points; the tables compare both at the `*TIME` cards.

```
Running simulation [simuapp]: Caustic-polymer slugs in a laboratory core

Elapsed: 0.39s

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

![png]({{ "/assets/images/benchmark_image_59.png" | relative_url }})

### Profiles along the core

* Water saturation, pressure and the adsorbed NaOH and polymer against distance from the injector, at the `*TIME` cards 0.0625 to 0.75 day (the times both programs wrote the grid), DeepFlow dashed and ours solid in the same colour. DeepFlow's come from the `.prn`, which prints the saturation to three digits and the pressure to 1 kPa, and lists the adsorption of each component under its own `Component =` line; ours from the VTU series.

* The adsorption is what the new keywords decide, and it agrees: the NaOH front (68 gmol/m3 is `*ADMAXT`) is within 4.5% of `*ADMAXT` at every time, and the polymer within 1.3% except at day 0.1875, where the front sits a block away (6.2%). The pressure is within 1.6 kPa, which is about one digit of the `.prn`.

* The saturation is the loose one: behind the NaOH front it ripples in both programs. The mean gap over the core is 0.007 at day 0.0625, 0.046 at day 0.125 and below 0.025 after; the largest single block is 0.19, at day 0.125.

![png]({{ "/assets/images/benchmark_image_60.png" | relative_url }})

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

![png]({{ "/assets/images/benchmark_image_61.png" | relative_url }})

#### Steam foam in a radial cross-section (stdrm010)

* 9x1x3 radial sector (`*RW 0`, rings of 2 to 14 m out to a 500 m outer ring, 60 degrees, 15 m layers, porosity 0.35) of a 1000 md bed with a 1e4 md higher-permeability path (all rings of the top layer, and rings 1 and 6 of the other two). The bed holds water at 0.15 (0.5 in the path) and a bitumen of three million cp at 10 C and 2.9 cp at 316 C (`*VISCTABLE`), at 15.5 C. Components `WATER`, `SURFACT` and `BITUMEN`.

* The injector (`*FRAC` 1/6) holds 150 m3/day of steam at 210 C, quality 0.7, in the bottom layer: 25 m3/day for the sector. The producer (`*FRAC` 0.5) holds 30 m3/day of liquid (`*STL`), 15 for the sector, in the same layer. From day 730 the steam carries surfactant (1.875e-4 mole fraction in the water, 1 wt%). The run ends at the `*STOP` of day 1460; the `*TIME` cards are 365, 730 and 1095.

* The foam is the empirical scheme of `../doc/rock-fluid.md` (Option 3): `*INTCOMP 'SURFACT' *WATER` with `*INTLIN` interpolates the rock-fluid curves on the surfactant mole fraction between three `*KRINTRP` sets (no foam, weak foam with a mobility reduction of 2.5 at `*DTRAPW` 0.4, strong foam with 50 at 0.02, which differ in `*KRGCW`), and `*FMSURF`, `*FMCAP`, `*FMOIL` and `*FMMOB` set where the foam acts. The surfactant adsorbs reversibly (`*ADSCOMP`, `*ADSLANG` at three temperatures, `../doc/adsorption.md`).

* Reference is DeepFlow THERM: `stars_stdrm010.log` (time step summary) and `stars_stdrm010.prn`, which holds a well table at each of its 94 steps, the grid at day 0.1 and at every `*TIME` card, and the cumulative balance. DeepFlow ran the template's default `*KDIR *UP` (K = 1 at the bottom); the deck here is the same model with K reversed and `*KDIR *DOWN`, which Catfish needs, so layer K of ours is layer 4 - K of DeepFlow's and the profile cells turn the `.prn` over. Our profiles come from the VTU series (a frame per step), so this deck is in `FIELD_PLOT_DECKS`.

```
Running simulation [simuapp]: Steam foam in a radial cross-section

Elapsed: 0.74s

No text to display.

```

```
OURS reached day 1460 of 1460

THERM: 94 steps marched, 3 cuts, 198 Newton cycles

 OURS: 86 steps marched, 6 cuts, 359 Newton cycles

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

1095        6.2905    5.8398              58.054          61.068             1801.6         1613.1            4175.8        3969.3

1460        7.6799     6.255              48.801          58.304             1944.6         1822.1            3987.1        3808.3

```

![png]({{ "/assets/images/benchmark_image_62.png" | relative_url }})

### Profiles along the radius

* Temperature, pressure, gas saturation and adsorbed surfactant against radius, one column per layer, at the `*TIME` cards 365 to 1460 (the surfactant starts at 730, so the adsorption is zero before then), DeepFlow dashed and ours solid in the same colour. DeepFlow's come from the `.prn` (temperature and pressure to the integer, saturation to three digits; the adsorption listed under `Component = SURFACT`), ours from the VTU frame of the step that ends at each card.

* The top layer agrees: over the four times the mean gap is 2.3 C, 73 kPa and 0.048 in Sg. The middle and bottom layers do not: 23 to 24 C, 230 to 310 kPa and 0.044 to 0.073, and the largest single blocks (98 to 176 C, 0.27 to 0.52 in Sg, up to 1100 kPa) are in them inside the first 50 m, where the steam front is. The two largest are the middle layer at 6 m at days 365 and 730 (day 365: 62 C in DeepFlow, 192 C in ours) and the bottom layer at 31 to 42 m at days 1095 and 1460.

* Over the whole grid the mean gap is 12 C at day 365, 19 C at days 730 and 1095 and 14 C at day 1460; the pressure 190, 210, 285 and 120 kPa; Sg 0.037, 0.037, 0.061 and 0.085. The surfactant adsorbed is within a mean of 0.18 gmol/m3 (7% of the 2.56 `*ADMAXT`), with the largest block, 1.1 gmol/m3, in the bottom layer at 42 m at day 1095.

![png]({{ "/assets/images/benchmark_image_63.png" | relative_url }})

```
 day  mean |dT C|  max |dT C|  mean |dP kPa|  max |dP kPa|  mean |dSg|  max |dSg|  mean |dAds|  max |dAds|

 365        9.955       130.9          151.9          1078     0.03805     0.2864            0           0

 730        9.721       178.2          147.5         999.4     0.02924     0.2907            0           0

1095         6.79       51.85          201.9           311     0.02653     0.2012      0.06834      0.5693

1460        8.468       79.94          140.6         282.5     0.05981     0.2837       0.0838       0.865

```

### Material balance

* The cumulative balance both programs print at the end of the run, in gmol (energy in J): the initial total, what was injected minus produced, and the error each program's own books show. DeepFlow's table carries a `Net Reactions` column that ours shares; the deck's surfactant degradation (`*STOREAC`, `*EACT`) consumes 1.16e5 gmol of surfactant in DeepFlow and 1.26e5 in ours.

* The initial totals differ by 0.10% in water and 0.04% in energy; the bitumen agrees to 0.002%. Net water injected minus produced is 2.4% higher in ours and net energy 0.8% higher; the bitumen produced is 6.7% higher (1.239e7 against 1.162e7 gmol), which is the same bias as the oil rate before day 1095. What is in the core at the end agrees to 0.2% for water and 0.06% for energy. The surfactant left in the core is 14% lower in ours (5.05e4 against 5.90e4 gmol). The balance error is within 0.04% for ours and up to 0.11% for DeepFlow.

```
          initial DEEPFLOW  initial OURS   net DEEPFLOW     net OURS  diff %  current diff %   balance error % DEEPFLOW / OURS

   WATER      3.814269e+10  3.818231e+10   1.124654e+09 1.135292e+09    0.95            0.16          -0.0147 / 0.0000

 SURFACT      0.000000e+00  0.000000e+00   1.810711e+05 1.821703e+05    0.61            5.93          -0.1113 / -0.0004

 BITUMEN      3.916811e+09  3.916889e+09  -1.161615e+07 -1.180416e+07    1.62           -0.00           0.0011 / 0.0020

  Energy      6.199378e+14  6.201891e+14   6.811423e+13 6.909408e+13    1.44            0.16          -0.0516 / -0.0012

```

### Step size

* Steps are compared on simulated time, as for the other decks. The first run is the reference. Both programs are forced to the `*TIME` cards (365, 730, 1095, and the `*STOP` at 1460 days). DeepFlow marches 94 steps with 3 cuts and 198 Newton cycles, ours 93 steps with 11 cuts and 392: twice the Newton cycles per step.

```
run              THERM   OURS

steps               94     86

newton             198    359

newton/step      2.106  4.174

cuts                 3      6

dt min             0.1 0.0798

dt geomean       5.384  5.592

dt max           79.08    100

end day           1460   1460

steps@1.46d         10     11

steps@14.6d         16     17

steps@146d          25     26

steps@730d          42     48

steps@1.46e+03d     94     86

```

![png]({{ "/assets/images/benchmark_image_64.png" | relative_url }})

#### Foam with a horizontal well in a thin oil zone (stdrm016)

* 2x5x9 Cartesian block of the Troll field idealisation: a 500 m horizontal well along I (`*DI` 100 and 400 m), five rows across it (2280.5, 175, 83, 175 and 2280.5 m; the well is in the 83 m row), nine layers of 32, 8, 6, 4, 4, 2, 4, 14 and 85 m below a top at 1523 m (`*DTOP`), porosity 0.25, 8100 md along I and J and 4455 md vertically. The reservoir is at 67 C and 16025.7 kPa at 1547 m: a gas cap above the gas-oil contact at 1547 m, a thin oil zone, and bottom water below the water-oil contact at 1567 m, initialised by `*VERTICAL *DEPTH_AVE`. Components `WATER`, `OIL`, `SURFACT`, `PROP` (propane) and `CH4`. The deck has no `*INUNIT`, so it is SI.

* One horizontal well is modelled as two wells in the same blocks (1:2, 3, 6; `*GEOMETRY *I`, radius 0.108 m), both in layer 6, which lies below the water-oil contact: a producer (`*STL` 5000 m3/day, minimum BHP 1500 kPa) and an injector (`*MOBWEIGHT`, an oil-phase stream, at most 5000 m3/day at standard conditions and 16500 kPa BHP). The producer runs from day 0 to 90. From day 90 the injector puts in propane with 4.2e-3 mole fraction of surfactant, and pure propane from day 135. At day 180 the injector shuts and the producer opens again, to the end at day 365.

* The foam is the empirical scheme of `../doc/rock-fluid.md` (Option 3) on the surfactant in the oil phase: `*INTCOMP 'SURFACT' *OIL` with an `*IFTTABLE` of 13 dyne/cm interpolates the rock-fluid curves between two `*KRINTRP` sets (no foam, and strong foam at `*DTRAPW` 0.0333 with `*KRGCW` overridden to 0.029), and `*FMMOB` 30, `*FMSURF` 4.2e-4, `*FMCAP` 2e-4 and `*FMGCP` 1e-6 with the exponents `*EPSURF` 1, `*EPCAP` 1 and `*EPGCP` 2 set where it acts. The template's second rock type (`*RPT 2`, the wellbore) is defined but `*KRTYPE CON 1` leaves it unused. The surfactant adsorbs reversibly (`*ADSCOMP`, `*ADSLANG` at 85 and 121 C).

* Reference is DeepFlow THERM: `stars_stdrm016.log` (time step summary, 56 steps) and `stars_stdrm016.prn`, which holds the initial volumes and grid, a well table at ten of its steps (days 0.1, 32.7, 90, 91.2, 118.4, 135, 180, 182.9, 276 and 365) and the cumulative balance. DeepFlow ran this deck as it stands (`*KDIR *DOWN`). The deck is in `FIELD_PLOT_DECKS`: its VTU frame 0 gives our initial layers.

```
Running simulation [simuapp]: Foam with a horizontal well in a thin oil zone

Elapsed: 0.80s

No text to display.

```

```
OURS reached day 365 of 365

THERM: 56 steps marched, 1 cuts, 145 Newton cycles, material balance error 0.037 % at the last step

 OURS: 54 steps marched, 1 cuts, 209 Newton cycles, material balance error 0.227 % at the last step

```

### Initial state

* DeepFlow's in-place volumes and its grid at the start of the run against ours (the initial state is uniform along I and J, so one column is compared; ours is VTU frame 0). The volumes agree to 0.003%: pore 9.9308e7 against 9.9306e7 m3, water 7.3646e7 against 7.3644e7, oil 1.1669e7 and gas 1.3993e7 in both. `read_prn_layers` is the one of the stdrm010 profile cell.

* The saturations agree layer by layer. `*VERTICAL *DEPTH_AVE` averages a block over its thickness, as STARS does: the gas-oil contact at 1547 m cuts layer 1 (1523 to 1555 m), so a block holds 0.701 gas in DeepFlow and 0.7005 in ours, and the water-oil contact at 1567 m cuts layer 3 (1563 to 1569 m), where Sw is 0.377 in both. Below it DeepFlow prints 1.000 and ours holds 0.9999, the `*WOC_SW` default.

* The pressure is 0.4 kPa lower in ours in layer 1 and 3.8 kPa in layer 2, then 22 to 24 kPa in layers 3 to 9: the gap opens across the oil zone, between layers 2 and 3, and stays in the water leg.

```
    m3     DEEPFLOW         OURS   diff %

  pore  9.93080e+07  9.93080e+07    0.000

 water  7.36460e+07  7.36460e+07    0.000

   oil  1.16690e+07  1.16690e+07    0.000

   gas  1.39930e+07  1.39930e+07    0.000

```

```
 layer  Sw DEEPFLOW  Sw OURS  So DEEPFLOW  So OURS  Sg DEEPFLOW  Sg OURS  P DEEPFLOW    P OURS

     1        0.066    0.066        0.233   0.2335        0.701   0.7005   1.602e+04 1.602e+04

     2        0.066    0.066        0.934    0.934            0        0   1.612e+04 1.612e+04

     3        0.377   0.3773        0.623   0.6227            0        0   1.618e+04 1.618e+04

     4            1   0.9999            0   0.0001            0        0   1.623e+04 1.623e+04

     5            1   0.9999            0   0.0001            0        0   1.627e+04 1.627e+04

     6            1   0.9999            0   0.0001            0        0    1.63e+04  1.63e+04

     7            1   0.9999            0   0.0001            0        0   1.632e+04 1.632e+04

     8            1   0.9999            0   0.0001            0        0   1.641e+04 1.641e+04

     9            1   0.9999            0   0.0001            0        0   1.689e+04 1.689e+04

```

### Wells

* Rates are m3/day at standard conditions. DeepFlow's field rates come from its time step summary (one row per step; it prints no rate per well), its bottom-hole pressures from the well tables of the `.prn` at ten steps; ours come from the `.smy`, which names the wells by the order of their cards, `31216-prod` first and `31216-inj` second. Our bottom-hole pressure is drawn only while the well flows, since the `.smy` keeps a shut well's last value. The first table compares the pressures and the oil rates of the flowing well at the days of the `.prn`'s tables, the second the field rates at days from the schedule.

* The producer's drawdown agrees (24.03 against 24.04 kPa in the first step) but the pressure level does not: its bottom-hole pressure is 181, 124 and 128 kPa higher in ours at days 0.1, 32.7 and 90. In the first step ours raises the pressure of every block, by 160 to 189 kPa (VTU frames 0 and 1), while DeepFlow's largest change is -35 kPa. The moles in place are not the same either (see the balance below: methane 3.3% higher in ours, oil 0.6% lower), which is where to look.

* The injector does not reach its rate. DeepFlow injects its 5000 m3/day limit at a bottom-hole pressure 23 to 34 kPa above the block (15912 to 16150 kPa); ours sits on the 16500 kPa limit with a drawdown of about 520 kPa at the start of injection and injects 1010, 758 and 733 m3/day at days 91.2, 118.4 and 135. The surfactant and propane put in are a fraction of DeepFlow's (the balance below), and the foam that follows is made from far less. Why is open; an oil-phase stream injected into blocks that hold water, under `*MOBWEIGHT`, is the first thing to check.

* After day 180 DeepFlow breaks gas through at day 192.7 (oil 986 and gas 2687 m3/day, water down from 5000 to 4014) and its oil peaks at 2286 m3/day at day 199.7; ours makes 0.03 m3/day of oil at day 200 and 180 at day 250 (DeepFlow 1232). Ours then peaks at 1361 m3/day at day 275 against DeepFlow's 1164 at day 276, is 28% below at day 300 (694 against 968), and at day 365 is 72% below in oil (386 against 1365), 75% in gas (2.5e4 against 1e5) and 27% above in water (4614 against 3635).

```
producer 31216-prod, injector 31216-inj

   day       well  BHP DEEPFLOW  BHP OURS  oil DEEPFLOW  oil OURS  BHP gap kPa

   0.1 31216-prod         16236     16473             0         0       237.38

32.732 31216-prod         16057     16201             0         0       144.06

    90 31216-prod         15794     15957             0         0       163.44

91.199  31216-inj         15912     16054          5000      5000       142.29

118.38  31216-inj         16124     16264          5000      5000       139.67

   135  31216-inj         16150     16293          5000      5000       143.41

182.88 31216-prod         16018     16157        0.6802   0.38391       139.25

275.98 31216-prod         15517     15658          1164    1091.5       140.97

   365 31216-prod         15124     15262          1365    1228.9       137.73

  day  oil DEEPFLOW  oil OURS  gas DEEPFLOW  gas OURS  water DEEPFLOW  water OURS  injected DEEPFLOW  injected OURS

   90             0         0             0         0            5000        5000                  0              0

 91.2             0         0             0         0               0           0               5000           5000

  135             0         0             0         0               0           0               5000           5000

180.5         1.228    0.6634             0 2.572e-07            4999        4999                  0              0

  200          2286      1948      1.52e+04 1.347e+04            2712        3052                  0              0

  250          1232      1299      3.47e+04 4.331e+04            3768        3701                  0              0

  300         967.6     933.7      5.53e+04 5.345e+04            4032        4066                  0              0

  365          1365      1229         1e+05 1.033e+05            3635        3771                  0              0

```

![png]({{ "/assets/images/benchmark_image_65.png" | relative_url }})

### Material balance

* The cumulative balance both programs print at the end of the run, in gmol (energy in J): the initial total, what was injected minus produced, and the error each program's own books show. DeepFlow's table has a `Net Reactions` column (zero here) and a `Net Adsorbed` one that ours leaves out.

* The initial totals differ although the volumes agree: water by -0.002%, oil by -0.64%, methane by +3.3% and energy by 0.10%. More methane in the same gas volume is a denser gas, which may be why the first step raises the pressure. Net propane injected is 87% lower in ours (1.43e8 against 1.08e9 gmol) and net surfactant 82% lower (1.59e6 against 8.72e6, which counts what adsorbs); net water produced is 11% higher and net methane produced 55% lower. The balance error is within 0.005% for ours except propane (0.073%), and within 0.037% for DeepFlow.

```
          initial DEEPFLOW  initial OURS   net DEEPFLOW     net OURS  diff %  current diff %   balance error % DEEPFLOW / OURS

   WATER      4.038058e+12  4.038125e+12  -6.458771e+10 -6.471529e+10    0.20           -0.04           0.0185 / -0.0000

     OIL      4.675358e+10  4.645702e+10  -3.174383e+08 -3.291916e+08    3.70           -0.67           0.0008 / -0.0068

 SURFACT      0.000000e+00  0.000000e+00   8.717758e+06 8.757514e+06    0.46            2.32          -0.0372 / -0.0184

    PROP      0.000000e+00  0.000000e+00   1.077342e+09 1.139730e+09    5.79            6.02           0.0050 / 0.2265

     CH4      1.172394e+11  1.211576e+11  -3.760746e+08 -4.161894e+08   10.67            3.32           0.0060 / 0.0138

  Energy     -1.643721e+15 -1.643933e+15   3.056696e+11 2.286294e+11  -25.20            0.02          -0.0000 / -0.0007

```

### Step size

* Steps are compared on simulated time, as for the other decks. The first run is the reference. Both programs are forced to the `*TIME` cards (90, 135 and 180 days) and the end at 365. DeepFlow marches 56 steps with 1 cut and 145 Newton cycles, ours 59 steps with 3 cuts and 259 (4.4 cycles per step against 2.6).

```
run           THERM  OURS

steps            56    54

newton          145   209

newton/step   2.589  3.87

cuts              1     1

dt min         0.02  0.02

dt geomean    2.706 2.693

dt max        33.59 24.96

end day         365   365

steps@0.365d      2     2

steps@3.65d       4     5

steps@36.5d      10    10

steps@182d       39    40

steps@365d       56    54

```

![png]({{ "/assets/images/benchmark_image_66.png" | relative_url }})

#### ES-SAGD with solvent, 2D live oil (stflu023)

* 30x1x32 Cartesian cross-section (144 m wide, 100 m thick slice, 1 m layers; porosity 0.2965, 4264 md horizontally and 852 md vertically) at 10 C. The oil is 97% `BITUMEN` with 2% `CH4` and 1% `C6H14` (3.8 million cp at 5 C), at a saturation of 0.79 with water at 0.21. Components `WATER`, `BITUMEN`, `CH4` and `C6H14`.

* A SAGD pair in the middle column: the injector `INJ-L` in layer 25 and the producer `PRD-L` in layer 30, 5 m below it. Both are shut in until day 90 (`DATE 2005 4 1`) while `*UHTR` / `*TMPSET` heat their blocks to 185 C. They then open: the injector with steam of quality 0.8 at 205 C and 2% `C6H14` (`*INCOMP *WATER-OIL`) on a 2500 kPa BHP limit, the producer on 1000 kPa. The deck is a `*GASTRAP` test with the keyword commented out. The run ends at the last `DATE`, 2013 April 1 (day 3012).

* Reference is DeepFlow THERM: `stars_stflu023.log` (time step summary, 463 steps) and `stars_stflu023.prn`, which holds the final cumulative balance and a well table at ten of its steps. The deck writes no grid to the `.prn`, so there are no profiles to compare, only the wells, the balance and the cost.

* The last `DATE` converts to 3011.958 days here, an hour short of 3012: the deck's dates go through local time, so the run depends on the machine's time zone (with `TZ=UTC` it ends at 3012 in 521 steps, not 511).

```
Running simulation [simuapp]: ES-SAGD with solvent, 2D live oil (-novtu)

Elapsed: 77.55s

No text to display.

```

```
OURS reached day 3012.0 of 3012

THERM: 463 steps marched, 14 cuts, 2268 Newton cycles

 OURS: 521 steps marched, 43 cuts, 3393 Newton cycles

```

### Wells

* Producer rates and the injected water, m3/day at standard conditions, one point per step in both programs: DeepFlow's from its time step summary (four digits), ours from the `.smy`. The time axis is logarithmic from day 80, since the wells open at day 90 and the first months carry the transient, and so is the gas axis. Both wells sit on their BHP limits in both programs from the day they open (injector 2500 kPa, producer 1000 kPa), so the rates are the result.

* The opening at day 90 is the sharpest event: the oil rate peaks at 444 m3/day in DeepFlow and 486 in ours, the gas at 3107 and 2233. After the first months the oil and water rates follow each other: the mean absolute gap to DeepFlow's steps is 5.5% in oil and 0.8% in water over days 200 to 1095, and 3.7% and 0.5% from day 1095 on. The gas rate is the loose one (25% and 18%): it is the smallest and burstiest rate, tens of m3/day after day 200.

* At the end of the run the oil rate is 44.4 m3/day in DeepFlow and 45.0 in ours, the water 2113 and 2122, the injected water 2111 and 2120 (ours at day 3011.96).

```
     rate  mean |gap| % day 90-200  mean |gap| % day 200-1095  mean |gap| % day 1095-3012

      oil                      9.2                        1.9                         0.7

      gas                     31.6                       11.4                         5.2

    water                      6.2                        0.7                         0.5

inj_water                      3.1                        0.7                         0.5

```

![png]({{ "/assets/images/benchmark_image_67.png" | relative_url }})

### Material balance

* The cumulative balance both programs print at the end of the run, in gmol (energy in J): the initial total, what was injected minus produced, and the error each program's own books show. The initial totals agree to 0.002% except the energy (-7.48e13 against -4.89e13 J), so the energy is read from what was injected minus produced.

* The net water injected is 1.7% higher in ours and the bitumen produced 0.3% lower; the `CH4` produced is 0.4% higher and the `C6H14` 5.3% higher; the net energy is 3.4% lower. The balance error is how far each program's own books are from closing: ours is within 0.03% for water, bitumen and energy but 0.26% for `CH4` and 3.5% for `C6H14`, against DeepFlow's 0.16% and 0.05%.

```
          initial DEEPFLOW  initial OURS   net DEEPFLOW     net OURS  diff %   balance error % DEEPFLOW / OURS

   WATER      1.575167e+09  1.575276e+09   1.504974e+08 1.487932e+08   -1.13          -0.0668 / -0.0004

 BITUMEN      1.768460e+08  1.768589e+08  -1.439350e+08 -1.440067e+08    0.05           0.0260 / -0.0354

     CH4      3.646309e+06  3.646575e+06  -3.619410e+06 -3.650587e+06    0.86          -0.1566 / 0.4890

   C6H14      1.823154e+06  1.823288e+06  -1.241833e+06 -1.277253e+06    2.85           0.0546 / 1.5512

  Energy     -7.479612e+13 -4.890307e+13   3.895656e+14 3.775561e+14   -3.08          -0.0022 / -0.0013

```

### Step size

* Steps are compared on simulated time, as for the other decks. The first run is the reference. Both programs are forced to the deck's `DATE` cards (monthly to 2005 May 1, then 2006 February 1, 2007 January 1, 2008 January 1 and the last at 2013 April 1). DeepFlow marches 463 steps with 14 cuts and 2268 Newton cycles, ours 511 steps with 41 cuts and 3497. The two have marched the same number of steps by day 1510 (330); after that ours takes 181 steps where DeepFlow takes 132.

```
run              THERM  OURS

steps              463   521

newton            2268  3393

newton/step      4.898 6.512

cuts                14    43

dt min            0.01  0.01

dt geomean        3.82 3.468

dt max            68.7 71.35

end day           3012  3012

steps@3.01d          9     9

steps@30.1d         15    15

steps@301d         132   133

steps@1.51e+03d    330   351

steps@3.01e+03d    462   521

```

![png]({{ "/assets/images/benchmark_image_68.png" | relative_url }})

#### ES-SAGD with solvent and a wellbore model (stflu031)

* The same model as stflu023 above (STARS Well Management Template No. 116: a `*GASTRAP` test with the keyword commented out, a semi-steady wellbore model), with a `DATE` card in most months and a `STOP` after the card of 2008 December 1 (day 1430), where the run ends. Its wells, fluids and schedule are stflu023's, so the first days of the two DeepFlow logs are identical.

* Reference is DeepFlow THERM: `stars_stflu031.log` and `stars_stflu031.prn`; its run ends at the same `STOP` in 320 steps. The deck here differs from DeepFlow's copy in a few output and perforation keywords only (`*OUTPRN`, `WPRN SECTOR`, and `OPEN FLOW-FROM` / `FLOW-TO` on the two perforations, which ours carries and DeepFlow's copy does not). As for stflu023 there is no grid in the `.prn`, so no profiles.

```
Running simulation [simuapp]: ES-SAGD with solvent and a wellbore model (-novtu)

Elapsed: 43.14s

No text to display.

```

```
OURS reached day 1430.0 of 1430

THERM: 320 steps marched, 9 cuts, 1420 Newton cycles

 OURS: 330 steps marched, 20 cuts, 1978 Newton cycles

```

### Wells

* As for stflu023: the producer's rates and the injected water, one point per step in both programs, on logarithmic time and gas axes, both wells on their BHP limits (2500 and 1000 kPa).

* The mean absolute gap to DeepFlow's steps is 14% in oil and 6% in water over days 90 to 200, 5.5% and 0.9% from day 200 to 1095, and 4.2% and 0.6% to day 1430; the gas 43%, 25% and 15%. These are stflu023's gaps over the same days, as the same model gives. At day 1430 the oil rate is 65.0 m3/day in DeepFlow and 67.1 in ours, the gas 30.5 and 33.8, the water 1939 and 1944.

```
     rate  mean |gap| % day 90-200  mean |gap| % day 200-1095  mean |gap| % day 1095-1430

      oil                      9.2                        1.7                         0.8

      gas                     31.6                       10.6                         5.6

    water                      6.2                        0.7                         0.5

inj_water                      3.1                        0.7                         0.5

```

![png]({{ "/assets/images/benchmark_image_69.png" | relative_url }})

### Material balance

* The cumulative balance at day 1430, the end of the run, in gmol (energy in J): DeepFlow's last table in its `.prn`, ours from the step of the `.out` that ends at day 1430. As for stflu023 the initial energy differs (-7.48e13 against -4.89e13 J), so it is compared on what was injected minus produced.

* The net water injected is 3.5% lower in ours, the bitumen produced 1.7% lower and the `CH4` 2.0% lower; the `C6H14` produced is 2.4% higher; the net energy is 4.2% lower. The balance error of ours is within 0.03% for water, bitumen, `CH4` and energy and 1.2% for `C6H14`, against DeepFlow's 0.12% for `CH4` and below 0.07% for the rest.

```
          initial DEEPFLOW  initial OURS   net DEEPFLOW     net OURS  diff %   balance error % DEEPFLOW / OURS

   WATER      1.575167e+09  1.575276e+09   3.380247e+08 3.355357e+08   -0.74          -0.0622 / -0.0003

 BITUMEN      1.768460e+08  1.768589e+08  -9.809174e+07 -9.780281e+07   -0.29           0.0206 / -0.0465

     CH4      3.646309e+06  3.646575e+06  -2.476333e+06 -2.497426e+06    0.85          -0.1225 / 0.6843

   C6H14      1.823154e+06  1.823288e+06   1.425575e+06 1.493350e+06    4.75           0.0485 / -0.2954

  Energy     -7.479612e+13 -4.890307e+13   2.327664e+14 2.256537e+14   -3.06           0.0010 / -0.0033

```

### Step size

* Steps are compared on simulated time, as for the other decks. The first run is the reference. Both programs are forced to the deck's `DATE` cards and end at its `STOP`. DeepFlow marches 320 steps with 9 cuts and 1420 Newton cycles, ours 321 steps with 20 cuts and 1922.

```
run              THERM  OURS

steps              320   330

newton            1420  1978

newton/step      4.438 5.994

cuts                 9    20

dt min            0.01  0.01

dt geomean       2.641 2.563

dt max           24.96  18.9

end day           1430  1430

steps@1.43d          7     7

steps@14.3d         13    13

steps@143d          85    89

steps@715d         182   181

steps@1.43e+03d    320   330

```

![png]({{ "/assets/images/benchmark_image_70.png" | relative_url }})

#### Dual-well SAGD in a dipping reservoir (stflu030)

* 25x3x26 Cartesian block (2 m blocks along I, three 100 m rows, 1 to 2 m layers; porosity 0.23 to 0.30, 1468 md horizontally and 562 md vertically) dipping across the rows (`*DTOP` 734.4, 739.6 and 744.0 m), at 48 C and 7600 kPa at 760 m. The oil is a dead oil, 122807 cp at 47 C and 3.3 cp at 300 C (`*VISCTABLE`); components `WATER` and `OIL`.

* Five wells with discretised wellbores (a `FLOW-TO` / `FLOW-FROM` chain through the perforations): the upper pair `UPCASI` (producer on the casing, minimum BHP 11700 kPa) and `UPTUB` (steam injector on the tubing), the lower pair `LWCASI` (producer, minimum BHP 10700 kPa, `STL` limit 50) and `LWTUB` (injector), and `LWTUBP` (producer on the lower tubing, `STL` limit 300). The steam is at 324 C and quality 0.5, `*STW` 200 and a BHP limit of 11700 kPa, on wells of `*FRAC` 0.5, so 100 m3/day each. Wells are shut in and opened by `DATE` cards through 1996; the run ends on 1997 to 2007 year-end cards at 2007 December 31 (day 4382).

* Reference is DeepFlow THERM's time step summary, `stars_stflu030.log` (340 steps). It carries the field totals only, so the wells are compared as field totals: ours is the sum of the producers' (and of the injectors') columns of the `.smy`. DeepFlow's copy of the deck differs from this one in the output cards, `*GRID *VARI` against `*CART`, and in the perforation keywords (`'SURFACE'` and `CLOSED` against 0 and `CLOSE`).

```
Running simulation [simuapp]: Dual-well SAGD in a dipping reservoir (-novtu)

Elapsed: 56.56s

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

![png]({{ "/assets/images/benchmark_image_71.png" | relative_url }})

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

![png]({{ "/assets/images/benchmark_image_72.png" | relative_url }})

# Speed



`-DCMAKE_BUILD_TYPE=Release`

### Dome corner grid

```
Running simulation [simuapp]: Dome Corner point

Elapsed: 4.77s

    65  41.9475  2    365.000     1.65                                                                   0.000   34.975   0.0697    3.673



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  4.488s  97.77%      

|- Newton                                 4.468s  |- 99.56%   

  |- Update                               1.482s    |- 33.17% 

  |- FluxJac                              1.379s    |- 30.86% 

  |- Solver                               0.535s    |- 11.97% 

  |- ScdAcc                               0.373s    |- 8.36%  

  |- update_dev                           0.276s    |- 6.19%  

  |- Precond                              0.190s    |- 4.26%  

  |- Residual                             0.058s    |- 1.31%  

  |- HeatLoss                             0.045s    |- 1.00%  

  |- SanitizeJac                          0.026s    |- 0.57%  

  |- alignvar                             0.025s    |- 0.55%  

  |- PerfJac                              0.010s    |- 0.23%  

|- Output                                 0.009s  |- 0.21%    

|- Logging                                0.005s  |- 0.12%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.102s  2.23%       

|- execution                              0.094s  |- 91.83%   

------------------------------------------------------------

TOTAL                                     4.590s

============================================================



Time steps : 65/68, step size: 5.61538, 11.8477

```

```
Found 4 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu018_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_73.png" | relative_url }})

## Heterogeneous

### SPE10 benchmark 2D 

```
Running simulation [simuapp]: SPE10 benchmark 2D water flooding 375 days ~7s single thread (OMP_NUM_THREADS=8)

Elapsed: 7.03s

    92   2.2603  2    375.000    19.31             4e-06             2e-05                      19.43    0.000    0.575   0.0466    0.002



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  6.764s  98.86%      

|- Newton                                 6.618s  |- 97.85%   

  |- Solver                               2.386s    |- 36.06% 

  |- Update                               1.682s    |- 25.42% 

  |- FluxJac                              1.272s    |- 19.22% 

  |- ScdAcc                               0.424s    |- 6.41%  

  |- update_dev                           0.291s    |- 4.39%  

  |- Precond                              0.168s    |- 2.54%  

  |- PerfJac                              0.163s    |- 2.46%  

  |- Residual                             0.068s    |- 1.02%  

  |- alignvar                             0.026s    |- 0.39%  

  |- SanitizeJac                          0.021s    |- 0.32%  

  |- HeatLoss                             0.010s    |- 0.15%  

|- Output                                 0.107s  |- 1.58%    

|- Logging                                0.035s  |- 0.52%    

|- Input                                  0.002s  |- 0.03%    

Initialization                            0.078s  1.14%       

|- execution                              0.070s  |- 89.75%   

------------------------------------------------------------

TOTAL                                     6.842s

============================================================



Time steps : 92/93, step size: 4.07609, 2.87497

```

![png]({{ "/assets/images/benchmark_image_74.png" | relative_url }})

### Medium size



* 202,005 grid block (201x201x5) with heterogeneous permeability

* 61 wells water flooding pattern 

* 1500 days

```
Running simulation [simuapp]: Heterogeneous + 61wells - performance test medium size ~4m.50s (Single) (OMP_NUM_THREADS=8, -novtu)

Elapsed: 300.86s

    34  23.7345  3    365.000   257.46              8.72              3.28                     720.00    0.000  137.265   0.0117    1.433



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                               4m 58.76s  99.47%      

|- Newton                              4m 57.25s  |- 99.50%   

  |- Solver                            1m 41.05s    |- 34.00% 

  |- FluxJac                           1m 16.09s    |- 25.60% 

  |- Update                             1m 9.31s    |- 23.32% 

  |- ScdAcc                              17.199s    |- 5.79%  

  |- update_dev                          12.282s    |- 4.13%  

  |- Precond                              8.253s    |- 2.78%  

  |- Residual                             3.401s    |- 1.14%  

  |- HeatLoss                             2.118s    |- 0.71%  

  |- PerfJac                              1.578s    |- 0.53%  

  |- alignvar                             0.701s    |- 0.24%  

  |- SanitizeJac                          0.601s    |- 0.20%  

|- Output                                 0.101s  |- 0.03%    

|- Logging                                0.077s  |- 0.03%    

|- Input                                  0.007s  |- 0.00%    

Initialization                            1.602s  0.53%       

|- execution                              1.446s  |- 90.24%   

------------------------------------------------------------

TOTAL                                   5m 0.36s

============================================================



Time steps : 34/35, step size: 10.7353, 11.6116

```

### Johnansen water flooding

```
Running simulation [simuapp]: Johnansen water flooding takes ~5m on M2 (OMP_NUM_THREADS=8)

Elapsed: 21.87s

    17 365.0000  1    25   3650.000   353.94              0.06              0.02                     189.09    0.000    3.220   0.0066  3.0e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 19.808s  92.61%      

|- Newton                                19.668s  |- 99.30%   

  |- Update                               6.584s    |- 33.48% 

  |- FluxJac                              5.577s    |- 28.36% 

  |- Solver                               4.095s    |- 20.82% 

  |- ScdAcc                               1.179s    |- 6.00%  

  |- update_dev                           0.896s    |- 4.55%  

  |- Precond                              0.616s    |- 3.13%  

  |- Residual                             0.300s    |- 1.53%  

  |- alignvar                             0.063s    |- 0.32%  

  |- SanitizeJac                          0.032s    |- 0.16%  

  |- PerfJac                              0.002s    |- 0.01%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.091s  |- 0.46%    

|- Logging                                0.002s  |- 0.01%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            1.581s  7.39%       

|- execution                              1.271s  |- 80.36%   

------------------------------------------------------------

TOTAL                                    21.389s

============================================================



Time steps : 17/17, step size: 214.706, 163.784

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data//stflu016_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_75.png" | relative_url }})

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

Elapsed: 1.29s

    75  53.9980  3    34   3650.000     0.01              4.31             99.77                       5.96    0.659  235.228   0.0062    2.644



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.054s  93.85%      

|- Newton                                 1.040s  |- 98.67%   

  |- FluxJac                              0.421s    |- 40.47% 

  |- Update                               0.281s    |- 26.99% 

  |- ScdAcc                               0.115s    |- 11.10% 

  |- update_dev                           0.110s    |- 10.57% 

  |- Solver                               0.037s    |- 3.55%  

  |- PerfJac                              0.029s    |- 2.79%  

  |- Precond                              0.017s    |- 1.60%  

  |- alignvar                             0.007s    |- 0.65%  

  |- Residual                             0.005s    |- 0.51%  

  |- HeatLoss                             0.004s    |- 0.34%  

  |- SanitizeJac                          0.001s    |- 0.10%  

|- Output                                 0.005s  |- 0.49%    

|- Logging                                0.003s  |- 0.27%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.069s  6.15%       

|- execution                              0.066s  |- 95.53%   

------------------------------------------------------------

TOTAL                                     1.123s

============================================================



Time steps : 75/75, step size: 48.6667, 60.2013

Running simulation [simumpi]: MPI comparison np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 1.34s

    54  36.7607  7    59   1249.050     1.97              6.22             75.95                       5.96    0.876   25.139   0.1994   51.689

    55  26.0137  6    44   1275.063     1.85              5.94             76.28                       5.96    0.876   25.724   0.1053   18.696

    56  33.1518  8    63   1308.215     1.69              5.80             77.48                       5.96    0.954   41.457   0.1670   25.758

    57  36.0661  7    54   1344.281     1.29              5.40             80.74                       5.96    0.950   45.739   0.1355   24.005

    58  40.7150  6    51   1384.996     1.27              5.29             80.70                       5.96    0.944   58.854   0.1252   25.583

    59  44.4552  5    44   1429.451     1.11              5.37             82.91                       5.96    0.939   63.965   0.1889   23.116

    60  45.9139  6    52   1475.365     0.96              5.31             84.73                       5.96    0.933   54.596   0.1576   31.387



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  44.7321  5    41   1520.097     0.87              5.49             86.39                       5.96    0.929   57.770   0.1944   15.742

    62  45.4536  6    52   1565.551     0.71              5.43             88.48                       5.96    0.924   58.921   0.1097   21.013

    63  54.8414  7    73   1620.392     0.61              5.31             89.69                       5.96    0.917   80.922   0.1464    8.034

    64  64.7696  4    37   1685.162     0.55              5.35             90.68                       5.96    0.909   91.889   0.0846    6.757

    65  96.6269  7    80   1781.789     0.44              5.35             92.46                       5.96    0.898  145.893   0.0767    6.430

    66 149.1514  4    41   1930.940     0.32              5.38             94.33                       5.96    0.882  240.692   0.0610    9.263

    67 211.9688  6    74   2142.909     0.21              5.31             96.12                       5.96    0.860  372.902   0.1094   12.037

    68 247.9906  4    47   2390.900     0.14              5.30             97.46                       5.96    0.833  494.049   0.0556   13.106

    69 249.6887  6    66   2640.588     0.09              5.20             98.32                       5.96    0.803  559.643   0.0801   12.309

    70 233.7552  7    93   2874.344     0.06              5.06             98.89                       5.96    0.773  601.043   0.0599   11.211

    71 209.5562  4    45   3083.900     0.04              4.96             99.25                       5.96    0.745  602.217   0.0331    9.759

    72 187.6365  4    46   3271.536     0.03              4.83             99.48                       5.96    0.719  591.998   0.0265    8.525

    73 169.7853  4    48   3441.322     0.02              4.68             99.62                       5.96    0.694  585.445   0.0222    7.620

    74 154.6805  6    68   3596.002     0.01              4.43             99.73                       5.96    0.669  591.286   0.0721    7.039

    75  53.9980  3    34   3650.000     0.01              4.31             99.77                       5.96    0.659  235.228   0.0062    2.644

Time steps : 75/75, step size: 48.6667, 60.2013

Running simulation [simumpi]: MPI comparison np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 0.99s

    54  36.7611  7   119   1249.051     1.97              6.22             75.95                       5.96    0.876   25.140   0.1994   51.689

    55  26.0140  6    86   1275.065     1.85              5.94             76.28                       5.96    0.876   25.724   0.1053   18.695

    56  33.1527  8   112   1308.217     1.69              5.80             77.48                       5.96    0.954   41.455   0.1670   25.758

    57  36.0671  7    98   1344.285     1.29              5.40             80.74                       5.96    0.950   45.739   0.1355   24.006

    58  40.7155  6    86   1385.000     1.27              5.29             80.70                       5.96    0.944   58.857   0.1252   25.584

    59  44.4544  6    92   1429.454     1.11              5.37             82.91                       5.96    0.939   64.019   0.1897   23.113

    60  45.7968  6    96   1475.251     0.96              5.31             84.73                       5.96    0.933   54.408   0.1575   31.388



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  44.6168  5    79   1519.868     0.87              5.49             86.38                       5.96    0.929   57.660   0.1947   15.773

    62  45.3037  6    97   1565.172     0.71              5.43             88.46                       5.96    0.924   58.815   0.1098   20.882

    63  54.8260  7   138   1619.998     0.61              5.31             89.69                       5.96    0.917   80.625   0.1452    8.029

    64  65.0006  4    69   1684.998     0.55              5.35             90.68                       5.96    0.909   92.188   0.0854    6.821

    65  96.6449  7   150   1781.643     0.44              5.35             92.45                       5.96    0.898  145.902   0.0771    6.432

    66 148.9741  3    60   1930.617     0.32              5.38             94.33                       5.96    0.883  240.384   0.0610    9.254

    67 211.8228  6   137   2142.440     0.21              5.31             96.12                       5.96    0.860  372.558   0.1095   12.031

    68 247.9341  4    85   2390.374     0.14              5.30             97.46                       5.96    0.833  493.828   0.0556   13.105

    69 249.6955  6   122   2640.070     0.09              5.20             98.32                       5.96    0.803  559.525   0.0802   12.311

    70 233.7910  7   160   2873.861     0.06              5.06             98.89                       5.96    0.773  600.974   0.0600   11.214

    71 209.6031  4    84   3083.464     0.04              4.96             99.25                       5.96    0.745  602.218   0.0331    9.762

    72 187.6784  4    85   3271.142     0.03              4.83             99.48                       5.96    0.719  592.014   0.0265    8.527

    73 169.8204  4    86   3440.963     0.02              4.68             99.62                       5.96    0.694  585.455   0.0222    7.622

    74 154.7109  6   123   3595.674     0.01              4.43             99.73                       5.96    0.669  591.232   0.0722    7.040

    75  54.3264  3    61   3650.000     0.01              4.31             99.77                       5.96    0.660  236.589   0.0062    2.659

Time steps : 75/75, step size: 48.6667, 60.1976

Running simulation [simumpi]: MPI comparison np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 0.73s

    54  36.7594  7   151   1249.046     1.97              6.22             75.95                       5.96    0.876   25.137   0.1994   51.689

    55  26.0127  6   111   1275.058     1.85              5.94             76.28                       5.96    0.876   25.725   0.1053   18.698

    56  33.1486  8   151   1308.207     1.69              5.80             77.48                       5.96    0.954   41.464   0.1670   25.758

    57  36.0624  7   128   1344.269     1.29              5.40             80.73                       5.96    0.950   45.738   0.1354   24.003

    58  40.7134  6   112   1384.983     1.27              5.29             80.70                       5.96    0.944   58.844   0.1252   25.578

    59  44.4581  5   103   1429.441     1.11              5.37             82.91                       5.96    0.939   63.964   0.1888   23.124

    60  45.9215  6   124   1475.362     0.96              5.31             84.73                       5.96    0.933   54.609   0.1577   31.395



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  44.7327  5   106   1520.095     0.87              5.49             86.39                       5.96    0.929   57.771   0.1945   15.742

    62  45.4520  6   131   1565.547     0.71              5.43             88.48                       5.96    0.924   58.920   0.1097   21.011

    63  54.8415  7   181   1620.389     0.61              5.31             89.69                       5.96    0.917   80.918   0.1463    8.034

    64  64.7730  4    95   1685.162     0.55              5.35             90.68                       5.96    0.909   91.893   0.0846    6.758

    65  96.6276  7   199   1781.789     0.44              5.35             92.46                       5.96    0.898  145.894   0.0767    6.430

    66 149.1496  4   103   1930.939     0.32              5.38             94.33                       5.96    0.882  240.689   0.0610    9.263

    67 211.9673  6   173   2142.906     0.21              5.31             96.12                       5.96    0.860  372.899   0.1094   12.037

    68 247.9898  4   108   2390.896     0.14              5.30             97.46                       5.96    0.833  494.047   0.0556   13.106

    69 249.6886  6   161   2640.585     0.09              5.20             98.32                       5.96    0.803  559.641   0.0801   12.309

    70 233.7554  7   217   2874.340     0.06              5.06             98.89                       5.96    0.773  601.042   0.0599   11.211

    71 209.5565  4   109   3083.896     0.04              4.96             99.25                       5.96    0.745  602.217   0.0331    9.759

    72 187.6368  4   112   3271.533     0.03              4.83             99.48                       5.96    0.719  591.998   0.0265    8.525

    73 169.7855  4   113   3441.319     0.02              4.68             99.62                       5.96    0.694  585.445   0.0222    7.620

    74 154.6808  6   164   3596.000     0.01              4.43             99.73                       5.96    0.668  591.285   0.0721    7.039

    75  54.0005  3    82   3650.000     0.01              4.31             99.77                       5.96    0.659  235.238   0.0062    2.644

Time steps : 75/75, step size: 48.6667, 60.2013

simuapp          rc=0   1.12s   75/ 75 steps  to  3650.00 days

simumpi np=1     rc=0   1.01s   75/ 75 steps,  0 cuts  to  3650.00 days

simumpi np=2     rc=0   0.64s   75/ 75 steps,  0 cuts  to  3650.00 days

simumpi np=4     rc=0   0.44s   75/ 75 steps,  0 cuts  to  3650.00 days

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


![png]({{ "/assets/images/benchmark_image_76.png" | relative_url }})

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

Elapsed: 19.78s

   153  53.9655  6    77   1095.000     1.34              1.17             46.66                               0.073   31.620   0.0691    3.479



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 19.548s  99.68%      

|- Newton                                19.521s  |- 99.86%   

  |- FluxJac                              8.966s    |- 45.93% 

  |- Update                               4.949s    |- 25.35% 

  |- ScdAcc                               1.997s    |- 10.23% 

  |- update_dev                           1.806s    |- 9.25%  

  |- Solver                               0.946s    |- 4.85%  

  |- Precond                              0.352s    |- 1.80%  

  |- alignvar                             0.108s    |- 0.55%  

  |- Residual                             0.087s    |- 0.45%  

  |- PerfJac                              0.075s    |- 0.38%  

  |- HeatLoss                             0.071s    |- 0.36%  

  |- SanitizeJac                          0.021s    |- 0.11%  

|- Logging                                0.016s  |- 0.08%    

|- Output                                 0.008s  |- 0.04%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.063s  0.32%       

|- execution                              0.060s  |- 96.25%   

------------------------------------------------------------

TOTAL                                    19.610s

============================================================



Time steps : 153/161, step size: 7.15686, 14.9924

Running simulation [simumpi]: CSS parity np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 19.82s

   132   0.7398  3    21    749.410     5.88             50.39             89.55                               0.045  144.857   0.2641    5.833

   133   0.6253  6    42    750.036     6.50             38.74             85.63                               0.045   96.207   0.3191    3.729

   134   0.4665  5    27    750.502     8.05             32.47             80.13                               0.045   61.826   0.0820    2.316

   135   0.7037  6    36    751.206     9.55             26.23             73.31                               0.045   77.962   0.4466    2.626

   136   0.4128  4    20    751.619    10.95             23.61             68.31                               0.045   42.673   0.1359    1.358

   137   0.5053  4    19    752.124    11.94             21.67             64.47                               0.045   47.315   0.2107    1.482

   138   0.4903  3    15    752.614    12.10             20.93             63.36                               0.045   41.430   0.0369    1.298

   139   0.9180  4    22    753.532    11.71             19.58             62.59                               0.045   64.154   0.2327   16.724

   140   0.8396  6    30    754.372    11.32             19.11             62.80                               0.045   49.513   0.2824    1.654

   141   0.6797  2    10    755.052    10.30             19.50             65.45                               0.045   35.874   0.0411    1.215

   142   1.2447  3    18    756.296     9.37             19.18             67.19                               0.045   58.511   0.0400    1.929

   143   2.2935  2    14    758.590     8.13             18.16             69.08                               0.045   88.705   0.0230    2.974

   144   4.6393  3    24    763.229     6.62             15.21             69.68                               0.045  125.603   0.0280    4.910

   145   9.1230  5    46    772.352     4.92             11.02             69.15                               0.045  146.725   0.0730    7.531

   146  14.3209  5    45    786.673     3.88              8.15             67.73                               0.045  133.262   0.0925    8.846

   147  20.6654  6    70    807.338     3.01              5.65             65.24                               0.045  113.871   0.0930    9.227

   148  29.7677  5    59    837.106     2.52              4.08             61.80                               0.045   90.353   0.0758    9.081

   149  46.1477 12   122    883.254     2.10              2.95             58.37                               0.045   74.816   0.1332    8.758

   150  46.1477 12   117    929.401     2.00              2.37             54.23                               0.045   48.229   0.0915    5.942



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   151  46.1477  6    68    975.549     1.80              1.88             51.00                               0.049   38.590   0.0966    4.771

   152  65.4853  5    55   1041.034     1.67              1.45             46.51                               0.049   43.149   0.0789    5.176

   153  53.9655  6    77   1095.000     1.34              1.17             46.66                               0.073   31.620   0.0691    3.479

Time steps : 153/161, step size: 7.15686, 14.9924

Running simulation [simumpi]: CSS parity np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 11.63s

   132   0.6112  6   104    750.028     6.37             38.92             85.94                               0.046   93.852   0.2923    3.688

   133   0.4836  4    54    750.512     7.77             32.33             80.62                               0.047   63.722   0.1119    2.427

   134   0.6464  4    58    751.158     9.08             26.94             74.78                               0.047   71.940   0.2913    2.554

   135   0.5127  4    52    751.671    10.32             23.33             69.34                               0.047   52.355   0.2198    1.651

   136   0.4852  3    39    752.156    11.48             21.37             65.04                               0.047   45.098   0.2091    1.401

   137   0.4729  5    58    752.629    11.66             20.56             63.81                               0.047   39.821   0.0571    1.237

   138   0.7992  6    80    753.428    11.44             19.38             62.88                               0.047   56.921   0.1061   13.552

   139   1.0922  5    72    754.520    11.40             18.12             61.39                               0.047   62.727   0.4441    8.674

   140   0.6435  6    74    755.164    10.27             18.77             64.63                               0.047   33.454   0.0491    1.128

   141   1.1312  3    41    756.295     9.41             18.39             66.14                               0.047   52.957   0.0525    1.741

   142   1.9550  3    45    758.250     8.26             17.91             68.44                               0.047   77.247   0.0284    2.549

   143   3.8365  3    55    762.087     6.86             15.66             69.53                               0.047  110.971   0.0222    4.282

   144   7.7960  5   103    769.882     5.17             11.69             69.33                               0.047  139.438   0.0733    6.877

   145  12.2168  5   110    782.099     4.08              8.88             68.51                               0.047  130.500   0.0863    8.182

   146  18.0969  4    84    800.196     3.31              6.27             65.44                               0.047  115.484   0.0593    8.903

   147  30.2580  8   194    830.454     2.57              4.29             62.54                               0.047  104.012   0.0771    9.981

   148  15.1290  7   119 1  845.583     2.33              3.71             61.40                               0.047   37.496   0.0579    4.079

   149  25.4687  6   136    871.052     2.02              3.14             60.82                               0.050   43.647   0.1258    5.158

   150  32.3242  6   144    903.376     1.94              2.62             57.48                               0.050   38.679   0.1085    4.741



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   151  43.7650  6   155    947.141     1.91              2.14             52.94                               0.050   40.257   0.0566    5.077

   152  74.1304 11   292   1021.272     1.68              1.55             47.96                               0.050   51.731   0.0994    6.304

   153  73.7284  7   196   1095.000     1.56              1.18             43.01                               0.050   42.985   0.0911    4.772

Time steps : 153/162, step size: 7.15686, 15.6515

Running simulation [simumpi]: CSS parity np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 7.15s

   132   0.7397  3    70    749.410     5.88             50.39             89.55                               0.045  144.859   0.2641    5.834

   133   0.6253  6   144    750.036     6.50             38.74             85.63                               0.045   96.220   0.3191    3.729

   134   0.4665  5    96    750.502     8.05             32.47             80.13                               0.045   61.832   0.0821    2.317

   135   0.7035  6   116    751.206     9.55             26.23             73.31                               0.045   77.952   0.4465    2.626

   136   0.4128  4    68    751.618    10.95             23.61             68.31                               0.045   42.671   0.1359    1.358

   137   0.5053  4    72    752.124    11.94             21.67             64.47                               0.045   47.320   0.2108    1.483

   138   0.4902  3    54    752.614    12.10             20.93             63.36                               0.045   41.425   0.0370    1.297

   139   0.9178  4    78    753.532    11.71             19.58             62.59                               0.045   64.144   0.2323   16.724

   140   0.8403  6   114    754.372    11.32             19.11             62.80                               0.045   49.555   0.2826    1.655

   141   0.6798  2    39    755.052    10.30             19.50             65.45                               0.045   35.882   0.0411    1.216

   142   1.2450  3    62    756.297     9.36             19.18             67.19                               0.045   58.520   0.0399    1.929

   143   2.2940  2    47    758.591     8.13             18.16             69.08                               0.045   88.718   0.0230    2.975

   144   4.6406  3    75    763.231     6.62             15.21             69.68                               0.045  125.616   0.0280    4.911

   145   9.1250  5   139    772.357     4.92             11.02             69.15                               0.045  146.725   0.0729    7.532

   146  14.3250  5   142    786.682     3.88              8.15             67.72                               0.045  133.264   0.0926    8.847

   147  20.6687  6   211    807.350     3.01              5.65             65.24                               0.045  113.860   0.0930    9.227

   148  29.7744  5   165    837.125     2.52              4.08             61.79                               0.045   90.345   0.0757    9.081

   149  46.1718 12   384    883.296     2.10              2.95             58.37                               0.045   74.824   0.1332    8.759

   150  46.1718 12   387    929.468     2.00              2.37             54.23                               0.045   48.233   0.0915    5.943



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   151  46.1718  6   218    975.640     1.80              1.88             50.99                               0.049   38.597   0.0966    4.772

   152  65.5376  5   178   1041.178     1.67              1.45             46.51                               0.049   43.166   0.0789    5.177

   153  53.8224  6   241   1095.000     1.33              1.17             46.71                               0.073   31.537   0.0690    3.470

Time steps : 153/161, step size: 7.15686, 14.992

simuapp          rc=0  19.61s  153/161 steps  to  1095.00 days

simumpi np=1     rc=0  19.49s  153/161 steps,  8 cuts  to  1095.00 days

simumpi np=2     rc=0  11.33s  153/162 steps,  9 cuts  to  1095.00 days

simumpi np=4     rc=0   6.85s  153/161 steps,  8 cuts  to  1095.00 days

```

![png]({{ "/assets/images/benchmark_image_77.png" | relative_url }})

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

Elapsed: 0.62s

    14  36.5999  1     3    365.000    63.57              0.03              0.04                               0.000    6.379 9.26e-05  3.5e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.319s  77.35%      

|- Newton                                 0.318s  |- 99.56%   

  |- Update                               0.119s    |- 37.46% 

  |- FluxJac                              0.116s    |- 36.58% 

  |- ScdAcc                               0.032s    |- 10.04% 

  |- update_dev                           0.022s    |- 6.96%  

  |- Solver                               0.014s    |- 4.37%  

  |- Precond                              0.006s    |- 1.88%  

  |- Residual                             0.002s    |- 0.77%  

  |- alignvar                             0.002s    |- 0.55%  

  |- HeatLoss                             0.001s    |- 0.32%  

  |- SanitizeJac                          0.000s    |- 0.12%  

  |- PerfJac                              0.000s    |- 0.02%  

|- Output                                 0.001s  |- 0.18%    

|- Logging                                0.000s  |- 0.11%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.093s  22.65%      

|- execution                              0.084s  |- 89.35%   

------------------------------------------------------------

TOTAL                                     0.413s

============================================================



Time steps : 14/14, step size: 26.0714, 49.2511

Running simulation [simumpi]: stflu015 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 0.60s

            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-27





VTU generation is suppressed.



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.0200  1     1      0.020    63.59             4e-06             6e-06                               0.000    0.016 2.37e-07  9.2e-07

     2   0.0467  1     1      0.067    63.59             1e-05             2e-05                               0.000    0.038 5.53e-07  2.2e-06

     3   0.1089  1     1      0.176    63.59             3e-05             5e-05                               0.000    0.089 1.29e-06  5.0e-06

     4   0.2540  1     1      0.430    63.59             8e-05             1e-04                               0.000    0.207 3.00e-06  1.2e-05

     5   0.5923  1     1      1.022    63.59             2e-04             3e-04                               0.000    0.479 6.95e-06  2.7e-05

     6   1.3802  1     1      2.402    63.59             5e-04             7e-04                               0.000    1.102 1.60e-05  6.2e-05

     7   3.2111  1     1      5.613    63.59              0.00              0.00                               0.000    2.494 3.62e-05  1.4e-04

     8   4.3868  1     2     10.000    63.59              0.00              0.00                               0.000    3.285 4.77e-05  1.9e-04

     9   7.0000  1     2     17.000    63.59              0.00              0.00                               0.000    4.956 7.19e-05  2.8e-04

    10  16.1203  1     2     33.120    63.59              0.01              0.01                               0.000   10.132 1.47e-04  5.7e-04

    11  36.6245  1     3     69.745    63.59              0.01              0.02                               0.000   18.253 2.65e-04    0.001

    12  81.4906  1     4    151.235    63.58              0.02              0.03                               0.000   27.474 3.99e-04    0.002

    13 177.1648  1     5    328.400    63.57              0.02              0.04                               0.000   34.806 5.04e-04    0.002

    14  36.5999  1     3    365.000    63.57              0.03              0.04                               0.000    6.379 9.26e-05  3.5e-04

Time steps : 14/14, step size: 26.0714, 49.2511

Running simulation [simumpi]: stflu015 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 0.47s

            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-27





VTU generation is suppressed.



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.0200  1     1      0.020    63.59             4e-06             6e-06                               0.000    0.016 2.37e-07  9.2e-07

     2   0.0467  1     1      0.067    63.59             1e-05             2e-05                               0.000    0.038 5.53e-07  2.2e-06

     3   0.1089  1     1      0.176    63.59             3e-05             5e-05                               0.000    0.089 1.29e-06  5.0e-06

     4   0.2540  1     1      0.430    63.59             8e-05             1e-04                               0.000    0.207 3.00e-06  1.2e-05

     5   0.5923  1     1      1.022    63.59             2e-04             3e-04                               0.000    0.479 6.95e-06  2.7e-05

     6   1.3802  1     1      2.402    63.59             5e-04             7e-04                               0.000    1.102 1.60e-05  6.2e-05

     7   3.2111  1     1      5.613    63.59              0.00              0.00                               0.000    2.494 3.62e-05  1.4e-04

     8   4.3868  1     2     10.000    63.59              0.00              0.00                               0.000    3.285 4.77e-05  1.9e-04

     9   7.0000  1     2     17.000    63.59              0.00              0.00                               0.000    4.956 7.19e-05  2.8e-04

    10  16.1203  1     2     33.120    63.59              0.01              0.01                               0.000   10.132 1.47e-04  5.7e-04

    11  36.6245  1     3     69.745    63.59              0.01              0.02                               0.000   18.253 2.65e-04    0.001

    12  81.4906  1     4    151.235    63.58              0.02              0.03                               0.000   27.474 3.99e-04    0.002

    13 177.1648  1     5    328.400    63.57              0.02              0.04                               0.000   34.806 5.04e-04    0.002

    14  36.5999  1     3    365.000    63.57              0.03              0.04                               0.000    6.379 9.26e-05  3.5e-04

Time steps : 14/14, step size: 26.0714, 49.2511

Running simulation [simumpi]: stflu015 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 0.40s



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-27





VTU generation is suppressed.

VTU generation is suppressed.



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.0200  1     1      0.020    63.59             4e-06             6e-06                               0.000    0.016 2.37e-07  9.2e-07

     2   0.0467  1     1      0.067    63.59             1e-05             2e-05                               0.000    0.038 5.53e-07  2.2e-06

     3   0.1089  1     1      0.176    63.59             3e-05             5e-05                               0.000    0.089 1.29e-06  5.0e-06

     4   0.2540  1     1      0.430    63.59             8e-05             1e-04                               0.000    0.207 3.00e-06  1.2e-05

     5   0.5923  1     2      1.022    63.59             2e-04             3e-04                               0.000    0.479 6.95e-06  2.7e-05

     6   1.3802  1     2      2.402    63.59             5e-04             7e-04                               0.000    1.102 1.60e-05  6.2e-05

     7   3.2111  1     2      5.613    63.59              0.00              0.00                               0.000    2.494 3.62e-05  1.4e-04

     8   4.3868  1     2     10.000    63.59              0.00              0.00                               0.000    3.285 4.77e-05  1.9e-04

     9   7.0000  1     2     17.000    63.59              0.00              0.00                               0.000    4.956 7.19e-05  2.8e-04

    10  16.1203  1     3     33.120    63.59              0.01              0.01                               0.000   10.132 1.47e-04  5.7e-04

    11  36.6245  1     3     69.745    63.59              0.01              0.02                               0.000   18.253 2.65e-04    0.001

    12  81.4906  1     4    151.235    63.58              0.02              0.03                               0.000   27.474 3.99e-04    0.002

    13 177.1648  1     8    328.400    63.57              0.02              0.04                               0.000   34.806 5.04e-04    0.002

    14  36.5999  1     5    365.000    63.57              0.03              0.04                               0.000    6.379 9.26e-05  3.5e-04

Time steps : 14/14, step size: 26.0714, 49.2511

Running simulation [simuapp]: stflu018 baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 9.51s

    65  41.9475  2    24    365.000     1.65                                                                   0.000   34.975   0.0697    3.673



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  9.255s  99.11%      

|- Newton                                 9.243s  |- 99.88%   

  |- FluxJac                              3.773s    |- 40.82% 

  |- Update                               2.689s    |- 29.10% 

  |- ScdAcc                               1.033s    |- 11.18% 

  |- update_dev                           0.899s    |- 9.73%  

  |- Solver                               0.445s    |- 4.82%  

  |- Precond                              0.183s    |- 1.98%  

  |- alignvar                             0.054s    |- 0.58%  

  |- Residual                             0.050s    |- 0.54%  

  |- HeatLoss                             0.038s    |- 0.41%  

  |- SanitizeJac                          0.011s    |- 0.12%  

  |- PerfJac                              0.010s    |- 0.10%  

|- Logging                                0.003s  |- 0.04%    

|- Output                                 0.003s  |- 0.03%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.083s  0.89%       

|- execution                              0.075s  |- 90.27%   

------------------------------------------------------------

TOTAL                                     9.338s

============================================================



Time steps : 65/68, step size: 5.61538, 11.8477

Running simulation [simumpi]: stflu018 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 9.50s

    44   0.3527  1     4     18.353     0.22             27.91             99.22                               0.001  274.721   0.0533    7.685

    45   0.6073  1     4     18.960     0.16             21.36             99.27                               0.001  299.576   0.0261    6.607

    46   1.0223  4    18     19.982                      15.65            100.00                               0.001  316.278   0.1346    8.173

    47   1.2572  3    15     21.239                      13.06            100.00                               0.001  272.371   0.2064    7.617

    48   1.2346  6    26     22.474                      10.41            100.00                               0.001  185.649   0.1090    6.278

    49   1.6684  2    10     24.142                       7.79            100.00                               0.001  172.386   0.0613   12.010

    50   2.7633  3    16     26.906                       5.77            100.00                               0.001  204.053   0.1065    6.314

    51   3.7705  4    26     30.676     0.53              4.34             89.20                               0.001  194.663   0.0915    6.231

    52   5.4654  2    14     36.142     0.66              3.28             83.27                               0.001  186.985   0.1673    6.864

    53   6.0285  3    21     42.170     0.60              2.57             80.95                               0.001  141.787   0.1190    5.953

    54   7.8428  5    34     50.013     0.56              2.00             78.30                               0.001  126.416   0.0827    6.665

    55  11.7941  5    34     61.807     0.65              1.38             67.92                               0.001  113.534   0.1219    8.269

    56  15.1806  5    37     76.988     0.65              0.97             59.73                               0.001  107.438   0.1463    8.151

    57  17.9317  9    76     94.919     0.56              0.71             56.09                               0.001   96.866   0.1504    7.632

    58  20.8916 10    94    115.811     0.38              0.57             60.05                               0.000   77.650   0.1756    7.125

    59  22.4594 14   128    138.270     0.28              0.48             62.86                               0.000   51.589   0.0848    6.817

    60  19.2509  3    26    157.521     0.38              0.30             44.54                               0.000   34.370   0.0820    4.890



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  29.0472  3    27    186.568     0.63              0.12             15.87                               0.000   38.454   0.0936    5.891

    62  41.7313  6    70    228.300     0.91              0.01              0.81                               0.000   44.431   0.1848    6.726

    63  43.6299 10   114    271.930     1.31                                                                   0.000   31.407   0.1487    5.763

    64  51.1230  7    90    323.053     1.37                                                                   0.000   25.178   0.1588    5.395

    65  41.9475  2    24    365.000     1.65                                                                   0.000   34.975   0.0697    3.673

Time steps : 65/68, step size: 5.61538, 11.8477

Running simulation [simumpi]: stflu018 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 5.30s

    44   0.3527  1     6     18.353     0.22             27.91             99.22                               0.001  274.721   0.0533    7.685

    45   0.6073  1     6     18.960     0.16             21.36             99.27                               0.001  299.576   0.0261    6.607

    46   1.0223  4    27     19.982                      15.65            100.00                               0.001  316.278   0.1346    8.173

    47   1.2572  3    21     21.239                      13.06            100.00                               0.001  272.371   0.2064    7.617

    48   1.2346  6    38     22.474                      10.41            100.00                               0.001  185.649   0.1090    6.278

    49   1.6684  2    14     24.142                       7.79            100.00                               0.001  172.386   0.0613   12.010

    50   2.7633  3    23     26.906                       5.77            100.00                               0.001  204.053   0.1065    6.314

    51   3.7705  4    32     30.676     0.53              4.34             89.20                               0.001  194.663   0.0915    6.231

    52   5.4654  2    18     36.142     0.66              3.28             83.27                               0.001  186.985   0.1673    6.864

    53   6.0285  3    25     42.170     0.60              2.57             80.95                               0.001  141.787   0.1190    5.953

    54   7.8428  5    46     50.013     0.56              2.00             78.30                               0.001  126.416   0.0827    6.665

    55  11.7941  5    51     61.807     0.65              1.38             67.92                               0.001  113.534   0.1219    8.269

    56  15.1806  5    52     76.988     0.65              0.97             59.73                               0.001  107.438   0.1463    8.151

    57  17.9317  9    97     94.919     0.56              0.71             56.09                               0.001   96.866   0.1504    7.632

    58  20.8916 10   125    115.811     0.38              0.57             60.05                               0.000   77.650   0.1756    7.125

    59  22.4594 14   171    138.270     0.28              0.48             62.86                               0.000   51.589   0.0848    6.817

    60  19.2509  3    32    157.521     0.38              0.30             44.54                               0.000   34.370   0.0820    4.890



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  29.0472  3    36    186.568     0.63              0.12             15.87                               0.000   38.454   0.0936    5.891

    62  41.7313  6    98    228.300     0.91              0.01              0.81                               0.000   44.431   0.1848    6.726

    63  43.6299 10   158    271.930     1.31                                                                   0.000   31.407   0.1487    5.763

    64  51.1230  7   122    323.053     1.37                                                                   0.000   25.178   0.1588    5.395

    65  41.9475  2    32    365.000     1.65                                                                   0.000   34.975   0.0697    3.673

Time steps : 65/68, step size: 5.61538, 11.8477

Running simulation [simumpi]: stflu018 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 3.38s

    44   0.3527  1     8     18.353     0.22             27.91             99.22                               0.001  274.721   0.0533    7.685

    45   0.6073  1     9     18.960     0.16             21.36             99.27                               0.001  299.576   0.0261    6.607

    46   1.0223  4    35     19.982                      15.65            100.00                               0.001  316.278   0.1346    8.173

    47   1.2572  3    26     21.239                      13.06            100.00                               0.001  272.371   0.2064    7.617

    48   1.2346  6    45     22.474                      10.41            100.00                               0.001  185.649   0.1090    6.278

    49   1.6684  2    18     24.142                       7.79            100.00                               0.001  172.386   0.0613   12.010

    50   2.7633  3    28     26.906                       5.77            100.00                               0.001  204.053   0.1065    6.314

    51   3.7705  4    41     30.676     0.53              4.34             89.20                               0.001  194.663   0.0915    6.231

    52   5.4654  2    22     36.142     0.66              3.28             83.27                               0.001  186.985   0.1673    6.864

    53   6.0285  3    32     42.170     0.60              2.57             80.95                               0.001  141.787   0.1190    5.953

    54   7.8428  5    51     50.013     0.56              2.00             78.30                               0.001  126.416   0.0827    6.665

    55  11.7941  5    59     61.807     0.65              1.38             67.92                               0.001  113.534   0.1219    8.269

    56  15.1806  5    63     76.988     0.65              0.97             59.73                               0.001  107.438   0.1463    8.151

    57  17.9317  9   118     94.919     0.56              0.71             56.09                               0.001   96.866   0.1504    7.632

    58  20.8916 10   153    115.811     0.38              0.57             60.05                               0.000   77.650   0.1756    7.125

    59  22.4594 14   193    138.270     0.28              0.48             62.86                               0.000   51.589   0.0848    6.817

    60  19.2509  3    43    157.521     0.38              0.30             44.54                               0.000   34.370   0.0820    4.890



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  29.0472  3    42    186.568     0.63              0.12             15.87                               0.000   38.454   0.0936    5.891

    62  41.7314  6   109    228.300     0.91              0.01              0.81                               0.000   44.431   0.1848    6.726

    63  43.6299 10   178    271.930     1.31                                                                   0.000   31.407   0.1487    5.763

    64  51.1230  7   135    323.053     1.37                                                                   0.000   25.178   0.1588    5.395

    65  41.9474  2    35    365.000     1.65                                                                   0.000   34.975   0.0697    3.673

Time steps : 65/68, step size: 5.61538, 11.8477

Running simulation [simuapp]: lauwerier baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 1.37s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.115s  94.16%      

|- Newton                                 1.113s  |- 99.83%   

  |- Update                               0.395s    |- 35.53% 

  |- FluxJac                              0.322s    |- 28.94% 

  |- ScdAcc                               0.174s    |- 15.60% 

  |- update_dev                           0.122s    |- 10.93% 

  |- Precond                              0.022s    |- 1.95%  

  |- HeatLoss                             0.016s    |- 1.47%  

  |- Solver                               0.015s    |- 1.32%  

  |- Residual                             0.012s    |- 1.11%  

  |- PerfJac                              0.009s    |- 0.80%  

  |- alignvar                             0.007s    |- 0.63%  

  |- SanitizeJac                          0.001s    |- 0.08%  

|- Logging                                0.005s  |- 0.44%    

|- Output                                 0.000s  |- 0.04%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.069s  5.84%       

|- execution                              0.066s  |- 95.00%   

------------------------------------------------------------

TOTAL                                     1.184s

============================================================



Time steps : 10/18, step size: 12.6635, 22.211

Running simulation [simumpi]: lauwerier np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 1.38s



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-27





VTU generation is suppressed.



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  9     9      0.100                     158.99            100.00                     158.99    0.000  6.6e+04           137.021

     2   0.1333  1     1      0.233                     158.99            100.00                     158.99    0.000  1.5e-11            55.391

     3   0.2917  1     1      0.525                     158.99            100.00                     158.99    0.000  7.3e-12            60.863

     4   0.6344  1     1      1.159                     158.99            100.00                     158.99    0.000  7.3e-12            63.518

     5   1.3753  1     1      2.535                     158.99            100.00                     158.99    0.000  7.3e-12            63.104

     6   2.9832  1     1      5.518                     158.99            100.00                     158.99    0.000  7.3e-12            61.037

     7   6.4857  1     1     12.004                     158.99            100.00                     158.99    0.000  7.3e-12            58.056

     8  14.1477  1     1     26.151                     158.99            100.00                     158.99    0.000  7.3e-12            54.466

     9  30.9861  1     1     57.138                     158.99            100.00                     158.99    0.000  7.3e-12            33.614

    10  69.4977  1     1    126.635                     158.99            100.00                     158.99    0.003  7.3e-12 1.00e-05   13.679





TimeLoop terminates due to: too many step cut





Time steps : 10/18, step size: 12.6635, 22.211

Running simulation [simumpi]: lauwerier np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 0.95s

            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-27





VTU generation is suppressed.

VTU generation is suppressed.



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  9    39      0.100                     158.99            100.00                     158.99    0.000  6.6e+04           137.021

     2   0.1333  1     2      0.233                     158.99            100.00                     158.99    0.000  7.3e-11            55.391

     3   0.2917  1     2      0.525                     158.99            100.00                     158.99    0.000  5.8e-11            60.863

     4   0.6344  1     2      1.159                     158.99            100.00                     158.99    0.000  5.8e-11            63.518

     5   1.3753  1     3      2.535                     158.99            100.00                     158.99    0.000  1.0e-10            63.104

     6   2.9832  1     3      5.518                     158.99            100.00                     158.99    0.000  1.0e-10            61.037

     7   6.4857  1     3     12.004                     158.99            100.00                     158.99    0.000  1.0e-10            58.056

     8  14.1477  1     3     26.151                     158.99            100.00                     158.99    0.000  1.0e-10            54.466

     9  30.9861  1     3     57.138                     158.99            100.00                     158.99    0.000  1.0e-10            33.614

    10  69.4977  1     3    126.635                     158.99            100.00                     158.99    0.003  1.0e-10 1.00e-05   13.679





TimeLoop terminates due to: too many step cut





Time steps : 10/18, step size: 12.6635, 22.211

Running simulation [simumpi]: lauwerier np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 0.63s

            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-27





VTU generation is suppressed.

VTU generation is suppressed.



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  9    81      0.100                     158.99            100.00                     158.99    0.000  6.6e+04           137.021

     2   0.1333  1     2      0.233                     158.99            100.00                     158.99    0.000  1.4e-08            55.391

     3   0.2917  1     2      0.525                     158.99            100.00                     158.99    0.000  1.4e-08            60.863

     4   0.6344  1     4      1.159                     158.99            100.00                     158.99    0.000  2.9e-08            63.518

     5   1.3753  1     5      2.535                     158.99            100.00                     158.99    0.000  4.2e-08            63.104

     6   2.9832  1     5      5.518                     158.99            100.00                     158.99    0.000  4.2e-08            61.037

     7   6.4857  1     5     12.004                     158.99            100.00                     158.99    0.000  4.2e-08            58.056

     8  14.1477  1     5     26.151                     158.99            100.00                     158.99    0.000  4.2e-08            54.466

     9  30.9861  1     5     57.138                     158.99            100.00                     158.99    0.000  4.2e-08            33.614

    10  69.4977  1     5    126.635                     158.99            100.00                     158.99    0.003  4.1e-08 1.00e-05   13.679





TimeLoop terminates due to: too many step cut





Time steps : 10/18, step size: 12.6635, 22.211

Running simulation [simuapp]: stflu028 baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 0.28s

    40  31.4527  2     4   2435.000     0.08     1.44     0.21    19.02    73.71                               0.000   16.384 2.36e-04    0.037



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.058s  52.10%      

|- Newton                                 0.050s  |- 85.57%   

  |- FluxJac                              0.017s    |- 34.75% 

  |- Update                               0.015s    |- 30.81% 

  |- ScdAcc                               0.006s    |- 11.64% 

  |- update_dev                           0.005s    |- 9.77%  

  |- Solver                               0.002s    |- 4.52%  

  |- Precond                              0.001s    |- 2.28%  

  |- PerfJac                              0.001s    |- 1.63%  

  |- Residual                             0.000s    |- 0.82%  

  |- HeatLoss                             0.000s    |- 0.80%  

  |- alignvar                             0.000s    |- 0.59%  

  |- SanitizeJac                          0.000s    |- 0.17%  

|- Output                                 0.003s  |- 4.32%    

|- Logging                                0.001s  |- 1.32%    

|- Input                                  0.001s  |- 0.99%    

Initialization                            0.053s  47.90%      

|- execution                              0.051s  |- 94.88%   

------------------------------------------------------------

TOTAL                                     0.112s

============================================================



Time steps : 40/40, step size: 60.875, 37.2029

Running simulation [simumpi]: stflu028 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 0.30s

    19  18.6252  1     1    718.625     0.06     1.19     0.01    19.02    16.06                       0.02    0.000   13.776 2.55e-04    0.009

    20  43.1712  2     2    761.796     0.06     1.18     0.01    19.02    16.05                       0.03    0.000   50.538 9.93e-04    0.031

    21  90.0000  2     4    851.796     0.06     1.17     0.01    19.02    16.06                       0.08    0.000  247.144   0.0051    0.138

    22  90.0000  4     7    941.796     0.06     1.16     0.01    19.02    16.09                       0.32    0.000  561.064   0.0118    0.339

    23  90.0000  3     8   1031.796     0.06     1.15     0.01    19.02    16.66                       0.78    0.000  717.301   0.0149    0.727

    24  90.0000  3     9   1121.796     0.06     1.13     0.02    19.02    24.38                       1.31    0.000  661.012   0.0137    1.042

    25  90.0000  3     9   1211.796     0.06     1.13     0.06    19.02    48.50                       1.79    0.000  547.374   0.0118    1.212

    26  90.0000  3    11   1301.796     0.06     1.12     0.16    19.02    72.83                       2.14    0.000  399.735   0.0097    1.214

    27  90.0000  2     8   1391.796     0.06     1.12     0.35    19.02    85.67                       2.40    0.000  321.704   0.0088    1.146

    28  39.2036  2     6   1431.000     0.06     1.11     0.46    19.02    88.68                       2.68    0.000  170.767   0.0049    0.556

    29  84.4989  4    13   1515.499     0.17     3.18     2.27    19.02    93.15                               0.000  3.2e+03   0.0550    1.529

    30  78.0484  3     9   1593.547     0.13     2.57     1.41    19.02    91.29                               0.000  798.378   0.0118    0.815



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    31  90.0000  2     6   1683.547     0.11     2.18     1.07    19.02    90.33                               0.000  399.207   0.0055    0.634

    32  90.0000  2     6   1773.547     0.10     1.95     0.86    19.02    89.31                               0.000  247.593   0.0036    0.465

    33  90.0000  2     5   1863.547     0.09     1.80     0.70    19.02    88.01                               0.000  179.361   0.0024    0.355

    34  90.0000  2     4   1953.547     0.09     1.70     0.57    19.02    86.44                               0.000  138.678   0.0018    0.280

    35  90.0000  2     4   2043.547     0.09     1.63     0.47    19.02    84.58                               0.000  110.552   0.0015    0.226

    36  90.0000  2     4   2133.547     0.08     1.57     0.39    19.02    82.47                               0.000   89.592   0.0012    0.186

    37  90.0000  2     4   2223.547     0.08     1.52     0.32    19.02    80.12                               0.000   73.337 9.94e-04    0.155

    38  90.0000  2     4   2313.547     0.08     1.48     0.27    19.02    77.55                               0.000   60.452 8.32e-04    0.132

    39  90.0000  2     4   2403.547     0.08     1.45     0.23    19.02    74.78                               0.000   50.111 7.13e-04    0.113

    40  31.4527  2     4   2435.000     0.08     1.44     0.21    19.02    73.71                               0.000   16.384 2.36e-04    0.037

Time steps : 40/40, step size: 60.875, 37.2029

Running simulation [simumpi]: stflu028 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 0.30s

    19  18.6252  1     3    718.625     0.06     1.19     0.01    19.02    16.06                       0.02    0.000   13.776 2.55e-04    0.009

    20  43.1712  2     6    761.796     0.06     1.18     0.01    19.02    16.05                       0.03    0.000   50.538 9.93e-04    0.031

    21  90.0000  2     8    851.796     0.06     1.17     0.01    19.02    16.06                       0.08    0.000  247.143   0.0051    0.138

    22  90.0000  4    19    941.796     0.06     1.16     0.01    19.02    16.09                       0.32    0.000  561.063   0.0118    0.339

    23  90.0000  3    19   1031.796     0.06     1.15     0.01    19.02    16.66                       0.78    0.000  717.301   0.0149    0.727

    24  90.0000  3    22   1121.796     0.06     1.13     0.02    19.02    24.38                       1.31    0.000  661.012   0.0137    1.042

    25  90.0000  3    24   1211.796     0.06     1.13     0.06    19.02    48.50                       1.79    0.000  547.374   0.0118    1.212

    26  90.0000  3    26   1301.796     0.06     1.12     0.16    19.02    72.83                       2.14    0.000  399.735   0.0097    1.214

    27  90.0000  2    18   1391.796     0.06     1.12     0.35    19.02    85.67                       2.40    0.000  321.704   0.0088    1.146

    28  39.2036  2    16   1431.000     0.06     1.11     0.46    19.02    88.68                       2.68    0.000  170.767   0.0049    0.556

    29  84.4989  4    34   1515.499     0.17     3.18     2.27    19.02    93.15                               0.000  3.2e+03   0.0550    1.529

    30  78.0484  3    23   1593.547     0.13     2.57     1.41    19.02    91.29                               0.000  798.378   0.0118    0.815



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    31  90.0000  2    14   1683.547     0.11     2.18     1.07    19.02    90.33                               0.000  399.207   0.0055    0.634

    32  90.0000  2    14   1773.547     0.10     1.95     0.86    19.02    89.31                               0.000  247.593   0.0036    0.465

    33  90.0000  2    14   1863.547     0.09     1.80     0.70    19.02    88.01                               0.000  179.361   0.0024    0.355

    34  90.0000  2    12   1953.547     0.09     1.70     0.57    19.02    86.44                               0.000  138.678   0.0018    0.280

    35  90.0000  2    12   2043.547     0.09     1.63     0.47    19.02    84.58                               0.000  110.552   0.0015    0.226

    36  90.0000  2    12   2133.547     0.08     1.57     0.39    19.02    82.47                               0.000   89.592   0.0012    0.186

    37  90.0000  2    11   2223.547     0.08     1.52     0.32    19.02    80.12                               0.000   73.337 9.94e-04    0.155

    38  90.0000  2    11   2313.547     0.08     1.48     0.27    19.02    77.55                               0.000   60.452 8.32e-04    0.132

    39  90.0000  2    11   2403.547     0.08     1.45     0.23    19.02    74.78                               0.000   50.111 7.13e-04    0.113

    40  31.4527  2     8   2435.000     0.08     1.44     0.21    19.02    73.71                               0.000   16.384 2.36e-04    0.037

Time steps : 40/40, step size: 60.875, 37.2029

Running simulation [simumpi]: stflu028 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 0.32s

    19  18.6252  1     3    718.625     0.06     1.19     0.01    19.02    16.06                       0.02    0.000   13.776 2.55e-04    0.009

    20  43.1712  2     6    761.796     0.06     1.18     0.01    19.02    16.05                       0.03    0.000   50.538 9.93e-04    0.031

    21  90.0000  2     8    851.796     0.06     1.17     0.01    19.02    16.06                       0.08    0.000  247.143   0.0051    0.138

    22  90.0000  4    19    941.796     0.06     1.16     0.01    19.02    16.09                       0.32    0.000  561.063   0.0118    0.339

    23  90.0000  3    19   1031.796     0.06     1.15     0.01    19.02    16.66                       0.78    0.000  717.301   0.0149    0.727

    24  90.0000  3    23   1121.796     0.06     1.13     0.02    19.02    24.38                       1.31    0.000  661.012   0.0137    1.042

    25  90.0000  3    26   1211.796     0.06     1.13     0.06    19.02    48.50                       1.79    0.000  547.374   0.0118    1.212

    26  90.0000  3    28   1301.796     0.06     1.12     0.16    19.02    72.83                       2.14    0.000  399.735   0.0097    1.214

    27  90.0000  2    19   1391.796     0.06     1.12     0.35    19.02    85.67                       2.40    0.000  321.705   0.0088    1.146

    28  39.2036  2    17   1431.000     0.06     1.11     0.46    19.02    88.68                       2.68    0.000  170.767   0.0049    0.556

    29  84.4989  4    37   1515.499     0.17     3.18     2.27    19.02    93.15                               0.000  3.2e+03   0.0550    1.529

    30  78.0484  3    24   1593.547     0.13     2.57     1.41    19.02    91.29                               0.000  798.378   0.0118    0.815



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    31  90.0000  2    16   1683.547     0.11     2.18     1.07    19.02    90.33                               0.000  399.207   0.0055    0.634

    32  90.0000  2    14   1773.547     0.10     1.95     0.86    19.02    89.31                               0.000  247.593   0.0036    0.465

    33  90.0000  2    14   1863.547     0.09     1.80     0.70    19.02    88.01                               0.000  179.361   0.0024    0.355

    34  90.0000  2    14   1953.547     0.09     1.70     0.57    19.02    86.44                               0.000  138.678   0.0018    0.280

    35  90.0000  2    12   2043.547     0.09     1.63     0.47    19.02    84.58                               0.000  110.552   0.0015    0.226

    36  90.0000  2    12   2133.547     0.08     1.57     0.39    19.02    82.47                               0.000   89.592   0.0012    0.186

    37  90.0000  2    12   2223.547     0.08     1.52     0.32    19.02    80.12                               0.000   73.337 9.94e-04    0.155

    38  90.0000  2    11   2313.547     0.08     1.48     0.27    19.02    77.55                               0.000   60.452 8.32e-04    0.132

    39  90.0000  2    11   2403.547     0.08     1.45     0.23    19.02    74.78                               0.000   50.111 7.13e-04    0.113

    40  31.4527  2     8   2435.000     0.08     1.44     0.21    19.02    73.71                               0.000   16.384 2.36e-04    0.037

Time steps : 40/40, step size: 60.875, 37.2029

Running simulation [simuapp]: stflu029 baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 5.55s

   224  30.0000  8   152    820.000     0.04     0.00     1.58     0.05    97.61                       1.59    0.093    0.891   0.0782   13.984



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  5.312s  98.76%      

|- Newton                                 5.284s  |- 99.48%   

  |- FluxJac                              2.148s    |- 40.64% 

  |- Update                               1.350s    |- 25.55% 

  |- ScdAcc                               0.706s    |- 13.36% 

  |- update_dev                           0.535s    |- 10.13% 

  |- Solver                               0.270s    |- 5.10%  

  |- Precond                              0.121s    |- 2.29%  

  |- alignvar                             0.035s    |- 0.66%  

  |- Residual                             0.027s    |- 0.50%  

  |- PerfJac                              0.010s    |- 0.19%  

  |- SanitizeJac                          0.008s    |- 0.14%  

  |- HeatLoss                             0.006s    |- 0.11%  

|- Logging                                0.029s  |- 0.54%    

|- Output                                 0.007s  |- 0.14%    

|- Input                                  0.001s  |- 0.02%    

Initialization                            0.067s  1.24%       

|- execution                              0.064s  |- 96.34%   

------------------------------------------------------------

TOTAL                                     5.379s

============================================================



Time steps : 224/230, step size: 3.66071, 5.92345

Running simulation [simumpi]: stflu029 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 5.52s

   203  10.8395  6    80    455.000     0.04     0.00     1.56     0.10    97.45                       1.57    0.047   22.038   0.0341    6.673

   204  19.5067  6    91    474.507     0.04     0.00     1.56     0.11    97.54                       1.57    0.048   40.361   0.0610    9.605

   205  10.4933  4    48    485.000     0.04     0.00     1.57     0.11    97.58                       1.57    0.048   17.985   0.0289    4.819

   206  20.1651  7   106    505.165     0.04     0.00     1.57     0.11    97.62                       1.58    0.048   36.960   0.0706   14.276

   207   9.8349  6    84    515.000     0.04     0.00     1.57     0.11    97.62                       1.58    0.048   14.180   0.0309    5.580

   208  18.3878  6    96    533.388     0.04     0.00     1.57     0.10    97.65                       1.58    0.049   25.427   0.0749   14.820

   209  11.6122  4    50    545.000     0.04     0.00     1.57     0.10    97.66                       1.58    0.049   17.014   0.0296    7.312

   210  20.4495  6    95    565.450     0.04     0.00     1.58     0.09    97.70                       1.59    0.049   25.073   0.0557   10.806



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   211   9.5505  5    63    575.000     0.04     0.00     1.58     0.09    97.72                       1.59    0.049   10.807   0.0220    5.004

   212  18.2303  5    68    593.230     0.04     0.00     1.58     0.09    97.72                       1.59    0.049   19.958   0.0754   12.631

   213  11.7697  6    94    605.000     0.04     0.00     1.58     0.09    97.69                       1.59    0.049   10.695   0.0440    6.507

   214  21.2321  6   100    626.232     0.04     0.00     1.58     0.09    97.68                       1.59    0.049   15.706   0.0729   12.245

   215   8.7679  4    53    635.000     0.04     0.00     1.58     0.09    97.67                       1.59    0.049    5.336   0.0296    5.014

   216  16.7302  6    85    651.730     0.04     0.00     1.58     0.08    97.68                       1.59    0.049    8.596   0.0449    8.287

   217  13.2698  6    95    665.000     0.04     0.00     1.58     0.08    97.70                       1.59    0.049    5.878   0.0327    6.977

   218  23.6343  6   104    688.634     0.04     0.00     1.58     0.08    97.70                       1.59    0.044    8.540   0.0765   13.503

   219   6.3657  5    63    695.000     0.04     0.00     1.58     0.08    97.68                       1.59    0.044    1.330   0.0195    2.654

   220  13.1438  5    72    708.144     0.04     0.00     1.58     0.07    97.67                       1.59    0.044    3.128   0.0492    6.665

   221  21.8562  6    92    730.000     0.04     0.00     1.58     0.07    97.65                       1.59    0.044    4.081   0.0778   13.676

   222  30.0000 12   209    760.000     0.04     0.00     1.58     0.06    97.63                       1.59    0.058    3.154   0.0739   15.400

   223  30.0000  7   128    790.000     0.04     0.00     1.58     0.06    97.62                       1.58    0.058    1.365   0.0683   13.844

   224  30.0000  8   152    820.000     0.04     0.00     1.58     0.05    97.61                       1.59    0.093    0.891   0.0782   13.984

Time steps : 224/230, step size: 3.66071, 5.92345

Running simulation [simumpi]: stflu029 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 3.36s

   205   8.3555  4   106    485.000     0.04     0.00     1.57     0.11    97.58                       1.57    0.047   14.168   0.0229    3.731

   206  16.7230  6   203    501.723     0.04     0.00     1.57     0.11    97.62                       1.58    0.048   31.222   0.0495   11.276

   207  13.2770  5   148    515.000     0.04     0.00     1.57     0.11    97.63                       1.58    0.048   19.841   0.0464    8.789

   208  22.2774  7   241    537.277     0.04     0.00     1.57     0.10    97.65                       1.59    0.048   30.888   0.0882   17.943

   209   7.7226  4   104    545.000     0.04     0.00     1.57     0.10    97.65                       1.58    0.048   11.341   0.0201    4.146

   210  15.2158  7   227    560.216     0.04     0.00     1.58     0.10    97.68                       1.59    0.062   19.105   0.0486    7.209



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   211  14.7842  6   172    575.000     0.04     0.00     1.58     0.09    97.72                       1.59    0.062   16.946   0.0339    8.877

   212  24.7370  6   208    599.737     0.04     0.00     1.58     0.09    97.70                       1.59    0.074   26.121   0.0930   16.305

   213   5.2630  4   108    605.000     0.04     0.00     1.58     0.09    97.68                       1.59    0.074    4.891   0.0142    2.611

   214  11.0035  4   109    616.004     0.04     0.00     1.58     0.09    97.66                       1.59    0.074    8.191   0.0436    5.240

   215  18.9965  6   205    635.000     0.04     0.00     1.58     0.09    97.67                       1.59    0.074   12.559   0.0745   12.400

   216  28.5765  7   246    663.576     0.04     0.00     1.58     0.08    97.69                       1.59    0.074   14.040   0.0707   14.333

   217   1.4235  2    49    665.000     0.04     0.00     1.58     0.08    97.69                       1.59    0.074    0.820   0.0034    0.631

   218   3.2309  3    81    668.231     0.04     0.00     1.58     0.08    97.69                       1.59    0.074    1.065   0.0075    1.481

   219   7.0731  4   114    675.304     0.04     0.00     1.58     0.08    97.70                       1.59    0.074    2.914   0.0159    4.461

   220  13.7730  5   146    689.077     0.04     0.00     1.58     0.08    97.69                       1.59    0.074    4.534   0.0477    7.372

   221   5.9230  5   130    695.000     0.04     0.00     1.58     0.08    97.68                       1.59    0.074    1.310   0.0188    2.633

   222  12.2829  5   142    707.283     0.04     0.00     1.58     0.07    97.67                       1.59    0.074    2.831   0.0443    6.244

   223  22.7171  7   249    730.000     0.04     0.00     1.58     0.07    97.65                       1.59    0.075    4.218   0.0831   14.289

   224  30.0000 12   405    760.000     0.04     0.00     1.58     0.06    97.63                       1.59    0.087    3.163   0.0731   15.367

   225  30.0000  7   256    790.000     0.04     0.00     1.58     0.06    97.62                       1.58    0.087    1.414   0.0683   13.711

   226  30.0000  8   298    820.000     0.04     0.00     1.58     0.05    97.61                       1.58    0.126    0.894   0.0793   13.914

Time steps : 226/232, step size: 3.62832, 5.9781

Running simulation [simumpi]: stflu029 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 2.43s



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   211  15.7088  6   221    530.709     0.04     0.00     1.59     0.12    97.79                       1.59    3.130   21.338   0.0375    8.154

   212  14.2912  5   161    545.000     0.04     0.00     1.59     0.11    97.79                       1.60    3.130   21.098   0.0552    8.560

   213  24.1563  7   277    569.156     0.04     0.00     1.58     0.10    97.75                       1.60    3.224   28.684   0.0943   14.859

   214   5.8437  6   185    575.000     0.04     0.00     1.58     0.10    97.74                       1.59    3.224    6.541   0.0194    2.735

   215  11.6873  6   224    586.687     0.04     0.00     1.58     0.10    97.75                       1.59    3.224   12.574   0.0519    7.415

   216  18.3127  6   232    605.000     0.04     0.00     1.59     0.10    97.77                       1.59    3.224   17.192   0.0464   10.925

   217  28.7635  6   238    633.764     0.04     0.00     1.59     0.09    97.75                       1.60    3.233   20.669   0.0910   15.071

   218   1.2365  2    52    635.000     0.04     0.00     1.59     0.09    97.75                       1.59    3.233    0.936   0.0036    0.588

   219   2.8116  2    57    637.812     0.04     0.00     1.58     0.09    97.74                       1.59    3.233    1.774   0.0076    1.528

   220   6.1431  3    93    643.955     0.04     0.00     1.58     0.09    97.73                       1.59    3.233    3.246   0.0224    3.260

   221  12.4700  7   238    656.425     0.04     0.00     1.58     0.08    97.73                       1.59    3.233    5.529   0.0354    6.908

   222   8.5753  5   148    665.000     0.04     0.00     1.58     0.08    97.73                       1.59    3.233    3.557   0.0372    4.430

   223  16.0296  5   163    681.030     0.04     0.00     1.59     0.08    97.75                       1.59    3.233    6.108   0.0411    7.903

   224  13.9704  6   195    695.000     0.04     0.00     1.59     0.08    97.77                       1.60    3.233    4.298   0.0362    7.674

   225  24.3069  6   227    719.307     0.04     0.00     1.59     0.07    97.75                       1.60    3.233    5.363   0.0658   11.855

   226  10.6931  5   156    730.000     0.04     0.00     1.59     0.07    97.73                       1.59    3.233    1.548   0.0314    4.596

   227  20.6293 10   376    750.629     0.04     0.00     1.58     0.06    97.70                       1.59    3.233    2.822   0.0654   11.778

   228   9.3707  6   194    760.000     0.04     0.00     1.58     0.06    97.68                       1.59    3.233    1.032   0.0309    4.911

   229  17.9479  7   262    777.948     0.04     0.00     1.58     0.06    97.67                       1.59    3.233    1.501   0.0639    9.350

   230  12.0521  6   223    790.000     0.04     0.00     1.58     0.06    97.66                       1.59    3.233    1.723   0.0276    4.536

   231  23.4038  7   268    813.404     0.04     0.00     1.58     0.05    97.67                       1.59    3.246    1.441   0.0528   10.689

   232   6.5962  5   148    820.000     0.04     0.00     1.58     0.05    97.67                       1.59    3.246    1.899   0.0128    2.759

Time steps : 232/239, step size: 3.53448, 5.44854

Running simulation [simuapp]: stflu019 baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 133.92s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                2m 3.50s  93.10%      

|- Newton                               2m 3.11s  |- 99.68%   

  |- Update                              57.416s    |- 46.64% 

  |- FluxJac                             34.701s    |- 28.19% 

  |- Solver                               9.835s    |- 7.99%  

  |- ScdAcc                               8.920s    |- 7.25%  

  |- update_dev                           7.715s    |- 6.27%  

  |- Precond                              1.557s    |- 1.26%  

  |- Residual                             0.753s    |- 0.61%  

  |- alignvar                             0.476s    |- 0.39%  

  |- SanitizeJac                          0.281s    |- 0.23%  

  |- HeatLoss                             0.022s    |- 0.02%  

  |- PerfJac                              0.013s    |- 0.01%  

|- Logging                                0.302s  |- 0.24%    

|- Output                                 0.053s  |- 0.04%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            9.149s  6.90%       

|- execution                              6.920s  |- 75.64%   

------------------------------------------------------------

TOTAL                                  2m 12.65s

============================================================



Time steps : 11/11, step size: 3.27389, 4.63394

Running simulation [simumpi]: stflu019 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 108.75s

            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-27





VTU generation is suppressed.



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1     3      0.100    29.89              0.02              0.05                      40.00    0.000  153.606   0.0015    0.078

     2   0.1655  1     4      0.266    27.99              0.03              0.11                      40.00    0.000  162.930   0.0029    0.108

     3   0.2693  1     5      0.535    26.18              0.04              0.16                      40.00    0.000  188.590   0.0051    0.150

     4   0.4180  1     5      0.953    24.67              0.05              0.20                      40.00    0.000  184.538   0.0082    0.206

     5   0.6537  1     6      1.607    23.49              0.05              0.23                      40.00    0.000  170.897   0.0128    0.297

     6   1.0478  1     9      2.654    22.58              0.06              0.26                      40.00    0.000  144.654   0.0171    0.444

     7   1.7643  1    12      4.419    21.83              0.06              0.27                      40.00    0.000  143.106   0.0234    0.715

     8   2.9796  1    15      7.398    21.15              0.06              0.29                      40.00    0.000  137.296   0.0218    1.166

     9   5.0892  1    19     12.487    20.49              0.06              0.30                      40.00    0.000  124.482   0.0274    1.876

    10   8.9153  1    26     21.403    19.83              0.06              0.31                      40.00    0.000  158.943   0.0354    3.004

    11  14.6100  1    30     36.013    19.27              0.06              0.31                      40.00    0.000  181.378   0.0568    4.175





TimeLoop terminates due to: reach maximum time step





Time steps : 11/11, step size: 3.27389, 4.63394

Running simulation [simumpi]: stflu019 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 62.34s

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-27





VTU generation is suppressed.

VTU generation is suppressed.



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1     4      0.100    29.89              0.02              0.05                      40.00    0.000  153.607   0.0015    0.078

     2   0.1655  1     4      0.266    27.99              0.03              0.11                      40.00    0.000  162.930   0.0029    0.108

     3   0.2693  1     5      0.535    26.18              0.04              0.16                      40.00    0.000  188.590   0.0051    0.150

     4   0.4180  1     5      0.953    24.67              0.05              0.20                      40.00    0.000  184.538   0.0082    0.206

     5   0.6537  1     6      1.607    23.49              0.05              0.23                      40.00    0.000  170.897   0.0128    0.297

     6   1.0478  1     9      2.654    22.58              0.06              0.26                      40.00    0.000  144.654   0.0171    0.444

     7   1.7643  1    12      4.419    21.83              0.06              0.27                      40.00    0.000  143.106   0.0234    0.715

     8   2.9796  1    15      7.398    21.15              0.06              0.29                      40.00    0.000  137.296   0.0218    1.166

     9   5.0892  1    19     12.487    20.49              0.06              0.30                      40.00    0.000  124.482   0.0274    1.876

    10   8.9153  1    26     21.403    19.83              0.06              0.31                      40.00    0.000  158.943   0.0354    3.004

    11  14.6100  1    30     36.013    19.27              0.06              0.31                      40.00    0.000  181.378   0.0568    4.175





TimeLoop terminates due to: reach maximum time step





Time steps : 11/11, step size: 3.27389, 4.63394

Running simulation [simumpi]: stflu019 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 43.68s

            DATE:    2026-11-27





VTU generation is suppressed.

VTU generation is suppressed.

VTU generation is suppressed.



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1     4      0.100    29.89              0.02              0.05                      40.00    0.000  153.607   0.0015    0.078

     2   0.1655  1     4      0.266    27.99              0.03              0.11                      40.00    0.000  162.930   0.0029    0.108

     3   0.2693  1     5      0.535    26.18              0.04              0.16                      40.00    0.000  188.590   0.0051    0.150

     4   0.4180  1     5      0.953    24.67              0.05              0.20                      40.00    0.000  184.538   0.0082    0.206

     5   0.6537  1     6      1.607    23.49              0.05              0.23                      40.00    0.000  170.897   0.0128    0.297

     6   1.0478  1     9      2.654    22.58              0.06              0.26                      40.00    0.000  144.654   0.0171    0.444

     7   1.7643  1    12      4.419    21.83              0.06              0.27                      40.00    0.000  143.106   0.0234    0.715

     8   2.9796  1    14      7.398    21.15              0.06              0.29                      40.00    0.000  137.296   0.0218    1.166

     9   5.0892  1    18     12.487    20.49              0.06              0.30                      40.00    0.000  124.483   0.0274    1.876

    10   8.9153  1    24     21.403    19.83              0.06              0.31                      40.00    0.000  158.943   0.0354    3.004

    11  14.6100  1    35     36.013    19.27              0.06              0.31                      40.00    0.000  181.379   0.0568    4.175





TimeLoop terminates due to: reach maximum time step





Time steps : 11/11, step size: 3.27389, 4.63394

Running simulation [simuapp]: stflu010 baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 3.97s

   278 1.75e-03  4    39      0.375    8e-04     0.07             92.81                       0.04             0.005    0.007   0.0551    0.107



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  3.664s  97.25%      

|- Newton                                 3.645s  |- 99.48%   

  |- FluxJac                              1.365s    |- 37.45% 

  |- Update                               0.846s    |- 23.21% 

  |- ScdAcc                               0.542s    |- 14.88% 

  |- update_dev                           0.373s    |- 10.23% 

  |- Solver                               0.264s    |- 7.24%  

  |- Precond                              0.156s    |- 4.27%  

  |- alignvar                             0.022s    |- 0.61%  

  |- Residual                             0.015s    |- 0.40%  

  |- PerfJac                              0.008s    |- 0.21%  

  |- SanitizeJac                          0.007s    |- 0.20%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Logging                                0.023s  |- 0.64%    

|- Output                                 0.011s  |- 0.31%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.104s  2.75%       

|- execution                              0.093s  |- 89.67%   

------------------------------------------------------------

TOTAL                                     3.768s

============================================================



Time steps : 278/293, step size: 0.00134892, 0.000607167

Running simulation [simumpi]: stflu010 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 3.86s

   257 1.74e-03  8    88      0.339    7e-04     0.07             98.28                       0.09             0.006    0.196   0.0405    0.292

   258 1.74e-03  6    62      0.340    7e-04     0.07             97.93                       0.25             0.006    0.085   0.0065    0.461

   259 1.74e-03  2    19      0.342    7e-04     0.07             97.62                       0.27             0.006    0.008 8.32e-04    0.554

   260 1.74e-03  3    27      0.344    7e-04     0.07             97.31                       0.27             0.006    0.010 5.43e-04    0.774

   261 1.74e-03  4    39      0.345    7e-04     0.07             96.98                       0.27             0.005    0.060 7.30e-04    1.005

   262 1.74e-03  5    49      0.347    7e-04     0.07             96.66                       0.27             0.005    0.097 7.99e-04    0.860

   263 1.74e-03  6    66      0.349    7e-04     0.07             96.35                       0.03             0.005    0.070   0.0540    0.594

   264 1.74e-03  6    38      0.351    7e-04     0.07             96.05                       0.07             0.005    0.028   0.0448    0.247

   265 1.74e-03  5    42      0.352    8e-04     0.07             95.75                       0.07             0.005    0.020   0.0461    0.223

   266 1.74e-03  4    34      0.354    8e-04     0.07             95.46                       0.06             0.005    0.013   0.0472    0.203

   267 1.74e-03  4    33      0.356    8e-04     0.07             95.18                       0.06             0.005    0.008   0.0482    0.187

   268 1.74e-03  4    32      0.358    8e-04     0.07             94.92                       0.05             0.005    0.005   0.0491    0.173

   269 1.74e-03  4    32      0.359    8e-04     0.07             94.66                       0.05             0.005    0.003   0.0500    0.161

   270 1.74e-03  4    31      0.361    8e-04     0.07             94.41                       0.05             0.005    0.002   0.0507    0.151



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   271 1.74e-03  4    31      0.363    8e-04     0.07             94.18                       0.05             0.005    0.002   0.0514    0.142

   272 1.74e-03  4    32      0.365    8e-04     0.07             93.95                       0.04             0.005    0.002   0.0521    0.135

   273 1.74e-03  3    27      0.366    8e-04     0.07             93.74                       0.04             0.005    0.002   0.0526    0.128

   274 1.74e-03  3    28      0.368    8e-04     0.07             93.53                       0.04             0.005    0.002   0.0532    0.123

   275 1.74e-03  3    27      0.370    8e-04     0.07             93.34                       0.04             0.005    0.003   0.0537    0.118

   276 1.74e-03  3    28      0.372    8e-04     0.07             93.15                       0.04             0.005    0.003   0.0541    0.113

   277 1.74e-03  3    29      0.373    8e-04     0.07             92.98                       0.04             0.005    0.004   0.0544    0.110

   278 1.75e-03  4    39      0.375    8e-04     0.07             92.81                       0.04             0.005    0.007   0.0551    0.107

Time steps : 278/293, step size: 0.00134892, 0.000607167

Running simulation [simumpi]: stflu010 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 2.16s

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   241 1.74e-03  3    40      0.335    7e-04     0.07             99.02                       0.05             0.135    0.051   0.0493    0.090

   242 1.74e-03  7    99      0.337    7e-04     0.07             98.65                       0.16             0.135    0.234   0.0242    0.404

   243 1.74e-03  3    36      0.339    7e-04     0.07             98.31                       0.26             0.134    0.017   0.0030    0.487

   244 1.74e-03  2    25      0.340    7e-04     0.07             97.99                       0.27             0.132    0.009 6.14e-04    0.614

   245 1.74e-03  3    36      0.342    7e-04     0.07             97.66                       0.27             0.131    0.013 6.35e-04    0.937

   246 1.74e-03  7    86      0.344    7e-04     0.07             97.32                       0.27             0.130    0.099 7.70e-04    0.939

   247 1.74e-03  5    64      0.345    7e-04     0.07             96.98                       0.14             0.130    0.083   0.0279    0.240

   248 1.74e-03  4    48      0.347    7e-04     0.07             96.65                       0.07             0.130    0.049   0.0436    0.268

   249 1.74e-03  5    57      0.349    7e-04     0.07             96.32                       0.07             0.130    0.027   0.0450    0.241

   250 1.74e-03  5    57      0.351    8e-04     0.07             95.99                       0.06             0.130    0.017   0.0463    0.218

   251 1.74e-03  5    55      0.352    8e-04     0.07             95.68                       0.06             0.130    0.011   0.0474    0.199

   252 1.74e-03  4    45      0.354    8e-04     0.07             95.38                       0.06             0.130    0.007   0.0483    0.184

   253 1.74e-03  5    56      0.356    8e-04     0.07             95.08                       0.05             0.130    0.005   0.0493    0.170

   254 1.74e-03  5    54      0.358    8e-04     0.07             94.80                       0.05             0.130    0.003   0.0501    0.159

   255 1.74e-03  5    54      0.359    8e-04     0.07             94.53                       0.05             0.130    0.002   0.0509    0.149

   256 1.74e-03  5    54      0.361    8e-04     0.07             94.27                       0.05             0.131    0.002   0.0515    0.141

   257 1.74e-03  4    40      0.363    8e-04     0.07             94.02                       0.04             0.131    0.002   0.0522    0.133

   258 1.74e-03  3    38      0.365    8e-04     0.07             93.78                       0.04             0.131    0.002   0.0528    0.127

   259 1.74e-03  3    38      0.366    8e-04     0.07             93.55                       0.04             0.131    0.002   0.0533    0.121

   260 1.74e-03  3    38      0.368    8e-04     0.07             93.34                       0.04             0.131    0.003   0.0538    0.117

   261 1.74e-03  4    48      0.370    8e-04     0.07             93.13                       0.04             0.131    0.003   0.0542    0.113

   262 1.74e-03  4    49      0.372    8e-04     0.07             92.94                       0.04             0.132    0.005   0.0545    0.109

   263 1.74e-03  4    50      0.373    8e-04     0.07             92.75                       0.04             0.132    0.008   0.0546    0.106

   264 1.75e-03  4    48      0.375    8e-04     0.07             92.58                       0.04             0.132    0.021   0.0546    0.103

Time steps : 264/272, step size: 0.00142045, 0.000575319

Running simulation [simumpi]: stflu010 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 0.42s



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-27





VTU generation is suppressed.

VTU generation is suppressed.

VTU generation is suppressed.

VTU generation is suppressed.



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1 6.94e-06  4   131    6.9e-06     0.02                                                  0.87             0.000  375.307 1.58e-07    0.064

     2 4.63e-06  2    66    1.2e-05     0.02                                                  1.56             0.000  144.003 7.32e-08    0.082

     3 5.51e-06  2    66    1.7e-05     0.02                                                  2.38             0.002  119.224 8.23e-08    0.169

     4 7.16e-06  3   100    2.4e-05     0.02                                                  3.47             0.001   67.798 9.70e-08    0.345

     5 3.84e-06  2    65 1  2.8e-05     0.02                                                  4.98             0.002   54.715 3.79e-08    0.280

     6 2.19e-06  2    66 1  3.0e-05     0.02                                                  6.00             0.002   58.620 2.45e-08    0.196

     7 1.22e-06  2    64 1  3.1e-05     0.02                                                  6.60             0.002   41.455 1.73e-08    0.122





TimeLoop terminates due to: time step too small





Time steps : 7/11, step size: 4.49779e-06, 2.25925e-06

Running simulation [simuapp]: stflu021 baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 5.51s

   178 113.2794  3    32   2526.000     2.23            149.16             98.53                     150.00    0.445   75.573   0.0406    5.069



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  5.278s  98.88%      

|- Newton                                 5.240s  |- 99.29%   

  |- FluxJac                              1.927s    |- 36.78% 

  |- Update                               1.266s    |- 24.16% 

  |- ScdAcc                               0.602s    |- 11.49% 

  |- update_dev                           0.553s    |- 10.55% 

  |- PerfJac                              0.525s    |- 10.02% 

  |- Solver                               0.161s    |- 3.07%  

  |- Precond                              0.072s    |- 1.38%  

  |- alignvar                             0.032s    |- 0.62%  

  |- Residual                             0.025s    |- 0.47%  

  |- SanitizeJac                          0.005s    |- 0.09%  

  |- HeatLoss                             0.004s    |- 0.08%  

|- Output                                 0.014s  |- 0.27%    

|- Logging                                0.011s  |- 0.22%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.060s  1.12%       

|- execution                              0.057s  |- 95.69%   

------------------------------------------------------------

TOTAL                                     5.337s

============================================================



Time steps : 178/189, step size: 14.191, 22.7331

Running simulation [simumpi]: stflu021 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 5.57s

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   151   4.1345  4    31   1965.914    62.32            220.88             77.99                     150.00    0.445    4.925   0.1666    4.225

   152   4.5713  4    32   1970.485    61.73            196.98             76.14                     150.00    0.445    7.050   0.1289    4.516

   153   5.7374  3    24   1976.223    62.54            183.51             74.58                     150.00    0.445    4.418   0.1709    6.630

   154   6.2585  5    38   1982.481    63.93            180.16             73.81                     150.00    0.445    4.847   0.1484    5.693

   155   7.3395  4    34   1989.821    66.95            196.59             74.60                     150.00    0.445    7.316   0.1718    9.186

   156   7.9821  4    34   1997.803    69.05            213.40             75.55                     150.00    0.445    4.062   0.2301   13.209

   157   7.3491  6    46   2005.152    62.56            191.55             75.38                     150.00    0.445    6.394   0.1401    2.947

   158   8.8677  5    40   2014.019    57.20            180.72             75.96                     150.00    0.445   12.841   0.2143   16.311

   159   8.5201  6    48   2022.540    53.13            161.70             75.27                     150.00    0.445   11.155   0.1008    6.424

   160  11.8919  6    65   2034.431    49.85            157.29             75.93                     150.00    0.445    4.974   0.1802    8.951

   161  12.6055  5    47   2047.037    48.68            171.84             77.92                     150.00    0.445    0.998   0.3106    7.400

   162   9.5792  6    62   2056.616    44.45            170.20             79.29                     150.00    0.445    4.702   0.1671    2.817

   163  10.5736  4    33   2067.190    43.51            168.96             79.52                     150.00    0.445    6.979   0.2117   11.114

   164  10.2329  5    44   2077.423    43.38            179.56             80.54                     150.00    0.445    5.198   0.2572    8.080

   165   8.7947  4    34   2086.217    41.70            183.01             81.44                     150.00    0.445    9.069   0.1963    7.533

   166   8.8890  5    41   2095.106    41.19            193.77             82.47                     150.00    0.445    5.041   0.2862   10.057

   167   7.1327  5    39   2102.239    37.37            180.92             82.88                     150.00    0.445    6.294   0.1216    3.700

   168   9.1922  4    32   2111.431    36.97            193.58             83.96                     150.00    0.445    6.721   0.2883    9.336

   169   7.3403  6    43   2118.772    32.72            190.42             85.34                     150.00    0.445    6.700   0.2125    7.548

   170   7.0864  4    29   2125.858    27.62            171.48             86.13                     150.00    0.445   14.110   0.0731    8.215

   171  11.1164  6    53   2136.974    30.35            168.96             84.77                     150.00    0.445   14.517   0.1081   17.372

   172  14.6370  5    46   2151.611    27.16            154.54             85.05                     150.00    0.445    3.718   0.1278    4.910

   173  18.4390  5    48   2170.050    19.79            145.59             88.04                     150.00    0.445    1.304   0.0860    3.579

   174  27.3483  3    30   2197.399    13.87            144.37             91.24                     150.00    0.445    5.549   0.0749    4.462

   175  42.5561  3    30   2239.955     9.28            145.86             94.02                     150.00    0.445   14.725   0.0736    5.311

   176  66.6117  3    31   2306.566     5.94            147.54             96.13                     150.00    0.445   32.157   0.0696    5.838

   177 106.1542  3    31   2412.721     3.55            148.66             97.67                     150.00    0.445   63.508   0.0626    6.203

   178 113.2794  3    32   2526.000     2.23            149.16             98.53                     150.00    0.445   75.573   0.0406    5.069

Time steps : 178/189, step size: 14.191, 22.7331

Running simulation [simumpi]: stflu021 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 5.82s

   152   4.5047  5   125   1971.166    57.26            210.38             78.60                     150.00    0.024   10.200   0.0969    8.812

   153   6.3849  5   128   1977.551    59.17            201.29             77.28                     150.00    0.024   10.442   0.2282   11.358

   154   5.9094  4   113   1983.460    61.81            195.46             75.98                     150.00    0.024    4.929   0.1926    6.389

   155   6.0365  4   102   1989.497    60.71            186.42             75.44                     150.00    0.024    3.846   0.1218    2.465

   156   7.7742  4   100   1997.271    58.06            182.92             75.91                     150.00    0.024    3.069   0.1754    4.986

   157   8.3631  5   132   2005.634    55.80            180.48             76.38                     150.00    0.024    4.802   0.1789    5.566

   158   8.9005  6   145   2014.534    53.71            175.86             76.60                     150.00    0.024    5.584   0.1959    7.751

   159   9.0061  5   129   2023.540    52.08            176.64             77.23                     150.00    0.024    6.419   0.2639    6.487

   160   7.6165  5   135   2031.157    49.22            166.50             77.18                     150.00    0.024    8.449   0.2330    5.808

   161   6.9606  5   135   2038.117    46.88            155.59             76.85                     150.00    0.024   10.770   0.0959    5.789

   162   9.9083  7   166   2048.026    49.64            168.99             77.30                     150.00    0.024   10.369   0.2224   17.019

   163   9.3131  5   133   2057.339    53.14            185.44             77.73                     150.00    0.024    5.445   0.2575    3.671

   164   7.9997  4    96   2065.339    50.59            189.02             78.88                     150.00    0.024    7.573   0.1876    6.520

   165   8.2934  5   122   2073.632    46.82            193.20             80.49                     150.00    0.024    4.149   0.2328    8.864

   166   7.5825  6   156   2081.214    40.98            173.22             80.87                     150.00    0.024    9.736   0.1362    7.706

   167   9.2720  5   146   2090.487    41.49            170.93             80.47                     150.00    0.024   11.197   0.2601   11.307

   168   7.9126  6   145   2098.399    43.82            188.47             81.13                     150.00    0.024    4.170   0.2354    7.925

   169   7.1851  5   125   2105.584    43.11            202.61             82.46                     150.00    0.024    6.060   0.2291    3.147

   170   6.6338  6   126   2112.218    39.44            205.75             83.92                     150.00    0.024    3.692   0.1998    6.223

   171   6.6373  5   127   2118.855    33.42            190.04             85.05                     150.00    0.024    9.788   0.2204    6.753

   172   6.2723  5   117   2125.128    29.69            173.98             85.42                     150.00    0.024   12.945   0.0973   10.013

   173   8.8758  4   112   2134.003    31.99            169.22             84.10                     150.00    0.024   12.979   0.0755   10.129

   174  13.7783  6   200   2147.782    27.57            156.10             84.99                     150.00    0.024    8.434   0.1128   11.676

   175  18.3518  5   161   2166.133    21.51            148.13             87.32                     150.00    0.024    1.982   0.1053    4.592

   176  25.1561  4   138   2191.290    15.33            144.69             90.42                     150.00    0.024    4.140   0.0808    4.287

   177  38.1464  3    99   2229.436    10.38            145.43             93.34                     150.00    0.024   11.441   0.0753    5.109

   178  59.2541  3   101   2288.690     6.73            147.13             95.63                     150.00    0.024   26.253   0.0717    5.685

   179  93.5565  3   104   2382.247     4.10            148.39             97.31                     150.00    0.024   53.112   0.0651    6.023

   180 143.7534  3   106   2526.000     2.31            149.14             98.48                     150.00    0.024   94.690   0.0547    6.467

Time steps : 180/190, step size: 14.0333, 22.0445

Running simulation [simumpi]: stflu021 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 5.93s

   162   7.8315  4  1047   2009.114    49.79            157.14             75.94                     150.00    0.010    9.674   0.1010    6.872

   163  10.9215  4   215   2020.035    51.31            160.17             75.74                     150.00    0.010    7.051   0.1791   11.189

   164  11.6140  6   474   2031.649    55.56            190.88             77.45                     150.00    0.010    4.426   0.3377    5.690

   165   8.3356  6   302   2039.985    53.39            195.46             78.54                     150.00    0.010    5.312   0.1773    2.815

   166   8.9143  6   313   2048.899    49.80            189.90             79.22                     150.00    0.010    8.724   0.2394   12.422

   167   8.0126  6   827   2056.912    46.54            175.11             79.00                     150.00    0.010   13.215   0.1882   11.002

   168   8.2927  4   459   2065.204    45.82            158.12             77.53                     150.00    0.010   12.206   0.0991   10.406

   169  11.6506 10   390   2076.855    48.49            175.90             78.39                     150.00    0.010    2.748   0.2424   10.254

   170  10.3908  6   272   2087.246    49.17            210.68             81.08                     150.00    0.010    5.445   0.3051    4.486

   171   7.9915  6   254   2095.237    41.23            199.00             82.84                     150.00    0.010    6.177   0.2148    6.330

   172   7.6679  4   162   2102.905    35.38            171.76             82.92                     150.00    0.010   13.824   0.0696   12.724

   173  11.4288  5   256   2114.334    37.12            163.04             81.45                     150.00    0.010   15.106   0.0902   16.381

   174  15.4318  6   292   2129.766    36.36            182.97             83.42                     150.00    0.010    3.480   0.4123    5.379

   175   9.6053  6   238   2139.371    29.23            172.28             85.49                     150.00    0.010    3.469   0.2143    2.002

   176   9.2288  6   256   2148.600    22.76            152.32             87.00                     150.00    0.010    5.951   0.0635    5.036

   177  15.1270  5   239   2163.727    18.98            149.49             88.74                     150.00    0.010    5.934   0.0464   10.943

   178  23.7468  5   274   2187.474    16.00            149.71             90.35                     150.00    0.010    4.095   0.0731   11.176

   179  37.0208  4   216   2224.494    12.13            147.66             92.41                     150.00    0.010   10.415   0.1303    5.885

   180  46.2251  3   174   2270.719     8.22            147.00             94.70                     150.00    0.010   17.822   0.0830    5.598



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   181  69.4465  3   173   2340.166     5.34            147.94             96.52                     150.00    0.010   35.533   0.0753    5.881

   182 107.8914  4   230   2448.057     3.23            148.84             97.88                     150.00    0.010   66.347   0.0664    6.103

   183  77.9426  3   173   2526.000     2.31            149.16             98.48                     150.00    0.010   51.933   0.0334    3.502

Time steps : 183/195, step size: 13.8033, 19.872

Running simulation [simuapp]: stflu033 baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 0.73s



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.503s  90.24%      

|- Newton                                 0.494s  |- 98.07%   

  |- FluxJac                              0.158s    |- 31.95% 

  |- ScdAcc                               0.093s    |- 18.77% 

  |- Update                               0.091s    |- 18.45% 

  |- update_dev                           0.047s    |- 9.43%  

  |- Reaction                             0.033s    |- 6.78%  

  |- Precond                              0.025s    |- 5.06%  

  |- Solver                               0.022s    |- 4.46%  

  |- PerfJac                              0.006s    |- 1.13%  

  |- alignvar                             0.003s    |- 0.69%  

  |- Residual                             0.002s    |- 0.44%  

  |- SanitizeJac                          0.001s    |- 0.19%  

  |- HeatLoss                             0.000s    |- 0.02%  

|- Logging                                0.007s  |- 1.47%    

|- Output                                 0.006s  |- 1.22%    

|- Input                                  0.000s  |- 0.05%    

Initialization                            0.054s  9.76%       

|- execution                              0.052s  |- 96.19%   

------------------------------------------------------------

TOTAL                                     0.558s

============================================================



Time steps : 120/122, step size: 0.00555556, 0.00352775

Running simulation [simumpi]: stflu033 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 0.75s

    92 9.02e-03  4     4      0.443    3e-11     2.84     0.01    9e+10   100.00              3.06     0.01    0.034    0.963   0.0678   30.096

    93 9.00e-03  4     4      0.452    3e-11     2.80     0.01    9e+10   100.00              3.06     0.01    0.033    0.836   0.1496   30.755

    94 2.96e-03  4     4 1    0.455    3e-11     2.67     0.01    9e+10   100.00              3.06     0.01    0.033    0.285   0.0505    9.931

    95 4.79e-03  3     3      0.459    3e-11     2.84     0.01    9e+10   100.00              3.06     0.01    0.033    0.541   0.0681   13.833

    96 6.92e-03  4     4      0.466    3e-11     3.05     0.01    1e+11   100.00              3.06     0.01    0.033    1.155   0.0556   23.623

    97 7.88e-03  3     3      0.474    3e-11     3.11     0.01    1e+11   100.00              3.06     0.01    0.032    0.891   0.0441   31.846

    98 7.61e-03  3     3      0.482    3e-11     2.91     0.01    1e+11   100.00              3.06     0.01    0.032    0.642   0.0542   26.667

    99 8.13e-03  4     4      0.490    4e-11     3.27     0.01    9e+10   100.00              3.06     0.01    0.031    1.997   0.0473   24.902

   100 9.00e-03  4     4      0.499    3e-11     2.64     0.01    9e+10   100.00              3.06     0.01    0.031    2.685   0.1333   30.976

   101 8.84e-03  5     5      0.508    3e-11     2.73     0.01    9e+10   100.00              3.06     0.01    0.031    0.349   0.1538   34.428

   102 8.15e-03  4     4      0.516    3e-11     3.02     0.01    1e+11   100.00              3.06     0.01    0.030    1.291   0.0878   26.596

   103 8.71e-03  4     4      0.525    4e-11     3.34     0.01    1e+11   100.00              3.06     0.01    0.029    1.884   0.0824   32.621

   104 8.30e-03  6     7      0.533    3e-11     2.85     0.01    9e+10   100.00              3.06     0.01    0.078    0.733   0.0202   31.310

   105 8.10e-03  4     4      0.541    3e-11     3.00     0.01    9e+10   100.00              3.06     0.01    0.078    1.150   0.0406   27.981

   106 8.42e-03  3     3      0.549    3e-11     2.64     0.01    9e+10   100.00              3.06     0.01    0.078    2.637   0.1385   26.150

   107 9.09e-03  4     4      0.559    3e-11     3.04     0.01    9e+10   100.00              3.06     0.01    0.078    0.867   0.1584   35.072

   108 8.29e-03  6     7      0.567    3e-11     3.00     0.01    9e+10   100.00              3.06     0.01    0.078    1.231   0.0816   30.695

   109 8.18e-03  4     4      0.575    3e-11     2.82     0.01    9e+10   100.00              3.06     0.01    0.078    0.431   0.0375   29.526

   110 8.25e-03  3     3      0.583    3e-11     3.11     0.01    9e+10   100.00              3.06     0.01    0.078    1.786   0.0656   32.047

   111 7.94e-03  4     4      0.591    4e-11     3.17     0.01    8e+10   100.00              3.06     0.01    0.078    0.819   0.0945   28.920

   112 8.11e-03  6     7      0.599    3e-11     2.59     0.01    9e+10   100.00              3.06     0.01    0.078    2.400   0.1420   23.620

   113 9.23e-03  5     5      0.609    3e-11     2.83     0.01    9e+10   100.00              3.06     0.01    0.078    0.499   0.1436   31.912

   114 8.91e-03  4     4      0.617    4e-11     3.32     0.01    9e+10   100.00              3.06     0.01    0.078    2.226   0.0858   32.182

   115 8.55e-03  5     5      0.626    3e-11     2.90     0.01    9e+10   100.00              3.06     0.01    0.078    0.347   0.0632   30.277

   116 8.51e-03  3     3      0.635    4e-11     2.98     0.01    8e+10   100.00              3.06     0.01    0.078    1.397   0.0477   29.293

   117 8.62e-03  4     4      0.643    3e-11     2.60     0.01    8e+10   100.00              3.06     0.01    0.078    3.265   0.1494   27.580

   118 9.04e-03  6     6      0.652    3e-11     3.07     0.01    9e+10   100.00              3.06     0.01    0.078    0.810   0.1606   26.836

   119 9.62e-03  3     3      0.662    3e-11     3.00     0.01    9e+10   100.00              3.06     0.01    0.078    1.544   0.0883   30.169

   120 4.86e-03  3     3      0.667    3e-11     2.71     0.01    9e+10   100.00              3.06     0.01    0.078    1.204   0.0258   17.444

Time steps : 120/122, step size: 0.00555556, 0.00352775

Running simulation [simumpi]: stflu033 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 0.56s

    92 9.02e-03  4    24      0.443    3e-11     2.84     0.01    9e+10   100.00              3.06     0.01    0.034    0.963   0.0678   30.096

    93 9.00e-03  4    24      0.452    3e-11     2.80     0.01    9e+10   100.00              3.06     0.01    0.033    0.836   0.1496   30.755

    94 2.96e-03  4    24 1    0.455    3e-11     2.67     0.01    9e+10   100.00              3.06     0.01    0.033    0.285   0.0505    9.931

    95 4.79e-03  3    18      0.459    3e-11     2.84     0.01    9e+10   100.00              3.06     0.01    0.033    0.541   0.0681   13.833

    96 6.92e-03  4    24      0.466    3e-11     3.05     0.01    1e+11   100.00              3.06     0.01    0.033    1.155   0.0556   23.623

    97 7.88e-03  3    18      0.474    3e-11     3.11     0.01    1e+11   100.00              3.06     0.01    0.032    0.891   0.0441   31.846

    98 7.61e-03  3    18      0.482    3e-11     2.91     0.01    1e+11   100.00              3.06     0.01    0.032    0.642   0.0542   26.667

    99 8.13e-03  4    22      0.490    4e-11     3.27     0.01    9e+10   100.00              3.06     0.01    0.031    1.997   0.0473   24.902

   100 9.00e-03  4    24      0.499    3e-11     2.64     0.01    9e+10   100.00              3.06     0.01    0.031    2.685   0.1333   30.976

   101 8.84e-03  5    30      0.508    3e-11     2.73     0.01    9e+10   100.00              3.06     0.01    0.031    0.349   0.1538   34.428

   102 8.15e-03  4    24      0.516    3e-11     3.02     0.01    1e+11   100.00              3.06     0.01    0.030    1.291   0.0878   26.596

   103 8.71e-03  4    24      0.525    4e-11     3.34     0.01    1e+11   100.00              3.06     0.01    0.029    1.884   0.0824   32.621

   104 8.30e-03  6    41      0.533    3e-11     2.85     0.01    9e+10   100.00              3.06     0.01    0.078    0.733   0.0202   31.310

   105 8.10e-03  4    24      0.541    3e-11     3.00     0.01    9e+10   100.00              3.06     0.01    0.078    1.150   0.0406   27.981

   106 8.42e-03  3    18      0.549    3e-11     2.64     0.01    9e+10   100.00              3.06     0.01    0.078    2.637   0.1385   26.150

   107 9.09e-03  4    24      0.559    3e-11     3.04     0.01    9e+10   100.00              3.06     0.01    0.078    0.867   0.1584   35.072

   108 8.29e-03  6    37      0.567    3e-11     3.00     0.01    9e+10   100.00              3.06     0.01    0.078    1.231   0.0816   30.695

   109 8.18e-03  4    24      0.575    3e-11     2.82     0.01    9e+10   100.00              3.06     0.01    0.078    0.431   0.0375   29.526

   110 8.25e-03  3    18      0.583    3e-11     3.11     0.01    9e+10   100.00              3.06     0.01    0.078    1.786   0.0656   32.047

   111 7.94e-03  4    24      0.591    4e-11     3.17     0.01    8e+10   100.00              3.06     0.01    0.078    0.819   0.0945   28.920

   112 8.11e-03  6    40      0.599    3e-11     2.59     0.01    9e+10   100.00              3.06     0.01    0.078    2.400   0.1420   23.620

   113 9.23e-03  5    30      0.609    3e-11     2.83     0.01    9e+10   100.00              3.06     0.01    0.078    0.499   0.1436   31.912

   114 8.91e-03  4    24      0.617    4e-11     3.32     0.01    9e+10   100.00              3.06     0.01    0.078    2.226   0.0858   32.182

   115 8.55e-03  5    27      0.626    3e-11     2.90     0.01    9e+10   100.00              3.06     0.01    0.078    0.347   0.0632   30.277

   116 8.51e-03  3    18      0.635    4e-11     2.98     0.01    8e+10   100.00              3.06     0.01    0.078    1.397   0.0477   29.293

   117 8.62e-03  4    24      0.643    3e-11     2.60     0.01    8e+10   100.00              3.06     0.01    0.078    3.265   0.1494   27.580

   118 9.04e-03  6    33      0.652    3e-11     3.07     0.01    9e+10   100.00              3.06     0.01    0.078    0.810   0.1606   26.836

   119 9.62e-03  3    18      0.662    3e-11     3.00     0.01    9e+10   100.00              3.06     0.01    0.078    1.544   0.0883   30.169

   120 4.86e-03  3    18      0.667    3e-11     2.71     0.01    9e+10   100.00              3.06     0.01    0.078    1.204   0.0258   17.444

Time steps : 120/122, step size: 0.00555556, 0.00352775

Running simulation [simumpi]: stflu033 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 0.47s

    92 9.02e-03  4    53      0.443    3e-11     2.84     0.01    9e+10   100.00              3.06     0.01    0.033    0.963   0.0678   30.096

    93 9.00e-03  4    50      0.452    3e-11     2.80     0.01    9e+10   100.00              3.06     0.01    0.033    0.836   0.1496   30.755

    94 2.96e-03  4    49 1    0.455    3e-11     2.67     0.01    9e+10   100.00              3.06     0.01    0.033    0.285   0.0505    9.931

    95 4.79e-03  3    38      0.459    3e-11     2.84     0.01    9e+10   100.00              3.06     0.01    0.033    0.541   0.0681   13.833

    96 6.92e-03  4    54      0.466    3e-11     3.05     0.01    1e+11   100.00              3.06     0.01    0.032    1.155   0.0556   23.622

    97 7.88e-03  4    53      0.474    3e-11     3.11     0.01    1e+11   100.00              3.06     0.01    0.032    0.891   0.0441   31.846

    98 7.61e-03  3    39      0.482    3e-11     2.91     0.01    1e+11   100.00              3.06     0.01    0.031    0.642   0.0542   26.667

    99 8.13e-03  4    48      0.490    4e-11     3.27     0.01    9e+10   100.00              3.06     0.01    0.031    1.997   0.0473   24.902

   100 9.00e-03  4    52      0.499    3e-11     2.64     0.01    9e+10   100.00              3.06     0.01    0.031    2.685   0.1333   30.976

   101 8.84e-03  5    60      0.508    3e-11     2.73     0.01    9e+10   100.00              3.06     0.01    0.030    0.349   0.1538   34.428

   102 8.15e-03  4    48      0.516    3e-11     3.02     0.01    1e+11   100.00              3.06     0.01    0.030    1.291   0.0878   26.596

   103 8.71e-03  4    47      0.525    4e-11     3.34     0.01    1e+11   100.00              3.06     0.01    0.029    1.884   0.0824   32.621

   104 8.30e-03  6    84      0.533    3e-11     2.85     0.01    9e+10   100.00              3.06     0.01    0.078    0.733   0.0202   31.310

   105 8.10e-03  4    49      0.541    3e-11     3.00     0.01    9e+10   100.00              3.06     0.01    0.078    1.150   0.0406   27.981

   106 8.42e-03  3    37      0.549    3e-11     2.64     0.01    9e+10   100.00              3.06     0.01    0.078    2.637   0.1385   26.150

   107 9.09e-03  4    48      0.559    3e-11     3.04     0.01    9e+10   100.00              3.06     0.01    0.078    0.867   0.1584   35.072

   108 8.29e-03  6    75      0.567    3e-11     3.00     0.01    9e+10   100.00              3.06     0.01    0.078    1.231   0.0816   30.695

   109 8.18e-03  4    48      0.575    3e-11     2.82     0.01    9e+10   100.00              3.06     0.01    0.078    0.431   0.0375   29.526

   110 8.25e-03  3    36      0.583    3e-11     3.11     0.01    9e+10   100.00              3.06     0.01    0.078    1.786   0.0656   32.047

   111 7.94e-03  4    46      0.591    4e-11     3.17     0.01    8e+10   100.00              3.06     0.01    0.078    0.819   0.0945   28.920

   112 8.11e-03  6    81      0.599    3e-11     2.59     0.01    9e+10   100.00              3.06     0.01    0.078    2.400   0.1420   23.621

   113 9.23e-03  5    60      0.609    3e-11     2.83     0.01    9e+10   100.00              3.06     0.01    0.078    0.499   0.1436   31.912

   114 8.91e-03  4    48      0.617    4e-11     3.32     0.01    9e+10   100.00              3.06     0.01    0.078    2.226   0.0858   32.183

   115 8.55e-03  5    55      0.626    3e-11     2.90     0.01    9e+10   100.00              3.06     0.01    0.078    0.347   0.0632   30.277

   116 8.51e-03  3    33      0.635    4e-11     2.98     0.01    8e+10   100.00              3.06     0.01    0.078    1.397   0.0477   29.293

   117 8.62e-03  4    46      0.643    3e-11     2.60     0.01    8e+10   100.00              3.06     0.01    0.078    3.265   0.1494   27.580

   118 9.04e-03  6    67      0.652    3e-11     3.07     0.01    9e+10   100.00              3.06     0.01    0.078    0.809   0.1606   26.836

   119 9.62e-03  3    35      0.662    3e-11     3.00     0.01    9e+10   100.00              3.06     0.01    0.078    1.544   0.0883   30.169

   120 4.86e-03  3    34      0.667    3e-11     2.71     0.01    9e+10   100.00              3.06     0.01    0.078    1.203   0.0258   17.446

Time steps : 120/122, step size: 0.00555556, 0.00352774

Running simulation [simuapp]: stsmo088 baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 8.89s

   173   0.6046  1     1      2.500                      1e-04            100.00                      1e-04    0.012  1.4e-07 1.09e-14  5.8e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  8.638s  99.03%      

|- Newton                                 8.625s  |- 99.85%   

  |- FluxJac                              2.555s    |- 29.62% 

  |- Update                               2.489s    |- 28.86% 

  |- update_dev                           1.590s    |- 18.44% 

  |- ScdAcc                               1.383s    |- 16.04% 

  |- Precond                              0.192s    |- 2.23%  

  |- Solver                               0.185s    |- 2.14%  

  |- alignvar                             0.066s    |- 0.76%  

  |- Residual                             0.046s    |- 0.54%  

  |- PerfJac                              0.016s    |- 0.18%  

  |- SanitizeJac                          0.013s    |- 0.15%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Logging                                0.027s  |- 0.31%    

|- Output                                 0.008s  |- 0.09%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.085s  0.97%       

|- execution                              0.070s  |- 82.17%   

------------------------------------------------------------

TOTAL                                     8.723s

============================================================



Time steps : 173/255, step size: 0.0144509, 0.0691969

Running simulation [simumpi]: stsmo088 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 8.98s

===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   151 2.70e-03  2     2 1    0.739    7e-06             1e-04             95.44                      1e-04    0.012    0.025   0.0147  2.1e-05

   152 5.75e-03  5     5      0.744    6e-06             1e-04             95.58                      1e-04    0.012    0.052   0.0281  4.4e-05

   153 3.77e-03  3     3 1    0.748    6e-06             1e-04             95.70                      1e-04    0.012    0.031   0.0191  2.9e-05

   154 7.79e-03  7     8      0.756    6e-06             1e-04             95.98                      1e-04    0.012    0.056   0.0385  5.9e-05

   155 1.48e-03  2     2 2    0.757    6e-06             1e-04             96.03                      1e-04    0.012    0.012   0.0101  1.1e-05

   156 3.24e-03  4     4      0.761    6e-06             1e-04             96.16                      1e-04    0.012    0.023   0.0200  2.4e-05

   157 6.68e-03  7     8      0.767    5e-06             1e-04             96.48                      1e-04    0.012    0.036   0.0345  4.9e-05

   158 1.27e-03  2     2 2    0.769    5e-06             1e-04             96.55                      1e-04    0.012    0.011   0.0088  9.4e-06

   159 2.80e-03  3     3      0.771    5e-06             1e-04             96.71                      1e-04    0.012    0.020   0.0179  2.1e-05

   160 1.95e-03  3     3 1    0.773    5e-06             1e-04             96.86                      1e-04    0.012    0.014   0.0130  1.4e-05

   161 4.18e-03  6     7      0.778    4e-06             1e-04             97.24                      1e-04    0.012    0.028   0.0254  3.0e-05

   162 8.35e-03  8     9      0.786    2e-06             1e-04             98.43                      1e-04    0.012    0.043   0.0423  6.0e-05

   163 4.18e-03  7     8 1    0.790    8e-07             1e-04             99.46                      1e-04    0.012    0.013   0.0114  3.0e-05

   164 7.95e-04  3     3 2    0.791    6e-07             1e-04             99.57                      1e-04    0.012    0.010   0.0083  5.6e-06

   165 1.76e-03  3     3      0.793    5e-07             1e-04             99.63                      1e-04    0.012    0.006   0.0044  1.2e-05

   166 3.98e-03  2     2      0.797    2e-07             1e-04             99.84                      1e-04    0.012    0.002   0.0016  2.8e-05

   167 9.20e-03  2     2      0.806    4e-08             1e-04             99.97                      1e-04    0.012  9.5e-04 8.63e-04  6.4e-05

   168   0.0213  2     2      0.827    2e-09             1e-04            100.00                      1e-04    0.012  1.9e-04 1.65e-04  1.4e-04

   169   0.0497  2     2      0.877    6e-11             1e-04            100.00                      1e-04    0.012  1.3e-05 1.07e-05  3.1e-04

   170   0.1160  1     1      0.993    5e-13             1e-04            100.00                      1e-04    0.012  4.5e-07 2.55e-07  6.1e-04

   171   0.2707  1     1      1.264    2e-15             1e-04            100.00                      1e-04    0.012  2.4e-07 2.33e-09  1.0e-03

   172   0.6317  1     1      1.895                      1e-04            100.00                      1e-04    0.012  2.8e-07 8.48e-12    0.001

   173   0.6046  1     1      2.500                      1e-04            100.00                      1e-04    0.012  1.4e-07 1.09e-14  5.8e-04

Time steps : 173/255, step size: 0.0144509, 0.0691969

Running simulation [simumpi]: stsmo088 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 7.88s

   232 2.59e-03  5    11      0.747    6e-06             1e-04             95.86                      1e-04    0.013    0.018   0.0137  2.0e-05

   233 1.84e-03  4    10 1    0.749    6e-06             1e-04             95.93                      1e-04    0.013    0.012   0.0108  1.4e-05

   234 4.01e-03  6    14      0.753    6e-06             1e-04             96.10                      1e-04    0.013    0.026   0.0227  3.0e-05

   235 8.92e-04  3     9 2    0.754    6e-06             1e-04             96.14                      1e-04    0.013    0.007   0.0060  6.8e-06

   236 2.00e-03  3     9      0.756    5e-06             1e-04             96.23                      1e-04    0.013    0.014   0.0130  1.5e-05

   237 1.43e-03  3     9 1    0.757    5e-06             1e-04             96.30                      1e-04    0.013    0.012   0.0103  1.1e-05

   238 3.13e-03  5    11      0.760    5e-06             1e-04             96.47                      1e-04    0.013    0.024   0.0205  2.3e-05

   239 2.14e-03  5    11 1    0.763    5e-06             1e-04             96.60                      1e-04    0.013    0.017   0.0147  1.6e-05

   240 1.52e-03  3     8 1    0.764    5e-06             1e-04             96.70                      1e-04    0.013    0.011   0.0105  1.1e-05



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   241 3.31e-03  5    11      0.767    4e-06             1e-04             97.00                      1e-04    0.013    0.023   0.0218  2.4e-05

   242 2.24e-03  3     9 1    0.770    4e-06             1e-04             97.23                      1e-04    0.013    0.016   0.0151  1.7e-05

   243 1.59e-03  3    12 1    0.771    4e-06             1e-04             97.40                      1e-04    0.013    0.014   0.0116  1.2e-05

   244 1.15e-03  3     9 1    0.772    4e-06             1e-04             97.54                      1e-04    0.013    0.010   0.0087  8.4e-06

   245 2.53e-03  4    10      0.775    3e-06             1e-04             98.03                      1e-04    0.013    0.019   0.0180  1.8e-05

   246 5.26e-03  6    13      0.780    1e-06             1e-04             99.29                      1e-04    0.013    0.022   0.0194  3.8e-05

   247   0.0105  3    11      0.791    9e-08             1e-04             99.94                      1e-04    0.013    0.005   0.0041  7.5e-05

   248   0.0239  2     7      0.815    3e-09             1e-04            100.00                      1e-04    0.013  4.8e-04 3.88e-04  1.6e-04

   249   0.0557  2     9      0.870    5e-11             1e-04            100.00                      1e-04    0.013  1.8e-05 1.48e-05  3.5e-04

   250   0.1299  1     3      1.000    3e-13             1e-04            100.00                      1e-04    0.013  2.8e-07 2.29e-07  6.8e-04

   251   0.3030  1     3      1.303                      1e-04            100.00                      1e-04    0.013  1.8e-09 1.46e-09    0.001

   252   0.7070  1     3      2.010                      1e-04            100.00                      1e-04    0.013  2.2e-10 1.45e-10    0.001

   253   0.4899  1     3      2.500                      1e-04            100.00                      1e-04    0.013  2.1e-10 1.44e-10  4.7e-04

Time steps : 253/382, step size: 0.00988142, 0.0574438

Running simulation [simumpi]: stsmo088 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 4.78s

   220 2.72e-03  5    23 1    0.736    6e-06             1e-04             95.50                      1e-04    0.002    0.025   0.0177  2.1e-05

   221 5.68e-03  3     8      0.742    6e-06             1e-04             95.71                      1e-04    0.002    0.048   0.0306  4.4e-05

   222 3.67e-03  5    26 1    0.746    6e-06             1e-04             95.85                      1e-04    0.002    0.026   0.0225  2.8e-05

   223 7.44e-03 12    17      0.753    5e-06             1e-04             96.21                      1e-04    0.002    0.042   0.0397  5.7e-05

   224 8.27e-04  3    19 2    0.754    5e-06             1e-04             96.25                      1e-04    0.002    0.007   0.0057  6.3e-06

   225 1.86e-03  3    22      0.756    5e-06             1e-04             96.35                      1e-04    0.002    0.015   0.0129  1.4e-05

   226 1.33e-03  4    21 1    0.757    5e-06             1e-04             96.42                      1e-04    0.002    0.012   0.0099  1.0e-05

   227 2.91e-03  4    21      0.760    5e-06             1e-04             96.59                      1e-04    0.002    0.022   0.0196  2.2e-05

   228 2.00e-03  2     7 1    0.762    5e-06             1e-04             96.73                      1e-04    0.002    0.015   0.0137  1.5e-05

   229 4.28e-03  6    25      0.766    4e-06             1e-04             97.14                      1e-04    0.002    0.029   0.0266  3.2e-05

   230 2.83e-03  5    22 1    0.769    4e-06             1e-04             97.45                      1e-04    0.002    0.021   0.0183  2.1e-05

   231 5.89e-03  7    12      0.775    2e-06             1e-04             98.38                      1e-04    0.002    0.033   0.0317  4.3e-05

   232 1.12e-03  4    22 2    0.776    2e-06             1e-04             98.73                      1e-04    0.002    0.010   0.0079  8.2e-06

   233 2.49e-03  3    21      0.779    5e-07             1e-04             99.62                      1e-04    0.002    0.007   0.0056  1.8e-05

   234 5.59e-03  1     5      0.784    8e-08             1e-04             99.94                      1e-04    0.002    0.003   0.0020  4.0e-05

   235   0.0129  3    33      0.797    5e-09             1e-04            100.00                      1e-04    0.002  4.1e-04 3.35e-04  9.1e-05

   236   0.0300  2    24      0.827    1e-10             1e-04            100.00                      1e-04    0.002  2.5e-05 2.02e-05  2.0e-04

   237   0.0699  1     9      0.897    1e-12             1e-04            100.00                      1e-04    0.002  6.4e-07 5.14e-07  4.3e-04

   238   0.1631  1    10      1.060    6e-15             1e-04            100.00                      1e-04    0.002  6.8e-09 5.47e-09  7.9e-04

   239   0.3807  1    10      1.441                      1e-04            100.00                      1e-04    0.002  2.0e-11 2.28e-11    0.001

   240   0.8882  1    10      2.329                      1e-04            100.00                      1e-04    0.002  9.1e-12 1.21e-13    0.001



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   241   0.1710  1    10      2.500                      1e-04            100.00                      1e-04    0.002  2.7e-12 1.85e-14  1.7e-04

Time steps : 241/360, step size: 0.0103734, 0.0636836

Running simulation [simuapp]: stsmo097 baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 1.75s

    45   1.0693  3     3      5.000    3e-07             1e-04             99.82                      1e-04    0.015    0.302   0.0216  1.6e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.484s  94.88%      

|- Newton                                 1.480s  |- 99.76%   

  |- Update                               0.440s    |- 29.76% 

  |- FluxJac                              0.412s    |- 27.84% 

  |- update_dev                           0.278s    |- 18.80% 

  |- ScdAcc                               0.244s    |- 16.46% 

  |- Precond                              0.035s    |- 2.33%  

  |- Solver                               0.033s    |- 2.23%  

  |- alignvar                             0.012s    |- 0.79%  

  |- Residual                             0.008s    |- 0.57%  

  |- PerfJac                              0.002s    |- 0.16%  

  |- SanitizeJac                          0.002s    |- 0.16%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Logging                                0.002s  |- 0.16%    

|- Output                                 0.002s  |- 0.13%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.080s  5.12%       

|- execution                              0.067s  |- 83.89%   

------------------------------------------------------------

TOTAL                                     1.563s

============================================================



Time steps : 45/49, step size: 0.111111, 0.301545

Running simulation [simumpi]: stsmo097 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 1.89s

    24 1.76e-03  8     9      0.030    1e-04                                                          1e-04    0.000    3.798   0.0539  4.7e-04

    25 2.64e-03 14    15      0.033    1e-04                                                          1e-04    0.000    5.562   0.0615  6.3e-04

    26 2.26e-03 10    11      0.035    1e-04                                                          1e-04    0.000    5.427   0.0529  5.2e-04

    27 2.72e-03 13    14      0.038    1e-04                                                          1e-04    0.000    6.766   0.0569  5.4e-04

    28 2.51e-03 11    12      0.040    1e-04                                                          1e-04    0.000    6.836   0.0536  4.4e-04

    29 2.74e-03 13    14      0.043    1e-04                                                          1e-04    0.000    7.836   0.0557  3.6e-04

    30 2.53e-03 11    12      0.045    1e-04             5e-06              3.61                      1e-04    0.031    7.809   0.0520  2.3e-04



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    31 2.76e-03  4     4      0.048    1e-04             3e-05             17.96                      1e-04    0.030    8.300   0.0389  1.9e-04

    32 1.84e-03  3     3      0.050    1e-04             4e-05             27.94                      1e-04    0.029    4.723   0.0184  1.0e-04

    33 3.82e-03  3     3      0.054    8e-05             6e-05             41.31                      1e-04    0.029    7.245   0.0281  1.5e-04

    34 7.50e-03  4     4      0.061    7e-05             8e-05             54.06                      1e-04    0.028    9.144   0.0268  3.5e-04

    35   0.0148  3     3      0.076    5e-05             9e-05             65.29                      1e-04    0.026   10.863   0.0301  7.1e-04

    36   0.0238  3     3      0.100    4e-05             1e-04             73.85                      1e-04    0.025   10.097   0.0337  9.9e-04

    37   0.0454  4     4      0.145    3e-05             1e-04             81.65                      1e-04    0.023   10.148   0.0440    0.001

    38   0.0819  4     4      0.227    2e-05             1e-04             87.76                      1e-04    0.021    8.780   0.0517    0.002

    39   0.1422  4     4      0.370    1e-05             1e-04             92.16                      1e-04    0.020    6.949   0.0564    0.002

    40   0.2411  4     4      0.611    7e-06             1e-04             95.21                      1e-04    0.018    5.125   0.0593    0.003

    41   0.4033  4     4      1.014    4e-06             1e-04             97.23                      1e-04    0.017    3.598   0.0613    0.003

    42   0.6681  4     4      1.682    2e-06             1e-04             98.50                      1e-04    0.016    2.363   0.0623    0.002

    43   0.8179  4     4      2.500    1e-06             1e-04             99.20                      1e-04    0.015    1.244   0.0501    0.001

    44   1.4307  4     4      3.931    5e-07             1e-04             99.66                      1e-04    0.015    0.830   0.0454  5.7e-04

    45   1.0693  3     3      5.000    3e-07             1e-04             99.82                      1e-04    0.015    0.302   0.0216  1.6e-04

Time steps : 45/49, step size: 0.111111, 0.301545

Running simulation [simumpi]: stsmo097 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 1.10s

    24 1.76e-03  8    43      0.030    1e-04                                                          1e-04    0.000    3.792   0.0539  4.8e-04

    25 2.64e-03 14    59      0.033    1e-04                                                          1e-04    0.000    5.577   0.0615  6.3e-04

    26 2.26e-03 10    47      0.035    1e-04                                                          1e-04    0.000    5.444   0.0529  5.3e-04

    27 2.72e-03 13    54      0.038    1e-04                                                          1e-04    0.000    6.770   0.0569  5.4e-04

    28 2.51e-03 11    55      0.040    1e-04                                                          1e-04    0.000    6.837   0.0536  4.4e-04

    29 2.74e-03 13    51      0.043    1e-04                                                          1e-04    0.000    7.843   0.0557  3.7e-04

    30 2.53e-03 11    44      0.045    1e-04             5e-06              3.61                      1e-04    0.031    7.811   0.0520  2.4e-04



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    31 2.76e-03  4    23      0.048    1e-04             3e-05             17.96                      1e-04    0.030    8.300   0.0389  1.9e-04

    32 1.84e-03  3    21      0.050    1e-04             4e-05             27.94                      1e-04    0.029    4.724   0.0184  1.0e-04

    33 3.82e-03  3    21      0.054    8e-05             6e-05             41.31                      1e-04    0.029    7.245   0.0281  1.5e-04

    34 7.50e-03  4    25      0.061    7e-05             8e-05             54.06                      1e-04    0.028    9.145   0.0268  3.5e-04

    35   0.0148  3    21      0.076    5e-05             9e-05             65.29                      1e-04    0.026   10.863   0.0301  7.1e-04

    36   0.0238  3    21      0.100    4e-05             1e-04             73.85                      1e-04    0.025   10.097   0.0337  9.9e-04

    37   0.0454  4    27      0.145    3e-05             1e-04             81.65                      1e-04    0.023   10.148   0.0440    0.001

    38   0.0819  5    34      0.227    2e-05             1e-04             87.76                      1e-04    0.021    8.780   0.0517    0.002

    39   0.1422  4    26      0.370    1e-05             1e-04             92.16                      1e-04    0.020    6.949   0.0564    0.002

    40   0.2411  5    29      0.611    7e-06             1e-04             95.21                      1e-04    0.018    5.125   0.0593    0.003

    41   0.4033  5    30      1.014    4e-06             1e-04             97.23                      1e-04    0.017    3.598   0.0613    0.003

    42   0.6681  4    23      1.682    2e-06             1e-04             98.50                      1e-04    0.016    2.363   0.0623    0.002

    43   0.8179  4    22      2.500    1e-06             1e-04             99.20                      1e-04    0.015    1.244   0.0501    0.001

    44   1.4308  5    29      3.931    5e-07             1e-04             99.66                      1e-04    0.015    0.830   0.0454  5.7e-04

    45   1.0692  5    28      5.000    3e-07             1e-04             99.82                      1e-04    0.015    0.302   0.0216  1.6e-04

Time steps : 45/49, step size: 0.111111, 0.301546

Running simulation [simumpi]: stsmo097 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 0.90s

    32 2.61e-03 13   181      0.044    1e-04                                                          1e-04    0.000    7.651   0.0564  2.7e-04

    33 2.40e-03  7    81      0.047    1e-04             1e-05              6.86                      1e-04    0.002    7.638   0.0511  1.8e-04

    34 3.24e-03  4    59      0.050    1e-04             4e-05             26.35                      1e-04    0.002    8.661   0.0399  1.8e-04

    35 5.97e-03  4    84      0.056    8e-05             7e-05             45.26                      1e-04    0.002   10.167   0.0385  2.3e-04

    36   0.0111  3    63      0.067    6e-05             9e-05             59.25                      1e-04    0.002   10.989   0.0331  5.4e-04

    37   0.0212  4    79      0.088    4e-05             1e-04             70.21                      1e-04    0.002   11.635   0.0333  9.5e-04

    38   0.0118  4    77      0.100    4e-05             1e-04             74.05                      1e-04    0.002    4.631   0.0166  4.9e-04

    39   0.0247  4    84      0.125    3e-05             1e-04             79.24                      1e-04    0.002    6.577   0.0285  8.5e-04

    40   0.0484  5    93      0.173    2e-05             1e-04             84.66                      1e-04    0.002    7.555   0.0402    0.001

    41   0.0891  4    79      0.262    2e-05             1e-04             89.42                      1e-04    0.002    7.161   0.0494    0.002

    42   0.1564  5   122      0.419    1e-05             1e-04             93.16                      1e-04    0.002    6.001   0.0549    0.002

    43   0.2672  5    92      0.686    6e-06             1e-04             95.81                      1e-04    0.002    4.548   0.0584    0.003

    44   0.4489  5   107      1.135    3e-06             1e-04             97.59                      1e-04    0.002    3.226   0.0608    0.002

    45   0.7453  5   395      1.880    2e-06             1e-04             98.73                      1e-04    0.002    2.091   0.0620    0.002

    46   0.6201  5   688      2.500    1e-06             1e-04             99.23                      1e-04    0.002    0.887   0.0371  7.7e-04

    47   1.1597  5   690      3.660    5e-07             1e-04             99.63                      1e-04    0.002    0.733   0.0398  5.0e-04

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 4.44161e-12) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 4.44161e-12) - this cycle cannot be accepted as converged

[rank 3] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 4.44161e-12) - this cycle cannot be accepted as converged

[rank 2] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 4.44161e-12) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 1.91577e-14) - this cycle cannot be accepted as converged

[rank 2] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 1.91577e-14) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 1.91577e-14) - this cycle cannot be accepted as converged

[rank 3] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 1.91577e-14) - this cycle cannot be accepted as converged

[rank 3] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.64217e-17) - this cycle cannot be accepted as converged

[rank 0] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.64217e-17) - this cycle cannot be accepted as converged

[rank 2] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.64217e-17) - this cycle cannot be accepted as converged

[rank 1] linear solve did not converge: DIVERGED_ITS after 500 iterations (residual norm 2.64217e-17) - this cycle cannot be accepted as converged

    48   1.3403  6  1539      5.000    2e-07             1e-04             99.83                      1e-04    0.002    0.364   0.0264  1.9e-04

Time steps : 48/55, step size: 0.104167, 0.286932

Running simulation [simuapp]: corner baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 2.81s

    78   5.0000  1     3   3650.000    93.81   499.83     1.99     5.33     2.07                               0.000    0.903 1.24e-06  9.6e-05



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.556s  96.85%      

|- Newton                                 2.543s  |- 99.50%   

  |- FluxJac                              0.995s    |- 39.11% 

  |- Update                               0.922s    |- 36.26% 

  |- ScdAcc                               0.196s    |- 7.72%  

  |- Solver                               0.175s    |- 6.86%  

  |- update_dev                           0.142s    |- 5.57%  

  |- Precond                              0.061s    |- 2.41%  

  |- Residual                             0.017s    |- 0.65%  

  |- alignvar                             0.008s    |- 0.33%  

  |- SanitizeJac                          0.004s    |- 0.17%  

  |- HeatLoss                             0.002s    |- 0.09%  

  |- PerfJac                              0.001s    |- 0.05%  

|- Output                                 0.005s  |- 0.21%    

|- Logging                                0.002s  |- 0.07%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.083s  3.15%       

|- execution                              0.077s  |- 92.52%   

------------------------------------------------------------

TOTAL                                     2.639s

============================================================



Time steps : 78/78, step size: 46.7949, 11.3162

Running simulation [simumpi]: corner np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 2.82s

    57  50.0000  1     6   2645.000    95.40   508.28     2.00     5.33     2.06                               0.000   11.885 1.22e-05    0.001

    58  50.0000  1     6   2695.000    95.31   507.81     2.00     5.33     2.06                               0.000   11.704 1.23e-05    0.001

    59  50.0000  1     6   2745.000    95.22   507.34     2.00     5.33     2.06                               0.000   11.528 1.23e-05    0.001

    60  50.0000  1     6   2795.000    95.14   506.88     2.00     5.33     2.06                               0.000   11.357 1.23e-05    0.001



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  50.0000  1     6   2845.000    95.05   506.42     2.00     5.33     2.06                               0.000   11.190 1.23e-05    0.001

    62  50.0000  1     6   2895.000    94.97   505.97     2.00     5.33     2.06                               0.000   11.027 1.23e-05    0.001

    63  50.0000  1     6   2945.000    94.88   505.53     2.00     5.33     2.06                               0.000   10.869 1.23e-05    0.001

    64  50.0000  1     6   2995.000    94.80   505.09     2.00     5.33     2.06                               0.000   10.717 1.23e-05    0.001

    65  50.0000  1     6   3045.000    94.72   504.66     2.00     5.33     2.06                               0.000   10.568 1.23e-05    0.001

    66  50.0000  1     6   3095.000    94.64   504.23     2.00     5.33     2.06                               0.000   10.423 1.23e-05    0.001

    67  50.0000  1     6   3145.000    94.56   503.81     1.99     5.33     2.07                               0.000   10.282 1.23e-05    0.001

    68  50.0000  1     6   3195.000    94.48   503.39     1.99     5.33     2.07                               0.000   10.144 1.23e-05    0.001

    69  50.0000  1     6   3245.000    94.41   502.98     1.99     5.33     2.07                               0.000   10.009 1.23e-05    0.001

    70  50.0000  1     6   3295.000    94.33   502.58     1.99     5.33     2.07                               0.000    9.878 1.23e-05    0.001

    71  50.0000  1     6   3345.000    94.25   502.17     1.99     5.33     2.07                               0.000    9.750 1.24e-05    0.002

    72  50.0000  1     6   3395.000    94.18   501.78     1.99     5.33     2.07                               0.000    9.624 1.24e-05    0.001

    73  50.0000  1     6   3445.000    94.11   501.39     1.99     5.33     2.07                               0.000    9.502 1.24e-05    0.001

    74  50.0000  1     6   3495.000    94.03   501.00     1.99     5.33     2.07                               0.000    9.382 1.24e-05  9.9e-04

    75  50.0000  1     6   3545.000    93.96   500.62     1.99     5.33     2.07                               0.000    9.265 1.24e-05    0.002

    76  50.0000  1     6   3595.000    93.89   500.24     1.99     5.33     2.07                               0.000    9.150 1.24e-05  9.7e-04

    77  50.0000  1     6   3645.000    93.82   499.86     1.99     5.33     2.07                               0.000    9.038 1.24e-05  9.6e-04

    78   5.0000  1     3   3650.000    93.81   499.83     1.99     5.33     2.07                               0.000    0.903 1.24e-06  9.6e-05

Time steps : 78/78, step size: 46.7949, 11.3162

Running simulation [simumpi]: corner np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 1.66s

    57  50.0000  1     9   2645.000    95.40   508.28     2.00     5.33     2.06                               0.000   11.885 1.22e-05    0.001

    58  50.0000  1     9   2695.000    95.31   507.81     2.00     5.33     2.06                               0.000   11.704 1.23e-05    0.001

    59  50.0000  1     9   2745.000    95.22   507.34     2.00     5.33     2.06                               0.000   11.528 1.23e-05    0.001

    60  50.0000  1     9   2795.000    95.14   506.88     2.00     5.33     2.06                               0.000   11.357 1.23e-05    0.001



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  50.0000  1     9   2845.000    95.05   506.42     2.00     5.33     2.06                               0.000   11.190 1.23e-05    0.001

    62  50.0000  1     9   2895.000    94.97   505.97     2.00     5.33     2.06                               0.000   11.027 1.23e-05    0.001

    63  50.0000  1     9   2945.000    94.88   505.53     2.00     5.33     2.06                               0.000   10.869 1.23e-05    0.001

    64  50.0000  1     9   2995.000    94.80   505.09     2.00     5.33     2.06                               0.000   10.717 1.23e-05    0.001

    65  50.0000  1     9   3045.000    94.72   504.66     2.00     5.33     2.06                               0.000   10.568 1.23e-05    0.001

    66  50.0000  1     9   3095.000    94.64   504.23     2.00     5.33     2.06                               0.000   10.423 1.23e-05    0.001

    67  50.0000  1     9   3145.000    94.56   503.81     1.99     5.33     2.07                               0.000   10.282 1.23e-05    0.001

    68  50.0000  1     9   3195.000    94.48   503.39     1.99     5.33     2.07                               0.000   10.144 1.23e-05    0.001

    69  50.0000  1     9   3245.000    94.41   502.98     1.99     5.33     2.07                               0.000   10.009 1.23e-05    0.001

    70  50.0000  1     9   3295.000    94.33   502.58     1.99     5.33     2.07                               0.000    9.878 1.23e-05    0.001

    71  50.0000  1     9   3345.000    94.25   502.17     1.99     5.33     2.07                               0.000    9.750 1.24e-05    0.002

    72  50.0000  1     9   3395.000    94.18   501.78     1.99     5.33     2.07                               0.000    9.624 1.24e-05    0.001

    73  50.0000  1     9   3445.000    94.11   501.39     1.99     5.33     2.07                               0.000    9.502 1.24e-05    0.001

    74  50.0000  1     9   3495.000    94.03   501.00     1.99     5.33     2.07                               0.000    9.382 1.24e-05  9.9e-04

    75  50.0000  1     9   3545.000    93.96   500.62     1.99     5.33     2.07                               0.000    9.265 1.24e-05    0.002

    76  50.0000  1     9   3595.000    93.89   500.24     1.99     5.33     2.07                               0.000    9.150 1.24e-05  9.7e-04

    77  50.0000  1     9   3645.000    93.82   499.86     1.99     5.33     2.07                               0.000    9.038 1.24e-05  9.6e-04

    78   5.0000  1     6   3650.000    93.81   499.83     1.99     5.33     2.07                               0.000    0.903 1.24e-06  9.6e-05

Time steps : 78/78, step size: 46.7949, 11.3162

Running simulation [simumpi]: corner np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 1.29s

    57  50.0000  1    19   2645.000    95.40   508.28     2.00     5.33     2.06                               0.000   11.885 1.22e-05    0.001

    58  50.0000  1    19   2695.000    95.31   507.81     2.00     5.33     2.06                               0.000   11.704 1.23e-05    0.001

    59  50.0000  1    19   2745.000    95.22   507.34     2.00     5.33     2.06                               0.000   11.528 1.23e-05    0.001

    60  50.0000  1    19   2795.000    95.14   506.88     2.00     5.33     2.06                               0.000   11.357 1.23e-05    0.001



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

    61  50.0000  1    19   2845.000    95.05   506.42     2.00     5.33     2.06                               0.000   11.190 1.23e-05    0.001

    62  50.0000  1    19   2895.000    94.97   505.97     2.00     5.33     2.06                               0.000   11.027 1.23e-05    0.001

    63  50.0000  1    19   2945.000    94.88   505.53     2.00     5.33     2.06                               0.000   10.869 1.23e-05    0.001

    64  50.0000  1    19   2995.000    94.80   505.09     2.00     5.33     2.06                               0.000   10.717 1.23e-05    0.001

    65  50.0000  1    19   3045.000    94.72   504.66     2.00     5.33     2.06                               0.000   10.568 1.23e-05    0.001

    66  50.0000  1    19   3095.000    94.64   504.23     2.00     5.33     2.06                               0.000   10.423 1.23e-05    0.001

    67  50.0000  1    19   3145.000    94.56   503.81     1.99     5.33     2.07                               0.000   10.282 1.23e-05    0.001

    68  50.0000  1    19   3195.000    94.48   503.39     1.99     5.33     2.07                               0.000   10.144 1.23e-05    0.001

    69  50.0000  1    19   3245.000    94.41   502.98     1.99     5.33     2.07                               0.000   10.009 1.23e-05    0.001

    70  50.0000  1    19   3295.000    94.33   502.58     1.99     5.33     2.07                               0.000    9.878 1.23e-05    0.001

    71  50.0000  1    19   3345.000    94.25   502.17     1.99     5.33     2.07                               0.000    9.750 1.24e-05    0.002

    72  50.0000  1    19   3395.000    94.18   501.78     1.99     5.33     2.07                               0.000    9.624 1.24e-05    0.001

    73  50.0000  1    19   3445.000    94.11   501.39     1.99     5.33     2.07                               0.000    9.502 1.24e-05    0.001

    74  50.0000  1    19   3495.000    94.03   501.00     1.99     5.33     2.07                               0.000    9.382 1.24e-05  9.9e-04

    75  50.0000  1    19   3545.000    93.96   500.62     1.99     5.33     2.07                               0.000    9.265 1.24e-05    0.002

    76  50.0000  1    19   3595.000    93.89   500.24     1.99     5.33     2.07                               0.000    9.150 1.24e-05  9.7e-04

    77  50.0000  1    19   3645.000    93.82   499.86     1.99     5.33     2.07                               0.000    9.038 1.24e-05  9.6e-04

    78   5.0000  1     9   3650.000    93.81   499.83     1.99     5.33     2.07                               0.000    0.903 1.24e-06  9.6e-05

Time steps : 78/78, step size: 46.7949, 11.3162

Running simulation [simuapp]: stflu011 baseline (OMP_NUM_THREADS=1, -novtu)

Elapsed: 0.59s

    10 144.8245  1    15   1095.000   171.12              0.02              0.01                      80.00    0.000    7.015   0.0036  8.9e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.290s  69.69%      

|- Newton                                 0.287s  |- 99.02%   

  |- FluxJac                              0.109s    |- 37.92% 

  |- Update                               0.101s    |- 35.17% 

  |- ScdAcc                               0.027s    |- 9.31%  

  |- update_dev                           0.021s    |- 7.46%  

  |- Solver                               0.017s    |- 5.77%  

  |- Precond                              0.004s    |- 1.49%  

  |- PerfJac                              0.003s    |- 0.97%  

  |- Residual                             0.002s    |- 0.60%  

  |- alignvar                             0.001s    |- 0.45%  

  |- SanitizeJac                          0.000s    |- 0.10%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.001s  |- 0.38%    

|- Logging                                0.000s  |- 0.12%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.126s  30.31%      

|- execution                              0.118s  |- 93.73%   

------------------------------------------------------------

TOTAL                                     0.416s

============================================================



Time steps : 10/10, step size: 109.5, 135.68

Running simulation [simumpi]: stflu011 np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 0.54s

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-27





VTU generation is suppressed.



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   1.0000  1     3      1.000   172.88             2e-04             1e-04                      80.00    0.000    1.391 5.16e-05  1.9e-04

     2   2.3247  1     3      3.325   172.86             7e-04             4e-04                      80.00    0.000    2.256 1.23e-04  3.1e-04

     3   5.3919  1     4      8.717   172.81              0.00             8e-04                      80.00    0.000    3.562 2.87e-04  4.8e-04

     4  12.4627  1     6     21.179   172.73              0.00              0.00                      80.00    0.000    5.476 6.65e-04  7.4e-04

     5  28.6610  1     8     49.840   172.58              0.00              0.00                      80.00    0.000    9.050   0.0015    0.001

     6  65.2998  1    11    115.140   172.34              0.01              0.00                      80.00    0.000   14.799   0.0035    0.002

     7 146.5816  1    15    261.722   171.99              0.01              0.01                      80.00    0.000   21.529   0.0076    0.003

     8 323.4538  1    22    585.176   171.55              0.02              0.01                      80.00    0.000   27.868   0.0156    0.004

     9 365.0000  1    23    950.176   171.23              0.02              0.01                      80.00    0.000   20.664   0.0103    0.003

    10 144.8245  1    15   1095.000   171.12              0.02              0.01                      80.00    0.000    7.015   0.0036  8.9e-04

Time steps : 10/10, step size: 109.5, 135.68

Running simulation [simumpi]: stflu011 np=2 (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 0.45s

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-27





VTU generation is suppressed.

VTU generation is suppressed.



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   1.0000  1     9      1.000   172.88             2e-04             1e-04                      80.00    0.000    1.391 5.16e-05  1.9e-04

     2   2.3247  1    10      3.325   172.86             7e-04             4e-04                      80.00    0.000    2.256 1.23e-04  3.1e-04

     3   5.3919  1    13      8.717   172.81              0.00             8e-04                      80.00    0.000    3.562 2.87e-04  4.8e-04

     4  12.4627  1    16     21.179   172.73              0.00              0.00                      80.00    0.000    5.476 6.65e-04  7.4e-04

     5  28.6610  1    25     49.840   172.58              0.00              0.00                      80.00    0.000    9.050   0.0015    0.001

     6  65.2998  1    32    115.140   172.34              0.01              0.00                      80.00    0.000   14.799   0.0035    0.002

     7 146.5816  1    50    261.722   171.99              0.01              0.01                      80.00    0.000   21.529   0.0076    0.003

     8 323.4538  1    70    585.176   171.55              0.02              0.01                      80.00    0.000   27.868   0.0156    0.004

     9 365.0000  1    69    950.176   171.23              0.02              0.01                      80.00    0.000   20.664   0.0103    0.003

    10 144.8245  1    48   1095.000   171.12              0.02              0.01                      80.00    0.000    7.015   0.0036  8.9e-04

Time steps : 10/10, step size: 109.5, 135.68

Running simulation [simumpi]: stflu011 np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 0.39s

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-27





VTU generation is suppressed.

VTU generation is suppressed.



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   1.0000  1    11      1.000   172.88             2e-04             1e-04                      80.00    0.000    1.391 5.16e-05  1.9e-04

     2   2.3247  1    11      3.325   172.86             7e-04             4e-04                      80.00    0.000    2.256 1.23e-04  3.1e-04

     3   5.3919  1    15      8.717   172.81              0.00             8e-04                      80.00    0.000    3.562 2.87e-04  4.8e-04

     4  12.4627  1    18     21.179   172.73              0.00              0.00                      80.00    0.000    5.476 6.65e-04  7.4e-04

     5  28.6610  1    27     49.840   172.58              0.00              0.00                      80.00    0.000    9.050   0.0015    0.001

     6  65.2998  1    39    115.140   172.34              0.01              0.00                      80.00    0.000   14.799   0.0035    0.002

     7 146.5816  1    57    261.722   171.99              0.01              0.01                      80.00    0.000   21.529   0.0076    0.003

     8 323.4538  1    78    585.176   171.55              0.02              0.01                      80.00    0.000   27.868   0.0156    0.004

     9 365.0000  1    80    950.176   171.23              0.02              0.01                      80.00    0.000   20.664   0.0103    0.003

    10 144.8245  1    58   1095.000   171.12              0.02              0.01                      80.00    0.000    7.015   0.0036  8.9e-04

Time steps : 10/10, step size: 109.5, 135.68

Difference from simuapp (worst relative cumulative well volume)

deck       mechanism                        end (d)             np=1             np=2             np=4

stflu015   corner point, no *NUMERICAL       365.00   7.8e-16     ok   8.4e-14     ok   6.3e-12     ok

stflu018   inactive-block perforation        365.00   7.1e-13     ok   1.3e-08     ok   1.7e-08     ok

lauwerier  thermal front, cut steps          126.64   0.0e+00     ok   7.3e-13     ok   3.3e-10     ok

stflu028   *KRTEMTAB                        2435.00   0.0e+00     ok   5.0e-08     ok   6.7e-08     ok

stflu029   *KRTEMTAB, shut-in wells          820.00   0.0e+00     ok   4.1e-03     ok   1.8e-02  CHECK

stflu019   *NETGROSS, *PVCUTOFF               36.01   1.1e-10     ok   5.4e-10     ok   1.8e-08     ok

stflu010   STG constraint switching            0.38   1.6e+00  CHECK   1.6e+00  CHECK   1.0e+00  SHORT

stflu021   SAGD, BHP-limit demotion         2526.00   0.0e+00     ok   5.1e-03     ok   3.9e-03     ok

stflu033   combustion reactions                0.67   0.0e+00     ok   1.4e-08     ok   2.0e-07     ok

stsmo088   imbibition capillary pressure       2.50   0.0e+00     ok   5.4e-03     ok   1.3e-02  CHECK

stsmo097   rock-fluid interpolation            5.00   0.0e+00     ok   1.3e-07     ok   1.2e-02  CHECK

corner     corner-point grid                3650.00   0.0e+00     ok   2.7e-08     ok   4.8e-08     ok

stflu011   1000-cell Cartesian grid         1095.00   0.0e+00     ok   1.7e-09     ok   4.0e-10     ok

  CHECK: stflu029 simumpi np=4 - worst column vratesc_gasoline1

  CHECK: stflu010 simumpi np=1 - worst column vratesc_gasoline0

  CHECK: stflu010 simumpi np=2 - worst column vratesc_gasoline0

  SHORT: stflu010 simumpi np=4 - rc=0, reached 0.00 days

  CHECK: stsmo088 simumpi np=4 - worst column vratesc_oleic1

  CHECK: stsmo097 simumpi np=4 - worst column vratesc_oleic1



Speed (seconds marching; speedup and efficiency against simumpi np=1)

deck       steps  simuapp    np=1    np=2    np=4   x np=2   x np=4  effic. cells/rank

stflu015      14     0.41    0.31    0.17    0.09    1.80x    3.33x     83%        238

stflu018      65     9.34    9.15    4.97    3.06    1.84x    2.99x     75%        393

lauwerier     10     1.18    1.11    0.58    0.35    1.91x    3.21x     80%        206

stflu028      40     0.11    0.06    0.04    0.03    1.36x    1.89x     47%          7

stflu029     224     5.38    5.25    3.09    2.13    1.70x    2.46x     61%         58

stflu019      11   133.92   96.52   50.90   31.09    1.90x    3.10x     78%      78972

stflu010     278     3.77    3.60    1.90    0.07    1.90x   53.92x   1348%         20

stflu021     178     5.34    5.33    5.56    5.64    0.96x    0.94x     24%         51

stflu033     120     0.56    0.49    0.29    0.19    1.70x    2.55x     64%          5

stsmo088     173     8.72    8.69    7.59    4.48    1.15x    1.94x     49%         62

stsmo097      45     1.56    1.57    0.82    0.62    1.92x    2.52x     63%         62

corner        78     2.64    2.52    1.36    0.97    1.85x    2.60x     65%        306

stflu011      10     0.42    0.27    0.16    0.09    1.74x    2.88x     72%        257

  effic. and cells/rank are at np=4; under ~500 cells per rank the time is collective overhead, not decomposition.

```

Left, the difference from `simuapp` on a log scale: np=1 should sit at the left edge

(roundoff), and anything right of the dashed line is worth chasing. Right, parallel efficiency

against np=1, with 100% the ideal. One row per deck in both; a deck with no marker for a rank count

failed or stopped short there - the tables above say which.

![png]({{ "/assets/images/benchmark_image_78.png" | relative_url }})

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

Elapsed: 32.93s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 31.048s  95.11%      

|- Newton                                30.971s  |- 99.75%   

  |- FluxJac                             12.317s    |- 39.77% 

  |- Update                               9.971s    |- 32.20% 

  |- ScdAcc                               2.906s    |- 9.38%  

  |- update_dev                           2.566s    |- 8.29%  

  |- Solver                               1.897s    |- 6.12%  

  |- Precond                              0.531s    |- 1.71%  

  |- Residual                             0.190s    |- 0.61%  

  |- alignvar                             0.153s    |- 0.49%  

  |- HeatLoss                             0.091s    |- 0.29%  

  |- PerfJac                              0.071s    |- 0.23%  

  |- SanitizeJac                          0.049s    |- 0.16%  

|- Output                                 0.008s  |- 0.03%    

|- Logging                                0.001s  |- 0.00%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            1.597s  4.89%       

|- execution                              1.460s  |- 91.43%   

------------------------------------------------------------

TOTAL                                    32.644s

============================================================



Time steps : 4/4, step size: 0.129382, 0.0269202

Running simulation [simuapp]: scaling baseline (attempt 2/2) (OMP_NUM_THREADS=1, -novtu)

Elapsed: 32.68s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 30.837s  95.12%      

|- Newton                                30.770s  |- 99.78%   

  |- FluxJac                             12.230s    |- 39.75% 

  |- Update                               9.998s    |- 32.49% 

  |- ScdAcc                               2.897s    |- 9.41%  

  |- update_dev                           2.567s    |- 8.34%  

  |- Solver                               1.788s    |- 5.81%  

  |- Precond                              0.523s    |- 1.70%  

  |- Residual                             0.190s    |- 0.62%  

  |- alignvar                             0.155s    |- 0.50%  

  |- HeatLoss                             0.087s    |- 0.28%  

  |- PerfJac                              0.070s    |- 0.23%  

  |- SanitizeJac                          0.042s    |- 0.14%  

|- Output                                 0.008s  |- 0.02%    

|- Logging                                0.001s  |- 0.00%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            1.581s  4.88%       

|- execution                              1.452s  |- 91.82%   

------------------------------------------------------------

TOTAL                                    32.418s

============================================================



Time steps : 4/4, step size: 0.129382, 0.0269202

Running simulation [simumpi]: scaling np=1 (attempt 1/2) (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 33.70s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-27





VTU generation is suppressed.



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1     3      0.100   595.64             20.22              3.28                     720.00    0.000  375.000   0.0027    0.110

     2   0.1167  1     4      0.217   497.87             26.41              5.04                     720.00    0.000  359.596   0.0032    0.122

     3   0.1390  2     8      0.356   426.18             27.34              6.03                     720.00    0.000  376.058   0.0037    0.138

     4   0.1619  2     8      0.518   376.54             25.85              6.42                     720.00    0.000  339.726   0.0034    0.150





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129382, 0.0269202

Running simulation [simumpi]: scaling np=1 (attempt 2/2) (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 34.16s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-27





VTU generation is suppressed.



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1     3      0.100   595.64             20.22              3.28                     720.00    0.000  375.000   0.0027    0.110

     2   0.1167  1     4      0.217   497.87             26.41              5.04                     720.00    0.000  359.596   0.0032    0.122

     3   0.1390  2     8      0.356   426.18             27.34              6.03                     720.00    0.000  376.058   0.0037    0.138

     4   0.1619  2     8      0.518   376.54             25.85              6.42                     720.00    0.000  339.726   0.0034    0.150





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129382, 0.0269202

Running simulation [simumpi]: scaling np=2 (attempt 1/2) (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 18.21s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-27





VTU generation is suppressed.



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1     5      0.100   595.64             20.22              3.28                     720.00    0.000  375.000   0.0027    0.110

     2   0.1167  1     5      0.217   497.87             26.41              5.04                     720.00    0.000  359.596   0.0032    0.122

     3   0.1390  2    10      0.356   426.18             27.34              6.03                     720.00    0.000  376.058   0.0037    0.138

     4   0.1619  2    11      0.518   376.54             25.85              6.42                     720.00    0.000  339.726   0.0034    0.150





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129382, 0.0269202

Running simulation [simumpi]: scaling np=2 (attempt 2/2) (OMP_NUM_THREADS=1, np=2, -novtu)

Elapsed: 18.42s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-27





VTU generation is suppressed.



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1     5      0.100   595.64             20.22              3.28                     720.00    0.000  375.000   0.0027    0.110

     2   0.1167  1     5      0.217   497.87             26.41              5.04                     720.00    0.000  359.596   0.0032    0.122

     3   0.1390  2    10      0.356   426.18             27.34              6.03                     720.00    0.000  376.058   0.0037    0.138

     4   0.1619  2    11      0.518   376.54             25.85              6.42                     720.00    0.000  339.726   0.0034    0.150





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129382, 0.0269202

Running simulation [simumpi]: scaling np=4 (attempt 1/2) (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 11.21s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-27





VTU generation is suppressed.



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1     4      0.100   595.64             20.22              3.28                     720.00    0.000  375.000   0.0027    0.110

     2   0.1167  1     4      0.217   497.87             26.41              5.04                     720.00    0.000  359.596   0.0032    0.122

     3   0.1390  2    10      0.356   426.18             27.34              6.03                     720.00    0.000  376.058   0.0037    0.138

     4   0.1619  2    10      0.518   376.54             25.85              6.42                     720.00    0.000  339.726   0.0034    0.150





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129382, 0.0269202

Running simulation [simumpi]: scaling np=4 (attempt 2/2) (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 11.31s

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-27





VTU generation is suppressed.

VTU generation is suppressed.

VTU generation is suppressed.



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1     4      0.100   595.64             20.22              3.28                     720.00    0.000  375.000   0.0027    0.110

     2   0.1167  1     4      0.217   497.87             26.41              5.04                     720.00    0.000  359.596   0.0032    0.122

     3   0.1390  2    10      0.356   426.18             27.34              6.03                     720.00    0.000  376.058   0.0037    0.138

     4   0.1619  2    10      0.518   376.54             25.85              6.42                     720.00    0.000  339.726   0.0034    0.150





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129382, 0.0269202

Running simulation [simumpi]: scaling np=8 (attempt 1/2) (OMP_NUM_THREADS=1, np=8, -novtu)

Elapsed: 13.23s



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-27





VTU generation is suppressed.

VTU generation is suppressed.

VTU generation is suppressed.

VTU generation is suppressed.

VTU generation is suppressed.



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1     5      0.100   595.64             20.22              3.28                     720.00    0.000  375.000   0.0027    0.110

     2   0.1167  1     5      0.217   497.87             26.41              5.04                     720.00    0.000  359.596   0.0032    0.122

     3   0.1390  2    10      0.356   426.18             27.34              6.03                     720.00    0.000  376.058   0.0037    0.138

     4   0.1619  2     9      0.518   376.54             25.85              6.42                     720.00    0.000  339.726   0.0034    0.150





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129382, 0.0269202

Running simulation [simumpi]: scaling np=8 (attempt 2/2) (OMP_NUM_THREADS=1, np=8, -novtu)

Elapsed: 13.13s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-27





VTU generation is suppressed.



===============================================================================================================================================

--------Time Step--------- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                         C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size             U                                         m3     Cut                                 err                              

 No      day    IT   LIN T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- ----- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

     1   0.1000  1     5      0.100   595.64             20.22              3.28                     720.00    0.000  375.000   0.0027    0.110

     2   0.1167  1     5      0.217   497.87             26.41              5.04                     720.00    0.000  359.596   0.0032    0.122

     3   0.1390  2    10      0.356   426.18             27.34              6.03                     720.00    0.000  376.058   0.0037    0.138

     4   0.1619  2     9      0.518   376.54             25.85              6.42                     720.00    0.000  339.726   0.0034    0.150





TimeLoop terminates due to: reach maximum time step





Time steps : 4/4, step size: 0.129382, 0.0269202

```

![png]({{ "/assets/images/benchmark_image_79.png" | relative_url }})

```
   config  steps   seconds   speedup   effic.  cells/rank   ghosts

  simuapp      4     32.42         -        -           -        -

     np=1      4     31.06     1.00x     100%      202005        0

     np=2      4     16.34     1.90x      95%      101080     2110

     np=4      4      9.53     3.26x      82%       50520     4235

     np=8      4     10.44     2.97x      37%       25610     8325 *

  * more ranks than the 4 fast cores on this CPU - paced by the slow ones, so read the efficiency as the machine's, not the partition's

```

```
Script completed at: 2026-11-27 09:18:50

```
