$dir = "C:\Users\good4\Temple\library\books\rommel\chapters"
Get-ChildItem -Path $dir -Filter *.md | ForEach-Object {
    $file = $_.FullName
    $lines = Get-Content $file -Encoding Byte
    $text = [System.Text.Encoding]::Default.GetString($lines)
    $newText = $text -replace "â€™", "'"
    if ($text -ne $newText) {
        Write-Output "Updated $file"
        [System.IO.File]::WriteAllText($file, $newText, [System.Text.Encoding]::UTF8)
    }
}