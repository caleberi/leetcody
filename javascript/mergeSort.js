function mergeSort(arr) {
  /*
  * take in a single unsorted array as a parameter
  * split the array into two halves
  */
  if (arr.length < 2) {
    return arr;
  }
  var middleIndex =  Math.floor(arr.length / 2);
  var firstHalf = arr.slice(0,middleIndex);
  var secondHalf = arr.slice(middleIndex);

  return merge(mergeSort(firstHalf),mergeSort(secondHalf));
}

function merge(array1,array2) {
  /*
  * takes in two sorted array as parameter
  * merge  those sorted arrays into one array
  * return one sorted array
  */
  var result =  [];
  while (array1.length && array2.length) {
    var minElem;
    if ( array1[0]< array2[0] ) {
      minElem = array1.shift()
    }else {
      minElem = array2.shift()
    }
    result.push(minElem)
  }
  if (array1.length) {
    result =  result.concat(array1)
  }else {
    result =  result.concat(array2)
  }
}
