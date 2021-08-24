var playerName;


document.getElementById("nameInputButton").addEventListener("click", function(){
    playerName = document.getElementById("nameInput").value;
    document.getElementById("Name").innerHTML = playerName;
    document.getElementById("overlay").remove();
});