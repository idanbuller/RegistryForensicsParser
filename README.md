# RegistryForensicsParser

The Windows Registry is one of the richest sources of digital evidence. You can find lots of extremely useful pieces of information during the examination of the Registry hives and keys. Computer configurations recently visited webpages and opened documents, connected USB devices, and many other artifacts can all be acquired through Windows Registry forensic examination.

The Registry has a tree structure. Each tree consists of keys, and each key may have one or more subkeys and values.

Learning about artifacts in Windows is crucial for digital forensics examiners, as Windows accounts for most of the traffic in the and examiners will most likely encounter Windows and will have to collect evidence from it in almost all cyber-crime cases.

### Analyzing Regedit's output with Python
### Tool's Options
```
What would you like to analyze?
    1 - Executable files running from with startup
    2 - DLL files running from with startup
    3 - Executable files running from with GUI startup
    4 - Keys Stats
    >>
```


## Structure
Structure
The Windows registry is an invaluable source of forensic artifacts for all examiners and analysts. The registry holds configurations for Windows and is a substitute for the .INI files in Windows 3.1. It is a binary, hierarchical database and some of its contents include configuration settings and data for the OS and for the different applications relying on it. The registry not only keeps records of OS and application settings but also monitors and records user-specific data to structure and enhance the user’s experience during interactions with the system. Most of the time users do not interact with the registry in a straightforward manner, but they interact indirectly with it via installation routines, applications, and programs, such as Microsoft Installer files. Nonetheless, system admins have the capability of interacting directly with the registry via regedit.exe (the registry editor) which comes with all varieties of Windows.

As we can see, the registry has a “folder-based, tree-like” structure, which is very typical for Microsoft Windows. If so, I am going to describe any key in this tree – 

### HKEY_CLASSES_ROOT  
HKCR contains file extensions association information, as well as a programmatic identifier, class ID, and interface data. HKCR contains all the necessary data for windows to know file-based action, such as viewing the content of a drive or opening certain file types.



The list of keys inside HKCR is very long, but Here are some of the many file extension association keys we can find under the HKEY_CLASSES_ROOT hive – 
* HKEY_CLASSES_ROOT\\.avi
* HKEY_CLASSES_ROOT\\.exe
* HKEY_CLASSES_ROOT\\.html
* HKEY_CLASSES_ROOT\\.pdf

Each of these registry keys stores information as to what Windows should do when you double-click or double-tap on a file with that extension. It may include the list of programs found in the "Open with" section when right-clicking/tapping a file, and the path to each application listed.

### HKEY_CURRENT_USER
HKCE contains configuration information for Windows and software specific to the currently logged-in user. User-level settings like the installed printers, desktop wallpaper, display settings, environment variables, keyboard layout, mapped network drives, etc.
Here are some of the registry keys we may find in the HKEY_CURRENT_USER hive – 
* HKEY_CURRENT_USER\Printers
* HKEY_CURRENT_USER\Software
* HKEY_CURRENT_USER\System
* HKEY_CURRENT_USER\Console
* HKEY_CURRENT_USER\Control Panel
The keys and values contained in it will differ from user to use even on the same computer.

### HKEY_LOCAL_MACHINE
HKLM contains all the configuration information for the software we have installed, as well as for the Windows operating system itself. In addition, HKLM also contains information about the hardware and device drivers.
Here are some of the registry keys we may find in the HKEY_LOCAL_MACHINE hive – 
* HKEY_LOCAL_MACHINE\DRIVERS
* HKEY_LOCAL_MACHINE\HARDWARE
* HKEY_LOCAL_MACHINE\SAM
* HKEY_LOCAL_MACHINE\SECURITY
* HKEY_LOCAL_MACHINE\SOFTWARE
* HKEY_LOCAL_MACHINE\SYSTEM

The HKEY_LOCAL_MACHINE\HARDWARE for example, contains plenty of information about the hardware, of course. Here we will find BIOS information such as version or vendor – 
Another interesting fact about this hive is that it does not really exist on the computer, it is only in charge of displaying the relevant data.

### HKEY_USERS
HKU contains user-specific configuration information for all currently active users on the computer. Each registry key located under the HKEY_USERS hive corresponds to a user on the system and is named with that user's security identifier or SID. The information is loaded when the user first logs on, We will find installed printers, environment variables, desktop background, etc.
The HKEY_CURRENT_USER hive acts as a kind of shortcut to the HKEY_USERS subkey corresponding to your SID.

### HKEY_CURRENT_CONFIG
HKCC doesn't store any information itself but instead acts as a pointer, or a shortcut, to a registry key that keeps the information about the hardware profile currently being used.


## Points Of Interest
As a forensics analyst, what should you pay attention to?
```
HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedMRU
```
This key maintains a list of recently opened or saved files, including those who opened or saved within a web browser but not including documents that are opened or saved via Microsoft Office programs.

 ```
HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedMRU
```
This key maintains a recently used program executable filename, and the folder path of a file to which the program has been used to open or save it.

```
HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs
```
This key reflects “recent files” we can find in the file-explorer.

```
HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU
```
The list of entries executed using the Start>Run command is stored in this key.

```
HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist
```
This key contains two GUID subkeys, and each subkey maintains a list of system objects such as program and control panel applets that a user has accessed.

```
HKCU\Software\Microsoft\Internet Explorer\TypedURLs
```
This key contains a listing of 25 recent URLs that is typed in the Internet Explorer.

```
HKLM\SYSTEM\MountedDevices
```
This key lists any volume that is mounted and assigned a drive letter, including USB storage devices and external DVD/CDROM drives.

```
HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2\CPCVolume
```
This key is a point of interest during a forensic analysis: the key records shares on remote systems such as C$, Temp$, etc.

```
HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
```
This key contains programs or components paths that are automatically run during system startup without requiring user interaction.

```
HKLM\SOFTWARE\Microsoft\Command Processor
```
This key contains a command that is automatically executed each time cmd.exe is running.

```
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon
```
This key contains windows logon activities often used by attackers to create persistence on the Operating system.


## Tools
### Regedit
Regedit or regedit.exe is a standard Windows executable file that opens the built-in registry editor. This allows you to view and edit keys and entries in the Windows registry database. The file is located in the Windows directory (typically C:\Windows), you can double-click it to launch the program. Alternatively, you can open the registry editor by entering “Regedit” in the search field of the start menu or in the “Run” dialog, which can be called up using the key combination [Windows] + [R].

With the help of Regedit, we may explore the hives describes above.

### RECmd + Timeline Explorer

RECmd is the command-line component of Registry Explorer that provides multiple capabilities to script and automate registry data collection.
Github project - 

(https://github.com/EricZimmerman/RECmd) 

Owner's website - 

(https://ericzimmerman.github.io/#!index.md) 


For the POC I choose to demonstrate RegistryASEPs.reb, a built-in source tool that holds an enormous collection of auto-start extensibility points (locations that can grant persistence to malicious code). The output will be in CSV format, providing different persistence locations that exist in the OS.

Bonus Tip:
The data better be filtered with the help of Timeline Explorer.

### RegRipper

Download link - https://sourceforge.net/projects/windowsir/files/latest/download

Once opened, we just must indicate, using the ‘Browse’ buttons, the registry file that we want to parse, and the name of the report we want to generate. We also select, by using the drop-down, the profile we want to load.


After pressing “Rip it”, the .log file and .txt file will be created. The ‘.log’ file contains information about the execution of the program and the ‘.txt’ file contains all the information that has been extracted from the Windows Registry file that we have parsed.


#### More tools will be described in the case studies.

## Case Studies
#### Case 1 – NTUSER.DAT
So, we want to analyze the NTUSER.DAT file to monitor the latest changes and to look at the behavior of Windows and other changes done in the memory.

We are going to use an FTK analyzer to obtain the protected files which we cannot analyze them directly. To do this, FTK analyzer suggest the option to obtain them – 








Now we can go to Users -> <username> -> NTUSER.DAT – 



With the help of registry viewer (rr.exe, https://accessdata.com/product-download/registry-viewer-2-0-0) we may take a closer look at what going on inside this file.

 


#### Case 2 – Recovering Deleted Entries

Windows is using transaction logs when performing writes to registry files. These transaction logs are used when registry hives cannot directly be written due to locking or corruption.

Transaction logs have one major problem, the oldest data in the log is overwritten by new data which makes it harder to perform forensics with the help of these logs. Although the new log format contains more recoverable information, turning a set of registry pages into useful data is quite tricky. It requires keeping track of all pages in the registry and determining what might have changed in a particular write.

For the POC, I created a registry value under the Run key that starts malware.exe when the user logs in to the system – 



Then, I overwrite it and deleted it from the system to withhold the forensics tools to recover the original data – 



However, in this case the data is still present in the transaction log and can be found in the NTUSER.DAT file – 



  

## Conclusion
When we are performing forensic analysis of past attacks, it might be particularly challenging. Advanced persistent threat actors will frequently utilize anti-forensic techniques to hide their tracks and make the jobs of incident responders more difficult. To provide our consultants with the best possible tools we revisited our existing registry forensic techniques and identified new ways to recover historical and deleted registry data.

Even so, registry hives may provide the analyst with many indications about malicious activity in the Windows operating system. With the help of the tools displayed we may catch the thief in his action.
