# -Hacking-Digital-Scale
A collection of scripts to read data from a Kern PCB1000-1 digital scale using Excel, with a little help from *Python*.

For a project we wanted to read in weight data from a digital scale in Excel. In this case a [Kern PCB1000-1](https://www.kern-sohn.com/shop/en/laboratory-balances/precision-balances/PCB/). So using a Macro in Excel and Python we could do this, please find the how-to here.

First download the scripts and put them somewhere useful and where you remember. Then open the script **ExcelMacro.txt**. Now change lines eight and nine to the correct paths (*PATH*).

    PythonExePath  = """C:\PATH\python"""
    PythonScript = "C:\PATH\Getweight.py" # the file downloaded in this repository


Now open Microsoft Excel and enable Macros and create a Macro. In the script copy and paste the **ExcelMacro.txt** in the script. Then create an action button in Excel linked to the Macro. *Voila*

Please be aware where the data is placed. You may want to change which excel cell is written.

I must admit, I did this a few months ago, so if something is wrong let me know.

The main trick here is using the *Python* Serial library. It writes "DSR" to the scale which asks for new data and returns it. This I believe is general, meaning the script should work with any digital balance that uses a serial communication. I haven't tested this though.
