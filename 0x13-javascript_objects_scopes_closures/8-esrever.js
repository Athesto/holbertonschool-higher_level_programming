#!/usr/bin/node

exports.esrever = function (list) {
  const a = [];

  for (let item = list.length - 1; item >= 0; item--) {
    a.push(list[item]);
  }
  return (a);
};
