/**
 * @param {string[]} list1
 * @param {string[]} list2
 * @return {string[]}
 */
let findRestaurant = function(list1, list2) {
    let min_ix_sum = 99999999;
    let min_ix_string = [];
    
    for (let i = 0; i < list1.length; i++) {
        for (let j = 0; j < list2.length; j++) {
            if (list1[i] === list2[j] && min_ix_sum >= i + j) {
                if (min_ix_sum > i + j) {
                    min_ix_string = [list1[i]];
                } else {
                    min_ix_string.push(list1[i])
                }
                min_ix_sum = i + j;
            }
        }
    }
    return min_ix_string;


}
