class Anagram{
    constructor() {
        const Number_Letters =  26;
    }

    getCharacterCount(string){
        var characterCount = this.Number_Letters;
        for (let i = 0; i < string.length; i++) {
            var c  = string.charAt(i);
            
        }
    }

    numberNeeded(firstString , secondString){
        var count1 = getCharacterCount(firstString);
        var count2 = getCharacterCount(secondString);
        return  getDelta(count1,count2);
    }
}