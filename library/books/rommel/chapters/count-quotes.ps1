$dir = "C:\Users\good4\Temple\library\books\rommel\chapters"
$patterns = @{
    "Left Single Quote (U+2018)" = ([char]0x2018)
    "Right Single Quote (U+2019)" = ([char]0x2019)
    "Left Double Quote (U+201C)" = ([char]0x201C)
    "Right Double Quote (U+201D)" = ([char]0x201D)
}
$totals = @{}
foreach ($key in $patterns.Keys) { $totals[$key] = 0 }

# Count Unicode curly quotes
Get-ChildItem -Path $dir -Filter *.md | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    foreach ($key in $patterns.Keys) {
        $count = ($content.ToCharArray() | Where-Object { $_ -eq $patterns[$key] }).Count
        $totals[$key] += $count
    }
}

# Now count mojibake patterns separately
$mojibakePatterns = @(
    @{ Name = "Mojibake Right Single (â€™)"; Pattern = "â€™" },
    @{ Name = "Mojibake Left Double (â€œ)"; Pattern = "â€œ" },
    @{ Name = "Mojibake Right Double (â€�)"; Pattern = "â€�" }
)
foreach ($moji in $mojibakePatterns) {
    $mojiCount = 0
    Get-ChildItem -Path $dir -Filter *.md | ForEach-Object {
        $content = Get-Content $_.FullName -Raw
        $mojiCount += ([regex]::Matches($content, [regex]::Escape($moji.Pattern))).Count
    }
    Write-Output "$($moji.Name): $mojiCount"
}

# Output Unicode curly quote counts
$totals.GetEnumerator() | ForEach-Object { Write-Output "$($_.Key): $($_.Value)" }