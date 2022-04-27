var pokémon = [
    { "id": 1,   "name": "Bulbasaur",  "types": ["poison", "grass"] },
    { "id": 5,   "name": "Charmeleon", "types": ["fire"] },
    { "id": 9,   "name": "Blastoise",  "types": ["water"] },
    { "id": 12,  "name": "Butterfree", "types": ["bug", "flying"] },
    { "id": 16,  "name": "Pidgey",     "types": ["normal", "flying"] },
    { "id": 23,  "name": "Ekans",      "types": ["poison"] },
    { "id": 24,  "name": "Arbok",      "types": ["poison"] },
    { "id": 25,  "name": "Pikachu",    "types": ["electric"] },
    { "id": 37,  "name": "Vulpix",     "types": ["fire"] },
    { "id": 52,  "name": "Meowth",     "types": ["normal"] },
    { "id": 63,  "name": "Abra",       "types": ["psychic"] },
    { "id": 67,  "name": "Machamp",    "types": ["fighting"] },
    { "id": 72,  "name": "Tentacool",  "types": ["water", "poison"] },
    { "id": 74,  "name": "Geodude",    "types": ["rock", "ground"] },
    { "id": 87,  "name": "Dewgong",    "types": ["water", "ice"] },
    { "id": 98,  "name": "Krabby",     "types": ["water"] },
    { "id": 115, "name": "Kangaskhan", "types": ["normal"] },
    { "id": 122, "name": "Mr. Mime",   "types": ["psychic"] },
    { "id": 133, "name": "Eevee",      "types": ["normal"] },
    { "id": 144, "name": "Articuno",   "types": ["ice", "flying"] },
    { "id": 145, "name": "Zapdos",     "types": ["electric", "flying"] },
    { "id": 146, "name": "Moltres",    "types": ["fire", "flying"] },
    { "id": 148, "name": "Dragonair",  "types": ["dragon"] }
];

function pokenames(pokémon){
    for(var i =0; i<pokémon.length; i++){
        if(pokémon[i].id > 99){
            console.log(pokémon[i].name)
        }
    }
}

var monster = {
    id: 1,
    name: "Bulbasaur",
    types: ["poison", "grass"]
};

console.log(monster.name)
console.log(monster.types[1])

// Challenges - using the array of pokémon above and loops:

// console.log the pokémon objects whose id is evenly divisible by 3
function poke3(pokémon) {
    for(var i = 0; i <pokémon.length; i++) {
        if(pokémon[1].id % 3 == 0){
        console.log(pokémon[i])
        }
    }
}
poke3 (pokémon);
// console.log the pokémon objects that have more than one type
function moretype(pokémon) {
    for(var i = 0; i<pokémon.length; i++) {
        if(pokémon[1].types.length > 1){
        console.log(pokémon[i]);
        }
    }
}
function(moretype);
// console.log the names of the pokémon whose only type is "poison"
for(var i = 0; i<pokémon.length; i++) {
    if(pokémon[1].types.length < 2 && pokémon[1].types == "poisin"){
    console.log(pokémon[i]);
    }
}
// console.log the first type of all the pokémon whose second type is "flying"
function secondflying(pokémon) {
    for( var i=0; i<pokémon.length; i++) {
        if(pokémon[i].types[i] == "flying") {
            console.log(pokémon[i].types[0]);
        }
    }
}
// Bonus Challenge: console.log the reverse of the names of the pokémon whose only type is "poison"





// console.log the pokémon objects whose id is evenly divisible by 3

function pokethrees(){
    for (var i = 0; i < pokemon.length; i++){
        if(pokemon[i].id % 3 == 0){
            console.log(pokemon[i]);
        }
    }
}

pokethrees();

// console.log the pokémon objects that have more than one type

function poketypes(){
    for (var i = 0; i < pokemon.length; i++){
        if(pokemon[i].types.length > 1){
            console.log(pokemon[i]);
        }
    }
}

poketypes();

// console.log the names of the pokémon whose only type is "poison"

function pokepoison(){
    for (var i = 0; i < pokemon.length; i++){
        if(pokemon[i].types.length == 1 && pokemon[i].types == "poison"){
            console.log(pokemon[i].name);
        }
    }
}

pokepoison();

// console.log the first type of all the pokémon whose second type is "flying"

function pokeflying(){
    for (var i = 0; i < pokemon.length; i++){
        if(pokemon[i].types.length > 1 && pokemon[i].types[1] == "flying"){
            console.log(pokemon[i].types[0]);
        }
    }
}

pokeflying();

// Bonus Challenge: console.log the reverse of the names of the pokémon whose only type is "poison"

function pokepoisonRev(){
    for (var i = 0; i < pokemon.length; i++){
        if(pokemon[i].types.length == 1 && pokemon[i].types == "poison"){
            var reverseName = "";
            for (var x = pokemon[i].name.length - 1; x >= 0 ; x--){
                reverseName += pokemon[i].name[x];
            }
            console.log(reverseName);
        }
    }
}

pokepoisonRev();