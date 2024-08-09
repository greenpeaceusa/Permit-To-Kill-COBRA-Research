
# Background
This repository contains the code and data corresponding to the analysis underlying Permit to Kill: Potential Health and Economic Impacts from U.S. LNG Export Terminal Permitted Emissions, a health briefing published by Greenpeace USA and Sierra Club.

# COBRA Methodology
## Overview
We used EPA's COBRA tool to execute 2 distinct experiments: 
(a) timeframe analysis comparing the health impacts in different LNG buildout scenarios and;
(b) project-by-project analysis where permitted emissions from each LNG project are modeled using a common analysis year.

Please refer to the Methodology section of the Permit to Kill report for more information on the COBRA methodology and determination of permitted emissions for each LNG project.

## Technical setup
There are 3 computation steps to the analysis.
(1) In a Google Colab environment, Jupyter Notebook/Python scripts are used to create COBRA input data csvs and executable batch files for running COBRA;
(2) In a separate desktop environment, the input files and batch files from step 1 are downloaded. Then the batch files are used to run COBRA. COBRA writes the results of each individual execution to output files;
(3) The output files are uploaded to the same Google Colab environment as Step 1. When all necessary COBRA runs have been completed, Jupyter Notebook/Python scripts are used to analyze the data.

## How to navigate the repo
* `COBRA (from desktop version) - v5.1` (directory): contains various COBRA input files provided by EPA. Note that 2030-2050 population, incidence, and valuation files were downloaded from EPA's website and renamed to fit the same convention used by default input files that are installed by the COBRA desktop installer.
* `Version 5 analysis` (directory): contains all other input files and code. The following directories and files sit beneath this parent directory.
  * `a.finalData.01`, `a.finalData.02`, `a.finalData.03` (directories): these respectively correspond to the Full Buildout, No New Permits, and Operating Projects Only timeframe analysis scenario runs.
  * `b.finalData.01`, `b.finalData.02`, `b.finalData.03` (directories): these respectively correspond to the single year analysis for analysis years 2023, 2030, and 2050. (Only 2023 is included in the final report.)
  * `240610-FinalData-[AllProjects].xlsx` (data): contains input data corresponding to each LNG project evaluated in the report (AllProjects) or in a specific LNG buildout scenario (Operating, PermitMoratorium), including county, estimated start year, and permitted emissions volumes
  * `[a].finalData.[01]/prep.[a].finalData.[01].ipynb` (code): Within each experimental directory, there is a single "prep" file that creates the COBRA tool "control scenario" input data for multiple runs and writes an executable batch script for batch running all the associated runs. This prep file reads in LNG project data from 240610-FinalData-[AllProjects].xlsx and EPA-supplied baseline emissions, population, valuation, and incidence data from the COBRA (from desktop version) ... directory. The "a" experiment creates 1 control emissions file for each year in the timeframe 2023-2030, per buildout scenario and a batch file to run all of these years in succession. The "b" experiment creates 1 control emissions file for each project, for a single year, and a batch file to run all the projects in succession.
  * `[a].finalData.[01]/emissions.[a].finalData.[01].*.csv` (data): these are the control emissions files created by the `prep...` scripts
  * `[a].finalData.[01]/execute.[a].finalData.[01].bat` (code): these are the batch files used to run COBRA on the Windows environment created by the `prep` scripts
  * `[a].finalData.[01]/results.[a].finalData.[01].*.csv` (data): these are the results files output by COBRA in analysis step 2 described above. (Remember: COBRA is run on a separate Windows machine, then the results csvs are uploaded back into this directory)
  * `analysis.final.[a].step1.ipynb` (code): this Jupyter Notebook/Python script reads in and concatenates COBRA output data from multiple runs. The combined results are saved at [a].finalData.results/[a].finalData.01-03.combined_results.csv. (The combined results csv is gitignored from the repo because it is too large.) These files are uploaded to Tableau for spatial analysis, in addition to being used for analysis in the following scripts.
  * `analysis.final.[a].step2.ipynb` (code): this script analyzes the combined results (mainly pivot table like analysis) and outputs some of the tables/figures used in the report. Figure outputs are saved in the directory [a].finalData.results
  * `ACSDP5Y2022[...]` and `ACSST5Y2022[...]` (directory): directories containing census data extracts that are used for population-weighted exposure analysis
  * `analysis.final.pop_exposure.step[1].ipynb` (code): these Jupyter Notebook/Python scripts respectively calculate and visualization population weighted exposure to LNG terminal air pollution. The results are saved to pop_weighted_exposure.results
* COBRA_LNGHEALTH_Data.xlsx (data): additional project-level metadata read in for certain analyses

# Sources
* https://www.sierraclub.org/dirty-fuels/us-lng-export-tracker (data on LNG project location, status, and estimated start date)
* https://www.epa.gov/cobra/forms/download-cobra-and-sign-updates (EPA COBRA Tool desktop edition download)
* https://www.epa.gov/cobra/cobra-future-input-files (COBRA data for future years)
* Please see the Permit to Kill report for sources of permitted air emissions data