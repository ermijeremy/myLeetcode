/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let sum = 0;
    for(i=0;i<s.length;i++){
        let current = s.charAt(i);
        let next = s.charAt(i+1);
        switch(current){
            case "I":
                sum +=1;
                break;
            case "V":
                sum +=5;
                break;
            case "X":
                sum +=10;
                break;
            case "L":
                sum +=50;
                break;
            case "C":
                sum +=100;
                break;
            case "D":
                sum +=500;
                break;
            case "M":
                sum +=1000;
                break;
        }
        if((current == "I" && next == "V") || (current == "I" && next == "X")){
            sum -= 2;
        }
        if((current == "X" && next == "L") || (current == "X" && next == "C")){
            sum -= 20;
        }
        if((current == "C" && next == "D") || (current == "C" && next == "M")){
            sum -= 200;
        }
    }
    return sum;
};