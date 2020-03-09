/**
 * @param {string} address
 * @return {string}
 */
const defangIPaddr = (address) => {
  const defangled = Array.from(address).map(char => {
    if (char === '.') return '[.]'
    else return char;
  })
  return defangled.join('');
};

console.log(defangIPaddr("1.1.1.1"));
