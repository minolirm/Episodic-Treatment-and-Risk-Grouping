
#### Create a virtual environment and install the packages in requirements.txt file

#### Follow the below steps for DDIG Process

1. Input following three csv files into ddi_input folder
    I) ClaimsToGroup file (csv)
   II) EnrollmentToGroup file (csv)
   III) MembersToGroup file (csv)
   
2. Input following three text files in the directory; "D:\ETG\output"
   
   I) ETGClaimsOutput file (txt)
   
   II) ETGConfinement file (txt)
   
   III) EtgSummary file (txt)
   
3. Run DDIG.py file
   
4. Following three Output file(s) and ControlReport will be saved in the ddi_output folder

   I) DDIGClaimOutput file (csv)
   
   II) DDIGConfinementOutput file (csv)
   
   III) DDIGSummaryOutput file (csv)
   
   IV) ControlReport file (text)

or 
#### For creating executable file, follow the below steps

1. In the terminal, run the below command.
   
   pyinstaller --onefile DDIG.py
   
2. After executable file creation process is successfully completed, in the DDIG project folder, 
   following output will be saved.
   - dist folder ---> Inside the dist folder, DDIG.exe file is created
   - build folder
   - DDIG.spec
   
3. Run the DDIG.exe file in the dist folder, 
   Following three Output file(s) and ControlReport will be saved in the ddi_output folder

   I) DDIGClaimOutput file (csv)
   
   II) DDIGConfinementOutput file (csv)
   
   III) DDIGSummaryOutput file (csv)
   
   IV) ControlReport file (text)
