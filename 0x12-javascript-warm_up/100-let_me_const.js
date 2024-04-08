#!/usr/bin/node
function modifyVar (varToModify) {
  varToModify.value = 333;
}
  
module.exports = modifyVar;
