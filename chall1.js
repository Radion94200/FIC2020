var game = new Array(116,228,203,270,334,382,354,417,485,548,586,673,658,761,801,797,788,850,879,894,959,1059,1071,1140,1207,1226,1258,1305,1376,1385,1431,1515);

const u_u = "CTF.By.HexpressoCTF.By.Hexpresso";
var newflag = "";

for (i = 0; i < u_u.length; i++) {
    newflag += String.fromCharCode(game[i] - (u_u.charCodeAt(i) + i * 42));
    console.log( );
}

// Good j0b
console.log(newflag);
