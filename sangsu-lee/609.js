/**
 * @param {string[]} paths
 * @return {string[][]}
 */
const path = require('path');

const findDuplicate = (paths) => {
  const contentObj = {};
  for (let _path of paths) {
    const [dir, ...rest ] = _path.split(' ')
    for (let name of rest) {
      let [fileName, content] = name.split('(');
      content = content.slice(0, -1);

      if (content in contentObj) {
        contentObj[content].push(path.join(dir, fileName));
      } else {
        contentObj[content] = [path.join(dir, fileName)];
      }
    }
  }
  const lol = Object.values(contentObj);
  return lol.filter(l => l.length > 1)
};


const ans = findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]);
console.log('ans: ', ans);

