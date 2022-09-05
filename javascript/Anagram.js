class Anagram{
    constructor() {
        const Number_Letters =  26;
    }

    getCharacterCount(string){
        var characterCount = this.Number_Letters;
        for (let i = 0; i < string.length; i++) { // O(N) | O(1) "racecar" , "kim", "a"
            var c  = string.charAt(i);
            
        }
    }

    numberNeeded(firstString , secondString){
        var count1 = getCharacterCount(firstString); // O(N)
        var count2 = getCharacterCount(secondString); // O(N)
        // O(N)+O(N) =  O(N)
        return  getDelta(count1,count2);
    }
}