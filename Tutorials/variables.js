// Doing it both with var in the beginning and without is perfectly valid.
var variableName = undefined;

variableName2 = 100;

var placeholderVariable;

if(true){
    // let variable makes a local variable. Still able to not include the 'let' keyword.
    let localVariable = 5
    let placeholderVariable = 5
    if(true){
        console.log(placeholderVariable)
    }
}
console.log(placeholderVariable)

array1 = []
array2 = [1,2,3,4]
array3 = [5,6,7]
array4 = new Array()
array5 = new Array(1,2,3,4,5) //array5 is = [1,2,3,4,5]

array2.push("Hello World!")
array2.unshift(10) // Adds 10 to the front of the array
array2[array2.length] = "Hello World V2!"
array2.pop() // Removes the last element from array
array2.shift() // Removes first element from array
delete array2[1]; // Will replace the element with undefined
array2.splice(2, 0, "Hello", "World", 1, 10)
array2.splice(2, 1)
var array2Copy = array2.slice(0)
// If you try to add a new item to an existing array with a higher index than the existing array has, it will create a 'Undefined' hole
array2[10] = 52 // [1,2,3,4,"Hello World!", "Hellow World V2!", Undefined, Undefined, Undefined, Undefined, 52]
array2.sort()
array2[0] = "Hello!"


for(num in array3){
    array2.push(num)
}





var compareArray = ["Tommy", 20, "Oregon", "Ohio"] // Arrays use Numbered indexes
var compareObject = {"Name": "Tommy",
                     "Age": 20,
                     "City": "Oregon",
                     "State": "Ohio"
                    } // Objects use Named indexes

console.log(compareArray[0])
console.log(compareObject["Name"])




// Mining, Woodcutting, Fishing, Runecrafting ...
skillLevel = [0,0,0,0]

if(minedOre == true){
    skillLevel[0] += 1
}
if(cutTree == true){
    skillLevel[1] += 1
}

skillLevel = {
    "Mining" : 0,
    "Woodcutting" : 0,
    "Fishing" : 0,
    "Runecrafting" : 0
}

if(minedOre == true){
    skillLevel["Mining"] += 1
}
if(cutTree == true){
    skillLevel["Woodcutting"] += 1
}



peopleInToledo = [
    {"Name": "Tommy", "Age": 20, "City": "Oregon", "State": "Ohio"},
    {"Name": "Nathaniel", "Age": 25, "City": "Oregon", "State": "Ohio"},
]


const skills = ["Mining", "Woodcutting", "Fishing"]
const maxLevel = 100

a = 5 + 2 // Add
b = 5 - 2 // Subtract
c = 5 * 2 // Multiply
d = 6 / 2 // Divide
e = 5 % 2 // Remainder

f = 10
//++f; // 11
//f++; // 12
console.log(f++) // Prints 10
// f = 11
console.log(++f) // Prints 12
// f = 12

g = 10
--g; // 9
g--; // 8

h = 5 ** 2  //Exponent
var day;
switch (new Date().getDay()) {
    case 0:
        day = "Sunday";
        break;
    case 1:
        day = "Monday";
        break;
    case 2:
        day = "Tuesday";
        break;
    case 3:
        day = "Wednesday";
        break;
    case 4:
        day = "Thursday";
        break;
    case 5:
        day = "Friday";
        break;
    case 6:
        day = "Saturday";
}