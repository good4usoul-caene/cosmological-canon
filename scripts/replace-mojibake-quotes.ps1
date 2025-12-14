$dir = "C:\Users\good4\Temple\library\books\rommel\chapters"
Get-ChildItem -Path $dir -Filter *.md | ForEach-Object {
    (Get-Content $_.FullName -Raw) `
        -replace "â€™", "'" `
        -replace "â€œ", '"' `
        -replace "â€�", '"' | Set-Content $_.FullName
        Write-Output "Processing $($_.FullName)"
}