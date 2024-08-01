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
# Commit the change
git add --all
git commit -m "VERSION is updated to $newVersion"

Write-Host "=============================== Create the new tag"
# Create the new tag
git tag $newVersion
git tag

# Push the changes and the new tag to the server
Write-Host "=============================== Push to github"
git push --tags github master
Write-Host "=============================== Push to gitlab"
git push --tags gitlab master
Write-Host "=============================== Push to origin"
git push --tags origin master

Write-Host "=============================== Version updated to $newVersion and pushed to the server."