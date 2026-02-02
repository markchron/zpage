---
layout: default
title: "Benchmark results of resrsim"
date: 2026-02-01
---

# Setup

1. select kernel before executing current jupyter book

2. Install `ipykernel` package. For a virtual environment, open a terminal, and active the environment. 



    ```bash

    python -m venv .venv

    source .venv/bin/activate

    ```



3. Run `which python` to make sure the right virtual environment activated

4. Install requirments by `pip install -r requirements.txt`

4. Install by `python -m pip install ipykernel -U --force-reinstall`. 

5. install dependent packages `python -m pip install pandas numpy matplotlib trame trame-vtk trame-vuetify vtk`

The following is optional:

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



3. `pip install jupyter` if needs

# 3D



```

python -m pip install --upgrade pip

python -m pip install pyvista

```

In Jupyter Notebook, `pyvista.set_jupyter_backend("trame")` must install trame by `pip install trame trame-vtk trame-vuetify`

# SPE4-b


### Load STARS

### Load ECL

### Load SMY File

Load the SMY file (`spe04b.smy`) into a pandas DataFrame, ensuring proper parsing of the data.

## Select and Plot Columns

Select specific columns from the loaded DataFrames and plot them using matplotlib. For example, plot `TIME` vs `TEMP 1-1-4` from `stars_spe4b_special.csv`.

### Cell property

#### Block Pressure


#### Block Temperature

#### Block Saturation

### vesus ECL

### Well property

#### Injector

#### Producer Corner

#### Producer Edge

# Buckley- Leverett



Two phase, isothermal problem

variable order: [Sw, P, T, So, X0, X1, Sg]



Acc w.r.t. [Sw, So, Sg, X0, X1, P, T]

### Load Benchmark

### Buckley Plot

# MISC

## spe04b_cw.dat



## watfld_cw.dat



## stflu001.dat

Inverted 9 spot water flooding with area/block modifier, 5 point transmissibility


## stflu002.dat

5000x5000x50, 2D diagonal water flooding in uniformed cartesian

## stflu003.dat

5000x5000x50, 2D diagonal water flooding in uniformed corner point

## stflu004.dat

2D diagonal water flooding for reduction of numerical dispersion and grid orientation effect


## stflu005.dat

steam injection in corner-point grid

# SPE4C


## Run & Load

#### Load CMG

### Load ECL

### Wells

### Block

#### Block Pressure


#### Block Temperature

#### v.s. ECL
