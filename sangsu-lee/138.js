/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */
/**
 * @param {Node} head
 * @return {Node}
 */
const copyRandomList = head => {
  const [nodes, dists] = [[], []];
  let node = head;
  if (node === null) return null;
  if (node.next === null) {
    const newNode = new Node(head.val, null, null);
    if (node.random !== null) return newNode.random = newNode;
    return newNode;
  }
  while (true) {
    nodes.push(node);
    if (node.next !== null) {
        node = node.next;
    } else break;
  }
  for (const node of nodes) {
    let curNode = node.random, dist = 1;
    if (curNode === null) {
        dists.push(null); continue;
    }
    while (curNode.next !== null) {
      dist += 1;
      curNode = curNode.next;
    }
    dists.push(dist);
  }
  const randomIxs = dists.map(x => x === null ? null : nodes.length - x)
  const newNodes = nodes.map(node => new Node(node.val, null, null))
  for (let i = 0; i < newNodes.length; i++) {
    const newNodeRandom = randomIxs[i] === null ? null : newNodes[randomIxs[i]];
    newNodes[i].random = newNodeRandom;
    if (i === newNodes.length - 1) break;
    newNodes[i].next = newNodes[i+1];
  }
  return newNodes[0];
};
