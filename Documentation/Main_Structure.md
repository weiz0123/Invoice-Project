# Main_Structure
![Main Structure](https://github.com/weiz0123/Invoice-Project/assets/76544381/1e3413a5-6270-463e-9cb9-dda0d877f647)
## User Level Management (ULM)
  1. User Level Management gets *data* from **Data Access**, then pass the *data* to GUI for Display
  2. Notice: this is the seperation between "Font-End" (display) and "Back-end" (data reads and writes)
_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
* "Back-End" Classes
## Example:
![Main Structure Example](https://github.com/weiz0123/Invoice-Project/assets/76544381/63aad4b1-554c-49a9-8cc4-a941b63f92a5)

## Data Access
  1. Data Access organize and format *raw data* such as company name, company folder path, image name, image path etc.
  2. The *raw data* are aqcuired from **CLM**, then it is formatted for display

## Company Level Management (CLM)
  1. Company Level Management serves the purpose to managem folder for each company
  2. When a *new company* folder is added to the system, a **CLM** will be created.
  3. All the files and directories in the *new company* will be managed by that **CLM**
     
## Data Access


## Process Access


## Image Level Management (ILM)  
  1. For each image, **ILM** will be created to keep track of the image information including image name, image path, cv image etc.

## Secure Data Management (SDM); including Data and Position



_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
## Example:

## Operation Access

## User Interface Management Main & Container
