; Inno Setup Script for BodyBuilderPro
[Setup]
AppName=BodyBuilderPro
AppVersion=1.0.0
DefaultDirName={pf}\\BodyBuilderPro
DefaultGroupName=BodyBuilderPro
Uninstallable=yes
DisableDirPage=no
OutputDir=.
OutputBaseFilename=BodyBuilderPro_Setup
SetupIconFile=..

[Languages]
Name: "farsi"; MessagesFile: "compiler:Languages\\Farsi.isl"

[Files]
Source: "..\\dist\\BodyBuilderPro\\BodyBuilderPro.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\\dist\\BodyBuilderPro\\app\\*"; DestDir: "{app}\\app"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\\BodyBuilderPro"; Filename: "{app}\\BodyBuilderPro.exe"
Name: "{commondesktop}\\BodyBuilderPro"; Filename: "{app}\\BodyBuilderPro.exe"

[Run]
Filename: "{app}\\BodyBuilderPro.exe"; Description: "اجرای BodyBuilderPro"; Flags: nowait postinstall skipifsilent
