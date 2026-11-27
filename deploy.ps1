# PowerShell deployment helper for GitHub Pages
param (
    [string]$RepoUrl
)

if (-not $RepoUrl) {
    Write-Host "========================================================" -ForegroundColor Cyan
    Write-Host "PSUT 11102 - GitHub Pages Quick Deployment Helper" -ForegroundColor Yellow
    Write-Host "========================================================" -ForegroundColor Cyan
    Write-Host "1. Create a new empty repository at: https://github.com/new"
    Write-Host "2. Copy its HTTPS URL (e.g. https://github.com/username/my-repo.git)"
    Write-Host ""
    $RepoUrl = Read-Host "Paste your GitHub Repository URL here"
}

if ($RepoUrl) {
    Write-Host "`nAdding remote origin..." -ForegroundColor Cyan
    git remote remove origin 2>$null
    git remote add origin $RepoUrl
    
    Write-Host "Pushing 'main' branch to GitHub..." -ForegroundColor Cyan
    git push -u origin main
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`n========================================================" -ForegroundColor Green
        Write-Host "SUCCESS! Code pushed to GitHub." -ForegroundColor Green
        Write-Host "To enable GitHub Pages:" -ForegroundColor Yellow
        Write-Host "1. Go to your repository on GitHub."
        Write-Host "2. Click 'Settings' -> 'Pages' (in the left sidebar)."
        Write-Host "3. Under 'Build and deployment' -> 'Branch', choose 'main' and '/ (root)'."
        Write-Host "4. Click 'Save'."
        Write-Host "Your live website will be ready in ~1 minute!" -ForegroundColor Green
        Write-Host "========================================================" -ForegroundColor Green
    } else {
        Write-Host "`nPush failed. Please check your GitHub permissions or credentials." -ForegroundColor Red
    }
}
