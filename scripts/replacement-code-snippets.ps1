$dir = "C:\Users\good4\Temple\library\books\rommel\chapters"
Get-ChildItem -Path $dir -Filter *.md | ForEach-Object {
    $content = Get-Content $_.FullName -Raw -Encoding Default
    $newContent = $content -replace "â€™", "'" -replace "â€œ", '"' -replace "â€�", '"'
    if ($content -ne $newContent) {
        Write-Output "Updated $($_.FullName)"
        $newContent | Set-Content $_.FullName -Encoding UTF8
    } else {
        # Write-Output "No changes in $($_.FullName)"
    }
}

The-Most-Holy-Bible-text-files%5C

$dir = "C:\Users\good4\Temple\library\books\rommel\chapters"
Get-ChildItem -Path $dir -Filter *.md | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    $newContent = $content -replace "The-Most-Holy-Bible-text-files%5C", "The-Most-Holy-Bible-text-files\" #-replace "Nevertheless-I", "Nevertheless I"
    if ($content -ne $newContent) {
        Write-Output "Updated $($_.FullName)"
        $newContent | Set-Content $_.FullName -Encoding UTF8
    } else {
        # Write-Output "No changes in $($_.FullName)"
    }
}

Get-ChildItem -Path "C:\Users\good4\Temple\library\books\rommel\chapters" -Filter *.md | 
  Select-String "â€™|â€œ|â€�" | 
  Select-Object Path, LineNumber, Line

Get-ChildItem -Path "C:\Users\good4\Temple\library\books\rommel\chapters" -Filter *.md | 
  Select-String "nevertheless" | 
  Select-Object Path, LineNumber, Line


  $dir = "C:\Users\good4\Temple\library\books\rommel\chapters"
Get-ChildItem -Path $dir -Filter *.md | ForEach-Object {
    $content = Get-Content $_.FullName -Raw -Encoding Latin1
    $newContent = $content -replace "â€™", "'" -replace "â€œ", '"' -replace "â€�", '"'
    if ($content -ne $newContent) {
        Write-Output "Updated $($_.FullName)"
        $newContent | Set-Content $_.FullName -Encoding UTF8
    } else {
       # Write-Output "No changes in $($_.FullName)"
    }
}


$dir = "C:\Users\good4\Temple\library\books\rommel\chapters"
Get-ChildItem -Path $dir -Filter *.md | ForEach-Object {
    $file = $_.FullName
    $lines = Get-Content $file -Encoding Byte
    $text = [System.Text.Encoding]::Default.GetString($lines)
    $newText = $text -replace "â€™", "'" -replace "â€œ", '"' -replace "â€�", '"'
    if ($text -ne $newText) {
        Write-Output "Updated $file"
        [System.IO.File]::WriteAllText($file, $newText, [System.Text.Encoding]::UTF8)
    } else {
        # Write-Output "No changes in $file"
    }
}