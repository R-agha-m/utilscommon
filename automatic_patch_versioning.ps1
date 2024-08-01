# Path to the VERSION file
$versionFilePath = "VERSION"

Write-Host "=============================== Check if VERSION exists"
# Check if VERSION exists
if (-not (Test-Path $versionFilePath))
{
    Write-Host "Error: VERSION file not found."
    $currentVersion = "v0.0.0"
    Write-Host "Current version is: $currentVersion"
}
else
{
    # Read the current version from VERSION
    $currentVersion = Get-Content -Path $versionFilePath
    Write-Host "Current version is: $currentVersion"
}

# Ensure the version follows the vx.y.z format
if ($currentVersion -notmatch "^v[0-9]+\.[0-9]+\.[0-9]+$")
{
    Write-Host "Error: VERSION does not contain a valid version (vx.y.z format)."
    exit 1
}

Write-Host "=============================== Increment patch"
# Increment the last part of the version
$parts = $currentVersion.Substring(1).Split('.')
$major = [int]$parts[0]
$minor = [int]$parts[1]
$patch = [int]$parts[2]

# Increment the patch version
$patch += 1

# Form the new version
$newVersion = "v{0}.{1}.{2}" -f $major, $minor, $patch
Write-Host "New version is: $newVersion"

# Write the new version to VERSION
Set-Content -Path $versionFilePath -Value $newVersion

Write-Host "=============================== Commit the change"
try
{
    git add --all
    git commit -m "VERSION is updated to $newVersion"
}
catch
{
    Write-Host "Error: Failed to commit changes."
    exit 1
}

# Define remotes and their URLs
$remotes = @{
    "github" = "git@github.com:hacknitive/utilscommon.git"
    "gitlab" = "git@gitlab.com:hacknitive/utilscommon.git"
}

# Ensure the remotes are added
foreach ($remote in $remotes.Keys)
{
    Write-Host "=============================== Check if $remote remote exists"
    $remoteExists = git remote | Select-String -Pattern "^$remote$"
    if (-not $remoteExists)
    {
        Write-Host "$remote remote not found. Adding $remote..."
        git remote add $remote $remotes[$remote]
        if ($LASTEXITCODE -ne 0)
        {
            Write-Host "Error: Failed to add $remote remote."
            exit 1
        }
    }
    else
    {
        Write-Host "$remote remote already exists."
    }
}

Write-Host "=============================== Create the new tag"
try
{
    git tag $newVersion
    git tag
}
catch
{
    Write-Host "Error: Failed to create or list tags."
    exit 1
}

# Push the changes and the new tag to the remotes
foreach ($remote in $remotes.Keys)
{
    Write-Host "=============================== Push to $remote"
    try
    {
        git push --tags $remote master
    }
    catch
    {
        Write-Host "Error: Failed to push to $remote."
        exit 1
    }
}

Write-Host "=============================== Version updated to $newVersion."