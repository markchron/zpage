---
layout: default
title: "Benchmark results of resrsim"
date: 2026-11-19
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

Elapsed: 0.71s

    22  55.0000  1   3650.000    47.22              1.86              3.80                      30.05    0.000   39.381 4.29e-04    0.029



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.230s  52.73%      

|- Newton                                 0.205s  |- 88.89%   

  |- Update                               0.078s    |- 38.01% 

  |- FluxJac                              0.050s    |- 24.56% 

  |- ScdAcc                               0.025s    |- 12.33% 

  |- Solver                               0.014s    |- 7.01%  

  |- Precond                              0.010s    |- 5.11%  

  |- update_dev                           0.010s    |- 4.88%  

  |- Residual                             0.005s    |- 2.65%  

  |- SanitizeJac                          0.002s    |- 0.90%  

  |- alignvar                             0.001s    |- 0.69%  

  |- PerfJac                              0.001s    |- 0.66%  

  |- HeatLoss                             0.001s    |- 0.36%  

|- Output                                 0.016s  |- 6.78%    

|- Logging                                0.001s  |- 0.24%    

|- Input                                  0.000s  |- 0.04%    

Initialization                            0.206s  47.27%      

|- execution                              0.188s  |- 91.35%   

------------------------------------------------------------

TOTAL                                     0.437s

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

Elapsed: 1.07s

    79  76.8632  5   3650.000     0.01              4.41             99.73                       4.59    0.044    0.560   0.0041    1.440



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.840s  93.19%      

|- Newton                                 0.821s  |- 97.69%   

  |- Update                               0.238s    |- 28.94% 

  |- FluxJac                              0.208s    |- 25.34% 

  |- Precond                              0.086s    |- 10.49% 

  |- ScdAcc                               0.081s    |- 9.87%  

  |- update_dev                           0.050s    |- 6.09%  

  |- Solver                               0.041s    |- 5.04%  

  |- PerfJac                              0.038s    |- 4.66%  

  |- SanitizeJac                          0.026s    |- 3.21%  

  |- alignvar                             0.017s    |- 2.06%  

  |- Residual                             0.009s    |- 1.04%  

  |- HeatLoss                             0.006s    |- 0.79%  

|- Logging                                0.007s  |- 0.87%    

|- Output                                 0.007s  |- 0.79%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.061s  6.81%       

|- execution                              0.059s  |- 95.78%   

------------------------------------------------------------

TOTAL                                     0.902s

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

Elapsed: 0.76s

    36 193.7837  6   3650.000     0.05              3.00             98.40                       5.84    0.197  483.732   0.0600    7.763



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.534s  89.56%      

|- Newton                                 0.523s  |- 98.00%   

  |- Update                               0.151s    |- 28.79% 

  |- FluxJac                              0.134s    |- 25.62% 

  |- Precond                              0.055s    |- 10.42% 

  |- ScdAcc                               0.050s    |- 9.48%  

  |- update_dev                           0.032s    |- 6.05%  

  |- Solver                               0.028s    |- 5.40%  

  |- PerfJac                              0.022s    |- 4.20%  

  |- SanitizeJac                          0.017s    |- 3.16%  

  |- alignvar                             0.011s    |- 2.02%  

  |- Residual                             0.005s    |- 0.97%  

  |- HeatLoss                             0.004s    |- 0.77%  

|- Logging                                0.008s  |- 1.41%    

|- Output                                 0.003s  |- 0.65%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.062s  10.44%      

|- execution                              0.059s  |- 95.44%   

------------------------------------------------------------

TOTAL                                     0.596s

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

Elapsed: 0.81s

    79   4.9496  1     10.000    5e-10              0.16            100.00                       0.16   13.643    0.005 7.13e-06  3.9e-07



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.580s  89.89%      

|- Newton                                 0.568s  |- 97.99%   

  |- Update                               0.197s    |- 34.74% 

  |- Precond                              0.079s    |- 13.91% 

  |- FluxJac                              0.075s    |- 13.17% 

  |- ScdAcc                               0.066s    |- 11.64% 

  |- update_dev                           0.033s    |- 5.77%  

  |- PerfJac                              0.029s    |- 5.15%  

  |- SanitizeJac                          0.026s    |- 4.56%  

  |- alignvar                             0.016s    |- 2.87%  

  |- Solver                               0.013s    |- 2.33%  

  |- HeatLoss                             0.010s    |- 1.84%  

  |- Residual                             0.008s    |- 1.38%  

|- Logging                                0.006s  |- 0.95%    

|- Output                                 0.004s  |- 0.62%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.065s  10.11%      

|- execution                              0.063s  |- 96.34%   

------------------------------------------------------------

TOTAL                                     0.645s

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

Elapsed: 0.81s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.569s  89.66%      

|- Newton                                 0.555s  |- 97.43%   

  |- Update                               0.238s    |- 42.91% 

  |- FluxJac                              0.108s    |- 19.40% 

  |- ScdAcc                               0.062s    |- 11.09% 

  |- update_dev                           0.036s    |- 6.41%  

  |- Precond                              0.036s    |- 6.40%  

  |- HeatLoss                             0.016s    |- 2.94%  

  |- Solver                               0.014s    |- 2.50%  

  |- Residual                             0.012s    |- 2.16%  

  |- PerfJac                              0.008s    |- 1.48%  

  |- SanitizeJac                          0.007s    |- 1.26%  

  |- alignvar                             0.005s    |- 0.95%  

|- Output                                 0.010s  |- 1.77%    

|- Logging                                0.001s  |- 0.25%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.066s  10.34%      

|- execution                              0.063s  |- 96.40%   

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

Elapsed: 0.28s

    17   1.4144  2     10.000                                                                 9521.20    0.053  152.652             1.045



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.057s  50.91%      

|- Newton                                 0.052s  |- 92.25%   

  |- Update                               0.017s    |- 32.75% 

  |- Precond                              0.009s    |- 18.17% 

  |- PerfJac                              0.005s    |- 9.71%  

  |- ScdAcc                               0.005s    |- 9.60%  

  |- FluxJac                              0.004s    |- 8.00%  

  |- SanitizeJac                          0.004s    |- 6.76%  

  |- update_dev                           0.003s    |- 5.83%  

  |- alignvar                             0.002s    |- 3.72%  

  |- Solver                               0.001s    |- 2.07%  

  |- Residual                             0.000s    |- 0.37%  

  |- HeatLoss                             0.000s    |- 0.01%  

|- Output                                 0.003s  |- 5.16%    

|- Logging                                0.001s  |- 1.98%    

|- Input                                  0.000s  |- 0.06%    

Initialization                            0.055s  49.09%      

|- execution                              0.053s  |- 96.34%   

------------------------------------------------------------

TOTAL                                     0.111s

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

Elapsed: 0.61s

    22 163.2234  2   3650.000     0.78             10.19             92.87                      10.73    0.000   13.707   0.0098    0.002



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.381s  85.76%      

|- Newton                                 0.376s  |- 98.81%   

  |- FluxJac                              0.125s    |- 33.18% 

  |- Update                               0.114s    |- 30.41% 

  |- ScdAcc                               0.035s    |- 9.23%  

  |- Solver                               0.034s    |- 9.14%  

  |- Precond                              0.024s    |- 6.42%  

  |- update_dev                           0.018s    |- 4.79%  

  |- PerfJac                              0.007s    |- 1.74%  

  |- SanitizeJac                          0.006s    |- 1.46%  

  |- Residual                             0.004s    |- 1.16%  

  |- alignvar                             0.004s    |- 1.07%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.001s  |- 0.36%    

|- Logging                                0.001s  |- 0.30%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.063s  14.24%      

|- execution                              0.061s  |- 96.44%   

------------------------------------------------------------

TOTAL                                     0.444s

============================================================



Time steps : 22/22, step size: 165.909, 155.033

```



## watfld_cw.dat

```
Running simulation [simuapp]: SPE4-b Water flooding without vmod (-novtu)

Elapsed: 0.79s

    35  32.2986  2   3650.000     1.04             79.00             98.70                      80.00    0.000    1.859   0.0028  3.1e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.561s  89.81%      

|- Newton                                 0.552s  |- 98.40%   

  |- Update                               0.171s    |- 30.98% 

  |- FluxJac                              0.162s    |- 29.45% 

  |- Solver                               0.056s    |- 10.11% 

  |- ScdAcc                               0.046s    |- 8.27%  

  |- Precond                              0.033s    |- 6.04%  

  |- PerfJac                              0.031s    |- 5.64%  

  |- update_dev                           0.024s    |- 4.43%  

  |- SanitizeJac                          0.008s    |- 1.44%  

  |- Residual                             0.006s    |- 1.16%  

  |- alignvar                             0.006s    |- 1.02%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.003s  |- 0.55%    

|- Logging                                0.002s  |- 0.30%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.064s  10.19%      

|- execution                              0.061s  |- 96.60%   

------------------------------------------------------------

TOTAL                                     0.624s

============================================================



Time steps : 35/35, step size: 104.286, 142.699

```

## stflu001.dat

Inverted 9 spot hot water flooding with area/block modifier, 5 point transmissibility


```
Running simulation [simuapp]: Inverted 9 spot hot water flooding (-novtu)

Elapsed: 1.13s

    95 281.6618  2   3650.000    5e-05            597.44            100.00                     597.44    0.486    0.077 9.13e-05    0.002



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.901s  93.48%      

|- Newton                                 0.887s  |- 98.41%   

  |- Update                               0.273s    |- 30.83% 

  |- FluxJac                              0.226s    |- 25.45% 

  |- Precond                              0.103s    |- 11.64% 

  |- ScdAcc                               0.089s    |- 10.05% 

  |- update_dev                           0.050s    |- 5.69%  

  |- Solver                               0.044s    |- 4.92%  

  |- SanitizeJac                          0.031s    |- 3.52%  

  |- alignvar                             0.020s    |- 2.26%  

  |- PerfJac                              0.016s    |- 1.79%  

  |- Residual                             0.010s    |- 1.11%  

  |- HeatLoss                             0.008s    |- 0.85%  

|- Output                                 0.007s  |- 0.82%    

|- Logging                                0.006s  |- 0.66%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.063s  6.52%       

|- execution                              0.061s  |- 96.22%   

------------------------------------------------------------

TOTAL                                     0.964s

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

Elapsed: 0.43s

    49 330.7333  5   3650.000   624.40             11.54              1.82                     635.95    0.000  1.1e+03   0.0498    0.028



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.199s  76.03%      

|- Newton                                 0.191s  |- 96.06%   

  |- Update                               0.067s    |- 34.94% 

  |- FluxJac                              0.037s    |- 19.43% 

  |- Precond                              0.023s    |- 11.90% 

  |- ScdAcc                               0.018s    |- 9.50%  

  |- update_dev                           0.009s    |- 4.85%  

  |- PerfJac                              0.008s    |- 4.27%  

  |- Solver                               0.008s    |- 4.19%  

  |- SanitizeJac                          0.007s    |- 3.80%  

  |- alignvar                             0.004s    |- 2.32%  

  |- HeatLoss                             0.003s    |- 1.52%  

  |- Residual                             0.002s    |- 1.31%  

|- Output                                 0.003s  |- 1.26%    

|- Logging                                0.002s  |- 0.86%    

|- Input                                  0.000s  |- 0.05%    

Initialization                            0.063s  23.97%      

|- execution                              0.060s  |- 96.20%   

------------------------------------------------------------

TOTAL                                     0.262s

============================================================



Time steps : 49/49, step size: 74.4898, 130.886

```



## stflu003.dat

5000x5000x50, 2D diagonal water flooding in uniformed corner point

```
Running simulation [simuapp]: uniformed corner grid (-novtu)

Elapsed: 0.43s

    46 255.0522  5   3650.000   624.70             11.24              1.77                     635.95    0.000  747.532   0.0384    0.019



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.199s  77.36%      

|- Newton                                 0.192s  |- 96.40%   

  |- Update                               0.065s    |- 34.10% 

  |- FluxJac                              0.039s    |- 20.61% 

  |- Precond                              0.022s    |- 11.49% 

  |- ScdAcc                               0.018s    |- 9.33%  

  |- update_dev                           0.009s    |- 4.83%  

  |- PerfJac                              0.008s    |- 4.28%  

  |- Solver                               0.008s    |- 4.16%  

  |- SanitizeJac                          0.007s    |- 3.60%  

  |- alignvar                             0.004s    |- 2.31%  

  |- HeatLoss                             0.003s    |- 1.51%  

  |- Residual                             0.002s    |- 1.30%  

|- Logging                                0.003s  |- 1.35%    

|- Output                                 0.002s  |- 1.10%    

|- Input                                  0.000s  |- 0.05%    

Initialization                            0.058s  22.64%      

|- execution                              0.055s  |- 95.14%   

------------------------------------------------------------

TOTAL                                     0.257s

============================================================



Time steps : 46/46, step size: 79.3478, 130.807

```

![png]({{ "/assets/images/benchmark_image_13.png" | relative_url }})



## stflu004.dat

2D diagonal water flooding for reduction of numerical dispersion and grid orientation effect


```
Running simulation [simuapp]: 2D diagonal flow: grid orientation

Elapsed: 0.76s

    61  58.6232  5   3650.000   613.68             22.27              3.50                     635.95    0.000  680.511   0.0195    0.039



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.529s  89.63%      

|- Newton                                 0.509s  |- 96.18%   

  |- Update                               0.203s    |- 39.83% 

  |- FluxJac                              0.119s    |- 23.32% 

  |- ScdAcc                               0.044s    |- 8.69%  

  |- Precond                              0.036s    |- 7.11%  

  |- Solver                               0.030s    |- 5.97%  

  |- update_dev                           0.023s    |- 4.62%  

  |- PerfJac                              0.013s    |- 2.48%  

  |- SanitizeJac                          0.009s    |- 1.85%  

  |- HeatLoss                             0.008s    |- 1.59%  

  |- alignvar                             0.007s    |- 1.28%  

  |- Residual                             0.006s    |- 1.26%  

|- Output                                 0.014s  |- 2.65%    

|- Logging                                0.003s  |- 0.53%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.061s  10.37%      

|- execution                              0.059s  |- 95.88%   

------------------------------------------------------------

TOTAL                                     0.590s

============================================================



Time steps : 61/61, step size: 59.8361, 80.6364

```

![png]({{ "/assets/images/benchmark_image_14.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_15.png" | relative_url }})

## stflu007.dat

PEBI_GRID


```
Running simulation [simuapp]: 2D diagonal flow: pebi grid

Elapsed: 0.97s

    59 354.4145  5   3650.000   623.41             12.54              1.97                     635.95    0.000  1.3e+03   0.0716    0.058



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.724s  90.31%      

|- Newton                                 0.703s  |- 97.07%   

  |- FluxJac                              0.240s    |- 34.16% 

  |- Update                               0.223s    |- 31.66% 

  |- Solver                               0.058s    |- 8.30%  

  |- ScdAcc                               0.058s    |- 8.22%  

  |- Precond                              0.037s    |- 5.31%  

  |- update_dev                           0.029s    |- 4.18%  

  |- HeatLoss                             0.012s    |- 1.67%  

  |- Residual                             0.010s    |- 1.46%  

  |- PerfJac                              0.009s    |- 1.31%  

  |- SanitizeJac                          0.008s    |- 1.18%  

  |- alignvar                             0.006s    |- 0.82%  

|- Output                                 0.015s  |- 2.05%    

|- Logging                                0.002s  |- 0.26%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.078s  9.69%       

|- execution                              0.068s  |- 87.44%   

------------------------------------------------------------

TOTAL                                     0.802s

============================================================



Time steps : 59/59, step size: 61.8644, 119.411

```

![png]({{ "/assets/images/benchmark_image_16.png" | relative_url }})

![png]({{ "/assets/images/benchmark_image_17.png" | relative_url }})

## stflu026.dat

* Steam flood on two component live oil

```
Running simulation [simuapp]: 3 component steam flooding (-novtu)

Elapsed: 1.38s

    94  36.8774  4   3650.000     0.01              4.36             99.85                       4.50    2.860    9.784   0.0020    0.821



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.155s  95.01%      

|- Newton                                 1.132s  |- 98.02%   

  |- FluxJac                              0.303s    |- 26.73% 

  |- Update                               0.296s    |- 26.19% 

  |- ScdAcc                               0.130s    |- 11.50% 

  |- Precond                              0.110s    |- 9.72%  

  |- Solver                               0.084s    |- 7.39%  

  |- update_dev                           0.063s    |- 5.57%  

  |- PerfJac                              0.048s    |- 4.25%  

  |- SanitizeJac                          0.030s    |- 2.61%  

  |- alignvar                             0.019s    |- 1.68%  

  |- Residual                             0.014s    |- 1.28%  

  |- HeatLoss                             0.009s    |- 0.75%  

|- Logging                                0.011s  |- 0.92%    

|- Output                                 0.008s  |- 0.71%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.061s  4.99%       

|- execution                              0.058s  |- 95.56%   

------------------------------------------------------------

TOTAL                                     1.216s

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

Elapsed: 1.66s

    95 165.6701  5   3650.000     0.01              4.25             99.86                       4.32    2.067    0.690   0.0040    3.074



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  1.411s  95.85%      

|- Newton                                 1.389s  |- 98.45%   

  |- FluxJac                              0.390s    |- 28.07% 

  |- Update                               0.344s    |- 24.77% 

  |- Solver                               0.156s    |- 11.26% 

  |- Precond                              0.140s    |- 10.08% 

  |- ScdAcc                               0.134s    |- 9.67%  

  |- update_dev                           0.072s    |- 5.18%  

  |- PerfJac                              0.055s    |- 3.96%  

  |- SanitizeJac                          0.029s    |- 2.08%  

  |- alignvar                             0.019s    |- 1.34%  

  |- Residual                             0.012s    |- 0.85%  

  |- HeatLoss                             0.011s    |- 0.81%  

|- Logging                                0.011s  |- 0.77%    

|- Output                                 0.009s  |- 0.63%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.061s  4.15%       

|- execution                              0.058s  |- 95.23%   

------------------------------------------------------------

TOTAL                                     1.472s

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

Elapsed: 0.96s

   110  16.2309  6   1095.000     0.79              0.50             38.50                               0.062    4.644   0.1420    1.026



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  0.729s  92.03%      

|- Newton                                 0.694s  |- 95.16%   

  |- Update                               0.211s    |- 30.36% 

  |- FluxJac                              0.128s    |- 18.43% 

  |- Precond                              0.084s    |- 12.05% 

  |- ScdAcc                               0.070s    |- 10.12% 

  |- PerfJac                              0.066s    |- 9.56%  

  |- update_dev                           0.037s    |- 5.27%  

  |- SanitizeJac                          0.028s    |- 3.98%  

  |- Solver                               0.024s    |- 3.44%  

  |- alignvar                             0.015s    |- 2.22%  

  |- Residual                             0.006s    |- 0.82%  

  |- HeatLoss                             0.004s    |- 0.61%  

|- Output                                 0.021s  |- 2.94%    

|- Logging                                0.008s  |- 1.09%    

|- Input                                  0.001s  |- 0.13%    

Initialization                            0.063s  7.97%       

|- execution                              0.061s  |- 96.23%   

------------------------------------------------------------

TOTAL                                     0.792s

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

Elapsed: 9.96s

   139  89.7013  6   1095.000     1.43              1.45             50.29                               0.476   49.444   0.1070    5.828



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  9.721s  99.28%      

|- Newton                                 9.620s  |- 98.95%   

  |- FluxJac                              3.571s    |- 37.12% 

  |- Update                               3.001s    |- 31.20% 

  |- Solver                               0.849s    |- 8.83%  

  |- ScdAcc                               0.748s    |- 7.77%  

  |- update_dev                           0.465s    |- 4.83%  

  |- Precond                              0.424s    |- 4.41%  

  |- Residual                             0.097s    |- 1.01%  

  |- PerfJac                              0.090s    |- 0.94%  

  |- HeatLoss                             0.090s    |- 0.94%  

  |- SanitizeJac                          0.087s    |- 0.91%  

  |- alignvar                             0.064s    |- 0.67%  

|- Output                                 0.078s  |- 0.80%    

|- Logging                                0.013s  |- 0.13%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.070s  0.72%       

|- execution                              0.068s  |- 96.43%   

------------------------------------------------------------

TOTAL                                     9.792s

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

Elapsed: 31.92s

   123  40.1083  6   1095.000     0.76              0.44             36.84                               0.161   75.104   0.1995    2.169



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 31.603s  99.57%      

|- Newton                                31.367s  |- 99.25%   

  |- FluxJac                             13.215s    |- 42.13% 

  |- Update                               8.599s    |- 27.41% 

  |- Solver                               3.984s    |- 12.70% 

  |- ScdAcc                               2.177s    |- 6.94%  

  |- update_dev                           1.201s    |- 3.83%  

  |- Precond                              1.033s    |- 3.29%  

  |- Residual                             0.311s    |- 0.99%  

  |- alignvar                             0.146s    |- 0.47%  

  |- HeatLoss                             0.141s    |- 0.45%  

  |- SanitizeJac                          0.088s    |- 0.28%  

  |- PerfJac                              0.070s    |- 0.22%  

|- Output                                 0.204s  |- 0.64%    

|- Logging                                0.023s  |- 0.07%    

|- Input                                  0.001s  |- 0.00%    

Initialization                            0.135s  0.43%       

|- execution                              0.090s  |- 66.79%   

------------------------------------------------------------

TOTAL                                    31.738s

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

Elapsed: 16.11s

   213  32.9215  7   1095.000     1.62              1.67             50.81                               1.543   25.689   0.1019    2.570



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 15.834s  99.42%      

|- Newton                                15.614s  |- 98.61%   

  |- FluxJac                              6.493s    |- 41.59% 

  |- Update                               4.176s    |- 26.74% 

  |- Solver                               1.845s    |- 11.81% 

  |- ScdAcc                               1.092s    |- 7.00%  

  |- Precond                              0.636s    |- 4.08%  

  |- update_dev                           0.604s    |- 3.87%  

  |- PerfJac                              0.173s    |- 1.11%  

  |- Residual                             0.135s    |- 0.87%  

  |- SanitizeJac                          0.123s    |- 0.79%  

  |- alignvar                             0.085s    |- 0.54%  

  |- HeatLoss                             0.067s    |- 0.43%  

|- Output                                 0.181s  |- 1.14%    

|- Logging                                0.026s  |- 0.16%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.092s  0.58%       

|- execution                              0.073s  |- 79.13%   

------------------------------------------------------------

TOTAL                                    15.926s

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

Elapsed: 8.15s

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

Elapsed: 0.43s

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

Elapsed: 3.40s

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

Elapsed: 3.91s

   213   9.6907  6   2526.000     5.52             52.63             90.50                      54.07    0.276    2.889   0.0408    6.325



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  3.670s  98.28%      

|- Newton                                 3.632s  |- 98.98%   

  |- Update                               1.196s    |- 32.93% 

  |- FluxJac                              1.013s    |- 27.89% 

  |- ScdAcc                               0.402s    |- 11.07% 

  |- Precond                              0.269s    |- 7.40%  

  |- update_dev                           0.235s    |- 6.48%  

  |- Solver                               0.178s    |- 4.91%  

  |- SanitizeJac                          0.070s    |- 1.94%  

  |- alignvar                             0.061s    |- 1.68%  

  |- PerfJac                              0.060s    |- 1.66%  

  |- Residual                             0.044s    |- 1.21%  

  |- HeatLoss                             0.008s    |- 0.23%  

|- Logging                                0.041s  |- 1.12%    

|- Output                                 0.013s  |- 0.34%    

|- Input                                  0.001s  |- 0.02%    

Initialization                            0.064s  1.72%       

|- execution                              0.062s  |- 96.07%   

------------------------------------------------------------

TOTAL                                     3.734s

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

Elapsed: 2.88s

   100 163.6974  6   2526.000     5.79            142.07             96.08                     150.00    1.212  124.377   0.0832   11.957



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.616s  97.29%      

|- Newton                                 2.590s  |- 98.98%   

  |- Update                               0.697s    |- 26.93% 

  |- FluxJac                              0.668s    |- 25.81% 

  |- PerfJac                              0.397s    |- 15.33% 

  |- ScdAcc                               0.248s    |- 9.59%  

  |- Precond                              0.161s    |- 6.20%  

  |- update_dev                           0.149s    |- 5.74%  

  |- Solver                               0.112s    |- 4.32%  

  |- SanitizeJac                          0.044s    |- 1.68%  

  |- alignvar                             0.032s    |- 1.25%  

  |- Residual                             0.026s    |- 0.99%  

  |- HeatLoss                             0.005s    |- 0.20%  

|- Logging                                0.012s  |- 0.47%    

|- Output                                 0.009s  |- 0.36%    

|- Input                                  0.000s  |- 0.02%    

Initialization                            0.073s  2.71%       

|- execution                              0.070s  |- 96.08%   

------------------------------------------------------------

TOTAL                                     2.689s

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

Elapsed: 23.67s

   154   3.6054  6    680.000    14.23             99.74             87.51                      90.66    1.090    1.472   0.0912    5.244



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 23.419s  99.68%      

|- Newton                                23.348s  |- 99.70%   

  |- FluxJac                              8.757s    |- 37.51% 

  |- Update                               6.877s    |- 29.46% 

  |- Solver                               2.645s    |- 11.33% 

  |- ScdAcc                               1.928s    |- 8.26%  

  |- update_dev                           1.044s    |- 4.47%  

  |- Precond                              0.874s    |- 3.74%  

  |- PerfJac                              0.352s    |- 1.51%  

  |- Residual                             0.239s    |- 1.02%  

  |- alignvar                             0.128s    |- 0.55%  

  |- SanitizeJac                          0.109s    |- 0.47%  

  |- HeatLoss                             0.097s    |- 0.41%  

|- Logging                                0.027s  |- 0.12%    

|- Output                                 0.022s  |- 0.10%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            0.076s  0.32%       

|- execution                              0.074s  |- 96.48%   

------------------------------------------------------------

TOTAL                                    23.496s

============================================================



Time steps : 154/160, step size: 4.41558, 3.45336

```

#### 2D live oil

* 10x1x20 cross-section, two-component live oil (CH4 + HOIL) with water. Injector 'Inj' (2:9,1,13) and producer 'Prod' (2:9,1,18); both are shut in and preheated for 60 days, then opened.

* CMG only (no ECL run for this deck).

```
Running simulation [simuapp]: SAGD live oil (-novtu)

Elapsed: 5.45s

   167   8.7430  6   2526.000     7.54     4.81   146.72     0.64    95.11                     150.00    0.973   10.397   0.0394    1.101



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  5.178s  98.65%      

|- Newton                                 5.132s  |- 99.11%   

  |- FluxJac                              1.364s    |- 26.58% 

  |- Update                               1.335s    |- 26.01% 

  |- PerfJac                              0.701s    |- 13.66% 

  |- ScdAcc                               0.507s    |- 9.88%  

  |- Solver                               0.338s    |- 6.58%  

  |- Precond                              0.323s    |- 6.29%  

  |- update_dev                           0.288s    |- 5.61%  

  |- SanitizeJac                          0.077s    |- 1.51%  

  |- alignvar                             0.058s    |- 1.13%  

  |- Residual                             0.045s    |- 0.87%  

  |- HeatLoss                             0.010s    |- 0.19%  

|- Logging                                0.024s  |- 0.47%    

|- Output                                 0.017s  |- 0.32%    

|- Input                                  0.001s  |- 0.01%    

Initialization                            0.071s  1.35%       

|- execution                              0.067s  |- 94.41%   

------------------------------------------------------------

TOTAL                                     5.249s

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

Elapsed: 34.22s

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

Elapsed: 0.40s

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

Elapsed: 4.54s

No text to display.

```

```
OURS reached day 820.0 of 820

THERM: 506 steps marched, 0 cuts, 659 Newton cycles

 OURS: 231 steps marched, 5 cuts, 1208 Newton cycles

```

### Wells

* Rates are m3/day at standard conditions, read from the time step summary. The wells are shut in until day 150, so there is nothing to plot before it.

![png]({{ "/assets/images/benchmark_image_46.png" | relative_url }})

# Speed



`-DCMAKE_BUILD_TYPE=Release`

### Dome corner grid

```
Running simulation [simuapp]: Dome Corner point

Elapsed: 2.73s

    76  77.6820  1    365.000                                                                            0.016   12.402   0.0148    4.869



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  2.444s  96.21%      

|- Newton                                 2.419s  |- 98.97%   

  |- Update                               0.835s    |- 34.51% 

  |- FluxJac                              0.804s    |- 33.25% 

  |- ScdAcc                               0.208s    |- 8.58%  

  |- Solver                               0.191s    |- 7.90%  

  |- update_dev                           0.129s    |- 5.32%  

  |- Precond                              0.103s    |- 4.26%  

  |- Residual                             0.039s    |- 1.62%  

  |- HeatLoss                             0.025s    |- 1.03%  

  |- SanitizeJac                          0.015s    |- 0.64%  

  |- alignvar                             0.014s    |- 0.57%  

  |- PerfJac                              0.002s    |- 0.08%  

|- Output                                 0.010s  |- 0.40%    

|- Logging                                0.005s  |- 0.22%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.096s  3.79%       

|- execution                              0.088s  |- 91.47%   

------------------------------------------------------------

TOTAL                                     2.541s

============================================================



Time steps : 76/79, step size: 4.80263, 16.5526

```

```
Found 4 VTU files

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data/stflu018_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_47.png" | relative_url }})

## Heterogeneous

### SPE10 benchmark 2D 

```
Running simulation [simuapp]: SPE10 benchmark 2D water flooding 375 days ~7s single thread (OMP_NUM_THREADS=8)

Elapsed: 9.06s

    89   2.1695  6    375.000    19.31             4e-06             2e-05                      19.43    3.367    0.557   0.0471    0.002



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                  8.790s  99.03%      

|- Newton                                 8.673s  |- 98.67%   

  |- FluxJac                              2.703s    |- 31.17% 

  |- Update                               2.622s    |- 30.24% 

  |- Solver                               1.288s    |- 14.85% 

  |- ScdAcc                               0.769s    |- 8.87%  

  |- update_dev                           0.387s    |- 4.46%  

  |- Precond                              0.316s    |- 3.64%  

  |- PerfJac                              0.248s    |- 2.85%  

  |- Residual                             0.102s    |- 1.18%  

  |- alignvar                             0.051s    |- 0.59%  

  |- SanitizeJac                          0.042s    |- 0.48%  

  |- HeatLoss                             0.019s    |- 0.22%  

|- Output                                 0.082s  |- 0.93%    

|- Logging                                0.013s  |- 0.15%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.086s  0.97%       

|- execution                              0.079s  |- 91.09%   

------------------------------------------------------------

TOTAL                                     8.876s

============================================================



Time steps : 89/89, step size: 4.21348, 2.75343

```

![png]({{ "/assets/images/benchmark_image_48.png" | relative_url }})

### Medium size



* 202,005 grid block (201x201x5) with heterogeneous permeability

* 61 wells water flooding pattern 

* 1500 days

```
Running simulation [simuapp]: Heterogeneous + 61wells - performance test medium size ~3m.50s (Single) (OMP_NUM_THREADS=8, -novtu)

Elapsed: 296.86s

    32  22.4900  5    365.000   257.30              7.92              2.99                     720.00    0.000  111.773   0.0064    1.457



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                               4m 55.07s  99.51%      

|- Newton                              4m 54.48s  |- 99.80%   

  |- FluxJac                           1m 39.62s    |- 33.83% 

  |- Update                            1m 16.86s    |- 26.10% 

  |- Solver                              58.718s    |- 19.94% 

  |- ScdAcc                              21.852s    |- 7.42%  

  |- update_dev                          11.100s    |- 3.77%  

  |- Precond                             10.573s    |- 3.59%  

  |- Residual                             4.117s    |- 1.40%  

  |- HeatLoss                             2.901s    |- 0.99%  

  |- PerfJac                              2.147s    |- 0.73%  

  |- alignvar                             0.957s    |- 0.32%  

  |- SanitizeJac                          0.619s    |- 0.21%  

|- Output                                 0.087s  |- 0.03%    

|- Logging                                0.036s  |- 0.01%    

|- Input                                  0.010s  |- 0.00%    

Initialization                            1.438s  0.49%       

|- execution                              1.293s  |- 89.92%   

------------------------------------------------------------

TOTAL                                  4m 56.50s

============================================================



Time steps : 32/32, step size: 11.4062, 13.2808

```

### Johnansen water flooding

```
Running simulation [simuapp]: Johnansen water flooding takes ~5m on M2 (OMP_NUM_THREADS=8)

Elapsed: 22.40s

    17 365.0000  1   3650.000   353.53              0.07              0.02                     188.86    0.000    3.270   0.0067  3.1e-04



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 20.568s  93.65%      

|- Newton                                20.427s  |- 99.31%   

  |- Update                               6.823s    |- 33.40% 

  |- FluxJac                              6.554s    |- 32.09% 

  |- Solver                               3.470s    |- 16.99% 

  |- ScdAcc                               1.403s    |- 6.87%  

  |- update_dev                           0.723s    |- 3.54%  

  |- Precond                              0.663s    |- 3.25%  

  |- Residual                             0.340s    |- 1.66%  

  |- alignvar                             0.068s    |- 0.34%  

  |- SanitizeJac                          0.030s    |- 0.15%  

  |- PerfJac                              0.002s    |- 0.01%  

  |- HeatLoss                             0.000s    |- 0.00%  

|- Output                                 0.099s  |- 0.48%    

|- Logging                                0.002s  |- 0.01%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            1.395s  6.35%       

|- execution                              1.067s  |- 76.47%   

------------------------------------------------------------

TOTAL                                    21.963s

============================================================



Time steps : 17/17, step size: 214.706, 163.784

Loading: /Users/mark/Documents/workspace/hatch/app/build-release/test/data//stflu016_00000.vtu

```

![png]({{ "/assets/images/benchmark_image_49.png" | relative_url }})

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

Timeloop                                  1.376s  95.52%      

|- Newton                                 1.353s  |- 98.35%   

  |- FluxJac                              0.608s    |- 44.97% 

  |- Update                               0.341s    |- 25.20% 

  |- ScdAcc                               0.149s    |- 10.98% 

  |- update_dev                           0.108s    |- 7.95%  

  |- Solver                               0.045s    |- 3.32%  

  |- PerfJac                              0.037s    |- 2.75%  

  |- Precond                              0.021s    |- 1.55%  

  |- alignvar                             0.008s    |- 0.60%  

  |- Residual                             0.007s    |- 0.50%  

  |- HeatLoss                             0.005s    |- 0.34%  

  |- SanitizeJac                          0.001s    |- 0.11%  

|- Logging                                0.012s  |- 0.89%    

|- Output                                 0.010s  |- 0.71%    

|- Input                                  0.000s  |- 0.01%    

Initialization                            0.065s  4.48%       

|- execution                              0.062s  |- 96.39%   

------------------------------------------------------------

TOTAL                                     1.440s

============================================================



Time steps : 79/79, step size: 46.2025, 50.7314

Running simulation [simumpi]: MPI comparison np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 1.80s

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

Elapsed: 1.15s

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

Elapsed: 1.19s

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

simumpi np=1     rc=0   1.33s   79/ 79 steps,  0 cuts  to  3650.00 days

simumpi np=2     rc=0   0.86s   79/ 79 steps,  0 cuts  to  3650.00 days

simumpi np=4     rc=0   0.82s   81/ 82 steps,  1 cuts  to  3650.00 days

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


![png]({{ "/assets/images/benchmark_image_50.png" | relative_url }})

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

Elapsed: 23.00s

   139  89.7013  6   1095.000     1.43              1.45             50.29                               0.476   49.444   0.1070    5.828



============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 22.597s  99.60%      

|- Newton                                22.556s  |- 99.82%   

  |- FluxJac                             11.375s    |- 50.43% 

  |- Update                               5.407s    |- 23.97% 

  |- ScdAcc                               2.269s    |- 10.06% 

  |- update_dev                           1.530s    |- 6.78%  

  |- Solver                               0.952s    |- 4.22%  

  |- Precond                              0.402s    |- 1.78%  

  |- alignvar                             0.123s    |- 0.55%  

  |- PerfJac                              0.103s    |- 0.46%  

  |- Residual                             0.099s    |- 0.44%  

  |- HeatLoss                             0.084s    |- 0.37%  

  |- SanitizeJac                          0.025s    |- 0.11%  

|- Logging                                0.040s  |- 0.18%    

|- Output                                 0.019s  |- 0.08%    

|- Input                                  0.003s  |- 0.01%    

Initialization                            0.090s  0.40%       

|- execution                              0.087s  |- 96.48%   

------------------------------------------------------------

TOTAL                                    22.688s

============================================================



Time steps : 139/147, step size: 7.8777, 16.6126

Running simulation [simumpi]: CSS parity np=1 (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 21.75s

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

Elapsed: 19.30s

   196   0.1451  6    747.256     0.08            148.25             99.95                               0.384  185.672   0.1047   10.267

   197   0.1995  6    747.456     0.02            126.35             99.98                               0.384  121.883   0.0523    5.577

   198   0.3450  6    747.801     0.83            101.87             99.20                               0.384  148.177   0.0906    5.847

   199   0.5020  6    748.303     2.23             79.88             97.28                               0.384  155.927   0.1161    6.005

   200   0.6602  6    748.963     4.15             61.48             93.68                               0.384  135.699   0.1615    5.502

   201   0.7417  6    749.705     5.77             49.20             89.50                               0.384  112.897   0.1570    4.476

   202   0.8456  6    750.550     7.37             40.89             84.74                               0.384   99.716   0.0820    3.834

   203   1.2754  6    751.826     8.65             33.30             79.38                               0.384  113.521   0.0451    4.626

   204   2.2877  6    754.113     8.84             26.71             75.14                               0.384  149.545   0.4596    6.176

   205   1.3135  6    755.427     8.23             24.64             74.96                               0.384   71.055   0.0167    3.068

   206   2.6270  6    758.054     7.60             20.97             73.39                               0.384  103.563   0.0944    4.879

   207   3.7619  6    761.816     6.81             17.15             71.58                               0.384  117.155   0.0692    5.418

   208   6.0059  6    767.822     5.68             13.07             69.71                               0.384  129.120   0.1053    7.065

   209   8.2343  6    776.056     4.47              9.89             68.86                               0.387  112.685   0.1311    7.210

   210  10.2528  6    786.309     3.72              8.07             68.44                               0.387   91.828   0.0270    7.259



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   211  20.2735  6    806.582     3.04              5.65             65.05                               0.387  106.918   0.1055   10.392

   212  27.7766 11    834.359     2.47              4.04             62.09                               0.387   83.129   0.0823    9.931

   213  30.3018  7    864.661     2.15              3.15             59.45                               0.387   55.957   0.0897    7.514

   214  44.2497  6    908.910     1.90              2.60             57.75                               0.416   51.278   0.1276    6.781

   215  55.7875  7    964.698     1.98              2.02             50.48                               0.448   48.483   0.1487    6.103

   216  65.3750  8   1030.073     1.53              1.41             48.00                               0.485   45.150   0.1074    5.492

   217  64.9271  7   1095.000     1.45              1.20             45.26                               0.478   34.060   0.1011    3.568

Time steps : 217/236, step size: 5.04608, 14.123

Running simulation [simumpi]: CSS parity np=4 (OMP_NUM_THREADS=1, np=4, -novtu)

Elapsed: 9.04s

   117   0.2605  6    747.594     0.48            118.29             99.59                               0.321  141.511   0.0716    7.584

   118   0.4114  6    748.005     1.60             93.27             98.31                               0.322  146.894   0.1052    5.599

   119   0.5643  6    748.570     3.40             72.62             95.52                               0.322  140.408   0.1401    5.495

   120   0.6808  6    749.250     4.98             56.70             91.92                               0.323  120.924   0.1935    4.844



=========================================================================================================================================

------Time Step----- --Time-- -----------------Production----------------- ---------Injection-------- --mat--- ------Maximum Changes-----

                   C             Oil     Gas      Water     GOR     Wat.      Oil      Gas    Water     bal      Pres     Sat     Temp   

        Size       U                                         m3     Cut                                 err                              

 No      day    IT T   day      m3/d     m3/d     m3/d      /m3      %       m3/d     m3/d     m3/d      %        kpa              degC  

------ -------- -- - -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- -------- --------

   121   0.6938  6    749.944     6.89             47.00             87.21                               0.323   96.012   0.0702    3.673

   122   1.1026  9    751.047     8.72             38.40             81.49                               0.323  114.548   0.0774    4.435

   123   1.4701  6    752.517     9.45             32.01             77.21                               0.324  117.687   0.4752    4.705

   124   0.8230  6    753.340     9.00             30.39             77.16                               0.324   58.536   0.0336    2.345

   125   1.5687  6    754.909     8.67             26.85             75.58                               0.324   88.753   0.0352    3.708

   126   2.9644  6    757.873     7.93             21.97             73.47                               0.325  118.831   0.1126    5.345

   127   3.9504  6    761.823     6.99             17.52             71.47                               0.325  124.110   0.0611    5.545

   128   6.5495  6    768.373     5.70             13.08             69.63                               0.326  139.323   0.0892    7.434

   129   9.5845  7    777.957     4.40              9.68             68.73                               0.326  124.264   0.1134    8.056

   130  12.7368  6    790.694     3.65              7.64             67.68                               0.327  101.944   0.1111    8.369

   131  17.0765  6    807.771     3.09              5.69             64.83                               0.328   87.728   0.1380    8.552

   132  20.7511  7    828.522     2.52              4.42             63.69                               0.328   67.636   0.0963    7.859

   133  29.4899 11    858.012     2.27              3.45             60.33                               0.329   59.152   0.0814    7.770

   134  32.1708  6    890.183     2.10              2.82             57.32                               0.329   43.979   0.1261    5.923

   135  40.7836  6    930.966     2.09              2.31             52.49                               0.330   41.381   0.0998    5.219

   136  57.1527  7    988.119     1.84              1.68             47.72                               0.330   46.716   0.1588    5.584

   137  64.7832  7   1052.902     1.70              1.33             43.82                               0.331   43.670   0.1130    4.922

   138  42.0979  6   1095.000     1.22              1.16             48.66                               0.332   26.999   0.0646    2.759

Time steps : 138/141, step size: 7.93478, 17.5143

simuapp          rc=0  22.69s  139/147 steps  to  1095.00 days

simumpi np=1     rc=0  21.28s  139/147 steps,  8 cuts  to  1095.00 days

simumpi np=2     rc=0  18.97s  217/236 steps, 19 cuts  to  1095.00 days

simumpi np=4     rc=0   8.67s  138/141 steps,  3 cuts  to  1095.00 days

```

![png]({{ "/assets/images/benchmark_image_51.png" | relative_url }})

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

Elapsed: 37.53s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 35.438s  95.40%      

|- Newton                                35.356s  |- 99.77%   

  |- FluxJac                             15.459s    |- 43.72% 

  |- Update                              10.711s    |- 30.30% 

  |- ScdAcc                               3.460s    |- 9.79%  

  |- update_dev                           2.186s    |- 6.18%  

  |- Solver                               2.015s    |- 5.70%  

  |- Precond                              0.617s    |- 1.75%  

  |- Residual                             0.215s    |- 0.61%  

  |- alignvar                             0.182s    |- 0.52%  

  |- HeatLoss                             0.107s    |- 0.30%  

  |- PerfJac                              0.084s    |- 0.24%  

  |- SanitizeJac                          0.056s    |- 0.16%  

|- Output                                 0.008s  |- 0.02%    

|- Logging                                0.001s  |- 0.00%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            1.710s  4.60%       

|- execution                              1.562s  |- 91.32%   

------------------------------------------------------------

TOTAL                                    37.148s

============================================================



Time steps : 4/4, step size: 0.129481, 0.0270325

Running simulation [simuapp]: scaling baseline (attempt 2/2) (OMP_NUM_THREADS=1, -novtu)

Elapsed: 36.74s





============================================================

                WALL-TIME PERFORMANCE REPORT                

============================================================

Category                              Total Time  % Total     

------------------------------------------------------------

Timeloop                                 34.751s  95.40%      

|- Newton                                34.692s  |- 99.83%   

  |- FluxJac                             15.302s    |- 44.11% 

  |- Update                              10.576s    |- 30.49% 

  |- ScdAcc                               3.331s    |- 9.60%  

  |- update_dev                           2.123s    |- 6.12%  

  |- Solver                               1.884s    |- 5.43%  

  |- Precond                              0.620s    |- 1.79%  

  |- Residual                             0.206s    |- 0.59%  

  |- alignvar                             0.179s    |- 0.51%  

  |- HeatLoss                             0.104s    |- 0.30%  

  |- PerfJac                              0.083s    |- 0.24%  

  |- SanitizeJac                          0.054s    |- 0.16%  

|- Output                                 0.007s  |- 0.02%    

|- Logging                                0.001s  |- 0.00%    

|- Input                                  0.000s  |- 0.00%    

Initialization                            1.674s  4.60%       

|- execution                              1.539s  |- 91.94%   

------------------------------------------------------------

TOTAL                                    36.425s

============================================================



Time steps : 4/4, step size: 0.129481, 0.0270325

Running simulation [simumpi]: scaling np=1 (attempt 1/2) (OMP_NUM_THREADS=1, np=1, -novtu)

Elapsed: 37.37s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-19





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

Elapsed: 38.23s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-19





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

Elapsed: 20.26s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-19





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

Elapsed: 20.00s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-19





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

Elapsed: 12.31s

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-19





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

Elapsed: 12.68s

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-19





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

Running simulation [simumpi]: scaling np=8 (attempt 1/2) (OMP_NUM_THREADS=1, np=8, -novtu)

Elapsed: 11.23s

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-19





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

Elapsed: 11.88s

          |   ||  |  __ |   \ |  ||   | `--.  .--' |  |____

          |   ||  | |. ||  .  \  ||   |    |  |    |  .____|

          |   ||  |__| ||  |\   \||   |    |  |    |  |____

          |___| \______||__| \___||___|    |__|    |_______|



            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                  



            VERSION: 1.0.0

            CONTACT: he.chron@gmail.com

            DATE:    2026-11-19





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

![png]({{ "/assets/images/benchmark_image_52.png" | relative_url }})

```
   config  steps   seconds   speedup   effic.  cells/rank   ghosts

  simuapp      4     36.42         -        -           -        -

     np=1      4     34.72     1.00x     100%      202005        0

     np=2      4     18.11     1.92x      96%      101080     2110

     np=4      4     10.68     3.25x      81%       50520     4235

     np=8      4      9.07     3.83x      48%       25610     8325 *

  * more ranks than the 4 fast cores on this CPU - paced by the slow ones, so read the efficiency as the machine's, not the partition's

```

```
Script completed at: 2026-11-19 10:49:00

```
