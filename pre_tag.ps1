param (
    [string]$tag
)

if (-not $tag) {
    Write-Host "Usage: .\pre_tag.ps1 <tag>"
    exit 1
}

if ($tag -match "^v[0-9]+\.[0-9]+\.[0-9]+$") {
    $version = $tag.Substring(1)  # Remove the leading 'v'

    # Update the version in version.txt
    Set-Content -Path "version.txt" -Value $tag

    # Commit the change
    git add version.txt
    git commit -m "version.txt is updated to $tag"

    # Create the tag
    git tag $tag
} else {
    Write-Host "Tag name $tag does not follow the vx.y.z format."
    exit 1
}