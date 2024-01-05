#!/usr/local/bin/python3

import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

print("Content-Type: text/html; charset=UTF-8\n\n")


html='''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="description" content="">
<meta name="keywords" content="">
<link rel="shortcut icon" type="image/x-icon" href="favicon.ico">
<title>title_test</title>
<style>
body{
    background-color:aquamarine;
    }
</style>
</head>
<body>
<h1>display</h1>

test_py

<script>
</script>
</body>
</html>
'''

print(html)
