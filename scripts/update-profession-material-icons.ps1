param(
    [string]$OutputDirectory = (Join-Path $PSScriptRoot '..\src\.vuepress\public\assets\img\materials')
)

$ErrorActionPreference = 'Stop'

# The official wiki renders material icons from a 16-column, 32 px grid.
# Position IDs come from Template:ProfessionIcon/pos.
$iconPositions = [ordered]@{
    '105' = [ordered]@{ ingot = 47; gem = 48; wood = 95; paper = 96; string = 143; grain = 144; oil = 191; meat = 192 }
    '110' = [ordered]@{ ingot = 50; gem = 51; wood = 98; paper = 99; string = 146; grain = 147; oil = 194; meat = 195 }
    '115' = [ordered]@{ ingot = 53; gem = 54; wood = 101; paper = 102; string = 149; grain = 150; oil = 197; meat = 198 }
}

$apiUrl = 'https://wynncraft.wiki.gg/api.php?action=query&format=json&titles=File%3AProfessionIcon.png&prop=imageinfo&iiprop=url'
$metadata = Invoke-RestMethod -Uri $apiUrl
$page = $metadata.query.pages.PSObject.Properties.Value | Select-Object -First 1
$spriteUrl = $page.imageinfo[0].url

$temporaryFile = Join-Path ([System.IO.Path]::GetTempPath()) ("wynn-profession-icons-{0}.png" -f [guid]::NewGuid())
try {
    Invoke-WebRequest -UseBasicParsing -Uri $spriteUrl -OutFile $temporaryFile

    Add-Type -AssemblyName System.Drawing
    $sprite = [System.Drawing.Bitmap]::FromFile($temporaryFile)
    try {
        if ($sprite.Width -ne 512 -or $sprite.Height -ne 512) {
            throw "Unexpected ProfessionIcon sprite size: $($sprite.Width)x$($sprite.Height)"
        }

        $resolvedOutput = [System.IO.Path]::GetFullPath($OutputDirectory)
        [System.IO.Directory]::CreateDirectory($resolvedOutput) | Out-Null

        foreach ($tier in $iconPositions.Keys) {
            foreach ($material in $iconPositions[$tier].Keys) {
                $position = $iconPositions[$tier][$material] - 1
                $sourceRectangle = [System.Drawing.Rectangle]::new(($position % 16) * 32, [math]::Floor($position / 16) * 32, 32, 32)
                $icon = $sprite.Clone($sourceRectangle, $sprite.PixelFormat)
                try {
                    $outputPath = Join-Path $resolvedOutput ("{0}_{1}.png" -f $material, $tier)
                    $icon.Save($outputPath, [System.Drawing.Imaging.ImageFormat]::Png)
                    Write-Host "Wrote $outputPath"
                }
                finally {
                    $icon.Dispose()
                }
            }
        }
    }
    finally {
        $sprite.Dispose()
    }
}
finally {
    Remove-Item -LiteralPath $temporaryFile -Force -ErrorAction SilentlyContinue
}
