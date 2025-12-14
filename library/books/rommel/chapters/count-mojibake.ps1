$dir = "C:\Users\good4\Temple\library\books\rommel\chapters"
$patternFile = "C:\Users\good4\Temple\library\books\rommel\chapters\count-mojibake-patterns.txt"
$mojibakePatterns = Get-Content $patternFile -Encoding UTF8

foreach ($pattern in $mojibakePatterns) {
    $count = 0
    Get-ChildItem -Path $dir -Filter *.md | ForEach-Object {
        # echo $_.FullName
        $content = Get-Content $_.FullName -Raw
        $count += ([regex]::Matches($content, [regex]::Escape($pattern))).Count
    }
    Write-Output "${pattern}: $count"
}


