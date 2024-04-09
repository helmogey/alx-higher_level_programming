#!/usr/bin/node
const occurrencesByUserId = require('./101-data');

const usersByOccurrence = {};

for (const occurrenceCount in occurrencesByUserId) {
  const userIds = occurrencesByUserId[occurrenceCount];

  if (!usersByOccurrence[occurrenceCount]) {
    usersByOccurrence[occurrenceCount] = [];
  }
  usersByOccurrence[occurrenceCount].push(...userIds);
}

console.log("Users by Occurrence:");
console.log(usersByOccurrence);
