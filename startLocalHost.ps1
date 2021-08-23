Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
$PORT = 9000;

Set-Location Medieval
python -m http.server $PORT